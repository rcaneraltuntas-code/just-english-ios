-- Just English: ilk şema.
-- Öğrenciler Apple ile giriş yapar (auth.users). Öğretmenler profiles.role = 'teacher' ile işaretlenir.

-- Profiller ------------------------------------------------------------------

create table public.profiles (
    id uuid primary key references auth.users (id) on delete cascade,
    role text not null default 'student' check (role in ('student', 'teacher', 'admin')),
    display_name text not null default '',
    created_at timestamptz not null default now()
);

alter table public.profiles enable row level security;

create policy "profil: kendi satırını okur" on public.profiles
    for select using (auth.uid() = id);

-- Öğrenci yalnızca adını değiştirebilir; rol yalnızca yöneticiler tarafından (SQL editörü) atanır.
create policy "profil: kendi adını günceller" on public.profiles
    for update using (auth.uid() = id) with check (auth.uid() = id);

revoke update on public.profiles from anon, authenticated;
grant update (display_name) on public.profiles to authenticated;

create function public.handle_new_user() returns trigger
language plpgsql security definer set search_path = public as $$
begin
    insert into public.profiles (id) values (new.id) on conflict do nothing;
    return new;
end;
$$;

create trigger on_auth_user_created
    after insert on auth.users
    for each row execute function public.handle_new_user();

create function public.is_teacher() returns boolean
language sql stable security definer set search_path = public as $$
    select exists (select 1 from public.profiles where id = auth.uid() and role in ('teacher', 'admin'));
$$;

-- Öğrenci ilerlemesi -----------------------------------------------------------
-- Uygulamadaki UserState tek bir JSON olarak saklanır; birleştirme istemcide yapılır.
-- current_level ve total_xp, öğretmen raporları ve ligler için ayrıca tutulur.

create table public.user_state (
    user_id uuid primary key references auth.users (id) on delete cascade,
    state jsonb not null,
    current_level text not null check (current_level in ('A1', 'A2', 'B1', 'B2', 'C1', 'C2')),
    total_xp integer not null default 0,
    display_name text not null default '',
    updated_at timestamptz not null default now()
);

alter table public.user_state enable row level security;

create policy "ilerleme: kendi satırı" on public.user_state
    for all using (auth.uid() = user_id) with check (auth.uid() = user_id);

create function public.touch_updated_at() returns trigger
language plpgsql as $$
begin
    new.updated_at = now();
    return new;
end;
$$;

create trigger user_state_touch before update on public.user_state
    for each row execute function public.touch_updated_at();

-- Canlı grup dersleri ----------------------------------------------------------

create table public.live_sessions (
    id uuid primary key default gen_random_uuid(),
    unit_id text not null,                       -- ör. 'b1-u03'
    level text not null check (level in ('A1', 'A2', 'B1', 'B2', 'C1', 'C2')),
    title text not null,
    starts_at timestamptz not null,
    duration_minutes integer not null default 45 check (duration_minutes between 15 and 180),
    teacher_id uuid not null references auth.users (id) default auth.uid(),
    teacher_name text not null,
    join_url text,                               -- toplantı bağlantısı; yalnızca kayıtlı öğrenciler görür
    capacity integer check (capacity > 0),
    cancelled boolean not null default false,
    created_at timestamptz not null default now()
);

create index live_sessions_starts_at on public.live_sessions (starts_at) where not cancelled;

alter table public.live_sessions enable row level security;

create policy "canlı ders: öğretmen yönetir" on public.live_sessions
    for all using (public.is_teacher() and teacher_id = auth.uid())
    with check (public.is_teacher() and teacher_id = auth.uid());

create table public.live_bookings (
    session_id uuid not null references public.live_sessions (id) on delete cascade,
    user_id uuid not null references auth.users (id) on delete cascade,
    attended boolean not null default false,
    created_at timestamptz not null default now(),
    primary key (session_id, user_id)
);

alter table public.live_bookings enable row level security;

create policy "kayıt: kendi kayıtlarını görür" on public.live_bookings
    for select using (auth.uid() = user_id);

create policy "kayıt: öğretmen kendi dersinin kayıtlarını görür" on public.live_bookings
    for select using (exists (
        select 1 from public.live_sessions s where s.id = session_id and s.teacher_id = auth.uid()
    ));

-- Herkese açık ders listesi: katılım bağlantısı yalnızca kayıtlı öğrenciye ve dersin öğretmenine gösterilir.
create view public.live_sessions_public with (security_invoker = false) as
select
    s.id, s.unit_id, s.level, s.title, s.starts_at, s.duration_minutes, s.teacher_name, s.capacity,
    (select count(*) from public.live_bookings b where b.session_id = s.id)::integer as booked,
    case
        when s.teacher_id = auth.uid()
          or exists (select 1 from public.live_bookings b where b.session_id = s.id and b.user_id = auth.uid())
        then s.join_url
    end as join_url
from public.live_sessions s
where not s.cancelled;

grant select on public.live_sessions_public to anon, authenticated;

create function public.book_live_session(p_session uuid) returns void
language plpgsql security definer set search_path = public as $$
declare
    v_capacity integer;
    v_booked integer;
begin
    if auth.uid() is null then
        raise exception 'giriş gerekli';
    end if;
    select capacity into v_capacity from live_sessions
        where id = p_session and not cancelled and starts_at > now() - interval '10 minutes'
        for update;
    if not found then
        raise exception 'ders bulunamadı';
    end if;
    select count(*) into v_booked from live_bookings where session_id = p_session;
    if v_capacity is not null and v_booked >= v_capacity then
        raise exception 'ders dolu';
    end if;
    insert into live_bookings (session_id, user_id) values (p_session, auth.uid()) on conflict do nothing;
end;
$$;

create function public.cancel_live_booking(p_session uuid) returns void
language sql security definer set search_path = public as $$
    delete from live_bookings where session_id = p_session and user_id = auth.uid();
$$;

create function public.mark_live_attended(p_session uuid) returns void
language sql security definer set search_path = public as $$
    update live_bookings set attended = true where session_id = p_session and user_id = auth.uid();
$$;

-- Hesap silme (App Store 5.1.1(v)): kullanıcı kendi hesabını ve tüm verisini siler.
create function public.delete_my_account() returns void
language plpgsql security definer set search_path = public, auth as $$
begin
    if auth.uid() is null then
        raise exception 'giriş gerekli';
    end if;
    delete from auth.users where id = auth.uid();
end;
$$;

revoke execute on function public.book_live_session(uuid), public.cancel_live_booking(uuid),
    public.mark_live_attended(uuid), public.delete_my_account() from anon, public;
grant execute on function public.book_live_session(uuid), public.cancel_live_booking(uuid),
    public.mark_live_attended(uuid), public.delete_my_account() to authenticated;

-- Haftalık XP ligleri.
-- Her hafta (pazartesi, İstanbul saati) öğrenciler kendi kademelerinde 30 kişilik gruplara yerleşir.
-- Hafta sonunda grubun ilk 7'si bir üst kademeye çıkar, son 5'i bir alta iner (10 kişiden küçük gruplarda kimse inmez).
-- Kademeler: 0 Bronz, 1 Gümüş, 2 Altın, 3 Safir, 4 Yakut, 5 Elmas.

create table public.league_members (
    user_id uuid not null references auth.users (id) on delete cascade,
    week_start date not null,
    tier smallint not null check (tier between 0 and 5),
    cohort integer not null,
    xp integer not null default 0 check (xp >= 0),
    display_name text not null default '',
    updated_at timestamptz not null default now(),
    primary key (user_id, week_start)
);

create index league_members_group on public.league_members (week_start, tier, cohort, xp desc);

alter table public.league_members enable row level security;
-- Doğrudan erişim yok; okuma ve yazma aşağıdaki fonksiyonlarla yapılır.

create function public.league_week() returns date
language sql stable as $$
    select date_trunc('week', now() at time zone 'Europe/Istanbul')::date;
$$;

-- Öğrencinin bu haftaki üyeliğini döndürür; yoksa geçen haftaki sonucuna göre kademe belirleyip bir gruba yerleştirir.
create function public.league_ensure_member(p_name text) returns public.league_members
language plpgsql security definer set search_path = public as $$
declare
    v_week date := league_week();
    v_row league_members;
    v_prev league_members;
    v_rank integer;
    v_size integer;
    v_tier smallint := 0;
    v_cohort integer;
begin
    if auth.uid() is null then
        raise exception 'giriş gerekli';
    end if;

    select * into v_row from league_members where user_id = auth.uid() and week_start = v_week;
    if found then
        return v_row;
    end if;

    select * into v_prev from league_members
        where user_id = auth.uid() and week_start < v_week
        order by week_start desc limit 1;
    if found then
        v_tier := v_prev.tier;
        -- Yalnızca bir önceki haftaya katıldıysa terfi/düşme uygulanır.
        if v_prev.week_start = v_week - 7 then
            select count(*) into v_size from league_members
                where week_start = v_prev.week_start and tier = v_prev.tier and cohort = v_prev.cohort;
            select count(*) + 1 into v_rank from league_members
                where week_start = v_prev.week_start and tier = v_prev.tier and cohort = v_prev.cohort
                  and (xp > v_prev.xp or (xp = v_prev.xp and updated_at < v_prev.updated_at));
            if v_rank <= 7 and v_prev.xp > 0 then
                v_tier := least(v_tier + 1, 5);
            elsif v_size >= 10 and v_rank > v_size - 5 then
                v_tier := greatest(v_tier - 1, 0);
            end if;
        end if;
    end if;

    -- Aynı kademeye aynı anda katılanlar aynı grubu aşmasın diye kilit.
    perform pg_advisory_xact_lock(hashtext(v_week::text || ':' || v_tier::text));
    select c.cohort into v_cohort from (
        select cohort, count(*) as n from league_members
        where week_start = v_week and tier = v_tier group by cohort
    ) c where c.n < 30 order by c.cohort limit 1;
    if v_cohort is null then
        select coalesce(max(cohort), 0) + 1 into v_cohort from league_members where week_start = v_week and tier = v_tier;
    end if;

    insert into league_members (user_id, week_start, tier, cohort, xp, display_name)
        values (auth.uid(), v_week, v_tier, v_cohort, 0, left(coalesce(p_name, ''), 40))
        returning * into v_row;
    return v_row;
end;
$$;

-- Uygulama bu haftaki toplam XP'yi bildirir. Değer yalnızca artabilir; haftalık üst sınır kötüye kullanımı sınırlar.
create function public.league_report(p_week_xp integer, p_name text) returns void
language plpgsql security definer set search_path = public as $$
begin
    perform league_ensure_member(p_name);
    update league_members
        set xp = greatest(xp, least(coalesce(p_week_xp, 0), 20000)),
            display_name = case when coalesce(p_name, '') = '' then display_name else left(p_name, 40) end,
            updated_at = case when least(coalesce(p_week_xp, 0), 20000) > xp then now() else updated_at end
        where user_id = auth.uid() and week_start = league_week();
end;
$$;

-- Öğrencinin bu haftaki grubundaki sıralama.
create function public.league_standings()
returns table (rank integer, display_name text, xp integer, is_me boolean, tier smallint, week_start date)
language plpgsql security definer set search_path = public as $$
declare
    v_me league_members;
begin
    select m.* into v_me from league_members m where m.user_id = auth.uid() and m.week_start = league_week();
    if not found then
        return;
    end if;
    return query
        select (row_number() over (order by m.xp desc, m.updated_at))::integer,
               coalesce(nullif(m.display_name, ''), 'Öğrenci'),
               m.xp,
               m.user_id = auth.uid(),
               m.tier,
               m.week_start
        from league_members m
        where m.week_start = v_me.week_start and m.tier = v_me.tier and m.cohort = v_me.cohort
        order by m.xp desc, m.updated_at;
end;
$$;

revoke execute on function public.league_ensure_member(text), public.league_report(integer, text),
    public.league_standings() from anon, public;
grant execute on function public.league_report(integer, text), public.league_standings() to authenticated;

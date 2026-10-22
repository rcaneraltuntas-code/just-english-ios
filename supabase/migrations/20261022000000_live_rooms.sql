-- Uygulama içi canlı yayın (LiveKit).
-- Öğretmen yayını başlattığında live_started_at, bitirdiğinde live_ended_at dolar.
-- Oda anahtarı supabase/functions/livekit-token tarafından üretilir; o fonksiyon bu alanları da yazar.

alter table public.live_sessions
    add column live_started_at timestamptz,
    add column live_ended_at timestamptz;

-- Yeni sütunlar görünümün sonuna eklenir (create or replace view yalnızca sona ekleme yapabilir).
create or replace view public.live_sessions_public with (security_invoker = false) as
select
    s.id, s.unit_id, s.level, s.title, s.starts_at, s.duration_minutes, s.teacher_name, s.capacity,
    (select count(*) from public.live_bookings b where b.session_id = s.id)::integer as booked,
    case
        when s.teacher_id = auth.uid()
          or exists (select 1 from public.live_bookings b where b.session_id = s.id and b.user_id = auth.uid())
        then s.join_url
    end as join_url,
    s.live_started_at,
    s.live_ended_at
from public.live_sessions s
where not s.cancelled;

grant select on public.live_sessions_public to anon, authenticated;

-- Öğretmen yayını bitirir. RLS zaten öğretmenin kendi dersini güncellemesine izin verir; bu fonksiyon
-- yalnızca bitiş zamanını yazdığı için istemcide tek satırlık çağrı olarak kalır.
create function public.end_live_session(p_session uuid) returns void
language sql security definer set search_path = public as $$
    update live_sessions set live_ended_at = now()
    where id = p_session and teacher_id = auth.uid() and live_started_at is not null and live_ended_at is null;
$$;

revoke execute on function public.end_live_session(uuid) from anon, public;
grant execute on function public.end_live_session(uuid) to authenticated;

-- Öğretmen ekranı için: dersin katılımcı listesi.
-- Öğrencilerin user_state satırları RLS ile gizli olduğu için ad, yalnızca dersin öğretmenine bu fonksiyonla gösterilir.

create function public.session_attendees(p_session uuid)
returns table (user_id uuid, display_name text, attended boolean, booked_at timestamptz)
language sql stable security definer set search_path = public as $$
    select b.user_id,
           coalesce(nullif(u.display_name, ''), nullif(p.display_name, ''), 'Öğrenci') as display_name,
           b.attended,
           b.created_at as booked_at
    from live_bookings b
    join live_sessions s on s.id = b.session_id
    left join user_state u on u.user_id = b.user_id
    left join profiles p on p.id = b.user_id
    where b.session_id = p_session and s.teacher_id = auth.uid()
    order by b.created_at;
$$;

revoke execute on function public.session_attendees(uuid) from anon, public;
grant execute on function public.session_attendees(uuid) to authenticated;

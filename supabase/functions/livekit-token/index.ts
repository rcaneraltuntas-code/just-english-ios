// Canlı ders odasına giriş anahtarı (LiveKit).
//
// İstemci: POST { "session_id": "<uuid>" }, Authorization: Bearer <kullanıcı JWT>
// Yanıt:   { "url": "wss://...", "token": "<jwt>", "role": "teacher" | "student" }
//
// Kurallar:
// - Dersin öğretmeni: başlangıçtan 30 dk önce ile bitişten 60 dk sonrası arasında girebilir. İlk girişte
//   live_started_at yazılır ve ders öğrencilere "Canlı" görünür. Kamera, mikrofon ve ekran paylaşımı açıktır.
// - Öğrenci: yer ayırtmış olmalı ve ders başlangıçtan 10 dk önce ile bitiş arasında olmalı. Yalnızca mikrofon
//   yayınlayabilir (kamera kapalı); söz alma uygulama içinde öğretmen izniyle olur.
//
// Gerekli gizli değerler (supabase secrets set ...): LIVEKIT_URL, LIVEKIT_API_KEY, LIVEKIT_API_SECRET.
// SUPABASE_URL, SUPABASE_ANON_KEY ve SUPABASE_SERVICE_ROLE_KEY Supabase tarafından otomatik verilir.

import { createClient } from "npm:@supabase/supabase-js@2.118.0";
import { AccessToken, TrackSource } from "npm:livekit-server-sdk@2.19.2";

const cors = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
};

function reply(status: number, body: Record<string, unknown>) {
  return new Response(JSON.stringify(body), { status, headers: { ...cors, "Content-Type": "application/json" } });
}

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: cors });
  if (req.method !== "POST") return reply(405, { error: "method_not_allowed" });

  const livekitURL = Deno.env.get("LIVEKIT_URL");
  const apiKey = Deno.env.get("LIVEKIT_API_KEY");
  const apiSecret = Deno.env.get("LIVEKIT_API_SECRET");
  if (!livekitURL || !apiKey || !apiSecret) return reply(503, { error: "livekit_not_configured" });

  const authHeader = req.headers.get("Authorization") ?? "";
  const supabaseURL = Deno.env.get("SUPABASE_URL")!;
  const userClient = createClient(supabaseURL, Deno.env.get("SUPABASE_ANON_KEY")!, {
    global: { headers: { Authorization: authHeader } },
  });
  const { data: { user } } = await userClient.auth.getUser();
  if (!user) return reply(401, { error: "not_signed_in" });

  let sessionID: string | undefined;
  try {
    sessionID = (await req.json())?.session_id;
  } catch {
    // Gövde yoksa aşağıda reddedilir.
  }
  if (!sessionID) return reply(400, { error: "missing_session_id" });

  const admin = createClient(supabaseURL, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);
  const { data: session } = await admin
    .from("live_sessions")
    .select("id, title, starts_at, duration_minutes, teacher_id, teacher_name, cancelled, live_started_at, live_ended_at")
    .eq("id", sessionID)
    .maybeSingle();
  if (!session || session.cancelled) return reply(404, { error: "session_not_found" });

  const start = new Date(session.starts_at).getTime();
  const end = start + session.duration_minutes * 60_000;
  const now = Date.now();
  const isTeacher = session.teacher_id === user.id;

  let displayName: string;
  if (isTeacher) {
    if (now < start - 30 * 60_000 || now > end + 60 * 60_000) return reply(403, { error: "outside_window" });
    displayName = session.teacher_name;
    // İlk girişte ya da öğretmen bitirdikten sonra yeniden açarsa ders tekrar canlı sayılır.
    if (!session.live_started_at || session.live_ended_at) {
      await admin.from("live_sessions")
        .update({ live_started_at: session.live_started_at ?? new Date().toISOString(), live_ended_at: null })
        .eq("id", session.id);
    }
  } else {
    if (now < start - 10 * 60_000 || now > end) return reply(403, { error: "outside_window" });
    if (session.live_ended_at) return reply(403, { error: "session_ended" });
    const { data: booking } = await admin
      .from("live_bookings")
      .select("user_id")
      .eq("session_id", session.id)
      .eq("user_id", user.id)
      .maybeSingle();
    if (!booking) return reply(403, { error: "not_booked" });
    const { data: state } = await admin.from("user_state").select("display_name").eq("user_id", user.id).maybeSingle();
    const { data: profile } = await admin.from("profiles").select("display_name").eq("id", user.id).maybeSingle();
    displayName = state?.display_name || profile?.display_name || "Öğrenci";
  }

  const token = new AccessToken(apiKey, apiSecret, {
    identity: user.id,
    name: displayName,
    ttl: "3h",
    attributes: { role: isTeacher ? "teacher" : "student" },
  });
  token.addGrant({
    room: `live-${session.id}`,
    roomJoin: true,
    canSubscribe: true,
    canPublish: true,
    canPublishData: true,
    canUpdateOwnMetadata: true, // el kaldırma, katılımcı özelliği olarak tutulur
    roomAdmin: isTeacher,
    canPublishSources: isTeacher
      ? [TrackSource.CAMERA, TrackSource.MICROPHONE, TrackSource.SCREEN_SHARE, TrackSource.SCREEN_SHARE_AUDIO]
      : [TrackSource.MICROPHONE],
  });

  return reply(200, { url: livekitURL, token: await token.toJwt(), role: isTeacher ? "teacher" : "student" });
});

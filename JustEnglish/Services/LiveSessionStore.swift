import Foundation
import JECore
import Observation
import Supabase

/// Öğretmenlerin açtığı canlı grup dersi.
struct LiveSession: Codable, Identifiable, Hashable {
    let id: UUID
    let unitID: String
    let level: CEFRLevel
    let title: String
    let startsAt: Date
    let durationMinutes: Int
    let teacherName: String
    let joinURL: URL?
    let capacity: Int?
    let booked: Int?
    /// Öğretmen uygulama içi yayını başlattığında / bitirdiğinde dolar.
    let liveStartedAt: Date?
    let liveEndedAt: Date?

    enum CodingKeys: String, CodingKey {
        case id, level, title, capacity, booked
        case unitID = "unit_id", startsAt = "starts_at", durationMinutes = "duration_minutes"
        case teacherName = "teacher_name", joinURL = "join_url"
        case liveStartedAt = "live_started_at", liveEndedAt = "live_ended_at"
    }

    var seatsLeft: Int? { capacity.map { max(0, $0 - (booked ?? 0)) } }

    /// Katılım bağlantısı dersten 10 dakika önce açılır.
    var isJoinable: Bool {
        let now = Date.now
        return now >= startsAt.addingTimeInterval(-600) && now <= startsAt.addingTimeInterval(TimeInterval(durationMinutes * 60))
            && liveEndedAt == nil
    }

    /// Öğretmen şu an uygulama içinden yayında.
    var isLive: Bool { liveStartedAt != nil && liveEndedAt == nil && isJoinable }
}

@MainActor
@Observable
final class LiveSessionStore {
    enum State: Equatable { case idle, loading, loaded, unavailable, failed(String) }

    private(set) var state: State = .idle
    private(set) var sessions: [LiveSession] = []
    private(set) var bookings: Set<UUID> = []

    /// Öğrenciye uyarı olarak gösterilecek mesaj (ör. giriş gerekli, ders dolu).
    var notice: String?

    /// Katılım XP'si için: AppModel'e bağlanır.
    var onAttend: ((LiveSession) -> Void)?

    func refresh() async {
        guard let client = Backend.client else { state = .unavailable; return }
        if sessions.isEmpty { state = .loading }
        do {
            let from = Date.now.addingTimeInterval(-3600)
            sessions = try await client.from("live_sessions_public")
                .select()
                .gte("starts_at", value: from.ISO8601Format())
                .order("starts_at")
                .limit(100)
                .execute()
                .value
            if let user = try? await client.auth.session.user {
                struct Booking: Decodable { let session_id: UUID }
                let rows: [Booking] = try await client.from("live_bookings")
                    .select("session_id").eq("user_id", value: user.id).execute().value
                bookings = Set(rows.map(\.session_id))
            }
            state = .loaded
        } catch {
            state = sessions.isEmpty ? .failed("İnternet bağlantınızı kontrol edin.") : .loaded
        }
    }

    func isBooked(_ session: LiveSession) -> Bool { bookings.contains(session.id) }

    func book(_ session: LiveSession) async {
        guard let client = Backend.client else { return }
        guard (try? await client.auth.session) != nil else {
            notice = "Canlı derse yer ayırtmak için Profil sekmesinden Apple ile giriş yapın."
            return
        }
        do {
            try await client.rpc("book_live_session", params: ["p_session": session.id]).execute()
            bookings.insert(session.id)
            await refresh()
        } catch {
            notice = "Yer ayrılamadı. Ders dolmuş olabilir."
        }
    }

    func cancel(_ session: LiveSession) async {
        guard let client = Backend.client else { return }
        do {
            try await client.rpc("cancel_live_booking", params: ["p_session": session.id]).execute()
            bookings.remove(session.id)
            await refresh()
        } catch {
            notice = "Kayıt iptal edilemedi. Lütfen tekrar deneyin."
        }
    }

    /// Aynı ders için XP bir kez verilir.
    private var attended: Set<UUID> = []

    func markAttended(_ session: LiveSession) {
        guard attended.insert(session.id).inserted else { return }
        onAttend?(session)
        guard let client = Backend.client else { return }
        Task { _ = try? await client.rpc("mark_live_attended", params: ["p_session": session.id]).execute() }
    }
}

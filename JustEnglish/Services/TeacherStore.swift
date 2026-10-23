import Foundation
import JECore
import Observation
import Supabase

/// Öğretmenin kendi açtığı canlı dersler. RLS, öğretmenin yalnızca kendi derslerini görmesini ve değiştirmesini sağlar.
@MainActor
@Observable
final class TeacherStore {
    struct Session: Codable, Identifiable, Hashable {
        let id: UUID
        var unitID: String
        var level: CEFRLevel
        var title: String
        var startsAt: Date
        var durationMinutes: Int
        var teacherName: String
        var joinURL: String?
        var capacity: Int?
        var cancelled: Bool

        enum CodingKeys: String, CodingKey {
            case id, level, title, capacity, cancelled
            case unitID = "unit_id", startsAt = "starts_at", durationMinutes = "duration_minutes"
            case teacherName = "teacher_name", joinURL = "join_url"
        }

        /// Uygulama içi yayın, dersten 30 dk önce ile bitişten 60 dk sonrası arasında açılabilir
        /// (supabase/functions/livekit-token ile aynı aralık). Harici bağlantı girilmiş derslerde gösterilmez.
        var canBroadcast: Bool {
            guard !cancelled, joinURL?.isEmpty ?? true else { return false }
            let now = Date.now
            return now >= startsAt.addingTimeInterval(-1800)
                && now <= startsAt.addingTimeInterval(TimeInterval(durationMinutes * 60 + 3600))
        }
    }

    /// Yeni ders ya da düzenleme için gönderilen alanlar. teacher_id veritabanında auth.uid() ile dolar.
    struct Draft: Encodable, Sendable {
        var unitID: String
        var level: CEFRLevel
        var title: String
        var startsAt: Date
        var durationMinutes: Int
        var teacherName: String
        var joinURL: String?
        var capacity: Int?

        enum CodingKeys: String, CodingKey {
            case level, title, capacity
            case unitID = "unit_id", startsAt = "starts_at", durationMinutes = "duration_minutes"
            case teacherName = "teacher_name", joinURL = "join_url"
        }
    }

    struct Attendee: Decodable, Identifiable, Hashable {
        let userID: UUID
        let displayName: String
        let attended: Bool
        var id: UUID { userID }

        enum CodingKeys: String, CodingKey {
            case userID = "user_id", displayName = "display_name", attended
        }
    }

    private(set) var sessions: [Session] = []
    private(set) var isLoading = false
    var error: String?

    func refresh() async {
        guard let client = Backend.client, let user = try? await client.auth.session.user else { return }
        isLoading = true
        defer { isLoading = false }
        do {
            sessions = try await client.from("live_sessions")
                .select("id, unit_id, level, title, starts_at, duration_minutes, teacher_name, join_url, capacity, cancelled")
                .eq("teacher_id", value: user.id)
                .gte("starts_at", value: Date.now.addingTimeInterval(-86_400).ISO8601Format())
                .order("starts_at")
                .execute()
                .value
        } catch {
            self.error = "Dersler yüklenemedi."
        }
    }

    func save(_ draft: Draft, editing id: UUID?) async -> Bool {
        guard let client = Backend.client else { return false }
        do {
            if let id {
                try await client.from("live_sessions").update(draft).eq("id", value: id).execute()
            } else {
                try await client.from("live_sessions").insert(draft).execute()
            }
            await refresh()
            return true
        } catch {
            self.error = "Ders kaydedilemedi. Bilgileri kontrol edip tekrar deneyin."
            return false
        }
    }

    func cancel(_ session: Session) async {
        guard let client = Backend.client else { return }
        do {
            try await client.from("live_sessions").update(["cancelled": true]).eq("id", value: session.id).execute()
            await refresh()
        } catch {
            self.error = "Ders iptal edilemedi."
        }
    }

    func attendees(of session: Session) async -> [Attendee] {
        guard let client = Backend.client else { return [] }
        return (try? await client.rpc("session_attendees", params: ["p_session": session.id]).execute().value) ?? []
    }
}

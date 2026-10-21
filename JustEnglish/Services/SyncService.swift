import Foundation
import Supabase

/// Öğrenci durumunu `user_state` tablosunda tek bir JSON satırı olarak saklar.
/// İki cihazda çalışılmışsa durumlar birleştirilir; hiçbir ilerleme kaybolmaz.
@MainActor
enum SyncService {
    private struct Row: Codable, Sendable {
        let userID: UUID
        let state: UserState
        let currentLevel: String
        let totalXP: Int
        let displayName: String

        enum CodingKeys: String, CodingKey {
            case userID = "user_id", state, currentLevel = "current_level", totalXP = "total_xp", displayName = "display_name"
        }
    }

    static func sync(_ model: AppModel, userID: UUID) async {
        guard let client = Backend.client else { return }
        do {
            let rows: [Row] = try await client.from("user_state").select().eq("user_id", value: userID).execute().value
            let merged = rows.first.map { model.state.merged(with: $0.state) } ?? model.state
            if merged != model.state { model.state = merged }
            try await client.from("user_state")
                .upsert(Row(userID: userID, state: merged, currentLevel: merged.currentLevel.rawValue,
                            totalXP: merged.progress.totalXP, displayName: merged.name))
                .execute()
        } catch {
            // Eşitleme hatası öğrenciyi durdurmaz; bir sonraki açılışta tekrar denenir.
            print("Eşitleme başarısız: \(error)")
        }
    }
}

extension UserState {
    /// İki cihazdaki durumu birleştirir: bitirilen dersler birleşir, puanlarda en iyisi, kartlarda en son tekrar kalır.
    func merged(with other: UserState) -> UserState {
        var result = self
        result.onboarded = onboarded || other.onboarded
        if result.name.isEmpty { result.name = other.name }
        result.currentLevel = max(currentLevel, other.currentLevel)
        result.placementLevel = placementLevel ?? other.placementLevel
        result.completedLessons = completedLessons.union(other.completedLessons)
        result.lessonScores = lessonScores.merging(other.lessonScores, uniquingKeysWith: max)
        result.unitTestScores = unitTestScores.merging(other.unitTestScores, uniquingKeysWith: max)
        result.cardMemory = cardMemory.merging(other.cardMemory) { a, b in a.lastReview >= b.lastReview ? a : b }
        var newCards = newCards
        for id in other.newCards where !newCards.contains(id) { newCards.append(id) }
        result.newCards = newCards.filter { result.cardMemory[$0] == nil }
        var mistakes = mistakes
        for id in other.mistakes where !mistakes.contains(id) { mistakes.append(id) }
        result.mistakes = mistakes
        // Seri ve XP için daha çok çalışılmış cihazın kaydı esas alınır.
        if other.progress.totalXP > progress.totalXP {
            result.progress = other.progress
            result.progress.dailyGoalXP = progress.dailyGoalXP
        }
        return result
    }
}

import Foundation

/// Öğrencinin bir kartı hatırlama değerlendirmesi.
public enum ReviewRating: Int, Codable, CaseIterable, Sendable {
    /// Hatırlamadı.
    case again = 1
    /// Zorlanarak hatırladı.
    case hard = 2
    /// Hatırladı.
    case good = 3
    /// Çok kolay hatırladı.
    case easy = 4
}

/// Bir kelime kartının öğrenciye özel hafıza durumu.
public struct CardMemory: Codable, Hashable, Sendable {
    /// Gün cinsinden kararlılık: hatırlama olasılığının %90'a düştüğü süre.
    public var stability: Double
    /// 1 (kolay) ile 10 (zor) arası zorluk.
    public var difficulty: Double
    public var lastReview: Date
    public var due: Date
    public var reps: Int
    public var lapses: Int

    public init(stability: Double, difficulty: Double, lastReview: Date, due: Date, reps: Int, lapses: Int) {
        self.stability = stability
        self.difficulty = difficulty
        self.lastReview = lastReview
        self.due = due
        self.reps = reps
        self.lapses = lapses
    }
}

/// FSRS-4.5 aralıklı tekrar zamanlayıcısı.
///
/// Anki'nin de kullandığı, bilimsel olarak doğrulanmış hafıza modeli. Her tekrardan sonra
/// kartın kararlılığını ve zorluğunu günceller ve hatırlama olasılığı `desiredRetention`
/// değerine düştüğünde kartı tekrar gösterir. Böylece öğrenci unutmak üzere olduğu kelimeyi
/// tam zamanında tekrar eder.
public struct FSRS: Sendable {
    public static let defaultWeights: [Double] = [
        0.4872, 1.4003, 3.7145, 13.8206, 5.1618, 1.2298, 0.8975, 0.031,
        1.6474, 0.1367, 1.0461, 2.1072, 0.0793, 0.3246, 1.587, 0.2272, 2.8755,
    ]
    static let decay = -0.5
    static let factor = 19.0 / 81.0

    public let w: [Double]
    public let desiredRetention: Double
    public let maximumInterval: Double

    public init(weights: [Double] = FSRS.defaultWeights, desiredRetention: Double = 0.9, maximumInterval: Double = 365) {
        precondition(weights.count == 17)
        self.w = weights
        self.desiredRetention = desiredRetention
        self.maximumInterval = maximumInterval
    }

    /// `elapsedDays` gün sonra hatırlama olasılığı.
    public func retrievability(elapsedDays: Double, stability: Double) -> Double {
        pow(1 + Self.factor * elapsedDays / stability, Self.decay)
    }

    public func retrievability(of memory: CardMemory, at now: Date) -> Double {
        retrievability(elapsedDays: max(0, now.timeIntervalSince(memory.lastReview) / 86_400), stability: memory.stability)
    }

    /// Kararlılığa göre bir sonraki tekrara kadar geçecek gün sayısı (en az 1).
    public func interval(for stability: Double) -> Double {
        let raw = stability / Self.factor * (pow(desiredRetention, 1 / Self.decay) - 1)
        return min(max(1, raw.rounded()), maximumInterval)
    }

    /// Yeni bir kartın ilk tekrarı.
    public func first(_ rating: ReviewRating, at now: Date) -> CardMemory {
        let s = w[rating.rawValue - 1]
        let d = initialDifficulty(rating)
        return CardMemory(stability: s, difficulty: d, lastReview: now,
                          due: due(after: s, rating: rating, from: now),
                          reps: 1, lapses: rating == .again ? 1 : 0)
    }

    /// Daha önce görülmüş bir kartın tekrarı.
    public func review(_ memory: CardMemory, _ rating: ReviewRating, at now: Date) -> CardMemory {
        let elapsed = max(0, now.timeIntervalSince(memory.lastReview) / 86_400)
        let r = retrievability(elapsedDays: elapsed, stability: memory.stability)
        let d = nextDifficulty(memory.difficulty, rating)
        let s: Double
        if rating == .again {
            s = min(forgetStability(d: memory.difficulty, s: memory.stability, r: r), memory.stability)
        } else {
            s = recallStability(d: memory.difficulty, s: memory.stability, r: r, rating: rating)
        }
        var next = memory
        next.stability = s
        next.difficulty = d
        next.lastReview = now
        next.due = due(after: s, rating: rating, from: now)
        next.reps += 1
        if rating == .again { next.lapses += 1 }
        return next
    }

    private func due(after stability: Double, rating: ReviewRating, from now: Date) -> Date {
        // Unutulan kart aynı oturumda 10 dakika sonra tekrar sorulur.
        if rating == .again { return now.addingTimeInterval(10 * 60) }
        return now.addingTimeInterval(interval(for: stability) * 86_400)
    }

    private func initialDifficulty(_ rating: ReviewRating) -> Double {
        clampDifficulty(w[4] - Double(rating.rawValue - 3) * w[5])
    }

    private func nextDifficulty(_ d: Double, _ rating: ReviewRating) -> Double {
        let next = d - w[6] * Double(rating.rawValue - 3)
        // Ortalamaya dönüş: zorluk uç değerlere sıkışıp kalmasın.
        return clampDifficulty(w[7] * initialDifficulty(.good) + (1 - w[7]) * next)
    }

    private func recallStability(d: Double, s: Double, r: Double, rating: ReviewRating) -> Double {
        let hardPenalty = rating == .hard ? w[15] : 1
        let easyBonus = rating == .easy ? w[16] : 1
        return s * (1 + exp(w[8]) * (11 - d) * pow(s, -w[9]) * (exp((1 - r) * w[10]) - 1) * hardPenalty * easyBonus)
    }

    private func forgetStability(d: Double, s: Double, r: Double) -> Double {
        w[11] * pow(d, -w[12]) * (pow(s + 1, w[13]) - 1) * exp((1 - r) * w[14])
    }

    private func clampDifficulty(_ d: Double) -> Double { min(max(d, 1), 10) }
}

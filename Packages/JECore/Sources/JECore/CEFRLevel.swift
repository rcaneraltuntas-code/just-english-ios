import Foundation

/// Avrupa Ortak Dil Çerçevesi (CEFR) seviyeleri. Tüm içerik bu seviyelere etiketlenir.
public enum CEFRLevel: String, Codable, CaseIterable, Comparable, Sendable, Identifiable {
    case a1 = "A1"
    case a2 = "A2"
    case b1 = "B1"
    case b2 = "B2"
    case c1 = "C1"
    case c2 = "C2"

    public var id: String { rawValue }

    public var index: Int { Self.allCases.firstIndex(of: self)! }

    /// Just English'in kurs adlandırmasıyla eşleşen başlık.
    public var title: String {
        switch self {
        case .a1: "Beginner"
        case .a2: "Elementary"
        case .b1: "Pre-Intermediate"
        case .b2: "Intermediate"
        case .c1: "Upper-Intermediate"
        case .c2: "Advanced"
        }
    }

    /// Öğrenciye gösterilen kısa "yapabilirim" özeti (CEFR can-do).
    public var canDoSummary: String {
        switch self {
        case .a1: "Kendini tanıtabilir, basit sorular sorup cevaplayabilirsin."
        case .a2: "Günlük işlerini halledebilir, geçmişte yaptıklarını anlatabilirsin."
        case .b1: "Seyahatte rahat iletişim kurabilir, fikrini gerekçesiyle söyleyebilirsin."
        case .b2: "Ana dili İngilizce olanlarla akıcı konuşabilir, tartışmaya katılabilirsin."
        case .c1: "Akademik ve iş ortamında dili esnek ve etkili kullanabilirsin."
        case .c2: "Neredeyse her şeyi zahmetsizce anlayıp ince anlam farklarını ifade edebilirsin."
        }
    }

    public var next: CEFRLevel? {
        let i = index + 1
        return i < Self.allCases.count ? Self.allCases[i] : nil
    }

    public var previous: CEFRLevel? {
        index > 0 ? Self.allCases[index - 1] : nil
    }

    public static func < (lhs: CEFRLevel, rhs: CEFRLevel) -> Bool { lhs.index < rhs.index }
}

/// Dil becerileri. Her içerik birimi en az bir beceriye hizmet eder.
public enum Skill: String, Codable, CaseIterable, Sendable {
    case grammar, vocabulary, reading, listening, speaking, writing
}

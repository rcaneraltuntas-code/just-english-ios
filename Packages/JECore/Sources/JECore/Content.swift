import Foundation

// Uygulamaya gömülü ünite içeriğinin modelleri. Şema `content-src/lib.py` ile birebir eşleşir;
// içerik orada doğrulandığı için burada yalnızca okunur.

/// Bir ünite: 5 ders, kelime kartları, ünite testi ve canlı ders planı.
public struct CourseUnit: Codable, Identifiable, Hashable, Sendable {
    public let id: String
    public let level: CEFRLevel
    public let number: Int
    public let title: String
    public let titleEn: String
    public let canDo: String
    public let grammar: [String]
    public let vocabularyThemes: [String]
    public let liveClass: LiveClassPlan
    public let vocabulary: [VocabularyCard]
    public let lessons: [Lesson]
    public let unitTest: UnitTest
}

public struct LiveClassPlan: Codable, Hashable, Sendable {
    public let title: String
    public let durationMinutes: Int
    public let goal: String
}

public struct VocabularyCard: Codable, Identifiable, Hashable, Sendable {
    public let id: String
    public let en: String
    public let tr: String
    public let example: String
    public let exampleTr: String
    public let note: String?
}

public struct UnitTest: Codable, Hashable, Sendable {
    public let passPercent: Int
    public let questions: [Exercise]
}

/// Bir ders dört adımdan oluşur: Keşfet → Öğren → Uygula → Kullan.
public struct Lesson: Codable, Identifiable, Hashable, Sendable {
    public let id: String
    public let number: Int
    public let title: String
    public let goal: String
    public let warmup: Warmup
    public let discover: Discover
    public let learn: Learn
    public let practice: [Exercise]
    public let use: UseTask
}

/// Dersin başındaki tekrar: önceki kartlardan birkaçı sorulur.
public struct Warmup: Codable, Hashable, Sendable {
    public let source: String
    public let count: Int?
    public let note: String?
}

public struct Discover: Codable, Hashable, Sendable {
    public enum Kind: String, Codable, Sendable { case text, dialogue }

    public struct Line: Codable, Hashable, Sendable {
        public let speaker: String
        public let text: String
    }

    public let kind: Kind
    public let title: String
    public let body: String?
    public let lines: [Line]?
    public let questions: [Exercise]
}

public struct Learn: Codable, Hashable, Sendable {
    public struct Example: Codable, Hashable, Sendable {
        public let en: String
        public let tr: String
    }

    /// Markdown: kalın, italik, liste ve tablo içerebilir.
    public let explanation: String
    public let examples: [Example]
    public let turkishNote: String?
}

public struct UseTask: Codable, Hashable, Sendable {
    public let id: String
    public let kind: String
    public let task: Exercise
}

public struct MatchPair: Codable, Hashable, Sendable {
    public let left: String
    public let right: String
}

/// Tüm alıştırma türleri. JSON'daki `type` alanına göre çözülür.
public enum Exercise: Identifiable, Hashable, Sendable {
    case multipleChoice(id: String, prompt: String, options: [String], answerIndex: Int,
                        explanation: String, wrongFeedback: [Int: String])
    case gapFill(id: String, text: String, answers: [String], explanation: String, hint: String?)
    case ordering(id: String, words: [String], answer: String, explanation: String, translation: String?)
    case matching(id: String, pairs: [MatchPair], explanation: String)
    case typeAnswer(id: String, prompt: String, accepted: [String], explanation: String)
    case listening(id: String, audioText: String, prompt: String, options: [String], answerIndex: Int,
                   explanation: String)
    case speaking(id: String, prompt: String, modelAnswer: String, rubric: [String])
    case writing(id: String, prompt: String, modelAnswer: String, rubric: [String])

    public var id: String {
        switch self {
        case let .multipleChoice(id, _, _, _, _, _), let .gapFill(id, _, _, _, _), let .ordering(id, _, _, _, _),
             let .matching(id, _, _), let .typeAnswer(id, _, _, _), let .listening(id, _, _, _, _, _),
             let .speaking(id, _, _, _), let .writing(id, _, _, _):
            id
        }
    }

    /// Konuşma ve yazma görevleri otomatik puanlanmaz; öğrenci örnek cevapla kendini değerlendirir.
    public var isAutoGraded: Bool {
        switch self {
        case .speaking, .writing: false
        default: true
        }
    }

    public var explanation: String? {
        switch self {
        case let .multipleChoice(_, _, _, _, e, _), let .gapFill(_, _, _, e, _), let .ordering(_, _, _, e, _),
             let .matching(_, _, e), let .typeAnswer(_, _, _, e), let .listening(_, _, _, _, _, e):
            e
        case .speaking, .writing:
            nil
        }
    }
}

extension Exercise: Codable {
    private enum CodingKeys: String, CodingKey {
        case type, id, prompt, options, answerIndex, explanation, wrongFeedback, text, answers, hint
        case words, answer, translation, pairs, accepted, audioText, modelAnswer, rubric
    }

    public init(from decoder: Decoder) throws {
        let c = try decoder.container(keyedBy: CodingKeys.self)
        let type = try c.decode(String.self, forKey: .type)
        // Konuşma/yazma görevlerinin kimliği derste `use.id` alanındadır; görevin kendisinde olmayabilir.
        let id = try c.decodeIfPresent(String.self, forKey: .id) ?? ""
        switch type {
        case "multipleChoice":
            let raw = try c.decodeIfPresent([String: String].self, forKey: .wrongFeedback) ?? [:]
            var feedback: [Int: String] = [:]
            for (k, v) in raw { if let i = Int(k) { feedback[i] = v } }
            self = .multipleChoice(id: id, prompt: try c.decode(String.self, forKey: .prompt),
                                   options: try c.decode([String].self, forKey: .options),
                                   answerIndex: try c.decode(Int.self, forKey: .answerIndex),
                                   explanation: try c.decode(String.self, forKey: .explanation),
                                   wrongFeedback: feedback)
        case "gapFill":
            self = .gapFill(id: id, text: try c.decode(String.self, forKey: .text),
                            answers: try c.decode([String].self, forKey: .answers),
                            explanation: try c.decode(String.self, forKey: .explanation),
                            hint: try c.decodeIfPresent(String.self, forKey: .hint))
        case "ordering":
            self = .ordering(id: id, words: try c.decode([String].self, forKey: .words),
                             answer: try c.decode(String.self, forKey: .answer),
                             explanation: try c.decode(String.self, forKey: .explanation),
                             translation: try c.decodeIfPresent(String.self, forKey: .translation))
        case "matching":
            self = .matching(id: id, pairs: try c.decode([MatchPair].self, forKey: .pairs),
                             explanation: try c.decode(String.self, forKey: .explanation))
        case "typeAnswer":
            self = .typeAnswer(id: id, prompt: try c.decode(String.self, forKey: .prompt),
                               accepted: try c.decode([String].self, forKey: .accepted),
                               explanation: try c.decode(String.self, forKey: .explanation))
        case "listening":
            self = .listening(id: id, audioText: try c.decode(String.self, forKey: .audioText),
                              prompt: try c.decode(String.self, forKey: .prompt),
                              options: try c.decode([String].self, forKey: .options),
                              answerIndex: try c.decode(Int.self, forKey: .answerIndex),
                              explanation: try c.decode(String.self, forKey: .explanation))
        case "speaking":
            self = .speaking(id: id, prompt: try c.decode(String.self, forKey: .prompt),
                             modelAnswer: try c.decode(String.self, forKey: .modelAnswer),
                             rubric: try c.decode([String].self, forKey: .rubric))
        case "writing":
            self = .writing(id: id, prompt: try c.decode(String.self, forKey: .prompt),
                            modelAnswer: try c.decode(String.self, forKey: .modelAnswer),
                            rubric: try c.decode([String].self, forKey: .rubric))
        default:
            throw DecodingError.dataCorruptedError(forKey: .type, in: c, debugDescription: "Bilinmeyen alıştırma türü: \(type)")
        }
    }

    public func encode(to encoder: Encoder) throws {
        var c = encoder.container(keyedBy: CodingKeys.self)
        try c.encode(id, forKey: .id)
        switch self {
        case let .multipleChoice(_, prompt, options, answerIndex, explanation, wrongFeedback):
            try c.encode("multipleChoice", forKey: .type)
            try c.encode(prompt, forKey: .prompt)
            try c.encode(options, forKey: .options)
            try c.encode(answerIndex, forKey: .answerIndex)
            try c.encode(explanation, forKey: .explanation)
            if !wrongFeedback.isEmpty {
                try c.encode(Dictionary(uniqueKeysWithValues: wrongFeedback.map { (String($0.key), $0.value) }),
                             forKey: .wrongFeedback)
            }
        case let .gapFill(_, text, answers, explanation, hint):
            try c.encode("gapFill", forKey: .type)
            try c.encode(text, forKey: .text)
            try c.encode(answers, forKey: .answers)
            try c.encode(explanation, forKey: .explanation)
            try c.encodeIfPresent(hint, forKey: .hint)
        case let .ordering(_, words, answer, explanation, translation):
            try c.encode("ordering", forKey: .type)
            try c.encode(words, forKey: .words)
            try c.encode(answer, forKey: .answer)
            try c.encode(explanation, forKey: .explanation)
            try c.encodeIfPresent(translation, forKey: .translation)
        case let .matching(_, pairs, explanation):
            try c.encode("matching", forKey: .type)
            try c.encode(pairs, forKey: .pairs)
            try c.encode(explanation, forKey: .explanation)
        case let .typeAnswer(_, prompt, accepted, explanation):
            try c.encode("typeAnswer", forKey: .type)
            try c.encode(prompt, forKey: .prompt)
            try c.encode(accepted, forKey: .accepted)
            try c.encode(explanation, forKey: .explanation)
        case let .listening(_, audioText, prompt, options, answerIndex, explanation):
            try c.encode("listening", forKey: .type)
            try c.encode(audioText, forKey: .audioText)
            try c.encode(prompt, forKey: .prompt)
            try c.encode(options, forKey: .options)
            try c.encode(answerIndex, forKey: .answerIndex)
            try c.encode(explanation, forKey: .explanation)
        case let .speaking(_, prompt, modelAnswer, rubric):
            try c.encode("speaking", forKey: .type)
            try c.encode(prompt, forKey: .prompt)
            try c.encode(modelAnswer, forKey: .modelAnswer)
            try c.encode(rubric, forKey: .rubric)
        case let .writing(_, prompt, modelAnswer, rubric):
            try c.encode("writing", forKey: .type)
            try c.encode(prompt, forKey: .prompt)
            try c.encode(modelAnswer, forKey: .modelAnswer)
            try c.encode(rubric, forKey: .rubric)
        }
    }
}

// MARK: - Cevap kontrolü

/// Öğrencinin yazdığı cevapları içerikteki kabul edilen cevaplarla karşılaştırır.
///
/// Büyük/küçük harf, baştaki/sondaki boşluk, sondaki noktalama ve kıvrık kesme işareti (’) farkları
/// hata sayılmaz. Bu kurallar `content-src/lib.py` doğrulayıcısıyla uyumludur.
public enum AnswerChecker {
    public static func normalize(_ s: String) -> String {
        var t = s.replacingOccurrences(of: "’", with: "'")
            .replacingOccurrences(of: "‘", with: "'")
            .replacingOccurrences(of: "“", with: "\"")
            .replacingOccurrences(of: "”", with: "\"")
            .trimmingCharacters(in: .whitespacesAndNewlines)
        while let last = t.last, ".!,".contains(last) { t.removeLast() }
        t = t.trimmingCharacters(in: .whitespaces)
        // Birden fazla boşluğu teke indir.
        t = t.split(whereSeparator: \.isWhitespace).joined(separator: " ")
        return t.lowercased()
    }

    public static func matches(_ input: String, accepted: [String]) -> Bool {
        let n = normalize(input)
        return !n.isEmpty && accepted.contains { normalize($0) == n }
    }

    /// Sıralama alıştırmasında seçilen kelime dizisi cevapla aynı mı.
    public static func ordering(_ chosen: [String], answer: String) -> Bool {
        let joined = chosen.joined(separator: " ")
            .replacingOccurrences(of: " ?", with: "?")
            .replacingOccurrences(of: " .", with: ".")
            .replacingOccurrences(of: " !", with: "!")
            .replacingOccurrences(of: " ,", with: ",")
        return normalize(joined).replacingOccurrences(of: ",", with: "")
            == normalize(answer).replacingOccurrences(of: ",", with: "")
    }
}

// MARK: - Kütüphane

/// Gömülü içerik dosyalarını okur ve seviyelere göre sıralar.
public struct ContentLibrary: Sendable {
    public let units: [CourseUnit]
    public let placement: [PlacementItem]

    public init(units: [CourseUnit], placement: [PlacementItem]) {
        self.units = units.sorted { ($0.level, $0.number) < ($1.level, $1.number) }
        self.placement = placement
    }

    /// `directory` içindeki `xN-uNN.json` ünite dosyalarını ve `placement.json` dosyasını okur.
    public static func load(from directory: URL) throws -> ContentLibrary {
        let decoder = JSONDecoder()
        let files = try FileManager.default.contentsOfDirectory(at: directory, includingPropertiesForKeys: nil)
        var units: [CourseUnit] = []
        for url in files where url.pathExtension == "json" && url.lastPathComponent.contains("-u") {
            do {
                units.append(try decoder.decode(CourseUnit.self, from: Data(contentsOf: url)))
            } catch {
                throw ContentError.invalidFile(url.lastPathComponent, error)
            }
        }
        let placementURL = directory.appendingPathComponent("placement.json")
        let placement = try decoder.decode([PlacementItem].self, from: Data(contentsOf: placementURL))
        return ContentLibrary(units: units, placement: placement)
    }

    public func units(for level: CEFRLevel) -> [CourseUnit] {
        units.filter { $0.level == level }
    }

    public func unit(id: String) -> CourseUnit? {
        units.first { $0.id == id }
    }

    /// Tüm kelime kartları (sözlükte ve tekrar destesinde kullanılır).
    public var allCards: [VocabularyCard] {
        units.flatMap(\.vocabulary)
    }
}

public enum ContentError: Error, CustomStringConvertible {
    case invalidFile(String, Error)

    public var description: String {
        switch self {
        case let .invalidFile(name, error): "\(name) okunamadı: \(error)"
        }
    }
}

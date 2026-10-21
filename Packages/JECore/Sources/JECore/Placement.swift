import Foundation

/// Seviye tespit sınavındaki tek bir soru.
public struct PlacementItem: Codable, Identifiable, Hashable, Sendable {
    public let id: String
    public let level: CEFRLevel
    public let skill: Skill
    /// Okuma sorularında önce gösterilen metin.
    public let passage: String?
    public let prompt: String
    public let options: [String]
    public let answerIndex: Int
    /// Sonuç ekranında gösterilen Türkçe açıklama: neden bu cevap doğru.
    public let explanation: String

    public init(id: String, level: CEFRLevel, skill: Skill, passage: String? = nil,
                prompt: String, options: [String], answerIndex: Int, explanation: String) {
        self.id = id
        self.level = level
        self.skill = skill
        self.passage = passage
        self.prompt = prompt
        self.options = options
        self.answerIndex = answerIndex
        self.explanation = explanation
    }
}

public struct PlacementAnswer: Codable, Hashable, Sendable {
    public let item: PlacementItem
    public let chosenIndex: Int
    public var isCorrect: Bool { chosenIndex == item.answerIndex }
}

public struct PlacementResult: Codable, Hashable, Sendable {
    /// Öğrencinin çalışmaya başlayacağı seviye: hâkim olduğu en yüksek seviyenin bir üstü.
    public let level: CEFRLevel
    /// Sınavda hâkim olduğu görülen en yüksek seviye (hiçbiri değilse nil).
    public let masteredLevel: CEFRLevel?
    public let answers: [PlacementAnswer]
    /// Beceri bazında doğru oranı; kişisel planı ağırlıklandırmak için kullanılır.
    public let skillScores: [Skill: Double]

    public var weakestSkill: Skill? {
        skillScores.min { $0.value < $1.value }?.key
    }
}

/// Çok aşamalı uyarlamalı seviye tespiti.
///
/// Sınav A2'den başlar ve her seviyeden 4 soruluk bir blok sorar.
/// Bloktaki 3+ doğru seviyeyi "geçti" sayar ve bir üst seviyeye çıkar,
/// 1 veya daha az doğru "kaldı" sayar ve bir alt seviyeye iner. 2 doğru sınırda kabul edilir:
/// aynı seviyeden ikinci bir blok sorulur ve iki bloğun toplamına (5/8) bakılır.
/// Bir seviye geçilip bir üstü kalındığında sınav biter. Böylece öğrenci
/// 60+ soruluk sabit bir test yerine genellikle 12-20 soruda doğru seviyeye yerleşir.
public struct PlacementEngine: Sendable {
    public static let blockSize = 4
    public static let maxBlocks = 7

    private let bank: [CEFRLevel: [PlacementItem]]
    private var used: Set<String> = []
    private var passed: Set<CEFRLevel> = []
    private var failed: Set<CEFRLevel> = []
    /// Sınırda kalınan seviyelerin ilk blok doğru sayısı.
    private var borderline: [CEFRLevel: Int] = [:]

    public private(set) var currentLevel: CEFRLevel
    public private(set) var currentBlock: [PlacementItem] = []
    public private(set) var answers: [PlacementAnswer] = []
    public private(set) var blocksAsked = 0
    public private(set) var result: PlacementResult?

    public var isFinished: Bool { result != nil }

    public init(items: [PlacementItem], startLevel: CEFRLevel = .a2) {
        self.bank = Dictionary(grouping: items, by: \.level)
        self.currentLevel = startLevel
        self.currentBlock = nextBlock(for: startLevel)
    }

    /// Mevcut bloktaki soruları cevaplar ve bir sonraki bloğu hazırlar.
    public mutating func submitBlock(_ chosen: [String: Int]) {
        precondition(!isFinished, "Sınav bitti")
        let blockAnswers = currentBlock.map { PlacementAnswer(item: $0, chosenIndex: chosen[$0.id] ?? -1) }
        answers += blockAnswers
        blocksAsked += 1
        let correct = blockAnswers.filter(\.isCorrect).count
        decide(level: currentLevel, correct: correct, total: blockAnswers.count)
    }

    private mutating func decide(level: CEFRLevel, correct: Int, total: Int) {
        let verdict: Bool?
        if let first = borderline.removeValue(forKey: level) {
            // İkinci blok: iki bloğun toplamında 5/8 ve üzeri geçti sayılır.
            verdict = Double(first + correct) / Double(total * 2) > 0.6
        } else if Double(correct) >= Double(total) * 0.75 {
            verdict = true
        } else if Double(correct) <= Double(total) * 0.25 {
            verdict = false
        } else {
            verdict = nil
            borderline[level] = correct
        }

        switch verdict {
        case true?: passed.insert(level)
        case false?: failed.insert(level)
        case nil: break
        }

        if let next = nextLevelToAsk(after: level, verdict: verdict), blocksAsked < Self.maxBlocks {
            let block = nextBlock(for: next)
            if !block.isEmpty {
                currentLevel = next
                currentBlock = block
                return
            }
        }
        finish()
    }

    private func nextLevelToAsk(after level: CEFRLevel, verdict: Bool?) -> CEFRLevel? {
        switch verdict {
        case nil:
            return level
        case true?:
            guard let up = level.next, !failed.contains(up), !passed.contains(up) else { return nil }
            return up
        case false?:
            guard let down = level.previous, !passed.contains(down), !failed.contains(down) else { return nil }
            return down
        }
    }

    private mutating func nextBlock(for level: CEFRLevel) -> [PlacementItem] {
        let available = (bank[level] ?? []).filter { !used.contains($0.id) }
        // Blok dengesi: önce dilbilgisi, kelime ve okuma birer tane, kalan yerler karışık.
        var block: [PlacementItem] = []
        for skill in [Skill.grammar, .vocabulary, .reading] {
            if let item = available.first(where: { $0.skill == skill }) { block.append(item) }
        }
        for item in available where block.count < Self.blockSize && !block.contains(item) {
            block.append(item)
        }
        block.forEach { used.insert($0.id) }
        return block
    }

    private mutating func finish() {
        // Hâkim olunan en yüksek seviyenin bir üstünden başlanır. Hiçbiri geçilmediyse A1.
        let mastered = passed.max()
        let level = mastered.map { $0.next ?? $0 } ?? .a1
        var scores: [Skill: Double] = [:]
        for (skill, group) in Dictionary(grouping: answers, by: \.item.skill) {
            scores[skill] = Double(group.filter(\.isCorrect).count) / Double(group.count)
        }
        result = PlacementResult(level: level, masteredLevel: mastered, answers: answers, skillScores: scores)
        currentBlock = []
    }
}

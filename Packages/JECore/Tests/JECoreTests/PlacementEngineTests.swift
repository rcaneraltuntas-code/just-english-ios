import XCTest
@testable import JECore

final class PlacementEngineTests: XCTestCase {
    /// Her seviyeden 8 soru içeren sahte soru bankası. Doğru cevap her zaman 0.
    private func bank() -> [PlacementItem] {
        CEFRLevel.allCases.flatMap { level in
            (0..<8).map { i in
                PlacementItem(id: "\(level.rawValue)-\(i)", level: level,
                              skill: [Skill.grammar, .vocabulary, .reading][i % 3],
                              prompt: "q", options: ["a", "b"], answerIndex: 0, explanation: "")
            }
        }
    }

    /// Öğrenci `knows` dahil o seviyeye kadar her soruyu doğru, üstündekileri yanlış cevaplar.
    private func run(knows: CEFRLevel?) -> PlacementEngine {
        var engine = PlacementEngine(items: bank())
        while !engine.isFinished {
            var answers: [String: Int] = [:]
            for item in engine.currentBlock {
                let correct = knows.map { item.level <= $0 } ?? false
                answers[item.id] = correct ? 0 : 1
            }
            engine.submitBlock(answers)
        }
        return engine
    }

    func testStartsAtA2WithBalancedBlock() {
        let engine = PlacementEngine(items: bank())
        XCTAssertEqual(engine.currentLevel, .a2)
        XCTAssertEqual(engine.currentBlock.count, PlacementEngine.blockSize)
        XCTAssertEqual(Set(engine.currentBlock.map(\.skill)), [.grammar, .vocabulary, .reading])
    }

    func testBeginnerIsPlacedAtA1() {
        let engine = run(knows: nil)
        XCTAssertEqual(engine.result?.level, .a1)
        XCTAssertNil(engine.result?.masteredLevel)
    }

    func testRecommendsLevelAboveMastered() {
        let engine = run(knows: .b1)
        XCTAssertEqual(engine.result?.masteredLevel, .b1)
        XCTAssertEqual(engine.result?.level, .b2)
    }

    func testTopLevelStaysAtC2() {
        let engine = run(knows: .c2)
        XCTAssertEqual(engine.result?.level, .c2)
        XCTAssertLessThanOrEqual(engine.blocksAsked, PlacementEngine.maxBlocks)
    }

    func testBorderlineAsksSecondBlockAtSameLevel() {
        var engine = PlacementEngine(items: bank())
        let ids = engine.currentBlock.map(\.id)
        // 4 sorudan 2 doğru: sınırda.
        engine.submitBlock([ids[0]: 0, ids[1]: 0, ids[2]: 1, ids[3]: 1])
        XCTAssertEqual(engine.currentLevel, .a2)
        XCTAssertTrue(Set(engine.currentBlock.map(\.id)).isDisjoint(with: ids), "Aynı soru tekrar sorulmamalı")
    }

    func testSkillScoresAreComputed() {
        let engine = run(knows: .a2)
        let scores = engine.result!.skillScores
        XCTAssertEqual(Set(scores.keys), [.grammar, .vocabulary, .reading])
        XCTAssertTrue(scores.values.allSatisfy { (0...1).contains($0) })
    }
}

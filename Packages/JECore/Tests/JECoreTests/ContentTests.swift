import XCTest
@testable import JECore

final class ContentTests: XCTestCase {
    /// Depodaki gerçek içerik klasörü: Packages/JECore/Tests/JECoreTests → JustEnglish/Resources/Content
    private var contentDirectory: URL {
        URL(fileURLWithPath: #filePath)
            .deletingLastPathComponent().deletingLastPathComponent().deletingLastPathComponent()
            .deletingLastPathComponent().deletingLastPathComponent()
            .appendingPathComponent("JustEnglish/Resources/Content")
    }

    func testAllUnitsDecode() throws {
        let library = try ContentLibrary.load(from: contentDirectory)
        XCTAssertEqual(library.units.count, 68)
        XCTAssertEqual(library.units(for: .a1).count, 12)
        XCTAssertEqual(library.units(for: .c2).count, 8)
        XCTAssertEqual(library.units.first?.id, "a1-u01")
        XCTAssertEqual(library.units.last?.id, "c2-u08")
        XCTAssertFalse(library.placement.isEmpty)
        for unit in library.units {
            XCTAssertEqual(unit.lessons.count, 5, unit.id)
            XCTAssertEqual(unit.unitTest.questions.count, 15, unit.id)
        }
    }

    func testCorrectAnswersAreAccepted() throws {
        let library = try ContentLibrary.load(from: contentDirectory)
        for unit in library.units {
            for exercise in unit.lessons.flatMap(\.practice) + unit.unitTest.questions {
                switch exercise {
                case let .gapFill(id, _, answers, _, _):
                    XCTAssertTrue(AnswerChecker.matches(answers[0], accepted: answers), id)
                case let .typeAnswer(id, _, accepted, _):
                    XCTAssertTrue(AnswerChecker.matches(accepted[0] + ".", accepted: accepted), id)
                default:
                    break
                }
            }
        }
    }

    func testAnswerNormalisation() {
        XCTAssertTrue(AnswerChecker.matches("  I’m fine. ", accepted: ["I'm fine"]))
        XCTAssertTrue(AnswerChecker.matches("HELLO", accepted: ["hello"]))
        XCTAssertFalse(AnswerChecker.matches("", accepted: [""]))
        XCTAssertFalse(AnswerChecker.matches("I fine", accepted: ["I'm fine"]))
    }

    func testOrderingChecker() {
        XCTAssertTrue(AnswerChecker.ordering(["What", "is", "your", "name", "?"], answer: "What is your name?"))
        XCTAssertTrue(AnswerChecker.ordering(["Admittedly", "it", "is", "expensive"], answer: "Admittedly, it is expensive."))
        XCTAssertFalse(AnswerChecker.ordering(["is", "What", "your", "name", "?"], answer: "What is your name?"))
    }

    func testExerciseRoundTrip() throws {
        let json = #"{"type":"multipleChoice","id":"x","prompt":"p","options":["a","b"],"answerIndex":1,"explanation":"e","wrongFeedback":{"0":"no"}}"#
        let exercise = try JSONDecoder().decode(Exercise.self, from: Data(json.utf8))
        let again = try JSONDecoder().decode(Exercise.self, from: JSONEncoder().encode(exercise))
        XCTAssertEqual(exercise, again)
        guard case let .multipleChoice(_, _, _, _, _, feedback) = exercise else { return XCTFail() }
        XCTAssertEqual(feedback[0], "no")
    }
}

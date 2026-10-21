import XCTest
import JECore
@testable import JustEnglish

final class MarkdownTests: XCTestCase {
    func testParsesTablesListsAndParagraphs() {
        let source = """
        **First conditional** olası bir sonucu anlatır.

        | If + present | will + fiil |
        |---|---|
        | If it **rains**, | I'll stay. |

        - I'll stay **if** it rains.
        - (~~If it will rain~~)
        1. Birinci
        2. İkinci
        """
        let blocks = MarkdownBlock.parse(source)
        XCTAssertEqual(blocks, [
            .paragraph("**First conditional** olası bir sonucu anlatır."),
            .table(header: ["If + present", "will + fiil"], rows: [["If it **rains**,", "I'll stay."]]),
            .bullets(["I'll stay **if** it rains.", "(~~If it will rain~~)"]),
            .numbered(["Birinci", "İkinci"]),
        ])
    }
}

final class UserStateMergeTests: XCTestCase {
    func testMergeKeepsProgressFromBothDevices() {
        let now = Date(timeIntervalSince1970: 1_800_000_000)
        let fsrs = FSRS()
        var phone = UserState()
        phone.completedLessons = ["a1-u01-l1"]
        phone.lessonScores = ["a1-u01-l1": 80]
        phone.cardMemory["a1-u01-v01"] = fsrs.first(.good, at: now)
        phone.newCards = ["a1-u01-v02"]

        var tablet = UserState()
        tablet.completedLessons = ["a1-u01-l2"]
        tablet.lessonScores = ["a1-u01-l1": 90]
        tablet.cardMemory["a1-u01-v01"] = fsrs.first(.again, at: now.addingTimeInterval(60))
        tablet.cardMemory["a1-u01-v02"] = fsrs.first(.easy, at: now)
        tablet.currentLevel = .a2
        tablet.progress.totalXP = 500

        let merged = phone.merged(with: tablet)
        XCTAssertEqual(merged.completedLessons, ["a1-u01-l1", "a1-u01-l2"])
        XCTAssertEqual(merged.lessonScores["a1-u01-l1"], 90)
        XCTAssertEqual(merged.cardMemory["a1-u01-v01"]?.lastReview, now.addingTimeInterval(60))
        // Diğer cihazda tekrar edilen kart artık yeni kart değildir.
        XCTAssertEqual(merged.newCards, [])
        XCTAssertEqual(merged.currentLevel, .a2)
        XCTAssertEqual(merged.progress.totalXP, 500)
    }
}

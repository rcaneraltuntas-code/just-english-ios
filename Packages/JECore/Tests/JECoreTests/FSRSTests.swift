import XCTest
@testable import JECore

final class FSRSTests: XCTestCase {
    let fsrs = FSRS()
    let start = Date(timeIntervalSince1970: 1_800_000_000)

    func testRetrievabilityIs90PercentAtStability() {
        XCTAssertEqual(fsrs.retrievability(elapsedDays: 10, stability: 10), 0.9, accuracy: 0.001)
    }

    func testIntervalEqualsStabilityAt90PercentRetention() {
        XCTAssertEqual(fsrs.interval(for: 10), 10)
        XCTAssertEqual(fsrs.interval(for: 0.2), 1, "En kısa aralık 1 gün")
    }

    func testFirstReviewOrdersByRating() {
        let ratings = ReviewRating.allCases.map { fsrs.first($0, at: start).stability }
        XCTAssertEqual(ratings, ratings.sorted())
        XCTAssertEqual(fsrs.first(.again, at: start).due, start.addingTimeInterval(600))
    }

    func testSuccessfulReviewsGrowInterval() {
        var card = fsrs.first(.good, at: start)
        var lastInterval = 0.0
        for _ in 0..<5 {
            let interval = card.due.timeIntervalSince(card.lastReview)
            XCTAssertGreaterThan(interval, lastInterval)
            lastInterval = interval
            card = fsrs.review(card, .good, at: card.due)
        }
        XCTAssertEqual(card.reps, 6)
    }

    func testLapseReducesStabilityAndRaisesDifficulty() {
        let card = fsrs.review(fsrs.first(.good, at: start), .good, at: start.addingTimeInterval(3 * 86_400))
        let lapsed = fsrs.review(card, .again, at: card.due)
        XCTAssertLessThan(lapsed.stability, card.stability)
        XCTAssertGreaterThan(lapsed.difficulty, card.difficulty)
        XCTAssertEqual(lapsed.lapses, 1)
    }

    func testDifficultyStaysInRange() {
        var card = fsrs.first(.again, at: start)
        for _ in 0..<20 { card = fsrs.review(card, .again, at: card.due) }
        XCTAssertLessThanOrEqual(card.difficulty, 10)
        for _ in 0..<40 { card = fsrs.review(card, .easy, at: card.due) }
        XCTAssertGreaterThanOrEqual(card.difficulty, 1)
        XCTAssertLessThanOrEqual(card.due.timeIntervalSince(card.lastReview), 365 * 86_400)
    }
}

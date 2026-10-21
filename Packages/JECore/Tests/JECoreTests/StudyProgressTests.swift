import XCTest
@testable import JECore

final class StudyProgressTests: XCTestCase {
    var calendar: Calendar = {
        var c = Calendar(identifier: .gregorian)
        c.timeZone = TimeZone(identifier: "Europe/Istanbul")!
        return c
    }()

    func day(_ n: Int, hour: Int = 12) -> Date {
        calendar.date(from: DateComponents(year: 2026, month: 11, day: n, hour: hour))!
    }

    func testGoalStartsAndExtendsStreak() {
        var p = StudyProgress(dailyGoalXP: 20)
        p.add(xp: 10, at: day(2), calendar: calendar)
        XCTAssertEqual(p.streak, 0, "Hedef tutmadan seri başlamaz")
        p.add(xp: 10, at: day(2), calendar: calendar)
        XCTAssertEqual(p.streak, 1)
        p.add(xp: 30, at: day(2, hour: 20), calendar: calendar)
        XCTAssertEqual(p.streak, 1, "Aynı gün seriyi iki kez artırmaz")
        p.add(xp: 20, at: day(3, hour: 8), calendar: calendar)
        XCTAssertEqual(p.streak, 2)
        XCTAssertEqual(p.totalXP, 70)
        XCTAssertEqual(p.todayXP, 20)
    }

    func testFreezeCoversOneMissedDay() {
        var p = StudyProgress(dailyGoalXP: 10)
        p.add(xp: 10, at: day(2), calendar: calendar)
        p.add(xp: 10, at: day(4), calendar: calendar)
        XCTAssertEqual(p.streak, 2)
        XCTAssertEqual(p.freezesAvailable, 0)
        p.add(xp: 10, at: day(6), calendar: calendar)
        XCTAssertEqual(p.streak, 1, "Koruyucu kalmadıysa seri sıfırlanır")
        XCTAssertEqual(p.longestStreak, 2)
    }

    func testDisplayedStreakExpires() {
        var p = StudyProgress(dailyGoalXP: 10)
        p.freezesAvailable = 0
        p.add(xp: 10, at: day(2), calendar: calendar)
        XCTAssertEqual(p.displayedStreak(at: day(3), calendar: calendar), 1)
        XCTAssertEqual(p.displayedStreak(at: day(4), calendar: calendar), 0)
    }

    func testFreezeRefillsOncePerWeek() {
        var p = StudyProgress()
        p.freezesAvailable = 0
        p.refillFreezeIfNeeded(at: day(2), calendar: calendar)   // ilk açılış: yalnızca hafta kaydedilir
        XCTAssertEqual(p.freezesAvailable, 0)
        p.refillFreezeIfNeeded(at: day(9), calendar: calendar)   // 9 Kasım 2026 pazartesi
        p.refillFreezeIfNeeded(at: day(9, hour: 20), calendar: calendar)
        p.refillFreezeIfNeeded(at: day(12), calendar: calendar)
        XCTAssertEqual(p.freezesAvailable, 1)
        p.refillFreezeIfNeeded(at: day(17), calendar: calendar)
        p.refillFreezeIfNeeded(at: day(24), calendar: calendar)
        XCTAssertEqual(p.freezesAvailable, 2)
    }

    func testWeeklyXPResetsOnMonday() {
        var p = StudyProgress()
        p.add(xp: 30, at: day(13), calendar: calendar)          // cuma
        p.add(xp: 20, at: day(15, hour: 23), calendar: calendar) // pazar gece
        XCTAssertEqual(p.weekXP(at: day(15), calendar: calendar), 50)
        XCTAssertEqual(p.weekXP(at: day(16), calendar: calendar), 0) // pazartesi: yeni hafta
        p.add(xp: 5, at: day(16), calendar: calendar)
        XCTAssertEqual(p.weekXP(at: day(17), calendar: calendar), 5)
        XCTAssertEqual(p.totalXP, 55)
    }
}

import Foundation

/// Öğrencinin günlük çalışma serisi ve XP'si.
///
/// Seri, öğrencinin günlük hedefini (dakika değil, XP) tutturduğu ardışık günlerdir.
/// Bir günü kaçırmak seriyi bozar; ancak öğrenci haftada bir kez "seri koruyucu" kullanabilir.
/// Amaç tekrar alışkanlığı kazandırmak: düzenli ve kısa çalışma, seyrek ve uzun çalışmadan iyidir.
public struct StudyProgress: Codable, Hashable, Sendable {
    public var dailyGoalXP: Int
    public var totalXP: Int
    public var streak: Int
    public var longestStreak: Int
    /// Hedefin tutturulduğu son gün (yerel takvim günü başlangıcı).
    public var lastGoalDay: Date?
    /// Bugün kazanılan XP ve bu değerin ait olduğu gün.
    public var todayXP: Int
    public var todayDay: Date?
    public var freezesAvailable: Int

    public init(dailyGoalXP: Int = 30) {
        self.dailyGoalXP = dailyGoalXP
        self.totalXP = 0
        self.streak = 0
        self.longestStreak = 0
        self.lastGoalDay = nil
        self.todayXP = 0
        self.todayDay = nil
        self.freezesAvailable = 1
    }

    public var goalReachedToday: Bool { todayXP >= dailyGoalXP }

    /// XP ekler ve gerekirse seriyi günceller.
    public mutating func add(xp: Int, at now: Date, calendar: Calendar = .current) {
        let today = calendar.startOfDay(for: now)
        if todayDay != today {
            todayDay = today
            todayXP = 0
        }
        let wasReached = goalReachedToday
        todayXP += xp
        totalXP += xp
        guard !wasReached, goalReachedToday else { return }

        if let last = lastGoalDay, let gap = calendar.dateComponents([.day], from: last, to: today).day {
            switch gap {
            case 0: break
            case 1: streak += 1
            case 2 where freezesAvailable > 0:
                // Tek bir kaçırılan gün koruyucuyla kapatılır.
                freezesAvailable -= 1
                streak += 1
            default: streak = 1
            }
        } else {
            streak = 1
        }
        lastGoalDay = today
        longestStreak = max(longestStreak, streak)
    }

    /// Uygulama açıldığında gösterilecek güncel seri: hedef dün veya bugün tutturulmadıysa seri bitmiştir.
    public func displayedStreak(at now: Date, calendar: Calendar = .current) -> Int {
        guard let last = lastGoalDay,
              let gap = calendar.dateComponents([.day], from: last, to: calendar.startOfDay(for: now)).day
        else { return 0 }
        if gap <= 1 { return streak }
        if gap == 2 && freezesAvailable > 0 { return streak }
        return 0
    }

    /// Her pazartesi bir seri koruyucu yenilenir (en fazla 2).
    public mutating func refillFreezeIfNeeded(at now: Date, calendar: Calendar = .current) {
        if calendar.component(.weekday, from: now) == 2 && freezesAvailable < 2 {
            freezesAvailable += 1
        }
    }
}

/// XP kuralları tek yerde tutulur, böylece tüm etkinlikler tutarlı ödüllendirilir.
public enum XPRule {
    public static let correctAnswer = 2
    public static let flashcardReview = 1
    public static let lessonCompleted = 10
    public static let perfectLesson = 5
    public static let gameWin = 8
    public static let liveClassAttended = 30
}

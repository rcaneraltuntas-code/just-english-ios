import Foundation
import JECore
import Observation

/// Öğrencinin cihazda saklanan tüm durumu. Önce yerelde tutulur; giriş yapılınca Supabase ile eşitlenir.
struct UserState: Codable, Equatable, Sendable {
    var onboarded = false
    var name = ""
    var currentLevel: CEFRLevel = .a1
    var placementLevel: CEFRLevel?
    var dailyGoal: DailyGoal = .regular
    var progress = StudyProgress(dailyGoalXP: DailyGoal.regular.xp)
    /// Bitirilen derslerin kimlikleri.
    var completedLessons: Set<String> = []
    /// Ders kimliği → en iyi doğru oranı (0-100).
    var lessonScores: [String: Int] = [:]
    /// Ünite kimliği → ünite testindeki en iyi yüzde.
    var unitTestScores: [String: Int] = [:]
    /// Kart kimliği → FSRS hafıza durumu. Desteye eklenmiş ama hiç tekrar edilmemiş kartlar `newCards` içindedir.
    var cardMemory: [String: CardMemory] = [:]
    var newCards: [String] = []
    /// Yanlış yapılan alıştırmalar: tekrar oturumunda yeniden sorulur.
    var mistakes: [String] = []
}

@MainActor
@Observable
final class AppModel {
    private(set) var library: ContentLibrary?
    private(set) var loadError: String?
    var state = UserState()

    private let store: StateStore
    let fsrs = FSRS()

    init(store: StateStore = .shared) {
        self.store = store
        if let saved = store.load() { state = saved }
        persistOnChange()
    }

    /// `state` her değiştiğinde diske yazar. Aynı döngüdeki birden çok değişiklik tek kayıtta toplanır.
    private func persistOnChange() {
        withObservationTracking {
            _ = state
        } onChange: { [weak self] in
            Task { @MainActor in
                guard let self else { return }
                self.store.save(self.state)
                self.persistOnChange()
            }
        }
    }

    func loadIfNeeded() {
        guard library == nil, loadError == nil else { return }
        do {
            guard let dir = Bundle.main.resourceURL else { throw CocoaError(.fileNoSuchFile) }
            library = try ContentLibrary.load(from: dir)
        } catch {
            loadError = String(describing: error)
        }
    }

    // MARK: - İçerik erişimi

    var units: [CourseUnit] { library?.units ?? [] }

    func units(for level: CEFRLevel) -> [CourseUnit] { library?.units(for: level) ?? [] }

    func unit(containing lessonID: String) -> CourseUnit? {
        units.first { $0.lessons.contains { $0.id == lessonID } }
    }

    func card(id: String) -> VocabularyCard? {
        if cardIndex.isEmpty { cardIndex = Dictionary(units.flatMap(\.vocabulary).map { ($0.id, $0) }, uniquingKeysWith: { a, _ in a }) }
        return cardIndex[id]
    }

    @ObservationIgnored private var cardIndex: [String: VocabularyCard] = [:]

    var dictionary: [DictionaryEntry] {
        if dictionaryCache.isEmpty { dictionaryCache = DictionaryEntry.build(from: units) }
        return dictionaryCache
    }

    @ObservationIgnored private var dictionaryCache: [DictionaryEntry] = []

    /// Öğrencinin şu an çalışması önerilen ders: mevcut seviyede bitmemiş ilk ders.
    var nextLesson: (unit: CourseUnit, lesson: Lesson)? {
        for unit in units(for: state.currentLevel) {
            if let lesson = unit.lessons.first(where: { !state.completedLessons.contains($0.id) }) {
                return (unit, lesson)
            }
        }
        return nil
    }

    func completedCount(in unit: CourseUnit) -> Int {
        unit.lessons.filter { state.completedLessons.contains($0.id) }.count
    }

    func isUnitPassed(_ unit: CourseUnit) -> Bool {
        (state.unitTestScores[unit.id] ?? 0) >= unit.unitTest.passPercent
    }

    // MARK: - Başlangıç

    func finishOnboarding(name: String, goal: DailyGoal, level: CEFRLevel, placement: CEFRLevel?) {
        state.name = name
        state.dailyGoal = goal
        state.progress.dailyGoalXP = goal.xp
        state.currentLevel = level
        state.placementLevel = placement
        state.onboarded = true
    }

    func setDailyGoal(_ goal: DailyGoal) {
        state.dailyGoal = goal
        state.progress.dailyGoalXP = goal.xp
    }

    // MARK: - İlerleme

    func award(xp: Int, now: Date = .now) {
        state.progress.add(xp: xp, at: now)
    }

    func recordAnswer(exerciseID: String, correct: Bool) {
        if correct {
            award(xp: XPRule.correctAnswer)
            state.mistakes.removeAll { $0 == exerciseID }
        } else if !state.mistakes.contains(exerciseID) {
            state.mistakes.append(exerciseID)
            if state.mistakes.count > 200 { state.mistakes.removeFirst() }
        }
    }

    /// Ders bittiğinde çağrılır: XP verir, ünitenin kelime kartlarını desteye ekler.
    func completeLesson(_ lesson: Lesson, in unit: CourseUnit, correct: Int, total: Int) {
        let percent = total == 0 ? 100 : Int((Double(correct) / Double(total) * 100).rounded())
        state.lessonScores[lesson.id] = max(state.lessonScores[lesson.id] ?? 0, percent)
        let firstTime = state.completedLessons.insert(lesson.id).inserted
        if firstTime {
            award(xp: XPRule.lessonCompleted + (percent == 100 ? XPRule.perfectLesson : 0))
            addCardsToDeck(for: lesson, in: unit)
        }
    }

    /// Her ders, ünitenin kartlarının yaklaşık beşte birini desteye ekler; son ders kalanların hepsini.
    private func addCardsToDeck(for lesson: Lesson, in unit: CourseUnit) {
        let cards = unit.vocabulary
        let per = Int((Double(cards.count) / Double(unit.lessons.count)).rounded(.up))
        let start = (lesson.number - 1) * per
        let end = lesson.number == unit.lessons.count ? cards.count : min(cards.count, start + per)
        guard start < end else { return }
        for card in cards[start..<end] where state.cardMemory[card.id] == nil && !state.newCards.contains(card.id) {
            state.newCards.append(card.id)
        }
    }

    func recordUnitTest(_ unit: CourseUnit, percent: Int) {
        let before = isUnitPassed(unit)
        state.unitTestScores[unit.id] = max(state.unitTestScores[unit.id] ?? 0, percent)
        if !before && isUnitPassed(unit) {
            award(xp: XPRule.lessonCompleted * 2)
            // Seviyenin son ünitesi geçildiyse bir üst seviyeye geç.
            if unit.id == units(for: unit.level).last?.id, let next = unit.level.next, state.currentLevel == unit.level {
                state.currentLevel = next
            }
        }
    }

    // MARK: - Kelime kartları (FSRS)

    func dueCards(now: Date = .now, limit: Int = 30) -> [VocabularyCard] {
        let due = state.cardMemory.filter { $0.value.due <= now }
            .sorted { $0.value.due < $1.value.due }
            .map(\.key)
        // Bir oturumda en fazla 15 yeni kart: önce vadesi gelen tekrarlar.
        let ids = Array((due + state.newCards.prefix(15)).prefix(limit))
        return ids.compactMap(card(id:))
    }

    var deckSize: Int { state.cardMemory.count + state.newCards.count }

    func isInDeck(_ cardID: String) -> Bool {
        state.cardMemory[cardID] != nil || state.newCards.contains(cardID)
    }

    /// Sözlükten elle eklenen kart, sıradaki tekrarda yeni kart olarak gelir.
    func addToDeck(_ cardID: String) {
        guard !isInDeck(cardID) else { return }
        state.newCards.insert(cardID, at: 0)
    }

    func review(cardID: String, rating: ReviewRating, now: Date = .now) {
        if let memory = state.cardMemory[cardID] {
            state.cardMemory[cardID] = fsrs.review(memory, rating, at: now)
        } else {
            state.cardMemory[cardID] = fsrs.first(rating, at: now)
            state.newCards.removeAll { $0 == cardID }
        }
        award(xp: XPRule.flashcardReview, now: now)
    }

    /// Dersin ısınma bölümü için daha önce öğrenilmiş kartlar.
    func warmupCards(count: Int) -> [VocabularyCard] {
        let known = state.cardMemory.sorted { $0.value.due < $1.value.due }.map(\.key)
        return Array(known.prefix(count)).compactMap(card(id:))
    }

    // MARK: - Oyunlar ve yanlışlar

    /// Oyunlarda kullanılan kelimeler: destedeki kartlar, az ise çalışılan ünitelerin tüm kelimeleri.
    var gamePool: [VocabularyCard] {
        let deck = (Array(state.cardMemory.keys) + state.newCards).compactMap(card(id:))
        guard deck.count < 20 else { return deck }
        let studied = units.filter { completedCount(in: $0) > 0 }.flatMap(\.vocabulary)
        var seen = Set(deck.map(\.id))
        return deck + studied.filter { seen.insert($0.id).inserted }
    }

    func mistakeExercises(limit: Int = 20) -> [Exercise] {
        if exerciseIndex.isEmpty {
            for unit in units {
                for exercise in unit.lessons.flatMap({ $0.discover.questions + $0.practice }) + unit.unitTest.questions {
                    exerciseIndex[exercise.id] = exercise
                }
            }
        }
        return state.mistakes.suffix(limit).compactMap { exerciseIndex[$0] }
    }

    @ObservationIgnored private var exerciseIndex: [String: Exercise] = [:]

    func resetAll() {
        state = UserState()
    }
}

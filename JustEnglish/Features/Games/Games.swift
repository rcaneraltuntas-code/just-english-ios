import SwiftUI
import JECore

enum GameRules {
    static let minimumCards = 8
    static let matchRaceRounds = 3
    static let matchRacePairs = 5
    static let speedQuizSeconds = 60
    static let spellingWords = 10
}

/// Oyun sonucu: yıldız sayısı ve kazanıp kazanmadığı (en az 2 yıldız XP kazandırır).
struct GameResult: Equatable {
    var stars: Int
    var headline: String
    var detail: String
    var won: Bool { stars >= 2 }
}

/// Oyunların ortak kabuğu: 3-2-1 geri sayımı, üst bar, bitiş ekranı (yıldızlar, konfeti, XP).
/// `content` oyun ekranıdır ve `started` true olduktan sonra çizilir; böylece süre geri sayımdan sonra başlar.
struct GameShell<Content: View>: View {
    let title: String
    let color: Color
    let result: GameResult?
    let onReplay: () -> Void
    @ViewBuilder let content: () -> Content

    @Environment(AppModel.self) private var model
    @Environment(\.dismiss) private var dismiss
    @State private var started = false
    @State private var awarded = false
    @State private var hop = 0

    var body: some View {
        ZStack {
            VStack(spacing: 0) {
                HStack {
                    Button { dismiss() } label: {
                        Image(systemName: "xmark").font(.jakarta(.headline, weight: .bold))
                    }
                    .foregroundStyle(.secondary)
                    Spacer()
                    Text(title).font(.jakarta(.headline, weight: .heavy))
                    Spacer()
                    Color.clear.frame(width: 20, height: 1)
                }
                .padding(.horizontal, 20)
                .padding(.vertical, 12)

                if let result {
                    resultView(result)
                        .transition(.opacity.combined(with: .scale(scale: 0.95)))
                } else if started {
                    content()
                        .transition(.opacity)
                } else {
                    Spacer()
                }
            }
            if !started {
                CountdownOverlay { withAnimation(Motion.smooth) { started = true } }
                    .transition(.opacity)
            }
        }
        .background(Theme.background)
        .animation(Motion.smooth, value: result)
    }

    private func resultView(_ result: GameResult) -> some View {
        ZStack {
            VStack(spacing: 18) {
                Spacer()
                JAIView(mood: result.won ? .celebrate : .sad, size: 120, color: color, bounceTrigger: hop)
                    .task {
                        guard result.won else { return }
                        for _ in 0..<3 {
                            try? await Task.sleep(for: .milliseconds(700))
                            hop += 1
                        }
                    }
                StarRating(stars: result.stars)
                Text(result.headline)
                    .font(.jakarta(.largeTitle, weight: .heavy))
                    .multilineTextAlignment(.center)
                Text(result.detail)
                    .font(.jakarta(.body))
                    .foregroundStyle(.secondary)
                    .multilineTextAlignment(.center)
                if result.won {
                    Label("+\(XPRule.gameWin) XP", systemImage: "bolt.fill")
                        .font(.jakarta(.headline, weight: .heavy))
                        .foregroundStyle(.white)
                        .padding(.horizontal, 16)
                        .padding(.vertical, 8)
                        .background(Theme.warning, in: Capsule())
                        .staggeredAppear(6, delay: 0.15)
                } else {
                    Text("XP kazanmak için en az 2 yıldız gerekiyor.")
                        .font(.jakarta(.footnote))
                        .foregroundStyle(.secondary)
                }
                Spacer()
                Button("Tekrar oyna") {
                    awarded = false
                    started = false
                    onReplay()
                }
                .buttonStyle(PrimaryButtonStyle(color: color))
                Button("Bitir") { dismiss() }.buttonStyle(.secondary)
            }
            .padding(20)
            if result.won { ConfettiView() }
        }
        .onAppear {
            guard result.won, !awarded else { return }
            awarded = true
            model.award(xp: XPRule.gameWin)
        }
    }
}

/// Oyunların üst satırı: solda skor, ortada kombo, sağda süre ya da tur.
struct GameHUD: View {
    let score: Int
    let combo: Int
    let trailing: String
    var trailingColor: Color = .primary

    var body: some View {
        HStack {
            HStack(spacing: 6) {
                Image(systemName: "star.fill").foregroundStyle(Theme.warning)
                RollingNumber(value: score, font: .jakarta(.title3, weight: .heavy))
            }
            Spacer()
            if combo >= 2 {
                HStack(spacing: 3) {
                    Image(systemName: "flame.fill").symbolEffect(.bounce, value: combo)
                    Text("x\(combo)").font(.jakarta(.headline, weight: .heavy)).contentTransition(.numericText())
                }
                .foregroundStyle(.white)
                .padding(.horizontal, 12)
                .padding(.vertical, 6)
                .background(Theme.streak, in: Capsule())
                .transition(.scale.combined(with: .opacity))
            }
            Spacer()
            Text(trailing)
                .font(.jakarta(.title3, weight: .heavy))
                .monospacedDigit()
                .foregroundStyle(trailingColor)
                .contentTransition(.numericText())
        }
        .animation(Motion.pop, value: combo)
    }
}

// MARK: - Eşleştirme yarışı

struct MatchRaceGame: View {
    let pool: [VocabularyCard]

    @State private var round = 0
    @State private var cards: [VocabularyCard] = []
    @State private var rightOrder: [Int] = []
    @State private var selected: Int?
    @State private var matched: Set<Int> = []
    @State private var wrong: Int?
    @State private var wrongShake = 0
    @State private var mistakes = 0
    @State private var combo = 0
    @State private var score = 0
    @State private var start: Date?
    @State private var result: GameResult?

    private var totalPairs: Int { GameRules.matchRaceRounds * GameRules.matchRacePairs }

    var body: some View {
        GameShell(title: "Eşleştirme yarışı", color: Theme.warning, result: result, onReplay: reset) {
            VStack(spacing: 16) {
                TimelineView(.periodic(from: .now, by: 0.1)) { context in
                    GameHUD(score: score, combo: combo,
                            trailing: String(format: "%.1f", context.date.timeIntervalSince(start ?? context.date)))
                }
                ProgressBar(value: Double(round * GameRules.matchRacePairs + matched.count) / Double(totalPairs),
                            color: Theme.warning, height: 10)
                HStack(alignment: .top, spacing: 12) {
                    VStack(spacing: 10) {
                        ForEach(cards.indices, id: \.self) { i in
                            cell(cards[i].en, highlight: matched.contains(i) ? Theme.success : (selected == i ? Theme.accent : nil),
                                 done: matched.contains(i)) {
                                withAnimation(Motion.press) { selected = i }
                                Haptics.tap()
                            }
                        }
                    }
                    VStack(spacing: 10) {
                        ForEach(rightOrder, id: \.self) { i in
                            cell(cards[i].tr, highlight: matched.contains(i) ? Theme.success : (wrong == i ? Theme.danger : nil),
                                 done: matched.contains(i)) { pick(i) }
                                .modifier(ShakeEffect(travel: 6, animatableData: wrong == i ? CGFloat(wrongShake) : 0))
                        }
                    }
                }
                .id(round)
                .transition(.asymmetric(insertion: .move(edge: .trailing).combined(with: .opacity),
                                        removal: .move(edge: .leading).combined(with: .opacity)))
                Spacer()
            }
            .padding(20)
            .animation(Motion.smooth, value: round)
            .onAppear { if start == nil { start = .now } }
        }
        .onAppear { if cards.isEmpty { newRound() } }
    }

    private func reset() {
        round = 0
        mistakes = 0
        combo = 0
        score = 0
        start = nil
        result = nil
        newRound()
    }

    private func newRound() {
        cards = Array(pool.shuffled().prefix(GameRules.matchRacePairs))
        rightOrder = Array(cards.indices).shuffled()
        matched = []
        selected = nil
    }

    private func pick(_ i: Int) {
        guard let s = selected else { return }
        if s == i {
            withAnimation(Motion.pop) {
                matched.insert(i)
                selected = nil
                combo += 1
                score += combo >= 3 ? 2 : 1
            }
            Haptics.success()
            if matched.count == cards.count {
                if round + 1 < GameRules.matchRaceRounds {
                    Task {
                        try? await Task.sleep(for: .milliseconds(250))
                        round += 1
                        newRound()
                    }
                } else {
                    finish()
                }
            }
        } else {
            mistakes += 1
            combo = 0
            wrong = i
            withAnimation(.linear(duration: 0.35)) { wrongShake += 1 }
            Haptics.error()
            Task { try? await Task.sleep(for: .milliseconds(400)); wrong = nil }
        }
    }

    private func finish() {
        let elapsed = Date.now.timeIntervalSince(start ?? .now)
        // 15 eşleştirme: hızlı ve hatasızsa 3 yıldız.
        let stars = mistakes <= 1 && elapsed < 45 ? 3 : mistakes <= 3 && elapsed < 75 ? 2 : 1
        result = GameResult(stars: stars, headline: String(format: "%.1f saniye", elapsed),
                            detail: "\(totalPairs) eşleştirme, \(mistakes) hata, \(score) puan.")
    }

    private func cell(_ text: String, highlight: Color?, done: Bool, action: @escaping () -> Void) -> some View {
        Button(action: action) {
            Text(text)
                .font(.jakarta(.callout, weight: .bold))
                .multilineTextAlignment(.center)
                .minimumScaleFactor(0.7)
                .frame(maxWidth: .infinity, minHeight: 60)
                .padding(.horizontal, 6)
        }
        .buttonStyle(TileButtonStyle(highlight: highlight))
        .opacity(done ? 0.4 : 1)
        .scaleEffect(done ? 0.94 : 1)
        .disabled(done)
    }
}

// MARK: - 60 saniye

struct SpeedQuizGame: View {
    let pool: [VocabularyCard]

    @State private var deadline: Date?
    @State private var question: VocabularyCard?
    @State private var options: [String] = []
    @State private var questionNumber = 0
    @State private var score = 0
    @State private var correctCount = 0
    @State private var asked = 0
    @State private var combo = 0
    @State private var flash: (option: String, correct: Bool)?
    @State private var reward: (id: Int, text: String)?
    @State private var result: GameResult?

    var body: some View {
        GameShell(title: "60 saniye", color: Theme.accent, result: result, onReplay: reset) {
            VStack(spacing: 20) {
                TimelineView(.periodic(from: .now, by: 0.1)) { context in
                    let left = max(0, (deadline ?? context.date).timeIntervalSince(context.date))
                    VStack(spacing: 10) {
                        GameHUD(score: score, combo: combo, trailing: "\(Int(left.rounded(.up))) sn",
                                trailingColor: left < 10 ? Theme.danger : .primary)
                        ProgressBar(value: left / Double(GameRules.speedQuizSeconds),
                                    color: left < 10 ? Theme.danger : Theme.accent, height: 12)
                    }
                    .onChange(of: left == 0) { _, over in if over && deadline != nil { finish() } }
                }
                Spacer()
                if let question {
                    ZStack(alignment: .top) {
                        VStack(spacing: 10) {
                            Text("Bu kelimenin anlamı ne?")
                                .font(.jakarta(.subheadline, weight: .semibold))
                                .foregroundStyle(.secondary)
                            Text(question.en)
                                .font(.jakarta(.largeTitle, weight: .heavy))
                                .multilineTextAlignment(.center)
                                .minimumScaleFactor(0.5)
                        }
                        .padding(.vertical, 34)
                        .padding(.horizontal, 16)
                        .frame(maxWidth: .infinity)
                        .background(Theme.surface, in: RoundedRectangle(cornerRadius: 24, style: .continuous))
                        .shadow(color: .black.opacity(0.08), radius: 14, y: 8)
                        .id(questionNumber)
                        .transition(.asymmetric(insertion: .scale(scale: 0.85).combined(with: .opacity),
                                                removal: .move(edge: .leading).combined(with: .opacity)))
                        if let reward {
                            FloatingReward(text: reward.text, color: Theme.success)
                                .id(reward.id)
                                .offset(y: -10)
                        }
                    }
                }
                Spacer()
                VStack(spacing: 8) {
                    ForEach(options, id: \.self) { option in
                        Button { answer(option) } label: {
                            Text(option)
                                .font(.jakarta(.body, weight: .bold))
                                .multilineTextAlignment(.center)
                                .frame(maxWidth: .infinity, minHeight: 52)
                                .padding(.horizontal, 10)
                        }
                        .buttonStyle(TileButtonStyle(highlight: flash?.option == option ? (flash!.correct ? Theme.success : Theme.danger) : nil))
                        .modifier(ShakeEffect(travel: 8, animatableData: flash?.option == option && flash?.correct == false ? 1 : 0))
                    }
                }
                .id(questionNumber)
                .transition(.opacity)
            }
            .padding(20)
            .animation(Motion.smooth, value: questionNumber)
            .onAppear {
                if deadline == nil { deadline = .now.addingTimeInterval(TimeInterval(GameRules.speedQuizSeconds)) }
            }
        }
        .onAppear { if question == nil { next() } }
    }

    private func reset() {
        deadline = nil
        score = 0
        correctCount = 0
        asked = 0
        combo = 0
        flash = nil
        result = nil
        next()
    }

    private func next() {
        guard let card = pool.randomElement() else { return }
        let distractors = Set(pool.map(\.tr)).subtracting([card.tr]).shuffled().prefix(3)
        question = card
        options = (distractors + [card.tr]).shuffled()
        questionNumber += 1
    }

    private func answer(_ option: String) {
        guard result == nil, flash == nil, let question else { return }
        asked += 1
        let correct = option == question.tr
        withAnimation(.linear(duration: 0.3)) { flash = (option, correct) }
        if correct {
            combo += 1
            correctCount += 1
            let points = combo >= 5 ? 3 : combo >= 3 ? 2 : 1
            score += points
            reward = (questionNumber, "+\(points)")
            Haptics.success()
        } else {
            combo = 0
            Haptics.error()
        }
        Task {
            try? await Task.sleep(for: .milliseconds(correct ? 250 : 550))
            flash = nil
            next()
        }
    }

    private func finish() {
        guard result == nil else { return }
        let stars = correctCount >= 25 ? 3 : correctCount >= 15 ? 2 : 1
        result = GameResult(stars: stars, headline: "\(score) puan",
                            detail: "\(asked) sorunun \(correctCount) tanesini bildiniz. Üst üste doğrular puanı katlar.")
    }
}

// MARK: - Dinle ve yaz

struct SpellingGame: View {
    let pool: [VocabularyCard]

    @State private var words: [VocabularyCard] = []
    @State private var index = 0
    @State private var input = ""
    @State private var score = 0
    @State private var combo = 0
    @State private var reveal: Bool?
    @State private var shakes = 0
    @State private var speaking = false
    @State private var result: GameResult?
    @FocusState private var focused: Bool

    var body: some View {
        GameShell(title: "Dinle ve yaz", color: Theme.success, result: result, onReplay: reset) {
            VStack(spacing: 22) {
                GameHUD(score: score, combo: combo, trailing: "\(min(index + 1, words.count))/\(words.count)")
                ProgressBar(value: Double(index) / Double(max(words.count, 1)), color: Theme.success, height: 10)
                if index < words.count {
                    let word = words[index]
                    Button { play(word.en) } label: {
                        Image(systemName: "speaker.wave.3.fill")
                            .font(.system(size: 40, weight: .semibold))
                            .symbolEffect(.variableColor.iterative, isActive: speaking)
                            .frame(width: 112, height: 112)
                            .foregroundStyle(.white)
                    }
                    .buttonStyle(RoundDepthButtonStyle(color: Theme.success))
                    .padding(.top, 10)
                    Label(word.tr, systemImage: "lightbulb.fill")
                        .font(.jakarta(.subheadline, weight: .semibold))
                        .foregroundStyle(.secondary)
                    if word.en.count <= 12 { letterSlots(for: word.en) }
                    TextField("Duyduğunuzu yazın", text: $input)
                        .font(.jakarta(.title3, weight: .bold))
                        .multilineTextAlignment(.center)
                        .textInputAutocapitalization(.never)
                        .autocorrectionDisabled()
                        .focused($focused)
                        .onSubmit(check)
                        .padding(16)
                        .background(Theme.surface, in: RoundedRectangle(cornerRadius: 16, style: .continuous))
                        .overlay(RoundedRectangle(cornerRadius: 16, style: .continuous)
                            .stroke(reveal == nil ? Color(uiColor: .systemGray4) : (reveal! ? Theme.success : Theme.danger), lineWidth: 2))
                        .shake(shakes)
                        .disabled(reveal != nil)
                    if let reveal {
                        Label(reveal ? "Doğru!" : "Doğrusu: \(word.en)",
                              systemImage: reveal ? "checkmark.circle.fill" : "xmark.circle.fill")
                            .font(.jakarta(.headline, weight: .heavy))
                            .foregroundStyle(reveal ? Theme.success : Theme.danger)
                            .transition(.scale.combined(with: .opacity))
                        Button("Devam", action: advance).buttonStyle(PrimaryButtonStyle(color: reveal ? Theme.success : Theme.danger))
                    } else {
                        Button("Kontrol et", action: check).buttonStyle(PrimaryButtonStyle(color: Theme.success)).disabled(input.isEmpty)
                    }
                    Spacer()
                }
            }
            .padding(20)
            .animation(Motion.pop, value: reveal)
            .onAppear {
                if let first = words.first { play(first.en) }
                focused = true
            }
        }
        .onAppear { if words.isEmpty { pickWords() } }
    }

    /// Kelimenin harf sayısını gösteren kutucuklar; yazdıkça dolar.
    private func letterSlots(for word: String) -> some View {
        let letters = Array(word)
        let typed = Array(input)
        return HStack(spacing: 5) {
            ForEach(letters.indices, id: \.self) { i in
                let filled = i < typed.count
                Text(filled ? String(typed[i]) : (letters[i] == " " ? " " : ""))
                    .font(.jakarta(.headline, weight: .heavy))
                    .frame(width: 24, height: 32)
                    .background(letters[i] == " " ? Color.clear : (filled ? Theme.success.opacity(0.15) : Color(uiColor: .systemGray6)),
                                in: RoundedRectangle(cornerRadius: 6))
                    .scaleEffect(filled ? 1 : 0.92)
                    .animation(Motion.pop, value: filled)
            }
        }
        .accessibilityHidden(true)
    }

    private func pickWords() {
        // Tek kelimelik kartlar tercih edilir; yazması makul uzunlukta olsun.
        let single = pool.filter { !$0.en.contains(" ") && $0.en.count <= 12 }
        words = Array((single.count >= GameRules.spellingWords ? single : pool).shuffled().prefix(GameRules.spellingWords))
    }

    private func reset() {
        index = 0
        score = 0
        combo = 0
        input = ""
        reveal = nil
        result = nil
        pickWords()
    }

    private func play(_ text: String) {
        Speech.shared.speak(text, rate: 0.4)
        speaking = true
        Task { try? await Task.sleep(for: .seconds(1.2)); speaking = false }
    }

    private func check() {
        guard reveal == nil, !input.isEmpty else { return }
        let correct = AnswerChecker.matches(input, accepted: [words[index].en])
        if correct {
            score += 1
            combo += 1
            Haptics.success()
        } else {
            combo = 0
            shakes += 1
            Haptics.error()
        }
        reveal = correct
    }

    private func advance() {
        reveal = nil
        input = ""
        index += 1
        if index < words.count {
            play(words[index].en)
            focused = true
        } else {
            let stars = score >= 9 ? 3 : score >= 7 ? 2 : 1
            result = GameResult(stars: stars, headline: "\(score)/\(words.count)", detail: "Kelimeleri doğru yazdınız.")
        }
    }
}

import SwiftUI
import JECore

enum GameRules {
    static let minimumCards = 8
    static let matchRaceRounds = 3
    static let matchRacePairs = 5
    static let speedQuizSeconds = 60
    static let spellingWords = 10
}

/// Oyunların ortak kabuğu: başlık, kapatma düğmesi ve bitiş ekranı.
struct GameShell<Content: View>: View {
    let title: String
    let finished: Bool
    let score: String
    let detail: String
    let won: Bool
    @ViewBuilder let content: () -> Content

    @Environment(AppModel.self) private var model
    @Environment(\.dismiss) private var dismiss
    @State private var awarded = false

    var body: some View {
        VStack(spacing: 0) {
            HStack {
                Button { dismiss() } label: { Image(systemName: "xmark").font(.jakarta(.headline, weight: .bold)) }
                    .foregroundStyle(.secondary)
                Spacer()
                Text(title).font(.jakarta(.headline))
                Spacer()
                Color.clear.frame(width: 20, height: 1)
            }
            .padding(.horizontal, 20)
            .padding(.vertical, 12)
            if finished {
                VStack(spacing: 16) {
                    Spacer()
                    Image(systemName: won ? "trophy.fill" : "flag.checkered")
                        .font(.system(size: 80))
                        .foregroundStyle(won ? Theme.warning : Theme.accent)
                    Text(score).font(.jakarta(.largeTitle, weight: .bold))
                    Text(detail).font(.jakarta(.body)).foregroundStyle(.secondary).multilineTextAlignment(.center)
                    if won { Text("+\(XPRule.gameWin) XP").font(.jakarta(.headline)).foregroundStyle(Theme.success) }
                    Spacer()
                    Button("Bitir") { dismiss() }.buttonStyle(.primary)
                }
                .padding(20)
                .onAppear {
                    guard won, !awarded else { return }
                    awarded = true
                    model.award(xp: XPRule.gameWin)
                }
            } else {
                content()
            }
        }
        .background(Theme.background)
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
    @State private var mistakes = 0
    @State private var start = Date.now
    @State private var elapsed: TimeInterval = 0
    @State private var finished = false

    var body: some View {
        GameShell(title: "Eşleştirme yarışı", finished: finished,
                  score: String(format: "%.1f sn", elapsed),
                  detail: "\(GameRules.matchRaceRounds * GameRules.matchRacePairs) eşleştirme, \(mistakes) hata.",
                  won: mistakes <= 2) {
            VStack(spacing: 16) {
                HStack {
                    Text("Tur \(round + 1)/\(GameRules.matchRaceRounds)").font(.jakarta(.subheadline, weight: .semibold))
                    Spacer()
                    TimelineView(.periodic(from: .now, by: 0.1)) { context in
                        Text(String(format: "%.1f", context.date.timeIntervalSince(start)))
                            .font(.jakarta(.headline, weight: .bold))
                            .monospacedDigit()
                    }
                }
                HStack(alignment: .top, spacing: 12) {
                    VStack(spacing: 10) {
                        ForEach(cards.indices, id: \.self) { i in
                            cell(cards[i].en, color: matched.contains(i) ? Theme.success : (selected == i ? Theme.accent : nil),
                                 done: matched.contains(i)) { selected = i; Haptics.tap() }
                        }
                    }
                    VStack(spacing: 10) {
                        ForEach(rightOrder, id: \.self) { i in
                            cell(cards[i].tr, color: matched.contains(i) ? Theme.success : (wrong == i ? Theme.danger : nil),
                                 done: matched.contains(i)) { pick(i) }
                        }
                    }
                }
                Spacer()
            }
            .padding(20)
        }
        .onAppear { if cards.isEmpty { newRound(); start = .now } }
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
            matched.insert(i)
            selected = nil
            Haptics.success()
            if matched.count == cards.count {
                if round + 1 < GameRules.matchRaceRounds {
                    round += 1
                    newRound()
                } else {
                    elapsed = Date.now.timeIntervalSince(start)
                    finished = true
                }
            }
        } else {
            mistakes += 1
            wrong = i
            Haptics.error()
            Task { try? await Task.sleep(for: .milliseconds(400)); wrong = nil }
        }
    }

    private func cell(_ text: String, color: Color?, done: Bool, action: @escaping () -> Void) -> some View {
        Button(action: action) {
            Text(text)
                .font(.jakarta(.callout, weight: .semibold))
                .multilineTextAlignment(.center)
                .minimumScaleFactor(0.7)
                .frame(maxWidth: .infinity, minHeight: 60)
                .padding(.horizontal, 6)
                .background((color ?? .clear).opacity(0.12), in: RoundedRectangle(cornerRadius: 12))
                .background(Theme.surface, in: RoundedRectangle(cornerRadius: 12))
                .overlay(RoundedRectangle(cornerRadius: 12).stroke(color ?? Color.secondary.opacity(0.25), lineWidth: 2))
                .opacity(done ? 0.45 : 1)
        }
        .buttonStyle(.plain)
        .disabled(done)
    }
}

// MARK: - 60 saniye

struct SpeedQuizGame: View {
    let pool: [VocabularyCard]

    @State private var deadline = Date.now.addingTimeInterval(TimeInterval(GameRules.speedQuizSeconds))
    @State private var question: VocabularyCard?
    @State private var options: [String] = []
    @State private var score = 0
    @State private var asked = 0
    @State private var flash: Color?
    @State private var finished = false

    var body: some View {
        GameShell(title: "60 saniye", finished: finished, score: "\(score) doğru",
                  detail: "\(asked) sorunun \(score) tanesini bildiniz.", won: score >= 15) {
            VStack(spacing: 24) {
                TimelineView(.periodic(from: .now, by: 0.2)) { context in
                    let left = max(0, deadline.timeIntervalSince(context.date))
                    VStack(spacing: 6) {
                        ProgressBar(value: left / Double(GameRules.speedQuizSeconds),
                                    color: left < 10 ? Theme.danger : Theme.accent, height: 10)
                        HStack {
                            Text("\(Int(left.rounded(.up))) sn").font(.jakarta(.headline, weight: .bold)).monospacedDigit()
                            Spacer()
                            Text("Skor: \(score)").font(.jakarta(.headline, weight: .bold))
                        }
                    }
                    .onChange(of: left == 0) { _, over in if over { finished = true } }
                }
                Spacer()
                if let question {
                    Text(question.en)
                        .font(.jakarta(.largeTitle, weight: .bold))
                        .multilineTextAlignment(.center)
                        .minimumScaleFactor(0.5)
                        .padding(.vertical, 30)
                        .frame(maxWidth: .infinity)
                        .background((flash ?? Theme.surface).opacity(flash == nil ? 1 : 0.2), in: RoundedRectangle(cornerRadius: 20))
                }
                Spacer()
                VStack(spacing: 10) {
                    ForEach(options, id: \.self) { option in
                        Button { answer(option) } label: {
                            Text(option)
                                .font(.jakarta(.body, weight: .semibold))
                                .frame(maxWidth: .infinity, minHeight: 52)
                                .background(Theme.surface, in: RoundedRectangle(cornerRadius: 14))
                                .overlay(RoundedRectangle(cornerRadius: 14).stroke(Color.secondary.opacity(0.2), lineWidth: 2))
                        }
                        .buttonStyle(.plain)
                    }
                }
            }
            .padding(20)
        }
        .onAppear { if question == nil { deadline = .now.addingTimeInterval(TimeInterval(GameRules.speedQuizSeconds)); next() } }
    }

    private func next() {
        guard let card = pool.randomElement() else { return }
        let distractors = Set(pool.map(\.tr)).subtracting([card.tr]).shuffled().prefix(3)
        question = card
        options = (distractors + [card.tr]).shuffled()
    }

    private func answer(_ option: String) {
        guard !finished, let question else { return }
        asked += 1
        if option == question.tr {
            score += 1
            flash = Theme.success
            Haptics.success()
        } else {
            flash = Theme.danger
            Haptics.error()
        }
        Task { try? await Task.sleep(for: .milliseconds(200)); flash = nil }
        next()
    }
}

// MARK: - Dinle ve yaz

struct SpellingGame: View {
    let pool: [VocabularyCard]

    @State private var words: [VocabularyCard] = []
    @State private var index = 0
    @State private var input = ""
    @State private var score = 0
    @State private var reveal: Bool?
    @FocusState private var focused: Bool

    private var finished: Bool { !words.isEmpty && index >= words.count }

    var body: some View {
        GameShell(title: "Dinle ve yaz", finished: finished, score: "\(score)/\(words.count)",
                  detail: "Kelimeleri doğru yazdınız.", won: score >= words.count * 7 / 10) {
            VStack(spacing: 20) {
                Text("\(min(index + 1, words.count))/\(words.count)")
                    .font(.jakarta(.subheadline, weight: .semibold))
                    .foregroundStyle(.secondary)
                if index < words.count {
                    let word = words[index]
                    Button { Speech.shared.speak(word.en, rate: 0.4) } label: {
                        Image(systemName: "speaker.wave.3.fill")
                            .font(.system(size: 36))
                            .frame(width: 100, height: 100)
                            .background(Theme.accent, in: Circle())
                            .foregroundStyle(.white)
                    }
                    Text("İpucu: \(word.tr)").font(.jakarta(.subheadline)).foregroundStyle(.secondary)
                    TextField("Duyduğunuzu yazın", text: $input)
                        .font(.jakarta(.title3))
                        .multilineTextAlignment(.center)
                        .textInputAutocapitalization(.never)
                        .autocorrectionDisabled()
                        .focused($focused)
                        .onSubmit(check)
                        .padding(16)
                        .background(Theme.surface, in: RoundedRectangle(cornerRadius: 14))
                        .disabled(reveal != nil)
                    if let reveal {
                        Label(reveal ? "Doğru!" : "Doğrusu: \(word.en)",
                              systemImage: reveal ? "checkmark.circle.fill" : "xmark.circle.fill")
                            .font(.jakarta(.headline))
                            .foregroundStyle(reveal ? Theme.success : Theme.danger)
                        Button("Devam") {
                            self.reveal = nil
                            input = ""
                            index += 1
                            if index < words.count { Speech.shared.speak(words[index].en, rate: 0.4); focused = true }
                        }
                        .buttonStyle(.primary)
                    } else {
                        Button("Kontrol et", action: check).buttonStyle(.primary).disabled(input.isEmpty)
                    }
                    Spacer()
                }
            }
            .padding(20)
        }
        .onAppear {
            guard words.isEmpty else { return }
            // Tek kelimelik kartlar tercih edilir; yazması makul uzunlukta olsun.
            let single = pool.filter { !$0.en.contains(" ") && $0.en.count <= 12 }
            words = Array((single.count >= GameRules.spellingWords ? single : pool).shuffled().prefix(GameRules.spellingWords))
            if let first = words.first { Speech.shared.speak(first.en, rate: 0.4) }
            focused = true
        }
    }

    private func check() {
        guard reveal == nil, !input.isEmpty else { return }
        let correct = AnswerChecker.matches(input, accepted: [words[index].en])
        if correct { score += 1; Haptics.success() } else { Haptics.error() }
        reveal = correct
    }
}

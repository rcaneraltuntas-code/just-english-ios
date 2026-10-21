import SwiftUI
import JECore

/// Bir alıştırmanın sonucu. Konuşma ve yazma görevlerinde `correct` nil'dir: öğrenci kendini değerlendirir.
struct ExerciseOutcome: Equatable {
    var correct: Bool?
    var message: String?
    var correctAnswer: String?
}

/// Her alıştırma türünü çizer, cevabı kontrol eder ve geri bildirimi gösterir.
/// `onContinue` öğrenci "Devam" dediğinde sonucu bildirir. Çağıran taraf her yeni soru için `.id` vermelidir.
struct ExerciseView: View {
    let exercise: Exercise
    var showsFeedback = true
    let onContinue: (ExerciseOutcome) -> Void

    @State private var outcome: ExerciseOutcome?
    @State private var wrongShakes = 0

    var body: some View {
        VStack(spacing: 0) {
            ScrollView {
                content
                    .padding(20)
                    .disabled(outcome != nil && exercise.isAutoGraded)
                    .shake(wrongShakes)
            }
            .scrollDismissesKeyboard(.interactively)
            if let outcome {
                FeedbackPanel(outcome: outcome, showsFeedback: showsFeedback) {
                    onContinue(outcome)
                }
                .transition(.move(edge: .bottom))
                .zIndex(1)
            }
        }
        .overlay(alignment: .bottom) {
            if showsFeedback, outcome?.correct == true {
                FloatingReward(text: "+\(XPRule.correctAnswer) XP")
                    .padding(.bottom, 200)
            }
        }
        .animation(Motion.smooth, value: outcome)
    }

    private func submit(_ result: ExerciseOutcome) {
        guard outcome == nil else { return }
        if let correct = result.correct {
            if correct { Haptics.success() } else { Haptics.error(); wrongShakes += 1 }
        }
        if !showsFeedback && exercise.isAutoGraded {
            onContinue(result)
        } else {
            outcome = result
        }
    }

    @ViewBuilder private var content: some View {
        switch exercise {
        case let .multipleChoice(_, prompt, options, answerIndex, explanation, wrongFeedback):
            ChoiceExercise(prompt: prompt, audioText: nil, options: options, answerIndex: answerIndex,
                           locked: outcome != nil) { chosen in
                let correct = chosen == answerIndex
                submit(.init(correct: correct, message: correct ? explanation : (wrongFeedback[chosen] ?? explanation),
                             correctAnswer: correct ? nil : options[answerIndex]))
            }
        case let .listening(_, audioText, prompt, options, answerIndex, explanation):
            ChoiceExercise(prompt: prompt, audioText: audioText, options: options, answerIndex: answerIndex,
                           locked: outcome != nil) { chosen in
                let correct = chosen == answerIndex
                submit(.init(correct: correct, message: explanation + "\n\n🔊 \"\(audioText)\"",
                             correctAnswer: correct ? nil : options[answerIndex]))
            }
        case let .gapFill(_, text, answers, explanation, hint):
            GapFillExercise(text: text, hint: hint) { input in
                let correct = AnswerChecker.matches(input, accepted: answers)
                submit(.init(correct: correct, message: explanation, correctAnswer: correct ? nil : answers[0]))
            }
        case let .typeAnswer(_, prompt, accepted, explanation):
            TypeAnswerExercise(prompt: prompt) { input in
                let correct = AnswerChecker.matches(input, accepted: accepted)
                submit(.init(correct: correct, message: explanation, correctAnswer: correct ? nil : accepted[0]))
            }
        case let .ordering(_, words, answer, explanation, translation):
            OrderingExercise(words: words, translation: translation) { chosen in
                let correct = AnswerChecker.ordering(chosen, answer: answer)
                submit(.init(correct: correct, message: explanation, correctAnswer: correct ? nil : answer))
            }
        case let .matching(_, pairs, explanation):
            MatchingExercise(pairs: pairs) { mistakes in
                submit(.init(correct: mistakes == 0,
                             message: mistakes == 0 ? explanation : "\(mistakes) yanlış eşleştirme. " + explanation))
            }
        case let .speaking(_, prompt, modelAnswer, rubric):
            SpeakingExercise(prompt: prompt, modelAnswer: modelAnswer, rubric: rubric, done: outcome != nil) {
                submit(.init(correct: nil, message: nil))
            }
        case let .writing(_, prompt, modelAnswer, rubric):
            WritingExercise(prompt: prompt, modelAnswer: modelAnswer, rubric: rubric, done: outcome != nil) {
                submit(.init(correct: nil, message: nil))
            }
        }
    }
}

// MARK: - Geri bildirim

struct FeedbackPanel: View {
    let outcome: ExerciseOutcome
    let showsFeedback: Bool
    let onContinue: () -> Void

    @State private var iconScale: CGFloat = 0.2

    private var color: Color {
        switch outcome.correct {
        case true?: Theme.success
        case false?: Theme.danger
        case nil: Theme.accent
        }
    }

    /// Doğru cevapta her seferinde aynı söz tekrarlanmasın diye küçük bir havuz.
    private static let praise = ["Harika!", "Doğru!", "Süper!", "Mükemmel!", "Aynen öyle!", "Çok iyi!"]
    @State private var title = FeedbackPanel.praise.randomElement() ?? "Doğru!"
    @State private var wrongTitle = ["Olmadı, ama sorun değil", "Neredeyse!", "Bir dahakine!"].randomElement() ?? "Doğru değil"
    @State private var hop = 0

    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            if showsFeedback, let correct = outcome.correct {
                HStack(spacing: 12) {
                    JAIView(mood: correct ? .happy : .sad, size: 56, color: color, bounceTrigger: hop)
                        .frame(width: 56, height: 56)
                        .scaleEffect(iconScale)
                    Text(correct ? title : wrongTitle)
                        .font(.jakarta(.title2, weight: .heavy))
                        .foregroundStyle(color)
                }
                if let answer = outcome.correctAnswer {
                    VStack(alignment: .leading, spacing: 2) {
                        Text("Doğru cevap").font(.jakarta(.caption, weight: .bold)).foregroundStyle(color)
                        Text(answer).font(.jakarta(.headline))
                    }
                }
                if let message = outcome.message, !message.isEmpty {
                    Text(message)
                        .font(.jakarta(.callout))
                        .foregroundStyle(.secondary)
                        .fixedSize(horizontal: false, vertical: true)
                }
            }
            Button("Devam", action: onContinue)
                .buttonStyle(PrimaryButtonStyle(color: color))
                .padding(.top, 4)
        }
        .padding(20)
        .padding(.bottom, 4)
        .frame(maxWidth: .infinity, alignment: .leading)
        .background(color.opacity(0.12))
        .background(.background)
        .overlay(alignment: .top) { Rectangle().fill(color.opacity(0.35)).frame(height: 2) }
        .onAppear {
            withAnimation(Motion.pop.delay(0.05)) { iconScale = 1 }
            if outcome.correct == true { hop += 1 }
        }
    }
}

// MARK: - Çoktan seçmeli ve dinleme

struct ChoiceExercise: View {
    let prompt: String
    let audioText: String?
    let options: [String]
    let answerIndex: Int
    let locked: Bool
    let onChoose: (Int) -> Void

    @State private var chosen: Int?
    @State private var speaking = false

    var body: some View {
        VStack(alignment: .leading, spacing: 20) {
            if let audioText {
                HStack(spacing: 18) {
                    Button { play(audioText, rate: 0.45) } label: {
                        Image(systemName: "speaker.wave.3.fill")
                            .font(.system(size: 34, weight: .semibold))
                            .symbolEffect(.variableColor.iterative, isActive: speaking)
                            .frame(width: 96, height: 96)
                            .foregroundStyle(.white)
                    }
                    .buttonStyle(RoundDepthButtonStyle(color: Theme.accent))
                    Button { play(audioText, rate: 0.3) } label: {
                        Image(systemName: "tortoise.fill")
                            .font(.system(size: 22, weight: .semibold))
                            .frame(width: 60, height: 60)
                            .foregroundStyle(Theme.accent)
                    }
                    .buttonStyle(RoundDepthButtonStyle(color: Theme.surfaceRaised))
                    .accessibilityLabel("Yavaş dinle")
                }
                .frame(maxWidth: .infinity)
                .onAppear { play(audioText, rate: 0.45) }
            }
            Text(prompt)
                .font(.jakarta(.title3, weight: .bold))
                .fixedSize(horizontal: false, vertical: true)
            VStack(spacing: 8) {
                ForEach(Array(options.enumerated()), id: \.offset) { index, option in
                    Button {
                        guard !locked else { return }
                        Haptics.tap()
                        withAnimation(Motion.press) { chosen = index }
                    } label: {
                        HStack(spacing: 14) {
                            Text(["A", "B", "C", "D", "E", "F"][min(index, 5)])
                                .font(.jakarta(.subheadline, weight: .heavy))
                                .foregroundStyle(tint(for: index) == nil ? Color.secondary : .white)
                                .frame(width: 30, height: 30)
                                .background(tint(for: index) ?? Color.secondary.opacity(0.12), in: RoundedRectangle(cornerRadius: 8))
                            Text(option)
                                .font(.jakarta(.body, weight: .semibold))
                                .multilineTextAlignment(.leading)
                                .frame(maxWidth: .infinity, alignment: .leading)
                            if locked && index == answerIndex {
                                Image(systemName: "checkmark.circle.fill").foregroundStyle(Theme.success).transition(.scale)
                            }
                        }
                        .padding(14)
                    }
                    .buttonStyle(TileButtonStyle(highlight: tint(for: index)))
                    .scaleEffect(locked && index == answerIndex ? 1.02 : 1)
                    .staggeredAppear(index)
                }
            }
            if !locked {
                Button("Kontrol et") {
                    if let chosen { onChoose(chosen) }
                }
                .buttonStyle(.primary)
                .disabled(chosen == nil)
                .padding(.top, 4)
            }
        }
        .animation(Motion.pop, value: locked)
    }

    private func play(_ text: String, rate: Float) {
        Speech.shared.speak(text, rate: rate)
        speaking = true
        Task {
            try? await Task.sleep(for: .seconds(Double(text.count) / (rate > 0.4 ? 14 : 9)))
            speaking = false
        }
    }

    private func tint(for index: Int) -> Color? {
        if locked {
            if index == answerIndex { return Theme.success }
            if index == chosen { return Theme.danger }
            return nil
        }
        return index == chosen ? Theme.accent : nil
    }
}

/// Yuvarlak 3D düğme (ses çal, mikrofon).
struct RoundDepthButtonStyle: ButtonStyle {
    var color: Color

    func makeBody(configuration: Configuration) -> some View {
        let pressed = configuration.isPressed
        return configuration.label
            .background(color, in: Circle())
            .background(Circle().fill(color.blended(with: .black, amount: 0.25)).offset(y: pressed ? 0 : 5))
            .offset(y: pressed ? 5 : 0)
            .padding(.bottom, 5)
            .animation(Motion.press, value: pressed)
    }
}

// MARK: - Boşluk doldurma ve yazarak cevap

struct GapFillExercise: View {
    let text: String
    let hint: String?
    let onSubmit: (String) -> Void

    @State private var input = ""
    @FocusState private var focused: Bool

    private var parts: [String] { text.components(separatedBy: "___") }

    var body: some View {
        VStack(alignment: .leading, spacing: 20) {
            Text("Boşluğu doldurun")
                .font(.jakarta(.subheadline, weight: .semibold))
                .foregroundStyle(.secondary)
            (Text(parts.first ?? "")
             + Text(input.isEmpty ? " ______ " : " \(input) ").foregroundColor(Theme.accent).bold()
             + Text(parts.dropFirst().joined(separator: "___")))
                .font(.jakarta(.title3, weight: .medium))
                .fixedSize(horizontal: false, vertical: true)
            if let hint {
                Label(hint, systemImage: "lightbulb.fill")
                    .font(.jakarta(.subheadline))
                    .foregroundStyle(Theme.warning)
            }
            AnswerField(input: $input, focused: $focused, onSubmit: submit)
            Button("Kontrol et", action: submit)
                .buttonStyle(.primary)
                .disabled(input.trimmingCharacters(in: .whitespaces).isEmpty)
        }
        .onAppear { focused = true }
    }

    private func submit() {
        guard !input.trimmingCharacters(in: .whitespaces).isEmpty else { return }
        focused = false
        onSubmit(input)
    }
}

struct TypeAnswerExercise: View {
    let prompt: String
    let onSubmit: (String) -> Void

    @State private var input = ""
    @FocusState private var focused: Bool

    var body: some View {
        VStack(alignment: .leading, spacing: 20) {
            Text(prompt)
                .font(.jakarta(.title3, weight: .semibold))
                .fixedSize(horizontal: false, vertical: true)
            AnswerField(input: $input, focused: $focused, onSubmit: submit)
            Button("Kontrol et", action: submit)
                .buttonStyle(.primary)
                .disabled(input.trimmingCharacters(in: .whitespaces).isEmpty)
        }
        .onAppear { focused = true }
    }

    private func submit() {
        guard !input.trimmingCharacters(in: .whitespaces).isEmpty else { return }
        focused = false
        onSubmit(input)
    }
}

struct AnswerField: View {
    @Binding var input: String
    var focused: FocusState<Bool>.Binding
    let onSubmit: () -> Void

    var body: some View {
        TextField("Cevabınız", text: $input)
            .font(.jakarta(.title3))
            .textInputAutocapitalization(.never)
            .autocorrectionDisabled()
            .submitLabel(.done)
            .focused(focused)
            .onSubmit(onSubmit)
            .padding(16)
            .background(Theme.surface, in: RoundedRectangle(cornerRadius: 14))
            .overlay(RoundedRectangle(cornerRadius: 14).stroke(Theme.accent.opacity(0.3)))
    }
}

// MARK: - Cümle kurma

struct OrderingExercise: View {
    let words: [String]
    let translation: String?
    let onSubmit: ([String]) -> Void

    /// Kelimelerin `words` içindeki indeksleri; aynı kelime iki kez geçebilir.
    @State private var chosen: [Int] = []
    @Namespace private var tiles

    var body: some View {
        VStack(alignment: .leading, spacing: 20) {
            Text("Cümleyi kurun")
                .font(.jakarta(.subheadline, weight: .bold))
                .foregroundStyle(Theme.accent)
            if let translation {
                HStack(alignment: .top, spacing: 10) {
                    Image(systemName: "text.bubble.fill").foregroundStyle(Theme.accent)
                    Text(translation).font(.jakarta(.title3, weight: .bold))
                }
            }
            // Cevap alanı: çizgili satırlar üzerinde seçilen kelimeler.
            FlowLayout(spacing: 8) {
                ForEach(chosen, id: \.self) { index in
                    tile(words[index]) { chosen.removeAll { $0 == index } }
                        .matchedGeometryEffect(id: index, in: tiles)
                }
            }
            .frame(maxWidth: .infinity, minHeight: 120, alignment: .topLeading)
            .padding(.vertical, 8)
            .background(alignment: .top) {
                VStack(spacing: 52) {
                    ForEach(0..<3, id: \.self) { _ in Rectangle().fill(Color.secondary.opacity(0.18)).frame(height: 2) }
                }
                .padding(.top, 52)
            }

            // Kelime bankası: seçilen kelimenin yerinde gri bir boşluk kalır.
            FlowLayout(spacing: 8) {
                ForEach(Array(words.enumerated()), id: \.offset) { index, word in
                    ZStack {
                        Text(word)
                            .font(.jakarta(.body, weight: .bold))
                            .padding(.horizontal, 14)
                            .padding(.vertical, 11)
                            .foregroundStyle(.clear)
                            .background(Color.secondary.opacity(0.12), in: RoundedRectangle(cornerRadius: 12, style: .continuous))
                            .padding(.bottom, 4)
                        if !chosen.contains(index) {
                            tile(word) { chosen.append(index) }
                                .matchedGeometryEffect(id: index, in: tiles)
                        }
                    }
                }
            }
            .frame(maxWidth: .infinity)
            Button("Kontrol et") { onSubmit(chosen.map { words[$0] }) }
                .buttonStyle(.primary)
                .disabled(chosen.count != words.count)
        }
    }

    private func tile(_ word: String, action: @escaping () -> Void) -> some View {
        Button {
            Haptics.tap()
            withAnimation(Motion.smooth) { action() }
        } label: {
            Text(word)
                .font(.jakarta(.body, weight: .bold))
                .padding(.horizontal, 14)
                .padding(.vertical, 11)
        }
        .buttonStyle(TileButtonStyle())
    }
}

// MARK: - Eşleştirme

struct MatchingExercise: View {
    let pairs: [MatchPair]
    let onFinish: (Int) -> Void

    @State private var rightOrder: [Int] = []
    @State private var selectedLeft: Int?
    @State private var matched: Set<Int> = []
    @State private var wrongFlash: Int?
    @State private var mistakes = 0

    var body: some View {
        VStack(alignment: .leading, spacing: 20) {
            Text("Eşleştirin")
                .font(.jakarta(.subheadline, weight: .semibold))
                .foregroundStyle(.secondary)
            HStack(alignment: .top, spacing: 12) {
                VStack(spacing: 10) {
                    ForEach(pairs.indices, id: \.self) { i in
                        cell(pairs[i].left, state: state(left: i)) {
                            selectedLeft = i
                            Haptics.tap()
                        }
                    }
                }
                VStack(spacing: 10) {
                    ForEach(rightOrder, id: \.self) { i in
                        cell(pairs[i].right, state: state(right: i)) { chooseRight(i) }
                    }
                }
            }
        }
        .onAppear { if rightOrder.isEmpty { rightOrder = Array(pairs.indices).shuffled() } }
    }

    private enum CellState { case normal, selected, matched, wrong }

    private func state(left i: Int) -> CellState {
        if matched.contains(i) { return .matched }
        return selectedLeft == i ? .selected : .normal
    }

    private func state(right i: Int) -> CellState {
        if matched.contains(i) { return .matched }
        return wrongFlash == i ? .wrong : .normal
    }

    private func chooseRight(_ i: Int) {
        guard let left = selectedLeft else { return }
        if left == i {
            matched.insert(i)
            selectedLeft = nil
            Haptics.success()
            if matched.count == pairs.count { onFinish(mistakes) }
        } else {
            mistakes += 1
            wrongFlash = i
            Haptics.error()
            Task {
                try? await Task.sleep(for: .milliseconds(450))
                wrongFlash = nil
            }
        }
    }

    private func cell(_ text: String, state: CellState, action: @escaping () -> Void) -> some View {
        let color: Color? = switch state {
        case .normal: nil
        case .selected: Theme.accent
        case .matched: Theme.success
        case .wrong: Theme.danger
        }
        return Button(action: action) {
            Text(text)
                .font(.jakarta(.callout, weight: .bold))
                .multilineTextAlignment(.center)
                .minimumScaleFactor(0.7)
                .frame(maxWidth: .infinity, minHeight: 58)
                .padding(.horizontal, 8)
        }
        .buttonStyle(TileButtonStyle(highlight: color))
        .opacity(state == .matched ? 0.45 : 1)
        .scaleEffect(state == .selected ? 1.03 : (state == .matched ? 0.96 : 1))
        .modifier(ShakeEffect(travel: 6, animatableData: state == .wrong ? 1 : 0))
        .animation(state == .wrong ? .linear(duration: 0.35) : Motion.pop, value: state)
        .disabled(state == .matched)
    }
}

// MARK: - Konuşma ve yazma

struct SpeakingExercise: View {
    let prompt: String
    let modelAnswer: String
    let rubric: [String]
    let done: Bool
    let onDone: () -> Void

    @State private var recognizer = SpeechRecognizer()
    @State private var revealed = false

    var body: some View {
        VStack(alignment: .leading, spacing: 20) {
            Label("Konuşma", systemImage: "mic.fill")
                .font(.jakarta(.subheadline, weight: .bold))
                .foregroundStyle(Theme.accent)
            JAISays(text: prompt, mood: recognizer.status == .recording ? .thinking : .talking, size: 64)

            VStack(spacing: 12) {
                Button {
                    Task { await recognizer.toggle() }
                } label: {
                    Image(systemName: recognizer.status == .recording ? "stop.fill" : "mic.fill")
                        .font(.system(size: 32, weight: .bold))
                        .frame(width: 92, height: 92)
                        .foregroundStyle(.white)
                        .symbolEffect(.pulse, isActive: recognizer.status == .recording)
                }
                .buttonStyle(RoundDepthButtonStyle(color: recognizer.status == .recording ? Theme.danger : Theme.accent))
                .background {
                    if recognizer.status == .recording {
                        // Kayıt sırasında dışa doğru yayılan halkalar.
                        TimelineView(.animation) { timeline in
                            let t = timeline.date.timeIntervalSinceReferenceDate
                            ZStack {
                                ForEach(0..<3, id: \.self) { i in
                                    let p = (t * 0.8 + Double(i) / 3).truncatingRemainder(dividingBy: 1)
                                    Circle()
                                        .stroke(Theme.danger.opacity(0.5 * (1 - p)), lineWidth: 3)
                                        .frame(width: 92 + 70 * p, height: 92 + 70 * p)
                                }
                            }
                        }
                        .offset(y: -2)
                    }
                }
                Text(statusText)
                    .font(.jakarta(.footnote))
                    .foregroundStyle(.secondary)
                    .multilineTextAlignment(.center)
            }
            .frame(maxWidth: .infinity)

            if !recognizer.transcript.isEmpty {
                VStack(alignment: .leading, spacing: 6) {
                    Text("Söyledikleriniz").font(.jakarta(.caption, weight: .bold)).foregroundStyle(.secondary)
                    Text(recognizer.transcript).font(.jakarta(.body))
                }
                .card()
            }

            if revealed {
                SelfCheckPanel(modelAnswer: modelAnswer, rubric: rubric, speakable: true)
                if !done {
                    Button("Tamamladım", action: onDone).buttonStyle(.primary)
                }
            } else {
                Button("Örnek cevabı göster") {
                    recognizer.stop()
                    revealed = true
                }
                .buttonStyle(.secondary)
            }
        }
        .onDisappear { recognizer.stop() }
    }

    private var statusText: String {
        switch recognizer.status {
        case .idle: "Mikrofona dokunun ve cevabınızı İngilizce söyleyin."
        case .recording: "Dinliyorum… Bitince durdurun."
        case .denied: "Mikrofon izni yok. Cevabınızı yine de sesli söyleyip örnekle karşılaştırabilirsiniz."
        case .unavailable: "Ses tanıma şu an kullanılamıyor. Cevabınızı sesli söyleyip örnekle karşılaştırın."
        }
    }
}

struct WritingExercise: View {
    let prompt: String
    let modelAnswer: String
    let rubric: [String]
    let done: Bool
    let onDone: () -> Void

    @State private var text = ""
    @State private var revealed = false

    private var wordCount: Int { text.split(whereSeparator: \.isWhitespace).count }

    var body: some View {
        VStack(alignment: .leading, spacing: 20) {
            Label("Yazma", systemImage: "pencil")
                .font(.jakarta(.subheadline, weight: .semibold))
                .foregroundStyle(.secondary)
            Text(prompt)
                .font(.jakarta(.title3, weight: .semibold))
                .fixedSize(horizontal: false, vertical: true)
            TextEditor(text: $text)
                .font(.jakarta(.body))
                .frame(minHeight: 180)
                .padding(10)
                .scrollContentBackground(.hidden)
                .background(Theme.surface, in: RoundedRectangle(cornerRadius: 14))
                .overlay(RoundedRectangle(cornerRadius: 14).stroke(Theme.accent.opacity(0.3)))
                .textInputAutocapitalization(.sentences)
            Text("\(wordCount) kelime")
                .font(.jakarta(.footnote))
                .foregroundStyle(.secondary)
                .frame(maxWidth: .infinity, alignment: .trailing)

            if revealed {
                SelfCheckPanel(modelAnswer: modelAnswer, rubric: rubric, speakable: false)
                if !done {
                    Button("Tamamladım", action: onDone).buttonStyle(.primary)
                }
            } else {
                Button("Örnek cevapla karşılaştır") { revealed = true }
                    .buttonStyle(.secondary)
                    .disabled(wordCount < 3)
            }
        }
    }
}

/// Örnek cevap ve öğrencinin işaretleyeceği kontrol listesi.
struct SelfCheckPanel: View {
    let modelAnswer: String
    let rubric: [String]
    let speakable: Bool

    @State private var checked: Set<Int> = []

    var body: some View {
        VStack(alignment: .leading, spacing: 14) {
            HStack {
                Text("Örnek cevap").font(.jakarta(.headline))
                Spacer()
                if speakable { SpeakButton(text: modelAnswer) }
            }
            Text(modelAnswer)
                .font(.jakarta(.body))
                .fixedSize(horizontal: false, vertical: true)
            Divider()
            Text("Kendinizi kontrol edin").font(.jakarta(.headline))
            ForEach(Array(rubric.enumerated()), id: \.offset) { index, item in
                Button {
                    if checked.contains(index) { checked.remove(index) } else { checked.insert(index) }
                    Haptics.tap()
                } label: {
                    Label {
                        Text(item).font(.jakarta(.callout)).multilineTextAlignment(.leading)
                    } icon: {
                        Image(systemName: checked.contains(index) ? "checkmark.square.fill" : "square")
                            .foregroundStyle(checked.contains(index) ? Theme.success : .secondary)
                    }
                }
                .buttonStyle(.plain)
            }
        }
        .card()
    }
}

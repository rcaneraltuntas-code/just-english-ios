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

    var body: some View {
        VStack(spacing: 0) {
            ScrollView {
                content
                    .padding(20)
                    .disabled(outcome != nil && exercise.isAutoGraded)
            }
            .scrollDismissesKeyboard(.interactively)
            if let outcome {
                FeedbackPanel(outcome: outcome, showsFeedback: showsFeedback) {
                    onContinue(outcome)
                }
                .transition(.move(edge: .bottom).combined(with: .opacity))
            }
        }
        .animation(.snappy, value: outcome)
    }

    private func submit(_ result: ExerciseOutcome) {
        guard outcome == nil else { return }
        if let correct = result.correct { correct ? Haptics.success() : Haptics.error() }
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

    private var color: Color {
        switch outcome.correct {
        case true?: Theme.success
        case false?: Theme.danger
        case nil: Theme.accent
        }
    }

    var body: some View {
        VStack(alignment: .leading, spacing: 10) {
            if showsFeedback, let correct = outcome.correct {
                Label(correct ? "Doğru!" : "Doğru değil", systemImage: correct ? "checkmark.circle.fill" : "xmark.circle.fill")
                    .font(.jakarta(.title3, weight: .bold))
                    .foregroundStyle(color)
                if let answer = outcome.correctAnswer {
                    (Text("Doğru cevap: ").bold() + Text(answer))
                        .font(.jakarta(.callout))
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
        }
        .padding(20)
        .frame(maxWidth: .infinity, alignment: .leading)
        .background(color.opacity(0.1))
        .background(.background)
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
    @State private var playCount = 0

    var body: some View {
        VStack(alignment: .leading, spacing: 20) {
            if let audioText {
                HStack(spacing: 16) {
                    Button {
                        Speech.shared.speak(audioText)
                        playCount += 1
                    } label: {
                        Image(systemName: "speaker.wave.3.fill")
                            .font(.system(size: 32))
                            .frame(width: 88, height: 88)
                            .background(Theme.accent, in: Circle())
                            .foregroundStyle(.white)
                    }
                    Button {
                        Speech.shared.speak(audioText, rate: 0.32)
                        playCount += 1
                    } label: {
                        Label("Yavaş", systemImage: "tortoise.fill")
                    }
                    .buttonStyle(.bordered)
                }
                .frame(maxWidth: .infinity)
                .onAppear { Speech.shared.speak(audioText) }
            }
            Text(prompt)
                .font(.jakarta(.title3, weight: .semibold))
                .fixedSize(horizontal: false, vertical: true)
            VStack(spacing: 10) {
                ForEach(Array(options.enumerated()), id: \.offset) { index, option in
                    Button {
                        guard !locked else { return }
                        chosen = index
                        Haptics.tap()
                        onChoose(index)
                    } label: {
                        Text(option)
                            .font(.jakarta(.body, weight: .medium))
                            .multilineTextAlignment(.leading)
                            .frame(maxWidth: .infinity, alignment: .leading)
                            .padding(16)
                            .background(background(for: index), in: RoundedRectangle(cornerRadius: 14))
                            .overlay(RoundedRectangle(cornerRadius: 14).stroke(border(for: index), lineWidth: 2))
                    }
                    .buttonStyle(.plain)
                }
            }
        }
    }

    private func background(for index: Int) -> Color {
        guard locked else { return Theme.surface }
        if index == answerIndex { return Theme.success.opacity(0.15) }
        if index == chosen { return Theme.danger.opacity(0.15) }
        return Theme.surface
    }

    private func border(for index: Int) -> Color {
        guard locked else { return Color.secondary.opacity(0.2) }
        if index == answerIndex { return Theme.success }
        if index == chosen { return Theme.danger }
        return Color.secondary.opacity(0.2)
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

    var body: some View {
        VStack(alignment: .leading, spacing: 20) {
            Text("Cümleyi kurun")
                .font(.jakarta(.subheadline, weight: .semibold))
                .foregroundStyle(.secondary)
            if let translation {
                Text(translation)
                    .font(.jakarta(.title3, weight: .semibold))
            }
            FlowLayout(spacing: 8) {
                ForEach(chosen, id: \.self) { index in
                    tile(words[index]) { chosen.removeAll { $0 == index } }
                }
            }
            .frame(maxWidth: .infinity, minHeight: 110, alignment: .topLeading)
            .padding(12)
            .background(Theme.surface, in: RoundedRectangle(cornerRadius: 14))
            .overlay(RoundedRectangle(cornerRadius: 14).stroke(Theme.accent.opacity(0.3), style: StrokeStyle(lineWidth: 1, dash: [5])))

            FlowLayout(spacing: 8) {
                ForEach(Array(words.enumerated()), id: \.offset) { index, word in
                    tile(word) { chosen.append(index) }
                        .opacity(chosen.contains(index) ? 0.25 : 1)
                        .disabled(chosen.contains(index))
                }
            }
            Button("Kontrol et") { onSubmit(chosen.map { words[$0] }) }
                .buttonStyle(.primary)
                .disabled(chosen.count != words.count)
        }
    }

    private func tile(_ word: String, action: @escaping () -> Void) -> some View {
        Button {
            Haptics.tap()
            withAnimation(.snappy(duration: 0.2)) { action() }
        } label: {
            Text(word)
                .font(.jakarta(.body, weight: .semibold))
                .padding(.horizontal, 14)
                .padding(.vertical, 10)
                .background(.background, in: RoundedRectangle(cornerRadius: 10))
                .overlay(RoundedRectangle(cornerRadius: 10).stroke(Color.secondary.opacity(0.3)))
        }
        .buttonStyle(.plain)
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
        let color: Color = switch state {
        case .normal: Color.secondary.opacity(0.25)
        case .selected: Theme.accent
        case .matched: Theme.success
        case .wrong: Theme.danger
        }
        return Button(action: action) {
            Text(text)
                .font(.jakarta(.callout, weight: .medium))
                .multilineTextAlignment(.center)
                .frame(maxWidth: .infinity, minHeight: 56)
                .padding(.horizontal, 8)
                .background(state == .normal ? Theme.surface : color.opacity(0.12), in: RoundedRectangle(cornerRadius: 12))
                .overlay(RoundedRectangle(cornerRadius: 12).stroke(color, lineWidth: 2))
                .opacity(state == .matched ? 0.5 : 1)
        }
        .buttonStyle(.plain)
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
                .font(.jakarta(.subheadline, weight: .semibold))
                .foregroundStyle(.secondary)
            Text(prompt)
                .font(.jakarta(.title3, weight: .semibold))
                .fixedSize(horizontal: false, vertical: true)

            VStack(spacing: 12) {
                Button {
                    Task { await recognizer.toggle() }
                } label: {
                    Image(systemName: recognizer.status == .recording ? "stop.fill" : "mic.fill")
                        .font(.system(size: 30, weight: .semibold))
                        .frame(width: 84, height: 84)
                        .background(recognizer.status == .recording ? Theme.danger : Theme.accent, in: Circle())
                        .foregroundStyle(.white)
                        .symbolEffect(.pulse, isActive: recognizer.status == .recording)
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

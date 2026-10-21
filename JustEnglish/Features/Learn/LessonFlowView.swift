import SwiftUI
import JECore

/// Bir dersin baştan sona akışı: ısınma → keşfet → öğren → pratik → kullan → özet.
/// Pratikte yanlış yapılan sorular dersin sonunda bir kez daha sorulur.
struct LessonFlowView: View {
    let unit: CourseUnit
    let lesson: Lesson

    @Environment(AppModel.self) private var model
    @Environment(\.dismiss) private var dismiss

    @State private var steps: [LessonStep] = []
    @State private var index = 0
    @State private var firstTryCorrect = 0
    @State private var graded = 0
    @State private var retried: Set<String> = []
    @State private var finished = false
    @State private var confirmExit = false

    var body: some View {
        VStack(spacing: 0) {
            header
            if finished {
                LessonSummaryView(lesson: lesson, correct: firstTryCorrect, total: graded) { dismiss() }
            } else if index < steps.count {
                stepView(steps[index])
                    .id(index)
                    .transition(.asymmetric(insertion: .move(edge: .trailing), removal: .move(edge: .leading)).combined(with: .opacity))
            }
        }
        .animation(.snappy, value: index)
        .background(Theme.background)
        .onAppear { if steps.isEmpty { steps = LessonStep.build(lesson: lesson, warmup: warmupCards) } }
        .onDisappear { Speech.shared.stop() }
        .confirmationDialog("Dersten çıkılsın mı?", isPresented: $confirmExit, titleVisibility: .visible) {
            Button("Çık", role: .destructive) { dismiss() }
        } message: {
            Text("Bu dersteki ilerlemeniz kaydedilmez.")
        }
    }

    private var warmupCards: [VocabularyCard] {
        lesson.warmup.source == "review" ? model.warmupCards(count: lesson.warmup.count ?? 6) : []
    }

    private var header: some View {
        HStack(spacing: 14) {
            Button {
                if finished || index == 0 { dismiss() } else { confirmExit = true }
            } label: {
                Image(systemName: "xmark").font(.jakarta(.headline, weight: .bold))
            }
            .foregroundStyle(.secondary)
            ProgressBar(value: finished ? 1 : Double(index) / Double(max(steps.count, 1)), height: 10)
        }
        .padding(.horizontal, 20)
        .padding(.vertical, 12)
    }

    @ViewBuilder private func stepView(_ step: LessonStep) -> some View {
        switch step {
        case .warmup(let cards):
            WarmupStep(cards: cards, onDone: next)
        case .discover:
            DiscoverStep(discover: lesson.discover, onDone: next)
        case .learn:
            LearnStep(learn: lesson.learn, goal: lesson.goal, onDone: next)
        case .exercise(let exercise, let section):
            VStack(alignment: .leading, spacing: 0) {
                Text(section.title)
                    .font(.jakarta(.caption, weight: .bold))
                    .foregroundStyle(Theme.accent)
                    .textCase(.uppercase)
                    .padding(.horizontal, 20)
                ExerciseView(exercise: exercise) { outcome in record(exercise, section: section, outcome: outcome) }
            }
        }
    }

    private func record(_ exercise: Exercise, section: LessonStep.Section, outcome: ExerciseOutcome) {
        if let correct = outcome.correct {
            let isRetry = retried.contains(exercise.id)
            if !isRetry {
                graded += 1
                if correct { firstTryCorrect += 1 }
                model.recordAnswer(exerciseID: exercise.id, correct: correct)
            }
            if !correct && !isRetry && section == .practice {
                retried.insert(exercise.id)
                // Kullan bölümünden önce tekrar sorulur.
                let useIndex = steps.lastIndex { if case .exercise(_, .use) = $0 { true } else { false } } ?? steps.count
                steps.insert(.exercise(exercise, .review), at: useIndex)
            }
        }
        next()
    }

    private func next() {
        if index + 1 < steps.count {
            index += 1
        } else {
            model.completeLesson(lesson, in: unit, correct: firstTryCorrect, total: graded)
            finished = true
        }
    }
}

enum LessonStep {
    enum Section: Equatable {
        case discover, practice, review, use
        var title: String {
            switch self {
            case .discover: "Keşfet"
            case .practice: "Pratik"
            case .review: "Tekrar deneyin"
            case .use: "Kullan"
            }
        }
    }

    case warmup([VocabularyCard])
    case discover
    case learn
    case exercise(Exercise, Section)

    static func build(lesson: Lesson, warmup: [VocabularyCard]) -> [LessonStep] {
        var steps: [LessonStep] = []
        if !warmup.isEmpty { steps.append(.warmup(warmup)) }
        steps.append(.discover)
        steps += lesson.discover.questions.map { .exercise($0, .discover) }
        steps.append(.learn)
        steps += lesson.practice.map { .exercise($0, .practice) }
        steps.append(.exercise(lesson.use.task, .use))
        return steps
    }
}

// MARK: - Isınma

/// Daha önce öğrenilen kelimelerin hızlı hatırlatması: kartı çevir, hatırladın mı?
struct WarmupStep: View {
    let cards: [VocabularyCard]
    let onDone: () -> Void

    @Environment(AppModel.self) private var model
    @State private var position = 0
    @State private var flipped = false

    var body: some View {
        VStack(spacing: 20) {
            VStack(spacing: 4) {
                Text("Isınma").font(.jakarta(.title2, weight: .bold))
                Text("Önceki derslerden kelimeler: anlamını hatırlayın, sonra kartı çevirin.")
                    .font(.jakarta(.subheadline))
                    .foregroundStyle(.secondary)
                    .multilineTextAlignment(.center)
            }
            Spacer()
            if position < cards.count {
                FlipCard(card: cards[position], flipped: $flipped)
                    .id(position)
            }
            Spacer()
            if flipped {
                HStack(spacing: 12) {
                    Button("Hatırlamadım") { answer(.again) }.buttonStyle(PrimaryButtonStyle(color: Theme.danger))
                    Button("Hatırladım") { answer(.good) }.buttonStyle(PrimaryButtonStyle(color: Theme.success))
                }
            } else {
                Button("Kartı çevir") { withAnimation(.spring) { flipped = true } }.buttonStyle(.primary)
            }
            Button("Geç", action: onDone).font(.jakarta(.subheadline)).foregroundStyle(.secondary)
        }
        .padding(20)
    }

    private func answer(_ rating: ReviewRating) {
        model.review(cardID: cards[position].id, rating: rating)
        flipped = false
        if position + 1 < cards.count { position += 1 } else { onDone() }
    }
}

// MARK: - Keşfet

struct DiscoverStep: View {
    let discover: Discover
    let onDone: () -> Void

    var body: some View {
        VStack(spacing: 0) {
            ScrollView {
                VStack(alignment: .leading, spacing: 16) {
                    Text("Keşfet").font(.jakarta(.caption, weight: .bold)).foregroundStyle(Theme.accent).textCase(.uppercase)
                    HStack {
                        Text(discover.title).font(.jakarta(.title2, weight: .bold))
                        Spacer()
                        SpeakButton(text: spokenText)
                    }
                    switch discover.kind {
                    case .text:
                        Text(discover.body ?? "")
                            .font(.jakarta(.body))
                            .lineSpacing(5)
                            .textSelection(.enabled)
                            .card()
                    case .dialogue:
                        DialogueView(lines: discover.lines ?? [])
                    }
                    Text("Okuyun ve dinleyin. Ardından birkaç soru gelecek.")
                        .font(.jakarta(.footnote))
                        .foregroundStyle(.secondary)
                }
                .padding(20)
            }
            Button("Sorulara geç", action: onDone)
                .buttonStyle(.primary)
                .padding(20)
        }
    }

    private var spokenText: String {
        switch discover.kind {
        case .text: discover.body ?? ""
        case .dialogue: (discover.lines ?? []).map(\.text).joined(separator: " ")
        }
    }
}

struct DialogueView: View {
    let lines: [Discover.Line]

    private var speakers: [String] {
        var seen: [String] = []
        for line in lines where !seen.contains(line.speaker) { seen.append(line.speaker) }
        return seen
    }

    var body: some View {
        VStack(spacing: 10) {
            ForEach(Array(lines.enumerated()), id: \.offset) { _, line in
                let isFirst = line.speaker == speakers.first
                HStack {
                    if !isFirst { Spacer(minLength: 40) }
                    VStack(alignment: .leading, spacing: 4) {
                        Text(line.speaker)
                            .font(.jakarta(.caption, weight: .bold))
                            .foregroundStyle(isFirst ? Theme.accent : Theme.color(for: .b2))
                        Text(line.text).font(.jakarta(.body))
                    }
                    .padding(12)
                    .background(isFirst ? Theme.accent.opacity(0.1) : Theme.surface, in: RoundedRectangle(cornerRadius: 14))
                    .onTapGesture { Speech.shared.speak(line.text) }
                    if isFirst { Spacer(minLength: 40) }
                }
            }
        }
    }
}

// MARK: - Öğren

struct LearnStep: View {
    let learn: Learn
    let goal: String
    let onDone: () -> Void

    var body: some View {
        VStack(spacing: 0) {
            ScrollView {
                VStack(alignment: .leading, spacing: 18) {
                    Text("Öğren").font(.jakarta(.caption, weight: .bold)).foregroundStyle(Theme.accent).textCase(.uppercase)
                    Text(goal).font(.jakarta(.title3, weight: .bold))
                    MarkdownView(learn.explanation)
                        .font(.jakarta(.body))
                    if !learn.examples.isEmpty {
                        SectionTitle(text: "Örnekler")
                        VStack(spacing: 10) {
                            ForEach(Array(learn.examples.enumerated()), id: \.offset) { _, example in
                                HStack(alignment: .top, spacing: 12) {
                                    VStack(alignment: .leading, spacing: 4) {
                                        Text(example.en).font(.jakarta(.body, weight: .semibold))
                                        Text(example.tr).font(.jakarta(.subheadline)).foregroundStyle(.secondary)
                                    }
                                    Spacer()
                                    SpeakButton(text: example.en)
                                }
                                .card()
                            }
                        }
                    }
                    if let note = learn.turkishNote, !note.isEmpty {
                        VStack(alignment: .leading, spacing: 8) {
                            Label("Türkçe konuşanlar için", systemImage: "exclamationmark.bubble.fill")
                                .font(.jakarta(.headline))
                                .foregroundStyle(Theme.warning)
                            MarkdownView(note).font(.jakarta(.callout))
                        }
                        .padding(16)
                        .background(Theme.warning.opacity(0.1), in: RoundedRectangle(cornerRadius: Theme.cornerRadius))
                    }
                }
                .padding(20)
            }
            Button("Pratiğe başla", action: onDone)
                .buttonStyle(.primary)
                .padding(20)
        }
    }
}

// MARK: - Özet

struct LessonSummaryView: View {
    let lesson: Lesson
    let correct: Int
    let total: Int
    let onClose: () -> Void

    @Environment(AppModel.self) private var model

    private var percent: Int { total == 0 ? 100 : Int((Double(correct) / Double(total) * 100).rounded()) }

    var body: some View {
        VStack(spacing: 24) {
            Spacer()
            Image(systemName: percent == 100 ? "star.circle.fill" : "checkmark.seal.fill")
                .font(.system(size: 88))
                .foregroundStyle(percent == 100 ? Theme.warning : Theme.success)
                .symbolEffect(.bounce, value: true)
            VStack(spacing: 6) {
                Text("Ders tamamlandı!").font(.jakarta(.title, weight: .bold))
                Text(lesson.title).font(.jakarta(.headline)).foregroundStyle(.secondary)
            }
            HStack(spacing: 12) {
                stat(value: "%\(percent)", label: "Doğruluk", color: Theme.success)
                stat(value: "\(model.state.progress.todayXP)", label: "Bugünkü XP", color: Theme.accent)
                stat(value: "\(model.state.progress.displayedStreak(at: .now))", label: "Gün serisi", color: Theme.streak)
            }
            if model.state.progress.goalReachedToday {
                Label("Günlük hedefinize ulaştınız!", systemImage: "flame.fill")
                    .font(.jakarta(.headline))
                    .foregroundStyle(Theme.streak)
            }
            Spacer()
            Button("Bitir", action: onClose).buttonStyle(.primary)
        }
        .padding(20)
    }

    private func stat(value: String, label: String, color: Color) -> some View {
        VStack(spacing: 4) {
            Text(value).font(.jakarta(.title2, weight: .bold)).foregroundStyle(color)
            Text(label).font(.jakarta(.caption)).foregroundStyle(.secondary)
        }
        .frame(maxWidth: .infinity)
        .padding(.vertical, 14)
        .background(color.opacity(0.1), in: RoundedRectangle(cornerRadius: 14))
    }
}

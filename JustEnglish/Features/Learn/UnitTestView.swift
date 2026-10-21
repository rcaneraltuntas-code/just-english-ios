import SwiftUI
import JECore

/// Ünite testi: sorular anında geri bildirim olmadan sorulur, sonunda sonuç ve yanlışların açıklaması gösterilir.
/// Yazma görevi otomatik puanlanmaz ve yüzdeye katılmaz.
struct UnitTestView: View {
    let unit: CourseUnit

    @Environment(AppModel.self) private var model
    @Environment(\.dismiss) private var dismiss

    @State private var index = 0
    @State private var results: [(exercise: Exercise, outcome: ExerciseOutcome)] = []
    @State private var confirmExit = false

    private var questions: [Exercise] { unit.unitTest.questions }
    private var finished: Bool { index >= questions.count }

    var body: some View {
        VStack(spacing: 0) {
            HStack(spacing: 14) {
                Button {
                    if finished || index == 0 { dismiss() } else { confirmExit = true }
                } label: {
                    Image(systemName: "xmark").font(.jakarta(.headline, weight: .bold))
                }
                .foregroundStyle(.secondary)
                ProgressBar(value: Double(index) / Double(max(questions.count, 1)), height: 10)
                Text("\(min(index + 1, questions.count))/\(questions.count)")
                    .font(.jakarta(.footnote, weight: .semibold))
                    .monospacedDigit()
                    .foregroundStyle(.secondary)
            }
            .padding(.horizontal, 20)
            .padding(.vertical, 12)

            if finished {
                TestResultView(unit: unit, results: results) { dismiss() } retry: {
                    results = []
                    index = 0
                }
            } else {
                ExerciseView(exercise: questions[index], showsFeedback: false) { outcome in
                    results.append((questions[index], outcome))
                    index += 1
                    if index == questions.count { model.recordUnitTest(unit, percent: percent) }
                }
                .id(index)
            }
        }
        .background(Theme.background)
        .confirmationDialog("Testten çıkılsın mı?", isPresented: $confirmExit, titleVisibility: .visible) {
            Button("Çık", role: .destructive) { dismiss() }
        }
    }

    private var percent: Int {
        let graded = results.filter { $0.outcome.correct != nil }
        guard !graded.isEmpty else { return 0 }
        let correct = graded.filter { $0.outcome.correct == true }.count
        return Int((Double(correct) / Double(graded.count) * 100).rounded())
    }
}

struct TestResultView: View {
    let unit: CourseUnit
    let results: [(exercise: Exercise, outcome: ExerciseOutcome)]
    let close: () -> Void
    let retry: () -> Void

    private var graded: [(exercise: Exercise, outcome: ExerciseOutcome)] { results.filter { $0.outcome.correct != nil } }
    private var wrong: [(exercise: Exercise, outcome: ExerciseOutcome)] { graded.filter { $0.outcome.correct == false } }
    private var percent: Int {
        graded.isEmpty ? 0 : Int((Double(graded.count - wrong.count) / Double(graded.count) * 100).rounded())
    }
    private var passed: Bool { percent >= unit.unitTest.passPercent }

    var body: some View {
        ScrollView {
            VStack(spacing: 20) {
                Image(systemName: passed ? "trophy.fill" : "arrow.counterclockwise.circle.fill")
                    .font(.system(size: 72))
                    .foregroundStyle(passed ? Theme.warning : Theme.accent)
                    .padding(.top, 20)
                Text("%\(percent)").font(.jakarta(.largeTitle, weight: .bold))
                Text(passed ? "Tebrikler, üniteyi geçtiniz!" : "Geçme notu %\(unit.unitTest.passPercent). Yanlışlarınızı inceleyip tekrar deneyin.")
                    .font(.jakarta(.headline))
                    .multilineTextAlignment(.center)

                if !wrong.isEmpty {
                    SectionTitle(text: "Yanlışlarınız")
                    ForEach(Array(wrong.enumerated()), id: \.offset) { _, item in
                        VStack(alignment: .leading, spacing: 6) {
                            Text(item.exercise.promptText).font(.jakarta(.callout, weight: .semibold))
                            if let answer = item.outcome.correctAnswer {
                                (Text("Doğru cevap: ").bold() + Text(answer)).font(.jakarta(.callout)).foregroundStyle(Theme.success)
                            }
                            if let message = item.outcome.message {
                                Text(message).font(.jakarta(.footnote)).foregroundStyle(.secondary)
                            }
                        }
                        .card()
                    }
                }

                Button("Bitir", action: close).buttonStyle(.primary)
                if !passed { Button("Tekrar dene", action: retry).buttonStyle(.secondary) }
            }
            .padding(20)
        }
    }
}

extension Exercise {
    /// Sonuç listelerinde soruyu tanıtan kısa metin.
    var promptText: String {
        switch self {
        case let .multipleChoice(_, prompt, _, _, _, _), let .typeAnswer(_, prompt, _, _),
             let .listening(_, _, prompt, _, _, _), let .speaking(_, prompt, _, _), let .writing(_, prompt, _, _):
            prompt
        case let .gapFill(_, text, _, _, _):
            text
        case let .ordering(_, _, answer, _, translation):
            translation ?? answer
        case let .matching(_, pairs, _):
            pairs.map(\.left).joined(separator: ", ")
        }
    }
}

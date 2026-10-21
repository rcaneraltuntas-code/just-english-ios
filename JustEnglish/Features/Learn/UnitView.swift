import SwiftUI
import JECore

struct UnitView: View {
    let unit: CourseUnit

    @Environment(AppModel.self) private var model
    @State private var activeLesson: LessonRoute?
    @State private var showTest = false

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 20) {
                VStack(alignment: .leading, spacing: 8) {
                    HStack {
                        LevelBadge(level: unit.level)
                        Text("Ünite \(unit.number) · \(unit.titleEn)").font(.jakarta(.subheadline, weight: .semibold)).foregroundStyle(.secondary)
                        Spacer()
                        Text("\(model.completedCount(in: unit))/\(unit.lessons.count)")
                            .font(.jakarta(.subheadline, weight: .heavy))
                            .foregroundStyle(Theme.color(for: unit.level))
                    }
                    ProgressBar(value: Double(model.completedCount(in: unit)) / Double(max(unit.lessons.count, 1)),
                                color: Theme.color(for: unit.level), height: 12)
                    Text(unit.canDo).font(.jakarta(.body))
                    if !unit.grammar.isEmpty {
                        FlowLayout(spacing: 6) {
                            ForEach(unit.grammar, id: \.self) { tag($0, color: Theme.accent) }
                            ForEach(unit.vocabularyThemes, id: \.self) { tag($0, color: Theme.color(for: unit.level)) }
                        }
                    }
                }

                LessonPathView(unit: unit) { lesson in
                    activeLesson = LessonRoute(unit: unit, lesson: lesson)
                } onTest: {
                    showTest = true
                }

                SectionTitle(text: "Ünite testi")
                Button { showTest = true } label: {
                    HStack(spacing: 14) {
                        Image(systemName: model.isUnitPassed(unit) ? "checkmark.seal.fill" : "doc.text.fill")
                            .font(.title2)
                            .foregroundStyle(model.isUnitPassed(unit) ? Theme.success : Theme.accent)
                        VStack(alignment: .leading, spacing: 3) {
                            Text("\(unit.unitTest.questions.count) soru · geçme notu %\(unit.unitTest.passPercent)")
                                .font(.jakarta(.headline))
                            if let best = model.state.unitTestScores[unit.id] {
                                Text("En iyi sonucunuz: %\(best)").font(.jakarta(.footnote)).foregroundStyle(.secondary)
                            } else {
                                Text("Tüm dersleri bitirdikten sonra önerilir.").font(.jakarta(.footnote)).foregroundStyle(.secondary)
                            }
                        }
                        Spacer()
                        Image(systemName: "chevron.right").foregroundStyle(.tertiary)
                    }
                    .card()
                }
                .buttonStyle(.plain)

                SectionTitle(text: "Canlı ders")
                LiveClassCard(unit: unit)

                SectionTitle(text: "Kelimeler (\(unit.vocabulary.count))")
                VStack(spacing: 0) {
                    ForEach(unit.vocabulary) { card in
                        VocabularyRow(card: card)
                        if card.id != unit.vocabulary.last?.id { Divider() }
                    }
                }
                .card()
            }
            .padding(20)
        }
        .background(Theme.background)
        .navigationTitle(unit.title)
        .navigationBarTitleDisplayMode(.large)
        .fullScreenCover(item: $activeLesson) { LessonFlowView(unit: $0.unit, lesson: $0.lesson) }
        .fullScreenCover(isPresented: $showTest) { UnitTestView(unit: unit) }
    }

    private func tag(_ text: String, color: Color) -> some View {
        Text(text)
            .font(.jakarta(.caption, weight: .semibold))
            .padding(.horizontal, 10)
            .padding(.vertical, 5)
            .foregroundStyle(color)
            .background(color.opacity(0.12), in: Capsule())
    }
}

struct LessonRow: View {
    let lesson: Lesson
    let done: Bool
    let score: Int?

    var body: some View {
        HStack(spacing: 14) {
            Image(systemName: done ? "checkmark.circle.fill" : "\(lesson.number).circle")
                .font(.title2)
                .foregroundStyle(done ? Theme.success : Theme.accent)
            VStack(alignment: .leading, spacing: 3) {
                Text(lesson.title).font(.jakarta(.headline))
                Text(lesson.goal).font(.jakarta(.footnote)).foregroundStyle(.secondary).lineLimit(2)
            }
            Spacer()
            if let score { Text("%\(score)").font(.jakarta(.footnote, weight: .bold)).foregroundStyle(.secondary) }
        }
        .card()
    }
}

struct VocabularyRow: View {
    let card: VocabularyCard

    var body: some View {
        HStack(alignment: .top, spacing: 12) {
            VStack(alignment: .leading, spacing: 3) {
                HStack(alignment: .firstTextBaseline) {
                    Text(card.en).font(.jakarta(.headline))
                    Text(card.tr).font(.jakarta(.subheadline)).foregroundStyle(.secondary)
                }
                Text(card.example).font(.jakarta(.footnote)).foregroundStyle(.secondary)
            }
            Spacer()
            SpeakButton(text: card.en)
        }
        .padding(.vertical, 8)
    }
}

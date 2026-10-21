import SwiftUI
import JECore

/// Ana sayfa: günlük hedef, seri, sıradaki ders ve seviyelere göre üniteler.
struct LearnView: View {
    @Environment(AppModel.self) private var model
    @State private var selectedLevel: CEFRLevel?
    @State private var activeLesson: LessonRoute?

    private var level: CEFRLevel { selectedLevel ?? model.state.currentLevel }

    var body: some View {
        NavigationStack {
            ScrollView {
                VStack(spacing: 20) {
                    TodayCard()
                    if let next = model.nextLesson {
                        ContinueCard(unit: next.unit, lesson: next.lesson) {
                            activeLesson = LessonRoute(unit: next.unit, lesson: next.lesson)
                        }
                    }
                    levelPicker
                    VStack(spacing: 12) {
                        ForEach(model.units(for: level)) { unit in
                            NavigationLink(value: unit) { UnitRow(unit: unit) }
                                .buttonStyle(.plain)
                        }
                    }
                }
                .padding(20)
            }
            .background(Theme.background)
            .navigationTitle(model.state.name.isEmpty ? "Merhaba!" : "Merhaba, \(model.state.name)!")
            .navigationDestination(for: CourseUnit.self) { UnitView(unit: $0) }
            .fullScreenCover(item: $activeLesson) { route in
                LessonFlowView(unit: route.unit, lesson: route.lesson)
            }
        }
    }

    private var levelPicker: some View {
        ScrollView(.horizontal, showsIndicators: false) {
            HStack(spacing: 8) {
                ForEach(CEFRLevel.allCases) { item in
                    Button {
                        selectedLevel = item
                        Haptics.tap()
                    } label: {
                        VStack(spacing: 2) {
                            Text(item.rawValue.uppercased()).font(.jakarta(.headline, weight: .bold))
                            Text(item.title).font(.jakarta(.caption2)).lineLimit(1)
                        }
                        .padding(.horizontal, 14)
                        .padding(.vertical, 8)
                        .foregroundStyle(item == level ? .white : Theme.color(for: item))
                        .background(item == level ? Theme.color(for: item) : Theme.color(for: item).opacity(0.12),
                                    in: RoundedRectangle(cornerRadius: 12))
                    }
                    .buttonStyle(.plain)
                }
            }
        }
    }
}

struct LessonRoute: Identifiable {
    let unit: CourseUnit
    let lesson: Lesson
    var id: String { lesson.id }
}

struct TodayCard: View {
    @Environment(AppModel.self) private var model

    var body: some View {
        let progress = model.state.progress
        let ratio = Double(progress.todayDay.map { Calendar.current.isDateInToday($0) } == true ? progress.todayXP : 0)
            / Double(max(progress.dailyGoalXP, 1))
        HStack(spacing: 18) {
            ZStack {
                ProgressRing(value: ratio, color: Theme.success, lineWidth: 10)
                VStack(spacing: 0) {
                    Text("\(Int(min(ratio, 9.99) * 100))%").font(.jakarta(.headline, weight: .bold))
                    Text("hedef").font(.jakarta(.caption2)).foregroundStyle(.secondary)
                }
            }
            .frame(width: 76, height: 76)
            VStack(alignment: .leading, spacing: 6) {
                Text(ratio >= 1 ? "Bugünkü hedef tamam!" : "Bugünkü hedef: \(progress.dailyGoalXP) XP")
                    .font(.jakarta(.headline))
                Label("\(progress.displayedStreak(at: .now)) gün seri", systemImage: "flame.fill")
                    .font(.jakarta(.subheadline, weight: .semibold))
                    .foregroundStyle(Theme.streak)
                Text("Toplam \(progress.totalXP) XP")
                    .font(.jakarta(.footnote))
                    .foregroundStyle(.secondary)
            }
            Spacer()
        }
        .card()
    }
}

struct ContinueCard: View {
    let unit: CourseUnit
    let lesson: Lesson
    let onStart: () -> Void

    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            HStack {
                LevelBadge(level: unit.level)
                Text("Ünite \(unit.number) · Ders \(lesson.number)")
                    .font(.jakarta(.footnote, weight: .semibold))
                    .foregroundStyle(.white.opacity(0.85))
            }
            Text(lesson.title).font(.jakarta(.title2, weight: .bold)).foregroundStyle(.white)
            Text(lesson.goal).font(.jakarta(.subheadline)).foregroundStyle(.white.opacity(0.9))
            Button(action: onStart) {
                Label("Derse başla", systemImage: "play.fill")
                    .font(.jakarta(.headline, weight: .bold))
                    .frame(maxWidth: .infinity, minHeight: 48)
                    .background(.white, in: RoundedRectangle(cornerRadius: 12))
                    .foregroundStyle(Theme.accent)
            }
            .buttonStyle(.plain)
        }
        .padding(18)
        .background(LinearGradient(colors: [Theme.accent, Theme.color(for: unit.level)],
                                   startPoint: .topLeading, endPoint: .bottomTrailing),
                    in: RoundedRectangle(cornerRadius: 20))
    }
}

struct UnitRow: View {
    let unit: CourseUnit
    @Environment(AppModel.self) private var model

    var body: some View {
        let done = model.completedCount(in: unit)
        HStack(spacing: 14) {
            ZStack {
                ProgressRing(value: Double(done) / Double(max(unit.lessons.count, 1)),
                             color: Theme.color(for: unit.level), lineWidth: 5)
                if model.isUnitPassed(unit) {
                    Image(systemName: "checkmark").font(.jakarta(.headline, weight: .bold)).foregroundStyle(Theme.success)
                } else {
                    Text("\(unit.number)").font(.jakarta(.headline, weight: .bold))
                }
            }
            .frame(width: 48, height: 48)
            VStack(alignment: .leading, spacing: 3) {
                Text(unit.title).font(.jakarta(.headline))
                Text(unit.canDo).font(.jakarta(.footnote)).foregroundStyle(.secondary).lineLimit(2)
            }
            Spacer()
            Image(systemName: "chevron.right").foregroundStyle(.tertiary)
        }
        .card()
    }
}

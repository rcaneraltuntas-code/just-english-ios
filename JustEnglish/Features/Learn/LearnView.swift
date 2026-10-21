import SwiftUI
import JECore

/// Ana sayfa: üstte yumuşak degrade bant ve selam, JAI kartı, seri haftası, haftalık XP ve hedef,
/// "akıcılık yolunuz" listesi, günün kelimesi ve seviyelere göre üniteler.
struct LearnView: View {
    @Environment(AppModel.self) private var model
    @State private var selectedLevel: CEFRLevel?
    @State private var activeLesson: LessonRoute?

    private var level: CEFRLevel { selectedLevel ?? model.state.currentLevel }

    var body: some View {
        NavigationStack {
            ScrollView {
                VStack(spacing: 18) {
                    HomeHeader()
                    AIBuddyCard().staggeredAppear(0)
                    if let next = model.nextLesson {
                        ContinueCard(unit: next.unit, lesson: next.lesson) {
                            activeLesson = LessonRoute(unit: next.unit, lesson: next.lesson)
                        }
                        .staggeredAppear(1)
                    }
                    StreakWeekCard().staggeredAppear(2)
                    HomeStatPair().staggeredAppear(3)
                    VStack(alignment: .leading, spacing: 12) {
                        SectionHeader(title: "Akıcılığa giden yol")
                        FluencyPathList(level: model.state.currentLevel)
                    }
                    .staggeredAppear(4)
                    WordOfTheDayCard().staggeredAppear(5)
                    VStack(alignment: .leading, spacing: 12) {
                        SectionHeader(title: "Üniteler")
                        levelPicker
                    }
                    .padding(.top, 4)
                    VStack(spacing: 12) {
                        ForEach(model.units(for: level)) { unit in
                            NavigationLink(value: unit) { UnitRow(unit: unit) }
                                .buttonStyle(PressableCardStyle())
                                .staggeredAppear(unit.number)
                        }
                    }
                }
                .padding(.horizontal, 20)
                .padding(.bottom, 20)
            }
            .tabBarSpacer()
            .background {
                ZStack(alignment: .top) {
                    AIBackground(animated: true)
                    // Referanstaki gibi üstte yumuşak mavi bant.
                    Theme.skyGradient
                        .frame(height: 300)
                        .opacity(0.75)
                }
                .ignoresSafeArea()
            }
            // Gezinme çubuğu gizli olduğundan, kaydırınca içerik saatin altına girmesin diye durum çubuğuna zemin.
            .safeAreaInset(edge: .top, spacing: 0) {
                Color.clear.frame(height: 0).background(.ultraThinMaterial, ignoresSafeAreaEdges: .top)
            }
            .toolbar(.hidden, for: .navigationBar)
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
                        withAnimation(Motion.smooth) { selectedLevel = item }
                        Haptics.tap()
                    } label: {
                        VStack(spacing: 2) {
                            Text(item.rawValue.uppercased()).font(.jakarta(.headline, weight: .heavy))
                            Text(item.title).font(.jakarta(.caption2, weight: .semibold)).lineLimit(1)
                        }
                        .padding(.horizontal, 16)
                        .padding(.vertical, 9)
                        .foregroundStyle(item == level ? .white : Theme.color(for: item))
                        .background(item == level ? AnyShapeStyle(Theme.color(for: item).gradient) : AnyShapeStyle(Theme.surface),
                                    in: RoundedRectangle(cornerRadius: 16, style: .continuous))
                        .overlay(RoundedRectangle(cornerRadius: 16, style: .continuous)
                            .stroke(item == level ? .clear : Theme.hairline, lineWidth: 1))
                    }
                    .buttonStyle(PressableCardStyle())
                }
            }
            .padding(.horizontal, 20)
            .padding(.vertical, 4)
        }
        // Çipler sayfa kenarına kadar kaysın, 20pt boşlukta kesilmesin.
        .padding(.horizontal, -20)
    }
}

struct LessonRoute: Identifiable {
    let unit: CourseUnit
    let lesson: Lesson
    var id: String { lesson.id }
}

/// Sıradaki ders: beyaz kart, seviye rozeti, ünite ilerlemesi ve birincil düğme.
struct ContinueCard: View {
    let unit: CourseUnit
    let lesson: Lesson
    let onStart: () -> Void
    @Environment(AppModel.self) private var model

    var body: some View {
        let done = model.completedCount(in: unit)
        VStack(alignment: .leading, spacing: 12) {
            HStack(spacing: 8) {
                LevelBadge(level: unit.level)
                Text("Ünite \(unit.number) · Ders \(lesson.number)")
                    .font(.jakarta(.footnote, weight: .semibold))
                    .foregroundStyle(.secondary)
                Spacer()
                Text("📘").font(.system(size: 26))
            }
            Text(lesson.title).font(.jakarta(.title3, weight: .heavy)).foregroundStyle(Theme.ink)
            Text(lesson.goal).font(.jakarta(.subheadline, weight: .medium)).foregroundStyle(.secondary)
            VStack(alignment: .leading, spacing: 6) {
                ProgressBar(value: Double(done) / Double(max(unit.lessons.count, 1)), color: Theme.accent, height: 8)
                Text("\(unit.title) · \(done)/\(unit.lessons.count) ders")
                    .font(.jakarta(.caption, weight: .semibold))
                    .foregroundStyle(.secondary)
            }
            Button(action: onStart) {
                Label("Derse başla", systemImage: "play.fill")
            }
            .buttonStyle(.primary)
        }
        .card()
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
                    Text("\(unit.number)").font(.jakarta(.headline, weight: .heavy)).foregroundStyle(Theme.ink)
                }
            }
            .frame(width: 48, height: 48)
            VStack(alignment: .leading, spacing: 3) {
                Text(unit.title).font(.jakarta(.headline, weight: .bold)).foregroundStyle(Theme.ink)
                Text(unit.canDo).font(.jakarta(.footnote)).foregroundStyle(.secondary).lineLimit(2)
            }
            Spacer()
            Image(systemName: "chevron.right").font(.jakarta(.subheadline, weight: .bold)).foregroundStyle(.tertiary)
        }
        .card()
    }
}

/// Kart şeklindeki gezinme bağlantıları için: basılınca hafifçe küçülür.
struct PressableCardStyle: ButtonStyle {
    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .scaleEffect(configuration.isPressed ? 0.97 : 1)
            .brightness(configuration.isPressed ? -0.03 : 0)
            .animation(Motion.press, value: configuration.isPressed)
    }
}

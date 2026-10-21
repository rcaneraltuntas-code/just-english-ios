import SwiftUI
import JECore

/// Ana sayfa (referans 2): üstte doygun mavi bant üzerinde selam ve JAI kartı; altında düz beyaz zeminde
/// seri haftası, iki istatistik kartı, "Akıcılığa giden yol" (ilk satır sıradaki dersi açar), günün kelimesi ve üniteler.
struct LearnView: View {
    @Environment(AppModel.self) private var model
    @State private var selectedLevel: CEFRLevel?
    @State private var activeLesson: LessonRoute?

    private var level: CEFRLevel { selectedLevel ?? model.state.currentLevel }

    var body: some View {
        NavigationStack {
            ScrollView {
                VStack(spacing: 0) {
                    HomeHeader()
                    AIBuddyCard().staggeredAppear(0).padding(.top, 14)
                    StreakWeekCard().staggeredAppear(1).padding(.top, 24)
                    HomeStatPair().staggeredAppear(2).padding(.top, 12)
                    VStack(alignment: .leading, spacing: 16) {
                        Text("Akıcılığa giden yol")
                            .font(.custom(Theme.fontFamily, size: 20, relativeTo: .title3).weight(.bold))
                            .foregroundStyle(HomeStyle.title)
                        FluencyPathList(level: model.state.currentLevel) {
                            if let next = model.nextLesson {
                                activeLesson = LessonRoute(unit: next.unit, lesson: next.lesson)
                            }
                        }
                    }
                    .frame(maxWidth: .infinity, alignment: .leading)
                    .staggeredAppear(3)
                    .padding(.top, 30)
                    WordOfTheDayCard().staggeredAppear(4).padding(.top, 24)
                    VStack(alignment: .leading, spacing: 12) {
                        SectionHeader(title: "Üniteler")
                        levelPicker
                    }
                    .padding(.top, 28)
                    VStack(spacing: 12) {
                        ForEach(model.units(for: level)) { unit in
                            NavigationLink(value: unit) { UnitRow(unit: unit) }
                                .buttonStyle(PressableCardStyle())
                                .staggeredAppear(unit.number)
                        }
                    }
                    .padding(.top, 12)
                }
                .padding(.horizontal, 16)
                .padding(.bottom, 20)
                .background(alignment: .top) {
                    // Bant içerikle birlikte kayar; en üst rengi durum çubuğunun arkasındaki şeritle aynı, ek yeri görünmez.
                    HomeStyle.band.frame(height: 340)
                }
            }
            .tabBarSpacer()
            .background(HomeStyle.page.ignoresSafeArea())
            // Gezinme çubuğu gizli; durum çubuğunun arkası bandın en üst rengiyle dolu, kaydırınca içerik altına girmez.
            .safeAreaInset(edge: .top, spacing: 0) {
                Color.clear.frame(height: 0).background(HomeStyle.bandTop, ignoresSafeAreaEdges: .top)
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

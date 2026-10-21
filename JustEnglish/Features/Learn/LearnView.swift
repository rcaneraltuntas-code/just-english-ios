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
                    StatsBar()
                    JAISays(text: greeting, mood: model.state.progress.goalReachedToday ? .happy : .talking, size: 70)
                        .frame(maxWidth: .infinity, alignment: .leading)
                    TodayCard().staggeredAppear(0)
                    if let next = model.nextLesson {
                        ContinueCard(unit: next.unit, lesson: next.lesson) {
                            activeLesson = LessonRoute(unit: next.unit, lesson: next.lesson)
                        }
                        .staggeredAppear(1)
                    }
                    QuickActionsGrid()
                    WeekActivityCard().staggeredAppear(2)
                    WordOfTheDayCard().staggeredAppear(3)
                    LeagueAndLiveRow().staggeredAppear(4)
                    SectionHeader(title: "Üniteler")
                        .padding(.top, 4)
                    levelPicker
                    VStack(spacing: 12) {
                        ForEach(model.units(for: level)) { unit in
                            NavigationLink(value: unit) { UnitRow(unit: unit) }
                                .buttonStyle(PressableCardStyle())
                                .staggeredAppear(unit.number)
                        }
                    }
                }
                .padding(20)
            }
            .background {
                ZStack(alignment: .top) {
                    Theme.background
                    AuroraBackground(colors: [Theme.accent, Theme.streak, Theme.color(for: level)],
                                     intensity: 0.35)
                        .frame(height: 360)
                        .mask(LinearGradient(colors: [.black, .clear], startPoint: .top, endPoint: .bottom))
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

    /// JAI'nin ana sayfadaki selamı: günün saatine ve öğrencinin durumuna göre değişir.
    private var greeting: String {
        let name = model.state.name.isEmpty ? "" : ", \(model.state.name)"
        let hour = Calendar.current.component(.hour, from: .now)
        let hello = hour < 12 ? "Günaydın" : hour < 18 ? "Merhaba" : "İyi akşamlar"
        let progress = model.state.progress
        if progress.goalReachedToday { return "Bugünkü hedef tamam\(name)! Harika gidiyorsunuz." }
        let due = model.dueCards().count
        if due >= 10 { return "\(hello)\(name)! \(due) kelime kartı tekrarınızı bekliyor." }
        let streak = progress.displayedStreak(at: .now)
        if streak > 0 { return "\(hello)\(name)! \(streak) günlük serinizi bugün de sürdürelim." }
        return "\(hello)\(name)! Bugün yeni bir şey öğrenmeye hazır mısınız?"
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
            .padding(.horizontal, 20)
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
                HStack(spacing: 4) {
                    Image(systemName: "flame.fill")
                        .symbolEffect(.bounce, options: .repeat(2), value: progress.goalReachedToday)
                    RollingNumber(value: progress.displayedStreak(at: .now), suffix: " gün seri",
                                  font: .jakarta(.subheadline, weight: .bold))
                }
                .foregroundStyle(progress.displayedStreak(at: .now) > 0 ? Theme.streak : .secondary)
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
            }
            .buttonStyle(DepthButtonStyle(color: .white, foreground: Theme.accent))
        }
        .padding(18)
        .background {
            ZStack(alignment: .topTrailing) {
                LinearGradient(colors: [Theme.accent, Theme.color(for: unit.level)],
                               startPoint: .topLeading, endPoint: .bottomTrailing)
                // Arka plandaki büyük, yarı saydam simge karta derinlik verir.
                Image(systemName: "graduationcap.fill")
                    .font(.system(size: 120, weight: .black))
                    .foregroundStyle(.white.opacity(0.12))
                    .rotationEffect(.degrees(-12))
                    .offset(x: 30, y: -10)
            }
            .clipShape(RoundedRectangle(cornerRadius: 22, style: .continuous))
        }
        .shadow(color: Theme.accent.opacity(0.3), radius: 14, y: 8)
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

/// Kart şeklindeki gezinme bağlantıları için: basılınca hafifçe küçülür.
struct PressableCardStyle: ButtonStyle {
    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .scaleEffect(configuration.isPressed ? 0.97 : 1)
            .brightness(configuration.isPressed ? -0.03 : 0)
            .animation(Motion.press, value: configuration.isPressed)
    }
}

/// Ana sayfanın en üstündeki satır: seviye, seri, toplam XP ve seri koruyucu.
struct StatsBar: View {
    @Environment(AppModel.self) private var model

    var body: some View {
        let progress = model.state.progress
        let streak = progress.displayedStreak(at: .now)
        HStack(spacing: 10) {
            chip(color: Theme.color(for: model.state.currentLevel)) {
                Text(model.state.currentLevel.rawValue).font(.jakarta(.subheadline, weight: .heavy))
            }
            Spacer()
            chip(color: streak > 0 ? Theme.streak : .secondary) {
                Image(systemName: "flame.fill")
                    .symbolEffect(.bounce, value: streak)
                RollingNumber(value: streak, font: .jakarta(.subheadline, weight: .heavy))
            }
            chip(color: Theme.warning) {
                Image(systemName: "bolt.fill")
                RollingNumber(value: progress.totalXP, font: .jakarta(.subheadline, weight: .heavy))
            }
            chip(color: Theme.ink) {
                Image(systemName: "snowflake")
                RollingNumber(value: progress.freezesAvailable, font: .jakarta(.subheadline, weight: .heavy))
            }
        }
    }

    private func chip<Content: View>(color: Color, @ViewBuilder _ content: () -> Content) -> some View {
        HStack(spacing: 4) { content() }
            .foregroundStyle(color)
            .padding(.horizontal, 10)
            .padding(.vertical, 6)
            .background(.ultraThinMaterial, in: Capsule())
            .overlay(Capsule().stroke(color.opacity(0.25), lineWidth: 1))
    }
}

import SwiftUI
import JECore

/// İlk açılış: karşılama → ad → günlük hedef → seviye (sınav ya da başlangıçtan).
struct OnboardingView: View {
    @Environment(AppModel.self) private var model

    private enum Step { case welcome, name, goal, level, placement }

    @State private var step: Step = .welcome
    @State private var name = ""
    @State private var goal: DailyGoal = .regular
    @State private var hop = 0
    @FocusState private var nameFocused: Bool

    var body: some View {
        ZStack {
            Theme.background.ignoresSafeArea()
            AuroraBackground(intensity: step == .welcome ? 0.5 : 0.18)
                .animation(Motion.smooth, value: step)
            switch step {
            case .welcome: welcome
            case .name: nameStep
            case .goal: goalStep
            case .level: levelStep
            case .placement:
                PlacementTestView { result in
                    model.finishOnboarding(name: name, goal: goal, level: result.level, placement: result.level)
                } onCancel: {
                    step = .level
                }
            }
        }
        .animation(.snappy, value: step)
    }

    private var welcome: some View {
        VStack(spacing: 24) {
            Spacer()
            JAIView(mood: .happy, size: 170, bounceTrigger: hop)
                .onTapGesture { hop += 1; Haptics.tap() }
                .task {
                    // JAI kendini tanıtırken birkaç kez zıplar.
                    for _ in 0..<3 {
                        try? await Task.sleep(for: .seconds(1.4))
                        hop += 1
                    }
                }
            VStack(spacing: 10) {
                Text("Merhaba, ben JAI!")
                    .font(.jakarta(.largeTitle, weight: .heavy))
                    .multilineTextAlignment(.center)
                    .staggeredAppear(1, delay: 0.15)
                Text("Just English'te İngilizceyi birlikte öğreneceğiz: A1'den C2'ye 68 ünite, oyunlar ve öğretmenlerimizle canlı dersler. Hepsi ücretsiz.")
                    .font(.jakarta(.body, weight: .medium))
                    .foregroundStyle(.secondary)
                    .multilineTextAlignment(.center)
                    .staggeredAppear(2, delay: 0.15)
            }
            Spacer()
            Button("Başlayalım") { step = .name }
                .buttonStyle(.primary)
                .staggeredAppear(3, delay: 0.15)
        }
        .padding(24)
    }

    private var nameStep: some View {
        VStack(alignment: .leading, spacing: 20) {
            JAISays(text: "Size nasıl hitap edeyim?", mood: .talking)
            TextField("Adınız", text: $name)
                .font(.jakarta(.title3))
                .textContentType(.givenName)
                .submitLabel(.next)
                .focused($nameFocused)
                .onSubmit { step = .goal }
                .padding(16)
                .background(Theme.surface, in: RoundedRectangle(cornerRadius: 14))
            Spacer()
            Button("Devam") { step = .goal }.buttonStyle(.primary)
        }
        .padding(24)
        .onAppear { nameFocused = true }
    }

    private var goalStep: some View {
        VStack(alignment: .leading, spacing: 20) {
            JAISays(text: name.isEmpty ? "Günde ne kadar çalışmak istersiniz?" : "Tanıştığımıza memnun oldum, \(name)! Günde ne kadar çalışmak istersiniz?",
                    mood: .happy)
            Text("Her gün biraz çalışmak, haftada bir uzun çalışmaktan çok daha etkilidir. Hedefi sonra değiştirebilirsiniz.")
                .font(.jakarta(.subheadline))
                .foregroundStyle(.secondary)
            GoalPicker(selection: $goal)
            Spacer()
            Button("Devam") { step = .level }.buttonStyle(.primary)
        }
        .padding(24)
    }

    private var levelStep: some View {
        VStack(alignment: .leading, spacing: 16) {
            JAISays(text: "Nereden başlayalım?", mood: .thinking)
            Button { step = .placement } label: {
                optionCard(icon: "chart.bar.fill", title: "Seviye testine gir",
                           detail: "10 dakikalık uyarlanabilir test seviyenizi bulur ve sizi doğru üniteden başlatır.")
            }
            .buttonStyle(.plain)
            Button {
                model.finishOnboarding(name: name, goal: goal, level: .a1, placement: nil)
            } label: {
                optionCard(icon: "leaf.fill", title: "Sıfırdan başla",
                           detail: "İngilizceye yeni başlıyorsanız A1 Beginner ile başlayın.")
            }
            .buttonStyle(.plain)
            Spacer()
        }
        .padding(24)
    }

    private func optionCard(icon: String, title: String, detail: String) -> some View {
        HStack(spacing: 16) {
            Image(systemName: icon).font(.title).foregroundStyle(Theme.accent).frame(width: 40)
            VStack(alignment: .leading, spacing: 4) {
                Text(title).font(.jakarta(.headline))
                Text(detail).font(.jakarta(.subheadline)).foregroundStyle(.secondary)
            }
            Spacer()
            Image(systemName: "chevron.right").foregroundStyle(.tertiary)
        }
        .card()
    }
}

struct GoalPicker: View {
    @Binding var selection: DailyGoal

    var body: some View {
        VStack(spacing: 10) {
            ForEach(DailyGoal.allCases) { goal in
                Button {
                    selection = goal
                    Haptics.tap()
                } label: {
                    HStack {
                        Text(goal.title).font(.jakarta(.headline))
                        Spacer()
                        Text("Günde \(goal.minutes) dk · \(goal.xp) XP")
                            .font(.jakarta(.subheadline))
                            .foregroundStyle(.secondary)
                    }
                    .padding(16)
                    .background(selection == goal ? Theme.accent.opacity(0.12) : Theme.surface,
                                in: RoundedRectangle(cornerRadius: 14))
                    .overlay(RoundedRectangle(cornerRadius: 14)
                        .stroke(selection == goal ? Theme.accent : .clear, lineWidth: 2))
                }
                .buttonStyle(.plain)
            }
        }
    }
}

import SwiftUI
import JECore

/// İlk açılış: karşılama → ad → günlük hedef → seviye (sınav ya da başlangıçtan).
struct OnboardingView: View {
    @Environment(AppModel.self) private var model

    private enum Step { case welcome, name, goal, level, placement }

    @State private var step: Step = .welcome
    @State private var name = ""
    @State private var goal: DailyGoal = .regular
    @FocusState private var nameFocused: Bool

    var body: some View {
        ZStack {
            Theme.background.ignoresSafeArea()
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
            Image(systemName: "bubble.left.and.text.bubble.right.fill")
                .font(.system(size: 80))
                .foregroundStyle(Theme.accent)
            VStack(spacing: 10) {
                Text("Just English'e hoş geldiniz").font(.jakarta(.largeTitle, weight: .bold)).multilineTextAlignment(.center)
                Text("A1'den C2'ye 68 ünite, kelime kartları, oyunlar ve öğretmenlerimizle canlı dersler. Tamamen ücretsiz.")
                    .font(.jakarta(.body))
                    .foregroundStyle(.secondary)
                    .multilineTextAlignment(.center)
            }
            Spacer()
            Button("Başlayalım") { step = .name }.buttonStyle(.primary)
        }
        .padding(24)
    }

    private var nameStep: some View {
        VStack(alignment: .leading, spacing: 20) {
            Text("Size nasıl hitap edelim?").font(.jakarta(.title, weight: .bold))
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
            Text("Günlük hedefiniz").font(.jakarta(.title, weight: .bold))
            Text("Her gün biraz çalışmak, haftada bir uzun çalışmaktan çok daha etkilidir. Hedefi sonra değiştirebilirsiniz.")
                .font(.jakarta(.body))
                .foregroundStyle(.secondary)
            GoalPicker(selection: $goal)
            Spacer()
            Button("Devam") { step = .level }.buttonStyle(.primary)
        }
        .padding(24)
    }

    private var levelStep: some View {
        VStack(alignment: .leading, spacing: 16) {
            Text("Nereden başlayalım?").font(.jakarta(.title, weight: .bold))
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

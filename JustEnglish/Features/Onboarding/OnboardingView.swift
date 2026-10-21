import AuthenticationServices
import SwiftUI
import JECore

/// İlk açılış: karşılama → ad → günlük hedef → seviye (sınav ya da başlangıçtan).
/// "Zaten hesabım var" Apple ile girişi açar; buluttaki ilerleme gelince uygulama doğrudan ana sayfaya geçer.
struct OnboardingView: View {
    @Environment(AppModel.self) private var model

    private enum Step: Int { case welcome, name, goal, level, placement }

    @State private var step: Step = .welcome
    @State private var name = ""
    @State private var goal: DailyGoal = .regular
    @State private var showSignIn = false
    @FocusState private var nameFocused: Bool

    var body: some View {
        ZStack {
            AIBackground(animated: true)
            switch step {
            case .welcome: welcome.transition(.opacity)
            case .name, .goal, .level:
                questionStep.transition(.asymmetric(insertion: .move(edge: .trailing), removal: .move(edge: .leading)).combined(with: .opacity))
            case .placement:
                PlacementTestView { result in
                    model.finishOnboarding(name: name, goal: goal, level: result.level, placement: result.level)
                } onCancel: {
                    step = .level
                }
            }
        }
        .animation(Motion.smooth, value: step)
        .sheet(isPresented: $showSignIn) { SignInSheet() }
    }

    // MARK: - Karşılama

    private var welcome: some View {
        VStack(spacing: 0) {
            WelcomeIllustration()
                .frame(maxHeight: .infinity)
            VStack(spacing: 12) {
                Text("Yapay zekâ ile daha akıllı öğrenin, daha hızlı konuşun")
                    .font(.jakarta(.title, weight: .heavy))
                    .foregroundStyle(Theme.ink)
                    .multilineTextAlignment(.center)
                    .staggeredAppear(1, delay: 0.12)
                Text("JAI ile İngilizceyi size göre, eğlenceli ve hızlı öğrenin. A1'den C2'ye 68 ünite, oyunlar ve canlı dersler; hepsi ücretsiz.")
                    .font(.jakarta(.callout, weight: .medium))
                    .foregroundStyle(.secondary)
                    .multilineTextAlignment(.center)
                    .staggeredAppear(2, delay: 0.12)
            }
            .padding(.horizontal, 8)
            .padding(.bottom, 28)
            VStack(spacing: 12) {
                Button("Başlayalım") { step = .name }
                    .buttonStyle(.primary)
                Button("Zaten hesabım var") { showSignIn = true }
                    .buttonStyle(.outline)
            }
            .staggeredAppear(3, delay: 0.12)
        }
        .padding(24)
    }

    // MARK: - Sorular

    private var questionStep: some View {
        ZStack(alignment: .top) {
            FadedPhraseCards()
                .padding(.top, 220)
            VStack(alignment: .leading, spacing: 18) {
                HStack {
                    Button {
                        step = Step(rawValue: step.rawValue - 1) ?? .welcome
                    } label: {
                        Image(systemName: "arrow.left")
                            .font(.system(size: 17, weight: .bold))
                            .foregroundStyle(Theme.ink)
                            .frame(width: 44, height: 44)
                            .glassCapsule(interactive: true)
                    }
                    .accessibilityLabel("Geri")
                    Spacer()
                    StepDots(current: step.rawValue - 1, total: 3)
                }
                Text(heading)
                    .font(.jakarta(.title, weight: .heavy))
                    .foregroundStyle(Theme.ink)
                    .fixedSize(horizontal: false, vertical: true)
                    .id(step)
                    .transition(.opacity.combined(with: .move(edge: .bottom)))
                Group {
                    switch step {
                    case .name: nameField
                    case .goal: GoalPicker(selection: $goal)
                    case .level: levelOptions
                    default: EmptyView()
                    }
                }
                .transition(.opacity)
                Spacer()
                if step != .level {
                    Button(step == .name ? "Devam edelim" : "Hadi başlayalım") {
                        step = step == .name ? .goal : .level
                    }
                    .buttonStyle(.primary)
                }
            }
            .padding(24)
        }
    }

    private var heading: String {
        switch step {
        case .name: "Merhaba!\nJust English'e hoş geldiniz. Başlamadan önce sizi biraz tanımak isteriz."
        case .goal: name.isEmpty ? "Günde ne kadar çalışmak istersiniz?" : "Tanıştığımıza memnun oldum, \(name)! Günde ne kadar çalışmak istersiniz?"
        default: "Nereden başlayalım?"
        }
    }

    private var nameField: some View {
        VStack(alignment: .leading, spacing: 8) {
            Text("Size nasıl hitap edelim?")
                .font(.jakarta(.subheadline, weight: .semibold))
                .foregroundStyle(.secondary)
            TextField("Adınız", text: $name)
                .font(.jakarta(.title3, weight: .semibold))
                .textContentType(.givenName)
                .submitLabel(.next)
                .focused($nameFocused)
                .onSubmit { step = .goal }
                .padding(18)
                .background(Theme.surface, in: RoundedRectangle(cornerRadius: 18, style: .continuous))
                .overlay(RoundedRectangle(cornerRadius: 18, style: .continuous)
                    .stroke(nameFocused ? Theme.accent : Theme.hairline, lineWidth: nameFocused ? 2 : 1))
                .animation(Motion.smooth, value: nameFocused)
        }
        .onAppear { nameFocused = true }
    }

    private var levelOptions: some View {
        VStack(spacing: 12) {
            Button { step = .placement } label: {
                optionCard(emoji: "🎯", title: "Seviye testine girin",
                           detail: "10 dakikalık uyarlanabilir test seviyenizi bulur ve sizi doğru üniteden başlatır.", tint: Theme.accent)
            }
            .buttonStyle(PressableCardStyle())
            Button {
                model.finishOnboarding(name: name, goal: goal, level: .a1, placement: nil)
            } label: {
                optionCard(emoji: "🌱", title: "Sıfırdan başlayın",
                           detail: "İngilizceye yeni başlıyorsanız A1 Beginner ile başlayın.", tint: Theme.success)
            }
            .buttonStyle(PressableCardStyle())
        }
    }

    private func optionCard(emoji: String, title: String, detail: String, tint: Color) -> some View {
        HStack(spacing: 16) {
            Text(emoji)
                .font(.system(size: 30))
                .frame(width: 56, height: 56)
                .background(tint.opacity(0.12), in: RoundedRectangle(cornerRadius: 16, style: .continuous))
            VStack(alignment: .leading, spacing: 4) {
                Text(title).font(.jakarta(.headline, weight: .bold)).foregroundStyle(Theme.ink)
                Text(detail).font(.jakarta(.subheadline)).foregroundStyle(.secondary)
            }
            Spacer()
            Image(systemName: "chevron.right").font(.jakarta(.subheadline, weight: .bold)).foregroundStyle(.tertiary)
        }
        .card()
    }
}

// MARK: - Parçalar

/// Karşılama görseli: cam kubbe içinde JAI, çevresinde süzülen dil balonları ve sinir ağı.
struct WelcomeIllustration: View {
    @State private var float = false
    @State private var hop = 0
    @Environment(\.accessibilityReduceMotion) private var reduceMotion

    private let bubbles: [(text: String, x: CGFloat, y: CGFloat, tint: Color)] = [
        ("🇬🇧 Hello!", -0.28, -0.32, Theme.accent),
        ("🇹🇷 Merhaba!", 0.27, -0.24, Theme.brandRed),
        ("How are you?", -0.3, 0.14, Theme.aiViolet),
        ("Nasılsınız?", 0.3, 0.2, Theme.success),
    ]

    var body: some View {
        GeometryReader { geo in
            let size = min(geo.size.width, geo.size.height)
            ZStack {
                // Referanstaki gibi karakterin çevresinde yumuşak ağ noktaları.
                NeuralNetwork(color: Theme.accent)
                    .frame(width: size * 0.95, height: size * 1.7)
                    .offset(y: size * 0.3)
                    .opacity(0.7)
                Circle()
                    .fill(Theme.accent.opacity(0.18))
                    .frame(width: size * 0.62)
                    .blur(radius: 30)
                Circle()
                    .fill(.white.opacity(0.4))
                    .frame(width: size * 0.5, height: size * 0.5)
                    .glass(cornerRadius: size * 0.25)
                JAIView(mood: .happy, size: size * 0.36, bounceTrigger: hop)
                    .onTapGesture { hop += 1; Haptics.tap() }
                ForEach(Array(bubbles.enumerated()), id: \.offset) { index, bubble in
                    Text(bubble.text)
                        .font(.jakarta(.subheadline, weight: .bold))
                        .foregroundStyle(bubble.tint)
                        .padding(.horizontal, 14)
                        .padding(.vertical, 9)
                        .glassCapsule()
                        .offset(x: bubble.x * geo.size.width,
                                y: bubble.y * size + (float ? -6 : 6) * (index.isMultiple(of: 2) ? 1 : -1))
                        .staggeredAppear(index + 1, delay: 0.15)
                }
            }
            .frame(width: geo.size.width, height: geo.size.height)
        }
        .onAppear {
            guard !reduceMotion else { return }
            withAnimation(.easeInOut(duration: 2.4).repeatForever(autoreverses: true)) { float = true }
        }
        .task {
            for _ in 0..<2 {
                try? await Task.sleep(for: .seconds(1.6))
                hop += 1
            }
        }
        .accessibilityHidden(true)
    }
}

/// Soru adımlarının arka planında yukarı doğru süzülen, soluk ifade kartları (referans ekran 2).
struct FadedPhraseCards: View {
    private let phrases: [(en: String, tr: String, flag: String, tint: Color)] = [
        ("How are you?", "Nasılsınız?", "🇬🇧", Theme.accent),
        ("Nice to meet you", "Tanıştığımıza memnun oldum", "🇺🇸", Theme.success),
        ("Where are you from?", "Nerelisiniz?", "🇬🇧", Theme.warning),
        ("I'm fine, thanks", "İyiyim, teşekkürler", "🇨🇦", Theme.aiViolet),
        ("See you soon!", "Görüşmek üzere!", "🇦🇺", Theme.color(for: .a2)),
        ("Good morning", "Günaydın", "🇮🇪", Theme.coral),
    ]
    @State private var drift = false
    @Environment(\.accessibilityReduceMotion) private var reduceMotion

    var body: some View {
        HStack(alignment: .top, spacing: 14) {
            column(Array(phrases.enumerated().filter { $0.offset.isMultiple(of: 2) }.map(\.element)))
            column(Array(phrases.enumerated().filter { !$0.offset.isMultiple(of: 2) }.map(\.element)))
                .padding(.top, 60)
        }
        .padding(.horizontal, 24)
        .offset(y: drift ? -30 : 0)
        .opacity(0.35)
        .mask(LinearGradient(colors: [.clear, .black, .black, .clear], startPoint: .top, endPoint: .bottom))
        .allowsHitTesting(false)
        .accessibilityHidden(true)
        .onAppear {
            guard !reduceMotion else { return }
            withAnimation(.easeInOut(duration: 6).repeatForever(autoreverses: true)) { drift = true }
        }
    }

    private func column(_ items: [(en: String, tr: String, flag: String, tint: Color)]) -> some View {
        VStack(spacing: 14) {
            ForEach(items, id: \.en) { item in
                VStack(spacing: 8) {
                    Text(item.flag)
                        .font(.system(size: 16))
                        .padding(.horizontal, 14)
                        .padding(.vertical, 6)
                        .background(item.tint.opacity(0.25), in: Capsule())
                    Text(item.en).font(.jakarta(.headline, weight: .bold)).foregroundStyle(item.tint)
                    Text(item.tr).font(.jakarta(.subheadline, weight: .medium)).foregroundStyle(.secondary)
                }
                .multilineTextAlignment(.center)
                .frame(maxWidth: .infinity)
                .padding(.vertical, 22)
                .background(Theme.surface, in: RoundedRectangle(cornerRadius: 22, style: .continuous))
            }
        }
    }
}

/// Adım göstergesi: geçerli adım uzun bir hap, diğerleri nokta.
struct StepDots: View {
    let current: Int
    let total: Int

    var body: some View {
        HStack(spacing: 6) {
            ForEach(0..<total, id: \.self) { i in
                Capsule()
                    .fill(i <= current ? Theme.accent : Theme.hairline)
                    .frame(width: i == current ? 24 : 8, height: 8)
            }
        }
        .animation(Motion.pop, value: current)
        .accessibilityLabel("Adım \(current + 1) / \(total)")
    }
}

struct GoalPicker: View {
    @Binding var selection: DailyGoal

    private func emoji(_ goal: DailyGoal) -> String {
        switch goal {
        case .casual: "🌿"
        case .regular: "🔥"
        case .serious: "🚀"
        }
    }

    var body: some View {
        VStack(spacing: 12) {
            ForEach(DailyGoal.allCases) { goal in
                let selected = selection == goal
                Button {
                    withAnimation(Motion.pop) { selection = goal }
                    Haptics.tap()
                } label: {
                    HStack(spacing: 14) {
                        Text(emoji(goal))
                            .font(.system(size: 26))
                            .frame(width: 48, height: 48)
                            .background((selected ? Theme.accent : Theme.ai).opacity(0.12), in: RoundedRectangle(cornerRadius: 14, style: .continuous))
                        VStack(alignment: .leading, spacing: 2) {
                            Text(goal.title).font(.jakarta(.headline, weight: .bold)).foregroundStyle(Theme.ink)
                            Text("Günde \(goal.minutes) dakika · \(goal.xp) XP")
                                .font(.jakarta(.subheadline))
                                .foregroundStyle(.secondary)
                        }
                        Spacer()
                        Image(systemName: selected ? "checkmark.circle.fill" : "circle")
                            .font(.system(size: 22))
                            .foregroundStyle(selected ? Theme.accent : Color(uiColor: .systemGray3))
                            .contentTransition(.symbolEffect(.replace))
                    }
                    .padding(14)
                    .background(selected ? Theme.accentSoft : Theme.surface, in: RoundedRectangle(cornerRadius: 20, style: .continuous))
                    .overlay(RoundedRectangle(cornerRadius: 20, style: .continuous)
                        .stroke(selected ? Theme.accent : Theme.hairline, lineWidth: selected ? 2 : 1))
                    .scaleEffect(selected ? 1.02 : 1)
                }
                .buttonStyle(PressableCardStyle())
            }
        }
    }
}

/// "Zaten hesabım var": Apple ile giriş. Buluttaki ilerleme varsa eşitleme sonrası ana sayfa açılır.
struct SignInSheet: View {
    @Environment(AppModel.self) private var model
    @Environment(AuthService.self) private var auth
    @Environment(\.dismiss) private var dismiss

    var body: some View {
        VStack(spacing: 18) {
            JAIView(mood: .happy, size: 90)
                .padding(.top, 28)
            Text("Tekrar hoş geldiniz!")
                .font(.jakarta(.title2, weight: .heavy))
                .foregroundStyle(Theme.ink)
            Text("Apple ile giriş yapın; ilerlemeniz bu cihaza gelsin.")
                .font(.jakarta(.callout, weight: .medium))
                .foregroundStyle(.secondary)
                .multilineTextAlignment(.center)
            Spacer()
            if Backend.isConfigured {
                SignInWithAppleButton(.signIn) { auth.prepare($0) } onCompletion: { result in
                    Task {
                        let name = await auth.complete(result)
                        if model.state.name.isEmpty, let given = name?.givenName { model.state.name = given }
                        if let id = auth.userID { await SyncService.sync(model, userID: id) }
                        if auth.isSignedIn { dismiss() }
                    }
                }
                .signInWithAppleButtonStyle(.black)
                .frame(height: 54)
                .clipShape(RoundedRectangle(cornerRadius: 16, style: .continuous))
                if let error = auth.error {
                    Text(error).font(.jakarta(.footnote)).foregroundStyle(Theme.danger)
                }
            } else {
                Label("Bulut hesabı bu sürümde kapalı. Yeni başlayarak devam edebilirsiniz.", systemImage: "icloud.slash")
                    .font(.jakarta(.subheadline, weight: .medium))
                    .foregroundStyle(.secondary)
                    .padding(14)
                    .frame(maxWidth: .infinity)
                    .glass(cornerRadius: 16)
            }
            Button("Vazgeç") { dismiss() }.buttonStyle(.outline)
        }
        .padding(24)
        .background { AIBackground(animated: false) }
        .presentationDetents([.medium, .large])
        .presentationDragIndicator(.visible)
    }
}

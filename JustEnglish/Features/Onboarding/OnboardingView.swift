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
            // Referans 1: düz, çok açık mavi zemin.
            Color(light: 0xEEF4FF, dark: 0x0B0D16).ignoresSafeArea()
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
            VStack(spacing: 14) {
                Text("Yapay zekâ ile daha akıllı öğrenin, daha hızlı konuşun")
                    .font(.custom(Theme.fontFamily, size: 27, relativeTo: .title).weight(.bold))
                    .foregroundStyle(Theme.ink)
                    .multilineTextAlignment(.center)
                    .fixedSize(horizontal: false, vertical: true)
                    .staggeredAppear(1, delay: 0.12)
                Text("JAI ile İngilizce öğrenmek eğlenceli, hızlı ve tamamen size göre.")
                    .font(.custom(Theme.fontFamily, size: 17, relativeTo: .body))
                    .foregroundStyle(Color(light: 0x4A4F5C, dark: 0x9AA3B5))
                    .lineSpacing(5)
                    .multilineTextAlignment(.center)
                    .fixedSize(horizontal: false, vertical: true)
                    .padding(.horizontal, 12)
                    .staggeredAppear(2, delay: 0.12)
            }
            .padding(.bottom, 56)
            VStack(spacing: 12) {
                Button("Başlayalım") { step = .name }
                    .buttonStyle(OnboardingButtonStyle(filled: true))
                Button("Zaten hesabım var") { showSignIn = true }
                    .buttonStyle(OnboardingButtonStyle(filled: false))
            }
            .staggeredAppear(3, delay: 0.12)
        }
        .padding(.horizontal, 20)
        .padding(.bottom, 24)
    }

    // MARK: - Sorular

    private var questionStep: some View {
        VStack(alignment: .leading, spacing: 18) {
            HStack {
                Button {
                    step = Step(rawValue: step.rawValue - 1) ?? .welcome
                } label: {
                    Image(systemName: "arrow.left")
                        .font(.system(size: 20, weight: .regular))
                        .foregroundStyle(Theme.ink)
                        .frame(width: 44, height: 44, alignment: .leading)
                }
                .accessibilityLabel("Geri")
                Spacer()
                StepDots(current: step.rawValue - 1, total: 3)
            }
            Text(heading)
                .font(.custom(Theme.fontFamily, size: 28, relativeTo: .title).weight(.bold))
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
                .buttonStyle(OnboardingButtonStyle(filled: true))
            }
        }
        .padding(.horizontal, 20)
        .padding(.top, 8)
        .padding(.bottom, 24)
        // Soluk kartlar arka planda, başlığın ve ad alanının altından başlar; yazıların arkasına binmez
        // ve sayfanın yüksekliğini etkilemez.
        .background(alignment: .top) {
            FadedPhraseCards()
                .padding(.top, step == .name ? 400 : 300)
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

/// Referans 1'deki butonlar: 44pt, köşesi 10pt; dolu olan vurgu renginde ve altı 3pt koyu, boş olan ince mavi çerçeveli beyaz.
struct OnboardingButtonStyle: ButtonStyle {
    let filled: Bool

    func makeBody(configuration: Configuration) -> some View {
        let pressed = configuration.isPressed
        return configuration.label
            .font(.custom(Theme.fontFamily, size: 17, relativeTo: .headline).weight(.medium))
            .foregroundStyle(filled ? .white : Theme.accent)
            .frame(maxWidth: .infinity, minHeight: 46)
            .background(filled ? Theme.accent : Theme.surface, in: RoundedRectangle(cornerRadius: 10, style: .continuous))
            .overlay {
                if !filled {
                    RoundedRectangle(cornerRadius: 10, style: .continuous).stroke(Theme.accent.opacity(0.8), lineWidth: 1.5)
                }
            }
            .background {
                if filled {
                    RoundedRectangle(cornerRadius: 10, style: .continuous).fill(Theme.accentDeep).offset(y: pressed ? 0 : 3)
                }
            }
            .offset(y: filled && pressed ? 3 : 0)
            .animation(Motion.press, value: pressed)
    }
}

/// Karşılama görseli (referans 1): ortada cam kubbe içinde JAI, üstünde bayraklı konuşma balonları,
/// çevresinde yumuşak sinir ağı noktaları. Balonlar hafifçe süzülür.
struct WelcomeIllustration: View {
    @State private var float = false
    @State private var hop = 0
    @Environment(\.accessibilityReduceMotion) private var reduceMotion

    /// Konum: görsel genişliğine/yüksekliğine oranla merkezden; boyut: genişliğe oranla.
    private let bubbles: [(flag: String, x: CGFloat, y: CGFloat, size: CGFloat, tint: Color, tailLeft: Bool)] = [
        ("🇬🇧", -0.22, -0.20, 0.18, Color(light: 0x4F7BEF, dark: 0x4F7BEF), false),
        ("🇺🇸", 0.02, -0.29, 0.21, Color(light: 0x4CC46A, dark: 0x4CC46A), true),
        ("🇹🇷", 0.24, -0.10, 0.15, Color(light: 0xF5C443, dark: 0xF5C443), true),
        ("🇦🇺", -0.29, 0.06, 0.11, Color(light: 0x6E8BFF, dark: 0x6E8BFF), false),
    ]

    var body: some View {
        GeometryReader { geo in
            let w = geo.size.width, h = geo.size.height
            ZStack {
                NeuralNetwork(color: Theme.accent)
                    .frame(width: w * 0.95, height: h * 0.8)
                    .offset(y: h * 0.05)
                    .opacity(0.55)
                Circle()
                    .fill(Theme.accent.opacity(0.14))
                    .frame(width: w * 0.62)
                    .blur(radius: 34)
                    .offset(y: h * 0.12)
                ZStack {
                    Circle()
                        .fill(RadialGradient(colors: [.white.opacity(0.95), Color(light: 0xC9DBFF, dark: 0x2A3A70).opacity(0.6)],
                                             center: .topLeading, startRadius: 4, endRadius: w * 0.4))
                        .overlay(Circle().stroke(.white.opacity(0.9), lineWidth: 1.5))
                        .frame(width: w * 0.46, height: w * 0.46)
                        .shadow(color: Theme.accent.opacity(0.2), radius: 18, y: 10)
                    JAIView(mood: .happy, size: w * 0.34, bounceTrigger: hop)
                }
                .offset(y: h * 0.14)
                .onTapGesture { hop += 1; Haptics.tap() }
                ForEach(Array(bubbles.enumerated()), id: \.offset) { index, bubble in
                    FlagBubble(flag: bubble.flag, tint: bubble.tint, size: w * bubble.size, tailLeft: bubble.tailLeft)
                        .offset(x: bubble.x * w,
                                y: bubble.y * h + (float ? -5 : 5) * (index.isMultiple(of: 2) ? 1 : -1))
                        .staggeredAppear(index + 1, delay: 0.15)
                }
            }
            .frame(width: w, height: h)
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

/// İçinde bayrak olan yuvarlak konuşma balonu; alt köşesinde küçük bir kuyruk.
struct FlagBubble: View {
    let flag: String
    let tint: Color
    let size: CGFloat
    var tailLeft = false

    var body: some View {
        ZStack {
            Circle()
                .fill(LinearGradient(colors: [tint.blended(with: .white, amount: 0.25), tint], startPoint: .top, endPoint: .bottom))
                .shadow(color: tint.opacity(0.35), radius: 8, y: 5)
            Text(flag).font(.system(size: size * 0.48))
        }
        .frame(width: size, height: size)
        .overlay(alignment: tailLeft ? .bottomLeading : .bottomTrailing) {
            Image(systemName: "arrowtriangle.down.fill")
                .font(.system(size: size * 0.26))
                .foregroundStyle(tint)
                .rotationEffect(.degrees(tailLeft ? 30 : -30))
                .offset(x: tailLeft ? size * 0.12 : -size * 0.12, y: size * 0.06)
        }
    }
}

/// Soru adımlarının arka planında yukarı doğru süzülen, soluk ifade kartları (referans ekran 2).
struct FadedPhraseCards: View {
    private let phrases: [(en: String, tr: String, flag: String, tint: Color)] = [
        ("How are you?", "Nasılsınız?", "🇬🇧 UK", Theme.accent),
        ("Nice to meet you", "Tanıştığımıza memnun oldum", "🇺🇸 US", Theme.success),
        ("Where are you from?", "Nerelisiniz?", "🇬🇧 UK", Theme.warning),
        ("I'm fine, thanks", "İyiyim, teşekkürler", "🇨🇦 CA", Theme.aiViolet),
        ("See you soon!", "Görüşmek üzere!", "🇦🇺 AU", Theme.color(for: .a2)),
        ("Good morning", "Günaydın", "🇮🇪 IE", Theme.coral),
    ]
    @State private var drift = false
    @Environment(\.accessibilityReduceMotion) private var reduceMotion

    var body: some View {
        HStack(alignment: .top, spacing: 14) {
            column(Array(phrases.enumerated().filter { $0.offset.isMultiple(of: 2) }.map(\.element)))
            column(Array(phrases.enumerated().filter { !$0.offset.isMultiple(of: 2) }.map(\.element)))
                .padding(.top, 60)
        }
        // Arka planda durduğu için yüksekliği sınırlanmasın; kartlar kendi doğal yüksekliklerini alır, yazı kesilmez.
        .fixedSize(horizontal: false, vertical: true)
        .padding(.horizontal, 4)
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
                        .font(.custom(Theme.fontFamily, size: 16, relativeTo: .callout).weight(.semibold))
                        .foregroundStyle(.white)
                        .padding(.horizontal, 14)
                        .padding(.vertical, 8)
                        .background(item.tint, in: Capsule())
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

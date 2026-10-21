import AuthenticationServices
import SwiftUI
import JECore

struct ProfileView: View {
    @Environment(AppModel.self) private var model
    @Environment(AuthService.self) private var auth
    @State private var confirmReset = false
    @State private var confirmDelete = false
    @State private var showPlacement = false

    var body: some View {
        @Bindable var model = model
        NavigationStack {
            ScrollView {
                VStack(spacing: 22) {
                    hero
                    statsGrid
                    NavigationLink { LeagueView() } label: { leagueCard }
                        .buttonStyle(PressableCardStyle())
                        .staggeredAppear(2)
                    VStack(alignment: .leading, spacing: 12) {
                        sectionTitle("Seviye yolculuğunuz")
                        LevelJourney()
                    }
                    VStack(alignment: .leading, spacing: 12) {
                        sectionTitle("Rozetler")
                        AchievementsGrid()
                    }
                    studyCard
                    accountCard
                    VStack(spacing: 8) {
                        Button("Tüm ilerlemeyi sıfırla", role: .destructive) { confirmReset = true }
                            .font(.custom(Theme.fontFamily, size: 15, relativeTo: .subheadline).weight(.semibold))
                            .foregroundStyle(Theme.danger)
                        Text("Sürüm \(Bundle.main.object(forInfoDictionaryKey: "CFBundleShortVersionString") as? String ?? "")")
                            .font(.custom(Theme.fontFamily, size: 13, relativeTo: .caption))
                            .foregroundStyle(HomeStyle.body)
                    }
                    .padding(.top, 4)
                }
                .padding(.horizontal, 16)
                .padding(.bottom, 20)
                .background(alignment: .top) {
                    // Ana sayfadaki gibi üstte doygun mavi bant; kaydırınca içerikle birlikte kayar.
                    HomeStyle.band.frame(height: 340).padding(.horizontal, -16)
                }
            }
            .tabBarSpacer()
            .background(HomeStyle.page.ignoresSafeArea())
            // Gezinme çubuğu gizli; durum çubuğunun arkası bandın en üst rengiyle dolu.
            .safeAreaInset(edge: .top, spacing: 0) {
                Color.clear.frame(height: 0).background(HomeStyle.bandTop, ignoresSafeAreaEdges: .top)
            }
            .toolbar(.hidden, for: .navigationBar)
            .confirmationDialog("Tüm ilerlemeniz silinsin mi?", isPresented: $confirmReset, titleVisibility: .visible) {
                Button("Sıfırla", role: .destructive) { model.resetAll() }
            } message: {
                Text("Bu cihazdaki dersler, kartlar ve seri silinir. Bu işlem geri alınamaz.")
            }
            .confirmationDialog("Hesabınız silinsin mi?", isPresented: $confirmDelete, titleVisibility: .visible) {
                Button("Hesabı sil", role: .destructive) {
                    Task { if await auth.deleteAccount() { model.resetAll() } }
                }
            } message: {
                Text("Buluttaki ilerlemeniz ve canlı ders kayıtlarınız kalıcı olarak silinir.")
            }
            .fullScreenCover(isPresented: $showPlacement) {
                PlacementTestView { result in
                    model.state.placementLevel = result.level
                    model.state.currentLevel = result.level
                    showPlacement = false
                } onCancel: {
                    showPlacement = false
                }
            }
        }
    }

    // MARK: - Bölümler

    private func sectionTitle(_ text: String) -> some View {
        Text(text)
            .font(.custom(Theme.fontFamily, size: 20, relativeTo: .title3).weight(.bold))
            .foregroundStyle(HomeStyle.title)
            .frame(maxWidth: .infinity, alignment: .leading)
    }

    /// Mavi bant üzerinde beyaz yuvarlak içinde baş harf, ad, seviye ve iki küçük sayaç.
    private var hero: some View {
        let level = model.state.currentLevel
        return VStack(spacing: 10) {
            AnimatedAvatar(initial: String(model.state.name.prefix(1)).uppercased().ifEmpty("?"))
            Text(model.state.name.ifEmpty("Öğrenci"))
                .font(.custom(Theme.fontFamily, size: 24, relativeTo: .title2).weight(.bold))
                .foregroundStyle(.white)
            Text("\(level.rawValue) · \(level.title) seviyesinde çalışıyorsunuz")
                .font(.custom(Theme.fontFamily, size: 15, relativeTo: .subheadline))
                .foregroundStyle(.white.opacity(0.9))
            HStack(spacing: 8) {
                heroChip("🔥", "\(model.state.progress.displayedStreak(at: .now)) gün seri")
                heroChip("⚡", "\(model.state.progress.weekXP(at: .now)) XP bu hafta")
            }
            .padding(.top, 4)
        }
        .frame(maxWidth: .infinity)
        .padding(.top, 18)
    }

    private func heroChip(_ emoji: String, _ text: String) -> some View {
        HStack(spacing: 6) {
            Text(emoji).font(.system(size: 14))
            Text(text)
                .font(.custom(Theme.fontFamily, size: 14, relativeTo: .footnote).weight(.semibold))
                .foregroundStyle(.white)
        }
        .padding(.horizontal, 12)
        .frame(height: 32)
        .background(.white.opacity(0.25), in: Capsule())
    }

    /// Altı küçük beyaz kart: simge, sayı ve açıklama.
    private var statsGrid: some View {
        let p = model.state.progress
        return LazyVGrid(columns: Array(repeating: GridItem(.flexible(), spacing: 10), count: 3), spacing: 10) {
            statTile(.asset("fire"), p.displayedStreak(at: .now), "Gün serisi", 0)
            statTile(.asset("trophy"), p.longestStreak, "En uzun seri", 1)
            statTile(.asset("medal"), p.totalXP, "Toplam XP", 2)
            statTile(.asset("closedbook"), model.state.completedLessons.count, "Ders", 3)
            statTile(.asset("cards"), model.deckSize, "Kelime", 4)
            statTile(.emoji("❄️"), p.freezesAvailable, "Koruyucu", 5)
        }
    }

    private enum TileIcon { case asset(String), emoji(String) }

    private func statTile(_ icon: TileIcon, _ value: Int, _ label: String, _ index: Int) -> some View {
        VStack(spacing: 6) {
            Group {
                switch icon {
                case .asset(let name): Image("lesson-\(name)").resizable().scaledToFit()
                case .emoji(let emoji): Text(emoji).font(.system(size: 26))
                }
            }
            .frame(width: 32, height: 32)
            RollingNumber(value: value, font: .custom(Theme.fontFamily, size: 20, relativeTo: .title3).weight(.bold))
                .foregroundStyle(HomeStyle.title)
            Text(label)
                .font(.custom(Theme.fontFamily, size: 13, relativeTo: .caption))
                .foregroundStyle(HomeStyle.body)
                .lineLimit(1)
                .minimumScaleFactor(0.8)
        }
        .frame(maxWidth: .infinity)
        .padding(.vertical, 14)
        .modifier(HomeCard(radius: 16))
        .staggeredAppear(index, delay: 0.05)
        .accessibilityElement(children: .combine)
    }

    /// Ana sayfadaki "Haftalık lig" satırıyla aynı: açık gri zemin, 3B kupa, ok.
    private var leagueCard: some View {
        HStack(spacing: 14) {
            Image("lesson-trophy").resizable().scaledToFit().frame(width: 44, height: 44)
            VStack(alignment: .leading, spacing: 4) {
                Text("Haftalık lig")
                    .font(.custom(Theme.fontFamily, size: 16, relativeTo: .headline).weight(.semibold))
                    .foregroundStyle(HomeStyle.title)
                Text("Bu hafta \(model.state.progress.weekXP(at: .now)) XP. İlk 7 kişi bir üst lige çıkar.")
                    .font(.custom(Theme.fontFamily, size: 15, relativeTo: .subheadline))
                    .foregroundStyle(HomeStyle.body)
                    .fixedSize(horizontal: false, vertical: true)
            }
            Spacer(minLength: 4)
            Image(systemName: "chevron.right").font(.system(size: 15, weight: .semibold)).foregroundStyle(HomeStyle.title)
        }
        .padding(.leading, 14)
        .padding(.trailing, 18)
        .padding(.vertical, 12)
        .background(HomeStyle.rowFill, in: RoundedRectangle(cornerRadius: 16, style: .continuous))
    }

    /// Çalışma ayarları: günlük hedef, çalışılan seviye ve seviye testi; beyaz, kenarlıklı kart.
    private var studyCard: some View {
        @Bindable var model = model
        return VStack(alignment: .leading, spacing: 12) {
            sectionTitle("Çalışma ayarları")
            VStack(alignment: .leading, spacing: 14) {
                settingLabel("Günlük hedef")
                HStack(spacing: 8) {
                    ForEach(DailyGoal.allCases) { goal in
                        SoftChip(title: "\(goal.minutes) dk", selected: model.state.dailyGoal == goal) {
                            model.setDailyGoal(goal)
                        }
                    }
                }
                Divider().overlay(HomeStyle.cardBorder)
                HStack {
                    settingLabel("Çalıştığım seviye")
                    Spacer()
                    Menu {
                        Picker("Seviye", selection: $model.state.currentLevel) {
                            ForEach(CEFRLevel.allCases) { Text("\($0.rawValue) · \($0.title)").tag($0) }
                        }
                    } label: {
                        HStack(spacing: 6) {
                            LevelBadge(level: model.state.currentLevel)
                            Text(model.state.currentLevel.title)
                                .font(.custom(Theme.fontFamily, size: 15, relativeTo: .subheadline).weight(.semibold))
                            Image(systemName: "chevron.up.chevron.down").font(.caption)
                        }
                        .foregroundStyle(HomeStyle.title)
                        .padding(.horizontal, 12)
                        .frame(height: 36)
                        .background(HomeStyle.rowFill, in: Capsule())
                    }
                }
                Button { showPlacement = true } label: {
                    Label("Seviye testine tekrar girin", systemImage: "chart.bar")
                }
                .buttonStyle(OnboardingButtonStyle(filled: false))
                Text("Seri koruyucu, hedefi kaçırdığınız tek bir günü kapatır. Her pazartesi bir tane yenilenir.")
                    .font(.custom(Theme.fontFamily, size: 13, relativeTo: .caption))
                    .foregroundStyle(HomeStyle.body)
                    .fixedSize(horizontal: false, vertical: true)
            }
            .padding(16)
            .frame(maxWidth: .infinity, alignment: .leading)
            .modifier(HomeCard())
        }
    }

    private func settingLabel(_ text: String) -> some View {
        Text(text)
            .font(.custom(Theme.fontFamily, size: 15, relativeTo: .subheadline).weight(.semibold))
            .foregroundStyle(HomeStyle.title)
    }

    /// Hesap: giriş yapılmışsa e-posta, çıkış ve hesabı silme; değilse Apple ile giriş.
    private var accountCard: some View {
        VStack(alignment: .leading, spacing: 12) {
            sectionTitle("Hesap")
            VStack(alignment: .leading, spacing: 14) {
                if auth.isSignedIn {
                    HStack(spacing: 12) {
                        Image(systemName: "checkmark.icloud")
                            .font(.system(size: 18, weight: .medium))
                            .foregroundStyle(Theme.success)
                            .frame(width: 40, height: 40)
                            .background(Theme.successSoft, in: Circle())
                        VStack(alignment: .leading, spacing: 2) {
                            Text(auth.email ?? "Apple hesabı")
                                .font(.custom(Theme.fontFamily, size: 15, relativeTo: .subheadline).weight(.semibold))
                                .foregroundStyle(HomeStyle.title)
                                .lineLimit(1)
                            Text("İlerlemeniz yedekleniyor")
                                .font(.custom(Theme.fontFamily, size: 13, relativeTo: .caption))
                                .foregroundStyle(HomeStyle.body)
                        }
                    }
                    Button { Task { await auth.signOut() } } label: {
                        Label("Çıkış yap", systemImage: "rectangle.portrait.and.arrow.right")
                    }
                    .buttonStyle(OnboardingButtonStyle(filled: false))
                    Button("Hesabımı sil", role: .destructive) { confirmDelete = true }
                        .font(.custom(Theme.fontFamily, size: 15, relativeTo: .subheadline).weight(.semibold))
                        .foregroundStyle(Theme.danger)
                        .frame(maxWidth: .infinity)
                } else if Backend.isConfigured {
                    SignInWithAppleButton(.signIn) { auth.prepare($0) } onCompletion: { result in
                        Task { await signedIn(result) }
                    }
                    .frame(height: 50)
                    .clipShape(RoundedRectangle(cornerRadius: 10, style: .continuous))
                    if let error = auth.error {
                        Text(error)
                            .font(.custom(Theme.fontFamily, size: 14, relativeTo: .footnote))
                            .foregroundStyle(Theme.danger)
                    }
                } else {
                    Label("Bulut yedekleme bu sürümde kapalı.", systemImage: "icloud.slash")
                        .font(.custom(Theme.fontFamily, size: 15, relativeTo: .subheadline))
                        .foregroundStyle(HomeStyle.body)
                }
                Text("Giriş yapmak isteğe bağlıdır. Giriş yaparsanız ilerlemeniz yedeklenir, başka cihazda devam edebilir ve canlı derslere kaydolabilirsiniz.")
                    .font(.custom(Theme.fontFamily, size: 13, relativeTo: .caption))
                    .foregroundStyle(HomeStyle.body)
                    .fixedSize(horizontal: false, vertical: true)
            }
            .padding(16)
            .frame(maxWidth: .infinity, alignment: .leading)
            .modifier(HomeCard())
        }
    }

    private func signedIn(_ result: Result<ASAuthorization, Error>) async {
        let name = await auth.complete(result)
        if model.state.name.isEmpty, let given = name?.givenName { model.state.name = given }
        if let id = auth.userID { await SyncService.sync(model, userID: id) }
    }
}

extension String {
    func ifEmpty(_ fallback: String) -> String { isEmpty ? fallback : self }
}

/// Profil fotoğrafı yerine beyaz yuvarlak içinde baş harf; çevresinde yavaşça dönen yarı saydam beyaz halka.
struct AnimatedAvatar: View {
    let initial: String
    @State private var spin = false
    @Environment(\.accessibilityReduceMotion) private var reduceMotion

    var body: some View {
        ZStack {
            Circle()
                .stroke(AngularGradient(colors: [.white, .white.opacity(0.15), .white.opacity(0.6), .white], center: .center), lineWidth: 3)
                .frame(width: 86, height: 86)
                .rotationEffect(.degrees(spin ? 360 : 0))
            Text(initial)
                .font(.custom(Theme.fontFamily, size: 32, relativeTo: .largeTitle).weight(.bold))
                .foregroundStyle(Theme.accent)
                .frame(width: 74, height: 74)
                .background(.white, in: Circle())
        }
        .onAppear {
            guard !reduceMotion else { return }
            withAnimation(.linear(duration: 6).repeatForever(autoreverses: false)) { spin = true }
        }
        .accessibilityHidden(true)
    }
}

/// A1'den C2'ye altı durak: her durağın doluluğu o seviyede bitirilen derslerin oranıdır.
struct LevelJourney: View {
    @Environment(AppModel.self) private var model
    @State private var shown = false

    var body: some View {
        let current = model.state.currentLevel
        HStack(alignment: .top, spacing: 0) {
            ForEach(CEFRLevel.allCases) { level in
                let ratio = progress(level)
                let isCurrent = level == current
                VStack(spacing: 6) {
                    ZStack {
                        Circle().stroke(Theme.color(for: level).opacity(0.18), lineWidth: 5)
                        Circle()
                            .trim(from: 0, to: shown ? ratio : 0)
                            .stroke(Theme.color(for: level), style: StrokeStyle(lineWidth: 5, lineCap: .round))
                            .rotationEffect(.degrees(-90))
                            .animation(Motion.smooth.delay(Double(level.index) * 0.08), value: shown)
                        Text(level.rawValue)
                            .font(.custom(Theme.fontFamily, size: 13, relativeTo: .caption).weight(.bold))
                            .foregroundStyle(isCurrent ? .white : Theme.color(for: level))
                            .frame(width: 34, height: 34)
                            .background(isCurrent ? AnyShapeStyle(Theme.color(for: level).gradient) : AnyShapeStyle(Color.clear), in: Circle())
                    }
                    .frame(width: 46, height: 46)
                    .scaleEffect(isCurrent ? 1.1 : 1)
                    Text("%\(Int(ratio * 100))")
                        .font(.custom(Theme.fontFamily, size: 12, relativeTo: .caption2).weight(.medium))
                        .foregroundStyle(HomeStyle.body)
                }
                .frame(maxWidth: .infinity)
            }
        }
        .padding(.vertical, 16)
        .padding(.horizontal, 8)
        .modifier(HomeCard())
        .onAppear { shown = true }
    }

    private func progress(_ level: CEFRLevel) -> Double {
        let units = model.units(for: level)
        let total = units.map(\.lessons.count).reduce(0, +)
        guard total > 0 else { return 0 }
        return Double(units.map { model.completedCount(in: $0) }.reduce(0, +)) / Double(total)
    }
}

/// Basit başarı rozetleri; açılanlar renkli ve parlak, kilitliler gri.
struct AchievementsGrid: View {
    @Environment(AppModel.self) private var model

    private struct Badge: Identifiable {
        let id: String, icon: String, title: String, color: Color, unlocked: Bool
    }

    private var badges: [Badge] {
        let p = model.state.progress
        let lessons = model.state.completedLessons.count
        let passedUnits = model.units.filter { model.isUnitPassed($0) }.count
        return [
            Badge(id: "first", icon: "star.fill", title: "İlk ders", color: Theme.warning, unlocked: lessons >= 1),
            Badge(id: "ten", icon: "book.fill", title: "10 ders", color: Theme.accent, unlocked: lessons >= 10),
            Badge(id: "streak3", icon: "flame.fill", title: "3 gün seri", color: Theme.streak, unlocked: p.longestStreak >= 3),
            Badge(id: "streak7", icon: "calendar", title: "7 gün seri", color: Theme.color(for: .b2), unlocked: p.longestStreak >= 7),
            Badge(id: "xp500", icon: "bolt.fill", title: "500 XP", color: Theme.color(for: .c1), unlocked: p.totalXP >= 500),
            Badge(id: "words", icon: "rectangle.stack.fill", title: "50 kelime", color: Theme.color(for: .a2), unlocked: model.deckSize >= 50),
            Badge(id: "unit", icon: "checkmark.seal.fill", title: "Ünite testi", color: Theme.success, unlocked: passedUnits >= 1),
            Badge(id: "level", icon: "crown.fill", title: "Seviye atla", color: Theme.color(for: .c2), unlocked: model.state.currentLevel > (model.state.placementLevel ?? .a1)),
        ]
    }

    var body: some View {
        let list = badges
        VStack(alignment: .leading, spacing: 12) {
            Text("\(list.filter(\.unlocked).count)/\(list.count) rozet açıldı")
                .font(.custom(Theme.fontFamily, size: 14, relativeTo: .footnote).weight(.medium))
                .foregroundStyle(HomeStyle.body)
            LazyVGrid(columns: Array(repeating: GridItem(.flexible(), spacing: 8), count: 4), spacing: 14) {
                ForEach(Array(list.enumerated()), id: \.element.id) { index, badge in
                    VStack(spacing: 6) {
                        ZStack {
                            Hexagon()
                                .fill(badge.unlocked ? AnyShapeStyle(badge.color.gradient) : AnyShapeStyle(HomeStyle.rowFill))
                                .frame(width: 56, height: 60)
                                .shadow(color: badge.unlocked ? badge.color.opacity(0.25) : .clear, radius: 5, y: 3)
                            Image(systemName: badge.unlocked ? badge.icon : "lock.fill")
                                .font(.system(size: 20, weight: .bold))
                                .foregroundStyle(badge.unlocked ? .white : Color(light: 0xB8BFCC, dark: 0x4A5168))
                                .symbolEffect(.bounce, value: badge.unlocked)
                        }
                        Text(badge.title)
                            .font(.custom(Theme.fontFamily, size: 12, relativeTo: .caption2).weight(.medium))
                            .foregroundStyle(badge.unlocked ? HomeStyle.title : HomeStyle.body)
                            .lineLimit(1)
                            .minimumScaleFactor(0.8)
                    }
                    .staggeredAppear(index, delay: 0.04)
                    .accessibilityElement(children: .ignore)
                    .accessibilityLabel("\(badge.title), \(badge.unlocked ? "açıldı" : "kilitli")")
                }
            }
        }
        .padding(16)
        .modifier(HomeCard())
    }
}

/// Rozet zemini: köşeleri yumuşatılmış altıgen.
struct Hexagon: Shape {
    func path(in rect: CGRect) -> Path {
        let w = rect.width, h = rect.height
        let points = [CGPoint(x: w / 2, y: 0), CGPoint(x: w, y: h * 0.25), CGPoint(x: w, y: h * 0.75),
                      CGPoint(x: w / 2, y: h), CGPoint(x: 0, y: h * 0.75), CGPoint(x: 0, y: h * 0.25)]
        var path = Path()
        path.addLines(points.map { CGPoint(x: rect.minX + $0.x, y: rect.minY + $0.y) })
        path.closeSubpath()
        return path.strokedPath(StrokeStyle(lineWidth: 6, lineJoin: .round)).union(path)
    }
}

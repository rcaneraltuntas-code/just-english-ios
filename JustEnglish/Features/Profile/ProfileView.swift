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
                        SectionHeader(title: "Seviye yolculuğunuz")
                        LevelJourney()
                    }
                    VStack(alignment: .leading, spacing: 12) {
                        SectionHeader(title: "Rozetler")
                        AchievementsGrid()
                    }
                    studyCard
                    accountCard
                    VStack(spacing: 8) {
                        Button("Tüm ilerlemeyi sıfırla", role: .destructive) { confirmReset = true }
                            .font(.jakarta(.subheadline, weight: .bold))
                            .foregroundStyle(Theme.danger)
                        Text("Sürüm \(Bundle.main.object(forInfoDictionaryKey: "CFBundleShortVersionString") as? String ?? "")")
                            .font(.jakarta(.caption))
                            .foregroundStyle(.tertiary)
                    }
                    .padding(.top, 4)
                }
                .padding(20)
            }
            .tabBarSpacer()
            .background(Theme.background)
            // Kaydırılan içerik saatin altına girmesin diye durum çubuğuna buzlu zemin.
            .safeAreaInset(edge: .top, spacing: 0) {
                Color.clear.frame(height: 0).background(.ultraThinMaterial, ignoresSafeAreaEdges: .top)
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

    private var hero: some View {
        let level = model.state.currentLevel
        // Lacivert başlık; kırmızı yalnızca avatardaki baş harfte.
        return HeroHeader(title: model.state.name.ifEmpty("Öğrenci"),
                          subtitle: "\(level.rawValue) · \(level.title) seviyesinde çalışıyorsunuz",
                          gradient: Theme.inkGradient, glow: Theme.ink) {
            AnimatedAvatar(initial: String(model.state.name.prefix(1)).uppercased().ifEmpty("?"))
        } bottom: {
            HStack(spacing: 8) {
                heroChip("flame.fill", "\(model.state.progress.displayedStreak(at: .now)) gün seri")
                heroChip("bolt.fill", "\(model.state.progress.weekXP(at: .now)) XP bu hafta")
            }
        }
    }

    private func heroChip(_ icon: String, _ text: String) -> some View {
        Label(text, systemImage: icon)
            .font(.jakarta(.caption, weight: .heavy))
            .foregroundStyle(.white)
            .padding(.horizontal, 10)
            .padding(.vertical, 6)
            .background(.white.opacity(0.18), in: Capsule())
    }

    private var statsGrid: some View {
        let p = model.state.progress
        return LazyVGrid(columns: Array(repeating: GridItem(.flexible(), spacing: 10), count: 3), spacing: 10) {
            StatTile(icon: "flame.fill", color: Theme.streak, value: p.displayedStreak(at: .now), label: "Gün serisi", index: 0)
            StatTile(icon: "crown.fill", color: Theme.warning, value: p.longestStreak, label: "En uzun seri", index: 1)
            StatTile(icon: "bolt.fill", color: Theme.accent, value: p.totalXP, label: "Toplam XP", index: 2)
            StatTile(icon: "checkmark.seal.fill", color: Theme.success, value: model.state.completedLessons.count, label: "Ders", index: 3)
            StatTile(icon: "rectangle.stack.fill", color: Theme.color(for: .b2), value: model.deckSize, label: "Kelime", index: 4)
            StatTile(icon: "snowflake", color: Theme.ink, value: p.freezesAvailable, label: "Koruyucu", index: 5)
        }
    }

    private var leagueCard: some View {
        HStack(spacing: 14) {
            ZStack {
                Image(systemName: "shield.fill").font(.system(size: 44)).foregroundStyle(Theme.warning.gradient)
                Image(systemName: "trophy.fill").font(.system(size: 16, weight: .bold)).foregroundStyle(.white)
            }
            VStack(alignment: .leading, spacing: 3) {
                Text("Haftalık lig").font(.jakarta(.headline, weight: .heavy)).foregroundStyle(Theme.ink)
                Text("Bu hafta \(model.state.progress.weekXP(at: .now)) XP. İlk 7 bir üst lige çıkar.")
                    .font(.jakarta(.footnote))
                    .foregroundStyle(.secondary)
            }
            Spacer()
            Image(systemName: "chevron.right").font(.jakarta(.subheadline, weight: .bold)).foregroundStyle(.tertiary)
        }
        .card()
    }

    private var studyCard: some View {
        @Bindable var model = model
        return VStack(alignment: .leading, spacing: 14) {
            SectionHeader(title: "Çalışma ayarları")
            Text("Günlük hedef").font(.jakarta(.subheadline, weight: .bold)).foregroundStyle(.secondary)
            HStack(spacing: 8) {
                ForEach(DailyGoal.allCases) { goal in
                    FilterChip(title: "\(goal.minutes) dk", selected: model.state.dailyGoal == goal) {
                        model.setDailyGoal(goal)
                    }
                }
            }
            Divider()
            HStack {
                Text("Çalıştığım seviye").font(.jakarta(.subheadline, weight: .bold)).foregroundStyle(.secondary)
                Spacer()
                Menu {
                    Picker("Seviye", selection: $model.state.currentLevel) {
                        ForEach(CEFRLevel.allCases) { Text("\($0.rawValue) · \($0.title)").tag($0) }
                    }
                } label: {
                    HStack(spacing: 6) {
                        LevelBadge(level: model.state.currentLevel)
                        Text(model.state.currentLevel.title).font(.jakarta(.subheadline, weight: .bold))
                        Image(systemName: "chevron.up.chevron.down").font(.caption)
                    }
                    .foregroundStyle(Theme.ink)
                }
            }
            Button { showPlacement = true } label: {
                Label("Seviye testine tekrar girin", systemImage: "chart.bar.fill")
            }
            .buttonStyle(.secondary)
            Text("Seri koruyucu, hedefi kaçırdığınız tek bir günü kapatır. Her pazartesi bir tane yenilenir.")
                .font(.jakarta(.caption))
                .foregroundStyle(.secondary)
        }
        .card()
    }

    private var accountCard: some View {
        VStack(alignment: .leading, spacing: 12) {
            SectionHeader(title: "Hesap")
            if auth.isSignedIn {
                Label(auth.email ?? "Apple hesabı", systemImage: "checkmark.icloud.fill")
                    .font(.jakarta(.subheadline, weight: .bold))
                    .foregroundStyle(Theme.success)
                Button("Çıkış yap") { Task { await auth.signOut() } }.buttonStyle(.secondary)
                Button("Hesabımı sil", role: .destructive) { confirmDelete = true }
                    .font(.jakarta(.subheadline, weight: .bold))
                    .foregroundStyle(Theme.danger)
            } else if Backend.isConfigured {
                SignInWithAppleButton(.signIn) { auth.prepare($0) } onCompletion: { result in
                    Task { await signedIn(result) }
                }
                .frame(height: 50)
                .clipShape(RoundedRectangle(cornerRadius: 14, style: .continuous))
                if let error = auth.error { Text(error).foregroundStyle(Theme.danger).font(.jakarta(.footnote)) }
            } else {
                Label("Bulut yedekleme bu sürümde kapalı.", systemImage: "icloud.slash")
                    .font(.jakarta(.subheadline))
                    .foregroundStyle(.secondary)
            }
            Text("Giriş yapmak isteğe bağlıdır. Giriş yaparsanız ilerlemeniz yedeklenir, başka cihazda devam edebilir ve canlı derslere kaydolabilirsiniz.")
                .font(.jakarta(.caption))
                .foregroundStyle(.secondary)
        }
        .card()
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

/// Profil fotoğrafı yerine baş harf; çevresinde yavaşça dönen marka renkli halka.
struct AnimatedAvatar: View {
    let initial: String
    @State private var spin = false
    @Environment(\.accessibilityReduceMotion) private var reduceMotion

    var body: some View {
        ZStack {
            Circle()
                .stroke(AngularGradient(colors: [.white, Theme.warning, .white.opacity(0.2), .white], center: .center), lineWidth: 4)
                .frame(width: 84, height: 84)
                .rotationEffect(.degrees(spin ? 360 : 0))
            Text(initial)
                .font(.jakarta(.largeTitle, weight: .heavy))
                .foregroundStyle(Theme.accent)
                .frame(width: 70, height: 70)
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
                            .font(.jakarta(.caption, weight: .heavy))
                            .foregroundStyle(isCurrent ? .white : Theme.color(for: level))
                            .frame(width: 34, height: 34)
                            .background(isCurrent ? AnyShapeStyle(Theme.color(for: level).gradient) : AnyShapeStyle(Color.clear), in: Circle())
                    }
                    .frame(width: 46, height: 46)
                    .scaleEffect(isCurrent ? 1.1 : 1)
                    Text("%\(Int(ratio * 100))")
                        .font(.jakarta(.caption2, weight: .bold))
                        .foregroundStyle(.secondary)
                }
                .frame(maxWidth: .infinity)
            }
        }
        .card()
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
                .font(.jakarta(.footnote, weight: .bold))
                .foregroundStyle(.secondary)
            LazyVGrid(columns: Array(repeating: GridItem(.flexible(), spacing: 8), count: 4), spacing: 14) {
                ForEach(Array(list.enumerated()), id: \.element.id) { index, badge in
                    VStack(spacing: 6) {
                        ZStack {
                            Hexagon()
                                .fill(badge.unlocked ? AnyShapeStyle(badge.color.gradient) : AnyShapeStyle(Color(uiColor: .systemGray5)))
                                .frame(width: 56, height: 60)
                                .shadow(color: badge.unlocked ? badge.color.opacity(0.45) : .clear, radius: 8, y: 4)
                            Image(systemName: badge.unlocked ? badge.icon : "lock.fill")
                                .font(.system(size: 20, weight: .bold))
                                .foregroundStyle(badge.unlocked ? .white : Color(uiColor: .systemGray2))
                                .symbolEffect(.bounce, value: badge.unlocked)
                        }
                        Text(badge.title)
                            .font(.jakarta(.caption2, weight: .bold))
                            .foregroundStyle(badge.unlocked ? Theme.ink : .secondary)
                            .lineLimit(1)
                            .minimumScaleFactor(0.8)
                    }
                    .staggeredAppear(index, delay: 0.04)
                    .accessibilityElement(children: .ignore)
                    .accessibilityLabel("\(badge.title), \(badge.unlocked ? "açıldı" : "kilitli")")
                }
            }
        }
        .card()
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

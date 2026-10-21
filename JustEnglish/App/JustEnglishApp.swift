import SwiftUI
import JECore

@main
struct JustEnglishApp: App {
    @State private var model = AppModel()
    @State private var auth = AuthService()
    @State private var liveStore = LiveSessionStore()
    @Environment(\.scenePhase) private var scenePhase

    init() {
        Theme.configureAppearance()
    }

    var body: some Scene {
        WindowGroup {
            RootView()
                .environment(model)
                .environment(auth)
                .environment(liveStore)
                .tint(Theme.accent)
                .font(.jakarta(.body))
                .onAppear {
                    liveStore.onAttend = { [model] _ in model.award(xp: XPRule.liveClassAttended) }
                }
                .onChange(of: scenePhase) { _, phase in
                    if phase == .active {
                        model.state.progress.refillFreezeIfNeeded(at: .now)
                        if let id = auth.userID { Task { await SyncService.sync(model, userID: id) } }
                    } else if phase == .background, let id = auth.userID {
                        Task { await SyncService.sync(model, userID: id) }
                    }
                }
                .onChange(of: auth.userID) { _, id in
                    if let id { Task { await SyncService.sync(model, userID: id) } }
                }
        }
    }
}

struct RootView: View {
    @Environment(AppModel.self) private var model

    var body: some View {
        Group {
            if let error = model.loadError {
                ContentUnavailableView("İçerik yüklenemedi", systemImage: "exclamationmark.triangle",
                                       description: Text(error))
            } else if model.library == nil {
                ProgressView()
            } else if !model.state.onboarded {
                OnboardingView()
            } else {
                MainTabView()
            }
        }
        .task { model.loadIfNeeded() }
    }
}

struct MainTabView: View {
    @Environment(AppModel.self) private var model
    @State private var tab: AppTab = .learn
    @State private var barHeight: CGFloat = 64
    @State private var showDictionary = false

    var body: some View {
        // Sistem sekme çubuğu gizlenir; her sekmenin gezinme durumu korunur, alttaki çubuk bizim.
        // Çubuğun yüksekliği ortama verilir; her ekranın ScrollView'ı `tabBarSpacer()` ile bu kadar boşluk bırakır,
        // yoksa sayfaların sonu çubuğun arkasında kalır.
        TabView(selection: $tab) {
            LearnView().toolbar(.hidden, for: .tabBar).tag(AppTab.learn)
            PracticeView().toolbar(.hidden, for: .tabBar).tag(AppTab.practice)
            JAIChatView().toolbar(.hidden, for: .tabBar).tag(AppTab.jai)
            LiveClassesView().toolbar(.hidden, for: .tabBar).tag(AppTab.live)
            ProfileView().toolbar(.hidden, for: .tabBar).tag(AppTab.profile)
        }
        .environment(\.tabBarInset, barHeight)
        .environment(\.openDictionary, OpenDictionaryAction { showDictionary = true })
        .sheet(isPresented: $showDictionary) {
            DictionaryView()
                .environment(\.tabBarInset, 0)
                .presentationDragIndicator(.visible)
        }
        .environment(\.selectTab, SelectTabAction { new in
            Haptics.tap()
            withAnimation(.spring(response: 0.38, dampingFraction: 0.78)) { tab = new }
        })
        .overlay(alignment: .bottom) {
            JETabBar(selection: $tab, badges: [.practice: model.dueCards().count])
                .onGeometryChange(for: CGFloat.self) { $0.size.height } action: { barHeight = $0 }
        }
    }
}

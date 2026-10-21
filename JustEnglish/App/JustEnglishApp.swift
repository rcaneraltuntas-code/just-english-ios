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

    var body: some View {
        TabView {
            LearnView()
                .tabItem { Label("Öğren", systemImage: "book.fill") }
            PracticeView()
                .tabItem { Label("Pratik", systemImage: "rectangle.stack.fill") }
                .badge(model.dueCards().count)
            DictionaryView()
                .tabItem { Label("Sözlük", systemImage: "character.book.closed.fill") }
            LiveClassesView()
                .tabItem { Label("Canlı ders", systemImage: "video.fill") }
            ProfileView()
                .tabItem { Label("Profil", systemImage: "person.crop.circle.fill") }
        }
    }
}

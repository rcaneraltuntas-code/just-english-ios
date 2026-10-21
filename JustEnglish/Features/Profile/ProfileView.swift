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
            List {
                Section {
                    HStack(spacing: 16) {
                        Text(String(model.state.name.prefix(1)).uppercased().ifEmpty("?"))
                            .font(.jakarta(.title, weight: .bold))
                            .foregroundStyle(.white)
                            .frame(width: 64, height: 64)
                            .background(Theme.accent, in: Circle())
                        VStack(alignment: .leading, spacing: 4) {
                            Text(model.state.name.ifEmpty("Öğrenci")).font(.jakarta(.title3, weight: .bold))
                            HStack {
                                LevelBadge(level: model.state.currentLevel)
                                Text(model.state.currentLevel.title).font(.jakarta(.subheadline)).foregroundStyle(.secondary)
                            }
                        }
                    }
                    .padding(.vertical, 6)
                }

                Section {
                    NavigationLink { LeagueView() } label: {
                        Label {
                            VStack(alignment: .leading, spacing: 2) {
                                Text("Haftalık lig").font(.jakarta(.headline))
                                Text("Bu hafta \(model.state.progress.weekXP(at: .now)) XP").font(.jakarta(.footnote)).foregroundStyle(.secondary)
                            }
                        } icon: {
                            Image(systemName: "trophy.fill").foregroundStyle(Theme.warning)
                        }
                    }
                }

                Section("İstatistikler") {
                    stat("Gün serisi", "\(model.state.progress.displayedStreak(at: .now))", "flame.fill", Theme.streak)
                    stat("En uzun seri", "\(model.state.progress.longestStreak)", "trophy.fill", Theme.warning)
                    stat("Toplam XP", "\(model.state.progress.totalXP)", "bolt.fill", Theme.accent)
                    stat("Bitirilen ders", "\(model.state.completedLessons.count)", "checkmark.circle.fill", Theme.success)
                    stat("Destedeki kelime", "\(model.deckSize)", "rectangle.stack.fill", Theme.color(for: .b2))
                    stat("Seri koruyucu", "\(model.state.progress.freezesAvailable)", "snowflake", Theme.color(for: .a2))
                }

                Section {
                    Picker("Günlük hedef", selection: Binding(get: { model.state.dailyGoal }, set: { model.setDailyGoal($0) })) {
                        ForEach(DailyGoal.allCases) { Text("\($0.title) · \($0.minutes) dk").tag($0) }
                    }
                    Picker("Çalıştığım seviye", selection: $model.state.currentLevel) {
                        ForEach(CEFRLevel.allCases) { Text("\($0.rawValue) · \($0.title)").tag($0) }
                    }
                    Button("Seviye testine tekrar gir") { showPlacement = true }
                } header: {
                    Text("Çalışma")
                } footer: {
                    Text("Seri koruyucu, hedefi kaçırdığınız tek bir günü kapatır. Her pazartesi bir tane yenilenir.")
                }

                Section {
                    if auth.isSignedIn {
                        Label(auth.email ?? "Apple hesabı", systemImage: "checkmark.icloud.fill")
                            .foregroundStyle(Theme.success)
                        Button("Çıkış yap") { Task { await auth.signOut() } }
                        Button("Hesabımı sil", role: .destructive) { confirmDelete = true }
                    } else if Backend.isConfigured {
                        SignInWithAppleButton(.signIn) { auth.prepare($0) } onCompletion: { result in
                            Task { await signedIn(result) }
                        }
                        .frame(height: 48)
                        .listRowInsets(EdgeInsets())
                        if let error = auth.error { Text(error).foregroundStyle(Theme.danger).font(.jakarta(.footnote)) }
                    } else {
                        Text("Bulut yedekleme bu sürümde kapalı.").foregroundStyle(.secondary)
                    }
                } header: {
                    Text("Hesap")
                } footer: {
                    Text("Giriş yapmak isteğe bağlıdır. Giriş yaparsanız ilerlemeniz yedeklenir, başka cihazda devam edebilir ve canlı derslere kaydolabilirsiniz.")
                }

                Section {
                    Button("Tüm ilerlemeyi sıfırla", role: .destructive) { confirmReset = true }
                } footer: {
                    Text("Sürüm \(Bundle.main.object(forInfoDictionaryKey: "CFBundleShortVersionString") as? String ?? "")")
                }
            }
            .navigationTitle("Profil")
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

    private func signedIn(_ result: Result<ASAuthorization, Error>) async {
        let name = await auth.complete(result)
        if model.state.name.isEmpty, let given = name?.givenName { model.state.name = given }
        if let id = auth.userID { await SyncService.sync(model, userID: id) }
    }

    private func stat(_ title: String, _ value: String, _ icon: String, _ color: Color) -> some View {
        HStack {
            Label { Text(title) } icon: { Image(systemName: icon).foregroundStyle(color) }
            Spacer()
            Text(value).font(.jakarta(.headline)).monospacedDigit()
        }
    }
}

extension String {
    func ifEmpty(_ fallback: String) -> String { isEmpty ? fallback : self }
}

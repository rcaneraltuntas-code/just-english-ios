import SwiftUI
import JECore

/// Canlı grup dersleri: öğretmenlerin açtığı oturumlar Supabase'den gelir. Her oturum bir üniteye bağlıdır;
/// öğrenci dersten önce o ünitenin derslerini bitirmiş olursa en çok faydayı görür.
struct LiveClassesView: View {
    @Environment(AppModel.self) private var model
    @Environment(LiveSessionStore.self) private var store
    @Environment(AuthService.self) private var auth
    @State private var levelFilter: CEFRLevel?

    var body: some View {
        NavigationStack {
            List {
                Section {
                    Picker("Seviye", selection: $levelFilter) {
                        Text("Tümü").tag(CEFRLevel?.none)
                        ForEach(CEFRLevel.allCases) { Text($0.rawValue).tag(Optional($0)) }
                    }
                    .pickerStyle(.segmented)
                    .listRowBackground(Color.clear)
                    .listRowInsets(EdgeInsets())
                }
                switch store.state {
                case .idle, .loading:
                    Section { HStack { Spacer(); ProgressView(); Spacer() } }
                case .unavailable:
                    Section {
                        ContentUnavailableView("Program yakında", systemImage: "calendar.badge.clock",
                                               description: Text("Canlı ders takvimi hazırlanıyor. Bu sırada ünitelerdeki ders planlarına göz atabilirsiniz."))
                    }
                case .failed(let message):
                    Section {
                        ContentUnavailableView("Dersler yüklenemedi", systemImage: "wifi.exclamationmark", description: Text(message))
                        Button("Tekrar dene") { Task { await store.refresh() } }
                    }
                case .loaded:
                    if sessions.isEmpty {
                        Section {
                            ContentUnavailableView("Yaklaşan ders yok", systemImage: "calendar",
                                                   description: Text("Bu seviyede planlanmış canlı ders yok. Yakında yenileri eklenecek."))
                        }
                    } else {
                        Section("Yaklaşan dersler") {
                            ForEach(sessions) { session in
                                LiveSessionRow(session: session, unit: model.library?.unit(id: session.unitID))
                            }
                        }
                    }
                }
            }
            .listStyle(.insetGrouped)
            .navigationTitle("Canlı dersler")
            .toolbar {
                if auth.isTeacher {
                    NavigationLink { TeacherSessionsView() } label: {
                        Label("Derslerim", systemImage: "person.badge.key.fill")
                    }
                }
            }
            .refreshable { await store.refresh() }
            .alert(store.notice ?? "", isPresented: Binding(get: { store.notice != nil }, set: { if !$0 { store.notice = nil } })) {
                Button("Tamam", role: .cancel) {}
            }
            .task {
                if levelFilter == nil { levelFilter = model.state.currentLevel }
                if store.state == .idle { await store.refresh() }
            }
        }
    }

    private var sessions: [LiveSession] {
        store.sessions.filter { levelFilter == nil || $0.level == levelFilter }
    }
}

struct LiveSessionRow: View {
    let session: LiveSession
    let unit: CourseUnit?

    @Environment(LiveSessionStore.self) private var store
    @Environment(\.openURL) private var openURL

    var body: some View {
        VStack(alignment: .leading, spacing: 8) {
            HStack {
                LevelBadge(level: session.level)
                Text(session.startsAt.formatted(.dateTime.weekday(.wide).day().month().hour().minute()))
                    .font(.jakarta(.footnote, weight: .semibold))
                    .foregroundStyle(.secondary)
            }
            Text(session.title).font(.jakarta(.headline))
            if let unit { Text("Ünite \(unit.number): \(unit.title) · \(unit.liveClass.goal)").font(.jakarta(.footnote)).foregroundStyle(.secondary) }
            HStack {
                Label(session.teacherName, systemImage: "person.fill")
                Label("\(session.durationMinutes) dk", systemImage: "clock")
                if let seats = session.seatsLeft { Label("\(seats) yer", systemImage: "person.3.fill") }
            }
            .font(.jakarta(.caption))
            .foregroundStyle(.secondary)
            HStack {
                if session.isJoinable, let url = session.joinURL {
                    Button("Derse katıl") {
                        store.markAttended(session)
                        openURL(url)
                    }
                    .buttonStyle(PrimaryButtonStyle(color: Theme.success))
                } else if store.isBooked(session) {
                    Button("Kaydınızı iptal edin") { Task { await store.cancel(session) } }
                        .buttonStyle(.secondary)
                } else {
                    Button("Yer ayırt") { Task { await store.book(session) } }
                        .buttonStyle(.primary)
                        .disabled(session.seatsLeft == 0)
                }
            }
            .padding(.top, 4)
        }
        .padding(.vertical, 6)
    }
}

/// Ünite sayfasında, o ünitenin canlı ders planı.
struct LiveClassCard: View {
    let unit: CourseUnit

    var body: some View {
        HStack(alignment: .top, spacing: 14) {
            Image(systemName: "video.fill")
                .font(.title3)
                .foregroundStyle(.white)
                .frame(width: 44, height: 44)
                .background(Theme.success, in: RoundedRectangle(cornerRadius: 12))
            VStack(alignment: .leading, spacing: 4) {
                Text(unit.liveClass.title).font(.jakarta(.headline))
                Text(unit.liveClass.goal).font(.jakarta(.subheadline)).foregroundStyle(.secondary)
                Text("\(unit.liveClass.durationMinutes) dakika · küçük grup · Just English öğretmeni")
                    .font(.jakarta(.caption))
                    .foregroundStyle(.secondary)
            }
        }
        .card()
    }
}

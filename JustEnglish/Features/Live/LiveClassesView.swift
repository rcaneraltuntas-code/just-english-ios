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
            ScrollView {
                VStack(alignment: .leading, spacing: 22) {
                    hero
                    ScrollView(.horizontal, showsIndicators: false) {
                        HStack(spacing: 8) {
                            SoftChip(title: "Tümü", selected: levelFilter == nil) { levelFilter = nil }
                            ForEach(CEFRLevel.allCases) { level in
                                SoftChip(title: level.rawValue, selected: levelFilter == level) { levelFilter = level }
                            }
                        }
                        .padding(.horizontal, 16)
                        .padding(.vertical, 2)
                    }
                    .padding(.horizontal, -16)
                    sessionList
                    howItWorks
                    plans
                }
                .padding(.horizontal, 16)
                .padding(.bottom, 20)
                .animation(Motion.smooth, value: levelFilter)
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

    /// Mavi bant üzerinde başlık, kısa açıklama ve canlı ders sayısı; öğretmenler için "Derslerim" düğmesi.
    private var hero: some View {
        VStack(alignment: .leading, spacing: 14) {
            HStack(alignment: .top) {
                VStack(alignment: .leading, spacing: 6) {
                    Text("Canlı dersler")
                        .font(.custom(Theme.fontFamily, size: 26, relativeTo: .title).weight(.bold))
                        .foregroundStyle(.white)
                    Text("Just English öğretmenleriyle küçük gruplarda konuşun. Ünitenizi bitirip derse hazır gelin.")
                        .font(.custom(Theme.fontFamily, size: 15, relativeTo: .subheadline))
                        .foregroundStyle(.white.opacity(0.9))
                        .lineSpacing(3)
                        .fixedSize(horizontal: false, vertical: true)
                }
                Spacer(minLength: 12)
                if auth.isTeacher {
                    NavigationLink { TeacherSessionsView() } label: {
                        Image(systemName: "person.badge.key")
                            .font(.system(size: 17, weight: .medium))
                            .foregroundStyle(.white)
                            .frame(width: 40, height: 40)
                            .background(.white.opacity(0.25), in: Circle())
                    }
                    .accessibilityLabel("Derslerim")
                }
            }
            HStack(spacing: 8) {
                HStack(spacing: 6) {
                    LivePulse()
                    Text(upcomingText)
                        .font(.custom(Theme.fontFamily, size: 14, relativeTo: .footnote).weight(.semibold))
                        .foregroundStyle(HomeStyle.title)
                }
                .padding(.horizontal, 12)
                .frame(height: 32)
                .background(.white.opacity(0.9), in: Capsule())
                Label("Küçük grup", systemImage: "person.3")
                    .font(.custom(Theme.fontFamily, size: 14, relativeTo: .footnote).weight(.semibold))
                    .foregroundStyle(.white)
                    .padding(.horizontal, 12)
                    .frame(height: 32)
                    .background(.white.opacity(0.25), in: Capsule())
            }
        }
        .padding(.top, 14)
    }

    private var upcomingText: String {
        store.sessions.isEmpty ? "Takvim" : "\(store.sessions.count) yaklaşan ders"
    }

    @ViewBuilder private var sessionList: some View {
        switch store.state {
        case .idle, .loading:
            VStack(spacing: 12) {
                ForEach(0..<2, id: \.self) { _ in
                    RoundedRectangle(cornerRadius: 18, style: .continuous)
                        .fill(Theme.surface)
                        .frame(height: 150)
                        .overlay(ProgressView())
                        .modifier(HomeCard())
                }
            }
        case .unavailable:
            JAIEmptyState(title: "Program yakında",
                          message: "Canlı ders takvimi hazırlanıyor. Bu sırada aşağıdaki ders planlarına göz atabilirsiniz.")
        case .failed(let message):
            JAIEmptyState(title: "Dersler yüklenemedi", message: message, mood: .sad, actionTitle: "Tekrar deneyin") {
                Task { await store.refresh() }
            }
        case .loaded:
            if sessions.isEmpty {
                JAIEmptyState(title: "Yaklaşan ders yok",
                              message: "Bu seviyede planlanmış canlı ders yok. Yakında yenileri eklenecek.", mood: .idle)
            } else {
                VStack(alignment: .leading, spacing: 12) {
                    sectionTitle("Yaklaşan dersler")
                    ForEach(Array(sessions.enumerated()), id: \.element.id) { index, session in
                        LiveSessionRow(session: session, unit: model.library?.unit(id: session.unitID))
                            .staggeredAppear(index)
                    }
                }
            }
        }
    }

    private func sectionTitle(_ text: String) -> some View {
        Text(text)
            .font(.custom(Theme.fontFamily, size: 20, relativeTo: .title3).weight(.bold))
            .foregroundStyle(HomeStyle.title)
    }

    private var howItWorks: some View {
        VStack(alignment: .leading, spacing: 12) {
            sectionTitle("Nasıl çalışır?")
            VStack(spacing: 10) {
                step(1, "calendar.badge.plus", "Yer ayırtın", "Seviyenize uygun dersi seçin.")
                step(2, "book", "Hazırlanın", "Derse bağlı üniteyi bitirin.")
                step(3, "video", "Katılın", "Ders uygulamanın içinde canlı yayınlanır; giriş dersten 10 dakika önce açılır.")
            }
        }
    }

    /// Ana sayfadaki "Akıcılığa giden yol" satırları gibi: açık gri zemin, solda numaralı simge.
    private func step(_ number: Int, _ icon: String, _ title: String, _ detail: String) -> some View {
        HStack(spacing: 14) {
            Image(systemName: icon)
                .font(.system(size: 19, weight: .medium))
                .foregroundStyle(Theme.accent)
                .frame(width: 44, height: 44)
                .background(Theme.accentSoft, in: Circle())
                .overlay(alignment: .topTrailing) {
                    Text("\(number)")
                        .font(.custom(Theme.fontFamily, size: 11, relativeTo: .caption2).weight(.bold))
                        .foregroundStyle(.white)
                        .frame(width: 18, height: 18)
                        .background(Theme.accent, in: Circle())
                        .offset(x: 4, y: -4)
                }
            VStack(alignment: .leading, spacing: 3) {
                Text(title)
                    .font(.custom(Theme.fontFamily, size: 16, relativeTo: .headline).weight(.semibold))
                    .foregroundStyle(HomeStyle.title)
                Text(detail)
                    .font(.custom(Theme.fontFamily, size: 15, relativeTo: .subheadline))
                    .foregroundStyle(HomeStyle.body)
                    .fixedSize(horizontal: false, vertical: true)
            }
            Spacer(minLength: 0)
        }
        .padding(.horizontal, 14)
        .padding(.vertical, 12)
        .background(HomeStyle.rowFill, in: RoundedRectangle(cornerRadius: 16, style: .continuous))
        .staggeredAppear(number)
    }

    @ViewBuilder private var plans: some View {
        let units = model.units(for: levelFilter ?? model.state.currentLevel)
        if !units.isEmpty {
            VStack(alignment: .leading, spacing: 12) {
                sectionTitle("\((levelFilter ?? model.state.currentLevel).rawValue) ders planları")
                ScrollView(.horizontal, showsIndicators: false) {
                    HStack(spacing: 12) {
                        ForEach(units) { unit in
                            LiveClassCard(unit: unit)
                                .frame(width: 260)
                        }
                    }
                    .padding(.horizontal, 16)
                    .padding(.vertical, 4)
                }
                .padding(.horizontal, -16)
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
    @State private var inRoom = false

    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            HStack(alignment: .top, spacing: 14) {
                VStack(spacing: 0) {
                    Text(session.startsAt.formatted(.dateTime.month(.abbreviated)))
                        .font(.custom(Theme.fontFamily, size: 12, relativeTo: .caption2).weight(.semibold))
                        .foregroundStyle(Theme.accent)
                        .padding(.top, 6)
                    Text(session.startsAt.formatted(.dateTime.day()))
                        .font(.custom(Theme.fontFamily, size: 24, relativeTo: .title2).weight(.bold))
                        .foregroundStyle(HomeStyle.title)
                    Text(session.startsAt.formatted(.dateTime.hour().minute()))
                        .font(.custom(Theme.fontFamily, size: 12, relativeTo: .caption2).weight(.medium))
                        .foregroundStyle(HomeStyle.body)
                        .padding(.bottom, 6)
                }
                .frame(width: 58)
                .background(Theme.accentSoft, in: RoundedRectangle(cornerRadius: 14, style: .continuous))
                VStack(alignment: .leading, spacing: 5) {
                    HStack(spacing: 6) {
                        LevelBadge(level: session.level)
                        if session.isJoinable {
                            HStack(spacing: 4) { LivePulse(); Text(session.isLive ? "Canlı" : "Şimdi").font(.custom(Theme.fontFamily, size: 13, relativeTo: .caption).weight(.semibold)) }
                                .foregroundStyle(Theme.brandRed)
                        } else {
                            Text(session.startsAt.formatted(.relative(presentation: .named)))
                                .font(.custom(Theme.fontFamily, size: 13, relativeTo: .caption).weight(.semibold))
                                .foregroundStyle(Theme.accent)
                        }
                    }
                    Text(session.title)
                        .font(.custom(Theme.fontFamily, size: 17, relativeTo: .headline).weight(.bold))
                        .foregroundStyle(HomeStyle.title)
                    if let unit {
                        Text("Ünite \(unit.number): \(unit.title) · \(unit.liveClass.goal)")
                            .font(.custom(Theme.fontFamily, size: 14, relativeTo: .footnote))
                            .foregroundStyle(HomeStyle.body)
                            .lineLimit(2)
                    }
                }
            }
            HStack(spacing: 10) {
                Text(String(session.teacherName.prefix(1)).uppercased())
                    .font(.custom(Theme.fontFamily, size: 13, relativeTo: .caption).weight(.bold))
                    .foregroundStyle(Theme.accent)
                    .frame(width: 28, height: 28)
                    .background(Theme.accentSoft, in: Circle())
                Text(session.teacherName)
                    .font(.custom(Theme.fontFamily, size: 15, relativeTo: .footnote).weight(.semibold))
                    .foregroundStyle(HomeStyle.title)
                Spacer()
                Label("\(session.durationMinutes) dk", systemImage: "clock")
                    .font(.custom(Theme.fontFamily, size: 14, relativeTo: .caption).weight(.medium))
                    .foregroundStyle(HomeStyle.body)
            }
            if let capacity = session.capacity, let seats = session.seatsLeft {
                VStack(alignment: .leading, spacing: 4) {
                    ProgressBar(value: Double(capacity - seats) / Double(max(capacity, 1)),
                                color: seats <= 2 ? Theme.danger : Theme.accent, height: 6)
                    Text(seats == 0 ? "Kontenjan dolu" : "\(seats) yer kaldı")
                        .font(.custom(Theme.fontFamily, size: 13, relativeTo: .caption).weight(.medium))
                        .foregroundStyle(seats <= 2 ? Theme.danger : HomeStyle.body)
                }
            }
            if session.isJoinable, let url = session.joinURL {
                // Öğretmen harici bir toplantı bağlantısı (Zoom, Meet) girdiyse o açılır.
                Button {
                    store.markAttended(session)
                    openURL(url)
                } label: {
                    Label("Derse katılın", systemImage: "video.fill")
                }
                .buttonStyle(PrimaryButtonStyle(color: Theme.success))
            } else if session.isJoinable, store.isBooked(session) {
                Button { inRoom = true } label: {
                    Label(session.isLive ? "Derse katılın" : "Derse girin · öğretmen bekleniyor", systemImage: "video.fill")
                }
                .buttonStyle(PrimaryButtonStyle(color: Theme.success))
            } else if store.isBooked(session) {
                Label("Yeriniz ayrıldı", systemImage: "checkmark.circle.fill")
                    .font(.custom(Theme.fontFamily, size: 15, relativeTo: .subheadline).weight(.semibold))
                    .foregroundStyle(Theme.success)
                Button("Kaydınızı iptal edin") { Task { await store.cancel(session) } }
                    .buttonStyle(OnboardingButtonStyle(filled: false))
            } else {
                Button("Yer ayırtın") { Task { await store.book(session) } }
                    .buttonStyle(OnboardingButtonStyle(filled: true))
                    .disabled(session.seatsLeft == 0)
            }
        }
        .padding(16)
        .modifier(HomeCard())
        .fullScreenCover(isPresented: $inRoom, onDismiss: { Task { await store.refresh() } }) {
            LiveRoomView(sessionID: session.id, title: session.title) { store.markAttended(session) }
        }
    }
}

/// Ünite sayfasında ve canlı ders planlarında, bir ünitenin canlı ders planı.
struct LiveClassCard: View {
    let unit: CourseUnit

    var body: some View {
        VStack(alignment: .leading, spacing: 10) {
            HStack {
                Image("lesson-videocam").resizable().scaledToFit().frame(width: 40, height: 40)
                Spacer()
                LevelBadge(level: unit.level)
            }
            Text(unit.liveClass.title)
                .font(.custom(Theme.fontFamily, size: 17, relativeTo: .headline).weight(.bold))
                .foregroundStyle(HomeStyle.title)
                .lineLimit(2)
            Text(unit.liveClass.goal)
                .font(.custom(Theme.fontFamily, size: 15, relativeTo: .subheadline))
                .foregroundStyle(HomeStyle.body)
                .lineLimit(3)
            Spacer(minLength: 0)
            Label("\(unit.liveClass.durationMinutes) dakika · küçük grup", systemImage: "person.3")
                .font(.custom(Theme.fontFamily, size: 14, relativeTo: .caption).weight(.semibold))
                .foregroundStyle(Theme.accent)
        }
        .frame(maxHeight: .infinity, alignment: .topLeading)
        .padding(16)
        .modifier(HomeCard())
    }
}

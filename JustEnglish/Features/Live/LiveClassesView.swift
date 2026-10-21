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
                VStack(alignment: .leading, spacing: 18) {
                    hero
                    ScrollView(.horizontal, showsIndicators: false) {
                        HStack(spacing: 8) {
                            FilterChip(title: "Tümü", selected: levelFilter == nil) { levelFilter = nil }
                            ForEach(CEFRLevel.allCases) { level in
                                FilterChip(title: level.rawValue, selected: levelFilter == level, color: Theme.color(for: level)) {
                                    levelFilter = level
                                }
                            }
                        }
                        .padding(.horizontal, 20)
                        .padding(.vertical, 4)
                    }
                    .padding(.horizontal, -20)
                    sessionList
                    howItWorks
                    plans
                }
                .padding(20)
                .animation(Motion.smooth, value: levelFilter)
            }
            .background(Theme.background)
            // Kaydırılan içerik saatin altına girmesin diye durum çubuğuna buzlu zemin.
            .safeAreaInset(edge: .top, spacing: 0) {
                Color.clear.frame(height: 0).background(.ultraThinMaterial, ignoresSafeAreaEdges: .top)
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

    private var hero: some View {
        HeroHeader(title: "Canlı dersler",
                   subtitle: "Just English öğretmenleriyle küçük gruplarda konuşun. Ünitenizi bitirip derse hazır gelin.",
                   gradient: Theme.inkGradient, glow: Theme.ink) {
            if auth.isTeacher {
                NavigationLink { TeacherSessionsView() } label: {
                    Image(systemName: "person.badge.key.fill")
                        .font(.system(size: 18, weight: .bold))
                        .foregroundStyle(.white)
                        .frame(width: 44, height: 44)
                        .background(.white.opacity(0.18), in: Circle())
                }
                .accessibilityLabel("Derslerim")
            }
        } bottom: {
            HStack(spacing: 8) {
                HStack(spacing: 6) {
                    LivePulse(color: .white)
                    Text(upcomingText).font(.jakarta(.caption, weight: .heavy)).foregroundStyle(.white)
                }
                .padding(.horizontal, 10)
                .padding(.vertical, 6)
                .background(Theme.accent, in: Capsule())
                Label("Küçük grup", systemImage: "person.3.fill")
                    .font(.jakarta(.caption, weight: .heavy))
                    .foregroundStyle(.white)
                    .padding(.horizontal, 10)
                    .padding(.vertical, 6)
                    .background(.white.opacity(0.15), in: Capsule())
            }
        }
    }

    private var upcomingText: String {
        store.sessions.isEmpty ? "Takvim" : "\(store.sessions.count) yaklaşan ders"
    }

    @ViewBuilder private var sessionList: some View {
        switch store.state {
        case .idle, .loading:
            VStack(spacing: 12) {
                ForEach(0..<2, id: \.self) { _ in
                    RoundedRectangle(cornerRadius: 22, style: .continuous)
                        .fill(Theme.surface)
                        .frame(height: 150)
                        .overlay(ProgressView())
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
                    SectionHeader(title: "Yaklaşan dersler")
                    ForEach(Array(sessions.enumerated()), id: \.element.id) { index, session in
                        LiveSessionRow(session: session, unit: model.library?.unit(id: session.unitID))
                            .staggeredAppear(index)
                    }
                }
            }
        }
    }

    private var howItWorks: some View {
        VStack(alignment: .leading, spacing: 12) {
            SectionHeader(title: "Nasıl çalışır?")
            HStack(alignment: .top, spacing: 10) {
                step(1, "calendar.badge.plus", "Yer ayırtın", "Seviyenize uygun dersi seçin.", Theme.color(for: .a2))
                step(2, "book.fill", "Hazırlanın", "Bağlı üniteyi bitirin.", Theme.color(for: .b2))
                step(3, "video.fill", "Katılın", "Bağlantı dersten 10 dk önce açılır.", Theme.accent)
            }
        }
    }

    private func step(_ number: Int, _ icon: String, _ title: String, _ detail: String, _ color: Color) -> some View {
        VStack(alignment: .leading, spacing: 8) {
            ZStack(alignment: .topTrailing) {
                Image(systemName: icon)
                    .font(.system(size: 18, weight: .bold))
                    .foregroundStyle(.white)
                    .frame(width: 40, height: 40)
                    .background(color.gradient, in: RoundedRectangle(cornerRadius: 12, style: .continuous))
                Text("\(number)")
                    .font(.jakarta(.caption2, weight: .heavy))
                    .foregroundStyle(color)
                    .frame(width: 18, height: 18)
                    .background(.white, in: Circle())
                    .overlay(Circle().stroke(color, lineWidth: 1.5))
                    .offset(x: 6, y: -6)
            }
            Text(title).font(.jakarta(.subheadline, weight: .heavy)).foregroundStyle(Theme.ink)
            Text(detail).font(.jakarta(.caption)).foregroundStyle(.secondary).fixedSize(horizontal: false, vertical: true)
        }
        .frame(maxWidth: .infinity, alignment: .leading)
        .padding(12)
        .background(Theme.surface, in: RoundedRectangle(cornerRadius: 18, style: .continuous))
        .overlay(RoundedRectangle(cornerRadius: 18, style: .continuous).stroke(Theme.hairline, lineWidth: 1))
        .staggeredAppear(number)
    }

    @ViewBuilder private var plans: some View {
        let units = model.units(for: levelFilter ?? model.state.currentLevel)
        if !units.isEmpty {
            VStack(alignment: .leading, spacing: 12) {
                SectionHeader(title: "\((levelFilter ?? model.state.currentLevel).rawValue) ders planları")
                ScrollView(.horizontal, showsIndicators: false) {
                    HStack(spacing: 12) {
                        ForEach(units) { unit in
                            LiveClassCard(unit: unit)
                                .frame(width: 260)
                        }
                    }
                    .padding(.horizontal, 20)
                    .padding(.vertical, 6)
                }
                .padding(.horizontal, -20)
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
        let color = Theme.color(for: session.level)
        VStack(alignment: .leading, spacing: 12) {
            HStack(alignment: .top, spacing: 14) {
                VStack(spacing: 0) {
                    Text(session.startsAt.formatted(.dateTime.month(.abbreviated)))
                        .font(.jakarta(.caption2, weight: .heavy))
                        .foregroundStyle(.white)
                        .frame(maxWidth: .infinity)
                        .padding(.vertical, 3)
                        .background(color)
                    Text(session.startsAt.formatted(.dateTime.day()))
                        .font(.jakarta(.title2, weight: .heavy))
                        .foregroundStyle(Theme.ink)
                        .padding(.top, 2)
                    Text(session.startsAt.formatted(.dateTime.hour().minute()))
                        .font(.jakarta(.caption2, weight: .bold))
                        .foregroundStyle(.secondary)
                        .padding(.bottom, 4)
                }
                .frame(width: 58)
                .background(Theme.surfaceRaised)
                .clipShape(RoundedRectangle(cornerRadius: 14, style: .continuous))
                VStack(alignment: .leading, spacing: 5) {
                    HStack(spacing: 6) {
                        LevelBadge(level: session.level)
                        if session.isJoinable {
                            HStack(spacing: 4) { LivePulse(); Text("Şimdi").font(.jakarta(.caption, weight: .heavy)) }
                                .foregroundStyle(Theme.accent)
                        } else {
                            Text(session.startsAt.formatted(.relative(presentation: .named)))
                                .font(.jakarta(.caption, weight: .bold))
                                .foregroundStyle(Theme.accent)
                        }
                    }
                    Text(session.title).font(.jakarta(.headline, weight: .heavy)).foregroundStyle(Theme.ink)
                    if let unit {
                        Text("Ünite \(unit.number): \(unit.title) · \(unit.liveClass.goal)")
                            .font(.jakarta(.footnote))
                            .foregroundStyle(.secondary)
                            .lineLimit(2)
                    }
                }
            }
            HStack(spacing: 10) {
                Text(String(session.teacherName.prefix(1)).uppercased())
                    .font(.jakarta(.caption, weight: .heavy))
                    .foregroundStyle(.white)
                    .frame(width: 26, height: 26)
                    .background(Theme.ink, in: Circle())
                Text(session.teacherName).font(.jakarta(.footnote, weight: .bold)).foregroundStyle(Theme.ink)
                Spacer()
                Label("\(session.durationMinutes) dk", systemImage: "clock.fill")
                    .font(.jakarta(.caption, weight: .bold))
                    .foregroundStyle(.secondary)
            }
            if let capacity = session.capacity, let seats = session.seatsLeft {
                VStack(alignment: .leading, spacing: 4) {
                    ProgressBar(value: Double(capacity - seats) / Double(max(capacity, 1)),
                                color: seats <= 2 ? Theme.danger : color, height: 8)
                    Text(seats == 0 ? "Kontenjan dolu" : "\(seats) yer kaldı")
                        .font(.jakarta(.caption, weight: .bold))
                        .foregroundStyle(seats <= 2 ? Theme.danger : .secondary)
                }
            }
            if session.isJoinable, let url = session.joinURL {
                Button {
                    store.markAttended(session)
                    openURL(url)
                } label: {
                    Label("Derse katılın", systemImage: "video.fill")
                }
                .buttonStyle(PrimaryButtonStyle(color: Theme.success))
            } else if store.isBooked(session) {
                Label("Yeriniz ayrıldı", systemImage: "checkmark.circle.fill")
                    .font(.jakarta(.subheadline, weight: .heavy))
                    .foregroundStyle(Theme.success)
                Button("Kaydınızı iptal edin") { Task { await store.cancel(session) } }
                    .buttonStyle(.secondary)
            } else {
                Button("Yer ayırtın") { Task { await store.book(session) } }
                    .buttonStyle(.primary)
                    .disabled(session.seatsLeft == 0)
            }
        }
        .card()
    }
}

/// Ünite sayfasında, o ünitenin canlı ders planı.
struct LiveClassCard: View {
    let unit: CourseUnit

    var body: some View {
        VStack(alignment: .leading, spacing: 10) {
            HStack {
                Image(systemName: "video.fill")
                    .font(.system(size: 17, weight: .bold))
                    .foregroundStyle(.white)
                    .frame(width: 40, height: 40)
                    .background(Theme.brandGradient, in: RoundedRectangle(cornerRadius: 12, style: .continuous))
                Spacer()
                LevelBadge(level: unit.level)
            }
            Text(unit.liveClass.title).font(.jakarta(.headline, weight: .heavy)).foregroundStyle(Theme.ink).lineLimit(2)
            Text(unit.liveClass.goal).font(.jakarta(.subheadline)).foregroundStyle(.secondary).lineLimit(3)
            Spacer(minLength: 0)
            Label("\(unit.liveClass.durationMinutes) dakika · küçük grup", systemImage: "person.3.fill")
                .font(.jakarta(.caption, weight: .bold))
                .foregroundStyle(Theme.accent)
        }
        .frame(maxHeight: .infinity, alignment: .topLeading)
        .card()
    }
}

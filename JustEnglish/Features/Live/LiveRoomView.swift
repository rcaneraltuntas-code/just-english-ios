import SwiftUI
import LiveKit

/// Uygulama içi canlı ders ekranı. Öğretmen için yayın ekranı, öğrenci için izleme ekranı.
/// Ortada öğretmenin kamerası, altta kontroller; sohbet ve katılımcı listesi alt sayfada açılır.
struct LiveRoomView: View {
    let title: String
    /// Öğrenci derse bağlandığında katılım işaretlenir (XP).
    var onJoined: (() -> Void)?

    @State private var room: LiveRoomController
    @State private var showChat = false
    @State private var showPeople = false
    @State private var confirmLeave = false
    @Environment(\.dismiss) private var dismiss

    init(sessionID: UUID, title: String, onJoined: (() -> Void)? = nil) {
        self.title = title
        self.onJoined = onJoined
        _room = State(initialValue: LiveRoomController(sessionID: sessionID))
    }

    var body: some View {
        ZStack {
            Color.black.ignoresSafeArea()
            switch room.phase {
            case .connecting:
                VStack(spacing: 14) {
                    ProgressView().tint(.white).controlSize(.large)
                    Text("Derse bağlanılıyor…").font(.jakarta(.subheadline, weight: .semibold)).foregroundStyle(.white.opacity(0.85))
                }
            case .failed(let message):
                status(icon: "wifi.exclamationmark", title: "Bağlanılamadı", message: message) {
                    Button("Tekrar deneyin") { Task { await room.connect() } }
                        .buttonStyle(PrimaryButtonStyle(color: Theme.accent))
                }
            case .ended:
                status(icon: "checkmark.circle", title: "Ders sona erdi", message: "Katıldığınız için teşekkürler.") {
                    Button("Kapat") { dismiss() }.buttonStyle(PrimaryButtonStyle(color: Theme.accent))
                }
            case .connected:
                stage
            }
        }
        .preferredColorScheme(.dark)
        .statusBarHidden(room.phase == .connected)
        .task {
            await room.connect()
            if room.phase == .connected, !room.isTeacher { onJoined?() }
        }
        .onAppear { UIApplication.shared.isIdleTimerDisabled = true }
        .onDisappear {
            UIApplication.shared.isIdleTimerDisabled = false
            Task { await room.leave() }
        }
        .sheet(isPresented: $showChat) {
            LiveChatSheet(room: room).presentationDetents([.medium, .large])
        }
        .sheet(isPresented: $showPeople) {
            LivePeopleSheet(room: room).presentationDetents([.medium, .large])
        }
        .onChange(of: showChat) { _, open in
            room.chatOpen = open
            if open { room.markChatRead() }
        }
        .confirmationDialog("Dersten çıkılsın mı?", isPresented: $confirmLeave, titleVisibility: .visible) {
            if room.isTeacher {
                Button("Dersi herkes için bitir", role: .destructive) { Task { await room.leave(endForEveryone: true); dismiss() } }
                Button("Yalnızca ben çıkayım") { Task { await room.leave(); dismiss() } }
            } else {
                Button("Dersten çık", role: .destructive) { Task { await room.leave(); dismiss() } }
            }
            Button("Vazgeç", role: .cancel) {}
        }
    }

    // MARK: - Sahne

    private var stage: some View {
        VStack(spacing: 0) {
            topBar
            ZStack {
                if let track = room.teacherVideo {
                    SwiftUIVideoView(track, layoutMode: room.isTeacher ? .fill : .fit)
                        .clipShape(RoundedRectangle(cornerRadius: 22, style: .continuous))
                } else {
                    RoundedRectangle(cornerRadius: 22, style: .continuous)
                        .fill(Color.white.opacity(0.06))
                        .overlay {
                            VStack(spacing: 10) {
                                Image(systemName: room.teacherPresent ? "video.slash" : "hourglass")
                                    .font(.system(size: 34, weight: .medium))
                                Text(room.teacherPresent ? "Kamera kapalı" : "Öğretmen bekleniyor")
                                    .font(.jakarta(.headline))
                                if !room.teacherPresent {
                                    Text("Ders başladığında yayın burada görünecek.")
                                        .font(.jakarta(.footnote))
                                        .foregroundStyle(.white.opacity(0.7))
                                }
                            }
                            .foregroundStyle(.white.opacity(0.9))
                        }
                }
            }
            .padding(.horizontal, 12)
            .overlay(alignment: .bottomLeading) { speakingStrip.padding(.horizontal, 24).padding(.bottom, 12) }
            if !room.isTeacher && room.maySpeak {
                Label("Öğretmen size söz verdi", systemImage: "mic.fill")
                    .font(.jakarta(.footnote, weight: .semibold))
                    .foregroundStyle(.white)
                    .padding(.horizontal, 14).padding(.vertical, 8)
                    .background(Theme.success, in: Capsule())
                    .padding(.top, 10)
            }
            controls
        }
    }

    private var topBar: some View {
        HStack(spacing: 10) {
            HStack(spacing: 6) {
                LivePulse()
                Text("CANLI").font(.jakarta(.caption, weight: .bold))
            }
            .foregroundStyle(.white)
            .padding(.horizontal, 10).frame(height: 28)
            .background(Theme.brandRed.opacity(0.85), in: Capsule())
            Text(title)
                .font(.jakarta(.subheadline, weight: .semibold))
                .foregroundStyle(.white)
                .lineLimit(1)
            Spacer(minLength: 8)
            Label("\(room.members.count + 1)", systemImage: "person.2.fill")
                .font(.jakarta(.footnote, weight: .semibold))
                .foregroundStyle(.white.opacity(0.85))
                .accessibilityLabel("\(room.members.count + 1) katılımcı")
        }
        .padding(.horizontal, 16)
        .padding(.vertical, 10)
    }

    /// Şu an konuşan öğrencilerin adları (öğretmen dışındakiler).
    @ViewBuilder private var speakingStrip: some View {
        let speaking = room.students.filter { $0.micOn }
        if !speaking.isEmpty {
            HStack(spacing: 6) {
                ForEach(speaking.prefix(3)) { member in
                    Label(member.name, systemImage: member.isSpeaking ? "waveform" : "mic.fill")
                        .font(.jakarta(.caption, weight: .semibold))
                        .foregroundStyle(.white)
                        .padding(.horizontal, 10).frame(height: 26)
                        .background(.black.opacity(0.55), in: Capsule())
                }
            }
        }
    }

    private var controls: some View {
        HStack(spacing: 14) {
            control(room.micOn ? "mic.fill" : "mic.slash.fill", room.micOn ? "Mikrofonu kapat" : "Mikrofonu aç",
                    active: room.micOn, disabled: !room.maySpeak && !room.micOn) {
                Task { await room.toggleMicrophone() }
            }
            if room.isTeacher {
                control(room.cameraOn ? "video.fill" : "video.slash.fill", room.cameraOn ? "Kamerayı kapat" : "Kamerayı aç",
                        active: room.cameraOn) { Task { await room.toggleCamera() } }
                control("arrow.triangle.2.circlepath.camera", "Kamerayı çevir", disabled: !room.cameraOn) {
                    Task { await room.switchCamera() }
                }
                control("person.3.fill", "Katılımcılar", badge: room.raisedHands) { showPeople = true }
            } else {
                control(room.handRaised ? "hand.raised.fill" : "hand.raised", room.handRaised ? "Elinizi indirin" : "El kaldırın",
                        active: room.handRaised, tint: Theme.warning) { Task { await room.toggleHand() } }
            }
            control("bubble.left.and.bubble.right.fill", "Sohbet", badge: room.unreadChat) { showChat = true }
            Button { confirmLeave = true } label: {
                Image(systemName: "phone.down.fill")
                    .font(.system(size: 20, weight: .semibold))
                    .foregroundStyle(.white)
                    .frame(width: 54, height: 54)
                    .background(Theme.danger, in: Circle())
            }
            .accessibilityLabel("Dersten çık")
        }
        .padding(.top, 16)
        .padding(.bottom, 8)
    }

    private func control(_ icon: String, _ label: String, active: Bool = false, tint: Color = .white,
                         disabled: Bool = false, badge: Int = 0, action: @escaping () -> Void) -> some View {
        Button(action: action) {
            Image(systemName: icon)
                .font(.system(size: 19, weight: .semibold))
                .foregroundStyle(active && tint != .white ? Color.black : Color.white)
                .frame(width: 50, height: 50)
                .background(active ? (tint == .white ? Color.white.opacity(0.28) : tint) : Color.white.opacity(0.12), in: Circle())
                .overlay(alignment: .topTrailing) {
                    if badge > 0 {
                        Text("\(badge)")
                            .font(.jakarta(.caption2, weight: .bold))
                            .foregroundStyle(.white)
                            .frame(minWidth: 18, minHeight: 18)
                            .background(Theme.brandRed, in: Circle())
                            .offset(x: 3, y: -3)
                    }
                }
        }
        .disabled(disabled)
        .opacity(disabled ? 0.4 : 1)
        .accessibilityLabel(label)
    }

    private func status<Action: View>(icon: String, title: String, message: String, @ViewBuilder action: () -> Action) -> some View {
        VStack(spacing: 14) {
            Image(systemName: icon).font(.system(size: 40, weight: .medium)).foregroundStyle(.white.opacity(0.9))
            Text(title).font(.jakarta(.title3, weight: .bold)).foregroundStyle(.white)
            Text(message)
                .font(.jakarta(.subheadline))
                .foregroundStyle(.white.opacity(0.8))
                .multilineTextAlignment(.center)
            action().padding(.top, 6)
            if case .failed = room.phase {
                Button("Kapat") { dismiss() }.foregroundStyle(.white.opacity(0.8)).padding(.top, 2)
            }
        }
        .padding(28)
    }
}

/// Ders içi sohbet.
private struct LiveChatSheet: View {
    let room: LiveRoomController
    @State private var draft = ""

    var body: some View {
        NavigationStack {
            ScrollViewReader { proxy in
                ScrollView {
                    LazyVStack(alignment: .leading, spacing: 10) {
                        if room.messages.isEmpty {
                            Text("Henüz mesaj yok. Sorunuzu buraya yazabilirsiniz.")
                                .font(.jakarta(.footnote))
                                .foregroundStyle(.secondary)
                                .frame(maxWidth: .infinity)
                                .padding(.top, 24)
                        }
                        ForEach(room.messages) { message in
                            VStack(alignment: message.mine ? .trailing : .leading, spacing: 3) {
                                if !message.mine {
                                    Text(message.sender).font(.jakarta(.caption, weight: .semibold)).foregroundStyle(.secondary)
                                }
                                Text(message.text)
                                    .font(.jakarta(.subheadline))
                                    .padding(.horizontal, 12).padding(.vertical, 8)
                                    .background(message.mine ? Theme.accent.opacity(0.85) : Theme.surfaceRaised,
                                                in: RoundedRectangle(cornerRadius: 14, style: .continuous))
                            }
                            .frame(maxWidth: .infinity, alignment: message.mine ? .trailing : .leading)
                            .id(message.id)
                        }
                    }
                    .padding(16)
                }
                .onChange(of: room.messages.count) { _, _ in
                    if let last = room.messages.last { withAnimation { proxy.scrollTo(last.id, anchor: .bottom) } }
                }
            }
            .safeAreaInset(edge: .bottom) {
                HStack(spacing: 10) {
                    TextField("Mesaj yazın", text: $draft)
                        .textFieldStyle(.roundedBorder)
                        .submitLabel(.send)
                        .onSubmit(send)
                    Button(action: send) { Image(systemName: "paperplane.fill") }
                        .disabled(draft.trimmingCharacters(in: .whitespaces).isEmpty)
                        .accessibilityLabel("Gönder")
                }
                .padding(12)
                .background(.bar)
            }
            .navigationTitle("Sohbet")
            .navigationBarTitleDisplayMode(.inline)
        }
    }

    private func send() {
        let text = draft
        draft = ""
        Task { await room.send(text) }
    }
}

/// Öğretmenin katılımcı listesi: el kaldıranlar üstte, söz verme ve herkesi sessize alma.
private struct LivePeopleSheet: View {
    let room: LiveRoomController

    var body: some View {
        NavigationStack {
            List {
                if room.students.isEmpty {
                    Text("Henüz öğrenci katılmadı.").foregroundStyle(.secondary)
                }
                ForEach(room.students) { member in
                    HStack(spacing: 12) {
                        Text(String(member.name.prefix(1)).uppercased())
                            .font(.jakarta(.footnote, weight: .bold))
                            .foregroundStyle(Theme.accent)
                            .frame(width: 32, height: 32)
                            .background(Theme.accentSoft, in: Circle())
                        VStack(alignment: .leading, spacing: 2) {
                            Text(member.name).font(.jakarta(.subheadline, weight: .semibold))
                            if member.handRaised {
                                Label("El kaldırdı", systemImage: "hand.raised.fill")
                                    .font(.jakarta(.caption, weight: .semibold))
                                    .foregroundStyle(Theme.warning)
                            }
                        }
                        Spacer()
                        if member.micOn {
                            Button("Sözü al") { Task { await room.setFloor(member, allowed: false) } }
                                .buttonStyle(.bordered).tint(Theme.danger)
                        } else {
                            Button("Söz ver") { Task { await room.setFloor(member, allowed: true) } }
                                .buttonStyle(.borderedProminent).tint(Theme.success)
                        }
                    }
                }
            }
            .navigationTitle("Katılımcılar (\(room.students.count))")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                Button("Herkesi sustur") { Task { await room.muteAllStudents() } }
                    .disabled(!room.students.contains { $0.micOn })
            }
        }
    }
}

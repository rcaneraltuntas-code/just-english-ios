import SwiftUI
import JECore

/// JAI ile sohbet. Gerçek yapay zekâ henüz bağlı değil: JAI, çalıştığınız ünitelerin kelimeleriyle
/// sizinle kelime ve cümle pratiği yapar (çevrimdışı, kurallı bir öğretmen). Sesle ya da klavyeyle cevap verilir.
struct JAIChatView: View {
    @Environment(AppModel.self) private var model
    @State private var tutor = ChatTutor()
    @State private var recognizer = SpeechRecognizer()
    @State private var typing = false
    @State private var input = ""
    @State private var jaiHop = 0
    @State private var showInfo = false
    @FocusState private var fieldFocused: Bool

    var body: some View {
        VStack(spacing: 0) {
            header
            ScrollViewReader { proxy in
                ScrollView {
                    LazyVStack(alignment: .leading, spacing: 22) {
                        ForEach(tutor.messages) { message in
                            ChatBubble(message: message)
                                .id(message.id)
                                .transition(.asymmetric(insertion: .move(edge: .bottom).combined(with: .opacity), removal: .opacity))
                        }
                        if tutor.thinking {
                            TypingIndicator().id("typing").transition(.opacity)
                        }
                        if recognizer.status == .recording, !recognizer.transcript.isEmpty {
                            ChatBubble(message: .init(role: .user, text: recognizer.transcript))
                                .opacity(0.6)
                                .id("live")
                        }
                    }
                    .padding(.horizontal, 18)
                    .padding(.top, 24)
                    .padding(.bottom, 12)
                    .animation(Motion.smooth, value: tutor.messages.count)
                    .animation(Motion.smooth, value: tutor.thinking)
                }
                .scrollDismissesKeyboard(.interactively)
                .onChange(of: tutor.messages.count) { _, _ in
                    withAnimation(Motion.smooth) { proxy.scrollTo(tutor.messages.last?.id, anchor: .bottom) }
                }
                .onChange(of: tutor.thinking) { _, thinking in
                    if thinking { withAnimation { proxy.scrollTo("typing", anchor: .bottom) } }
                }
            }
            controls
        }
        .tabBarSpacer()
        .background(Theme.surface.ignoresSafeArea())
        .sheet(isPresented: $showInfo) { infoSheet }
        .task {
            if tutor.messages.isEmpty { await tutor.start(name: model.state.name, pool: pool) }
        }
        .onChange(of: tutor.messages.count) { _, _ in
            if tutor.messages.last?.role == .jai { jaiHop += 1 }
        }
        .onChange(of: recognizer.status) { old, new in
            // Kayıt bitince söylenen cümle gönderilir.
            if old == .recording, new == .idle, !recognizer.transcript.isEmpty { send(recognizer.transcript) }
        }
    }

    /// Pratik edilecek kelimeler: destedekiler ve çalışılan üniteler; yoksa mevcut seviyenin ilk ünitesi.
    private var pool: [VocabularyCard] {
        let studied = model.gamePool.filter { !$0.en.contains("/") }
        if studied.count >= 4 { return studied }
        let fallback = model.nextLesson?.unit.vocabulary ?? model.units(for: model.state.currentLevel).first?.vocabulary ?? []
        return fallback.filter { !$0.en.contains("/") }
    }

    /// Üst bant (referans 2): açık mavi degrade, düz alt kenar; solda başlık, sağda ayar, ortada cam küre içinde JAI
    /// ve kürenin altına binen beyaz ad rozeti.
    private var header: some View {
        ZStack(alignment: .top) {
            HStack {
                Text("JAI ile sohbet")
                    .font(.custom(Theme.fontFamily, size: 22, relativeTo: .title2).weight(.bold))
                    .foregroundStyle(Theme.ink)
                Spacer()
                Button { showInfo = true } label: {
                    Image(systemName: "gearshape")
                        .font(.system(size: 21, weight: .regular))
                        .foregroundStyle(Theme.ink)
                        .frame(width: 40, height: 40)
                }
                .accessibilityLabel("Sohbet hakkında")
            }
            .padding(.horizontal, 18)
            .padding(.top, 8)
            ZStack {
                Circle()
                    .fill(RadialGradient(colors: [.white.opacity(0.9), Color(light: 0xC9DBFF, dark: 0x2A3A70).opacity(0.55)],
                                         center: .topLeading, startRadius: 4, endRadius: 120))
                    .overlay(Circle().stroke(.white.opacity(0.9), lineWidth: 1.5))
                    .frame(width: 112, height: 112)
                    .shadow(color: Theme.accent.opacity(0.18), radius: 14, y: 6)
                JAIView(mood: tutor.thinking ? .thinking : (tutor.lastWasCorrect ? .happy : .idle), size: 84, bounceTrigger: jaiHop)
            }
            .overlay(alignment: .bottom) {
                HStack(spacing: 6) {
                    Circle().fill(Color(light: 0x3FD3E8, dark: 0x5EE3F5)).frame(width: 10, height: 10)
                    Text("JAI")
                        .font(.custom(Theme.fontFamily, size: 16, relativeTo: .callout).weight(.semibold))
                        .foregroundStyle(Theme.ink)
                }
                .padding(.horizontal, 12)
                .frame(height: 30)
                .background(Theme.surface, in: Capsule())
                .shadow(color: Theme.ink.opacity(0.08), radius: 4, y: 2)
                .offset(y: 14)
            }
            // Küre başlık satırının altından başlar; uzun Türkçe başlık küreye binmesin.
            .padding(.top, 46)
        }
        .padding(.bottom, 28)
        .frame(maxWidth: .infinity)
        .background {
            LinearGradient(colors: [Color(light: 0xDCE7FF, dark: 0x1C2850), Color(light: 0xEAF1FF, dark: 0x151C38)],
                           startPoint: .top, endPoint: .bottom)
                .ignoresSafeArea(edges: .top)
        }
    }

    /// Ayar simgesinin açtığı bilgi: gerçek yapay zekâ henüz bağlı değil.
    private var infoSheet: some View {
        VStack(alignment: .leading, spacing: 14) {
            Text("JAI hakkında")
                .font(.custom(Theme.fontFamily, size: 22, relativeTo: .title2).weight(.bold))
                .foregroundStyle(Theme.ink)
            Text("Gerçek yapay zekâ sohbeti yakında. Şimdilik JAI, derslerinizdeki kelimelerle sizinle pratik yapıyor: Türkçesini verdiği kelimenin İngilizcesini sorar, sonra o kelimeyle bir cümle kurmanızı ister.")
                .font(.custom(Theme.fontFamily, size: 16, relativeTo: .body))
                .foregroundStyle(HomeStyle.body)
                .fixedSize(horizontal: false, vertical: true)
            Spacer()
        }
        .padding(24)
        .presentationDetents([.height(240)])
    }

    private var controls: some View {
        VStack(spacing: 10) {
            if fieldFocused || !input.isEmpty {
                HStack(spacing: 10) {
                    TextField("İngilizce yazın", text: $input)
                        .font(.jakarta(.body, weight: .medium))
                        .textInputAutocapitalization(.never)
                        .autocorrectionDisabled()
                        .focused($fieldFocused)
                        .submitLabel(.send)
                        .onSubmit { send(input) }
                    Button { send(input) } label: {
                        Image(systemName: "arrow.up")
                            .font(.system(size: 16, weight: .heavy))
                            .foregroundStyle(.white)
                            .frame(width: 36, height: 36)
                            .background(Theme.accent, in: Circle())
                    }
                    .disabled(input.trimmingCharacters(in: .whitespaces).isEmpty)
                    .accessibilityLabel("Gönder")
                }
                .padding(.leading, 16)
                .padding(.trailing, 6)
                .padding(.vertical, 6)
                .glassCapsule()
                .padding(.horizontal, 20)
                .transition(.move(edge: .bottom).combined(with: .opacity))
            }
            Text(micCaption)
                .font(.custom(Theme.fontFamily, size: 13, relativeTo: .caption))
                .foregroundStyle(Color(light: 0xA0A6B1, dark: 0x6C7690))
            HStack(alignment: .center, spacing: 40) {
                sideButton("Hints", icon: "sparkles", label: "İpucu") { tutor.hint() }
                MicButton(recording: recognizer.status == .recording) {
                    Task { await recognizer.toggle() }
                }
                sideButton("Keyboard", icon: "keyboard", label: "Klavye") {
                    withAnimation(Motion.smooth) { fieldFocused.toggle() }
                }
            }
        }
        .padding(.top, 8)
        .padding(.bottom, 8)
        .animation(Motion.smooth, value: fieldFocused)
    }

    private var micCaption: String {
        switch recognizer.status {
        case .recording: "Dinliyorum… bitirince tekrar dokunun"
        case .denied: "Mikrofon izni yok; klavyeyi kullanabilirsiniz"
        case .unavailable: "Ses tanıma kullanılamıyor; klavyeyi kullanın"
        case .idle: "Konuşmak için bir kez dokunun"
        }
    }

    private func sideButton(_ id: String, icon: String, label: String, action: @escaping () -> Void) -> some View {
        Button(action: action) {
            VStack(spacing: 6) {
                Image(systemName: icon)
                    .font(.system(size: 17, weight: .regular))
                    .foregroundStyle(Theme.ink)
                    .frame(width: 40, height: 40)
                    .background(Color(light: 0xF2F4F7, dark: 0x252A3B), in: Circle())
                Text(label)
                    .font(.custom(Theme.fontFamily, size: 13, relativeTo: .caption))
                    .foregroundStyle(HomeStyle.body)
            }
            .frame(width: 56)
            // Ortadaki mikrofonla aynı hizada dursun diye, etiket kadar aşağı kaydırılır.
            .offset(y: 10)
        }
        .buttonStyle(PressableCardStyle())
    }

    private func send(_ text: String) {
        let clean = text.trimmingCharacters(in: .whitespacesAndNewlines)
        guard !clean.isEmpty else { return }
        input = ""
        Task { await tutor.reply(to: clean) }
    }
}

// MARK: - Öğretmen

/// JAI'nin kurallı pratik akışı: Türkçesi verilen kelimenin İngilizcesini sorar, sonra o kelimeyle bir cümle ister.
@MainActor
@Observable
final class ChatTutor {
    struct Message: Identifiable, Equatable {
        enum Role { case jai, user }
        let id = UUID()
        let role: Role
        let text: String
        /// Sesli okunabilecek İngilizce kısım.
        var english: String?
    }

    private enum Step { case word, sentence }

    private(set) var messages: [Message] = []
    private(set) var thinking = false
    private(set) var lastWasCorrect = false
    private var pool: [VocabularyCard] = []
    private var current: VocabularyCard?
    private var step: Step = .word
    private var attempts = 0

    func start(name: String, pool: [VocabularyCard]) async {
        self.pool = pool.shuffled()
        let hello = name.isEmpty ? "Merhaba!" : "Merhaba \(name)!"
        await say("\(hello) Ben JAI, İngilizce pratik arkadaşınız. Birlikte birkaç kelime çalışalım mı?")
        await askNext()
    }

    func reply(to text: String) async {
        messages.append(Message(role: .user, text: text))
        guard let card = current else { await askNext(); return }
        switch step {
        case .word:
            if AnswerChecker.matches(text, accepted: [card.en]) {
                lastWasCorrect = true
                Haptics.success()
                await say("Harika! \"\(card.en)\" doğru. Şimdi bunu bir cümlede kullanın, örneğin:", english: nil)
                await say("\"\(card.example)\"", english: card.example)
                step = .sentence
                attempts = 0
            } else {
                lastWasCorrect = false
                attempts += 1
                Haptics.error()
                if attempts == 1 {
                    await say("Tam değil. İpucu: \"\(String(card.en.prefix(max(1, card.en.count / 3))))…\" ile başlıyor. Bir daha deneyin.")
                } else {
                    await say("Doğrusu \"\(card.en)\". Şimdi bunu bir cümlede kullanalım:", english: card.en)
                    await say("\"\(card.example)\"", english: card.example)
                    step = .sentence
                    attempts = 0
                }
            }
        case .sentence:
            let normalized = AnswerChecker.normalize(text)
            let word = AnswerChecker.normalize(card.en)
            if normalized.contains(word) && normalized.split(separator: " ").count >= 3 {
                lastWasCorrect = true
                Haptics.success()
                await say(["Çok iyi bir cümle!", "Mükemmel, aynen böyle!", "Harika gidiyorsunuz!"].randomElement()!)
                await askNext()
            } else {
                lastWasCorrect = false
                attempts += 1
                if attempts >= 2 {
                    await say("Sorun değil, örneği tekrar dinleyin ve sonraki kelimeye geçelim.", english: card.example)
                    await askNext()
                } else {
                    await say("Cümlenizde \"\(card.en)\" kelimesi geçsin ve en az üç kelime olsun. Bir daha deneyin.")
                }
            }
        }
    }

    func hint() {
        guard let card = current else { return }
        Task {
            switch step {
            case .word: await say("İpucu: \(card.en.count) harf, \"\(card.en.prefix(1))\" ile başlıyor.")
            case .sentence: await say("Şu kalıbı deneyin:", english: card.example)
            }
        }
    }

    private func askNext() async {
        guard !pool.isEmpty else {
            await say("Pratik için önce birkaç ders tamamlayın, sonra burada birlikte çalışalım.")
            return
        }
        let card = pool.removeFirst()
        pool.append(card)
        current = card
        step = .word
        attempts = 0
        await say("\"\(card.tr)\" İngilizce nasıl söylenir?")
    }

    private func say(_ text: String, english: String? = nil) async {
        thinking = true
        try? await Task.sleep(for: .milliseconds(min(1200, 400 + text.count * 8)))
        thinking = false
        messages.append(Message(role: .jai, text: text, english: english))
        if let english { Speech.shared.speak(english) }
    }
}

// MARK: - Parçalar

/// JAI mesajı balonsuz: yuvarlak JAI avatarı ve düz metin, sesli okunabiliyorsa sonunda hoparlör (dokununca okur).
/// Kullanıcı mesajı sağda açık gri balon.
struct ChatBubble: View {
    let message: ChatTutor.Message

    var body: some View {
        if message.role == .jai {
            HStack(alignment: .top, spacing: 12) {
                JAIAvatar()
                Group {
                    if message.english != nil {
                        Text(message.text) + Text("  ") + Text(Image(systemName: "speaker.wave.2")).foregroundColor(HomeStyle.body)
                    } else {
                        Text(message.text)
                    }
                }
                .font(.custom(Theme.fontFamily, size: 16, relativeTo: .callout))
                .foregroundStyle(Theme.ink)
                .lineSpacing(5)
                .fixedSize(horizontal: false, vertical: true)
                .padding(.top, 6)
                .onTapGesture { if let english = message.english { Speech.shared.speak(english) } }
                .accessibilityAddTraits(message.english != nil ? .isButton : [])
                .accessibilityHint(message.english != nil ? "Sesli okumak için dokunun" : "")
                Spacer(minLength: 16)
            }
        } else {
            HStack {
                Spacer(minLength: 60)
                Text(message.text)
                    .font(.custom(Theme.fontFamily, size: 16, relativeTo: .callout))
                    .foregroundStyle(Theme.ink)
                    .padding(.horizontal, 14)
                    .padding(.vertical, 11)
                    .background(Color(light: 0xF2F4F7, dark: 0x252A3B), in: RoundedRectangle(cornerRadius: 16, style: .continuous))
            }
        }
    }
}

/// Mesajların yanındaki 36pt yuvarlak JAI.
struct JAIAvatar: View {
    var mood: JAIView.Mood = .idle

    var body: some View {
        JAIView(mood: mood, size: 30)
            .frame(width: 36, height: 36)
            .background(Color(light: 0xE6EEFF, dark: 0x1F2A4D), in: Circle())
    }
}

/// JAI yazıyor: zıplayan üç nokta.
struct TypingIndicator: View {
    @State private var phase = 0

    var body: some View {
        HStack(spacing: 10) {
            JAIAvatar(mood: .thinking)
            HStack(spacing: 5) {
                ForEach(0..<3) { i in
                    Circle()
                        .fill(Theme.ai.opacity(phase == i ? 0.9 : 0.35))
                        .frame(width: 8, height: 8)
                        .offset(y: phase == i ? -3 : 0)
                }
            }
            .padding(.horizontal, 14)
            .padding(.vertical, 12)
            .background(Color(light: 0xF2F4F7, dark: 0x252A3B), in: Capsule())
        }
        .task {
            while !Task.isCancelled {
                try? await Task.sleep(for: .milliseconds(220))
                withAnimation(Motion.pop) { phase = (phase + 1) % 3 }
            }
        }
        .accessibilityLabel("JAI yazıyor")
    }
}

/// Büyük yuvarlak mikrofon düğmesi; kayıt sırasında çevresinde dalgalar yayılır.
struct MicButton: View {
    let recording: Bool
    let action: () -> Void
    @State private var wave = false

    var body: some View {
        Button(action: action) {
            ZStack {
                if recording {
                    ForEach(0..<2) { i in
                        Circle()
                            .stroke(Theme.accent.opacity(0.4), lineWidth: 2)
                            .frame(width: 68, height: 68)
                            .scaleEffect(wave ? 1.5 + Double(i) * 0.2 : 1)
                            .opacity(wave ? 0 : 0.9)
                    }
                }
                Circle()
                    .fill(Theme.accent)
                    .frame(width: 68, height: 68)
                    .shadow(color: Theme.accent.opacity(0.25), radius: 8, y: 4)
                Image(systemName: recording ? "stop.fill" : "mic.fill")
                    .font(.system(size: 26, weight: .semibold))
                    .foregroundStyle(.white)
                    .contentTransition(.symbolEffect(.replace))
            }
        }
        .buttonStyle(PressableCardStyle())
        .accessibilityLabel(recording ? "Kaydı bitir" : "Konuş")
        .onChange(of: recording) { _, new in
            wave = false
            if new { withAnimation(.easeOut(duration: 1.2).repeatForever(autoreverses: false)) { wave = true } }
        }
    }
}

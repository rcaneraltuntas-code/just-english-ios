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
    @FocusState private var fieldFocused: Bool

    var body: some View {
        VStack(spacing: 0) {
            header
            ScrollViewReader { proxy in
                ScrollView {
                    LazyVStack(alignment: .leading, spacing: 14) {
                        comingSoon
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
                    .padding(20)
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
        .background { AIBackground(animated: true) }
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

    private var header: some View {
        VStack(spacing: 10) {
            ZStack {
                Circle()
                    .fill(.white.opacity(0.35))
                    .frame(width: 128, height: 128)
                    .glass(cornerRadius: 64)
                JAIView(mood: tutor.thinking ? .thinking : (tutor.lastWasCorrect ? .happy : .idle), size: 96, bounceTrigger: jaiHop)
            }
            AIBadge(text: "JAI · İngilizce pratik arkadaşınız")
        }
        .padding(.top, 8)
        .padding(.bottom, 14)
        .frame(maxWidth: .infinity)
        .background {
            Theme.skyGradient.opacity(0.55).ignoresSafeArea(edges: .top)
        }
    }

    private var comingSoon: some View {
        Label("Gerçek yapay zekâ sohbeti yakında. Şimdilik JAI, derslerinizdeki kelimelerle sizinle pratik yapıyor.",
              systemImage: "sparkles")
            .font(.jakarta(.caption, weight: .semibold))
            .foregroundStyle(Theme.ai)
            .padding(12)
            .frame(maxWidth: .infinity, alignment: .leading)
            .glass(cornerRadius: 16, tint: Theme.ai)
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
                .font(.jakarta(.caption, weight: .medium))
                .foregroundStyle(.secondary)
            HStack(alignment: .center) {
                sideButton("Hints", icon: "sparkles", label: "İpucu") { tutor.hint() }
                Spacer()
                MicButton(recording: recognizer.status == .recording) {
                    Task { await recognizer.toggle() }
                }
                Spacer()
                sideButton("Keyboard", icon: "keyboard", label: "Klavye") {
                    withAnimation(Motion.smooth) { fieldFocused.toggle() }
                }
            }
            .padding(.horizontal, 44)
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
            VStack(spacing: 4) {
                Image(systemName: icon)
                    .font(.system(size: 18, weight: .semibold))
                    .foregroundStyle(Theme.ink)
                    .frame(width: 48, height: 48)
                    .glassCapsule(interactive: true)
                Text(label).font(.jakarta(.caption2, weight: .semibold)).foregroundStyle(.secondary)
            }
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

struct ChatBubble: View {
    let message: ChatTutor.Message

    var body: some View {
        if message.role == .jai {
            HStack(alignment: .top, spacing: 10) {
                JAIView(mood: .idle, size: 34)
                    .frame(width: 38, height: 38)
                    .background(Theme.surface, in: Circle())
                    .overlay(Circle().stroke(Theme.hairline))
                HStack(alignment: .top, spacing: 6) {
                    Text(message.text)
                        .font(.jakarta(.callout, weight: .medium))
                        .foregroundStyle(Theme.ink)
                        .fixedSize(horizontal: false, vertical: true)
                    if let english = message.english {
                        Button { Speech.shared.speak(english) } label: {
                            Image(systemName: "speaker.wave.2").foregroundStyle(Theme.accent)
                        }
                        .accessibilityLabel("Sesli oku")
                    }
                }
                .padding(.top, 8)
                Spacer(minLength: 30)
            }
        } else {
            HStack {
                Spacer(minLength: 60)
                Text(message.text)
                    .font(.jakarta(.callout, weight: .semibold))
                    .foregroundStyle(Theme.ink)
                    .padding(.horizontal, 16)
                    .padding(.vertical, 11)
                    .background(Theme.surfaceRaised, in: RoundedRectangle(cornerRadius: 18, style: .continuous))
            }
        }
    }
}

/// JAI yazıyor: zıplayan üç nokta.
struct TypingIndicator: View {
    @State private var phase = 0

    var body: some View {
        HStack(spacing: 10) {
            JAIView(mood: .thinking, size: 34)
                .frame(width: 38, height: 38)
                .background(Theme.surface, in: Circle())
                .overlay(Circle().stroke(Theme.hairline))
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
            .glassCapsule()
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
                            .frame(width: 84, height: 84)
                            .scaleEffect(wave ? 1.5 + Double(i) * 0.2 : 1)
                            .opacity(wave ? 0 : 0.9)
                    }
                }
                Circle()
                    .fill(Theme.brandGradient)
                    .frame(width: 84, height: 84)
                    .shadow(color: Theme.accent.opacity(0.45), radius: 16, y: 8)
                Image(systemName: recording ? "stop.fill" : "mic.fill")
                    .font(.system(size: 30, weight: .bold))
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

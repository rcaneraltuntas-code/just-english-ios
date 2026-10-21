import SwiftUI

/// JAI: Just English'in konuşma balonu biçimindeki maskotu. Tamamen SwiftUI ile çizilir,
/// böylece her boyutta keskin görünür ve ruh haline göre canlı olarak değişir.
struct JAIView: View {
    enum Mood: Equatable {
        case idle, happy, sad, thinking, talking, celebrate, sleepy
    }

    var mood: Mood = .idle
    var size: CGFloat = 120
    var color: Color = Theme.coral
    /// Değiştiğinde JAI bir kez zıplar (ör. her doğru cevapta artırın).
    var bounceTrigger: Int = 0

    @State private var blink = false
    @State private var look: CGSize = .zero
    @State private var breathe = false
    @State private var talkOpen = false
    @Environment(\.accessibilityReduceMotion) private var reduceMotion

    private var unit: CGFloat { size / 100 }

    var body: some View {
        ZStack {
            // Gölge: zıplarken küçülür.
            Ellipse()
                .fill(.black.opacity(0.12))
                .frame(width: 62 * unit, height: 10 * unit)
                .offset(y: 54 * unit)

            body3D
                .keyframeAnimator(initialValue: Pose(), trigger: bounceTrigger) { content, pose in
                    content
                        .scaleEffect(x: pose.squashX, y: pose.squashY, anchor: .bottom)
                        .offset(y: pose.lift)
                        .rotationEffect(.degrees(pose.tilt))
                } keyframes: { _ in
                    KeyframeTrack(\.squashY) {
                        SpringKeyframe(0.85, duration: 0.1)
                        SpringKeyframe(1.12, duration: 0.18)
                        SpringKeyframe(1, duration: 0.3)
                    }
                    KeyframeTrack(\.squashX) {
                        SpringKeyframe(1.12, duration: 0.1)
                        SpringKeyframe(0.92, duration: 0.18)
                        SpringKeyframe(1, duration: 0.3)
                    }
                    KeyframeTrack(\.lift) {
                        LinearKeyframe(0, duration: 0.1)
                        SpringKeyframe(-26 * unit, duration: 0.2)
                        SpringKeyframe(0, duration: 0.35, spring: .bouncy)
                    }
                    KeyframeTrack(\.tilt) {
                        LinearKeyframe(0, duration: 0.12)
                        SpringKeyframe(mood == .sad ? 0 : -8, duration: 0.18)
                        SpringKeyframe(0, duration: 0.4)
                    }
                }
        }
        .frame(width: size, height: size * 1.1)
        .task(id: mood) { await animateMood() }
        .task { await blinkLoop() }
        .accessibilityHidden(true)
    }

    private var body3D: some View {
        ZStack {
            // Gövde: kuyruklu konuşma balonu, üstten ışık alan degrade.
            BubbleShape()
                .fill(color.blended(with: .black, amount: 0.22))
                .offset(y: 4 * unit)
            BubbleShape()
                .fill(LinearGradient(colors: [color.blended(with: .white, amount: 0.18), color],
                                     startPoint: .top, endPoint: .bottom))
            // Parlaklık
            Capsule()
                .fill(.white.opacity(0.28))
                .frame(width: 26 * unit, height: 8 * unit)
                .rotationEffect(.degrees(-18))
                .offset(x: -24 * unit, y: -30 * unit)

            face
                .offset(y: -4 * unit)
        }
        .frame(width: 100 * unit, height: 92 * unit)
        .scaleEffect(y: breathe ? 1.025 : 1, anchor: .bottom)
        .rotationEffect(.degrees(mood == .thinking ? -6 : (mood == .sad ? 4 : 0)), anchor: .bottom)
        .offset(y: mood == .sleepy ? 4 * unit : 0)
        .animation(Motion.smooth, value: mood)
    }

    private var face: some View {
        VStack(spacing: 8 * unit) {
            HStack(spacing: 18 * unit) {
                eye
                eye
            }
            ZStack {
                // Yanaklar
                HStack(spacing: 46 * unit) {
                    Circle().fill(Color.pink.opacity(mood == .happy || mood == .celebrate ? 0.45 : 0.25))
                    Circle().fill(Color.pink.opacity(mood == .happy || mood == .celebrate ? 0.45 : 0.25))
                }
                .frame(height: 9 * unit)
                .offset(y: -4 * unit)
                mouth
            }
        }
    }

    @ViewBuilder private var eye: some View {
        let w = 16 * unit, h = 20 * unit
        switch mood {
        case .happy, .celebrate:
            // Mutlu: ters "U" kavisli gözler (^ ^)
            HappyEyeShape()
                .stroke(.white, style: StrokeStyle(lineWidth: 4 * unit, lineCap: .round))
                .frame(width: w, height: h * 0.5)
                .frame(height: h)
        case .sleepy:
            Capsule().fill(.white).frame(width: w, height: 3.5 * unit).frame(height: h)
        default:
            ZStack {
                Ellipse().fill(.white)
                Circle()
                    .fill(Color(white: 0.12))
                    .frame(width: 9 * unit)
                    .overlay(alignment: .topTrailing) {
                        Circle().fill(.white).frame(width: 3 * unit).offset(x: -1 * unit, y: 1 * unit)
                    }
                    .offset(x: look.width * unit, y: (mood == .sad ? 3 : look.height) * unit)
            }
            .frame(width: w, height: h)
            .scaleEffect(y: blink ? 0.08 : (mood == .sad ? 0.8 : 1))
            .overlay(alignment: .top) {
                if mood == .sad {
                    // Üzgün kaşlar
                    Capsule().fill(.white).frame(width: w, height: 3 * unit)
                        .rotationEffect(.degrees(12)).offset(y: -6 * unit)
                }
            }
        }
    }

    @ViewBuilder private var mouth: some View {
        switch mood {
        case .happy, .celebrate:
            SmileShape(depth: 1)
                .fill(Color(white: 0.12))
                .frame(width: 22 * unit, height: 12 * unit)
                .overlay(alignment: .bottom) {
                    Ellipse().fill(Color(red: 1, green: 0.45, blue: 0.5)).frame(width: 11 * unit, height: 5 * unit).offset(y: -1 * unit)
                }
                .clipShape(SmileShape(depth: 1))
        case .sad:
            SmileShape(depth: -1)
                .stroke(Color(white: 0.12), style: StrokeStyle(lineWidth: 3 * unit, lineCap: .round))
                .frame(width: 16 * unit, height: 6 * unit)
        case .talking:
            Ellipse()
                .fill(Color(white: 0.12))
                .frame(width: 12 * unit, height: (talkOpen ? 10 : 4) * unit)
        case .thinking:
            Capsule().fill(Color(white: 0.12)).frame(width: 10 * unit, height: 3 * unit).offset(x: 6 * unit)
        case .sleepy:
            Circle().fill(Color(white: 0.12)).frame(width: 6 * unit)
        case .idle:
            SmileShape(depth: 0.6)
                .stroke(Color(white: 0.12), style: StrokeStyle(lineWidth: 3 * unit, lineCap: .round))
                .frame(width: 16 * unit, height: 6 * unit)
        }
    }

    private func blinkLoop() async {
        guard !reduceMotion else { return }
        while !Task.isCancelled {
            try? await Task.sleep(for: .seconds(Double.random(in: 2.2...4.5)))
            withAnimation(.easeIn(duration: 0.07)) { blink = true }
            try? await Task.sleep(for: .milliseconds(110))
            withAnimation(.easeOut(duration: 0.1)) { blink = false }
            // Ara sıra etrafa bakar.
            if Bool.random() {
                withAnimation(Motion.smooth) {
                    look = CGSize(width: .random(in: -2.5...2.5), height: .random(in: -2...1.5))
                }
            }
        }
    }

    private func animateMood() async {
        guard !reduceMotion else { return }
        withAnimation(.easeInOut(duration: 1.6).repeatForever(autoreverses: true)) { breathe = true }
        switch mood {
        case .thinking:
            withAnimation(Motion.smooth) { look = CGSize(width: 2.5, height: -2.5) }
        case .talking:
            while !Task.isCancelled && mood == .talking {
                withAnimation(.easeInOut(duration: 0.12)) { talkOpen.toggle() }
                try? await Task.sleep(for: .milliseconds(140))
            }
        default:
            withAnimation(Motion.smooth) { look = .zero }
        }
    }

    struct Pose {
        var squashX: CGFloat = 1
        var squashY: CGFloat = 1
        var lift: CGFloat = 0
        var tilt: Double = 0
    }
}

/// Sol altta kuyruğu olan yuvarlak konuşma balonu.
struct BubbleShape: Shape {
    func path(in rect: CGRect) -> Path {
        let body = CGRect(x: rect.minX, y: rect.minY, width: rect.width, height: rect.height * 0.86)
        var path = Path(roundedRect: body, cornerRadius: rect.width * 0.34, style: .continuous)
        let tailTop = body.maxY - rect.height * 0.04
        path.move(to: CGPoint(x: rect.minX + rect.width * 0.22, y: tailTop))
        path.addQuadCurve(to: CGPoint(x: rect.minX + rect.width * 0.12, y: rect.maxY),
                          control: CGPoint(x: rect.minX + rect.width * 0.22, y: rect.maxY - rect.height * 0.04))
        path.addQuadCurve(to: CGPoint(x: rect.minX + rect.width * 0.44, y: tailTop),
                          control: CGPoint(x: rect.minX + rect.width * 0.3, y: rect.maxY - rect.height * 0.02))
        path.closeSubpath()
        return path
    }
}

struct HappyEyeShape: Shape {
    func path(in rect: CGRect) -> Path {
        var path = Path()
        path.move(to: CGPoint(x: rect.minX, y: rect.maxY))
        path.addQuadCurve(to: CGPoint(x: rect.maxX, y: rect.maxY), control: CGPoint(x: rect.midX, y: rect.minY - rect.height * 0.6))
        return path
    }
}

/// depth > 0 gülümseme (dolu ağız için kapalı yol), depth < 0 üzgün kavis.
struct SmileShape: Shape {
    var depth: CGFloat

    func path(in rect: CGRect) -> Path {
        var path = Path()
        if depth >= 1 {
            path.move(to: CGPoint(x: rect.minX, y: rect.minY))
            path.addLine(to: CGPoint(x: rect.maxX, y: rect.minY))
            path.addQuadCurve(to: CGPoint(x: rect.minX, y: rect.minY), control: CGPoint(x: rect.midX, y: rect.maxY * 1.9))
            path.closeSubpath()
        } else if depth > 0 {
            path.move(to: CGPoint(x: rect.minX, y: rect.minY))
            path.addQuadCurve(to: CGPoint(x: rect.maxX, y: rect.minY), control: CGPoint(x: rect.midX, y: rect.maxY * (1 + depth)))
        } else {
            path.move(to: CGPoint(x: rect.minX, y: rect.maxY))
            path.addQuadCurve(to: CGPoint(x: rect.maxX, y: rect.maxY), control: CGPoint(x: rect.midX, y: rect.minY - rect.height))
        }
        return path
    }
}

/// JAI'nin yanında beliren konuşma balonu.
struct JAISays: View {
    let text: String
    var mood: JAIView.Mood = .talking
    var size: CGFloat = 76
    var bounceTrigger = 0

    @State private var shown = false
    /// "Konuşuyor" ruh hali metin okunacak kadar sürer, sonra JAI sakinleşir.
    @State private var talkingDone = false

    var body: some View {
        HStack(alignment: .bottom, spacing: 10) {
            JAIView(mood: mood == .talking && talkingDone ? .idle : mood, size: size, bounceTrigger: bounceTrigger)
            Text(text)
                .font(.jakarta(.callout, weight: .semibold))
                .fixedSize(horizontal: false, vertical: true)
                .padding(.horizontal, 14)
                .padding(.vertical, 11)
                .background(Theme.surface, in: SpeechCalloutShape())
                .overlay(SpeechCalloutShape().stroke(Color(uiColor: .systemGray4), lineWidth: 2))
                .scaleEffect(shown ? 1 : 0.6, anchor: .bottomLeading)
                .opacity(shown ? 1 : 0)
                .padding(.bottom, size * 0.3)
        }
        .onAppear { withAnimation(Motion.pop.delay(0.15)) { shown = true } }
        .task(id: text) {
            talkingDone = false
            try? await Task.sleep(for: .seconds(min(3, 0.6 + Double(text.count) * 0.035)))
            talkingDone = true
        }
    }
}

/// Solunda küçük bir çıkıntı olan söz balonu.
struct SpeechCalloutShape: Shape {
    func path(in rect: CGRect) -> Path {
        var path = Path(roundedRect: rect, cornerRadius: 16, style: .continuous)
        path.move(to: CGPoint(x: rect.minX, y: rect.maxY - 22))
        path.addLine(to: CGPoint(x: rect.minX - 9, y: rect.maxY - 12))
        path.addLine(to: CGPoint(x: rect.minX, y: rect.maxY - 10))
        path.closeSubpath()
        return path
    }
}

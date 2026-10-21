import SwiftUI

// Uygulamanın hareket dili: basılınca çöken 3D düğmeler, yanlışta sallanma, başarıda konfeti,
// kazanılan XP'nin uçarak kaybolması ve ekrana sırayla giren öğeler.

enum Motion {
    static let press = Animation.spring(response: 0.18, dampingFraction: 0.7)
    static let pop = Animation.spring(response: 0.35, dampingFraction: 0.55)
    static let smooth = Animation.spring(response: 0.45, dampingFraction: 0.85)
}

// MARK: - 3D düğme

/// Alt kenarı koyu, basılınca aşağı çöken düğme. Birincil eylemler için.
struct DepthButtonStyle: ButtonStyle {
    var color: Color = Theme.accent
    var foreground: Color = .white
    var height: CGFloat = 54
    @Environment(\.isEnabled) private var isEnabled

    func makeBody(configuration: Configuration) -> some View {
        let face = isEnabled ? color : Color(uiColor: .systemGray4)
        let pressed = configuration.isPressed
        return configuration.label
            .font(.jakarta(.headline, weight: .heavy))
            .foregroundStyle(isEnabled ? foreground : Color(uiColor: .systemGray))
            .frame(maxWidth: .infinity, minHeight: height)
            .background(face, in: RoundedRectangle(cornerRadius: 16, style: .continuous))
            .background(
                RoundedRectangle(cornerRadius: 16, style: .continuous)
                    .fill(face.blended(with: .black, amount: 0.25))
                    .offset(y: pressed ? 0 : 5)
            )
            .offset(y: pressed ? 5 : 0)
            .padding(.bottom, 5)
            .animation(Motion.press, value: pressed)
            .sensoryFeedback(.impact(weight: .light), trigger: pressed) { _, new in new }
    }
}

/// Seçenek kartları için: kenarlıklı yüzey, basılınca hafifçe çöker. `highlight` seçili/doğru/yanlış rengidir.
struct TileButtonStyle: ButtonStyle {
    var highlight: Color?

    func makeBody(configuration: Configuration) -> some View {
        let pressed = configuration.isPressed
        let edge = highlight ?? Color(uiColor: .systemGray4)
        let shape = RoundedRectangle(cornerRadius: 16, style: .continuous)
        return configuration.label
            .background((highlight ?? .clear).opacity(0.12), in: shape)
            .background(Theme.surface, in: shape)
            .overlay(shape.stroke(edge, lineWidth: 2))
            .background(shape.fill(edge).offset(y: pressed ? 0 : 4))
            .offset(y: pressed ? 4 : 0)
            .padding(.bottom, 4)
            .animation(Motion.press, value: pressed)
    }
}

extension Color {
    /// İki rengi karıştırır (Color.mix iOS 18 ile geldiği için UIKit üzerinden).
    func blended(with other: Color, amount: CGFloat) -> Color {
        Color(uiColor: UIColor { traits in
            let a = UIColor(self).resolvedColor(with: traits), b = UIColor(other).resolvedColor(with: traits)
            var (r1, g1, b1, a1): (CGFloat, CGFloat, CGFloat, CGFloat) = (0, 0, 0, 0)
            var (r2, g2, b2, a2): (CGFloat, CGFloat, CGFloat, CGFloat) = (0, 0, 0, 0)
            a.getRed(&r1, green: &g1, blue: &b1, alpha: &a1)
            b.getRed(&r2, green: &g2, blue: &b2, alpha: &a2)
            return UIColor(red: r1 + (r2 - r1) * amount, green: g1 + (g2 - g1) * amount,
                           blue: b1 + (b2 - b1) * amount, alpha: a1 + (a2 - a1) * amount)
        })
    }
}

// MARK: - Sallanma

struct ShakeEffect: GeometryEffect {
    var travel: CGFloat = 10
    var animatableData: CGFloat

    func effectValue(size: CGSize) -> ProjectionTransform {
        ProjectionTransform(CGAffineTransform(translationX: travel * sin(animatableData * .pi * 4), y: 0))
    }
}

extension View {
    /// `trigger` her arttığında görünümü yatay sallar (yanlış cevap).
    func shake(_ trigger: Int) -> some View {
        modifier(ShakeEffect(animatableData: CGFloat(trigger)))
            .animation(.linear(duration: 0.4), value: trigger)
    }

    /// Ekrana açılışta sırayla, aşağıdan kayarak gelir.
    func staggeredAppear(_ index: Int, delay: Double = 0.05) -> some View {
        modifier(StaggeredAppear(index: index, delay: delay))
    }
}

private struct StaggeredAppear: ViewModifier {
    let index: Int
    let delay: Double
    @State private var visible = false
    @Environment(\.accessibilityReduceMotion) private var reduceMotion

    func body(content: Content) -> some View {
        content
            .opacity(visible ? 1 : 0)
            .offset(y: visible || reduceMotion ? 0 : 18)
            .onAppear {
                withAnimation(Motion.smooth.delay(Double(min(index, 12)) * delay)) { visible = true }
            }
    }
}

// MARK: - Konfeti

/// Tek seferlik konfeti patlaması. `active` true olduğunda başlar, yaklaşık 3 saniye sürer.
struct ConfettiView: View {
    var colors: [Color] = [Theme.accent, Theme.success, Theme.warning, Theme.streak, Theme.color(for: .b2), Theme.color(for: .c1)]
    var count = 90

    @State private var start = Date.now
    @State private var particles: [Particle] = []
    @Environment(\.accessibilityReduceMotion) private var reduceMotion

    struct Particle {
        let x: CGFloat, vx: CGFloat, vy: CGFloat, spin: Double, size: CGFloat, color: Int, shape: Int
    }

    var body: some View {
        TimelineView(.animation) { timeline in
            Canvas { context, size in
                let t = timeline.date.timeIntervalSince(start)
                guard t < 3.2 else { return }
                for p in particles {
                    let x = p.x * size.width + p.vx * t * 60
                    let y = -20 + p.vy * t * 60 + 260 * t * t
                    guard y < size.height + 20 else { continue }
                    var c = context
                    c.opacity = max(0, 1 - max(0, t - 2.2))
                    c.translateBy(x: x, y: y)
                    c.rotate(by: .degrees(p.spin * t * 360))
                    let rect = CGRect(x: -p.size / 2, y: -p.size / 4, width: p.size, height: p.shape == 0 ? p.size / 2 : p.size)
                    let path = p.shape == 2 ? Path(ellipseIn: rect) : Path(roundedRect: rect, cornerRadius: 1.5)
                    c.fill(path, with: .color(colors[p.color % colors.count]))
                }
            }
        }
        .allowsHitTesting(false)
        .ignoresSafeArea()
        .opacity(reduceMotion ? 0 : 1)
        .onAppear {
            start = .now
            particles = (0..<count).map { _ in
                Particle(x: .random(in: 0.1...0.9), vx: .random(in: -3...3), vy: .random(in: -9 ... -3),
                         spin: .random(in: -2...2), size: .random(in: 7...12), color: .random(in: 0..<100), shape: .random(in: 0...2))
            }
        }
    }
}

// MARK: - Uçan XP

/// "+2 XP" gibi küçük bir rozet: yukarı süzülür ve kaybolur.
struct FloatingReward: View {
    let text: String
    var color: Color = Theme.warning
    @State private var popped = false
    @State private var risen = false

    var body: some View {
        Text(text)
            .font(.jakarta(.headline, weight: .heavy))
            .foregroundStyle(.white)
            .padding(.horizontal, 12)
            .padding(.vertical, 6)
            .background(color, in: Capsule())
            .shadow(color: color.opacity(0.5), radius: 8, y: 4)
            .scaleEffect(popped ? 1 : 0.4)
            .offset(y: risen ? -70 : 0)
            .opacity(risen ? 0 : 1)
            .onAppear {
                withAnimation(Motion.pop) { popped = true }
                withAnimation(.easeIn(duration: 0.9).delay(0.35)) { risen = true }
            }
            .allowsHitTesting(false)
    }
}

// MARK: - Sayaç

/// Değiştiğinde rakamları kaydırarak güncellenen sayı.
struct RollingNumber: View {
    let value: Int
    var prefix = ""
    var suffix = ""
    var font: Font = .jakarta(.title2, weight: .heavy)

    var body: some View {
        Text("\(prefix)\(value)\(suffix)")
            .font(font)
            .monospacedDigit()
            .contentTransition(.numericText(value: Double(value)))
            .animation(Motion.smooth, value: value)
    }
}

/// Açılışta 0'dan hedef değere sayarak yükselen sayı (özet ekranları).
struct CountUpNumber: View {
    let target: Int
    var prefix = ""
    var suffix = ""
    var font: Font = .jakarta(.title2, weight: .heavy)
    var delay: Double = 0
    @State private var shown = 0

    var body: some View {
        RollingNumber(value: shown, prefix: prefix, suffix: suffix, font: font)
            .task {
                try? await Task.sleep(for: .seconds(delay))
                let steps = min(max(target, 1), 24)
                for step in 1...steps {
                    try? await Task.sleep(for: .milliseconds(35))
                    shown = target * step / steps
                }
            }
    }
}

// MARK: - Geri sayım

/// Oyun başlangıcında 3-2-1-Başla! Bitince `onFinish` çağrılır.
struct CountdownOverlay: View {
    let onFinish: () -> Void
    @State private var value = 3
    @State private var scale: CGFloat = 0.3

    var body: some View {
        ZStack {
            Rectangle().fill(.ultraThinMaterial).ignoresSafeArea()
            Text(value > 0 ? "\(value)" : "Başla!")
                .font(.custom(Theme.fontFamily, size: value > 0 ? 120 : 64).weight(.heavy))
                .scaleEffect(scale)
                .foregroundStyle(value > 0 ? Theme.accent : Theme.success)
                .id(value)
                .transition(.scale.combined(with: .opacity))
        }
        .task {
            for next in [3, 2, 1, 0] {
                value = next
                scale = 0.3
                withAnimation(Motion.pop) { scale = 1 }
                Haptics.tap()
                try? await Task.sleep(for: .milliseconds(next == 0 ? 450 : 700))
            }
            onFinish()
        }
    }
}

// MARK: - Yıldızlar

/// Sonuç ekranlarında 0-3 yıldız, tek tek zıplayarak gelir.
struct StarRating: View {
    let stars: Int
    @State private var shown = 0

    var body: some View {
        HStack(spacing: 10) {
            ForEach(0..<3, id: \.self) { i in
                Image(systemName: "star.fill")
                    .font(.system(size: i == 1 ? 54 : 42, weight: .bold))
                    .foregroundStyle(i < shown ? Theme.warning : Color(uiColor: .systemGray5))
                    .shadow(color: i < shown ? Theme.warning.opacity(0.5) : .clear, radius: 8, y: 3)
                    .scaleEffect(i < shown ? 1 : 0.7)
                    .rotationEffect(.degrees(i < shown ? 0 : -25))
                    .offset(y: i == 1 ? -10 : 0)
            }
        }
        .task {
            for i in 0..<stars {
                try? await Task.sleep(for: .milliseconds(i == 0 ? 300 : 280))
                withAnimation(Motion.pop) { shown = i + 1 }
                Haptics.success()
            }
        }
    }
}

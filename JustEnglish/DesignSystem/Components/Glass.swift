import SwiftUI

// Yapay zekâ temalı tasarım dilinin temel parçaları: cam yüzeyler (liquid glass), havadar arka plan,
// arka plandaki sinir ağı dokusu ve ince kenarlıklı ikincil düğme.

extension View {
    /// Cam yüzey: iOS 26'da sistemin liquid glass etkisi, daha eskilerde buzlu malzeme ve ince beyaz kenar.
    @ViewBuilder
    func glass(cornerRadius: CGFloat = 22, tint: Color? = nil, interactive: Bool = false) -> some View {
        let shape = RoundedRectangle(cornerRadius: cornerRadius, style: .continuous)
        if #available(iOS 26, *) {
            self.glassEffect(Self.glassStyle(tint: tint, interactive: interactive), in: shape)
        } else {
            self
                .background((tint ?? .clear).opacity(0.18), in: shape)
                .background(.ultraThinMaterial, in: shape)
                .overlay(shape.stroke(LinearGradient(colors: [.white.opacity(0.85), .white.opacity(0.25)],
                                                     startPoint: .topLeading, endPoint: .bottomTrailing), lineWidth: 1))
                .shadow(color: Theme.ink.opacity(0.08), radius: 12, y: 6)
        }
    }

    /// Kapsül biçiminde cam (çipler, sekme çubuğu, yüzen düğmeler).
    @ViewBuilder
    func glassCapsule(tint: Color? = nil, interactive: Bool = false) -> some View {
        if #available(iOS 26, *) {
            self.glassEffect(Self.glassStyle(tint: tint, interactive: interactive), in: Capsule())
        } else {
            self
                .background((tint ?? .clear).opacity(0.18), in: Capsule())
                .background(.ultraThinMaterial, in: Capsule())
                .overlay(Capsule().stroke(.white.opacity(0.7), lineWidth: 1))
                .shadow(color: Theme.ink.opacity(0.08), radius: 12, y: 6)
        }
    }

    @available(iOS 26, *)
    private static func glassStyle(tint: Color?, interactive: Bool) -> Glass {
        var style = Glass.regular
        if let tint { style = style.tint(tint.opacity(0.35)) }
        if interactive { style = style.interactive() }
        return style
    }

    /// Ekranın havadar zemini (durağan). Ana sayfa ve sohbet gibi yerlerde `AIBackground(animated: true)` kullanılır.
    func appBackground() -> some View {
        background { AIBackground(animated: false) }
    }
}

/// Referanstaki gibi düz, açık mavi degrade ve çok yumuşak ışık lekeleri.
struct AIBackground: View {
    var animated = true
    @Environment(\.accessibilityReduceMotion) private var reduceMotion

    var body: some View {
        ZStack {
            LinearGradient(colors: [Theme.backgroundTop, Theme.background], startPoint: .top, endPoint: .bottom)
            if animated {
                TimelineView(.animation(minimumInterval: 1 / 24, paused: reduceMotion)) { timeline in
                    glows(t: timeline.date.timeIntervalSinceReferenceDate)
                }
            } else {
                glows(t: 0)
            }
        }
        .ignoresSafeArea()
        .allowsHitTesting(false)
        .accessibilityHidden(true)
    }

    private func glows(t: Double) -> some View {
        GeometryReader { geo in
            let w = geo.size.width, h = geo.size.height
            ZStack {
                glow(Theme.accent.opacity(0.12), size: w * 0.9)
                    .position(x: w * (0.2 + 0.08 * cos(t * 0.15)), y: h * (0.12 + 0.04 * sin(t * 0.12)))
                glow(Theme.aiViolet.opacity(0.07), size: w * 0.8)
                    .position(x: w * (0.85 + 0.06 * sin(t * 0.11)), y: h * (0.3 + 0.05 * cos(t * 0.13)))
                glow(Color(light: 0xCFE0FF, dark: 0x1E2A50).opacity(0.3), size: w * 0.7)
                    .position(x: w * (0.4 + 0.08 * sin(t * 0.09)), y: h * (0.7 + 0.04 * cos(t * 0.1)))
            }
        }
    }

    private func glow(_ color: Color, size: CGFloat) -> some View {
        Circle().fill(color).frame(width: size, height: size).blur(radius: 70)
    }
}

/// Noktalar ve onları bağlayan ince çizgiler: yapay zekâ dokusu. Yavaşça süzülür.
struct NeuralNetwork: View {
    var animated = true
    var color: Color = Theme.ai
    @Environment(\.accessibilityReduceMotion) private var reduceMotion

    /// Sabit tohumla üretilen noktalar: her açılışta aynı desen.
    private static let nodes: [(x: Double, y: Double, phase: Double)] = {
        var seed: UInt64 = 42
        func next() -> Double {
            seed = seed &* 6364136223846793005 &+ 1442695040888963407
            return Double(seed >> 33) / Double(UInt32.max)
        }
        return (0..<22).map { _ in (next(), next() * 0.55, next() * 6.28) }
    }()

    var body: some View {
        TimelineView(.animation(minimumInterval: 1 / 20, paused: reduceMotion || !animated)) { timeline in
            let t = animated ? timeline.date.timeIntervalSinceReferenceDate : 0
            Canvas { context, size in
                let points = Self.nodes.map { node in
                    CGPoint(x: size.width * (node.x + 0.015 * sin(t * 0.4 + node.phase)),
                            y: size.height * (node.y + 0.01 * cos(t * 0.35 + node.phase)))
                }
                let limit = size.width * 0.28
                for i in points.indices {
                    for j in points.indices where j > i {
                        let d = hypot(points[i].x - points[j].x, points[i].y - points[j].y)
                        guard d < limit else { continue }
                        var path = Path()
                        path.move(to: points[i])
                        path.addLine(to: points[j])
                        context.stroke(path, with: .color(color.opacity(0.14 * (1 - d / limit))), lineWidth: 0.8)
                    }
                }
                for (i, p) in points.enumerated() {
                    let r: CGFloat = i.isMultiple(of: 3) ? 2.6 : 1.6
                    context.fill(Path(ellipseIn: CGRect(x: p.x - r, y: p.y - r, width: r * 2, height: r * 2)),
                                 with: .color(color.opacity(0.3)))
                }
            }
        }
    }
}

/// İkincil eylem: beyaz zemin, ince vurgu kenarı, vurgu renginde yazı (referanstaki "I already have an account").
struct OutlineButtonStyle: ButtonStyle {
    var color: Color = Theme.accent
    var height: CGFloat = 54
    @Environment(\.isEnabled) private var isEnabled

    func makeBody(configuration: Configuration) -> some View {
        let shape = RoundedRectangle(cornerRadius: 16, style: .continuous)
        return configuration.label
            .font(.jakarta(.headline, weight: .bold))
            .foregroundStyle(isEnabled ? color : .secondary)
            .frame(maxWidth: .infinity, minHeight: height)
            .background(Theme.surface, in: shape)
            .overlay(shape.stroke(isEnabled ? color.opacity(0.7) : Theme.hairline, lineWidth: 1.5))
            .scaleEffect(configuration.isPressed ? 0.97 : 1)
            .animation(Motion.press, value: configuration.isPressed)
    }
}

extension ButtonStyle where Self == OutlineButtonStyle {
    static var outline: OutlineButtonStyle { OutlineButtonStyle() }
}

/// Küçük, parlayan "yapay zekâ" rozeti (ör. "JAI · çevrim içi").
struct AIBadge: View {
    let text: String
    var body: some View {
        HStack(spacing: 6) {
            Circle().fill(Color(light: 0x22D3EE, dark: 0x67E8F9)).frame(width: 8, height: 8)
                .shadow(color: Color(light: 0x22D3EE, dark: 0x67E8F9), radius: 4)
            Text(text).font(.jakarta(.caption, weight: .bold)).foregroundStyle(Theme.ink)
        }
        .padding(.horizontal, 12)
        .padding(.vertical, 6)
        .glassCapsule()
    }
}

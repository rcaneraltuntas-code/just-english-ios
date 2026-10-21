import SwiftUI
import JECore

/// Birincil eylem: 3D, basılınca çöken düğme (bkz. Motion.swift).
typealias PrimaryButtonStyle = DepthButtonStyle

extension ButtonStyle where Self == DepthButtonStyle {
    static var primary: DepthButtonStyle { DepthButtonStyle() }
    /// İkincil eylem: açık yüzeyli 3D düğme, vurgu renginde yazı.
    static var secondary: DepthButtonStyle { DepthButtonStyle(color: Theme.surfaceRaised, foreground: Theme.accent) }
}

struct CardModifier: ViewModifier {
    func body(content: Content) -> some View {
        content
            .padding(16)
            .frame(maxWidth: .infinity, alignment: .leading)
            .background(Theme.surface, in: RoundedRectangle(cornerRadius: Theme.cornerRadius))
    }
}

extension View {
    func card() -> some View { modifier(CardModifier()) }
}

struct LevelBadge: View {
    let level: CEFRLevel

    var body: some View {
        Text(level.rawValue.uppercased())
            .font(.jakarta(.caption, weight: .bold))
            .foregroundStyle(.white)
            .padding(.horizontal, 8)
            .padding(.vertical, 3)
            .background(Theme.color(for: level), in: Capsule())
    }
}

struct ProgressBar: View {
    let value: Double
    var color: Color = Theme.accent
    var height: CGFloat = 8

    var body: some View {
        GeometryReader { geo in
            let width = geo.size.width * min(max(value, 0), 1)
            ZStack(alignment: .leading) {
                Capsule().fill(Color(uiColor: .systemGray5))
                Capsule()
                    .fill(color)
                    .frame(width: value > 0 ? max(width, height) : 0)
                    // Üstteki parlak şerit dolguya hacim verir.
                    .overlay(alignment: .top) {
                        Capsule()
                            .fill(.white.opacity(0.3))
                            .frame(height: height * 0.28)
                            .padding(.horizontal, height * 0.45)
                            .padding(.top, height * 0.2)
                    }
            }
        }
        .frame(height: height)
        .animation(Motion.smooth, value: value)
    }
}

struct ProgressRing: View {
    let value: Double
    var color: Color = Theme.accent
    var lineWidth: CGFloat = 8

    var body: some View {
        ZStack {
            Circle().stroke(color.opacity(0.15), lineWidth: lineWidth)
            Circle()
                .trim(from: 0, to: min(max(value, 0), 1))
                .stroke(color, style: StrokeStyle(lineWidth: lineWidth, lineCap: .round))
                .rotationEffect(.degrees(-90))
        }
        .animation(.easeOut, value: value)
    }
}

struct SectionTitle: View {
    let text: String
    var body: some View {
        Text(text)
            .font(.jakarta(.title3, weight: .bold))
            .frame(maxWidth: .infinity, alignment: .leading)
    }
}

/// Bir İngilizce metni sesli okuyan küçük düğme.
struct SpeakButton: View {
    let text: String
    var rate: Float = 0.45

    var body: some View {
        Button {
            Speech.shared.speak(text, rate: rate)
        } label: {
            Image(systemName: "speaker.wave.2.fill")
                .font(.jakarta(.body, weight: .semibold))
                .frame(width: 36, height: 36)
                .background(Theme.accent.opacity(0.12), in: Circle())
        }
        .buttonStyle(.plain)
        .foregroundStyle(Theme.accent)
        .accessibilityLabel("Sesli oku")
    }
}

@MainActor
enum Haptics {
    static func success() { UINotificationFeedbackGenerator().notificationOccurred(.success) }
    static func error() { UINotificationFeedbackGenerator().notificationOccurred(.error) }
    static func tap() { UIImpactFeedbackGenerator(style: .light).impactOccurred() }
}

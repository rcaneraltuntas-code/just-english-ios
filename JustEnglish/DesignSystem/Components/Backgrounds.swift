import SwiftUI

/// Yavaşça süzülen, bulanık renk lekeleri. Karşılama, ana sayfa başlığı ve sonuç ekranlarının arka planı.
struct AuroraBackground: View {
    var colors: [Color] = [Theme.accent.opacity(0.35), Theme.color(for: .a2), Theme.warning]
    var intensity: Double = 0.55
    @Environment(\.accessibilityReduceMotion) private var reduceMotion

    var body: some View {
        TimelineView(.animation(minimumInterval: 1 / 30, paused: reduceMotion)) { timeline in
            let t = timeline.date.timeIntervalSinceReferenceDate
            GeometryReader { geo in
                let w = geo.size.width, h = geo.size.height
                ZStack {
                    ForEach(colors.indices, id: \.self) { i in
                        let phase = Double(i) * 2.1
                        Circle()
                            .fill(colors[i].opacity(intensity))
                            .frame(width: max(w, h) * 0.75)
                            .position(x: w * (0.5 + 0.35 * cos(t * 0.13 + phase)),
                                      y: h * (0.45 + 0.3 * sin(t * 0.11 + phase * 1.3)))
                    }
                }
                .blur(radius: 60)
            }
        }
        .ignoresSafeArea()
        .allowsHitTesting(false)
    }
}

/// Arka planda yavaşça dönen İngilizce kelimelerden oluşan desen: Just English'e özgü doku.
struct WordPattern: View {
    var words = ["hello", "learn", "speak", "listen", "write", "read", "play", "talk", "think", "grow", "smile", "travel"]
    var color: Color = .white
    @Environment(\.accessibilityReduceMotion) private var reduceMotion

    var body: some View {
        TimelineView(.animation(minimumInterval: 1 / 20, paused: reduceMotion)) { timeline in
            let t = timeline.date.timeIntervalSinceReferenceDate
            Canvas { context, size in
                let rows = 7, cols = 3
                for r in 0..<rows {
                    for c in 0..<cols {
                        let word = words[(r * cols + c) % words.count]
                        let drift = (t * 8).truncatingRemainder(dividingBy: size.width / CGFloat(cols))
                        let x = CGFloat(c) * size.width / CGFloat(cols) + (r.isMultiple(of: 2) ? drift : -drift) + 40
                        let y = CGFloat(r) * size.height / CGFloat(rows) + 20
                        context.opacity = 0.09
                        context.draw(Text(word).font(.jakarta(.title3, weight: .heavy)).foregroundColor(color),
                                     at: CGPoint(x: x, y: y))
                    }
                }
            }
        }
        .allowsHitTesting(false)
    }
}

import SwiftUI
import JECore

/// Ünitenin dersleri, referanstaki senaryo yolu gibi: yukarıdan aşağı kıvrılan geniş, açık gri bir yol
/// (ortasında ince beyaz çizgi), üzerinde sırayla sağa sola yerleşen hap etiketler ve her birinin karşı
/// yanında konusuna uygun büyük bir görsel. Bitirilen kısım mavi; sıradaki dersin yanında "Başla" balonu.
struct LessonPathView: View {
    let unit: CourseUnit
    let onLesson: (Lesson) -> Void
    let onTest: () -> Void

    @Environment(AppModel.self) private var model
    @State private var drawn = false

    private let rowHeight: CGFloat = 92
    private let pillWidth: CGFloat = 168
    /// Referanstaki yolun her satırdaki yatay konumu (0...1): önce sola, sonra sağa kıvrılan uzun bir S.
    private let roadRatios: [CGFloat] = [0.36, 0.3, 0.36, 0.64, 0.68, 0.56]

    private var nextIndex: Int? {
        unit.lessons.firstIndex { !model.state.completedLessons.contains($0.id) }
    }

    var body: some View {
        let count = unit.lessons.count + 1
        let doneCount = unit.lessons.filter { model.state.completedLessons.contains($0.id) }.count
        let emojis = LessonEmoji.sequence(for: unit.lessons.map(\.title))
        GeometryReader { geo in
            let w = geo.size.width
            let points = (0..<count).map { CGPoint(x: w * roadRatios[$0 % roadRatios.count], y: rowHeight * (CGFloat($0) + 0.5)) }
            let progress = CGFloat(doneCount) / CGFloat(max(count - 1, 1))
            ZStack(alignment: .topLeading) {
                // Yol: iki ince gri kenar çizgisi ve aralarında çok açık bir şerit.
                // Uçlar düz kesilir; yuvarlak uç yolun başında "U" gibi görünüyordu.
                road(points, shift: 0)
                    .stroke(Color(light: 0xE2E7F0, dark: 0x2A3150), style: StrokeStyle(lineWidth: 32, lineCap: .butt, lineJoin: .round))
                road(points, shift: 0)
                    .stroke(Theme.surface, style: StrokeStyle(lineWidth: 22, lineCap: .butt, lineJoin: .round))
                // Bitirilen kısım: yolun sol kenarı maviye döner.
                road(points, shift: -13.5)
                    .trim(from: 0, to: drawn ? progress : 0)
                    .stroke(Theme.accent, style: StrokeStyle(lineWidth: 5, lineCap: .round, lineJoin: .round))
                    .animation(.easeInOut(duration: 1.2).delay(0.25), value: drawn)

                ForEach(0..<count, id: \.self) { i in
                    let roadX = points[i].x
                    let y = points[i].y
                    let isTest = i == unit.lessons.count
                    let lesson = isTest ? nil : unit.lessons[i]
                    let done = lesson.map { model.state.completedLessons.contains($0.id) } ?? model.isUnitPassed(unit)
                    let current = isTest ? (nextIndex == nil && !done) : i == nextIndex
                    // Yol solda kalıyorsa hap sağa, sağda kalıyorsa sola uzanır; bir ucu yolun üstündedir.
                    let extendsRight = roadX < w / 2
                    let anchored = extendsRight ? roadX - 10 + pillWidth / 2 : roadX + 10 - pillWidth / 2
                    // Sıradaki hapın yanındaki "Başla" balonu (~80pt) ekrandan taşmasın.
                    let pillCenter = !current ? anchored
                        : (extendsRight ? min(anchored, w - 8 - 82 - pillWidth / 2) : max(anchored, 8 + 82 + pillWidth / 2))
                    PathPill(title: lesson?.title ?? "Ünite testi",
                             state: done ? .done : (current ? .current : .locked),
                             width: pillWidth,
                             extendsRight: extendsRight) {
                        if let lesson { onLesson(lesson) } else { onTest() }
                    }
                    .position(x: pillCenter, y: y)
                    .staggeredAppear(i, delay: 0.08)
                    // Görsel yolun öbür yanında, yola yakın; referanstaki gibi büyük.
                    Text(isTest ? "🏆" : emojis[i])
                        .font(.system(size: 66))
                        .shadow(color: Theme.ink.opacity(0.22), radius: 7, x: 2, y: 6)
                        .position(x: min(max(extendsRight ? roadX - 62 : roadX + 62, 40), w - 40), y: y)
                        .staggeredAppear(i, delay: 0.08)
                }
            }
        }
        .frame(height: rowHeight * CGFloat(count) + 30)
        .onAppear { drawn = true }
    }

    /// Satır noktalarından geçen yumuşak S eğrisi; başta ve sonda biraz taşar. `shift` yolun kenarını çizmek için.
    private func road(_ points: [CGPoint], shift: CGFloat) -> Path {
        var path = Path()
        let pts = points.map { CGPoint(x: $0.x + shift, y: $0.y) }
        guard let first = pts.first, let last = pts.last else { return path }
        path.move(to: CGPoint(x: first.x + 12, y: first.y - rowHeight * 0.5))
        path.addQuadCurve(to: first, control: CGPoint(x: first.x + 6, y: first.y - rowHeight * 0.2))
        for i in 1..<pts.count {
            let a = pts[i - 1], b = pts[i]
            let midY = (a.y + b.y) / 2
            path.addCurve(to: b, control1: CGPoint(x: a.x, y: midY), control2: CGPoint(x: b.x, y: midY))
        }
        path.addQuadCurve(to: CGPoint(x: last.x - 30, y: last.y + rowHeight * 0.7), control: CGPoint(x: last.x - 6, y: last.y + rowHeight * 0.4))
        return path
    }
}

/// Ders adındaki anahtar sözcüklere göre konu görseli; bulunamazsa 📘.
enum LessonEmoji {
    private static let map: [(String, String)] = [
        ("selam", "👋"), ("merhaba", "👋"), ("ben, sen", "🧑‍🤝‍🧑"), ("nereli", "🌍"), ("ülke", "🌍"), ("yaş", "🎂"),
        ("evet", "✅"), ("aile", "👨‍👩‍👧"), ("kardeş", "👫"), ("nasıl biri", "🧑‍🎨"), ("benim, senin", "🎒"),
        ("çoğul", "🧺"), ("bu ve şu", "👉"), ("bunlar", "👉"), ("renk", "🎨"), ("ev", "🏠"), ("oda", "🛏️"),
        ("içinde", "📦"), ("yanında", "🪑"), ("var mı", "🔎"), ("sayı", "🔢"), ("saat", "⏰"), ("gün", "📅"),
        ("rutin", "⏰"), ("yemek", "🍽️"), ("kafe", "☕"), ("kahve", "☕"), ("restoran", "🍽️"), ("sipariş", "🧾"),
        ("alışveriş", "🛒"), ("market", "🛒"), ("fiyat", "🏷️"), ("giysi", "👕"), ("şehir", "🏙️"), ("yol", "🗺️"),
        ("tarif", "🗺️"), ("ulaşım", "🚌"), ("taksi", "🚕"), ("otel", "🏨"), ("havaalanı", "✈️"), ("seyahat", "✈️"),
        ("tatil", "🏖️"), ("hava", "⛅"), ("iş", "💼"), ("meslek", "💼"), ("okul", "🏫"), ("spor", "⚽"),
        ("müzik", "🎵"), ("film", "🎬"), ("sağlık", "🩺"), ("doktor", "🩺"), ("telefon", "📱"), ("hafta sonu", "🎉"),
        ("yetenek", "🎸"), ("geçmiş", "🕰️"), ("gelecek", "🔮"), ("plan", "🗓️"), ("hikâye", "📖"), ("hikaye", "📖"),
    ]

    private static let fallbacks = ["📘", "✏️", "💬", "🎯", "🧩", "🌟"]

    static func `for`(_ title: String) -> String {
        let lower = title.lowercased(with: Locale(identifier: "tr"))
        return map.first { lower.contains($0.0) }?.1 ?? "📘"
    }

    /// Bir ünitenin dersleri için görseller; aynı görsel art arda iki kez gelmez.
    static func sequence(for titles: [String]) -> [String] {
        var result: [String] = []
        for (i, title) in titles.enumerated() {
            var emoji = self.for(title)
            if emoji == result.last || (emoji == "📘" && result.contains(emoji)) {
                emoji = fallbacks.first { $0 != result.last && !result.contains($0) } ?? fallbacks[i % fallbacks.count]
            }
            result.append(emoji)
        }
        return result
    }
}

/// Yol üzerindeki hap: bitti = mavi, yolun üstündeki ucunda sarı yıldız; sıradaki = mavi ve yanında "Başla" balonu;
/// kilitli = açık gri, gri yazı ve yol tarafında kilit.
struct PathPill: View {
    enum State { case done, current, locked }
    let title: String
    let state: State
    var width: CGFloat = 168
    /// Hap yoldan sağa mı uzanıyor (yol ucu solda) yoksa sola mı.
    var extendsRight = true
    let action: () -> Void

    @SwiftUI.State private var bob = false
    @SwiftUI.State private var shakes = 0
    @Environment(\.accessibilityReduceMotion) private var reduceMotion

    var body: some View {
        Button {
            // Kilitli ders açılmaz: hafifçe sallanır ve titreşir.
            if state == .locked {
                shakes += 1
                Haptics.error()
            } else {
                action()
            }
        } label: {
            HStack(spacing: 8) {
                if state == .locked && extendsRight { lock }
                Text(title)
                    .lineLimit(1)
                    .minimumScaleFactor(0.7)
                if state == .locked && !extendsRight { lock }
            }
            .font(.jakarta(.callout, weight: .medium))
            .foregroundStyle(state == .locked ? Color(light: 0x9AA3B2, dark: 0x6C7690) : .white)
            .padding(.leading, extendsRight ? 26 : 14)
            .padding(.trailing, extendsRight ? 14 : 26)
            .frame(width: width, height: 46)
            .background {
                RoundedRectangle(cornerRadius: 16, style: .continuous)
                    .fill(state == .locked ? Color(light: 0xE2E6EE, dark: 0x262D45) : Theme.accent)
            }
            .background {
                RoundedRectangle(cornerRadius: 16, style: .continuous)
                    .fill(state == .locked ? Color.clear : Theme.accentDeep)
                    .offset(x: 1, y: 2.5)
            }
            .overlay(alignment: extendsRight ? .leading : .trailing) {
                if state != .locked {
                    // Yıldız hapın yola değen ucunda.
                    Image(systemName: "star.fill")
                        .font(.system(size: 17))
                        .foregroundStyle(Theme.warning)
                        .shadow(color: Theme.warning.opacity(0.5), radius: 2)
                        .offset(x: extendsRight ? 4 : -4)
                        .opacity(state == .done ? 1 : 0.95)
                }
            }
        }
        .buttonStyle(PressableCardStyle())
        .shake(shakes)
        .overlay(alignment: extendsRight ? .trailing : .leading) {
            if state == .current {
                StartBubble(pointsRight: !extendsRight)
                    .fixedSize()
                    .offset(x: extendsRight ? 80 : -80)
                    .scaleEffect(bob ? 1.04 : 0.98)
                    .allowsHitTesting(false)
            }
        }
        .onAppear {
            guard state == .current, !reduceMotion else { return }
            withAnimation(.easeInOut(duration: 0.9).repeatForever()) { bob = true }
        }
        .accessibilityLabel("\(title), \(state == .done ? "tamamlandı" : state == .current ? "sıradaki" : "kilitli")")
    }

    private var lock: some View {
        Image(systemName: "lock.fill").font(.system(size: 13, weight: .semibold))
    }
}

/// Sıradaki dersin yanındaki beyaz dikdörtgen "Başla" balonu; hapa doğru küçük bir ucu var.
struct StartBubble: View {
    var pointsRight = false

    var body: some View {
        Text("Başla")
            .font(.jakarta(.title3, weight: .bold))
            .foregroundStyle(Theme.accent)
            .padding(.horizontal, 13)
            .padding(.vertical, 9)
            .background(Theme.surface, in: RoundedRectangle(cornerRadius: 4, style: .continuous))
            .overlay(RoundedRectangle(cornerRadius: 4, style: .continuous).stroke(Color(light: 0xC9D3E3, dark: 0x3A4361), lineWidth: 1))
            .overlay(alignment: pointsRight ? .trailing : .leading) {
                Image(systemName: pointsRight ? "arrowtriangle.right.fill" : "arrowtriangle.left.fill")
                    .font(.system(size: 12))
                    .foregroundStyle(Theme.surface)
                    .offset(x: pointsRight ? 9 : -9)
            }
            .shadow(color: Theme.ink.opacity(0.1), radius: 6, y: 3)
    }
}

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

    // Ölçüler referans görselden piksel piksel alındı (1pt ≈ 1.48px).
    private let rowHeight: CGFloat = 88
    private let roadTop: CGFloat = 23
    private let edgeOffset: CGFloat = 7.75
    private let pillHeight: CGFloat = 42
    private let pillWidth: CGFloat = 167
    private let bubbleWidth: CGFloat = 66

    private var nextIndex: Int? {
        unit.lessons.firstIndex { !model.state.completedLessons.contains($0.id) }
    }

    /// Yolun ortasının yatay konumu (genişliğin oranı), y'nin sürekli bir sinüsü:
    /// önce sola (en sol ≈0.32, 1,5. satır), sonra sağa (en sağ ≈0.61, 4. satır) kıvrılan tek parça bir S.
    private func roadRatio(_ y: CGFloat) -> CGFloat {
        0.468 - 0.144 * CGFloat(cos(2 * Double.pi * (Double(y) / Double(rowHeight) - 1.6) / 5))
    }

    var body: some View {
        let count = unit.lessons.count + 1
        let doneCount = unit.lessons.filter { model.state.completedLessons.contains($0.id) }.count
        let arts = LessonArt.sequence(for: unit.lessons.map(\.title))
        let total = rowHeight * CGFloat(count) + 40
        GeometryReader { geo in
            let w = geo.size.width
            let center = samples(width: w, from: roadTop, to: total)
            // Mavi çizgi yolun başından sıradaki dersin satırına kadar.
            let currentY = rowHeight * (CGFloat(min(doneCount, count - 1)) + 0.5)
            ZStack(alignment: .topLeading) {
                offsetLine(center, by: edgeOffset)
                    .stroke(Color(light: 0xD8DFEA, dark: 0x2A3150), style: StrokeStyle(lineWidth: 6.5, lineCap: .butt, lineJoin: .round))
                offsetLine(center, by: -edgeOffset)
                    .stroke(Color(light: 0xD8DFEA, dark: 0x2A3150), style: StrokeStyle(lineWidth: 6.5, lineCap: .butt, lineJoin: .round))
                offsetLine(center.filter { $0.y <= currentY }, by: 2.5)
                    .trim(from: 0, to: drawn ? 1 : 0)
                    .stroke(Theme.accent, style: StrokeStyle(lineWidth: 4, lineCap: .round, lineJoin: .round))
                    .animation(.easeInOut(duration: 1.1).delay(0.25), value: drawn)

                ForEach(0..<count, id: \.self) { i in
                    let y = rowHeight * (CGFloat(i) + 0.5)
                    let roadX = w * roadRatio(y)
                    let isTest = i == unit.lessons.count
                    let lesson = isTest ? nil : unit.lessons[i]
                    let done = lesson.map { model.state.completedLessons.contains($0.id) } ?? model.isUnitPassed(unit)
                    let current = isTest ? (nextIndex == nil && !done) : i == nextIndex
                    // Yol ekranın solundaysa hap sağa, sağındaysa sola uzanır; yola değen ucu yolun ortasında.
                    let extendsRight = roadRatio(y) < 0.47
                    // Sıradaki hapın balonu da ekrana sığsın diye genişlik gerekirse kısalır.
                    let room = extendsRight ? (w - 6 - (current ? bubbleWidth + 8 : 0)) - (roadX - 4)
                                            : (roadX + 4) - (6 + (current ? bubbleWidth + 8 : 0))
                    let width = max(140, min(pillWidth, room))
                    let pillCenter = extendsRight ? roadX - 4 + width / 2 : roadX + 4 - width / 2
                    PathPill(title: lesson?.title ?? "Ünite testi",
                             state: done ? .done : (current ? .current : .locked),
                             width: width, height: pillHeight,
                             extendsRight: extendsRight) {
                        if let lesson { onLesson(lesson) } else { onTest() }
                    }
                    .position(x: pillCenter, y: y)
                    .staggeredAppear(i, delay: 0.08)
                    // Yıldız yolun ortasında, hapın yola değen ucunun üstünde.
                    if done || current {
                        Image(systemName: "star.fill")
                            .font(.system(size: 20))
                            .foregroundStyle(Color(light: 0xF5B400, dark: 0xFBBF24))
                            .shadow(color: Color.orange.opacity(0.35), radius: 1.5, y: 1)
                            .position(x: roadX, y: y)
                            .staggeredAppear(i, delay: 0.08)
                    }
                    // Referanstaki gibi 3B görsel (Microsoft Fluent 3D Emoji, MIT lisanslı), yolun öbür yanında.
                    Image("lesson-\(isTest ? "trophy" : arts[i])")
                        .resizable()
                        .scaledToFit()
                        .frame(width: 76, height: 76)
                        .position(x: min(max(extendsRight ? roadX - 56 : roadX + 56, 40), w - 40), y: y - 4)
                        .staggeredAppear(i, delay: 0.08)
                }
            }
        }
        .frame(height: total)
        .onAppear { drawn = true }
    }

    /// Yolun orta çizgisi: 2pt aralıkla örneklenmiş noktalar.
    private func samples(width: CGFloat, from top: CGFloat, to bottom: CGFloat) -> [CGPoint] {
        stride(from: top, through: bottom, by: 2).map { CGPoint(x: width * roadRatio($0), y: $0) }
    }

    /// Orta çizgiye her noktada dik (normal) yönde `distance` kadar kaydırılmış paralel çizgi.
    /// Pozitif değer yolun soluna (akış yönüne göre) kaydırır.
    private func offsetLine(_ points: [CGPoint], by distance: CGFloat) -> Path {
        var path = Path()
        guard points.count > 1 else { return path }
        for i in points.indices {
            let a = points[max(i - 1, 0)], b = points[min(i + 1, points.count - 1)]
            let tx = b.x - a.x, ty = b.y - a.y
            let length = max(hypot(tx, ty), 0.001)
            // Aşağı akan eğride (-ty, tx) sola bakar.
            let p = CGPoint(x: points[i].x + distance * (-ty / length), y: points[i].y + distance * (tx / length))
            if i == 0 { path.move(to: p) } else { path.addLine(to: p) }
        }
        return path
    }
}

/// Ders adındaki sözcüklere göre konu görseli (Assets → Lessons içindeki `lesson-*` görselleri).
/// Sözcük başına bakılır ("ev" "seviye"nin içinde eşleşmesin); bulunamazsa sırayla yedek görseller.
enum LessonArt {
    private static let map: [(String, String)] = [
        ("selam", "wave"), ("merhaba", "wave"), ("ben, sen", "pointright"), ("nereli", "globe"), ("ülke", "globe"),
        ("yaş", "cake"), ("evet", "check"), ("aile", "couple"), ("kardeş", "couple"), ("nasıl biri", "palette"),
        ("benim, senin", "backpack"), ("çoğul", "basket"), ("bu ve şu", "pointright"), ("bunlar", "pointright"),
        ("renk", "palette"), ("ev", "house"), ("oda", "bed"), ("içinde", "package"), ("yanında", "chair"),
        ("var mı", "search"), ("sayı", "numbers"), ("saat", "clock"), ("gün", "calendar"), ("rutin", "clock"),
        ("yemek", "food"), ("kafe", "coffee"), ("kahve", "coffee"), ("restoran", "food"), ("sipariş", "receipt"),
        ("alışveriş", "cart"), ("market", "cart"), ("fiyat", "label"), ("giysi", "tshirt"), ("kıyafet", "tshirt"),
        ("şehir", "city"), ("yol", "map"), ("tarif", "map"), ("ulaşım", "bus"), ("otobüs", "bus"), ("taksi", "taxi"),
        ("otel", "hotel"), ("havaalanı", "airplane"), ("seyahat", "airplane"), ("uçak", "airplane"), ("tatil", "beach"),
        ("hava", "weather"), ("iş", "briefcase"), ("meslek", "briefcase"), ("okul", "school"), ("spor", "ball"),
        ("müzik", "music"), ("film", "film"), ("sağlık", "health"), ("doktor", "health"), ("telefon", "phone"),
        ("hafta sonu", "party"), ("parti", "party"), ("yetenek", "guitar"), ("geçmiş", "hourglass"),
        ("gelecek", "crystal"), ("plan", "spiral"), ("hikâye", "book"), ("hikaye", "book"), ("kitap", "books"),
    ]
    private static let fallbacks = ["books", "pencil", "chat", "target", "puzzle", "bulb", "memo", "headphone", "star", "pushpin"]

    static func key(for title: String) -> String? {
        let lower = title.lowercased(with: Locale(identifier: "tr"))
        let words = lower.split { !$0.isLetter }.map(String.init)
        return map.first { entry in
            entry.0.contains(" ") || entry.0.contains(",") ? lower.contains(entry.0) : words.contains { $0.hasPrefix(entry.0) }
        }?.1
    }

    /// Bir ünitenin dersleri için görseller; aynı görsel art arda gelmez, eşleşmeyenler yedeklerden alınır.
    static func sequence(for titles: [String]) -> [String] {
        var result: [String] = []
        var spare = fallbacks.makeIterator()
        for title in titles {
            var art = key(for: title)
            if art == nil || art == result.last {
                art = nil
                while let next = spare.next() {
                    if !result.contains(next) { art = next; break }
                }
            }
            result.append(art ?? "books")
        }
        return result
    }
}

/// Yol üzerindeki hap: bitti/sıradaki = mavi (alt kenarı koyu), sıradakinin dış ucunda "Başla" balonu;
/// kilitli = açık gri, gri yazı ve yol tarafında kilit. Kilitliye dokununca sallanır.
struct PathPill: View {
    enum State { case done, current, locked }
    let title: String
    let state: State
    var width: CGFloat = 167
    var height: CGFloat = 42
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
            .font(.custom(Theme.fontFamily, size: 17, relativeTo: .body).weight(.medium))
            .foregroundStyle(state == .locked ? Color(light: 0xA0A8B5, dark: 0x6C7690) : .white)
            .padding(.leading, extendsRight ? 22 : 12)
            .padding(.trailing, extendsRight ? 12 : 22)
            .frame(width: width, height: height)
            .background {
                RoundedRectangle(cornerRadius: 11, style: .continuous)
                    .fill(state == .locked ? Color(light: 0xDCE1E9, dark: 0x262D45) : Theme.accent)
            }
            .background {
                RoundedRectangle(cornerRadius: 11, style: .continuous)
                    .fill(state == .locked ? Color.clear : Theme.accentDeep)
                    .offset(y: 3)
            }
        }
        .buttonStyle(PressableCardStyle())
        .shake(shakes)
        .overlay(alignment: extendsRight ? .trailing : .leading) {
            if state == .current {
                StartBubble(pointsRight: !extendsRight)
                    .offset(x: extendsRight ? 66 + 8 : -(66 + 8))
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
        Image(systemName: "lock.fill").font(.system(size: 15, weight: .semibold))
    }
}

/// Sıradaki dersin yanındaki beyaz dikdörtgen "Başla" balonu (66x40); hapa doğru küçük bir ucu var.
struct StartBubble: View {
    var pointsRight = false

    var body: some View {
        Text("Başla")
            .font(.custom(Theme.fontFamily, size: 22, relativeTo: .title3).weight(.semibold))
            .foregroundStyle(Theme.accent)
            .lineLimit(1)
            .minimumScaleFactor(0.7)
            .frame(width: 66, height: 40)
            .background(Theme.surface, in: RoundedRectangle(cornerRadius: 3, style: .continuous))
            .overlay(RoundedRectangle(cornerRadius: 3, style: .continuous).stroke(Color(light: 0xC9D3E3, dark: 0x3A4361), lineWidth: 1))
            .overlay(alignment: pointsRight ? .trailing : .leading) {
                Image(systemName: pointsRight ? "arrowtriangle.right.fill" : "arrowtriangle.left.fill")
                    .font(.system(size: 11))
                    .foregroundStyle(Theme.surface)
                    .offset(x: pointsRight ? 8 : -8)
            }
    }
}

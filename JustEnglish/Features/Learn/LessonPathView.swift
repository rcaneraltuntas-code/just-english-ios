import SwiftUI
import JECore

/// Ünitenin dersleri, referanstaki senaryo yolu gibi: yukarıdan aşağı kıvrılan, iki açık gri kenar çizgili bir yol;
/// yolun altından sırayla sağa sola çıkan hap etiketler ve her birinin karşı yanında konusuna uygun büyük bir emoji.
/// Bitirilen kısım mavi; sıradaki dersin yanında "Başla" balonu.
struct LessonPathView: View {
    let unit: CourseUnit
    let onLesson: (Lesson) -> Void
    let onTest: () -> Void

    @Environment(AppModel.self) private var model
    @State private var drawn = false

    // Ölçüler referans görselden piksel piksel alındı (1pt ≈ 1.48px).
    private let rowHeight: CGFloat = 96
    /// Yol ilk satırın üstünden başlar: ünite kartının (yolun 13–87pt yukarısında) altında kalır, başlangıcı görünmez.
    private let roadTop: CGFloat = -70
    /// Yol sayfanın sonundan da bu kadar aşağı uzanır; en alta kaydırınca sekme çubuğunun ve ekranın altına girer.
    private let roadOverrun: CGFloat = 800
    private let edgeOffset: CGFloat = 9.5
    /// Son dersten sonra yolun aşağı doğru devam ettiği boşluk (referanstaki gibi yol sayfanın sonuna kadar iner).
    private let tail: CGFloat = 140
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

    /// Bir satırın yerleşimi: hap, yıldız ve emoji aynı hesaptan çizilir (katmanlar ayrı olduğu için).
    private struct Row: Identifiable {
        let id: Int
        let y: CGFloat
        let roadX: CGFloat
        let title: String
        let lesson: Lesson?
        let state: PathPill.State
        let extendsRight: Bool
        let width: CGFloat
        let twoLines: Bool
        let emoji: String
        var pillCenter: CGFloat { extendsRight ? roadX - underRoad + width / 2 : roadX + underRoad - width / 2 }
    }

    /// Hapın yola bakan ucu yolun ortasını bu kadar geçip yolun altında kalır; yuvarlak köşesi görünmez.
    private static let underRoad: CGFloat = 14
    private var underRoad: CGFloat { Self.underRoad }

    private func rows(width w: CGFloat) -> [Row] {
        let emojis = LessonEmoji.sequence(for: unit)
        return (0...unit.lessons.count).map { i in
            let y = rowHeight * (CGFloat(i) + 0.5)
            let roadX = w * roadRatio(y)
            let isTest = i == unit.lessons.count
            let lesson = isTest ? nil : unit.lessons[i]
            let done = lesson.map { model.state.completedLessons.contains($0.id) } ?? model.isUnitPassed(unit)
            let current = isTest ? (nextIndex == nil && !done) : i == nextIndex
            // Yol ekranın solundaysa hap sağa, sağındaysa sola uzanır; yola bakan ucu yolun altına girer.
            let extendsRight = roadRatio(y) < 0.47
            // Sıradaki hapın balonu da ekrana sığsın diye genişlik gerekirse kısalır.
            let room = extendsRight ? (w - 6 - (current ? bubbleWidth + 8 : 0)) - (roadX - underRoad)
                                    : (roadX + underRoad) - (6 + (current ? bubbleWidth + 8 : 0))
            let title = lesson?.title ?? "Ünite testi"
            let locked = !done && !current
            // Hap başlığı tek satıra sığacak kadar uzar (en fazla yer kadar); yine sığmazsa 15pt iki satır olur.
            let needed = Self.textWidth(title, size: 17) + PathPill.roadSidePadding + 12 + (locked ? 23 : 0) + 4
            let width = max(150, min(max(pillWidth, needed), room))
            return Row(id: i, y: y, roadX: roadX, title: title, lesson: lesson,
                       state: done ? .done : (current ? .current : .locked),
                       extendsRight: extendsRight, width: width, twoLines: needed > width,
                       emoji: isTest ? "🏆" : emojis[i])
        }
    }

    var body: some View {
        let doneCount = unit.lessons.filter { model.state.completedLessons.contains($0.id) }.count
        let total = rowHeight * CGFloat(unit.lessons.count + 1) + tail
        GeometryReader { geo in
            let w = geo.size.width
            let rows = rows(width: w)
            let center = samples(width: w, from: roadTop, to: total + roadOverrun)
            // Mavi çizgi yolun başından sıradaki dersin satırına kadar.
            let currentY = rowHeight * (CGFloat(min(doneCount, unit.lessons.count)) + 0.5)
            // Katmanlar (referanstaki gibi): önce haplar, üstüne yol (beyaz dolgu hapların ucunu örter, sonra gri
            // kenar çizgileri), mavi ilerleme çizgisi, en üstte yıldızlar; emojiler yolun öbür yanında.
            ZStack(alignment: .topLeading) {
                // Haplar yolun orta çizgisinde kesilir: kıvrımlarda bile ucu yolun altından çıkıyormuş gibi görünür.
                // Sağa ve sola uzananlar ayrı katmanlarda, her biri yolun kendi tarafıyla maskelenir.
                ForEach([true, false], id: \.self) { right in
                    ZStack(alignment: .topLeading) {
                        ForEach(rows.filter { $0.extendsRight == right }) { row in
                            PathPill(title: row.title, state: row.state,
                                     width: row.width, height: row.twoLines ? 56 : pillHeight, twoLines: row.twoLines,
                                     extendsRight: row.extendsRight) {
                                if let lesson = row.lesson { onLesson(lesson) } else { onTest() }
                            }
                            .position(x: row.pillCenter, y: row.y)
                            .staggeredAppear(row.id, delay: 0.08)
                        }
                    }
                    .frame(width: w, height: total)
                    .mask { side(of: center, right: right, width: w, height: total) }
                }

                Group {
                    linePath(center)
                        .stroke(Theme.surface, style: StrokeStyle(lineWidth: edgeOffset * 2, lineCap: .butt, lineJoin: .round))
                    offsetLine(center, by: edgeOffset)
                        .stroke(Color(light: 0xE2E7EF, dark: 0x2A3150), style: StrokeStyle(lineWidth: 7, lineCap: .butt, lineJoin: .round))
                    offsetLine(center, by: -edgeOffset)
                        .stroke(Color(light: 0xE2E7EF, dark: 0x2A3150), style: StrokeStyle(lineWidth: 7, lineCap: .butt, lineJoin: .round))
                    // Mavi çizgi sol kenar çizgisinin hemen içinde, ona yaslanarak akar.
                    offsetLine(center.filter { $0.y <= currentY }, by: edgeOffset - 5.5)
                        .trim(from: 0, to: drawn ? 1 : 0)
                        .stroke(Theme.accent, style: StrokeStyle(lineWidth: 4, lineCap: .round, lineJoin: .round))
                        .animation(.easeInOut(duration: 1.1).delay(0.25), value: drawn)
                }
                .allowsHitTesting(false)

                ForEach(rows) { row in
                    // Yıldız yolun ortasında, hapın yolun altına giren ucunun üstünde.
                    if row.state != .locked {
                        Image(systemName: "star.fill")
                            .font(.system(size: 20))
                            .foregroundStyle(Color(light: 0xF5B400, dark: 0xFBBF24))
                            .shadow(color: Color.orange.opacity(0.35), radius: 1.5, y: 1)
                            .position(x: row.roadX, y: row.y)
                            .staggeredAppear(row.id, delay: 0.08)
                            .allowsHitTesting(false)
                    }
                    Text(row.emoji)
                        .font(.system(size: 68))
                        .shadow(color: Theme.ink.opacity(0.12), radius: 4, x: 0, y: 3)
                        .position(x: min(max(row.extendsRight ? row.roadX - 58 : row.roadX + 58, 40), w - 40), y: row.y - 2)
                        .staggeredAppear(row.id, delay: 0.08)
                        .accessibilityHidden(true)
                }
            }
        }
        .frame(height: total)
        .onAppear { drawn = true }
    }

    /// Hap yazı tipinde (Plus Jakarta Sans orta kalınlık, kullanıcının yazı boyutuna göre) başlığın genişliği.
    static func textWidth(_ text: String, size: CGFloat) -> CGFloat {
        let descriptor = UIFontDescriptor(fontAttributes: [
            .family: Theme.fontFamily,
            .traits: [UIFontDescriptor.TraitKey.weight: UIFont.Weight.medium.rawValue],
        ])
        let font = UIFontMetrics(forTextStyle: .body).scaledFont(for: UIFont(descriptor: descriptor, size: size))
        return ceil((text as NSString).size(withAttributes: [.font: font]).width)
    }

    /// Yolun orta çizgisi: 2pt aralıkla örneklenmiş noktalar.
    private func samples(width: CGFloat, from top: CGFloat, to bottom: CGFloat) -> [CGPoint] {
        stride(from: top, through: bottom, by: 2).map { CGPoint(x: width * roadRatio($0), y: $0) }
    }

    /// Orta çizginin sağında (ya da solunda) kalan alan: hapları yolun ortasında kesmek için.
    private func side(of points: [CGPoint], right: Bool, width: CGFloat, height: CGFloat) -> Path {
        var path = Path()
        guard let first = points.first, let last = points.last else { return path }
        let edge: CGFloat = right ? width + 200 : -200
        path.move(to: CGPoint(x: edge, y: -200))
        path.addLine(to: CGPoint(x: first.x, y: -200))
        // addLines yeni bir alt yol başlatır; çokgen kopmasın diye noktalar tek tek eklenir.
        for point in points { path.addLine(to: point) }
        path.addLine(to: CGPoint(x: last.x, y: height + 200))
        path.addLine(to: CGPoint(x: edge, y: height + 200))
        path.closeSubpath()
        return path
    }

    /// Orta çizgi (yolun beyaz dolgusu için).
    private func linePath(_ points: [CGPoint]) -> Path {
        var path = Path()
        path.addLines(points)
        return path
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

/// Ders adındaki sözcüklere göre konu emojisi (Apple sistem emojisi).
/// Sözcük başına bakılır ("ev" "seviye"nin içinde eşleşmesin); bulunamazsa sırayla yedek emojiler.
enum LessonEmoji {
    private static let map: [(String, String)] = [
        ("selam", "👋"), ("merhaba", "👋"), ("ben, sen", "🪪"), ("nereli", "🌍"), ("ülke", "🌍"), ("yaş", "🎂"),
        ("evet", "💬"), ("aile", "🖼️"), ("kardeş", "🎈"), ("nasıl biri", "🪞"), ("benim, senin", "🎒"),
        ("çoğul", "🧺"), ("bu ve şu", "👉"), ("bunlar", "👉"), ("renk", "🎨"), ("ev", "🏠"), ("oda", "🛏️"),
        ("içinde", "📦"), ("yanında", "🪑"), ("var mı", "🔎"), ("sayı", "🔢"), ("saat", "⏰"), ("gün", "📅"),
        ("rutin", "⏰"), ("yemek", "🍽️"), ("kafe", "☕"), ("kahve", "☕"), ("restoran", "🍽️"), ("sipariş", "🧾"),
        ("alışveriş", "🛒"), ("market", "🛒"), ("fiyat", "🏷️"), ("giysi", "👕"), ("kıyafet", "👕"), ("şehir", "🏙️"),
        ("yol", "🗺️"), ("tarif", "🗺️"), ("ulaşım", "🚌"), ("otobüs", "🚌"), ("taksi", "🚕"), ("otel", "🏨"),
        ("havaalanı", "✈️"), ("havalimanı", "✈️"), ("seyahat", "✈️"), ("uçak", "✈️"), ("tatil", "🏖️"), ("hava", "⛅"), ("iş", "💼"),
        ("meslek", "💼"), ("okul", "🏫"), ("spor", "⚽"), ("müzik", "🎵"), ("film", "🎬"), ("sağlık", "🩺"),
        ("doktor", "🩺"), ("telefon", "📱"), ("hafta sonu", "🎉"), ("parti", "🎉"), ("yetenek", "🎸"),
        ("geçmiş", "🕰️"), ("gelecek", "🔮"), ("plan", "🗓️"), ("hikâye", "📖"), ("hikaye", "📖"), ("kitap", "📚"),
    ]
    private static let fallbacks = ["📘", "✏️", "💬", "🎯", "🧩", "💡", "📝", "🎧", "🌟", "📌"]

    /// Her ünitenin dersleri için elle seçilmiş emojiler (ders sırasıyla). Dilbilgisi başlıkları sözcükten tahmin
    /// edilemediği için burada; kişi, el ve kutu simgelerinden kaçınılır, nesne gibi duran emojiler seçilir.
    private static let curated: [String: [String]] = [
        "a1-u01": ["👋", "🪪", "🌍", "🎂", "💬"],
        "a1-u02": ["🖼️", "🎒", "🎀", "🎈", "🪞"],
        "a1-u03": ["🍎", "🧺", "👉", "📦", "🎨"],
        "a1-u04": ["🏠", "🔎", "🛋️", "🪑", "🛏️"],
        "a1-u05": ["🪥", "⏰", "🛑", "🤔", "📅"],
        "a1-u06": ["💼", "💻", "💤", "🔧", "🏢"],
        "a1-u07": ["🍪", "🥛", "☕", "🧾", "💳"],
        "a1-u08": ["🏙️", "🚦", "🗺️", "🚪", "🚌"],
        "a1-u09": ["⚽", "🏅", "🎸", "❤️", "💌"],
        "a1-u10": ["👕", "🏷️", "💰", "🛍️", "👟"],
        "a1-u11": ["⛅", "📱", "👀", "📆", "📸"],
        "a1-u12": ["📍", "❓", "✍️", "🎳", "🎉"],
        "a2-u01": ["📜", "📝", "🕰️", "🕵️", "📖"],
        "a2-u02": ["🏖️", "⏳", "🎬", "🌧️", "📷"],
        "a2-u03": ["🐘", "💎", "🏆", "⚖️", "🤔"],
        "a2-u04": ["🎯", "🗓️", "📒", "🌦️", "🗺️"],
        "a2-u05": ["🤕", "🩺", "💡", "🧭", "💊"],
        "a2-u06": ["🗽", "🪂", "✈️", "📍", "🌟"],
        "a2-u07": ["💻", "⚡", "⏱️", "📲", "🛠️"],
        "a2-u08": ["📋", "😌", "⛔", "🚭", "🏫"],
        "a2-u09": ["🔮", "🤨", "🎲", "🚀", "🌍"],
        "a2-u10": ["💌", "😔", "🍿", "✉️", "🎉"],
        "a2-u11": ["✈️", "🏨", "🧳", "🐢", "⭐"],
        "a2-u12": ["😊", "🔗", "🪜", "⚡", "📖"],
        "b1-u01": ["🎭", "🌦️", "💭", "🪞", "🌟"],
        "b1-u02": ["⏳", "🏁", "⏱️", "🧮", "🦋"],
        "b1-u03": ["🛣️", "💰", "🚧", "⚡", "⚖️"],
        "b1-u04": ["🎰", "👟", "☁️", "🤔", "🏝️"],
        "b1-u05": ["⌛", "🧮", "📖", "📰", "👂"],
        "b1-u06": ["🏭", "💡", "⚙️", "🧱", "🚀"],
        "b1-u07": ["💬", "🕰️", "📅", "📣", "📨"],
        "b1-u08": ["👥", "🔗", "📍", "🤯", "🏡"],
        "b1-u09": ["📼", "🧸", "🏕️", "🍂", "🎈"],
        "b1-u10": ["🎨", "📌", "🎯", "❓", "🧠"],
        "b1-u11": ["🔍", "🌫️", "👀", "🕵️", "🗝️"],
        "b1-u12": ["💭", "🌧️", "☔", "⚖️", "✍️"],
        "b2-u01": ["🎭", "⏳", "🎞️", "⚡", "📖"],
        "b2-u02": ["📆", "🔮", "🏁", "💼", "📄"],
        "b2-u03": ["🌠", "🚪", "⭐", "😣", "📝"],
        "b2-u04": ["🔧", "📋", "✂️", "🚗", "✉️"],
        "b2-u05": ["❓", "📩", "📜", "❌", "🎙️"],
        "b2-u06": ["🔗", "💡", "🧩", "🗻", "🧳"],
        "b2-u07": ["🔍", "🤔", "😬", "😅", "🕵️"],
        "b2-u08": ["🍀", "💌", "🏔️", "🧩", "💛"],
        "b2-u09": ["🤔", "🪶", "👔", "🗣️", "📧"],
        "b2-u10": ["🔬", "📌", "🧪", "⚗️", "📊"],
        "b2-u11": ["💰", "😟", "🏦", "📈", "💡"],
        "b2-u12": ["🧱", "🔗", "📝", "⚖️", "🗞️"],
        "c1-u01": ["😲", "✨", "🔒", "🤯", "🎚️"],
        "c1-u02": ["🎯", "🔑", "🎁", "🎤", "📊"],
        "c1-u03": ["⏳", "🪞", "🪄", "💭", "🛤️"],
        "c1-u04": ["✂️", "📎", "🧵", "🎓", "📚"],
        "c1-u05": ["🎲", "📊", "🔍", "🤨", "🔮"],
        "c1-u06": ["👁️", "🌡️", "📉", "🤫", "⚖️"],
        "c1-u07": ["💼", "😊", "🔗", "💪", "🍃"],
        "c1-u08": ["🗣️", "🤔", "💭", "📰", "✍️"],
        "c1-u09": ["🎨", "👔", "💬", "🎭", "✍️"],
        "c1-u10": ["♻️", "✂️", "🗨️", "☕", "📝"],
        "c1-u11": ["🏷️", "🎨", "🌑", "🔧", "🌳"],
        "c1-u12": ["🏛️", "⚔️", "🔍", "🎤", "✍️"],
        "c2-u01": ["🚀", "🌀", "📣", "🗝️", "🎵"],
        "c2-u02": ["🧠", "🎯", "🎭", "🔥", "👓"],
        "c2-u03": ["🏷️", "🧱", "📚", "🧪", "🎓"],
        "c2-u04": ["📢", "🌓", "❓", "🌈", "🎤"],
        "c2-u05": ["👁️", "🎬", "📖", "🪶", "✍️"],
        "c2-u06": ["🗣️", "🇬🇧", "📱", "🧩", "😎"],
        "c2-u07": ["🐜", "🙃", "🃏", "😂", "😄"],
        "c2-u08": ["🔑", "🧩", "🔎", "🎙️", "📝"],
    ]

    /// Ünitenin dersleri için emojiler: elle seçilmiş liste varsa o, yoksa başlıktaki sözcüklerden.
    static func sequence(for unit: CourseUnit) -> [String] {
        if let list = curated[unit.id], list.count == unit.lessons.count { return list }
        return sequence(for: unit.lessons.map(\.title))
    }

    static func emoji(for title: String) -> String? {
        let lower = title.lowercased(with: Locale(identifier: "tr"))
        let words = lower.split { !$0.isLetter }.map(String.init)
        return map.first { entry in
            entry.0.contains(" ") || entry.0.contains(",") ? lower.contains(entry.0) : words.contains { $0.hasPrefix(entry.0) }
        }?.1
    }

    /// Bir ünitenin dersleri için emojiler; aynı emoji art arda gelmez, eşleşmeyenler yedeklerden alınır.
    static func sequence(for titles: [String]) -> [String] {
        var result: [String] = []
        var spare = fallbacks.makeIterator()
        for title in titles {
            var emoji = self.emoji(for: title)
            if emoji == nil || emoji == result.last {
                emoji = nil
                while let next = spare.next() {
                    if !result.contains(next) { emoji = next; break }
                }
            }
            result.append(emoji ?? "📘")
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
    /// Başlık tek satıra sığmıyorsa 15pt, gerektiği kadar satır (hap uzar, yazı kesilmez).
    var twoLines = false
    /// Hap yoldan sağa mı uzanıyor (yol ucu solda) yoksa sola mı.
    var extendsRight = true
    let action: () -> Void
    /// Yola bakan uçtaki iç boşluk: ucun bir kısmı yolun altında kaldığı için geniş.
    static let roadSidePadding: CGFloat = 34

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
                    .lineLimit(twoLines ? nil : 1)
                    .multilineTextAlignment(.center)
                    .fixedSize(horizontal: false, vertical: true)
                if state == .locked && !extendsRight { lock }
            }
            .font(.custom(Theme.fontFamily, size: twoLines ? 15 : 17, relativeTo: .body).weight(.medium))
            .foregroundStyle(state == .locked ? Color(light: 0xA0A8B5, dark: 0x6C7690) : .white)
            .padding(.leading, extendsRight ? Self.roadSidePadding : 12)
            .padding(.trailing, extendsRight ? 12 : Self.roadSidePadding)
            .frame(width: width)
            .frame(minHeight: height)
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

import SwiftUI
import UIKit
import JECore

/// Uygulamanın tüm renk ve yazı tipi kararları burada. Marka rengi Just English kırmızısı (#E21724).
/// Kırmızı yalnızca vurgu içindir (düğmeler, seçili sekme, küçük ayrıntılar); büyük yüzeyler beyaz,
/// lacivert ya da seviye renginde kalır ki ekran tek renge boğulmasın.
enum Theme {
    static let accent = Color("AccentColor")
    /// Marka kırmızısının koyu tonu: degradelerin alt ucu ve 3D düğme kenarları.
    static let accentDeep = Color(light: 0xA50E18, dark: 0xC21F2A)
    /// Kırmızının çok açık tonu: seçili yüzeyler, rozet zeminleri.
    static let accentSoft = Color(light: 0xFDEBEC, dark: 0x3A1518)
    /// Kırmızıyı dengeleyen koyu lacivert: koyu kartlar ve başlık metinleri.
    static let ink = Color(light: 0x1B1B2F, dark: 0xF2F2F7)
    static let inkSurface = Color(light: 0x1B1B2F, dark: 0x22232F)
    static let coral = Color(light: 0xFF6B5B, dark: 0xFF8A7D)
    static let success = Color(light: 0x16A34A, dark: 0x4ADE80)
    /// Yanlış cevap rengi marka kırmızısından ayrışsın diye daha koyu, morumsu bir kırmızı;
    /// her zaman bir simge ve sallanmayla birlikte kullanılır.
    static let danger = Color(light: 0x9B1C31, dark: 0xF0697D)
    static let warning = Color(light: 0xF2A100, dark: 0xFBBF24)
    static let streak = Color(light: 0xFF6A13, dark: 0xFF9248)
    static let background = Color(light: 0xF6F6F9, dark: 0x0E0E11)
    static let surface = Color(light: 0xFFFFFF, dark: 0x1B1B20)
    /// İkincil düğmelerin yüzeyi: açık temada sıcak gri, koyu temada bir ton açık.
    static let surfaceRaised = Color(light: 0xEFEFF4, dark: 0x2A2A30)
    static let hairline = Color(light: 0xE7E7EE, dark: 0x2C2C33)
    static let muted = Color.secondary

    /// Marka degradesi: kahraman kartları ve başlıklar.
    static let brandGradient = LinearGradient(colors: [Color(light: 0xF0333E, dark: 0xF0333E), Color(light: 0xE21724, dark: 0xE21724), accentDeep],
                                              startPoint: .topLeading, endPoint: .bottomTrailing)
    static let warmGradient = LinearGradient(colors: [Color(light: 0xFF8A3D, dark: 0xFF8A3D), Color(light: 0xE21724, dark: 0xE21724)],
                                             startPoint: .topLeading, endPoint: .bottomTrailing)
    static let inkGradient = LinearGradient(colors: [Color(light: 0x2A2D45, dark: 0x2A2D45), Color(light: 0x14152A, dark: 0x101120)],
                                            startPoint: .topLeading, endPoint: .bottomTrailing)
    /// Mor-lacivert degrade: sözlük ve kelime kartları.
    static let violetGradient = LinearGradient(colors: [Color(light: 0x6D4AE0, dark: 0x6D4AE0), Color(light: 0x2B2A6B, dark: 0x22215A)],
                                               startPoint: .topLeading, endPoint: .bottomTrailing)

    static let cornerRadius: CGFloat = 16
    static let fontFamily = "Plus Jakarta Sans"

    static func color(for level: CEFRLevel) -> Color {
        switch level {
        // Çeşitli ama uyumlu bir merdiven: yeşil → camgöbeği → mavi → mor → magenta → lacivert.
        case .a1: Color(light: 0x22A06B, dark: 0x4ADE80)
        case .a2: Color(light: 0x0EA5A4, dark: 0x2DD4BF)
        case .b1: Color(light: 0x2F6FED, dark: 0x6B9BFF)
        case .b2: Color(light: 0x7C5CFF, dark: 0xA594FF)
        case .c1: Color(light: 0xC2338A, dark: 0xF06BB8)
        case .c2: Color(light: 0x1E2A5A, dark: 0x8FA3E8)
        }
    }

    /// UIKit tarafındaki gezinme ve sekme çubuklarının da aynı yazı tipini kullanması için.
    @MainActor static func configureAppearance() {
        // Boyutlar varsayılan (Large) yazı boyutundaki değerlerdir; UIFontMetrics kullanıcının ayarına göre ölçekler.
        func font(_ style: UIFont.TextStyle, size: CGFloat, weight: UIFont.Weight) -> UIFont {
            let descriptor = UIFontDescriptor(fontAttributes: [
                .family: fontFamily,
                .traits: [UIFontDescriptor.TraitKey.weight: weight.rawValue],
            ])
            return UIFontMetrics(forTextStyle: style).scaledFont(for: UIFont(descriptor: descriptor, size: size))
        }
        let nav = UINavigationBar.appearance()
        nav.largeTitleTextAttributes = [.font: font(.largeTitle, size: 34, weight: .bold)]
        nav.titleTextAttributes = [.font: font(.headline, size: 17, weight: .semibold)]
        UITabBarItem.appearance().setTitleTextAttributes([.font: font(.caption2, size: 11, weight: .medium)], for: .normal)
    }
}

extension Font {
    /// Plus Jakarta Sans, Dinamik Yazı boyutlarına uyarlanır.
    static func jakarta(_ style: TextStyle, weight: Weight = .regular) -> Font {
        let size: CGFloat = switch style {
        case .largeTitle: 34
        case .title: 28
        case .title2: 22
        case .title3: 20
        case .headline: 17
        case .subheadline: 15
        case .callout: 16
        case .footnote: 13
        case .caption: 12
        case .caption2: 11
        default: 17
        }
        let defaultWeight: Weight = style == .headline ? .semibold : weight
        return .custom(Theme.fontFamily, size: size, relativeTo: style).weight(weight == .regular ? defaultWeight : weight)
    }
}

extension Color {
    init(light: UInt32, dark: UInt32) {
        self.init(uiColor: UIColor { traits in
            UIColor(hex: traits.userInterfaceStyle == .dark ? dark : light)
        })
    }
}

extension UIColor {
    convenience init(hex: UInt32) {
        self.init(red: CGFloat((hex >> 16) & 0xFF) / 255,
                  green: CGFloat((hex >> 8) & 0xFF) / 255,
                  blue: CGFloat(hex & 0xFF) / 255,
                  alpha: 1)
    }
}

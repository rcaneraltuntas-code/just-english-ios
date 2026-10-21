import SwiftUI
import UIKit
import JECore

/// Uygulamanın tüm renk ve yazı tipi kararları burada.
/// Vurgu rengi tek yerden gelir: `AccentColor` (Assets). Onu değiştirmek düğmeleri, seçili sekmeyi,
/// ilerleme çubuklarını ve seçimleri birlikte değiştirir; degradeler de ondan türetilir.
/// Tasarım dili: yapay zekâ temalı, havadar, açık mavi-lila zemin, cam (liquid glass) yüzeyler.
enum Theme {
    /// Vurgu: referans mavisi (#3D7BF7, koyu temada #6B9BFF).
    static let accent = Color("AccentColor")
    static let accentDeep = accent.blended(with: .black, amount: 0.22)
    static let accentSoft = Color(light: 0xEAF1FF, dark: 0x1A2340)
    /// Just English kırmızısı: yalnızca logo/yazı işareti ve çok küçük ayrıntılar (canlı noktası, bildirim rozeti).
    static let brandRed = Color(light: 0xE21724, dark: 0xFF4A55)
    /// Yapay zekâ öğeleri (JAI, ışıltılar): mavi-mor.
    static let ai = Color(light: 0x5B6CFF, dark: 0x8C98FF)
    static let aiViolet = Color(light: 0x8B5CF6, dark: 0xB197FF)
    /// Başlıklar için koyu lacivert.
    static let ink = Color(light: 0x1A1F36, dark: 0xF2F4FA)
    static let inkSurface = Color(light: 0x1A1F36, dark: 0x22253A)
    static let coral = Color(light: 0xFF6B5B, dark: 0xFF8A7D)
    static let success = Color(light: 0x22A06B, dark: 0x4ADE80)
    static let successSoft = Color(light: 0xE6F6EE, dark: 0x173326)
    /// Yanlış cevap: koyu kırmızı, her zaman simge ve sallanmayla birlikte.
    static let danger = Color(light: 0xD1344B, dark: 0xF0697D)
    static let warning = Color(light: 0xF5B400, dark: 0xFBBF24)
    static let streak = Color(light: 0xFF7A1A, dark: 0xFF9248)
    /// Havadar zemin: üstte açık mavi, altta neredeyse beyaz.
    static let background = Color(light: 0xF5F8FF, dark: 0x0B0D16)
    static let backgroundTop = Color(light: 0xE6EFFF, dark: 0x151B33)
    static let surface = Color(light: 0xFFFFFF, dark: 0x171A26)
    /// İkincil düğmelerin yüzeyi.
    static let surfaceRaised = Color(light: 0xF0F3FA, dark: 0x252A3B)
    static let hairline = Color(light: 0xE3E8F2, dark: 0x2A2F42)
    static let muted = Color.secondary

    /// Vurgudan türetilen degrade: birincil kartlar ve ilerleme.
    static let brandGradient = LinearGradient(colors: [accent.blended(with: .white, amount: 0.15), accent, accentDeep],
                                              startPoint: .topLeading, endPoint: .bottomTrailing)
    /// Yapay zekâ degradesi: JAI kartları ve sohbet.
    static let aiGradient = LinearGradient(colors: [Color(light: 0x6E8BFF, dark: 0x5A73F0), Color(light: 0x8B5CF6, dark: 0x7A4FE0)],
                                           startPoint: .topLeading, endPoint: .bottomTrailing)
    static let warmGradient = LinearGradient(colors: [Color(light: 0xFFB13D, dark: 0xFFB13D), Color(light: 0xFF7A1A, dark: 0xFF7A1A)],
                                             startPoint: .topLeading, endPoint: .bottomTrailing)
    static let inkGradient = LinearGradient(colors: [Color(light: 0x2A3156, dark: 0x2A3156), Color(light: 0x141832, dark: 0x0F1226)],
                                            startPoint: .topLeading, endPoint: .bottomTrailing)
    static let violetGradient = LinearGradient(colors: [Color(light: 0x7A6BFF, dark: 0x6A5BEF), Color(light: 0x3D4BC7, dark: 0x2F3AA0)],
                                               startPoint: .topLeading, endPoint: .bottomTrailing)
    /// Ana sayfa ve sohbet başlığındaki yumuşak bant.
    static let skyGradient = LinearGradient(colors: [Color(light: 0x5B8DF8, dark: 0x2B3F86), Color(light: 0x8FB2FF, dark: 0x22336E), Color(light: 0xF5F8FF, dark: 0x0B0D16)],
                                            startPoint: .top, endPoint: .bottom)

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

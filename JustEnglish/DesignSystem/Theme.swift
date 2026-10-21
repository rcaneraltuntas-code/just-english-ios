import SwiftUI
import UIKit
import JECore

/// Uygulamanın tüm renk ve yazı tipi kararları burada. Marka renkleri netleşince yalnızca bu dosya değişir.
enum Theme {
    static let accent = Color("AccentColor")
    static let success = Color(light: 0x1F9D55, dark: 0x4ADE80)
    static let danger = Color(light: 0xD93636, dark: 0xF87171)
    static let warning = Color(light: 0xE08A00, dark: 0xFBBF24)
    static let streak = Color(light: 0xF2620F, dark: 0xFB923C)
    static let background = Color(uiColor: .systemGroupedBackground)
    static let surface = Color(uiColor: .secondarySystemGroupedBackground)
    /// İkincil düğmelerin yüzeyi: açık temada hafif gri, koyu temada bir ton açık.
    static let surfaceRaised = Color(light: 0xEEF1F8, dark: 0x2C2C30)
    static let muted = Color.secondary

    static let cornerRadius: CGFloat = 16
    static let fontFamily = "Plus Jakarta Sans"

    static func color(for level: CEFRLevel) -> Color {
        switch level {
        case .a1: Color(light: 0x16A34A, dark: 0x4ADE80)
        case .a2: Color(light: 0x0D9488, dark: 0x2DD4BF)
        case .b1: Color(light: 0x2563EB, dark: 0x60A5FA)
        case .b2: Color(light: 0x7C3AED, dark: 0xA78BFA)
        case .c1: Color(light: 0xC026D3, dark: 0xE879F9)
        case .c2: Color(light: 0xDC2626, dark: 0xF87171)
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

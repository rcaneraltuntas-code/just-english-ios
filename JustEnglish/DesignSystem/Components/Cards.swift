import SwiftUI
import JECore

// Sekme sayfalarının ortak parçaları: kahraman başlık, istatistik kutusu, filtre çipi, bölüm başlığı.

/// Sekmelerin üstündeki büyük, degradeli başlık kartı. Arka planda kayan İngilizce kelimeler Just English dokusudur.
struct HeroHeader<Trailing: View, Bottom: View>: View {
    let title: String
    let subtitle: String
    var gradient: LinearGradient = Theme.brandGradient
    var glow: Color = Theme.accent
    @ViewBuilder var trailing: () -> Trailing
    @ViewBuilder var bottom: () -> Bottom

    var body: some View {
        VStack(alignment: .leading, spacing: 14) {
            HStack(alignment: .top, spacing: 12) {
                VStack(alignment: .leading, spacing: 6) {
                    Text(title)
                        .font(.jakarta(.largeTitle, weight: .heavy))
                        .foregroundStyle(.white)
                    Text(subtitle)
                        .font(.jakarta(.subheadline, weight: .medium))
                        .foregroundStyle(.white.opacity(0.85))
                        .fixedSize(horizontal: false, vertical: true)
                }
                Spacer(minLength: 0)
                trailing()
            }
            bottom()
        }
        .padding(20)
        .frame(maxWidth: .infinity, alignment: .leading)
        .background {
            ZStack {
                gradient
                WordPattern()
                Circle().fill(.white.opacity(0.08)).frame(width: 220).offset(x: 140, y: -70)
            }
            .clipShape(RoundedRectangle(cornerRadius: 28, style: .continuous))
        }
        .shadow(color: glow.opacity(0.3), radius: 18, y: 10)
    }
}

extension HeroHeader where Bottom == EmptyView {
    init(title: String, subtitle: String, gradient: LinearGradient = Theme.brandGradient, glow: Color = Theme.accent,
         @ViewBuilder trailing: @escaping () -> Trailing) {
        self.init(title: title, subtitle: subtitle, gradient: gradient, glow: glow, trailing: trailing, bottom: { EmptyView() })
    }
}

/// Simge, açılışta sayarak yükselen değer ve etiketten oluşan küçük kutu.
struct StatTile: View {
    let icon: String
    let color: Color
    let value: Int
    let label: String
    var index = 0

    var body: some View {
        VStack(alignment: .leading, spacing: 8) {
            Image(systemName: icon)
                .font(.system(size: 17, weight: .bold))
                .foregroundStyle(.white)
                .frame(width: 34, height: 34)
                .background(color.gradient, in: RoundedRectangle(cornerRadius: 10, style: .continuous))
            CountUpNumber(target: value, font: .jakarta(.title2, weight: .heavy), delay: 0.15 + Double(index) * 0.05)
                .foregroundStyle(Theme.ink)
            Text(label)
                .font(.jakarta(.caption, weight: .semibold))
                .foregroundStyle(.secondary)
                .lineLimit(1)
                .minimumScaleFactor(0.8)
        }
        .frame(maxWidth: .infinity, alignment: .leading)
        .padding(14)
        .background(Theme.surface, in: RoundedRectangle(cornerRadius: 18, style: .continuous))
        .overlay(RoundedRectangle(cornerRadius: 18, style: .continuous).stroke(Theme.hairline, lineWidth: 1))
        .staggeredAppear(index)
    }
}

/// Seçilebilir kapsül çip (seviye filtreleri, hedef seçimi). Seçili olan renkli dolar ve hafifçe büyür.
struct FilterChip: View {
    let title: String
    let selected: Bool
    var color: Color = Theme.accent
    let action: () -> Void

    var body: some View {
        Button {
            Haptics.tap()
            action()
        } label: {
            Text(title)
                .font(.jakarta(.subheadline, weight: .bold))
                .foregroundStyle(selected ? .white : color)
                .padding(.horizontal, 16)
                .padding(.vertical, 9)
                .background(selected ? AnyShapeStyle(color.gradient) : AnyShapeStyle(color.opacity(0.12)), in: Capsule())
                .scaleEffect(selected ? 1.04 : 1)
                .shadow(color: selected ? color.opacity(0.35) : .clear, radius: 6, y: 3)
        }
        .buttonStyle(PressableCardStyle())
        .animation(Motion.pop, value: selected)
    }
}

/// Yeni tasarımın süzgeç düğmesi: seçili olan vurgu renginde beyaz yazılı, diğerleri açık gri kapsül.
struct SoftChip: View {
    let title: String
    let selected: Bool
    let action: () -> Void

    var body: some View {
        Button {
            Haptics.tap()
            withAnimation(Motion.smooth) { action() }
        } label: {
            Text(title)
                .font(.custom(Theme.fontFamily, size: 15, relativeTo: .subheadline).weight(.semibold))
                .foregroundStyle(selected ? .white : HomeStyle.title)
                .padding(.horizontal, 16)
                .frame(height: 36)
                .background(selected ? Theme.accent : HomeStyle.rowFill, in: Capsule())
        }
        .buttonStyle(PressableCardStyle())
        .accessibilityAddTraits(selected ? .isSelected : [])
    }
}

/// Bölüm başlığı; isteğe bağlı sağda küçük bir eylem.
struct SectionHeader: View {
    let title: String
    var action: (title: String, run: () -> Void)?

    var body: some View {
        HStack(alignment: .firstTextBaseline) {
            Text(title).font(.jakarta(.title3, weight: .heavy)).foregroundStyle(Theme.ink)
            Spacer()
            if let action {
                Button(action.title, action: action.run)
                    .font(.jakarta(.subheadline, weight: .bold))
                    .foregroundStyle(Theme.accent)
            }
        }
    }
}

/// JAI ile boş durum: liste boşken ya da bağlantı yokken.
struct JAIEmptyState: View {
    let title: String
    let message: String
    var mood: JAIView.Mood = .thinking
    var actionTitle: String?
    var action: (() -> Void)?

    var body: some View {
        VStack(spacing: 12) {
            JAIView(mood: mood, size: 96)
            Text(title).font(.jakarta(.title3, weight: .heavy)).foregroundStyle(Theme.ink)
            Text(message)
                .font(.jakarta(.subheadline))
                .foregroundStyle(.secondary)
                .multilineTextAlignment(.center)
            if let actionTitle, let action {
                Button(actionTitle, action: action)
                    .buttonStyle(.primary)
                    .padding(.top, 4)
            }
        }
        .padding(24)
        .frame(maxWidth: .infinity)
        .background(Theme.surface, in: RoundedRectangle(cornerRadius: 24, style: .continuous))
        .overlay(RoundedRectangle(cornerRadius: 24, style: .continuous).stroke(Theme.hairline, lineWidth: 1))
    }
}

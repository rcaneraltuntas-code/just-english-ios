import SwiftUI

enum AppTab: Int, CaseIterable, Identifiable {
    case learn, practice, jai, live, profile
    var id: Int { rawValue }

    var title: String {
        switch self {
        case .learn: "Öğren"
        case .practice: "Pratik"
        case .jai: "JAI"
        case .live: "Canlı"
        case .profile: "Profil"
        }
    }

    var icon: String {
        switch self {
        case .learn: "house.fill"
        case .practice: "rectangle.stack.fill"
        case .jai: "sparkles"
        case .live: "video.fill"
        case .profile: "person.crop.circle.fill"
        }
    }

    /// Seçili sekme vurgu renginde; diğerleri gri.
    var color: Color { Theme.accent }
}

/// Sözlük artık bir sekme değil; ana sayfa ve pratikten açılan bir sayfa.
struct OpenDictionaryAction {
    let run: () -> Void
    func callAsFunction() { run() }
}

private struct OpenDictionaryKey: EnvironmentKey {
    static let defaultValue = OpenDictionaryAction {}
}

extension EnvironmentValues {
    var openDictionary: OpenDictionaryAction {
        get { self[OpenDictionaryKey.self] }
        set { self[OpenDictionaryKey.self] = newValue }
    }
}

/// Herhangi bir ekrandan sekme değiştirmek için (ana sayfadaki kısayollar).
struct SelectTabAction {
    let run: (AppTab) -> Void
    func callAsFunction(_ tab: AppTab) { run(tab) }
}

private struct SelectTabKey: EnvironmentKey {
    static let defaultValue = SelectTabAction { _ in }
}

private struct TabBarInsetKey: EnvironmentKey {
    static let defaultValue: CGFloat = 0
}

extension View {
    /// Kaydırılan içeriğin sonunu alttaki sekme çubuğunun üstünde bitirir.
    /// Doğrudan ScrollView'a/List'e uygulanmalı: TabView sayfasına verilen boşluk NavigationStack'in içine ulaşmıyor.
    func tabBarSpacer() -> some View { modifier(TabBarSpacer()) }
}

private struct TabBarSpacer: ViewModifier {
    @Environment(\.tabBarInset) private var inset

    func body(content: Content) -> some View {
        content.safeAreaInset(edge: .bottom, spacing: 0) { Color.clear.frame(height: inset) }
    }
}

extension EnvironmentValues {
    var tabBarInset: CGFloat {
        get { self[TabBarInsetKey.self] }
        set { self[TabBarInsetKey.self] = newValue }
    }

    var selectTab: SelectTabAction {
        get { self[SelectTabKey.self] }
        set { self[SelectTabKey.self] = newValue }
    }
}

/// Uygulamanın kendi sekme çubuğu: ekranın altında yüzen cam bir kapsül. Seçili sekmenin arkasında kayan
/// bir hap var; simgeler seçilince zıplar; ortadaki JAI sekmesi küçük JAI başıyla gösterilir.
struct JETabBar: View {
    @Binding var selection: AppTab
    var badges: [AppTab: Int] = [:]
    @Namespace private var pill

    var body: some View {
        HStack(spacing: 2) {
            ForEach(AppTab.allCases) { tab in
                let selected = tab == selection
                Button {
                    guard !selected else { return }
                    Haptics.tap()
                    withAnimation(.spring(response: 0.38, dampingFraction: 0.78)) { selection = tab }
                } label: {
                    VStack(spacing: 2) {
                        icon(tab, selected: selected)
                            .frame(height: 26)
                            .overlay(alignment: .topTrailing) {
                                if let count = badges[tab], count > 0 {
                                    Text(count > 99 ? "99+" : "\(count)")
                                        .font(.jakarta(.caption2, weight: .heavy))
                                        .foregroundStyle(.white)
                                        .padding(.horizontal, 5)
                                        .frame(minWidth: 18, minHeight: 18)
                                        .background(Theme.brandRed, in: Capsule())
                                        .offset(x: 12, y: -6)
                                        .contentTransition(.numericText())
                                        .transition(.scale)
                                }
                            }
                        Text(tab.title)
                            .font(.jakarta(.caption2, weight: selected ? .heavy : .semibold))
                    }
                    .foregroundStyle(selected ? tab.color : Color.secondary)
                    .frame(maxWidth: .infinity)
                    .padding(.vertical, 7)
                    .background {
                        if selected {
                            Capsule()
                                .fill(tab.color.opacity(0.13))
                                .matchedGeometryEffect(id: "pill", in: pill)
                        }
                    }
                    .contentShape(Rectangle())
                }
                .buttonStyle(.plain)
                .accessibilityLabel(tab.title)
                .accessibilityAddTraits(selected ? .isSelected : [])
            }
        }
        .padding(6)
        .glassCapsule()
        .padding(.horizontal, 16)
        .padding(.bottom, 2)
    }

    @ViewBuilder private func icon(_ tab: AppTab, selected: Bool) -> some View {
        if tab == .jai {
            JAIView(mood: selected ? .happy : .idle, size: 26)
                .scaleEffect(selected ? 1.12 : 1)
                .animation(Motion.pop, value: selected)
        } else {
            Image(systemName: tab.icon)
                .font(.system(size: 19, weight: .bold))
                .symbolEffect(.bounce.up.byLayer, value: selected)
        }
    }
}

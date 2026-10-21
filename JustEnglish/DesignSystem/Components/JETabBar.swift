import SwiftUI

enum AppTab: Int, CaseIterable, Identifiable {
    case learn, practice, dictionary, live, profile
    var id: Int { rawValue }

    var title: String {
        switch self {
        case .learn: "Öğren"
        case .practice: "Pratik"
        case .dictionary: "Sözlük"
        case .live: "Canlı"
        case .profile: "Profil"
        }
    }

    var icon: String {
        switch self {
        case .learn: "house.fill"
        case .practice: "rectangle.stack.fill"
        case .dictionary: "character.book.closed.fill"
        case .live: "video.fill"
        case .profile: "person.crop.circle.fill"
        }
    }

    var color: Color {
        switch self {
        case .learn: Theme.accent
        case .practice: Theme.streak
        case .dictionary: Theme.color(for: .a2)
        case .live: Theme.success
        case .profile: Theme.color(for: .b2)
        }
    }
}

/// Uygulamanın kendi sekme çubuğu: seçili sekmenin arkasında kayan renkli bir hap,
/// simgeler seçilince zıplar, rozet sayıları yuvarlanarak değişir.
struct JETabBar: View {
    @Binding var selection: AppTab
    var badges: [AppTab: Int] = [:]
    @Namespace private var pill

    var body: some View {
        HStack(spacing: 4) {
            ForEach(AppTab.allCases) { tab in
                let selected = tab == selection
                Button {
                    guard !selected else { return }
                    Haptics.tap()
                    withAnimation(.spring(response: 0.38, dampingFraction: 0.78)) { selection = tab }
                } label: {
                    VStack(spacing: 3) {
                        Image(systemName: tab.icon)
                            .font(.system(size: 20, weight: .bold))
                            .symbolEffect(.bounce.up.byLayer, value: selected)
                            .overlay(alignment: .topTrailing) {
                                if let count = badges[tab], count > 0 {
                                    Text(count > 99 ? "99+" : "\(count)")
                                        .font(.jakarta(.caption2, weight: .heavy))
                                        .foregroundStyle(.white)
                                        .padding(.horizontal, 5)
                                        .frame(minWidth: 18, minHeight: 18)
                                        .background(Theme.danger, in: Capsule())
                                        .offset(x: 12, y: -8)
                                        .contentTransition(.numericText())
                                        .transition(.scale)
                                }
                            }
                        Text(tab.title)
                            .font(.jakarta(.caption2, weight: selected ? .heavy : .semibold))
                    }
                    .foregroundStyle(selected ? tab.color : Color.secondary)
                    .frame(maxWidth: .infinity)
                    .padding(.vertical, 8)
                    .background {
                        if selected {
                            RoundedRectangle(cornerRadius: 16, style: .continuous)
                                .fill(tab.color.opacity(0.14))
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
        .padding(.horizontal, 10)
        .padding(.top, 8)
        .padding(.bottom, 4)
        .background {
            Rectangle()
                .fill(.bar)
                .overlay(alignment: .top) { Divider() }
                .ignoresSafeArea(edges: .bottom)
        }
    }
}

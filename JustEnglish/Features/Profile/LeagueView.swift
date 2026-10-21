import SwiftUI
import Supabase

/// Lig kademeleri: her hafta grubun ilk 7'si bir üst kademeye çıkar, son 5'i iner.
enum LeagueTier: Int, CaseIterable {
    case bronze, silver, gold, sapphire, ruby, diamond

    var title: String {
        switch self {
        case .bronze: "Bronz"
        case .silver: "Gümüş"
        case .gold: "Altın"
        case .sapphire: "Safir"
        case .ruby: "Yakut"
        case .diamond: "Elmas"
        }
    }

    var color: Color {
        switch self {
        case .bronze: Color(light: 0xB8733B, dark: 0xD99A62)
        case .silver: Color(light: 0x8A94A6, dark: 0xB8C1CF)
        case .gold: Color(light: 0xE0A100, dark: 0xFBC531)
        case .sapphire: Color(light: 0x1E3A8A, dark: 0x7B9BFF)
        case .ruby: Color(light: 0xD61F4C, dark: 0xF2557A)
        case .diamond: Color(light: 0x0EA5B7, dark: 0x5EEAD4)
        }
    }
}

struct LeagueRow: Decodable, Identifiable, Hashable {
    let rank: Int
    let displayName: String
    let xp: Int
    let isMe: Bool
    let tier: Int
    var id: Int { rank }

    enum CodingKeys: String, CodingKey {
        case rank, xp, tier
        case displayName = "display_name", isMe = "is_me"
    }
}

struct LeagueView: View {
    @Environment(AppModel.self) private var model
    @Environment(AuthService.self) private var auth
    @State private var rows: [LeagueRow] = []
    @State private var loading = true
    @State private var failed = false

    private var tier: LeagueTier { LeagueTier(rawValue: rows.first?.tier ?? 0) ?? .bronze }
    private static let promote = 7
    private static let demote = 5

    var body: some View {
        ScrollView {
            VStack(spacing: 18) {
                header
                if !auth.isSignedIn {
                    JAIEmptyState(title: "Lige katılmak için giriş yapın",
                                  message: "Profil sekmesinden Apple ile giriş yaptığınızda bu haftanın ligine otomatik katılırsınız.",
                                  mood: .idle)
                } else if loading && rows.isEmpty {
                    ProgressView().padding(40)
                } else if failed && rows.isEmpty {
                    JAIEmptyState(title: "Lig yüklenemedi",
                                  message: "İnternet bağlantınızı kontrol edip yeniden deneyin.",
                                  mood: .sad, actionTitle: "Tekrar deneyin") {
                        Task { await load() }
                    }
                } else {
                    VStack(spacing: 0) {
                        ForEach(rows) { row in
                            if row.rank == Self.promote + 1 && rows.count > Self.promote {
                                zoneDivider("Yükselme bölgesi", icon: "arrow.up", color: Theme.success)
                            }
                            if rows.count >= 10 && row.rank == rows.count - Self.demote + 1 {
                                zoneDivider("Düşme bölgesi", icon: "arrow.down", color: Theme.danger)
                            }
                            rowView(row)
                                .staggeredAppear(row.rank, delay: 0.03)
                        }
                    }
                    .padding(.vertical, 6)
                    .modifier(HomeCard())
                }
            }
            .padding(16)
        }
        .tabBarSpacer()
        .background(Theme.surface.ignoresSafeArea())
        .navigationTitle("Haftalık lig")
        .navigationBarTitleDisplayMode(.inline)
        .refreshable { await load() }
        .task { await load() }
    }

    /// Açık mavi kart: 3B kupa, lig adı, kural ve bu haftanın XP'si.
    private var header: some View {
        VStack(spacing: 10) {
            Image("lesson-trophy")
                .resizable()
                .scaledToFit()
                .frame(width: 84, height: 84)
                .symbolEffect(.bounce, value: rows.count)
            Text("\(tier.title) Ligi")
                .font(.custom(Theme.fontFamily, size: 24, relativeTo: .title2).weight(.bold))
                .foregroundStyle(HomeStyle.title)
            Text("İlk \(Self.promote) kişi bir üst lige çıkar. Liste her pazartesi yenilenir.")
                .font(.custom(Theme.fontFamily, size: 15, relativeTo: .subheadline))
                .foregroundStyle(HomeStyle.body)
                .multilineTextAlignment(.center)
            HStack(spacing: 6) {
                Image("lesson-medal").resizable().scaledToFit().frame(width: 22, height: 22)
                RollingNumber(value: model.state.progress.weekXP(at: .now), suffix: " XP bu hafta",
                              font: .custom(Theme.fontFamily, size: 15, relativeTo: .subheadline).weight(.semibold))
                    .foregroundStyle(HomeStyle.title)
            }
            .padding(.horizontal, 14)
            .frame(height: 36)
            .background(Theme.surface, in: Capsule())
            .padding(.top, 4)
        }
        .padding(.vertical, 22)
        .padding(.horizontal, 20)
        .frame(maxWidth: .infinity)
        .background(Color(light: 0xEAF1FF, dark: 0x151C38), in: RoundedRectangle(cornerRadius: 18, style: .continuous))
    }

    private func rowView(_ row: LeagueRow) -> some View {
        HStack(spacing: 12) {
            Group {
                if row.rank <= 3 {
                    Text(["🥇", "🥈", "🥉"][row.rank - 1]).font(.system(size: 24))
                } else {
                    Text("\(row.rank)")
                        .font(.custom(Theme.fontFamily, size: 16, relativeTo: .headline).weight(.bold))
                        .foregroundStyle(row.rank <= Self.promote ? Theme.success : HomeStyle.body)
                }
            }
            .frame(width: 30)
            Text(String(row.displayName.prefix(1)).uppercased())
                .font(.custom(Theme.fontFamily, size: 16, relativeTo: .headline).weight(.bold))
                .foregroundStyle(Theme.accent)
                .frame(width: 38, height: 38)
                .background(Theme.accentSoft, in: Circle())
            Text(row.isMe ? "\(row.displayName) (siz)" : row.displayName)
                .font(.custom(Theme.fontFamily, size: 16, relativeTo: .body).weight(row.isMe ? .bold : .medium))
                .foregroundStyle(HomeStyle.title)
                .lineLimit(1)
            Spacer()
            Text("\(row.xp) XP")
                .font(.custom(Theme.fontFamily, size: 15, relativeTo: .subheadline).weight(.semibold))
                .foregroundStyle(HomeStyle.body)
                .monospacedDigit()
        }
        .padding(.horizontal, 14)
        .padding(.vertical, 10)
        .background(row.isMe ? Theme.accentSoft : .clear, in: RoundedRectangle(cornerRadius: 12, style: .continuous))
        .padding(.horizontal, 6)
    }

    private func zoneDivider(_ text: String, icon: String, color: Color) -> some View {
        HStack(spacing: 6) {
            Rectangle().fill(color.opacity(0.35)).frame(height: 1.5)
            Label(text, systemImage: icon)
                .font(.custom(Theme.fontFamily, size: 13, relativeTo: .caption).weight(.semibold))
                .foregroundStyle(color)
                .fixedSize()
            Rectangle().fill(color.opacity(0.35)).frame(height: 1.5)
        }
        .padding(.horizontal, 16)
        .padding(.vertical, 8)
    }

    private func load() async {
        guard let client = Backend.client, let id = auth.userID else { loading = false; return }
        loading = true
        defer { loading = false }
        // Önce bu haftanın XP'si bildirilir; ilk açılışta öğrenci lige burada katılır.
        await SyncService.sync(model, userID: id)
        do {
            rows = try await client.rpc("league_standings").execute().value
            failed = false
        } catch {
            failed = true
        }
    }
}

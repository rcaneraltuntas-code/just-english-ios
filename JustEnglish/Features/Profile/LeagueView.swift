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
                    ContentUnavailableView("Lige katılmak için giriş yapın", systemImage: "person.crop.circle.badge.plus",
                                           description: Text("Profil sekmesinden Apple ile giriş yaptığınızda bu haftanın ligine otomatik katılırsınız."))
                } else if loading && rows.isEmpty {
                    ProgressView().padding(40)
                } else if failed && rows.isEmpty {
                    ContentUnavailableView("Lig yüklenemedi", systemImage: "wifi.exclamationmark",
                                           description: Text("İnternet bağlantınızı kontrol edip aşağı çekerek yenileyin."))
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
                    .background(Theme.surface, in: RoundedRectangle(cornerRadius: 18, style: .continuous))
                }
            }
            .padding(20)
        }
        .tabBarSpacer()
        .background(Theme.background)
        .navigationTitle("Haftalık lig")
        .navigationBarTitleDisplayMode(.inline)
        .refreshable { await load() }
        .task { await load() }
    }

    private var header: some View {
        VStack(spacing: 10) {
            ZStack {
                Image(systemName: "shield.fill")
                    .font(.system(size: 92))
                    .foregroundStyle(LinearGradient(colors: [tier.color, tier.color.blended(with: .black, amount: 0.25)],
                                                    startPoint: .top, endPoint: .bottom))
                    .shadow(color: tier.color.opacity(0.45), radius: 16, y: 8)
                Image(systemName: "trophy.fill").font(.system(size: 34, weight: .bold)).foregroundStyle(.white)
            }
            .symbolEffect(.bounce, value: rows.count)
            Text("\(tier.title) Ligi").font(.jakarta(.title, weight: .heavy))
            Text("İlk \(Self.promote) bir üst lige çıkar. Liste her pazartesi yenilenir.")
                .font(.jakarta(.subheadline))
                .foregroundStyle(.secondary)
                .multilineTextAlignment(.center)
            HStack(spacing: 4) {
                Image(systemName: "bolt.fill").foregroundStyle(Theme.warning)
                RollingNumber(value: model.state.progress.weekXP(at: .now), suffix: " XP bu hafta",
                              font: .jakarta(.headline, weight: .heavy))
            }
        }
    }

    private func rowView(_ row: LeagueRow) -> some View {
        HStack(spacing: 14) {
            Group {
                if row.rank <= 3 {
                    Image(systemName: "medal.fill")
                        .foregroundStyle([Theme.warning, LeagueTier.silver.color, LeagueTier.bronze.color][row.rank - 1])
                } else {
                    Text("\(row.rank)").foregroundStyle(row.rank <= Self.promote ? Theme.success : .secondary)
                }
            }
            .font(.jakarta(.headline, weight: .heavy))
            .frame(width: 28)
            Text(String(row.displayName.prefix(1)).uppercased())
                .font(.jakarta(.headline, weight: .bold))
                .foregroundStyle(.white)
                .frame(width: 40, height: 40)
                .background(avatarColor(row.displayName), in: Circle())
            Text(row.isMe ? "\(row.displayName) (siz)" : row.displayName)
                .font(.jakarta(.body, weight: row.isMe ? .heavy : .semibold))
                .lineLimit(1)
            Spacer()
            Text("\(row.xp) XP").font(.jakarta(.subheadline, weight: .bold)).foregroundStyle(.secondary).monospacedDigit()
        }
        .padding(.horizontal, 16)
        .padding(.vertical, 12)
        .background(row.isMe ? Theme.accent.opacity(0.12) : .clear)
    }

    private func zoneDivider(_ text: String, icon: String, color: Color) -> some View {
        HStack(spacing: 6) {
            Rectangle().fill(color.opacity(0.4)).frame(height: 1.5)
            Label(text, systemImage: icon).font(.jakarta(.caption, weight: .heavy)).foregroundStyle(color).fixedSize()
            Rectangle().fill(color.opacity(0.4)).frame(height: 1.5)
        }
        .padding(.horizontal, 16)
        .padding(.vertical, 8)
    }

    private func avatarColor(_ name: String) -> Color {
        let palette: [Color] = [Theme.accent, Theme.success, Theme.streak, Theme.color(for: .b2), Theme.color(for: .c1), Theme.color(for: .a2)]
        return palette[abs(name.unicodeScalars.reduce(0) { $0 &+ Int($1.value) }) % palette.count]
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

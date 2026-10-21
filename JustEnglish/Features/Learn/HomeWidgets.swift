import SwiftUI
import JECore

// Ana sayfanın parçaları (referans 2'deki düzen): mavi bant üstünde selam ve JAI kartı, ardından beyaz zeminde
// seri haftası, iki küçük istatistik kartı, "Akıcılığa giden yol" listesi ve günün kelimesi.

/// Ana sayfa renkleri: üstte doygun mavi bant, altında düz, neredeyse beyaz zemin.
enum HomeStyle {
    static let bandTop = Color(light: 0x6A9BFF, dark: 0x2A3F86)
    static let bandMid = Color(light: 0x8DB4FF, dark: 0x22336E)
    static let page = Color(light: 0xF7F9FC, dark: 0x0B0D16)
    static let cardBorder = Color(light: 0xE3E7EE, dark: 0x2A2F42)
    static let rowFill = Color(light: 0xF5F6F8, dark: 0x1A1E2C)
    static let body = Color(light: 0x6B7280, dark: 0x9AA3B5)
    static let title = Color(light: 0x2E3240, dark: 0xF2F4FA)

    /// Bant: en üstte #6A9BFF, ~330pt'de zemin rengine iner.
    static var band: some View {
        LinearGradient(stops: [.init(color: bandTop, location: 0),
                               .init(color: bandMid, location: 0.45),
                               .init(color: page, location: 1)],
                       startPoint: .top, endPoint: .bottom)
    }
}

/// Mavi bandın üstündeki selam: beyaz yuvarlak içinde JAI, beyaz ad, zil ve bayrak yarı saydam beyaz dairelerde.
struct HomeHeader: View {
    @Environment(AppModel.self) private var model
    @Environment(\.selectTab) private var selectTab

    var body: some View {
        let progress = model.state.progress
        HStack(spacing: 10) {
            JAIView(mood: progress.goalReachedToday ? .happy : .idle, size: 28)
                .frame(width: 36, height: 36)
                .background(.white, in: Circle())
            Text(model.state.name.isEmpty ? "Merhaba!" : "Merhaba, \(model.state.name)!")
                .font(.custom(Theme.fontFamily, size: 20, relativeTo: .title3).weight(.bold))
                .foregroundStyle(.white)
                .lineLimit(1)
                .minimumScaleFactor(0.8)
            Spacer(minLength: 8)
            // Zil: bekleyen kart tekrarı varsa küçük kırmızı nokta; dokununca pratiğe götürür.
            Button { selectTab(.practice) } label: {
                Image(systemName: "bell")
                    .font(.system(size: 17, weight: .medium))
                    .foregroundStyle(.white)
                    .frame(width: 36, height: 36)
                    .background(.white.opacity(0.25), in: Circle())
                    .overlay(alignment: .topTrailing) {
                        if model.dueCards().count > 0 {
                            Circle().fill(Theme.brandRed).frame(width: 8, height: 8).offset(x: -7, y: 7)
                        }
                    }
            }
            .accessibilityLabel("Bildirimler")
            Text("🇬🇧")
                .font(.system(size: 20))
                .frame(width: 36, height: 36)
                .background(.white.opacity(0.25), in: Circle())
                .accessibilityLabel("Öğrenilen dil: İngilizce")
        }
        .padding(.top, 8)
    }
}

/// "JAI ile tanışın" kartı: mavi bant üstünde yarı saydam beyaz cam; JAI sekmesine götürür.
struct AIBuddyCard: View {
    @Environment(\.selectTab) private var selectTab
    @State private var hop = 0

    var body: some View {
        VStack(alignment: .leading, spacing: 0) {
            Text("Yapay zekâ arkadaşınız JAI ile tanışın")
                .font(.custom(Theme.fontFamily, size: 17, relativeTo: .headline).weight(.bold))
                .foregroundStyle(HomeStyle.title)
                .fixedSize(horizontal: false, vertical: true)
                .padding(.trailing, 64)
            Text("Bir arkadaşınızla konuşur gibi gerçek hayattan cümlelerle pratik yapın.")
                .font(.custom(Theme.fontFamily, size: 15, relativeTo: .subheadline))
                .foregroundStyle(HomeStyle.body)
                .lineSpacing(4)
                .fixedSize(horizontal: false, vertical: true)
                .padding(.trailing, 40)
                .padding(.top, 8)
            Button { selectTab(.jai) } label: {
                Text("Pratiğe başla")
                    .font(.custom(Theme.fontFamily, size: 17, relativeTo: .headline).weight(.medium))
                    .foregroundStyle(.white)
                    .padding(.horizontal, 18)
                    .frame(height: 38)
                    .background(Theme.accent, in: RoundedRectangle(cornerRadius: 10, style: .continuous))
                    .background(RoundedRectangle(cornerRadius: 10, style: .continuous).fill(Theme.accentDeep).offset(y: 3))
            }
            .buttonStyle(PressableCardStyle())
            .padding(.top, 18)
        }
        .padding(.leading, 17)
        .padding(.trailing, 14)
        .padding(.top, 22)
        .padding(.bottom, 22)
        .frame(maxWidth: .infinity, alignment: .leading)
        .overlay(alignment: .topTrailing) {
            JAIView(mood: .happy, size: 56, bounceTrigger: hop)
                .padding(.top, 14)
                .padding(.trailing, 14)
                .onTapGesture { hop += 1; Haptics.tap() }
        }
        .background(Color(light: 0xFFFFFF, dark: 0x171A26).opacity(0.6), in: RoundedRectangle(cornerRadius: 18, style: .continuous))
        .background(.ultraThinMaterial.opacity(0.5), in: RoundedRectangle(cornerRadius: 18, style: .continuous))
        .overlay(RoundedRectangle(cornerRadius: 18, style: .continuous).stroke(.white.opacity(0.8), lineWidth: 1))
        .task {
            try? await Task.sleep(for: .seconds(0.8))
            hop += 1
        }
    }
}

/// Beyaz, ince kenarlıklı, gölgesiz ana sayfa kartı.
private struct HomeCard: ViewModifier {
    var radius: CGFloat = 18
    func body(content: Content) -> some View {
        content
            .background(Theme.surface, in: RoundedRectangle(cornerRadius: radius, style: .continuous))
            .overlay(RoundedRectangle(cornerRadius: radius, style: .continuous).stroke(HomeStyle.cardBorder, lineWidth: 1.5))
    }
}

/// Seri kartı: krem kare içinde 3B alev, mesaj ve pazartesiden pazara yedi gün (hedefi tutturulan günler altın).
struct StreakWeekCard: View {
    @Environment(AppModel.self) private var model

    private static let labels = ["Pt", "Sa", "Ça", "Pe", "Cu", "Ct", "Pz"]

    var body: some View {
        let progress = model.state.progress
        let streak = progress.displayedStreak(at: .now)
        let done = weekDone(progress)
        HStack(spacing: 14) {
            Image("lesson-fire")
                .resizable()
                .scaledToFit()
                .frame(width: 40, height: 40)
                .frame(width: 58, height: 66)
                .background(Color(light: 0xFFF6E8, dark: 0x2E2418), in: RoundedRectangle(cornerRadius: 12, style: .continuous))
                .symbolEffect(.bounce, value: streak)
            VStack(alignment: .leading, spacing: 10) {
                Text(streak > 0 ? "\(streak) günlük seri. Harika gidiyorsunuz!" : "Bugün hedefinizi tutturun, seriniz başlasın!")
                    .font(.custom(Theme.fontFamily, size: 16, relativeTo: .headline).weight(.bold))
                    .foregroundStyle(HomeStyle.title)
                    .fixedSize(horizontal: false, vertical: true)
                HStack(spacing: 0) {
                    ForEach(0..<7, id: \.self) { i in
                        VStack(spacing: 5) {
                            ZStack {
                                if done[i] {
                                    Circle().fill(Color(light: 0xF5B731, dark: 0xFBBF24))
                                    Image(systemName: "checkmark").font(.system(size: 11, weight: .heavy)).foregroundStyle(.white)
                                } else {
                                    Circle().stroke(Color(light: 0xC9CED8, dark: 0x3A4058), lineWidth: 1.5)
                                }
                            }
                            .frame(width: 26, height: 26)
                            Text(Self.labels[i])
                                .font(.custom(Theme.fontFamily, size: 14, relativeTo: .footnote))
                                .foregroundStyle(HomeStyle.body)
                        }
                        .frame(maxWidth: .infinity)
                        .staggeredAppear(i, delay: 0.04)
                    }
                }
            }
        }
        .padding(.horizontal, 16)
        .padding(.vertical, 18)
        .modifier(HomeCard())
        .accessibilityElement(children: .combine)
    }

    /// Bu haftanın (pazartesi başlar) her günü için hedef tutturuldu mu?
    private func weekDone(_ progress: StudyProgress) -> [Bool] {
        let calendar = Calendar.current
        let goal = max(progress.dailyGoalXP, 1)
        guard let monday = StudyProgress.weekStart(of: .now, calendar: calendar) else { return Array(repeating: false, count: 7) }
        let recent = progress.recentDays(7, endingAt: .now, calendar: calendar)
        return (0..<7).map { offset in
            guard let day = calendar.date(byAdding: .day, value: offset, to: monday) else { return false }
            return recent.first { calendar.isDate($0.day, inSameDayAs: day) }.map { $0.xp >= goal } ?? false
        }
    }
}

/// İki küçük kart: bu haftaki XP ve günlük hedefe kalan, 3B simgelerle.
struct HomeStatPair: View {
    @Environment(AppModel.self) private var model

    var body: some View {
        let progress = model.state.progress
        let today = progress.todayDay.map { Calendar.current.isDateInToday($0) } == true ? progress.todayXP : 0
        let left = max(progress.dailyGoalXP - today, 0)
        // Hedef dakika olarak seçildi; 1 dakika ≈ 2 XP (DailyGoal.xp).
        let minutes = Int((Double(left) / 2).rounded(.up))
        HStack(spacing: 13) {
            tile(art: "medal", title: "\(progress.weekXP(at: .now)) XP kazanıldı", detail: "bu hafta")
            tile(art: "target", title: left == 0 ? "Hedef tamam!" : "\(minutes) dk kaldı", detail: left == 0 ? "bugün harikasınız" : "günlük hedefe")
        }
    }

    private func tile(art: String, title: String, detail: String) -> some View {
        HStack(spacing: 10) {
            Image("lesson-\(art)").resizable().scaledToFit().frame(width: 40, height: 40)
            VStack(alignment: .leading, spacing: 2) {
                Text(title)
                    .font(.custom(Theme.fontFamily, size: 16, relativeTo: .headline).weight(.semibold))
                    .foregroundStyle(HomeStyle.title)
                    .lineLimit(1)
                    .minimumScaleFactor(0.8)
                    .contentTransition(.numericText())
                Text(detail)
                    .font(.custom(Theme.fontFamily, size: 15, relativeTo: .subheadline).weight(.medium))
                    .foregroundStyle(HomeStyle.title)
                    .lineLimit(1)
                    .minimumScaleFactor(0.8)
            }
            Spacer(minLength: 0)
        }
        .padding(.horizontal, 12)
        .frame(height: 75)
        .modifier(HomeCard(radius: 16))
    }
}

/// Referanstaki "Your path to fluency": açık gri satırlar, solda 3B simge, başlık, gri ayrıntı ve ok.
/// İlk satır sıradaki dersi doğrudan açar.
struct FluencyPathList: View {
    let level: CEFRLevel
    let onContinue: () -> Void
    @Environment(AppModel.self) private var model
    @Environment(\.selectTab) private var selectTab
    @Environment(\.openDictionary) private var openDictionary

    var body: some View {
        let units = model.units(for: level)
        let total = units.map(\.lessons.count).reduce(0, +)
        let done = units.map { model.completedCount(in: $0) }.reduce(0, +)
        let due = model.dueCards().count
        VStack(spacing: 13) {
            if model.nextLesson != nil {
                Button(action: onContinue) {
                    row("closedbook", "Dersleri tamamlayın, ödül kazanın", "\(done)/\(total) ders tamamlandı")
                }
                .buttonStyle(PressableCardStyle())
            }
            Button { selectTab(.practice) } label: {
                row("cards", "Kelime kartlarını tekrar edin", due > 0 ? "\(due) kart sizi bekliyor" : "Bugünlük tekrar tamam")
            }
            .buttonStyle(PressableCardStyle())
            Button { selectTab(.practice) } label: {
                row("game", "Oyunlarla pekiştirin", "Eşleştirme, 60 saniye, dinle ve yaz")
            }
            .buttonStyle(PressableCardStyle())
            Button { openDictionary() } label: {
                row("book", "Sözlükte kelime arayın", "\(model.dictionary.count) kelime ve kalıp")
            }
            .buttonStyle(PressableCardStyle())
            Button { selectTab(.live) } label: {
                row("videocam", "Canlı derse katılın", "Öğretmenle küçük grup dersleri")
            }
            .buttonStyle(PressableCardStyle())
            NavigationLink { LeagueView() } label: {
                row("trophy", "Haftalık lig", "Bu hafta \(model.state.progress.weekXP(at: .now)) XP")
            }
            .buttonStyle(PressableCardStyle())
        }
    }

    private func row(_ art: String, _ title: String, _ detail: String) -> some View {
        HStack(spacing: 14) {
            Image("lesson-\(art)").resizable().scaledToFit().frame(width: 44, height: 44)
            VStack(alignment: .leading, spacing: 4) {
                Text(title)
                    .font(.custom(Theme.fontFamily, size: 15, relativeTo: .subheadline).weight(.semibold))
                    .foregroundStyle(HomeStyle.title)
                    .fixedSize(horizontal: false, vertical: true)
                Text(detail)
                    .font(.custom(Theme.fontFamily, size: 15, relativeTo: .footnote))
                    .foregroundStyle(HomeStyle.body)
                    .lineLimit(1)
                    .minimumScaleFactor(0.85)
            }
            Spacer(minLength: 4)
            Image(systemName: "chevron.right").font(.system(size: 15, weight: .semibold)).foregroundStyle(HomeStyle.title)
        }
        .padding(.leading, 14)
        .padding(.trailing, 18)
        .padding(.vertical, 12)
        .frame(minHeight: 68)
        .background(HomeStyle.rowFill, in: RoundedRectangle(cornerRadius: 16, style: .continuous))
    }
}

/// Her gün değişen bir kelime. Karta dokununca Türkçe anlamı bulanıklıktan çıkar.
struct WordOfTheDayCard: View {
    @Environment(AppModel.self) private var model
    @State private var revealed = false

    private var entry: DictionaryEntry? {
        let words = model.dictionary.filter { !$0.headword.contains(" ") && $0.senses.first?.level == model.state.currentLevel }
        let pool = words.isEmpty ? model.dictionary : words
        guard !pool.isEmpty else { return nil }
        let day = Calendar.current.ordinality(of: .day, in: .era, for: .now) ?? 0
        return pool[day % pool.count]
    }

    var body: some View {
        if let entry, let sense = entry.senses.first {
            VStack(alignment: .leading, spacing: 12) {
                HStack {
                    Label("Günün kelimesi", systemImage: "sparkles")
                        .font(.jakarta(.caption, weight: .heavy))
                        .foregroundStyle(.white.opacity(0.9))
                    Spacer()
                    LevelBadge(level: sense.level)
                }
                HStack(alignment: .center) {
                    Text(entry.headword)
                        .font(.jakarta(.title, weight: .heavy))
                        .foregroundStyle(.white)
                        .minimumScaleFactor(0.6)
                        .lineLimit(1)
                    Spacer()
                    SpeakButton(text: entry.headword)
                        .colorScheme(.dark)
                }
                ZStack(alignment: .leading) {
                    Text(sense.card.tr)
                        .font(.jakarta(.title3, weight: .bold))
                        .foregroundStyle(.white)
                        .blur(radius: revealed ? 0 : 10)
                        .opacity(revealed ? 1 : 0.5)
                    if !revealed {
                        Label("Anlamı görmek için dokunun", systemImage: "hand.tap.fill")
                            .font(.jakarta(.caption, weight: .bold))
                            .foregroundStyle(.white)
                            .fixedSize()
                            .transition(.opacity)
                    }
                }
                Text("“\(sense.card.example)”")
                    .font(.jakarta(.subheadline, weight: .medium))
                    .foregroundStyle(.white.opacity(0.85))
                    .fixedSize(horizontal: false, vertical: true)
                if model.isInDeck(sense.card.id) {
                    Label("Destenizde", systemImage: "checkmark.circle.fill")
                        .font(.jakarta(.footnote, weight: .bold))
                        .foregroundStyle(.white)
                } else {
                    Button {
                        withAnimation(Motion.pop) { model.addToDeck(sense.card.id) }
                        Haptics.success()
                    } label: {
                        Label("Kartlarıma ekle", systemImage: "plus")
                    }
                    .buttonStyle(DepthButtonStyle(color: .white, foreground: Theme.ai, height: 44))
                }
            }
            .padding(18)
            .background {
                ZStack(alignment: .topTrailing) {
                    Theme.aiGradient
                    NeuralNetwork(animated: false, color: .white).opacity(0.6)
                    Circle().fill(.white.opacity(0.15)).frame(width: 160).blur(radius: 30).offset(x: 40, y: -40)
                }
                .clipShape(RoundedRectangle(cornerRadius: 24, style: .continuous))
            }
            .shadow(color: Theme.ai.opacity(0.3), radius: 16, y: 8)
            .contentShape(Rectangle())
            .onTapGesture { withAnimation(Motion.smooth) { revealed.toggle() } }
        }
    }
}

/// "Canlı" yazısının yanında atan küçük kırmızı nokta (markanın kırmızısı yalnızca burada).
struct LivePulse: View {
    var color: Color = Theme.brandRed
    @State private var pulse = false
    @Environment(\.accessibilityReduceMotion) private var reduceMotion

    var body: some View {
        ZStack {
            Circle().fill(color.opacity(0.35)).frame(width: 18, height: 18)
                .scaleEffect(pulse ? 1.3 : 0.6)
                .opacity(pulse ? 0 : 1)
            Circle().fill(color).frame(width: 9, height: 9)
        }
        .onAppear {
            guard !reduceMotion else { return }
            withAnimation(.easeOut(duration: 1.2).repeatForever(autoreverses: false)) { pulse = true }
        }
        .accessibilityHidden(true)
    }
}

import SwiftUI
import JECore

// Ana sayfanın parçaları (referans tasarımdaki düzen): selamlı başlık, JAI kartı, seri haftası,
// iki küçük istatistik kartı, "akıcılık yolunuz" listesi ve günün kelimesi.

/// Mavi bandın üstündeki selam: JAI avatarı, ad, zil ve öğrenilen dilin bayrağı.
struct HomeHeader: View {
    @Environment(AppModel.self) private var model
    @Environment(\.selectTab) private var selectTab

    var body: some View {
        let progress = model.state.progress
        HStack(spacing: 12) {
            JAIView(mood: progress.goalReachedToday ? .happy : .idle, size: 38)
                .frame(width: 46, height: 46)
                .background(.white, in: Circle())
                .shadow(color: Theme.ink.opacity(0.12), radius: 6, y: 3)
            VStack(alignment: .leading, spacing: 1) {
                Text(greetingTime).font(.jakarta(.caption, weight: .semibold)).foregroundStyle(.white.opacity(0.85))
                Text(model.state.name.isEmpty ? "Merhaba!" : "Merhaba, \(model.state.name)!")
                    .font(.jakarta(.title3, weight: .heavy))
                    .foregroundStyle(.white)
                    .lineLimit(1)
                    .minimumScaleFactor(0.8)
            }
            Spacer(minLength: 8)
            // Zil: bekleyen kart tekrarı varsa küçük kırmızı nokta; dokununca pratiğe götürür.
            Button { selectTab(.practice) } label: {
                Image(systemName: "bell")
                    .font(.system(size: 18, weight: .semibold))
                    .foregroundStyle(.white)
                    .frame(width: 42, height: 42)
                    .glassCapsule(tint: .white, interactive: true)
                    .overlay(alignment: .topTrailing) {
                        if model.dueCards().count > 0 {
                            Circle().fill(Theme.brandRed).frame(width: 9, height: 9).offset(x: -9, y: 9)
                        }
                    }
            }
            .accessibilityLabel("Bildirimler")
            Text("🇬🇧")
                .font(.system(size: 24))
                .frame(width: 42, height: 42)
                .glassCapsule(tint: .white)
                .accessibilityLabel("Öğrenilen dil: İngilizce")
        }
        .padding(.top, 8)
    }

    private var greetingTime: String {
        let hour = Calendar.current.component(.hour, from: .now)
        return hour < 12 ? "Günaydın" : hour < 18 ? "İyi günler" : "İyi akşamlar"
    }

}

/// "Yapay zekâ arkadaşınızla tanışın" kartı: JAI sekmesine götürür.
struct AIBuddyCard: View {
    @Environment(\.selectTab) private var selectTab
    @State private var hop = 0

    var body: some View {
        HStack(alignment: .center, spacing: 12) {
            VStack(alignment: .leading, spacing: 8) {
                Text("Yapay zekâ arkadaşınız JAI ile tanışın")
                    .font(.jakarta(.headline, weight: .heavy))
                    .foregroundStyle(Theme.ink)
                    .fixedSize(horizontal: false, vertical: true)
                Text("Bir arkadaşınızla konuşur gibi gerçek hayattan cümlelerle pratik yapın.")
                    .font(.jakarta(.subheadline, weight: .medium))
                    .foregroundStyle(.secondary)
                    .fixedSize(horizontal: false, vertical: true)
                Button { selectTab(.jai) } label: {
                    Label("Pratiğe başla", systemImage: "sparkles")
                        .padding(.horizontal, 18)
                }
                .buttonStyle(DepthButtonStyle(height: 44))
                .fixedSize()
                .padding(.top, 4)
            }
            Spacer(minLength: 0)
            JAIView(mood: .happy, size: 86, bounceTrigger: hop)
                .onTapGesture { hop += 1; Haptics.tap() }
        }
        .padding(18)
        .glass(cornerRadius: 26)
        .task {
            try? await Task.sleep(for: .seconds(0.8))
            hop += 1
        }
    }
}

/// Seri kartı: alev, mesaj ve pazartesiden pazara yedi gün (hedefi tutturulan günler işaretli).
struct StreakWeekCard: View {
    @Environment(AppModel.self) private var model

    private static let labels = ["Pt", "Sa", "Ça", "Pe", "Cu", "Ct", "Pz"]

    var body: some View {
        let progress = model.state.progress
        let streak = progress.displayedStreak(at: .now)
        let done = weekDone(progress)
        HStack(spacing: 14) {
            Text("🔥")
                .font(.system(size: 40))
                .frame(width: 64, height: 76)
                .background(Theme.streak.opacity(0.1), in: RoundedRectangle(cornerRadius: 18, style: .continuous))
                .symbolEffect(.bounce, value: streak)
            VStack(alignment: .leading, spacing: 10) {
                Text(streak > 0 ? "\(streak) günlük seri. Harika gidiyorsunuz!" : "Bugün hedefinizi tutturun, seriniz başlasın!")
                    .font(.jakarta(.subheadline, weight: .heavy))
                    .foregroundStyle(Theme.ink)
                    .fixedSize(horizontal: false, vertical: true)
                HStack(spacing: 0) {
                    ForEach(0..<7, id: \.self) { i in
                        VStack(spacing: 4) {
                            ZStack {
                                Circle()
                                    .fill(done[i] ? AnyShapeStyle(Theme.warning.gradient) : AnyShapeStyle(Color.clear))
                                Circle()
                                    .stroke(done[i] ? Theme.warning : Color(uiColor: .systemGray4), lineWidth: 1.5)
                                if done[i] {
                                    Image(systemName: "checkmark").font(.system(size: 11, weight: .black)).foregroundStyle(.white)
                                }
                            }
                            .frame(width: 24, height: 24)
                            .scaleEffect(done[i] ? 1 : 0.92)
                            Text(Self.labels[i])
                                .font(.jakarta(.caption2, weight: .semibold))
                                .foregroundStyle(.secondary)
                        }
                        .frame(maxWidth: .infinity)
                        .staggeredAppear(i, delay: 0.04)
                    }
                }
            }
        }
        .card()
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

/// İki küçük kart: bu haftaki XP ve günlük hedefe kalan.
struct HomeStatPair: View {
    @Environment(AppModel.self) private var model

    var body: some View {
        let progress = model.state.progress
        let today = progress.todayDay.map { Calendar.current.isDateInToday($0) } == true ? progress.todayXP : 0
        let left = max(progress.dailyGoalXP - today, 0)
        // Hedef dakika olarak seçildi; 1 dakika ≈ 2 XP (DailyGoal.xp).
        let minutes = Int((Double(left) / 2).rounded(.up))
        HStack(spacing: 12) {
            tile(emoji: "🏅", title: "\(progress.weekXP(at: .now)) XP", detail: "bu hafta kazanıldı")
            tile(emoji: "🎯", title: left == 0 ? "Hedef tamam!" : "\(minutes) dk kaldı", detail: left == 0 ? "bugün harikasınız" : "günlük hedefe")
        }
    }

    private func tile(emoji: String, title: String, detail: String) -> some View {
        HStack(spacing: 10) {
            Text(emoji).font(.system(size: 30))
            VStack(alignment: .leading, spacing: 1) {
                Text(title)
                    .font(.jakarta(.headline, weight: .heavy))
                    .foregroundStyle(Theme.ink)
                    .lineLimit(1)
                    .minimumScaleFactor(0.7)
                    .contentTransition(.numericText())
                Text(detail).font(.jakarta(.caption, weight: .medium)).foregroundStyle(.secondary).lineLimit(1)
            }
            Spacer(minLength: 0)
        }
        .card()
    }
}

/// Referanstaki "Your path to fluency": her satır bir yere götürür, ilerleme metniyle.
struct FluencyPathList: View {
    let level: CEFRLevel
    @Environment(AppModel.self) private var model
    @Environment(\.selectTab) private var selectTab
    @Environment(\.openDictionary) private var openDictionary

    var body: some View {
        let units = model.units(for: level)
        let total = units.map(\.lessons.count).reduce(0, +)
        let done = units.map { model.completedCount(in: $0) }.reduce(0, +)
        let due = model.dueCards().count
        VStack(spacing: 10) {
            if let unit = model.nextLesson?.unit {
                NavigationLink(value: unit) {
                    row("📚", "Dersleri tamamlayın", "\(level.rawValue): \(done) / \(total) ders tamamlandı", progress: Double(done) / Double(max(total, 1)))
                }
                .buttonStyle(PressableCardStyle())
            }
            Button { selectTab(.practice) } label: {
                row("🃏", "Kelime kartlarını tekrar edin", due > 0 ? "\(due) kart sizi bekliyor" : "Bugünlük tekrar tamam")
            }
            .buttonStyle(PressableCardStyle())
            Button { selectTab(.practice) } label: {
                row("🎮", "Oyunlarla pekiştirin", "Eşleştirme, 60 saniye, dinle ve yaz")
            }
            .buttonStyle(PressableCardStyle())
            Button { openDictionary() } label: {
                row("📖", "Sözlükte kelime arayın", "\(model.dictionary.count) kelime ve kalıp")
            }
            .buttonStyle(PressableCardStyle())
            Button { selectTab(.live) } label: {
                row("🎥", "Canlı derse katılın", "Öğretmenle küçük grup dersleri")
            }
            .buttonStyle(PressableCardStyle())
            NavigationLink { LeagueView() } label: {
                row("🏆", "Haftalık lig", "Bu hafta \(model.state.progress.weekXP(at: .now)) XP")
            }
            .buttonStyle(PressableCardStyle())
        }
    }

    private func row(_ emoji: String, _ title: String, _ detail: String, progress: Double? = nil) -> some View {
        HStack(spacing: 14) {
            Text(emoji)
                .font(.system(size: 28))
                .frame(width: 50, height: 50)
                .background(Theme.surfaceRaised, in: RoundedRectangle(cornerRadius: 14, style: .continuous))
            VStack(alignment: .leading, spacing: 4) {
                Text(title).font(.jakarta(.subheadline, weight: .heavy)).foregroundStyle(Theme.ink)
                Text(detail).font(.jakarta(.footnote, weight: .medium)).foregroundStyle(.secondary).lineLimit(1)
                if let progress {
                    ProgressBar(value: progress, color: Theme.accent, height: 5).padding(.top, 2)
                }
            }
            Spacer(minLength: 4)
            Image(systemName: "chevron.right").font(.jakarta(.subheadline, weight: .bold)).foregroundStyle(.tertiary)
        }
        .padding(12)
        .background(Theme.surface, in: RoundedRectangle(cornerRadius: 20, style: .continuous))
        .overlay(RoundedRectangle(cornerRadius: 20, style: .continuous).stroke(Theme.hairline, lineWidth: 1))
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

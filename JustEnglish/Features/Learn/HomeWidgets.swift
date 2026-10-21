import SwiftUI
import JECore

// Ana sayfanın içerik kartları: haftalık etkinlik, kısayollar, günün kelimesi, lig ve sıradaki canlı ders.

/// Son 7 günün XP çubukları; bugünkü çubuk marka kırmızısı, hedefe ulaşılan günler dolu.
struct WeekActivityCard: View {
    @Environment(AppModel.self) private var model
    @State private var grown = false

    var body: some View {
        let progress = model.state.progress
        let days = progress.recentDays(7, endingAt: .now)
        let goal = max(progress.dailyGoalXP, 1)
        let peak = max(days.map(\.xp).max() ?? 0, goal)
        let total = days.map(\.xp).reduce(0, +)
        VStack(alignment: .leading, spacing: 14) {
            HStack(alignment: .firstTextBaseline) {
                VStack(alignment: .leading, spacing: 2) {
                    Text("Bu hafta").font(.jakarta(.headline, weight: .heavy)).foregroundStyle(Theme.ink)
                    Text("Son 7 günde \(total) XP").font(.jakarta(.footnote)).foregroundStyle(.secondary)
                }
                Spacer()
                Label("\(days.filter { $0.xp >= goal }.count)/7 gün hedef", systemImage: "target")
                    .font(.jakarta(.caption, weight: .bold))
                    .foregroundStyle(Theme.accent)
                    .padding(.horizontal, 10)
                    .padding(.vertical, 5)
                    .background(Theme.accentSoft, in: Capsule())
            }
            HStack(alignment: .bottom, spacing: 10) {
                ForEach(Array(days.enumerated()), id: \.offset) { index, day in
                    let isToday = index == days.count - 1
                    let reached = day.xp >= goal
                    VStack(spacing: 6) {
                        Text(day.xp > 0 ? "\(day.xp)" : "")
                            .font(.jakarta(.caption2, weight: .bold))
                            .foregroundStyle(isToday ? Theme.accent : reached ? Theme.success : .secondary)
                        Capsule()
                            .fill(isToday ? AnyShapeStyle(Theme.brandGradient)
                                  : reached ? AnyShapeStyle(Theme.success.gradient) : AnyShapeStyle(Color(uiColor: .systemGray4)))
                            .frame(height: grown ? max(8, 84 * CGFloat(day.xp) / CGFloat(peak)) : 8)
                            .overlay(alignment: .top) {
                                if reached {
                                    Image(systemName: "checkmark")
                                        .font(.system(size: 9, weight: .black))
                                        .foregroundStyle(.white)
                                        .padding(.top, 5)
                                }
                            }
                            .animation(Motion.pop.delay(Double(index) * 0.06), value: grown)
                        Text(day.day.formatted(.dateTime.weekday(.narrow)))
                            .font(.jakarta(.caption, weight: isToday ? .heavy : .semibold))
                            .foregroundStyle(isToday ? Theme.accent : .secondary)
                    }
                    .frame(maxWidth: .infinity)
                }
            }
            .frame(height: 124, alignment: .bottom)
        }
        .card()
        .onAppear { grown = true }
        .accessibilityElement(children: .combine)
        .accessibilityLabel("Son 7 günde \(total) XP")
    }
}

/// Dört kısayol: diğer sekmelere tek dokunuşla geçiş. Beyaz kartlar, her birinin kendi renkli simgesi var.
struct QuickActionsGrid: View {
    @Environment(AppModel.self) private var model
    @Environment(\.selectTab) private var selectTab

    var body: some View {
        let due = model.dueCards().count
        LazyVGrid(columns: [GridItem(.flexible(), spacing: 12), GridItem(.flexible(), spacing: 12)], spacing: 12) {
            tile("Kelime tekrarı", detail: due > 0 ? "\(due) kart bekliyor" : "Bugünlük tamam",
                 icon: "rectangle.stack.fill", color: Theme.accent, badge: due, index: 0) { selectTab(.practice) }
            tile("Oyunlar", detail: "Eşleştir, yarış, yaz", icon: "gamecontroller.fill",
                 color: Theme.warning, index: 1) { selectTab(.practice) }
            tile("Sözlük", detail: "\(model.dictionary.count) kelime", icon: "character.book.closed.fill",
                 color: Theme.color(for: .a2), index: 2) { selectTab(.dictionary) }
            tile("Canlı ders", detail: "Öğretmenle konuşun", icon: "video.fill",
                 color: Theme.color(for: .c2), index: 3) { selectTab(.live) }
        }
    }

    private func tile(_ title: String, detail: String, icon: String, color: Color, badge: Int = 0, index: Int,
                      action: @escaping () -> Void) -> some View {
        Button(action: action) {
            VStack(alignment: .leading, spacing: 12) {
                HStack(alignment: .top) {
                    Image(systemName: icon)
                        .font(.system(size: 19, weight: .bold))
                        .foregroundStyle(.white)
                        .frame(width: 44, height: 44)
                        .background(color.gradient, in: RoundedRectangle(cornerRadius: 13, style: .continuous))
                        .shadow(color: color.opacity(0.35), radius: 6, y: 3)
                    Spacer()
                    if badge > 0 {
                        Text("\(badge)")
                            .font(.jakarta(.caption, weight: .heavy))
                            .foregroundStyle(.white)
                            .padding(.horizontal, 8)
                            .padding(.vertical, 3)
                            .background(Theme.accent, in: Capsule())
                    }
                }
                VStack(alignment: .leading, spacing: 2) {
                    Text(title).font(.jakarta(.headline, weight: .heavy)).foregroundStyle(Theme.ink)
                    Text(detail).font(.jakarta(.caption, weight: .semibold)).foregroundStyle(.secondary).lineLimit(1)
                }
            }
            .frame(maxWidth: .infinity, alignment: .topLeading)
            .card()
        }
        .buttonStyle(PressableCardStyle())
        .staggeredAppear(index)
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
                        .foregroundStyle(Theme.warning)
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
                    .foregroundStyle(.white.opacity(0.8))
                    .fixedSize(horizontal: false, vertical: true)
                if model.isInDeck(sense.card.id) {
                    Label("Destenizde", systemImage: "checkmark.circle.fill")
                        .font(.jakarta(.footnote, weight: .bold))
                        .foregroundStyle(Theme.success)
                } else {
                    Button {
                        withAnimation(Motion.pop) { model.addToDeck(sense.card.id) }
                        Haptics.success()
                    } label: {
                        Label("Kartlarıma ekle", systemImage: "plus")
                    }
                    .buttonStyle(DepthButtonStyle(color: .white, foreground: Theme.ink, height: 44))
                }
            }
            .padding(18)
            .background {
                ZStack(alignment: .topTrailing) {
                    Theme.violetGradient
                    Circle().fill(.white.opacity(0.12)).frame(width: 160).blur(radius: 30).offset(x: 40, y: -40)
                }
                .clipShape(RoundedRectangle(cornerRadius: 24, style: .continuous))
            }
            .contentShape(Rectangle())
            .onTapGesture { withAnimation(Motion.smooth) { revealed.toggle() } }
        }
    }
}

/// Lig ve sıradaki canlı ders: yan yana iki küçük kart.
struct LeagueAndLiveRow: View {
    @Environment(AppModel.self) private var model
    @Environment(LiveSessionStore.self) private var store
    @Environment(\.selectTab) private var selectTab

    var body: some View {
        HStack(alignment: .top, spacing: 12) {
            NavigationLink { LeagueView() } label: {
                VStack(alignment: .leading, spacing: 8) {
                    Image(systemName: "trophy.fill")
                        .font(.system(size: 18, weight: .bold))
                        .foregroundStyle(.white)
                        .frame(width: 38, height: 38)
                        .background(Theme.warning.gradient, in: Circle())
                    Text("Haftalık lig").font(.jakarta(.headline, weight: .heavy)).foregroundStyle(Theme.ink)
                    RollingNumber(value: model.state.progress.weekXP(at: .now), suffix: " XP",
                                  font: .jakarta(.title3, weight: .heavy))
                        .foregroundStyle(Theme.warning)
                    Text("Bu hafta").font(.jakarta(.caption)).foregroundStyle(.secondary)
                }
                .frame(maxWidth: .infinity, minHeight: 150, alignment: .topLeading)
                .card()
            }
            .buttonStyle(PressableCardStyle())

            Button { selectTab(.live) } label: {
                VStack(alignment: .leading, spacing: 8) {
                    HStack(spacing: 6) {
                        LivePulse()
                        Text("Canlı").font(.jakarta(.caption, weight: .heavy)).foregroundStyle(Theme.accent)
                    }
                    .frame(height: 38)
                    if let next = store.sessions.first(where: { $0.startsAt > .now.addingTimeInterval(-3600) }) {
                        Text(next.title).font(.jakarta(.headline, weight: .heavy)).foregroundStyle(Theme.ink).lineLimit(2)
                        Text(next.startsAt.formatted(.relative(presentation: .named)))
                            .font(.jakarta(.subheadline, weight: .bold))
                            .foregroundStyle(Theme.accent)
                        Text(next.teacherName).font(.jakarta(.caption)).foregroundStyle(.secondary)
                    } else if let unit = model.nextLesson?.unit {
                        Text(unit.liveClass.title).font(.jakarta(.headline, weight: .heavy)).foregroundStyle(Theme.ink).lineLimit(2)
                        Text("\(unit.liveClass.durationMinutes) dk · küçük grup").font(.jakarta(.caption)).foregroundStyle(.secondary)
                    } else {
                        Text("Canlı dersler").font(.jakarta(.headline, weight: .heavy)).foregroundStyle(Theme.ink)
                    }
                }
                .frame(maxWidth: .infinity, minHeight: 150, alignment: .topLeading)
                .card()
            }
            .buttonStyle(PressableCardStyle())
        }
    }
}

/// "Canlı" yazısının yanında atan kırmızı nokta.
struct LivePulse: View {
    var color: Color = Theme.accent
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

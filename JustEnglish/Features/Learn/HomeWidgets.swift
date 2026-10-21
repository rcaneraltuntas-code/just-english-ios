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
                            .foregroundStyle(isToday ? Theme.accent : .secondary)
                        Capsule()
                            .fill(isToday ? AnyShapeStyle(Theme.brandGradient)
                                  : reached ? AnyShapeStyle(Theme.accent.opacity(0.55)) : AnyShapeStyle(Theme.accent.opacity(0.14)))
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

/// Dört kısayol: diğer sekmelere tek dokunuşla geçiş.
struct QuickActionsGrid: View {
    @Environment(AppModel.self) private var model
    @Environment(\.selectTab) private var selectTab

    var body: some View {
        let due = model.dueCards().count
        LazyVGrid(columns: [GridItem(.flexible(), spacing: 12), GridItem(.flexible(), spacing: 12)], spacing: 12) {
            tile("Kelime tekrarı", detail: due > 0 ? "\(due) kart bekliyor" : "Bugünlük tamam",
                 icon: "rectangle.stack.fill", gradient: Theme.brandGradient, index: 0) { selectTab(.practice) }
            tile("Oyunlar", detail: "Eşleştir, yarış, yaz", icon: "gamecontroller.fill",
                 gradient: Theme.warmGradient, index: 1) { selectTab(.practice) }
            tile("Sözlük", detail: "\(model.dictionary.count) kelime", icon: "character.book.closed.fill",
                 gradient: LinearGradient(colors: [Theme.color(for: .b2), Theme.color(for: .c1)], startPoint: .topLeading, endPoint: .bottomTrailing),
                 index: 2) { selectTab(.dictionary) }
            tile("Canlı ders", detail: "Öğretmenle konuşun", icon: "video.fill", gradient: Theme.inkGradient, index: 3) { selectTab(.live) }
        }
    }

    private func tile(_ title: String, detail: String, icon: String, gradient: LinearGradient, index: Int,
                      action: @escaping () -> Void) -> some View {
        Button(action: action) {
            VStack(alignment: .leading, spacing: 10) {
                Image(systemName: icon)
                    .font(.system(size: 20, weight: .bold))
                    .foregroundStyle(.white)
                    .frame(width: 42, height: 42)
                    .background(.white.opacity(0.2), in: RoundedRectangle(cornerRadius: 12, style: .continuous))
                    .symbolEffect(.bounce, value: index)
                VStack(alignment: .leading, spacing: 2) {
                    Text(title).font(.jakarta(.headline, weight: .heavy)).foregroundStyle(.white)
                    Text(detail).font(.jakarta(.caption, weight: .semibold)).foregroundStyle(.white.opacity(0.85)).lineLimit(1)
                }
            }
            .padding(14)
            .frame(maxWidth: .infinity, minHeight: 118, alignment: .topLeading)
            .background {
                ZStack(alignment: .bottomTrailing) {
                    gradient
                    Image(systemName: icon)
                        .font(.system(size: 64, weight: .black))
                        .foregroundStyle(.white.opacity(0.12))
                        .rotationEffect(.degrees(-14))
                        .offset(x: 14, y: 12)
                }
                .clipShape(RoundedRectangle(cornerRadius: 20, style: .continuous))
            }
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
                    Theme.inkGradient
                    Circle().fill(Theme.accent.opacity(0.35)).frame(width: 160).blur(radius: 40).offset(x: 40, y: -40)
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

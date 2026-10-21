import SwiftUI
import JECore

/// Kurstaki tüm kelimelerde İngilizce ya da Türkçe arama.
/// Aynı kelime birden fazla ünitede geçiyorsa tek satırda, tüm anlamlarıyla gösterilir.
struct DictionaryView: View {
    @Environment(AppModel.self) private var model
    @State private var query = ""
    @State private var levelFilter: CEFRLevel?
    @FocusState private var searching: Bool

    var body: some View {
        NavigationStack {
            ScrollView {
                VStack(alignment: .leading, spacing: 18) {
                    HeroHeader(title: "Sözlük",
                               subtitle: "\(model.dictionary.count) kelime ve kalıp. İngilizce ya da Türkçe arayın.",
                               gradient: LinearGradient(colors: [Theme.color(for: .a2), Theme.color(for: .c2)], startPoint: .topLeading, endPoint: .bottomTrailing),
                               glow: Theme.color(for: .a2)) {
                        Image(systemName: "character.book.closed.fill")
                            .font(.system(size: 34, weight: .bold))
                            .foregroundStyle(.white)
                            .frame(width: 64, height: 64)
                            .background(.white.opacity(0.18), in: RoundedRectangle(cornerRadius: 18, style: .continuous))
                    } bottom: {
                        searchField
                    }
                    ScrollView(.horizontal, showsIndicators: false) {
                        HStack(spacing: 8) {
                            FilterChip(title: "Tümü", selected: levelFilter == nil) { levelFilter = nil }
                            ForEach(CEFRLevel.allCases) { level in
                                FilterChip(title: level.rawValue, selected: levelFilter == level, color: Theme.color(for: level)) {
                                    levelFilter = levelFilter == level ? nil : level
                                }
                            }
                        }
                        .padding(.horizontal, 20)
                        .padding(.vertical, 4)
                    }
                    .padding(.horizontal, -20)
                    if query.isEmpty && levelFilter == nil {
                        WordOfTheDayCard()
                        SectionHeader(title: "Kelimeler")
                    }
                    if results.isEmpty {
                        JAIEmptyState(title: "Bulunamadı",
                                      message: "\"\(query)\" için bir sonuç yok. Yazımı kontrol edin ya da Türkçesiyle arayın.")
                    } else {
                        LazyVStack(spacing: 10) {
                            ForEach(Array(results.enumerated()), id: \.element.id) { index, entry in
                                NavigationLink(value: entry) { DictionaryRow(entry: entry) }
                                    .buttonStyle(PressableCardStyle())
                                    .staggeredAppear(index, delay: 0.02)
                            }
                        }
                    }
                }
                .padding(20)
                .animation(Motion.smooth, value: levelFilter)
            }
            .tabBarSpacer()
            .scrollDismissesKeyboard(.immediately)
            .background(Theme.background)
            // Kaydırılan içerik saatin altına girmesin diye durum çubuğuna buzlu zemin.
            .safeAreaInset(edge: .top, spacing: 0) {
                Color.clear.frame(height: 0).background(.ultraThinMaterial, ignoresSafeAreaEdges: .top)
            }
            .toolbar(.hidden, for: .navigationBar)
            .navigationDestination(for: DictionaryEntry.self) { DictionaryDetailView(entry: $0) }
        }
    }

    private var searchField: some View {
        HStack(spacing: 10) {
            Image(systemName: "magnifyingglass").font(.jakarta(.headline, weight: .bold)).foregroundStyle(Theme.accent)
            TextField("Kelime arayın", text: $query)
                .font(.jakarta(.body, weight: .semibold))
                .foregroundStyle(Theme.ink)
                .autocorrectionDisabled()
                .textInputAutocapitalization(.never)
                .focused($searching)
                .submitLabel(.search)
            if !query.isEmpty {
                Button {
                    withAnimation(Motion.smooth) { query = "" }
                } label: {
                    Image(systemName: "xmark.circle.fill").foregroundStyle(.secondary)
                }
                .transition(.scale.combined(with: .opacity))
                .accessibilityLabel("Aramayı temizle")
            }
        }
        .padding(.horizontal, 14)
        .frame(height: 50)
        .background(Theme.surface, in: RoundedRectangle(cornerRadius: 16, style: .continuous))
        .scaleEffect(searching ? 1.02 : 1)
        .animation(Motion.pop, value: searching)
        .animation(Motion.smooth, value: query.isEmpty)
    }

    private var results: [DictionaryEntry] {
        let pool = levelFilter.map { level in model.dictionary.filter { $0.senses.contains { $0.level == level } } } ?? model.dictionary
        let q = AnswerChecker.normalize(query).folding(options: .diacriticInsensitive, locale: Locale(identifier: "tr"))
        guard !q.isEmpty else { return Array(pool.prefix(60)) }
        let matches = pool.filter { $0.searchKey.contains(q) }
        // Baştan eşleşenler önce gelir.
        return matches.sorted { a, b in
            let aStarts = a.headword.lowercased().hasPrefix(q), bStarts = b.headword.lowercased().hasPrefix(q)
            if aStarts != bStarts { return aStarts }
            return a.headword.count < b.headword.count
        }
        .prefix(100)
        .map { $0 }
    }
}

struct DictionaryEntry: Identifiable, Hashable {
    let headword: String
    let senses: [Sense]
    let searchKey: String
    var id: String { headword.lowercased() }

    struct Sense: Hashable {
        let card: VocabularyCard
        let unitID: String
        let level: CEFRLevel
        let unitTitle: String
    }

    static func build(from units: [CourseUnit]) -> [DictionaryEntry] {
        var groups: [String: [Sense]] = [:]
        var order: [String] = []
        for unit in units {
            for card in unit.vocabulary {
                let key = card.en.lowercased()
                if groups[key] == nil { order.append(key) }
                groups[key, default: []].append(Sense(card: card, unitID: unit.id, level: unit.level, unitTitle: unit.title))
            }
        }
        return order.compactMap { key in
            guard let senses = groups[key], let first = senses.first else { return nil }
            let text = ([first.card.en] + senses.map(\.card.tr)).joined(separator: " ").lowercased()
            return DictionaryEntry(headword: first.card.en, senses: senses,
                                   searchKey: text.folding(options: .diacriticInsensitive, locale: Locale(identifier: "tr")))
        }
        .sorted { $0.headword.localizedCaseInsensitiveCompare($1.headword) == .orderedAscending }
    }
}

struct DictionaryRow: View {
    let entry: DictionaryEntry

    var body: some View {
        let level = entry.senses.first?.level ?? .a1
        HStack(spacing: 12) {
            RoundedRectangle(cornerRadius: 3, style: .continuous)
                .fill(Theme.color(for: level).gradient)
                .frame(width: 5)
            VStack(alignment: .leading, spacing: 3) {
                Text(entry.headword).font(.jakarta(.headline, weight: .heavy)).foregroundStyle(Theme.ink)
                Text(entry.senses.map(\.card.tr).joined(separator: "; "))
                    .font(.jakarta(.subheadline))
                    .foregroundStyle(.secondary)
                    .lineLimit(1)
            }
            Spacer(minLength: 8)
            LevelBadge(level: level)
            SpeakButton(text: entry.headword)
        }
        .padding(.vertical, 12)
        .padding(.leading, 10)
        .padding(.trailing, 12)
        .background(Theme.surface, in: RoundedRectangle(cornerRadius: 18, style: .continuous))
        .overlay(RoundedRectangle(cornerRadius: 18, style: .continuous).stroke(Theme.hairline, lineWidth: 1))
    }
}

struct DictionaryDetailView: View {
    let entry: DictionaryEntry

    @Environment(AppModel.self) private var model

    var body: some View {
        let level = entry.senses.first?.level ?? .a1
        ScrollView {
            VStack(alignment: .leading, spacing: 16) {
                VStack(alignment: .leading, spacing: 10) {
                    LevelBadge(level: level)
                    HStack(alignment: .center) {
                        Text(entry.headword)
                            .font(.jakarta(.largeTitle, weight: .heavy))
                            .foregroundStyle(.white)
                            .minimumScaleFactor(0.5)
                        Spacer()
                        SpeakButton(text: entry.headword).colorScheme(.dark)
                    }
                    Text(entry.senses.map(\.card.tr).joined(separator: " · "))
                        .font(.jakarta(.title3, weight: .bold))
                        .foregroundStyle(.white.opacity(0.9))
                }
                .padding(20)
                .frame(maxWidth: .infinity, alignment: .leading)
                .background {
                    ZStack {
                        LinearGradient(colors: [Theme.color(for: level), Theme.color(for: level).blended(with: .black, amount: 0.3)],
                                       startPoint: .topLeading, endPoint: .bottomTrailing)
                        WordPattern(words: [entry.headword])
                    }
                    .clipShape(RoundedRectangle(cornerRadius: 26, style: .continuous))
                }
                .shadow(color: Theme.color(for: level).opacity(0.35), radius: 16, y: 8)
                .staggeredAppear(0)
                ForEach(Array(entry.senses.enumerated()), id: \.element.card.id) { index, sense in
                    VStack(alignment: .leading, spacing: 12) {
                        HStack {
                            Text(sense.card.tr).font(.jakarta(.title3, weight: .heavy)).foregroundStyle(Theme.ink)
                            Spacer()
                            LevelBadge(level: sense.level)
                        }
                        HStack(alignment: .top, spacing: 10) {
                            RoundedRectangle(cornerRadius: 2).fill(Theme.accent).frame(width: 3)
                            VStack(alignment: .leading, spacing: 4) {
                                Text(sense.card.example).font(.jakarta(.body, weight: .semibold))
                                Text(sense.card.exampleTr).font(.jakarta(.subheadline)).foregroundStyle(.secondary)
                            }
                            Spacer()
                            SpeakButton(text: sense.card.example)
                        }
                        if let note = sense.card.note, !note.isEmpty {
                            Label(note, systemImage: "lightbulb.fill")
                                .font(.jakarta(.footnote, weight: .semibold))
                                .foregroundStyle(Theme.warning)
                        }
                        Label("\(sense.level.rawValue) · \(sense.unitTitle)", systemImage: "book.closed.fill")
                            .font(.jakarta(.caption, weight: .semibold))
                            .foregroundStyle(.secondary)
                        deckButton(sense.card)
                    }
                    .card()
                    .staggeredAppear(index + 1)
                }
            }
            .padding(20)
        }
        .tabBarSpacer()
        .background(Theme.background)
        .navigationBarTitleDisplayMode(.inline)
    }

    @ViewBuilder private func deckButton(_ card: VocabularyCard) -> some View {
        if model.isInDeck(card.id) {
            Label("Destenizde", systemImage: "checkmark.circle.fill")
                .font(.jakarta(.footnote, weight: .semibold))
                .foregroundStyle(Theme.success)
        } else {
            Button {
                withAnimation(Motion.pop) { model.addToDeck(card.id) }
                Haptics.success()
            } label: {
                Label("Kartlarıma ekle", systemImage: "plus")
            }
            .buttonStyle(DepthButtonStyle(height: 44))
        }
    }
}

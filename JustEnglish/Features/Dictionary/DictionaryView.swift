import SwiftUI
import JECore

/// Kurstaki tüm kelimelerde İngilizce ya da Türkçe arama.
/// Aynı kelime birden fazla ünitede geçiyorsa tek satırda, tüm anlamlarıyla gösterilir.
struct DictionaryView: View {
    @Environment(AppModel.self) private var model
    @State private var query = ""

    var body: some View {
        NavigationStack {
            List {
                if query.isEmpty {
                    Section {
                        Text("\(model.dictionary.count) kelime ve kalıp. İngilizce ya da Türkçe arayın.")
                            .font(.jakarta(.subheadline))
                            .foregroundStyle(.secondary)
                    }
                }
                ForEach(results) { entry in
                    NavigationLink(value: entry) { DictionaryRow(entry: entry) }
                }
            }
            .listStyle(.insetGrouped)
            .searchable(text: $query, placement: .navigationBarDrawer(displayMode: .always), prompt: "Kelime ara")
            .autocorrectionDisabled()
            .textInputAutocapitalization(.never)
            .navigationTitle("Sözlük")
            .navigationDestination(for: DictionaryEntry.self) { DictionaryDetailView(entry: $0) }
            .overlay {
                if !query.isEmpty && results.isEmpty {
                    ContentUnavailableView.search(text: query)
                }
            }
        }
    }

    private var results: [DictionaryEntry] {
        let q = AnswerChecker.normalize(query).folding(options: .diacriticInsensitive, locale: Locale(identifier: "tr"))
        guard !q.isEmpty else { return Array(model.dictionary.prefix(50)) }
        let matches = model.dictionary.filter { $0.searchKey.contains(q) }
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
        HStack {
            VStack(alignment: .leading, spacing: 2) {
                Text(entry.headword).font(.jakarta(.headline))
                Text(entry.senses.map(\.card.tr).joined(separator: "; "))
                    .font(.jakarta(.subheadline))
                    .foregroundStyle(.secondary)
                    .lineLimit(1)
            }
            Spacer()
            if let level = entry.senses.first?.level { LevelBadge(level: level) }
        }
    }
}

struct DictionaryDetailView: View {
    let entry: DictionaryEntry

    @Environment(AppModel.self) private var model

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 16) {
                HStack {
                    Text(entry.headword).font(.jakarta(.largeTitle, weight: .bold))
                    Spacer()
                    SpeakButton(text: entry.headword)
                }
                ForEach(entry.senses, id: \.card.id) { sense in
                    VStack(alignment: .leading, spacing: 10) {
                        HStack {
                            Text(sense.card.tr).font(.jakarta(.title3, weight: .bold))
                            Spacer()
                            LevelBadge(level: sense.level)
                        }
                        HStack(alignment: .top) {
                            VStack(alignment: .leading, spacing: 4) {
                                Text(sense.card.example).font(.jakarta(.body, weight: .medium))
                                Text(sense.card.exampleTr).font(.jakarta(.subheadline)).foregroundStyle(.secondary)
                            }
                            Spacer()
                            SpeakButton(text: sense.card.example)
                        }
                        if let note = sense.card.note, !note.isEmpty {
                            Text(note).font(.jakarta(.footnote)).foregroundStyle(Theme.warning)
                        }
                        Text("\(sense.level.rawValue) · \(sense.unitTitle)").font(.jakarta(.caption)).foregroundStyle(.secondary)
                        deckButton(sense.card)
                    }
                    .card()
                }
            }
            .padding(20)
        }
        .background(Theme.background)
        .navigationBarTitleDisplayMode(.inline)
    }

    @ViewBuilder private func deckButton(_ card: VocabularyCard) -> some View {
        if model.isInDeck(card.id) {
            Label("Destenizde", systemImage: "checkmark.circle.fill")
                .font(.jakarta(.footnote, weight: .semibold))
                .foregroundStyle(Theme.success)
        } else {
            Button { model.addToDeck(card.id) } label: {
                Label("Kartlarıma ekle", systemImage: "plus.circle.fill").font(.jakarta(.footnote, weight: .semibold))
            }
        }
    }
}

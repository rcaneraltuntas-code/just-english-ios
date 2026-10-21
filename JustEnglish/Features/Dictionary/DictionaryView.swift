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
                VStack(alignment: .leading, spacing: 0) {
                    header
                    VStack(alignment: .leading, spacing: 18) {
                        levelChips
                        if query.isEmpty && levelFilter == nil {
                            WordOfTheDayCard()
                            Text("Kelimeler")
                                .font(.custom(Theme.fontFamily, size: 20, relativeTo: .title3).weight(.bold))
                                .foregroundStyle(HomeStyle.title)
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
                    .padding(.horizontal, 16)
                    .padding(.top, 18)
                    .padding(.bottom, 20)
                }
                .animation(Motion.smooth, value: levelFilter)
            }
            .tabBarSpacer()
            .scrollDismissesKeyboard(.immediately)
            .background(Theme.surface.ignoresSafeArea())
            .toolbar(.hidden, for: .navigationBar)
            .navigationDestination(for: DictionaryEntry.self) { DictionaryDetailView(entry: $0) }
        }
    }

    /// Üst bant (JAI sohbetiyle aynı): açık mavi degrade, düz alt kenar; başlık, kelime sayısı ve arama alanı.
    private var header: some View {
        VStack(alignment: .leading, spacing: 6) {
            HStack(spacing: 12) {
                Image("lesson-book").resizable().scaledToFit().frame(width: 40, height: 40)
                VStack(alignment: .leading, spacing: 2) {
                    Text("Sözlük")
                        .font(.custom(Theme.fontFamily, size: 26, relativeTo: .title).weight(.bold))
                        .foregroundStyle(Theme.ink)
                    Text("\(model.dictionary.count) kelime ve kalıp")
                        .font(.custom(Theme.fontFamily, size: 15, relativeTo: .subheadline))
                        .foregroundStyle(HomeStyle.body)
                }
            }
            searchField.padding(.top, 14)
        }
        .padding(.horizontal, 16)
        .padding(.top, 22)
        .padding(.bottom, 20)
        .frame(maxWidth: .infinity, alignment: .leading)
        .background {
            LinearGradient(colors: [Color(light: 0xDCE7FF, dark: 0x1C2850), Color(light: 0xEAF1FF, dark: 0x151C38)],
                           startPoint: .top, endPoint: .bottom)
                .ignoresSafeArea(edges: .top)
        }
    }

    /// Seviye süzgeci: seçili olan vurgu renginde, diğerleri açık gri kapsül.
    private var levelChips: some View {
        ScrollView(.horizontal, showsIndicators: false) {
            HStack(spacing: 8) {
                chip("Tümü", selected: levelFilter == nil) { levelFilter = nil }
                ForEach(CEFRLevel.allCases) { level in
                    chip(level.rawValue, selected: levelFilter == level) {
                        levelFilter = levelFilter == level ? nil : level
                    }
                }
            }
            .padding(.horizontal, 16)
            .padding(.vertical, 2)
        }
        .padding(.horizontal, -16)
    }

    private func chip(_ title: String, selected: Bool, action: @escaping () -> Void) -> some View {
        Button {
            Haptics.tap()
            withAnimation(Motion.smooth) { action() }
        } label: {
            Text(title)
                .font(.custom(Theme.fontFamily, size: 15, relativeTo: .subheadline).weight(.semibold))
                .foregroundStyle(selected ? .white : HomeStyle.title)
                .padding(.horizontal, 16)
                .frame(height: 36)
                .background(selected ? Theme.accent : HomeStyle.rowFill, in: Capsule())
        }
        .buttonStyle(PressableCardStyle())
        .accessibilityAddTraits(selected ? .isSelected : [])
    }

    private var searchField: some View {
        HStack(spacing: 10) {
            Image(systemName: "magnifyingglass").font(.system(size: 17, weight: .medium)).foregroundStyle(HomeStyle.body)
            TextField("İngilizce ya da Türkçe arayın", text: $query)
                .font(.custom(Theme.fontFamily, size: 17, relativeTo: .body))
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
        .background(Theme.surface, in: RoundedRectangle(cornerRadius: 14, style: .continuous))
        .overlay(RoundedRectangle(cornerRadius: 14, style: .continuous)
            .stroke(searching ? Theme.accent : HomeStyle.cardBorder, lineWidth: searching ? 2 : 1.5))
        .animation(Motion.smooth, value: searching)
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

/// Sözlük satırı (ana sayfadaki "Akıcılığa giden yol" satırları gibi): açık gri zemin, kelime, Türkçesi, seviye ve hoparlör.
struct DictionaryRow: View {
    let entry: DictionaryEntry

    var body: some View {
        let level = entry.senses.first?.level ?? .a1
        HStack(spacing: 12) {
            VStack(alignment: .leading, spacing: 3) {
                Text(entry.headword)
                    .font(.custom(Theme.fontFamily, size: 17, relativeTo: .headline).weight(.semibold))
                    .foregroundStyle(HomeStyle.title)
                Text(entry.senses.map(\.card.tr).joined(separator: "; "))
                    .font(.custom(Theme.fontFamily, size: 15, relativeTo: .subheadline))
                    .foregroundStyle(HomeStyle.body)
                    .lineLimit(1)
            }
            Spacer(minLength: 8)
            LevelBadge(level: level)
            SpeakButton(text: entry.headword)
        }
        .padding(.vertical, 12)
        .padding(.leading, 16)
        .padding(.trailing, 10)
        .frame(minHeight: 64)
        .background(HomeStyle.rowFill, in: RoundedRectangle(cornerRadius: 16, style: .continuous))
    }
}

struct DictionaryDetailView: View {
    let entry: DictionaryEntry

    @Environment(AppModel.self) private var model

    var body: some View {
        let level = entry.senses.first?.level ?? .a1
        ScrollView {
            VStack(alignment: .leading, spacing: 14) {
                // Başlık: açık mavi bantta büyük kelime, Türkçesi ve hoparlör.
                VStack(alignment: .leading, spacing: 8) {
                    LevelBadge(level: level)
                    HStack(alignment: .center, spacing: 12) {
                        Text(entry.headword)
                            .font(.custom(Theme.fontFamily, size: 34, relativeTo: .largeTitle).weight(.bold))
                            .foregroundStyle(Theme.ink)
                            .minimumScaleFactor(0.5)
                            .lineLimit(1)
                        Spacer()
                        SpeakButton(text: entry.headword)
                    }
                    Text(entry.senses.map(\.card.tr).joined(separator: " · "))
                        .font(.custom(Theme.fontFamily, size: 18, relativeTo: .title3).weight(.medium))
                        .foregroundStyle(HomeStyle.body)
                }
                .padding(20)
                .frame(maxWidth: .infinity, alignment: .leading)
                .background(Color(light: 0xEAF1FF, dark: 0x151C38), in: RoundedRectangle(cornerRadius: 18, style: .continuous))
                .staggeredAppear(0)
                ForEach(Array(entry.senses.enumerated()), id: \.element.card.id) { index, sense in
                    VStack(alignment: .leading, spacing: 12) {
                        HStack {
                            Text(sense.card.tr)
                                .font(.custom(Theme.fontFamily, size: 19, relativeTo: .title3).weight(.bold))
                                .foregroundStyle(HomeStyle.title)
                            Spacer()
                            LevelBadge(level: sense.level)
                        }
                        HStack(alignment: .top, spacing: 10) {
                            RoundedRectangle(cornerRadius: 2).fill(Theme.accent).frame(width: 3)
                            VStack(alignment: .leading, spacing: 4) {
                                Text(sense.card.example)
                                    .font(.custom(Theme.fontFamily, size: 16, relativeTo: .body).weight(.medium))
                                    .foregroundStyle(Theme.ink)
                                Text(sense.card.exampleTr)
                                    .font(.custom(Theme.fontFamily, size: 15, relativeTo: .subheadline))
                                    .foregroundStyle(HomeStyle.body)
                            }
                            Spacer()
                            SpeakButton(text: sense.card.example)
                        }
                        if let note = sense.card.note, !note.isEmpty {
                            Label(note, systemImage: "lightbulb.fill")
                                .font(.custom(Theme.fontFamily, size: 14, relativeTo: .footnote).weight(.medium))
                                .foregroundStyle(Color(light: 0xB7791F, dark: 0xFBBF24))
                        }
                        Label("\(sense.level.rawValue) · \(sense.unitTitle)", systemImage: "book.closed")
                            .font(.custom(Theme.fontFamily, size: 13, relativeTo: .caption))
                            .foregroundStyle(HomeStyle.body)
                        deckButton(sense.card)
                    }
                    .padding(16)
                    .modifier(HomeCard())
                    .staggeredAppear(index + 1)
                }
            }
            .padding(16)
        }
        .tabBarSpacer()
        .background(Theme.surface.ignoresSafeArea())
        .navigationBarTitleDisplayMode(.inline)
    }

    @ViewBuilder private func deckButton(_ card: VocabularyCard) -> some View {
        if model.isInDeck(card.id) {
            Label("Destenizde", systemImage: "checkmark.circle.fill")
                .font(.custom(Theme.fontFamily, size: 15, relativeTo: .footnote).weight(.semibold))
                .foregroundStyle(Theme.success)
        } else {
            Button {
                withAnimation(Motion.pop) { model.addToDeck(card.id) }
                Haptics.success()
            } label: {
                Label("Kartlarıma ekle", systemImage: "plus")
            }
            .buttonStyle(OnboardingButtonStyle(filled: true))
        }
    }
}

import SwiftUI
import JECore

struct UnitView: View {
    let unit: CourseUnit

    @Environment(AppModel.self) private var model
    @Environment(\.dismiss) private var dismiss
    @Environment(\.selectTab) private var selectTab
    @State private var activeLesson: LessonRoute?
    @State private var showTest = false
    @State private var showInfo = false
    /// Bilgi sayfasından teste geçilirken test, sayfa kapandıktan sonra açılır.
    @State private var testAfterInfo = false

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 20) {
                topBar
                // Referanstaki seviye kartı: açık gri zemin, küçük gri üst satır, kalın ünite adı, sağda 🔥 ve ⭐ sayaçları.
                HStack(alignment: .center) {
                    VStack(alignment: .leading, spacing: 4) {
                        Text("ÜNİTE \(unit.number) · \(unit.level.rawValue)")
                            .font(.custom(Theme.fontFamily, size: 13, relativeTo: .footnote))
                            .tracking(0.8)
                            .foregroundStyle(Color(light: 0x6B7385, dark: 0x9AA3B5))
                        Text(unit.title)
                            .font(.custom(Theme.fontFamily, size: 20, relativeTo: .title3).weight(.bold))
                            .foregroundStyle(Color(light: 0x3C4250, dark: 0xE6E9F0))
                    }
                    Spacer()
                    HStack(spacing: 14) {
                        Text("🔥 \(model.state.progress.displayedStreak(at: .now))")
                        Text("⭐ \(model.state.progress.totalXP)")
                    }
                    .font(.jakarta(.headline, weight: .semibold))
                    .foregroundStyle(Theme.ink.opacity(0.75))
                }
                .padding(.horizontal, 18)
                .frame(height: 74)
                .background(Color(light: 0xF3F4F6, dark: 0x1D2233), in: RoundedRectangle(cornerRadius: 14, style: .continuous))
                .padding(.horizontal, -3)
                .padding(.bottom, -7)
                .staggeredAppear(0)

                LessonPathView(unit: unit) { lesson in
                    activeLesson = LessonRoute(unit: unit, lesson: lesson)
                } onTest: {
                    showTest = true
                }
            }
            .padding(.horizontal, 20)
            .padding(.top, 20)
        }
        .tabBarSpacer()
        // Referanstaki gibi düz beyaz sayfa; gezinme çubuğu yerine kendi üst satırımız.
        .background(Theme.surface.ignoresSafeArea())
        .toolbar(.hidden, for: .navigationBar)
        .fullScreenCover(item: $activeLesson) { LessonFlowView(unit: $0.unit, lesson: $0.lesson) }
        .fullScreenCover(isPresented: $showTest) { UnitTestView(unit: unit) }
        .sheet(isPresented: $showInfo, onDismiss: {
            if testAfterInfo { testAfterInfo = false; showTest = true }
        }) { infoSheet }
    }

    /// Bilgi simgesinin açtığı sayfa: ünitenin hedefi, konular, ünite testi, canlı ders ve kelimeler.
    /// Ana ekran referanstaki gibi yalnızca başlık kartı ve yoldan oluşur.
    private var infoSheet: some View {
        NavigationStack {
            ScrollView {
                VStack(alignment: .leading, spacing: 20) {
                    VStack(alignment: .leading, spacing: 10) {
                        SectionHeader(title: "Bu ünitede")
                        Text(unit.canDo).font(.jakarta(.subheadline, weight: .medium)).foregroundStyle(.secondary)
                        if !unit.grammar.isEmpty {
                            FlowLayout(spacing: 6) {
                                ForEach(unit.grammar, id: \.self) { tag($0, color: Theme.accent) }
                                ForEach(unit.vocabularyThemes, id: \.self) { tag($0, color: Theme.color(for: unit.level)) }
                            }
                        }
                    }
                    .card()

                    SectionTitle(text: "Ünite testi")
                    Button { testAfterInfo = true; showInfo = false } label: {
                        HStack(spacing: 14) {
                            Image(systemName: model.isUnitPassed(unit) ? "checkmark.seal.fill" : "doc.text.fill")
                                .font(.title2)
                                .foregroundStyle(model.isUnitPassed(unit) ? Theme.success : Theme.accent)
                            VStack(alignment: .leading, spacing: 3) {
                                Text("\(unit.unitTest.questions.count) soru · geçme notu %\(unit.unitTest.passPercent)")
                                    .font(.jakarta(.headline))
                                if let best = model.state.unitTestScores[unit.id] {
                                    Text("En iyi sonucunuz: %\(best)").font(.jakarta(.footnote)).foregroundStyle(.secondary)
                                } else {
                                    Text("Tüm dersleri bitirdikten sonra önerilir.").font(.jakarta(.footnote)).foregroundStyle(.secondary)
                                }
                            }
                            Spacer()
                            Image(systemName: "chevron.right").foregroundStyle(.tertiary)
                        }
                        .card()
                    }
                    .buttonStyle(.plain)

                    SectionTitle(text: "Canlı ders")
                    LiveClassCard(unit: unit)

                    SectionTitle(text: "Kelimeler (\(unit.vocabulary.count))")
                    VStack(spacing: 0) {
                        ForEach(unit.vocabulary) { card in
                            VocabularyRow(card: card)
                            if card.id != unit.vocabulary.last?.id { Divider() }
                        }
                    }
                    .card()
                }
                .padding(20)
            }
            .background(Theme.background.ignoresSafeArea())
            .navigationTitle("Ünite \(unit.number): \(unit.title)")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .confirmationAction) {
                    Button("Kapat") { showInfo = false }
                }
            }
        }
        .presentationDetents([.large])
    }

    /// Üst satır: geri, büyük kalın başlık, zil ve bayrak (referanstaki "Scenarios" satırı).
    private var topBar: some View {
        HStack(spacing: 12) {
            Button { dismiss() } label: {
                Image(systemName: "chevron.left")
                    .font(.system(size: 17, weight: .semibold))
                    .foregroundStyle(.secondary)
                    .frame(width: 24, height: 36, alignment: .leading)
            }
            .accessibilityLabel("Geri")
            Text("Ünite \(unit.number)")
                .font(.custom(Theme.fontFamily, size: 22, relativeTo: .title2).weight(.bold))
                .foregroundStyle(Theme.ink)
            Spacer()
            Button { showInfo = true } label: {
                Image(systemName: "info.circle")
                    .font(.system(size: 21, weight: .regular))
                    .foregroundStyle(Theme.ink)
            }
            .accessibilityLabel("Ünite bilgisi, test ve kelimeler")
            Button { selectTab(.practice) } label: {
                Image(systemName: "bell")
                    .font(.system(size: 21, weight: .regular))
                    .foregroundStyle(Theme.ink)
            }
            .accessibilityLabel("Bildirimler")
            Text("🇬🇧")
                .font(.system(size: 22))
                .frame(width: 30, height: 30)
                .background(Theme.surfaceRaised, in: Circle())
                .clipShape(Circle())
                .accessibilityLabel("Öğrenilen dil: İngilizce")
        }
        .padding(.top, 4)
    }

    private func tag(_ text: String, color: Color) -> some View {
        Text(text)
            .font(.jakarta(.caption, weight: .semibold))
            .padding(.horizontal, 10)
            .padding(.vertical, 5)
            .foregroundStyle(color)
            .background(color.opacity(0.12), in: Capsule())
    }
}

struct LessonRow: View {
    let lesson: Lesson
    let done: Bool
    let score: Int?

    var body: some View {
        HStack(spacing: 14) {
            Image(systemName: done ? "checkmark.circle.fill" : "\(lesson.number).circle")
                .font(.title2)
                .foregroundStyle(done ? Theme.success : Theme.accent)
            VStack(alignment: .leading, spacing: 3) {
                Text(lesson.title).font(.jakarta(.headline))
                Text(lesson.goal).font(.jakarta(.footnote)).foregroundStyle(.secondary).lineLimit(2)
            }
            Spacer()
            if let score { Text("%\(score)").font(.jakarta(.footnote, weight: .bold)).foregroundStyle(.secondary) }
        }
        .card()
    }
}

struct VocabularyRow: View {
    let card: VocabularyCard

    var body: some View {
        HStack(alignment: .top, spacing: 12) {
            VStack(alignment: .leading, spacing: 3) {
                HStack(alignment: .firstTextBaseline) {
                    Text(card.en).font(.jakarta(.headline))
                    Text(card.tr).font(.jakarta(.subheadline)).foregroundStyle(.secondary)
                }
                Text(card.example).font(.jakarta(.footnote)).foregroundStyle(.secondary)
            }
            Spacer()
            SpeakButton(text: card.en)
        }
        .padding(.vertical, 8)
    }
}

/// Simge ile sayı arasında az boşluklu etiket (sayaçlar için).
struct TightLabelStyle: LabelStyle {
    func makeBody(configuration: Configuration) -> some View {
        HStack(spacing: 4) { configuration.icon; configuration.title.foregroundStyle(Theme.ink) }
    }
}

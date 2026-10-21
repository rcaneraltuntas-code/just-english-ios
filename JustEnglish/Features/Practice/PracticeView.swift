import SwiftUI
import JECore

/// Pratik sekmesi: aralıklı tekrar, yanlışları tekrar ve kelime oyunları.
struct PracticeView: View {
    @Environment(AppModel.self) private var model
    @State private var session: PracticeSession?

    enum PracticeSession: String, Identifiable {
        case review, mistakes, matchRace, speedQuiz, spelling
        var id: String { rawValue }
    }

    var body: some View {
        NavigationStack {
            ScrollView {
                VStack(spacing: 16) {
                    reviewCard
                    if !model.state.mistakes.isEmpty {
                        tile(icon: "arrow.uturn.backward.circle.fill", color: Theme.danger,
                             title: "Yanlışlarım", detail: "\(model.state.mistakes.count) soruyu tekrar çözün") {
                            session = .mistakes
                        }
                    }
                    SectionTitle(text: "Oyunlar").padding(.top, 8)
                    tile(icon: "bolt.fill", color: Theme.warning, title: "Eşleştirme yarışı",
                         detail: "Kelimeleri anlamlarıyla olabildiğince hızlı eşleştirin.") { session = .matchRace }
                    tile(icon: "timer", color: Theme.color(for: .b1), title: "60 saniye",
                         detail: "Süre bitmeden kaç kelimenin anlamını bilebilirsiniz?") { session = .speedQuiz }
                    tile(icon: "ear.fill", color: Theme.success, title: "Dinle ve yaz",
                         detail: "Duyduğunuz kelimeyi doğru yazın.") { session = .spelling }
                    if model.gamePool.count < GameRules.minimumCards {
                        Text("Oyunlar, çalıştığınız ünitelerin kelimeleriyle oynanır. Önce birkaç ders tamamlayın.")
                            .font(.jakarta(.footnote))
                            .foregroundStyle(.secondary)
                    }
                }
                .padding(20)
            }
            .tabBarSpacer()
            .appBackground()
            .navigationTitle("Pratik")
            .fullScreenCover(item: $session) { session in
                switch session {
                case .review: FlashcardSessionView(cards: model.dueCards())
                case .mistakes: MistakesSessionView(exercises: model.mistakeExercises())
                case .matchRace: MatchRaceGame(pool: model.gamePool)
                case .speedQuiz: SpeedQuizGame(pool: model.gamePool)
                case .spelling: SpellingGame(pool: model.gamePool)
                }
            }
        }
    }

    private var reviewCard: some View {
        let due = model.dueCards().count
        return VStack(alignment: .leading, spacing: 12) {
            Label("Kelime kartları", systemImage: "rectangle.stack.fill")
                .font(.jakarta(.headline))
                .foregroundStyle(.white)
            Text(due > 0 ? "\(due) kart sizi bekliyor" : "Bugünlük tekrar yok")
                .contentTransition(.numericText())
                .font(.jakarta(.title2, weight: .bold))
                .foregroundStyle(.white)
            Text("Destede \(model.deckSize) kelime var. Kartlar, unutmak üzere olduğunuz anda yeniden karşınıza çıkar.")
                .font(.jakarta(.subheadline))
                .foregroundStyle(.white.opacity(0.9))
            Button(due > 0 ? "Tekrara başla" : "Kart yok") { session = .review }
                .buttonStyle(DepthButtonStyle(color: .white, foreground: Theme.accent))
                .disabled(due == 0)
        }
        .padding(18)
        .background {
            ZStack(alignment: .topTrailing) {
                Theme.violetGradient
                Image(systemName: "rectangle.stack.fill")
                    .font(.system(size: 110, weight: .black))
                    .foregroundStyle(.white.opacity(0.12))
                    .rotationEffect(.degrees(12))
                    .offset(x: 24, y: -6)
            }
            .clipShape(RoundedRectangle(cornerRadius: 22, style: .continuous))
        }
        .shadow(color: Theme.accent.opacity(0.3), radius: 14, y: 8)
    }

    private func tile(icon: String, color: Color, title: String, detail: String, action: @escaping () -> Void) -> some View {
        Button(action: action) {
            HStack(spacing: 14) {
                Image(systemName: icon)
                    .font(.title2)
                    .foregroundStyle(.white)
                    .frame(width: 48, height: 48)
                    .background(color, in: RoundedRectangle(cornerRadius: 12))
                VStack(alignment: .leading, spacing: 3) {
                    Text(title).font(.jakarta(.headline))
                    Text(detail).font(.jakarta(.footnote)).foregroundStyle(.secondary)
                }
                Spacer()
                Image(systemName: "chevron.right").foregroundStyle(.tertiary)
            }
            .card()
        }
        .buttonStyle(PressableCardStyle())
        .disabled(title != "Yanlışlarım" && model.gamePool.count < GameRules.minimumCards)
    }
}

// MARK: - Aralıklı tekrar oturumu

struct FlashcardSessionView: View {
    /// Oturum başındaki kartlar sabitlenir; tekrar sırasında model değişse de liste kaymaz.
    @State private var cards: [VocabularyCard]

    init(cards: [VocabularyCard]) {
        _cards = State(initialValue: cards)
    }

    @Environment(AppModel.self) private var model
    @Environment(\.dismiss) private var dismiss
    @State private var position = 0
    @State private var flipped = false
    @State private var remembered = 0

    var body: some View {
        VStack(spacing: 20) {
            HStack(spacing: 14) {
                Button { dismiss() } label: { Image(systemName: "xmark").font(.jakarta(.headline, weight: .bold)) }
                    .foregroundStyle(.secondary)
                ProgressBar(value: Double(position) / Double(max(cards.count, 1)), height: 10)
            }
            if position < cards.count {
                Spacer()
                FlipCard(card: cards[position], flipped: $flipped).id(position)
                Spacer()
                if flipped {
                    Text("Ne kadar iyi hatırladınız?").font(.jakarta(.subheadline)).foregroundStyle(.secondary)
                    HStack(spacing: 8) {
                        rate(.again, "Hiç", Theme.danger)
                        rate(.hard, "Zor", Theme.warning)
                        rate(.good, "İyi", Theme.success)
                        rate(.easy, "Kolay", Theme.accent)
                    }
                } else {
                    Button("Cevabı göster") { withAnimation(.spring) { flipped = true } }.buttonStyle(.primary)
                }
            } else {
                Spacer()
                Image(systemName: "checkmark.seal.fill").font(.system(size: 80)).foregroundStyle(Theme.success)
                Text("Tekrar bitti!").font(.jakarta(.title, weight: .bold))
                Text("\(cards.count) kartın \(remembered) tanesini hatırladınız.")
                    .font(.jakarta(.body)).foregroundStyle(.secondary)
                Spacer()
                Button("Bitir") { dismiss() }.buttonStyle(.primary)
            }
        }
        .padding(20)
        .appBackground()
    }

    private func rate(_ rating: ReviewRating, _ title: String, _ color: Color) -> some View {
        Button(title) {
            model.review(cardID: cards[position].id, rating: rating)
            if rating != .again { remembered += 1 }
            flipped = false
            position += 1
        }
        .buttonStyle(PrimaryButtonStyle(color: color))
    }
}

// MARK: - Yanlışları tekrar

struct MistakesSessionView: View {
    @State private var exercises: [Exercise]

    init(exercises: [Exercise]) {
        _exercises = State(initialValue: exercises)
    }

    @Environment(AppModel.self) private var model
    @Environment(\.dismiss) private var dismiss
    @State private var index = 0
    @State private var fixed = 0

    var body: some View {
        VStack(spacing: 0) {
            HStack(spacing: 14) {
                Button { dismiss() } label: { Image(systemName: "xmark").font(.jakarta(.headline, weight: .bold)) }
                    .foregroundStyle(.secondary)
                ProgressBar(value: Double(index) / Double(max(exercises.count, 1)), height: 10)
            }
            .padding(.horizontal, 20)
            .padding(.vertical, 12)
            if index < exercises.count {
                ExerciseView(exercise: exercises[index]) { outcome in
                    if let correct = outcome.correct {
                        model.recordAnswer(exerciseID: exercises[index].id, correct: correct)
                        if correct { fixed += 1 }
                    }
                    index += 1
                }
                .id(index)
            } else {
                Spacer()
                Image(systemName: "arrow.uturn.backward.circle.fill").font(.system(size: 80)).foregroundStyle(Theme.success)
                Text("\(fixed) yanlışı düzelttiniz").font(.jakarta(.title2, weight: .bold)).padding(.top, 12)
                Spacer()
                Button("Bitir") { dismiss() }.buttonStyle(.primary).padding(20)
            }
        }
        .appBackground()
    }
}

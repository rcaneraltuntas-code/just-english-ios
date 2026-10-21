import SwiftUI
import JECore

/// Önde İngilizce kelime, arkada Türkçe anlam ve örnek cümle.
struct FlipCard: View {
    let card: VocabularyCard
    @Binding var flipped: Bool

    var body: some View {
        ZStack {
            face {
                VStack(spacing: 16) {
                    Text(card.en)
                        .font(.jakarta(.largeTitle, weight: .bold))
                        .multilineTextAlignment(.center)
                        .minimumScaleFactor(0.5)
                    SpeakButton(text: card.en)
                }
            }
            .opacity(flipped ? 0 : 1)

            face {
                VStack(spacing: 14) {
                    Text(card.tr)
                        .font(.jakarta(.title, weight: .bold))
                        .multilineTextAlignment(.center)
                        .minimumScaleFactor(0.5)
                    Divider()
                    HStack(alignment: .top) {
                        VStack(alignment: .leading, spacing: 4) {
                            Text(card.example).font(.jakarta(.body, weight: .medium))
                            Text(card.exampleTr).font(.jakarta(.subheadline)).foregroundStyle(.secondary)
                        }
                        Spacer(minLength: 8)
                        SpeakButton(text: card.example)
                    }
                    if let note = card.note, !note.isEmpty {
                        Text(note)
                            .font(.jakarta(.footnote))
                            .foregroundStyle(Theme.warning)
                            .frame(maxWidth: .infinity, alignment: .leading)
                    }
                }
            }
            .rotation3DEffect(.degrees(180), axis: (0, 1, 0))
            .opacity(flipped ? 1 : 0)
        }
        .rotation3DEffect(.degrees(flipped ? 180 : 0), axis: (0, 1, 0))
        .onTapGesture { withAnimation(.spring(duration: 0.4)) { flipped.toggle() } }
        .onAppear { if !flipped { Speech.shared.speak(card.en) } }
        .accessibilityAction(named: "Çevir") { flipped.toggle() }
    }

    private func face<Content: View>(@ViewBuilder _ content: () -> Content) -> some View {
        content()
            .padding(24)
            .frame(maxWidth: .infinity, minHeight: 300)
            .background(Theme.surface, in: RoundedRectangle(cornerRadius: 24))
            .shadow(color: .black.opacity(0.08), radius: 12, y: 6)
    }
}

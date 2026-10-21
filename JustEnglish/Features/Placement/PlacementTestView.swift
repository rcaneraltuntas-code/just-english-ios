import SwiftUI
import JECore

/// Uyarlanabilir seviye testi. Sorular 4'lük bloklar halinde gelir; motor her bloktan sonra seviyeyi yukarı
/// ya da aşağı taşır. Öğrenciye tek tek soru gösterilir ve anında doğru/yanlış söylenmez.
struct PlacementTestView: View {
    let onFinish: (PlacementResult) -> Void
    var onCancel: (() -> Void)?

    @Environment(AppModel.self) private var model
    @State private var engine: PlacementEngine?
    @State private var position = 0
    @State private var chosen: [String: Int] = [:]
    @State private var answered = 0

    var body: some View {
        VStack(spacing: 0) {
            HStack(spacing: 14) {
                if let onCancel {
                    Button(action: onCancel) { Image(systemName: "xmark").font(.jakarta(.headline, weight: .bold)) }
                        .foregroundStyle(.secondary)
                }
                // En fazla 7 blok sorulur; ilerleme bu üst sınıra göre gösterilir.
                ProgressBar(value: Double(answered) / Double(PlacementEngine.blockSize * PlacementEngine.maxBlocks), height: 10)
            }
            .padding(.horizontal, 20)
            .padding(.vertical, 12)

            if let engine {
                if let result = engine.result {
                    PlacementResultView(result: result) { onFinish(result) }
                } else if position < engine.currentBlock.count {
                    question(engine.currentBlock[position])
                        .id(engine.currentBlock[position].id)
                        .transition(.asymmetric(insertion: .move(edge: .trailing), removal: .move(edge: .leading)))
                }
            } else {
                Spacer()
                ProgressView()
                Spacer()
            }
        }
        .animation(.snappy, value: answered)
        .background(Theme.background)
        .onAppear {
            if engine == nil, let items = model.library?.placement { engine = PlacementEngine(items: items) }
        }
    }

    private func question(_ item: PlacementItem) -> some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 18) {
                Text(item.skill.turkishName)
                    .font(.jakarta(.caption, weight: .bold))
                    .foregroundStyle(Theme.accent)
                    .textCase(.uppercase)
                if let passage = item.passage {
                    Text(passage).font(.jakarta(.body)).lineSpacing(4).card()
                }
                Text(item.prompt).font(.jakarta(.title3, weight: .semibold))
                ForEach(Array(item.options.enumerated()), id: \.offset) { index, option in
                    Button { choose(item, index) } label: {
                        Text(option)
                            .font(.jakarta(.body, weight: .medium))
                            .multilineTextAlignment(.leading)
                            .frame(maxWidth: .infinity, alignment: .leading)
                            .padding(16)
                            .background(Theme.surface, in: RoundedRectangle(cornerRadius: 14))
                            .overlay(RoundedRectangle(cornerRadius: 14).stroke(Color.secondary.opacity(0.2), lineWidth: 2))
                    }
                    .buttonStyle(.plain)
                }
                Button("Bilmiyorum") { choose(item, -1) }
                    .font(.jakarta(.subheadline, weight: .semibold))
                    .foregroundStyle(.secondary)
                    .frame(maxWidth: .infinity)
                    .padding(.top, 4)
            }
            .padding(20)
        }
    }

    private func choose(_ item: PlacementItem, _ index: Int) {
        Haptics.tap()
        chosen[item.id] = index
        answered += 1
        guard var current = engine else { return }
        if position + 1 < current.currentBlock.count {
            position += 1
        } else {
            current.submitBlock(chosen)
            engine = current
            chosen = [:]
            position = 0
        }
    }

}

struct PlacementResultView: View {
    let result: PlacementResult
    let onContinue: () -> Void

    var body: some View {
        ScrollView {
            VStack(spacing: 20) {
                Text("Seviyeniz").font(.jakarta(.headline)).foregroundStyle(.secondary).padding(.top, 24)
                Text(result.level.rawValue)
                    .font(.system(size: 72, weight: .heavy, design: .rounded))
                    .foregroundStyle(Theme.color(for: result.level))
                Text(result.level.title).font(.jakarta(.title2, weight: .bold))
                Text(result.level.canDoSummary)
                    .font(.jakarta(.body))
                    .foregroundStyle(.secondary)
                    .multilineTextAlignment(.center)

                VStack(alignment: .leading, spacing: 12) {
                    ForEach(Skill.allCases.filter { result.skillScores[$0] != nil }, id: \.self) { skill in
                        let score = result.skillScores[skill] ?? 0
                        VStack(alignment: .leading, spacing: 4) {
                            HStack {
                                Text(skill.turkishName).font(.jakarta(.subheadline, weight: .semibold))
                                Spacer()
                                Text("%\(Int(score * 100))").font(.jakarta(.subheadline)).foregroundStyle(.secondary)
                            }
                            ProgressBar(value: score, color: skill == result.weakestSkill ? Theme.warning : Theme.success)
                        }
                    }
                    if let weakest = result.weakestSkill {
                        Text("En çok gelişmeye açık alanınız: \(weakest.turkishName.lowercased()). Derslerde buna ağırlık verin.")
                            .font(.jakarta(.footnote))
                            .foregroundStyle(.secondary)
                    }
                }
                .card()

                Text("\(result.level.rawValue) seviyesinin ilk ünitesinden başlayacaksınız. İsterseniz istediğiniz seviyeye her zaman geçebilirsiniz.")
                    .font(.jakarta(.footnote))
                    .foregroundStyle(.secondary)
                    .multilineTextAlignment(.center)
                Button("Öğrenmeye başla", action: onContinue).buttonStyle(.primary)
            }
            .padding(20)
        }
    }

}

extension Skill {
    var turkishName: String {
        switch self {
        case .grammar: "Dilbilgisi"
        case .vocabulary: "Kelime"
        case .reading: "Okuma"
        case .listening: "Dinleme"
        case .speaking: "Konuşma"
        case .writing: "Yazma"
        }
    }
}

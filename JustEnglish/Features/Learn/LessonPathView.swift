import SwiftUI
import JECore

/// Ünitenin dersleri, sağa sola kıvrılan bir yol üzerinde yuvarlak düğümler olarak.
/// Bitirilen dersler dolu, sıradaki ders nabız gibi atan bir halkayla, en sonda ünite testi kupası.
struct LessonPathView: View {
    let unit: CourseUnit
    let onLesson: (Lesson) -> Void
    let onTest: () -> Void

    @Environment(AppModel.self) private var model

    /// Düğümlerin yatay kayması: dalgalı bir yol çizer.
    private let offsets: [CGFloat] = [0, -70, -40, 40, 70, 0]

    private var nextIndex: Int? {
        unit.lessons.firstIndex { !model.state.completedLessons.contains($0.id) }
    }

    var body: some View {
        let color = Theme.color(for: unit.level)
        VStack(spacing: 18) {
            ForEach(Array(unit.lessons.enumerated()), id: \.element.id) { index, lesson in
                let done = model.state.completedLessons.contains(lesson.id)
                let current = index == nextIndex
                PathNode(icon: done ? "checkmark" : icon(for: index), color: done ? Theme.warning : (current ? color : nil),
                         current: current, label: lesson.title) {
                    onLesson(lesson)
                }
                .offset(x: offsets[index % offsets.count])
                .staggeredAppear(index, delay: 0.07)
            }
            let passed = model.isUnitPassed(unit)
            PathNode(icon: "trophy.fill", color: passed ? Theme.warning : (nextIndex == nil ? color : nil),
                     current: nextIndex == nil && !passed, label: "Ünite testi", size: 84, action: onTest)
                .offset(x: offsets[unit.lessons.count % offsets.count])
                .staggeredAppear(unit.lessons.count, delay: 0.07)
        }
        .frame(maxWidth: .infinity)
        .padding(.vertical, 8)
    }

    private func icon(for index: Int) -> String {
        ["star.fill", "book.fill", "dumbbell.fill", "bubble.left.and.bubble.right.fill", "sparkles"][index % 5]
    }
}

struct PathNode: View {
    let icon: String
    /// nil: henüz sırası gelmemiş ders (gri).
    let color: Color?
    let current: Bool
    let label: String
    var size: CGFloat = 72
    let action: () -> Void

    @State private var pulse = false
    @State private var bob = false

    var body: some View {
        VStack(spacing: 6) {
            if current {
                Text("BAŞLA")
                    .font(.jakarta(.caption, weight: .heavy))
                    .foregroundStyle(color ?? Theme.accent)
                    .padding(.horizontal, 12)
                    .padding(.vertical, 7)
                    .background(Theme.surface, in: RoundedRectangle(cornerRadius: 10, style: .continuous))
                    .overlay(RoundedRectangle(cornerRadius: 10, style: .continuous).stroke(Color(uiColor: .systemGray4), lineWidth: 2))
                    .offset(y: bob ? -4 : 2)
                    .onAppear { withAnimation(.easeInOut(duration: 0.9).repeatForever()) { bob = true } }
            }
            ZStack {
                if current {
                    Circle()
                        .stroke((color ?? Theme.accent).opacity(0.35), lineWidth: 6)
                        .frame(width: size + 18, height: size + 18)
                        .scaleEffect(pulse ? 1.08 : 0.96)
                        .opacity(pulse ? 0.4 : 1)
                        .onAppear { withAnimation(.easeInOut(duration: 1.1).repeatForever()) { pulse = true } }
                }
                Button(action: action) {
                    Image(systemName: icon)
                        .font(.system(size: size * 0.38, weight: .black))
                        .foregroundStyle(color == nil ? Color(uiColor: .systemGray2) : .white)
                        .frame(width: size, height: size)
                }
                .buttonStyle(RoundDepthButtonStyle(color: color ?? Color(uiColor: .systemGray5)))
                .accessibilityLabel(label)
            }
            Text(label)
                .font(.jakarta(.caption, weight: .semibold))
                .foregroundStyle(.secondary)
                .multilineTextAlignment(.center)
                .lineLimit(2)
                .frame(width: 130)
        }
    }
}

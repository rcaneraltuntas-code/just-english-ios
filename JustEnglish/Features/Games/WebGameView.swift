import SwiftUI
import WebKit
import JECore

/// Uygulamaya gömülü HTML oyunları (WebGames/<oyun>/index.html). Çevrimdışı çalışır; sayfa
/// `webkit.messageHandlers.jengo` ile kapatma, sesli okuma ve gün sonu bilgisini uygulamaya iletir.
struct WebGameScreen: View {
    let game: String

    @Environment(AppModel.self) private var model
    @Environment(\.dismiss) private var dismiss

    var body: some View {
        WebGameView(game: game) { message in
            switch message["type"] as? String {
            case "close":
                Speech.shared.stop()
                dismiss()
            case "speak":
                if let text = message["text"] as? String { Speech.shared.speak(text) }
            case "stopSpeech":
                Speech.shared.stop()
            case "dayEnd":
                // Diğer oyunlardaki gibi: yıldızların en az üçte ikisi XP kazandırır.
                let stars = message["stars"] as? Int ?? 0, max = message["max"] as? Int ?? 1
                if stars * 3 >= max * 2 { model.award(xp: XPRule.gameWin) }
            default:
                break
            }
        }
        .ignoresSafeArea()
        .background(Color(light: 0xF3EEE7, dark: 0xF3EEE7).ignoresSafeArea())
        .statusBarHidden()
        .onDisappear { Speech.shared.stop() }
    }
}

private struct WebGameView: UIViewRepresentable {
    let game: String
    let onMessage: ([String: Any]) -> Void

    func makeCoordinator() -> Coordinator { Coordinator(onMessage: onMessage) }

    func makeUIView(context: Context) -> WKWebView {
        let config = WKWebViewConfiguration()
        config.allowsInlineMediaPlayback = true
        config.mediaTypesRequiringUserActionForPlayback = []
        config.userContentController.add(context.coordinator, name: "jengo")
        let web = WKWebView(frame: .zero, configuration: config)
        web.isOpaque = false
        web.backgroundColor = UIColor(red: 0xF3 / 255, green: 0xEE / 255, blue: 0xE7 / 255, alpha: 1)
        web.scrollView.isScrollEnabled = false
        web.scrollView.bounces = false
        web.scrollView.contentInsetAdjustmentBehavior = .never
        if let root = Bundle.main.url(forResource: "WebGames", withExtension: nil) {
            web.loadFileURL(root.appending(path: "\(game)/index.html"), allowingReadAccessTo: root)
        }
        return web
    }

    func updateUIView(_ web: WKWebView, context: Context) {}

    static func dismantleUIView(_ web: WKWebView, coordinator: Coordinator) {
        web.configuration.userContentController.removeScriptMessageHandler(forName: "jengo")
    }

    final class Coordinator: NSObject, WKScriptMessageHandler {
        let onMessage: ([String: Any]) -> Void
        init(onMessage: @escaping ([String: Any]) -> Void) { self.onMessage = onMessage }

        func userContentController(_ controller: WKUserContentController, didReceive message: WKScriptMessage) {
            guard let body = message.body as? [String: Any] else { return }
            Task { @MainActor in self.onMessage(body) }
        }
    }
}

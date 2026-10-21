import AVFoundation

/// Dinleme alıştırmaları ve kelime kartları için cihazın İngilizce sesiyle okuma.
@MainActor
final class Speech {
    static let shared = Speech()

    private let synthesizer = AVSpeechSynthesizer()
    private lazy var voice: AVSpeechSynthesisVoice? = {
        let english = AVSpeechSynthesisVoice.speechVoices().filter { $0.language == "en-GB" || $0.language == "en-US" }
        // Varsa yüksek kaliteli ses tercih edilir.
        return english.max { $0.quality.rawValue < $1.quality.rawValue } ?? AVSpeechSynthesisVoice(language: "en-GB")
    }()

    func speak(_ text: String, rate: Float = 0.45) {
        try? AVAudioSession.sharedInstance().setCategory(.playback, mode: .spokenAudio, options: .duckOthers)
        synthesizer.stopSpeaking(at: .immediate)
        let utterance = AVSpeechUtterance(string: text)
        utterance.voice = voice
        utterance.rate = rate
        synthesizer.speak(utterance)
    }

    func stop() {
        synthesizer.stopSpeaking(at: .immediate)
    }
}

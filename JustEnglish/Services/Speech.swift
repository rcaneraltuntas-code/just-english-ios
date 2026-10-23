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
    private var genderVoices: [AVSpeechSynthesisVoiceGender: AVSpeechSynthesisVoice] = [:]

    /// Oyun karakterleri için kadın ya da erkek İngilizce ses; cihazda yoksa varsayılan ses.
    private func voice(for gender: AVSpeechSynthesisVoiceGender) -> AVSpeechSynthesisVoice? {
        if let cached = genderVoices[gender] { return cached }
        let match = AVSpeechSynthesisVoice.speechVoices().filter {
            ($0.language == "en-US" || $0.language == "en-GB") && $0.gender == gender
                && !$0.voiceTraits.contains(.isNoveltyVoice) && !$0.voiceTraits.contains(.isPersonalVoice)
        }.max { $0.quality.rawValue < $1.quality.rawValue }
        genderVoices[gender] = match
        return match ?? voice
    }

    func speak(_ text: String, rate: Float = 0.45, gender: AVSpeechSynthesisVoiceGender? = nil) {
        try? AVAudioSession.sharedInstance().setCategory(.playback, mode: .spokenAudio, options: .duckOthers)
        synthesizer.stopSpeaking(at: .immediate)
        let utterance = AVSpeechUtterance(string: text)
        utterance.voice = gender.flatMap { voice(for: $0) } ?? voice
        utterance.rate = rate
        synthesizer.speak(utterance)
    }

    func stop() {
        synthesizer.stopSpeaking(at: .immediate)
    }
}

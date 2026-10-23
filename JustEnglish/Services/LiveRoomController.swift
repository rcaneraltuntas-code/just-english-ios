import Foundation
import LiveKit
import Observation
import Supabase

/// Uygulama içi canlı ders odası (LiveKit). Öğretmen kamerası ve sesiyle yayın yapar; öğrenciler izler,
/// el kaldırır ve öğretmen söz verince mikrofonlarını açabilir. Sohbet ve söz verme veri mesajlarıyla taşınır.
@MainActor
@Observable
final class LiveRoomController {
    enum Phase: Equatable { case connecting, connected, ended, failed(String) }

    struct ChatMessage: Identifiable, Hashable {
        let id = UUID()
        let sender: String
        let text: String
        let mine: Bool
    }

    /// Ekranda gösterilen katılımcı özeti. LiveKit nesneleri her olayda yeniden okunur.
    struct Member: Identifiable {
        let id: String
        let name: String
        let isTeacher: Bool
        let handRaised: Bool
        let micOn: Bool
        let isSpeaking: Bool
        let participant: Participant
    }

    let sessionID: UUID
    let room = Room()

    private(set) var phase: Phase = .connecting
    private(set) var isTeacher = false
    private(set) var members: [Member] = []
    private(set) var teacherVideo: VideoTrack?
    private(set) var teacherPresent = false
    private(set) var messages: [ChatMessage] = []
    private(set) var unreadChat = 0
    private(set) var micOn = false
    private(set) var cameraOn = false
    private(set) var handRaised = false
    /// Öğrenci, öğretmen söz verene kadar mikrofonunu açamaz. Öğretmen her zaman konuşabilir.
    private(set) var maySpeak = false
    var chatOpen = false

    private var events: RoomEvents?
    private var myName = ""

    private enum Topic {
        static let chat = "chat"
        static let floor = "floor"
        static let muteAll = "mute-all"
    }

    init(sessionID: UUID) {
        self.sessionID = sessionID
    }

    var students: [Member] {
        members.filter { !$0.isTeacher }.sorted { ($0.handRaised ? 0 : 1, $0.name) < ($1.handRaised ? 0 : 1, $1.name) }
    }

    var raisedHands: Int { members.filter(\.handRaised).count }

    // MARK: - Bağlantı

    private struct TokenResponse: Decodable {
        let url: String
        let token: String
        let role: String
    }

    func connect() async {
        guard phase != .connected else { return }
        guard let client = Backend.client else { phase = .failed("Canlı dersler şu an kullanılamıyor."); return }
        phase = .connecting
        do {
            let response: TokenResponse = try await client.functions.invoke(
                "livekit-token", options: FunctionInvokeOptions(body: ["session_id": sessionID.uuidString]))
            isTeacher = response.role == "teacher"
            maySpeak = isTeacher

            if events == nil {
                let events = RoomEvents { [weak self] in
                    Task { @MainActor in self?.refresh() }
                } onData: { [weak self] data, topic, sender in
                    Task { @MainActor in self?.receive(data, topic: topic, from: sender) }
                }
                self.events = events
                room.add(delegate: events)
            }

            try await room.connect(url: response.url, token: response.token,
                                   roomOptions: RoomOptions(adaptiveStream: true, dynacast: true))
            myName = room.localParticipant.name ?? ""
            if isTeacher {
                try await room.localParticipant.setCamera(enabled: true)
                try await room.localParticipant.setMicrophone(enabled: true)
            }
            phase = .connected
            refresh()
        } catch let FunctionsError.httpError(code, data) {
            phase = .failed(Self.message(forStatus: code, data: data))
        } catch {
            phase = .failed("Derse bağlanılamadı. İnternet bağlantınızı kontrol edip tekrar deneyin.")
        }
    }

    /// Odadan çıkar. Öğretmen çıkarken "Dersi bitir" derse ders öğrencilere bitmiş görünür.
    func leave(endForEveryone: Bool = false) async {
        if endForEveryone, isTeacher, let client = Backend.client {
            _ = try? await client.rpc("end_live_session", params: ["p_session": sessionID]).execute()
        }
        await room.disconnect()
        phase = .ended
    }

    private static func message(forStatus code: Int, data: Data) -> String {
        let reason = (try? JSONDecoder().decode([String: String].self, from: data))?["error"]
        switch reason {
        case "not_signed_in": return "Derse katılmak için Profil sekmesinden Apple ile giriş yapın."
        case "not_booked": return "Bu derse yer ayırtmadınız."
        case "outside_window": return "Ders bağlantısı dersten 10 dakika önce açılır."
        case "session_ended": return "Bu ders sona erdi."
        case "session_not_found": return "Ders bulunamadı ya da iptal edildi."
        case "livekit_not_configured": return "Canlı yayın henüz ayarlanmadı. Lütfen okulla iletişime geçin."
        default: return "Derse bağlanılamadı (\(code)). Lütfen tekrar deneyin."
        }
    }

    // MARK: - Kontroller

    func toggleMicrophone() async {
        guard maySpeak || micOn else { return }
        _ = try? await room.localParticipant.setMicrophone(enabled: !micOn)
        refresh()
    }

    func toggleCamera() async {
        guard isTeacher else { return }
        _ = try? await room.localParticipant.setCamera(enabled: !cameraOn)
        refresh()
    }

    func switchCamera() async {
        guard let track = room.localParticipant.firstCameraVideoTrack as? LocalVideoTrack,
              let capturer = track.capturer as? CameraCapturer else { return }
        _ = try? await capturer.switchCameraPosition()
    }

    func toggleHand() async {
        guard !isTeacher else { return }
        await setHand(!handRaised)
    }

    private func setHand(_ raised: Bool) async {
        handRaised = raised
        try? await room.localParticipant.set(attributes: ["role": "student", "hand": raised ? "1" : "0"])
    }

    /// Öğretmen bir öğrenciye söz verir ya da sözü geri alır.
    func setFloor(_ member: Member, allowed: Bool) async {
        guard isTeacher else { return }
        let payload = try? JSONEncoder().encode(["identity": member.id, "allow": allowed ? "1" : "0"])
        guard let payload else { return }
        try? await room.localParticipant.publish(
            data: payload,
            options: DataPublishOptions(destinationIdentities: [Participant.Identity(from: member.id)],
                                        topic: Topic.floor, reliable: true))
    }

    func muteAllStudents() async {
        guard isTeacher else { return }
        try? await room.localParticipant.publish(data: Data("{}".utf8),
                                                 options: DataPublishOptions(topic: Topic.muteAll, reliable: true))
    }

    func send(_ text: String) async {
        let text = text.trimmingCharacters(in: .whitespacesAndNewlines)
        guard !text.isEmpty, let payload = try? JSONEncoder().encode(["name": myName, "text": text]) else { return }
        try? await room.localParticipant.publish(data: payload, options: DataPublishOptions(topic: Topic.chat, reliable: true))
        messages.append(ChatMessage(sender: myName, text: text, mine: true))
    }

    func markChatRead() { unreadChat = 0 }

    // MARK: - Olaylar

    private func receive(_ data: Data, topic: String, from sender: RemoteParticipant?) {
        let fields = (try? JSONDecoder().decode([String: String].self, from: data)) ?? [:]
        switch topic {
        case Topic.chat:
            guard let text = fields["text"], !text.isEmpty else { return }
            messages.append(ChatMessage(sender: fields["name"] ?? sender?.name ?? "", text: text, mine: false))
            if !chatOpen { unreadChat += 1 }
        case Topic.floor where !isTeacher && sender?.attributes["role"] == "teacher":
            let allowed = fields["allow"] == "1"
            maySpeak = allowed
            Task {
                if allowed {
                    await setHand(false)
                    _ = try? await room.localParticipant.setMicrophone(enabled: true)
                } else {
                    _ = try? await room.localParticipant.setMicrophone(enabled: false)
                }
                refresh()
            }
        case Topic.muteAll where !isTeacher && sender?.attributes["role"] == "teacher":
            maySpeak = false
            Task {
                _ = try? await room.localParticipant.setMicrophone(enabled: false)
                refresh()
            }
        default:
            break
        }
    }

    private func refresh() {
        if room.connectionState == .disconnected, phase == .connected { phase = .ended }
        members = room.remoteParticipants.values.map { participant in
            Member(id: participant.identity?.stringValue ?? UUID().uuidString,
                   name: participant.name.flatMap { $0.isEmpty ? nil : $0 } ?? "Öğrenci",
                   isTeacher: participant.attributes["role"] == "teacher",
                   handRaised: participant.attributes["hand"] == "1",
                   micOn: participant.isMicrophoneEnabled(),
                   isSpeaking: participant.isSpeaking,
                   participant: participant)
        }
        let local = room.localParticipant
        micOn = local.isMicrophoneEnabled()
        cameraOn = local.isCameraEnabled()
        let teacher = members.first(where: \.isTeacher)
        teacherPresent = isTeacher || teacher != nil
        teacherVideo = isTeacher ? local.firstCameraVideoTrack : teacher?.participant.firstCameraVideoTrack
    }
}

/// LiveKit olaylarını ana iş parçacığındaki denetleyiciye iletir. RoomDelegate bir @objc protokolü olduğu için ayrı bir NSObject.
private final class RoomEvents: NSObject, RoomDelegate, @unchecked Sendable {
    private let onChange: @Sendable () -> Void
    private let onData: @Sendable (Data, String, RemoteParticipant?) -> Void

    init(onChange: @escaping @Sendable () -> Void, onData: @escaping @Sendable (Data, String, RemoteParticipant?) -> Void) {
        self.onChange = onChange
        self.onData = onData
    }

    func room(_ room: Room, didUpdateConnectionState connectionState: ConnectionState, from oldConnectionState: ConnectionState) { onChange() }
    func room(_ room: Room, participantDidConnect participant: RemoteParticipant) { onChange() }
    func room(_ room: Room, participantDidDisconnect participant: RemoteParticipant) { onChange() }
    func room(_ room: Room, didUpdateSpeakingParticipants participants: [Participant]) { onChange() }
    func room(_ room: Room, participant: Participant, didUpdateName name: String) { onChange() }
    func room(_ room: Room, participant: Participant, didUpdateAttributes attributes: [String: String]) { onChange() }
    func room(_ room: Room, participant: Participant, trackPublication: TrackPublication, didUpdateIsMuted isMuted: Bool) { onChange() }
    func room(_ room: Room, participant: LocalParticipant, didPublishTrack publication: LocalTrackPublication) { onChange() }
    func room(_ room: Room, participant: LocalParticipant, didUnpublishTrack publication: LocalTrackPublication) { onChange() }
    func room(_ room: Room, participant: RemoteParticipant, didSubscribeTrack publication: RemoteTrackPublication) { onChange() }
    func room(_ room: Room, participant: RemoteParticipant, didUnsubscribeTrack publication: RemoteTrackPublication) { onChange() }

    func room(_ room: Room, participant: RemoteParticipant?, didReceiveData data: Data, forTopic topic: String, encryptionType: EncryptionType) {
        onData(data, topic, participant)
    }
}

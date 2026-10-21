import Foundation

/// Öğrenci durumunu Application Support klasöründe JSON olarak saklar.
struct StateStore {
    static let shared = StateStore(url: StateStore.defaultURL)

    let url: URL

    static var defaultURL: URL {
        let dir = FileManager.default.urls(for: .applicationSupportDirectory, in: .userDomainMask)[0]
        return dir.appendingPathComponent("user-state.json")
    }

    func load() -> UserState? {
        guard let data = try? Data(contentsOf: url) else { return nil }
        return try? JSONDecoder().decode(UserState.self, from: data)
    }

    func save(_ state: UserState) {
        do {
            try FileManager.default.createDirectory(at: url.deletingLastPathComponent(), withIntermediateDirectories: true)
            try JSONEncoder().encode(state).write(to: url, options: .atomic)
        } catch {
            assertionFailure("Durum kaydedilemedi: \(error)")
        }
    }
}

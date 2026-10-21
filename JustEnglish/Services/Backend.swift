import Foundation
import Supabase

/// Supabase istemcisi. Anahtarlar Info.plist'e Config/Secrets.xcconfig'ten gelir.
/// Anahtar yoksa uygulama tamamen çevrimdışı çalışır: giriş, eşitleme ve canlı dersler kapalı olur.
enum Backend {
    static let client: SupabaseClient? = {
        guard let urlString = Bundle.main.object(forInfoDictionaryKey: "SupabaseURL") as? String,
              let key = Bundle.main.object(forInfoDictionaryKey: "SupabaseAnonKey") as? String,
              let url = URL(string: urlString), url.host?.contains(".") == true,
              !key.isEmpty, !key.hasPrefix("eyJ...")
        else { return nil }
        return SupabaseClient(supabaseURL: url, supabaseKey: key)
    }()

    static var isConfigured: Bool { client != nil }
}

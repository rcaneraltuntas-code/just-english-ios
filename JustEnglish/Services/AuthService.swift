import AuthenticationServices
import CryptoKit
import Foundation
import Observation
import Supabase

/// Apple ile giriş. Giriş isteğe bağlıdır: öğrenci giriş yapmadan da tüm dersleri kullanabilir;
/// giriş yapınca ilerleme buluta yedeklenir ve canlı derslere kayıt açılır.
@MainActor
@Observable
final class AuthService {
    private(set) var userID: UUID?
    private(set) var email: String?
    private(set) var error: String?
    /// profiles.role: öğretmenler canlı ders açabilir.
    private(set) var role = "student"
    private var currentNonce: String?

    var isSignedIn: Bool { userID != nil }
    var isTeacher: Bool { role == "teacher" || role == "admin" }

    init() {
        Task { await restore() }
    }

    func restore() async {
        guard let client = Backend.client, let session = try? await client.auth.session else { return }
        userID = session.user.id
        email = session.user.email
        await loadRole()
    }

    func loadRole() async {
        guard let client = Backend.client, let userID else { return }
        struct Profile: Decodable { let role: String }
        let rows: [Profile]? = try? await client.from("profiles").select("role").eq("id", value: userID).execute().value
        role = rows?.first?.role ?? "student"
    }

    /// SignInWithAppleButton'ın isteğini hazırlar.
    func prepare(_ request: ASAuthorizationAppleIDRequest) {
        let nonce = Self.randomNonce()
        currentNonce = nonce
        request.requestedScopes = [.fullName, .email]
        request.nonce = Self.sha256(nonce)
    }

    func complete(_ result: Result<ASAuthorization, Error>) async -> PersonNameComponents? {
        error = nil
        do {
            guard let client = Backend.client else { throw AuthError.notConfigured }
            let authorization = try result.get()
            guard let credential = authorization.credential as? ASAuthorizationAppleIDCredential,
                  let tokenData = credential.identityToken,
                  let token = String(data: tokenData, encoding: .utf8),
                  let nonce = currentNonce
            else { throw AuthError.invalidCredential }
            let session = try await client.auth.signInWithIdToken(
                credentials: OpenIDConnectCredentials(provider: .apple, idToken: token, nonce: nonce))
            userID = session.user.id
            email = session.user.email
            await loadRole()
            return credential.fullName
        } catch let error as ASAuthorizationError where error.code == .canceled {
            return nil
        } catch {
            self.error = "Giriş yapılamadı. Lütfen tekrar deneyin."
            return nil
        }
    }

    func signOut() async {
        try? await Backend.client?.auth.signOut()
        userID = nil
        email = nil
        role = "student"
    }

    /// Hesap silme: App Store kuralı gereği uygulama içinden yapılabilmelidir.
    func deleteAccount() async -> Bool {
        guard let client = Backend.client else { return false }
        do {
            try await client.rpc("delete_my_account").execute()
            await signOut()
            return true
        } catch {
            self.error = "Hesap silinemedi. Lütfen tekrar deneyin."
            return false
        }
    }

    enum AuthError: Error { case notConfigured, invalidCredential }

    private static func randomNonce(length: Int = 32) -> String {
        let charset = Array("0123456789ABCDEFGHIJKLMNOPQRSTUVXYZabcdefghijklmnopqrstuvwxyz-._")
        var generator = SystemRandomNumberGenerator()
        return String((0..<length).map { _ in charset.randomElement(using: &generator)! })
    }

    private static func sha256(_ input: String) -> String {
        SHA256.hash(data: Data(input.utf8)).map { String(format: "%02x", $0) }.joined()
    }
}

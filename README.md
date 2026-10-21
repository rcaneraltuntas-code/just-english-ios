# Just English iOS

Just English'in herkese açık, ücretsiz hibrit İngilizce uygulaması.

## Yapı

| Klasör | İçerik |
| --- | --- |
| `JustEnglish/` | SwiftUI uygulaması (iOS 17+) |
| `Packages/JECore/` | Platformdan bağımsız öğrenme motoru: seviye tespiti, FSRS aralıklı tekrar, seri/XP |
| `JustEnglish/Resources/Content/` | Uygulamaya gömülü içerik (JSON): seviye testi, üniteler |
| `content-src/` | İçeriğin kaynak dosyaları ve öğretmen inceleme çıktısı üreten araçlar |
| `supabase/` | Veritabanı şeması ve migration'lar |

## Kurulum (Mac)

```sh
brew install xcodegen
xcodegen generate
open JustEnglish.xcodeproj
```

Çekirdek testleri: `cd Packages/JECore && swift test`

Supabase anahtarları için `Config/Secrets.example.xcconfig` dosyasını `Config/Secrets.xcconfig` olarak kopyalayın.

## Uygulamanın yapısı

| Klasör | İçerik |
| --- | --- |
| `JustEnglish/App` | Giriş noktası, `AppModel` (öğrenci durumu, ilerleme kuralları), yerel kayıt |
| `JustEnglish/DesignSystem` | Renkler ve yazı tipi (`Theme.swift`), ortak bileşenler, Markdown görüntüleyici |
| `JustEnglish/Features` | Ekranlar: karşılama, seviye testi, öğren (ana sayfa, ünite, ders akışı, ünite testi), alıştırmalar, pratik ve oyunlar, sözlük, canlı dersler, profil |
| `JustEnglish/Services` | Sesli okuma, ses tanıma, Supabase (giriş, eşitleme, canlı dersler) |

Uygulama önce yerelde çalışır: tüm içerik uygulamanın içindedir ve giriş yapmadan kullanılabilir.
Supabase anahtarları girilmezse giriş, bulut yedekleme ve canlı ders listesi kapalı olur; geri kalan her şey çalışır.

Marka renkleri `JustEnglish/DesignSystem/Theme.swift` ve `Assets.xcassets/AccentColor` içinde; değiştirmek için yalnızca bu iki yer yeterli.

## Supabase kurulumu

1. Supabase'de yeni proje açın. **Authentication → Providers → Apple**'ı açın ve bundle id olarak `com.justenglishtr.app` girin.
2. `supabase/migrations/` altındaki SQL'i **SQL Editor**'da çalıştırın (ya da `supabase db push`).
3. **Project Settings → API**'deki URL ve anon anahtarı `Config/Secrets.xcconfig` dosyasına yazın.
4. Öğretmen hesabı: öğretmen uygulamada Apple ile giriş yaptıktan sonra SQL Editor'da
   `update profiles set role = 'teacher' where id = '<kullanıcı id>';` çalıştırın.

### Canlı ders ekleme

Şimdilik canlı dersler **Table Editor → live_sessions** üzerinden eklenir:
`unit_id` (ör. `b1-u03`), `level` (`B1`), `title`, `starts_at`, `duration_minutes`, `teacher_id`, `teacher_name`,
`join_url` (Zoom/Meet bağlantısı) ve isteğe bağlı `capacity`. Katılım bağlantısını yalnızca yer ayırtan öğrenciler görür
ve bağlantı dersten 10 dakika önce açılır.

## İçerik üretimi

```sh
cd content-src
python3 placement.py ../JustEnglish/Resources/Content/placement.json
for f in [a-c][12]_u*.py; do python3 "$f" "../JustEnglish/Resources/Content/$(basename "$f" .py | tr _ -).json"; done
python3 render_review.py ../JustEnglish/Resources/Content/a1-u01.json > a1-u01.md   # öğretmen incelemesi için
```

Her üretim betiği içeriği doğrular (cevap indeksleri, tekrar eden seçenekler, cümle kurma kelimeleri) ve hata varsa durur.

Fontlar: Plus Jakarta Sans, SIL Open Font License (`JustEnglish/Resources/Fonts/OFL.txt`).

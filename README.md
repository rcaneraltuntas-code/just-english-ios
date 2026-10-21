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

## İçerik üretimi

```sh
cd content-src
python3 placement.py ../JustEnglish/Resources/Content/placement.json
for f in [a-c][12]_u*.py; do python3 "$f" "../JustEnglish/Resources/Content/$(basename "$f" .py | tr _ -).json"; done
python3 render_review.py ../JustEnglish/Resources/Content/a1-u01.json > a1-u01.md   # öğretmen incelemesi için
```

Her üretim betiği içeriği doğrular (cevap indeksleri, tekrar eden seçenekler, cümle kurma kelimeleri) ve hata varsa durur.

Fontlar: Plus Jakarta Sans, SIL Open Font License (`JustEnglish/Resources/Fonts/OFL.txt`).

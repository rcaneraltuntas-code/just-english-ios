"""B2 Ünite 1: Anlatı."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("B2", 1, "Anlatı", "Storytelling",
         "Bir hikâyeyi bütün anlatı zamanlarını (past perfect continuous dahil) ustaca kullanarak, güçlü sıfat ve zarflarla, dinleyicinin ilgisini canlı tutacak şekilde anlatabilirim.",
         ["anlatı zamanları: tekrar ve ince farklar", "past perfect continuous", "past perfect simple ve continuous farkı", "zaman bağlaçları: as soon as, the moment, no sooner... than (giriş)", "güçlü sıfatlar ve derecelendirme zarfları"],
         ["hikâye anlatımı sıfatları", "duygu ve tepki", "anlatı bağlayıcıları"],
         {"title": "Hikâye gecesi", "durationMinutes": 45,
          "goal": "Her öğrenci başından geçmiş (ya da hayali) unutulmaz bir olayı 2 dakikada anlatır. Anlatımda en az bir past perfect continuous cümlesi, iki güçlü sıfat ve bir gerilim anı olmalıdır. Dinleyenler You'll never guess... / What happened next? gibi tepkilerle katılır, sonunda sınıf en sürükleyici hikâyeyi seçer ve öğretmen dil kullanımına geri bildirim verir."})

u.vocab([
    ("terrified", "çok korkmuş, dehşete düşmüş", "I was absolutely terrified.", "Tamamen dehşete düşmüştüm.", "scared'in güçlüsü"),
    ("exhausted", "bitkin", "We were exhausted after the climb.", "Tırmanıştan sonra bitkindik.", "tired'ın güçlüsü"),
    ("furious", "öfkeden kudurmuş", "My boss was furious.", "Patronum çok öfkeliydi.", "angry'nin güçlüsü"),
    ("astonished", "hayretler içinde", "Everyone was astonished by the news.", "Herkes habere hayret etti.", "surprised'ın güçlüsü"),
    ("delighted", "çok memnun", "She was delighted with her present.", "Hediyesinden çok memnun kaldı.", "pleased'in güçlüsü"),
    ("devastated", "yıkılmış", "He was devastated when he lost his job.", "İşini kaybedince yıkıldı.", "sad'in güçlüsü"),
    ("freezing", "buz gibi", "It was freezing on the mountain.", "Dağda hava buz gibiydi.", "cold'un güçlüsü"),
    ("hilarious", "çok komik", "The film was hilarious.", "Film çok komikti.", "funny'nin güçlüsü"),
    ("gripping", "sürükleyici", "It was a gripping story.", "Sürükleyici bir hikâyeydi.", None),
    ("nerve-racking", "sinir bozucu, gergin edici", "The interview was nerve-racking.", "Mülakat çok gerdi.", None),
    ("absolutely", "tamamen, kesinlikle", "It was absolutely amazing.", "Kesinlikle muhteşemdi.", "güçlü sıfatlarla"),
    ("utterly", "tamamen, büsbütün", "I was utterly exhausted.", "Tamamen bitkindim.", None),
    ("gradually", "yavaş yavaş", "Gradually, the sky got darker.", "Gökyüzü yavaş yavaş karardı.", None),
    ("all of a sudden", "birdenbire", "All of a sudden, the lights went out.", "Birdenbire ışıklar söndü.", None),
    ("eventually", "sonunda (uzun süreden sonra)", "Eventually, we found the way.", "Sonunda yolu bulduk.", "≠ eventually 'muhtemelen' değil"),
    ("meanwhile", "bu arada, o sırada", "Meanwhile, the others were waiting.", "Bu arada diğerleri bekliyordu.", None),
    ("the moment", "-dığı anda", "The moment I saw her, I knew.", "Onu gördüğüm anda anladım.", None),
    ("it turned out that", "anlaşıldı ki", "It turned out that he was her brother.", "Meğer onun kardeşiymiş.", None),
    ("to my surprise", "şaşırtıcı bir şekilde", "To my surprise, nobody was there.", "Şaşırtıcı bir şekilde orada kimse yoktu.", None),
    ("as it happens", "tesadüfe bak ki", "As it happens, I was there too.", "Tesadüfe bak ki ben de oradaydım.", None),
    ("plot", "olay örgüsü", "The plot was hard to follow.", "Olay örgüsünü takip etmek zordu.", None),
    ("twist", "beklenmedik gelişme", "The story has an amazing twist at the end.", "Hikâyenin sonunda harika bir sürpriz var.", None),
    ("anecdote", "kısa ve ilginç anı", "He told us a funny anecdote.", "Bize komik bir anı anlattı.", None),
    ("ending", "son", "I didn't expect that ending.", "O sonu beklemiyordum.", None),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Zamanlar sahnede", "Past simple, past continuous ve past perfect'i bir hikâyede bilinçli olarak ve doğru sırayla kullanabilirim.",
    {"kind": "text", "title": "Sisli gece", "body": "It was nearly midnight when Elif finally left the office. A thick fog had come in from the sea, and the streets were completely empty.\n\nShe was walking towards the car park when she heard footsteps behind her. She stopped. The footsteps stopped too.\n\nHer heart was pounding. She had read about a series of robberies in the area, and she had promised her mother that she would never walk alone at night.\n\nShe turned around slowly. A tall figure was standing under the streetlight, holding something in his hand. Then he stepped forward and smiled.\n\n\"Excuse me,\" he said. \"I think you dropped your keys.\"",
     "questions": [
        mc("What had Elif read about?", ["A series of robberies", "A missing woman", "A storm"], 0, "\"She had read about a series of robberies in the area\""),
        mc("What was the man holding?", ["A knife", "Elif's keys", "A phone"], 1, "\"I think you dropped your keys.\""),
     ]},
    {"explanation": "B1'de üç temel anlatı zamanını öğrendiniz. B2'de bunları **bilinçli seçimlerle** kullanarak etki yaratırız.\n\n| Zaman | Hikâyedeki işlevi | Örnek |\n|---|---|---|\n| **Past continuous** | Sahneyi kurar, yavaşlatır, gerilim yaratır | She **was walking** towards the car park ... |\n| **Past simple** | Olayları ilerletir, hızlandırır | She **stopped**. The footsteps **stopped** too. |\n| **Past perfect** | Geri dönüş (flashback), arka plan bilgisi | She **had read** about a series of robberies. |\n\n**Ritim için ipuçları:**\n\n- **Kısa past simple cümleleri** gerilim yaratır: *She stopped. The footsteps stopped too.*\n- **Uzun past continuous cümleleri** atmosfer kurar: *The rain was falling softly and the town was sleeping.*\n- Past perfect'i **paragrafın başında bir kez** kullandıktan sonra past simple'a dönebilirsiniz; okuyucu zaten geri dönüşte olduğunu anlar.\n\n**Sık hata:** Her geçmiş olayı past perfect ile anlatmak. Past perfect sadece **zaman çizgisinde geri gittiğinizde** gereklidir.",
     "examples": [{"en": "The sun was setting and the children were playing on the beach.", "tr": "Güneş batıyordu ve çocuklar sahilde oynuyordu."},
                  {"en": "He opened the door. Nobody was there.", "tr": "Kapıyı açtı. Orada kimse yoktu."},
                  {"en": "She had never seen anything so beautiful.", "tr": "Hiç bu kadar güzel bir şey görmemişti."}],
     "turkishNote": "Türkçede hikâye anlatırken zamanlar arasında \"-yordu\", \"-dı\" ve \"-mıştı\" ile geçiş yaparız ve bu İngilizceye oldukça iyi uyar. B2 seviyesinde asıl hedef doğruluktan çok etkidir: Türkçe konuşanlar genellikle tek bir zamana (çoğunlukla past simple) bağlı kalır ve anlatım düz kalır. Zamanları değiştirerek hikâyenin hızını kontrol edin."},
    [
        mc("Atmosfer kuran cümle:", ["The wind was howling and the windows were shaking.", "The wind howled. The windows shook."], 0, "Past continuous → sahne, atmosfer."),
        mc("Gerilimi artıran cümle:", ["She was slowly opening the door while she was thinking.", "She opened the door. Silence."], 1, "Kısa past simple → gerilim."),
        mc("Geri dönüş (flashback):", ["She met him ten years earlier.", "She had met him ten years earlier."], 1, "Geri dönüş → past perfect."),
        mc("Hangisinde past perfect gereksiz?", ["I woke up, had a shower and had gone to work.", "When I arrived, the meeting had already started."], 0, "Sıralı olaylar → past simple."),
        gap("It was raining heavily and the wind ___ (blow) hard.", ["was blowing"], "Arka plan → past continuous."),
        gap("He ___ (never / feel) so alone before.", ["had never felt"], "Önceki deneyim → past perfect."),
        gap("She was reading when the phone ___ (ring).", ["rang"], "Kesen olay → past simple."),
        gap("By the time the police arrived, the thieves ___ (disappear).", ["had disappeared"], "Önce olan → past perfect."),
        listen("I was sitting on the train, half asleep, when a woman sat down next to me. She looked familiar. Then I realised: we had been at primary school together thirty years earlier!", "Konuşan kadını nereden tanıyordu?", ["İş yerinden", "İlkokuldan", "Trenden"], 1, "\"we had been at primary school together\""),
        typ("İngilizce yazın: \"Hiç bu kadar güzel bir şey görmemişti.\" (she)", variants("She had never seen anything so beautiful.", "She'd never seen anything so beautiful.", "She had never seen anything as beautiful.", "She had never seen such a beautiful thing.", "She had never seen anything this beautiful.", "She'd never seen anything as beautiful."), "She had never seen anything so beautiful."),
    ],
    {"kind": "speaking", "task": speak("\"Sisli gece\" hikâyesine benzer, gerilimli bir sahne anlatın (gece eve dönerken, boş bir binada, bir yolculukta). Past continuous ile atmosferi kurun, kısa past simple cümleleriyle gerilimi artırın, bir past perfect ile geri dönüş yapın ve beklenmedik bir sonla bitirin.",
                                       "It was late and the last bus had already left. I was walking home through the park. The trees were moving in the wind and there wasn't a single person around. Suddenly, I heard a noise. I stopped. Something was moving behind the bushes. I had seen a film about a wolf in a city park only the week before, and I was terrified. Then a small white dog ran out and started licking my shoes!",
                                       ["Üç zamanın bilinçli kullanımı", "Ritim: kısa ve uzun cümleler", "Beklenmedik son"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "Ne zamandır yapıyordu?", "Past perfect continuous ile geçmişteki bir andan önce süregelen eylemleri ve görünür sonuçlarını anlatabilirim.",
    {"kind": "dialogue", "title": "Havalimanında uzun bir gün", "lines": [
        {"speaker": "Zehra", "text": "How was your trip back from Berlin?"},
        {"speaker": "İlker", "text": "A nightmare! By the time the plane took off, we'd been sitting at the gate for six hours."},
        {"speaker": "Zehra", "text": "Six hours? Why?"},
        {"speaker": "İlker", "text": "There was a technical problem. And the worst thing is that I'd been planning to see my daughter's school play that evening."},
        {"speaker": "Zehra", "text": "Oh no. Did you miss it?"},
        {"speaker": "İlker", "text": "Completely. When I got home, she was in bed. She'd been crying, my wife said. I felt awful."}],
     "questions": [
        mc("How long had they been sitting at the gate?", ["Two hours", "Six hours", "All night"], 1, "\"we'd been sitting at the gate for six hours\""),
        mc("What had İlker been planning to do?", ["Go to a meeting", "See his daughter's school play", "Have dinner with his wife"], 1, "\"I'd been planning to see my daughter's school play\""),
     ]},
    {"explanation": "**Past perfect continuous:** had been + fiil-**ing**\n\nGeçmişteki bir andan **önce başlamış ve o ana kadar süren** eylemleri anlatır. **Süre** ve **süreç** vurgulanır.\n\n| Kullanım | Örnek |\n|---|---|\n| Geçmişteki bir ana kadar süren eylem (+ süre) | By the time the plane took off, we **had been sitting** there **for six hours**. |\n| Geçmişte görünen bir sonucun nedeni | Her eyes were red. She **had been crying**. |\n| Geçmişte yarım kalan bir plan | I **had been planning** to see the play, but ... |\n\n**Zaman çizgisi:**\n\n```\n  [had been sitting.................]X took off   →  şimdi\n   (6 saat boyunca)                  (geçmişteki an)\n```\n\n**Present perfect continuous ile karşılaştırın:**\n\n- I'm tired. I**'ve been working** all day. (Şimdiye kadar)\n- I was tired. I **had been working** all day. (Geçmişteki bir ana kadar)\n\n**Durum fiilleri** (know, be, have, like) continuous olmaz: She **had known** him for years. (~~had been knowing~~)",
     "examples": [{"en": "The ground was wet. It had been raining all night.", "tr": "Yer ıslaktı. Bütün gece yağmur yağmıştı."},
                  {"en": "She had been working there for ten years when the company closed.", "tr": "Şirket kapandığında on yıldır orada çalışıyordu."},
                  {"en": "How long had you been waiting when the bus finally came?", "tr": "Otobüs sonunda geldiğinde ne kadar zamandır bekliyordun?"}],
     "turkishNote": "Türkçedeki \"on yıldır orada çalışıyordu\" (şirket kapandığında) yapısı İngilizcede past perfect continuous'a denk gelir. Türkçe konuşanlar bu durumda genellikle \"she was working there for ten years\" der; ama geçmişteki bir ana kadar süren bir süreden bahsederken had been + -ing gerekir."},
    [
        mc("Şirket kapandığında on yıldır orada çalışıyordu.", ["She was working there for ten years when the company closed.", "She had been working there for ten years when the company closed."], 1, "Geçmişteki bir ana kadar süre → past perfect continuous."),
        mc("Görünen sonucun nedeni: \"His clothes were dirty. He ___ in the garden.\"", ["had been working", "has been working"], 0, "Geçmişteki sonuç → had been + -ing."),
        mc("Durum fiili: \"I ___ her for years before we got married.\"", ["had been knowing", "had known"], 1, "know → simple."),
        gap("We ___ (wait) for an hour when the doctor finally arrived.", ["had been waiting", "'d been waiting"], "had been + -ing."),
        gap("The road was wet. It ___ (rain).", ["had been raining", "'d been raining"], "had been + -ing."),
        gap("How long had you ___ (live) there before you moved?", ["been living"], "had been + -ing."),
        gap("I'd been ___ (plan) to call you, but I forgot.", ["planning"], "Yarım kalan plan."),
        order(["been", "They", "had", "arguing", "for", "hours", "when", "I", "arrived"], "They had been arguing for hours when I arrived.", "had been + -ing + süre + when + past simple.", "Ben geldiğimde saatlerdir tartışıyorlardı."),
        listen("When I finally found my glasses, I realised I'd been wearing them on my head the whole time. I'd been looking for them for twenty minutes!", "Gözlüklerini ne kadar süre aramıştı?", ["İki dakika", "Yirmi dakika", "Bütün gün"], 1, "\"I'd been looking for them for twenty minutes\""),
        typ("İngilizce yazın: \"Yer ıslaktı. Bütün gece yağmur yağmıştı.\"", variants("The ground was wet. It had been raining all night.", "The ground was wet. It'd been raining all night.", "The ground was wet. It had rained all night.", "The ground was wet, it had been raining all night.", "The ground was wet because it had been raining all night."), "The ground was wet. It had been raining all night."),
    ],
    {"kind": "speaking", "task": speak("Uzun süre beklediğiniz, uğraştığınız ya da bir şey planladığınız ama sonucun farklı çıktığı bir deneyimi anlatın. En az 3 past perfect continuous cümlesi kullanın (süre, görünen sonuç, yarım kalan plan).",
                                       "Last year I'd been saving money for months to buy a new laptop. I'd been checking prices every day, and when it finally went on sale, I went straight to the shop. I'd been standing in the queue for almost an hour when they announced that they'd sold the last one. I was furious! I'd been dreaming about that laptop for so long.",
                                       ["had been + -ing doğru", "Süre ve sonuç vurgusu", "Durum fiillerinde simple"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "Simple mı, continuous mu?", "Past perfect simple ile past perfect continuous arasındaki anlam farkını kavrayıp doğru seçimi yapabilirim.",
    {"kind": "text", "title": "Bir maratoncunun günlüğü", "body": "When I crossed the finish line, I burst into tears.\n\nI had been training for this marathon for eighteen months. I had been getting up at five every morning, and I had been running in rain, snow and burning summer heat.\n\nBy race day, I had run more than 3,000 kilometres in training. I had worn out four pairs of running shoes, and I had lost nine kilos.\n\nThree years earlier, I had never run more than five kilometres in my life. My doctor had told me to do more exercise, and I had chosen running almost by accident.\n\nNow, at the age of 52, I had finished my first marathon.",
     "questions": [
        mc("How long had the writer been training?", ["Six months", "Eighteen months", "Three years"], 1, "\"I had been training for this marathon for eighteen months\""),
        mc("Why did the writer start running?", ["A friend asked them to.", "Their doctor told them to exercise more.", "They wanted to win a race."], 1, "\"My doctor had told me to do more exercise\""),
     ]},
    {"explanation": "| Past perfect **simple** | Past perfect **continuous** |\n|---|---|\n| **Sonuç, tamamlanmış iş, sayı** | **Süreç, süre, tekrarlanan eylem** |\n| I **had run** 3,000 km. | I **had been running** for 18 months. |\n| I **had worn out** four pairs of shoes. | I **had been getting up** at five every morning. |\n| **How many / How much?** | **How long?** |\n\n**Aynı fiil, farklı vurgu:**\n\n- She **had painted** the kitchen. (Bitmişti; sonuç)\n- She **had been painting** the kitchen. (Süreç; üstü boyalıydı, belki bitmemişti)\n\n**Sayı ya da miktar varsa → simple:**\n\n- He **had written** three novels by the age of 30. (~~had been writing three novels~~)\n\n**Tek seferlik, kısa eylemler → simple:**\n\n- She **had broken** her leg. (~~had been breaking~~)\n\nBu, present perfect simple / continuous farkının (B1) geçmişteki karşılığıdır.",
     "examples": [{"en": "By midnight, they had been talking for four hours.", "tr": "Gece yarısına kadar dört saattir konuşuyorlardı."},
                  {"en": "By midnight, they had discussed every possible plan.", "tr": "Gece yarısına kadar mümkün olan her planı konuşmuşlardı."},
                  {"en": "She had been crying, but she had stopped by the time I arrived.", "tr": "Ağlamıştı ama ben vardığımda durmuştu."}],
     "turkishNote": "Türkçede \"-mıştı\" ve \"-yordu\" ayrımı bu farkı kabaca karşılar: \"3.000 km koşmuştum\" (simple, sonuç) ve \"18 aydır koşuyordum\" (continuous, süre). Cümlede bir sayı ya da \"kaç tane\" sorusu varsa simple, \"ne zamandır\" vurgusu varsa continuous seçin."},
    [
        mc("By the end of the day, she ___ 50 emails.", ["had written", "had been writing"], 0, "Sayı → simple."),
        mc("She was tired because she ___ emails all day.", ["had written", "had been writing"], 1, "Süreç → continuous."),
        mc("Tek seferlik eylem: \"He couldn't walk. He ___ his leg.\"", ["had been breaking", "had broken"], 1, "Kısa, tek olay → simple."),
        mc("How ___ had you been learning English before you moved?", ["many", "long"], 1, "How long → continuous."),
        gap("By 2020, they ___ (visit) 40 countries.", ["had visited", "'d visited"], "Sayı → simple."),
        gap("Her hands were dirty because she ___ (garden).", ["had been gardening", "'d been gardening"], "Görünür sonuç, süreç → continuous."),
        gap("By the time I arrived, they ___ (eat) all the cake!", ["had eaten", "'d eaten"], "Tamamlanmış sonuç → simple."),
        gap("He ___ (smoke) for twenty years before he finally gave up.", ["had been smoking", "'d been smoking"], "Süre → continuous."),
        listen("By the time I retired, I had been teaching for thirty-five years, and I had taught more than four thousand students.", "Kaç öğrenciye ders vermişti?", ["Otuz beş", "Dört yüzden fazla", "Dört binden fazla"], 2, "\"more than four thousand students\""),
        typ("İngilizce yazın: \"Gece yarısına kadar dört saattir konuşuyorlardı.\"", variants("By midnight, they had been talking for four hours.", "By midnight they had been talking for four hours.", "By midnight, they'd been talking for four hours.", "They had been talking for four hours by midnight."), "By midnight, they had been talking for four hours."),
    ],
    {"kind": "speaking", "task": speak("Hayatınızda uzun bir çabanın sonuna geldiğiniz bir anı anlatın (bir sınavı geçmek, bir projeyi bitirmek, bir hedefe ulaşmak). O ana kadar ne zamandır ne yapıyordunuz (continuous) ve neleri tamamlamıştınız (simple)? İkisini de en az ikişer kez kullanın.",
                                       "When I got my university acceptance letter, I couldn't stop smiling. I had been preparing for the exam for two years. I had been studying every evening and every weekend. By the day of the exam, I had solved more than 10,000 questions and I had taken 40 practice tests. I had also given up football for a whole year!",
                                       ["Simple ile sonuç ve sayılar", "Continuous ile süre ve süreç", "Doğru seçim"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Güçlü kelimelerle anlat", "Güçlü sıfatlar, derecelendirme zarfları ve anlatı bağlayıcılarıyla hikâyemi daha canlı hale getirebilirim.",
    {"kind": "dialogue", "title": "Kamp hikâyesi", "lines": [
        {"speaker": "Selim", "text": "So how was the camping trip?"},
        {"speaker": "Damla", "text": "Absolutely unforgettable. On the first night it was freezing, and we were utterly exhausted after the climb."},
        {"speaker": "Selim", "text": "Sounds tough."},
        {"speaker": "Damla", "text": "It gets better. All of a sudden, we heard something huge moving outside the tent. We were terrified!"},
        {"speaker": "Selim", "text": "No way! What was it?"},
        {"speaker": "Damla", "text": "Eventually, Can looked outside, and it turned out that it was a cow! We laughed until we cried. It was hilarious."}],
     "questions": [
        mc("How was the weather on the first night?", ["Very hot", "Very cold", "Rainy"], 1, "\"it was freezing\""),
        mc("What was outside the tent?", ["A bear", "A cow", "Another camper"], 1, "\"it turned out that it was a cow!\""),
     ]},
    {"explanation": "**Normal sıfatlar ve güçlü (aşırı) sıfatlar:**\n\n| Normal | Güçlü |\n|---|---|\n| tired | **exhausted** |\n| scared | **terrified** |\n| angry | **furious** |\n| cold | **freezing** |\n| funny | **hilarious** |\n| surprised | **astonished** |\n| sad | **devastated** |\n| good | **fantastic, superb** |\n\n**Zarf eşleşmeleri** çok önemlidir:\n\n| Normal sıfatlarla | Güçlü sıfatlarla |\n|---|---|\n| **very, extremely, a bit** | **absolutely, utterly, completely** |\n| very tired ✓ | absolutely exhausted ✓ |\n| ~~absolutely tired~~ ✗ | ~~very exhausted~~ ✗ |\n\n**really** ikisiyle de kullanılabilir: really tired ✓ / really exhausted ✓\n\n**Anlatı bağlayıcıları:**\n\n- **All of a sudden / Suddenly** → ani olay\n- **Meanwhile** → aynı anda başka yerde\n- **Eventually / In the end** → uzun süre sonra\n- **It turned out that ...** → sonradan anlaşıldı ki\n- **To my surprise / horror / relief** → duygu",
     "examples": [{"en": "I was absolutely furious when I saw the bill.", "tr": "Hesabı görünce öfkeden deliye döndüm."},
                  {"en": "Meanwhile, back at home, my parents were getting worried.", "tr": "Bu arada evde annemle babam endişelenmeye başlamıştı."},
                  {"en": "To my relief, the doctor said it was nothing serious.", "tr": "Doktorun ciddi bir şey olmadığını söylemesi beni rahatlattı."}],
     "turkishNote": "Türkçede \"çok\" kelimesini her sıfatla kullanabiliriz (çok yorgun, çok bitkin). İngilizcede ise very güçlü sıfatlarla kullanılmaz: \"very exhausted\" ya da \"very hilarious\" doğal değildir. Güçlü sıfatlarla absolutely, utterly, completely ya da really kullanın. \"eventually\" kelimesi Türkçedeki \"eventüel\" (muhtemel) anlamına gelmez; \"sonunda\" demektir."},
    [
        mc("Hangisi doğal?", ["very exhausted", "absolutely exhausted"], 1, "Güçlü sıfat → absolutely."),
        mc("Hangisi doğal?", ["absolutely tired", "extremely tired"], 1, "Normal sıfat → extremely / very."),
        mc("\"eventually\" ne demektir?", ["muhtemelen", "sonunda"], 1, "eventually = sonunda."),
        mc("\"Çok komik\" için güçlü sıfat:", ["hilarious", "furious", "freezing"], 0, "hilarious."),
        gap("It was ___ cold, so we stayed inside. (çok; normal sıfatla)", ["very", "extremely", "really"], "Normal sıfat → very."),
        gap("The view was ___ amazing. (kesinlikle; güçlü sıfatla)", ["absolutely", "utterly", "really", "completely"], "Güçlü → absolutely."),
        gap("It turned ___ that the man was a famous actor.", ["out"], "It turned out that."),
        gap("To my ___, nobody was hurt. (rahatlama)", ["relief"], "To my relief."),
        match([("tired", "exhausted"), ("angry", "furious"), ("scared", "terrified"), ("surprised", "astonished"), ("sad", "devastated")], "Normal sıfatı güçlüsüyle eşleştirin."),
        listen("We'd been driving for hours and we were completely lost. Meanwhile, the petrol light was flashing. Eventually, we found a tiny village, and to our surprise, the only petrol station was open.", "Sonunda ne buldular?", ["Bir otel", "Küçük bir köy ve açık bir benzin istasyonu", "Polis"], 1, "\"we found a tiny village... the only petrol station was open\""),
    ],
    {"kind": "speaking", "task": speak("Aşağıdaki \"düz\" hikâyeyi JAI'ye daha canlı şekilde yeniden anlatın: \"I went to a concert. It was good. I was tired. It was cold outside. I lost my phone. I found it later.\" Güçlü sıfatlar, doğru zarflar ve en az 4 anlatı bağlayıcısı ekleyin.",
                                       "Last Saturday I went to an absolutely fantastic concert. The band was superb. By the end, I was utterly exhausted from dancing. When we left, it was freezing outside. All of a sudden, I realised my phone had gone. I was devastated! Meanwhile, my friends were looking everywhere. Eventually, it turned out that a security guard had found it under a seat. To my relief, it wasn't even broken.",
                                       ["Güçlü sıfatlar", "Zarf-sıfat uyumu", "Anlatı bağlayıcıları", "Zaman çeşitliliği"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "İyi bir hikâyeci olmak", "Bir anıyı dinleyicinin ilgisini canlı tutacak şekilde yapılandırarak anlatabilir, dinlerken uygun tepkiler verebilirim.",
    {"kind": "dialogue", "title": "Akşam yemeğinde bir anı", "lines": [
        {"speaker": "Kaya", "text": "Did I ever tell you about the time I got locked in a museum?"},
        {"speaker": "Nehir", "text": "No! You're joking. What happened?"},
        {"speaker": "Kaya", "text": "Well, I'd been looking at this huge painting for ages, and I hadn't noticed that everyone else had left."},
        {"speaker": "Nehir", "text": "Oh no. So what did you do?"},
        {"speaker": "Kaya", "text": "Hang on, it gets worse. The moment I tried to open the door, the alarm went off!"},
        {"speaker": "Nehir", "text": "I can't believe it! And then?"},
        {"speaker": "Kaya", "text": "Long story short, I spent an hour explaining to the police that I wasn't an art thief."}],
     "questions": [
        mc("Why didn't Kaya notice that everyone had left?", ["He was asleep.", "He'd been looking at a painting for a long time.", "He was on the phone."], 1, "\"I'd been looking at this huge painting for ages\""),
        mc("What happened when Kaya tried to open the door?", ["It was locked forever.", "The alarm went off.", "A guard opened it."], 1, "\"the alarm went off!\""),
     ]},
    {"explanation": "**İyi bir anlatının yapısı:**\n\n| Bölüm | Amaç | Kalıplar |\n|---|---|---|\n| **Giriş** | Dikkati çek | **Did I ever tell you about the time** ...? / **You'll never guess what happened** ... / **I'll never forget** ... |\n| **Arka plan** | Sahneyi kur | **It was** a hot summer day ... / I'd been ... for ages |\n| **Gelişme** | Gerilimi artır | **Then, all of a sudden**, ... / **Hang on, it gets worse.** |\n| **Doruk** | Ana olay | **The moment** I ..., ... / **No sooner had** I ... **than** ... (resmî) |\n| **Son** | Toparla | **In the end**, ... / **Long story short**, ... / **Looking back**, ... |\n\n**Dinleyici olarak tepki vermek:**\n\n- Merak: **What happened next? / And then? / Go on!**\n- Şaşkınlık: **You're joking! / No way! / I can't believe it!**\n- Empati: **Oh no! / That must have been awful.** (must have → Ünite 7)\n- Mizah: **That's hilarious!**\n\n**the moment / as soon as** + past simple → \"-ır -maz\":\n\n- **The moment** I opened the door, the alarm **went off**.",
     "examples": [{"en": "Did I ever tell you about the time I met a famous footballer?", "tr": "Ünlü bir futbolcuyla tanıştığım zamanı sana anlattım mı hiç?"},
                  {"en": "The moment she walked in, everyone stopped talking.", "tr": "İçeri girdiği anda herkes konuşmayı kesti."},
                  {"en": "Long story short, we missed the flight.", "tr": "Uzun lafın kısası, uçağı kaçırdık."}],
     "turkishNote": "\"Uzun lafın kısası\" ifadesinin İngilizce karşılığı \"Long story short\" ya da \"To cut a long story short\"tur. Türkçede de olduğu gibi, iyi bir hikâyeci sonucu en başta söylemez; \"Hang on, it gets worse\" gibi ifadelerle dinleyiciyi bekletir."},
    [
        mc("Hikâyeye başlamak:", ["Did I ever tell you about the time ...?", "In conclusion, ..."], 0, "Giriş kalıbı."),
        mc("Merakla tepki:", ["What happened next?", "So what?", "I don't care."], 0, "Merak."),
        mc("\"Uzun lafın kısası\"", ["Short story long", "Long story short"], 1, "Long story short."),
        gap("The ___ I saw him, I knew something was wrong. (-dığı anda)", ["moment"], "The moment."),
        gap("Hang on, it gets ___! (daha da kötüleşiyor)", ["worse"], "it gets worse."),
        gap("You'll never ___ what happened!", ["guess"], "You'll never guess."),
        gap("I'd been waiting for ___ when the bus finally came. (çok uzun süre)", ["ages", "hours"], "for ages."),
        gap("___ back, it was the best day of my life. (geriye dönüp bakınca)", ["Looking"], "Looking back."),
        listen("You'll never guess who I saw at the airport. I was queuing for coffee, and the man in front of me turned around. It was my old maths teacher! He'd been living in Canada for twenty years.", "Konuşan havalimanında kimi gördü?", ["Eski matematik öğretmenini", "Ünlü bir oyuncuyu", "Kuzenini"], 0, "\"It was my old maths teacher!\""),
        typ("İngilizce yazın: \"İçeri girdiği anda herkes konuşmayı kesti.\" (she)", variants("The moment she walked in, everyone stopped talking.", "The moment she came in, everyone stopped talking.", "As soon as she walked in, everyone stopped talking.", "As soon as she came in, everyone stopped talking.", "The moment she entered, everyone stopped talking.", "Everyone stopped talking the moment she walked in.", "The moment she walked in everyone stopped talking."), "The moment she walked in, everyone stopped talking."),
    ],
    {"kind": "writing", "task": write("Bir hikâye yarışması için \"Hayatımın en tuhaf günü\" başlıklı kısa bir öykü yazın (180–220 kelime). Gerçek ya da hayali olabilir. Bütün anlatı zamanlarını (past perfect continuous dahil), en az 4 güçlü sıfat (doğru zarflarla), anlatı bağlayıcıları ve beklenmedik bir son kullanın.",
                                      "The Strangest Day of My Life\n\nIt was a grey Monday morning in November, and I was running late for the most important interview of my career. I had been preparing for weeks, and I had practised my answers so many times that I could say them in my sleep.\n\nI was rushing down the stairs of the metro when, all of a sudden, an elderly man in front of me slipped and fell. Everyone else hurried past. I stopped, helped him up and carried his bag to a bench. He had been visiting his granddaughter, he told me, and he was utterly exhausted.\n\nBy the time I reached the office, I was twenty minutes late and absolutely furious with myself. The receptionist looked at me coldly and told me to wait.\n\nEventually, the door opened and the director came out. I couldn't believe my eyes. It was the man from the metro! He smiled and said, \"I've been looking for someone who stops when others don't.\"\n\nLong story short, I got the job. Looking back, being late was the best mistake I've ever made.",
                                      ["Anlatı zamanları çeşitli ve doğru", "Past perfect continuous", "Güçlü sıfat + doğru zarf", "Anlatı bağlayıcıları", "Yapı ve beklenmedik son"])},
)

u.test([
    mc("Atmosfer kuran zaman:", ["Past simple", "Past continuous", "Past perfect"], 1, "Past continuous"),
    mc("She was exhausted. She ___ all night.", ["had been studying", "has been studying"], 0, "Past perfect continuous"),
    mc("By 2015, he ___ five books.", ["had written", "had been writing"], 0, "Sayı → simple"),
    mc("Durum fiili: \"They ___ each other for years before they got married.\"", ["had been knowing", "had known"], 1, "know"),
    mc("Hangisi doğal?", ["very furious", "absolutely furious"], 1, "Güçlü sıfat"),
    mc("Hangisi doğal?", ["absolutely cold", "very cold"], 1, "Normal sıfat"),
    gap("We ___ (walk) for hours when we finally saw the village.", ["had been walking", "'d been walking"], "had been + -ing"),
    gap("When I got to the station, the train ___ (already / leave).", ["had already left", "'d already left"], "Past perfect"),
    gap("I was cooking when the doorbell ___ (ring).", ["rang"], "Past simple"),
    gap("It turned ___ that she was his sister.", ["out"], "It turned out"),
    mc("\"eventually\"", ["sonunda", "muhtemelen"], 0, "eventually"),
    gap("The ___ I opened the door, the dog ran out. (-dığı anda)", ["moment"], "The moment"),
    listen("I'd been working at the café for only two days when a famous singer came in. I was so nervous that I dropped her coffee. To my surprise, she just laughed and helped me clean it up.", "Şarkıcı nasıl tepki verdi?", ["Kızdı", "Güldü ve temizlemeye yardım etti", "Kafeden çıktı"], 1, "\"she just laughed and helped me clean it up\""),
    typ("İngilizce yazın: \"Otobüs geldiğinde bir saattir bekliyorduk.\"", variants("We had been waiting for an hour when the bus came.", "We'd been waiting for an hour when the bus came.", "We had been waiting for an hour when the bus arrived.", "We'd been waiting for an hour when the bus arrived.", "When the bus came, we had been waiting for an hour.", "When the bus arrived, we had been waiting for an hour."), "We had been waiting for an hour when the bus came."),
    write("Bir yolculukta başınıza gelen (gerçek ya da hayali) beklenmedik bir olayı anlatın (180–220 kelime). Past simple, past continuous, past perfect ve past perfect continuous'u bilinçli kullanın; güçlü sıfatlar, anlatı bağlayıcıları ve dinleyicinin ilgisini çeken bir giriş ve son ekleyin.",
          "I'll never forget my first trip to Cappadocia. My friends and I had been planning it for months, and we had booked a hot-air balloon flight for sunrise on our second day.\n\nThat morning, we got up at four. It was absolutely freezing, and we were all half asleep. We had been waiting at the take-off field for almost an hour when the pilot announced that the flight was cancelled because of the wind. We were devastated.\n\nWe were walking back to the minibus when, all of a sudden, an old man waved at us from a small farmhouse. He had been watching us, he explained, and he wanted to invite us for breakfast. To our surprise, his wife had already prepared a huge table with fresh bread, cheese, eggs and homemade jam.\n\nMeanwhile, the sun was rising over the valleys, and dozens of balloons from other companies were flying in the distance. It turned out that only our company had cancelled!\n\nLooking back, I'm actually glad. I've seen balloons in a hundred photos, but that breakfast with strangers was something truly unique.",
          ["Dört anlatı zamanı doğru", "Güçlü sıfatlar ve zarflar", "Anlatı bağlayıcıları", "Etkileyici giriş ve son", "Akıcı ve düzenli metin"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

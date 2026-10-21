"""B1 Ünite 2: Değişimler."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("B1", 2, "Değişimler", "Life Changes",
         "Hayatımdaki değişiklikleri ve ne kadar süredir devam ettiklerini anlatabilir, geçmişte başlayıp hâlâ süren durumlar ile yakın zamandaki etkinlikleri ayırt edebilirim.",
         ["present perfect + for / since", "How long have you ...?", "present perfect ve past simple (süre)", "present perfect continuous", "present perfect simple ve continuous farkı", "recently / lately / since then"],
         ["yaşam değişiklikleri", "kariyer ve eğitim", "alışkanlık değişiklikleri"],
         {"title": "O zamandan beri...", "durationMinutes": 45,
          "goal": "Öğrenciler ikili olarak 5 yıl sonra karşılaşan iki eski arkadaşı canlandırır. Birbirlerine How long have you...? / What have you been doing? soruları sorarlar ve hayatlarındaki değişiklikleri for / since ile anlatırlar. Sonra her öğrenci, partnerinin hayatındaki en büyük değişikliği sınıfa aktarır."})

u.vocab([
    ("move house", "taşınmak", "We've moved house three times since 2015.", "2015'ten beri üç kez taşındık.", None),
    ("settle down", "düzen kurmak, yerleşmek", "After years of travelling, he wants to settle down.", "Yıllarca seyahat ettikten sonra yerleşmek istiyor.", None),
    ("get promoted", "terfi etmek", "She's just got promoted to manager.", "Yeni yönetici olarak terfi etti.", "promotion (terfi)"),
    ("change career", "kariyer değiştirmek", "He changed career at 40 and became a chef.", "40 yaşında kariyer değiştirip aşçı oldu.", None),
    ("quit", "bırakmak (iş, alışkanlık)", "I quit my job to start my own business.", "Kendi işimi kurmak için işimi bıraktım.", "quit → quit → quit"),
    ("retire", "emekli olmak", "My parents have been retired for five years.", "Ailem beş yıldır emekli.", None),
    ("split up", "ayrılmak (çift)", "They split up last year.", "Geçen yıl ayrıldılar.", "break up da olur."),
    ("start a family", "aile kurmak (çocuk sahibi olmak)", "They want to start a family soon.", "Yakında çocuk sahibi olmak istiyorlar.", None),
    ("take up", "başlamak (hobi)", "I've taken up running.", "Koşuya başladım.", None),
    ("give up", "bırakmak (alışkanlık)", "He's given up sugar.", "Şekeri bıraktı.", None),
    ("since", "-den beri (başlangıç noktası)", "I've lived here since 2018.", "2018'den beri burada yaşıyorum.", "since + zaman noktası"),
    ("for", "-dır, -dir (süre)", "I've lived here for six years.", "Altı yıldır burada yaşıyorum.", "for + süre"),
    ("How long ...?", "Ne kadar zamandır ...?", "How long have you known her?", "Onu ne zamandır tanıyorsun?", None),
    ("recently", "son zamanlarda", "Have you seen any good films recently?", "Son zamanlarda iyi bir film izledin mi?", None),
    ("lately", "son zamanlarda", "I've been feeling tired lately.", "Son zamanlarda yorgun hissediyorum.", "Genelde cümle sonunda."),
    ("since then", "o zamandan beri", "We met in 2010. Since then we've been best friends.", "2010'da tanıştık. O zamandan beri en iyi arkadaşız.", None),
    ("ever since", "-den beri hiç durmadan", "I've loved music ever since I was a child.", "Çocukluğumdan beri müziği severim.", None),
    ("degree", "diploma, derece (üniversite)", "She's been studying for her degree for three years.", "Üç yıldır diploması için okuyor.", None),
    ("course", "kurs", "I've been taking a cooking course.", "Bir yemek kursuna gidiyorum.", None),
    ("habit", "alışkanlık", "Changing a habit takes time.", "Bir alışkanlığı değiştirmek zaman alır.", None),
    ("grow", "büyümek, artmak", "Our company has grown a lot.", "Şirketimiz çok büyüdü.", "grow → grew → grown"),
    ("improve", "gelişmek, geliştirmek", "Your English has improved a lot!", "İngilizcen çok gelişti!", None),
    ("whole new", "bambaşka, yepyeni", "Moving abroad was a whole new life.", "Yurt dışına taşınmak bambaşka bir hayattı.", None),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Ne zamandır?", "for ve since ile hâlâ devam eden durumların ne zamandır sürdüğünü anlatabilirim.",
    {"kind": "dialogue", "title": "Mezunlar buluşması", "lines": [
        {"speaker": "Ela", "text": "Murat! I haven't seen you for ages! Where are you living now?"},
        {"speaker": "Murat", "text": "In Izmir. I've lived there since 2019."},
        {"speaker": "Ela", "text": "Wow. And are you still a teacher?"},
        {"speaker": "Murat", "text": "No, I changed career. I've worked as a web designer for three years now."},
        {"speaker": "Ela", "text": "That's a big change! Are you married?"},
        {"speaker": "Murat", "text": "Yes, I've been married for two years. And we've had a dog since last summer. What about you?"}],
     "questions": [
        mc("Since when has Murat lived in Izmir?", ["Since 2016", "Since 2019", "For two years"], 1, "\"I've lived there since 2019.\""),
        mc("How long has Murat been married?", ["Three years", "Two years", "Since last summer"], 1, "\"I've been married for two years.\""),
     ]},
    {"explanation": "Geçmişte başlayıp **şu anda da devam eden** durumlar için **present perfect** kullanılır.\n\n- I**'ve lived** in Izmir **since** 2019. (Hâlâ orada yaşıyorum.)\n- She**'s been** married **for** two years. (Hâlâ evli.)\n\n| for + **süre** | since + **başlangıç noktası** |\n|---|---|\n| for three years | since 2019 |\n| for six months | since January |\n| for a long time / ages | since last summer |\n| for two hours | since 9 o'clock |\n| for a week | since I was a child |\n\n**Soru:** **How long have** you **lived** here? – **For** five years. / **Since** 2020.\n\n**Durum fiilleri** (know, be, have, like) bu yapıda simple halde kalır:\n\n- I**'ve known** her **for** ten years. (~~I know her for ten years.~~)",
     "examples": [{"en": "I've known Selin since primary school.", "tr": "Selin'i ilkokuldan beri tanıyorum."},
                  {"en": "How long have you had your car?", "tr": "Arabana ne zamandır sahipsin?"},
                  {"en": "We haven't seen each other for ages.", "tr": "Uzun zamandır görüşmüyoruz."}],
     "turkishNote": "Türkçede \"2019'dan beri İzmir'de yaşıyorum\" deriz ve şimdiki zaman kullanırız; bu yüzden Türkçe konuşanlar \"I live here since 2019\" ya da \"I am living here for three years\" der. İngilizcede geçmişten bugüne süren bir durum için present perfect zorunludur: I've lived here since 2019."},
    [
        mc("Hangisi doğru?", ["I live here since 2018.", "I've lived here since 2018."], 1, "Geçmişten bugüne → present perfect."),
        mc("Hangisi doğru?", ["I know him for ten years.", "I've known him for ten years."], 1, "know → present perfect simple."),
        mc("___ three months", ["for", "since"], 0, "Süre → for."),
        mc("___ last Christmas", ["for", "since"], 1, "Başlangıç noktası → since."),
        mc("___ I was a child", ["for", "since"], 1, "since + cümle."),
        gap("She's worked here ___ 2020.", ["since"], "since + yıl."),
        gap("We've been married ___ fifteen years.", ["for"], "for + süre."),
        gap("How long ___ you had this phone?", ["have"], "How long have you...?"),
        listen("I've had this flat since I got my first job, so that's about eight years now. I love it, but it's getting a bit small.", "Ne zamandır bu dairede yaşıyor?", ["İlk işinden beri, yaklaşık sekiz yıl", "Sekiz aydır", "Geçen yıldan beri"], 0, "\"since I got my first job, so that's about eight years now\""),
        typ("İngilizce yazın: \"Uzun zamandır görüşmüyoruz.\"", variants("We haven't seen each other for ages.", "We haven't seen each other for a long time.", "We have not seen each other for ages.", "We haven't seen each other in ages.", "We haven't met for ages.", "We haven't met for a long time."), "We haven't seen each other + for ages."),
    ],
    {"kind": "speaking", "task": speak("Kendi hayatınızdan 5 durumu ne zamandır sürdüğüyle anlatın (yaşadığınız yer, işiniz/okulunuz, bir hobi, bir arkadaşlık, sahip olduğunuz bir şey). for ve since'i en az ikişer kez kullanın.",
                                       "I've lived in Ankara since 2012. I've worked at the same bank for seven years. I've known my best friend Deniz since we were six. I've had my cat for three years, and I've played the guitar since university.",
                                       ["Present perfect doğru", "for / since doğru seçildi", "Durum fiilleri simple halde"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "Hâlâ mı, bitti mi?", "Bitmiş bir süre ile hâlâ devam eden bir süreyi doğru zamanla ayırt edebilirim.",
    {"kind": "text", "title": "Bir yazarın biyografisi", "body": "Leyla Kara is a novelist and teacher.\n\nShe was born in Kayseri and lived there for eighteen years. Then she moved to Istanbul to study literature. She worked as a journalist for ten years, from 2005 to 2015.\n\nIn 2015 she published her first novel. Since then, she has written four more books, and she has won two national prizes.\n\nShe has lived in Bodrum for the last six years, and she has taught creative writing at a local school since 2020.",
     "questions": [
        mc("Is Leyla still a journalist?", ["Yes, she is.", "No, she isn't."], 1, "\"She worked as a journalist for ten years, from 2005 to 2015.\" (bitti)"),
        mc("How many books has she written in total?", ["Four", "Five", "Two"], 1, "İlk roman + \"four more books\" = beş."),
     ]},
    {"explanation": "**for** hem past simple hem present perfect ile kullanılabilir, ama anlam farklıdır:\n\n| Past simple + for | Present perfect + for |\n|---|---|\n| Süre **bitti**. | Süre **hâlâ devam ediyor**. |\n| She **lived** in Kayseri **for** 18 years. (Artık orada yaşamıyor.) | She**'s lived** in Bodrum **for** six years. (Hâlâ orada.) |\n| I **worked** there **for** ten years. | I**'ve worked** here **for** ten years. |\n\n**since** neredeyse her zaman **present perfect** ile kullanılır (bugüne kadar).\n\n**Sorularda:**\n\n- **How long did** you **live** in Paris? (Artık Paris'te değil.)\n- **How long have** you **lived** in Paris? (Hâlâ Paris'te.)\n\n**since + past simple cümle:**\n\n- I**'ve lived** here **since** I **got** married.",
     "examples": [{"en": "I studied in Germany for two years. Then I came back.", "tr": "İki yıl Almanya'da okudum. Sonra geri döndüm."},
                  {"en": "I've studied English for two years, and I'm still learning.", "tr": "İki yıldır İngilizce çalışıyorum ve hâlâ öğreniyorum."},
                  {"en": "He's been much happier since he changed jobs.", "tr": "İş değiştirdiğinden beri çok daha mutlu."}],
     "turkishNote": "Türkçede \"İki yıl Almanya'da okudum\" (bitti) ve \"İki yıldır İngilizce çalışıyorum\" (sürüyor) farkı -dı / -yor ekleriyle verilir. İngilizcede bu fark past simple / present perfect ile verilir. Bir durumun hâlâ sürüp sürmediğini kendinize sorun."},
    [
        mc("Ali artık Londra'da yaşamıyor:", ["He's lived in London for five years.", "He lived in London for five years."], 1, "Bitmiş süre → past simple."),
        mc("Ayşe hâlâ bu şirkette:", ["She worked here for ten years.", "She's worked here for ten years."], 1, "Devam eden → present perfect."),
        mc("Hâlâ Paris'te olan birine:", ["How long did you live in Paris?", "How long have you lived in Paris?"], 1, "Hâlâ orada → present perfect."),
        gap("My grandfather ___ in the army for twenty years. He retired in 1990. (serve)", ["served"], "Bitmiş → past simple."),
        gap("I've been happier since I ___ yoga. (take up → geçmiş)", ["took up"], "since + past simple."),
        gap("She ___ won three prizes since 2015.", ["has", "'s"], "since → present perfect."),
        mc("Hangisi doğru?", ["I've lived here since I've got married.", "I've lived here since I got married."], 1, "since + past simple cümle."),
        listen("I worked in a bank for twelve years, but I hated it. Three years ago I quit and opened a café. I've been my own boss since then, and I love it.", "Konuşan ne kadar süre bankada çalıştı?", ["Üç yıl", "On iki yıl", "Hâlâ çalışıyor"], 1, "\"I worked in a bank for twelve years\""),
        order(["has", "She", "taught", "at", "this", "school", "since", "2020"], "She has taught at this school since 2020.", "has + V3 + since + yıl.", "2020'den beri bu okulda öğretmenlik yapıyor."),
        typ("İngilizce yazın: \"İki yıl Almanya'da okudum.\" (artık orada değil)", variants("I studied in Germany for two years.", "I studied for two years in Germany."), "Bitmiş süre → I studied in Germany for two years."),
    ],
    {"kind": "speaking", "task": speak("Hayat çizginizi anlatın: geçmişte yaptığınız ve bitmiş 2 şeyi (past simple + for) ve hâlâ devam eden 3 şeyi (present perfect + for/since) söyleyin. Bir tane de since + past simple kullanın.",
                                       "I lived in Trabzon for twenty years. I worked in a hotel for two years when I was a student. I've lived in Istanbul since 2016. I've worked as a nurse for six years, and I've felt much more confident since I started this job.",
                                       ["Past simple ile bitmiş süre", "Present perfect ile devam eden süre", "since + past simple"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "Ne zamandır yapıyorsun?", "Present perfect continuous ile geçmişte başlayıp hâlâ devam eden etkinlikleri anlatabilirim.",
    {"kind": "dialogue", "title": "Spor salonunda", "lines": [
        {"speaker": "Tarık", "text": "You look fantastic! Have you been training a lot?"},
        {"speaker": "Nil", "text": "Thanks! Yes, I've been coming here four times a week since January."},
        {"speaker": "Tarık", "text": "That's impressive. How long have you been doing yoga?"},
        {"speaker": "Nil", "text": "Only for two months. And I've been eating more healthily too."},
        {"speaker": "Tarık", "text": "I should do the same. I've been sitting at a desk all day for years."},
        {"speaker": "Nil", "text": "Why don't you come with me tomorrow?"}],
     "questions": [
        mc("Since when has Nil been coming to the gym?", ["Since January", "For two months", "Since last year"], 0, "\"since January\""),
        mc("What else has Nil been doing?", ["Sleeping more", "Eating more healthily", "Running every day"], 1, "\"I've been eating more healthily too.\""),
     ]},
    {"explanation": "**Present perfect continuous** geçmişte başlayıp **hâlâ devam eden** (ya da az önce biten) **etkinlikleri** anlatır. **Süreç ve süre** vurgulanır.\n\n**Yapı:** have / has + **been** + fiil-**ing**\n\n| | |\n|---|---|\n| I / You / We / They **have been** | working |\n| He / She / It **has been** | working |\n\n- I**'ve been learning** English **for** three years.\n- She**'s been working** here **since** May.\n- **How long have** you **been waiting**? – **For** twenty minutes.\n\n**Az önce biten etkinlik + görünen sonuç:**\n\n- You look tired. – Yes, I**'ve been running**. (Koştum, o yüzden yorgunum.)\n- It**'s been raining**. The streets are wet.\n\n**Olumsuz:** I **haven't been sleeping** well lately.",
     "examples": [{"en": "I've been studying for this exam for weeks.", "tr": "Haftalardır bu sınava çalışıyorum."},
                  {"en": "How long have you been living here?", "tr": "Ne zamandır burada yaşıyorsun?"},
                  {"en": "Your eyes are red. Have you been crying?", "tr": "Gözlerin kızarmış. Ağladın mı?"}],
     "turkishNote": "Türkçedeki \"-dır / -dir ...-yor\" yapısı (üç yıldır çalışıyorum) genellikle present perfect continuous'a denk gelir: I've been working for three years. \"I am working here for three years\" çok yaygın bir hatadır; for/since ile şimdiki zaman kullanılmaz."},
    [
        mc("Hangisi doğru?", ["I'm learning English for three years.", "I've been learning English for three years."], 1, "Süre + devam eden etkinlik → present perfect continuous."),
        mc("Hangisi doğru?", ["She has been work here since May.", "She has been working here since May."], 1, "have been + -ing."),
        gap("How long have you been ___? (wait)", ["waiting"], "been + -ing."),
        gap("It's ___ raining all day. (been)", ["been"], "has been + -ing."),
        gap("I ___ been sleeping well lately. (haven't)", ["haven't", "have not"], "Olumsuz."),
        mc("Gözleri kırmızı, yüzü ıslak:", ["Have you cried?", "Have you been crying?"], 1, "Görünen sonuç + etkinlik → continuous."),
        order(["been", "I've", "studying", "for", "this", "exam", "for", "weeks"], "I've been studying for this exam for weeks.", "have been + -ing + for + süre.", "Haftalardır bu sınava çalışıyorum."),
        listen("Sorry I'm late! Have you been waiting long? – Not really, I've only been sitting here for about ten minutes.", "Ne kadar süredir bekliyor?", ["Yarım saat", "Yaklaşık on dakika", "Bir saat"], 1, "\"for about ten minutes\""),
        typ("İngilizce yazın: \"Ne zamandır burada yaşıyorsun?\"", variants("How long have you been living here?", "How long have you lived here?"), "How long have you been living here?"),
        typ("İngilizce yazın: \"Son zamanlarda çok çalışıyorum.\"", variants("I've been working a lot lately.", "I've been working a lot recently.", "Lately I've been working a lot.", "Recently I've been working a lot.", "I've been working hard lately.", "I've been working hard recently.", "I have been working a lot lately."), "I've been working a lot + lately."),
    ],
    {"kind": "speaking", "task": speak("Son zamanlarda yaptığınız 4 etkinliği ve ne zamandır yaptığınızı present perfect continuous ile anlatın. JAI size \"You look...!\" diyecek; nedenini continuous ile açıklayın.",
                                       "I've been learning to cook Italian food since last autumn. I've been running in the park for two months. I've been reading a lot of crime novels lately, and I've been planning a trip to Japan. ... I look tired because I've been working on a report all night.",
                                       ["have/has been + -ing", "for / since / lately", "Görünen sonuç açıklaması"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Kaç tane mi, ne kadar süre mi?", "Present perfect simple ve continuous arasında doğru seçimi yapabilirim.",
    {"kind": "dialogue", "title": "Yazarla röportaj", "lines": [
        {"speaker": "Reporter", "text": "You've written eight novels. How long have you been writing?"},
        {"speaker": "Writer", "text": "I've been writing since I was fifteen, but I've only been doing it professionally for ten years."},
        {"speaker": "Reporter", "text": "What are you working on now?"},
        {"speaker": "Writer", "text": "I've been writing a new book for about a year. I've finished six chapters so far."},
        {"speaker": "Reporter", "text": "And have you ever thought about writing for children?"},
        {"speaker": "Writer", "text": "Actually, I've been thinking about it a lot recently!"}],
     "questions": [
        mc("How many chapters of the new book has the writer finished?", ["Eight", "Six", "Ten"], 1, "\"I've finished six chapters so far.\""),
        mc("What has the writer been thinking about recently?", ["Retiring", "Writing for children", "Moving abroad"], 1, "\"I've been thinking about it a lot recently!\""),
     ]},
    {"explanation": "| Present perfect **simple** | Present perfect **continuous** |\n|---|---|\n| **Sonuç, tamamlanan iş** | **Süreç, etkinliğin kendisi** |\n| **Kaç tane / ne kadar?** (how many / how much) | **Ne zamandır?** (how long) |\n| I**'ve written** three emails. | I**'ve been writing** emails all morning. |\n| She**'s read** 200 pages. | She**'s been reading** for two hours. |\n| I**'ve painted** the kitchen. (bitti) | I**'ve been painting** the kitchen. (bitmeyebilir; üstüm boyalı) |\n\n**Sayı ya da miktar varsa → simple:**\n\n- I**'ve drunk** four coffees today. (~~I've been drinking four coffees~~)\n\n**Durum fiilleri → her zaman simple:**\n\n- I**'ve known** her for years. (~~I've been knowing~~)\n- He**'s had** that car since 2010.\n\n**Bazı fiillerde ikisi de doğru, anlam neredeyse aynı:** live, work, study, teach\n\n- I've lived / I've been living here for five years.",
     "examples": [{"en": "I've been cleaning all day, and I've cleaned three rooms.", "tr": "Bütün gün temizlik yapıyorum ve üç oda temizledim."},
                  {"en": "How many countries have you visited?", "tr": "Kaç ülke gezdin?"},
                  {"en": "How long have you been travelling?", "tr": "Ne zamandır seyahat ediyorsun?"}],
     "turkishNote": "Basit bir test: Cümlede bir sayı ya da \"kaç tane\" sorusu varsa simple; \"ne zamandır\" ya da \"bütün gün\" gibi bir süre vurgusu varsa continuous kullanın. \"so far\" (şimdiye kadar) genellikle simple ile kullanılır: I've read 50 pages so far."},
    [
        mc("I ___ three books this month.", ["'ve read", "'ve been reading"], 0, "Sayı → simple."),
        mc("I ___ this book for two weeks.", ["'ve read", "'ve been reading"], 1, "Süre, süreç → continuous."),
        mc("Hangisi doğru?", ["I've been knowing him for years.", "I've known him for years."], 1, "know → durum fiili."),
        mc("How ___ emails have you sent today?", ["long", "many"], 1, "Sayı → How many + simple."),
        gap("I've ___ four coffees today! (drink)", ["drunk", "had"], "Sayı → simple (V3)."),
        gap("She's been ___ the piano since she was six. (play)", ["playing"], "Süre → continuous."),
        gap("We've visited five museums ___ far. (şimdiye kadar)", ["so"], "so far."),
        mc("Üstü başı boya içinde, oda yarım:", ["I've painted the room.", "I've been painting the room."], 1, "Süreç, bitmemiş → continuous."),
        listen("I've been looking for a new flat for three months. I've seen about twenty flats, but I haven't found the right one yet.", "Kaç daire gördü?", ["Üç", "Yaklaşık yirmi", "Hiç"], 1, "\"I've seen about twenty flats\""),
        typ("Doğru zamanla yazın: \"I / call / her / five times / today\"", variants("I've called her five times today.", "I have called her five times today."), "Sayı → I've called her five times today."),
    ],
    {"kind": "speaking", "task": speak("Şu sıralar üzerinde çalıştığınız bir projeyi ya da hedefi anlatın (bir kurs, bir ev tadilatı, bir spor hedefi). Ne zamandır yaptığınızı continuous ile, şimdiye kadar ne kadar tamamladığınızı simple ile söyleyin.",
                                       "I've been training for a half marathon since March. I've been running four times a week. So far I've run about 300 kilometres and I've lost five kilos. I haven't run the full distance yet, but I've done 18 kilometres.",
                                       ["Continuous ile süre", "Simple ile sonuç / sayı", "so far / yet doğru"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Neler değişti?", "Uzun zamandır görmediğim birine hayatımdaki değişiklikleri doğal bir şekilde anlatabilirim.",
    {"kind": "text", "title": "Eski bir arkadaşa e-posta", "body": "Hi Jess,\n\nIt's been ages since we last spoke! I'm sorry I haven't written for so long. A lot has changed since we finished university.\n\nFirst, big news: I've moved to Barcelona! I've been living here for about eight months. I've been learning Spanish, and I've just passed my first exam.\n\nI've also changed career. I was an accountant for five years, but I never really enjoyed it. Since September I've been working as a tour guide, and I love it.\n\nThe only bad thing is that I've been missing my family a lot lately. What about you? What have you been doing? Have you finished your master's yet?\n\nLove,\nDefne",
     "questions": [
        mc("How long has Defne been living in Barcelona?", ["Five years", "About eight months", "Since university"], 1, "\"I've been living here for about eight months.\""),
        mc("What was Defne's old job?", ["Tour guide", "Teacher", "Accountant"], 2, "\"I was an accountant for five years\""),
     ]},
    {"explanation": "**Uzun aradan sonra yazmak / konuşmak:**\n\n- **It's been ages** since we last spoke. / Long time no see!\n- I'm sorry I **haven't written for** so long.\n- **A lot has changed since** ...\n\n**Haberleri vermek:**\n\n- **Big news:** I've moved / I've got engaged / I've changed jobs!\n- I**'ve just** + V3 → I've just passed my exam.\n- I**'ve been** + -ing **for** ... → I've been living here for eight months.\n\n**Değişimi anlatmak:**\n\n| Kalıp | Örnek |\n|---|---|\n| I used to ..., but now ... | I used to be shy, but now I'm more confident. (9. ünitede ayrıntılı) |\n| I was ... for ..., but since ... I've been ... | I was an accountant for five years, but since September I've been working as a guide. |\n| I've become + sıfat | I've become more patient. |\n| ... has changed a lot | My life has changed a lot. |\n\n**Karşı tarafa sormak:** What have you been doing? / What have you been up to? / Have you ... yet?",
     "examples": [{"en": "It's been ages since we last met!", "tr": "Son görüşmemizin üzerinden çok zaman geçti!"},
                  {"en": "What have you been up to?", "tr": "Neler yapıyorsun bu aralar?"},
                  {"en": "I've become much more confident since I moved here.", "tr": "Buraya taşındığımdan beri çok daha özgüvenli oldum."}],
     "turkishNote": "\"Neler yapıyorsun bu aralar?\" sorusunun en doğal karşılığı \"What have you been up to?\"dır. \"It's been ages\" kalıbında it's = it has: \"It has been ages since...\" (... beri uzun zaman oldu)."},
    [
        mc("Uzun aradan sonra selamlaşma:", ["It's been ages!", "It was ages!", "It is ages!"], 0, "It's (has) been ages."),
        mc("\"Neler yapıyorsun bu aralar?\"", ["What are you doing these times?", "What have you been up to?", "What did you do?"], 1, "What have you been up to?"),
        gap("I'm sorry I haven't written ___ so long.", ["for"], "for + süre."),
        gap("A lot has ___ since we finished school. (change)", ["changed"], "has + V3."),
        gap("I've ___ much more patient since I had kids. (become)", ["become"], "become → become (V3)."),
        gap("Since September I've ___ working as a tour guide.", ["been"], "have been + -ing."),
        gap("Have you finished your degree ___? (henüz)", ["yet"], "yet."),
        order(["been", "It's", "ages", "since", "we", "last", "spoke"], "It's been ages since we last spoke.", "It's been + süre + since + past simple.", "Son konuşmamızın üzerinden çok zaman geçti."),
        listen("Long time no see! So, what's new? – Well, I've just got engaged, and we've been looking for a flat together for a few weeks.", "Konuşan ne zamandır ev arıyor?", ["Birkaç aydır", "Birkaç haftadır", "Bir yıldır"], 1, "\"for a few weeks\""),
        typ("İngilizce yazın: \"Buraya taşındığımdan beri çok daha mutluyum.\"", variants("I've been much happier since I moved here.", "I have been much happier since I moved here.", "Since I moved here, I've been much happier.", "Since I moved here I've been much happier.", "I've been a lot happier since I moved here."), "I've been much happier + since I moved here."),
    ],
    {"kind": "writing", "task": write("Uzun zamandır görüşmediğiniz bir arkadaşınıza e-posta yazın (120–150 kelime). Defne'nin e-postasındaki kalıpları kullanın: selamlama, en az 3 değişiklik (present perfect simple ve continuous, for/since), bitmiş bir durum (past simple + for) ve sorular.",
                                      "Hi Can,\nIt's been ages since we last spoke! I'm sorry I haven't been in touch for so long. A lot has happened since your wedding.\nBig news first: I've got a new job! I worked at the bank for six years, but last spring I quit. Since June I've been working for a small design company, and I'm much happier. I've also moved to a flat near the sea. I've been living here for four months, and I've been swimming almost every morning.\nAnd guess what? I've taken up the guitar. I've been practising for two months and I've already learned ten songs!\nWhat have you been up to? Have you and Ayşe found a house yet? I'd love to hear from you.\nBest,\nMert",
                                      ["Present perfect simple / continuous doğru", "for / since doğru", "Past simple ile bitmiş durum", "E-posta kalıpları", "Sorular"])},
)

u.test([
    mc("Hangisi doğru?", ["I live here since 2015.", "I've lived here since 2015."], 1, "Present perfect"),
    mc("___ two weeks", ["for", "since"], 0, "for + süre"),
    mc("___ Monday", ["for", "since"], 1, "since + nokta"),
    mc("Hangisi doğru?", ["I know her for years.", "I've known her for years."], 1, "Durum fiili"),
    mc("Ahmet artık Londra'da değil:", ["He's lived in London for six years.", "He lived in London for six years."], 1, "Bitmiş → past simple"),
    gap("I've been happier since I ___ jobs. (change → geçmiş)", ["changed"], "since + past simple"),
    gap("How long have you been ___ English? (learn)", ["learning"], "been + -ing"),
    mc("Hangisi doğru?", ["I'm working here for five years.", "I've been working here for five years."], 1, "Present perfect continuous"),
    mc("I ___ four cups of tea today.", ["'ve drunk", "'ve been drinking"], 0, "Sayı → simple"),
    mc("You're all wet!", ["Have you swum?", "Have you been swimming?"], 1, "Görünen sonuç → continuous"),
    gap("I've read 100 pages so ___.", ["far"], "so far"),
    mc("\"Bu aralar neler yapıyorsun?\"", ["What have you been up to?", "What are you up?"], 0, "What have you been up to?"),
    listen("I've been teaching for twenty years. I taught in a village school for the first five years, and I've worked in this city since 2009.", "Köy okulunda kaç yıl öğretmenlik yaptı?", ["Yirmi", "Beş", "On beş"], 1, "\"I taught in a village school for the first five years\""),
    typ("İngilizce yazın: \"Haftalardır bu projede çalışıyorum.\"", variants("I've been working on this project for weeks.", "I have been working on this project for weeks."), "I've been working on this project + for weeks."),
    write("\"Son 5 yılda hayatım nasıl değişti?\" başlıklı bir paragraf yazın (120–150 kelime). Present perfect simple ve continuous, for / since, past simple ile bitmiş durumlar ve recently / lately / since then kullanın.",
          "My life has changed a lot in the last five years. Five years ago I was a student in Eskişehir. I lived in a small flat with three friends for four years, and I worked part-time in a café. Then, in 2021, I got my first job in Istanbul. I've worked as a software developer since then, and I've been promoted once. I've also met the love of my life. We've been together for three years, and we've been living together since last summer. Recently I've been learning to cook, and I've become much more organised. I've also been trying to exercise more lately. I think I've grown up a lot!",
          ["Present perfect simple / continuous", "for / since doğru", "Past simple ile bitmiş durumlar", "Zaman ifadeleri (recently, since then)", "Akıcı ve düzenli paragraf"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

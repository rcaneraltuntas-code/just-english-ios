"""A2 Ünite 6: Deneyimler."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("A2", 6, "Deneyimler", "Experiences",
         "Hayatım boyunca yaşadığım ve hiç yaşamadığım deneyimleri anlatabilir, başkalarına deneyimlerini sorup ayrıntılarını öğrenebilirim.",
         ["present perfect: have / has + V3", "Have you ever ...? / never", "been ve gone farkı", "present perfect ve past simple", "once / twice / ... times"],
         ["deneyimler", "başarılar", "macera etkinlikleri"],
         {"title": "Hiç ... yaptın mı?", "durationMinutes": 45,
          "goal": "Öğrencilere 'Find someone who has...' kartları verilir (ör. ... has been to another country, ... has met a famous person). Öğrenciler Have you ever...? sorusuyla birini bulur, sonra past simple ile ayrıntı sorar (When did you...? Who was it?). Sınıfla en ilginç deneyimler paylaşılır."})

u.vocab([
    ("ever", "hiç (soru)", "Have you ever been to Japan?", "Hiç Japonya'ya gittin mi?", "Soru cümlelerinde."),
    ("never", "hiç (olumsuz), asla", "I've never eaten sushi.", "Hiç suşi yemedim.", "never + olumlu fiil"),
    ("been (to)", "bulunmuş, gitmiş (ve dönmüş)", "She's been to Paris three times.", "Paris'e üç kez gitti.", "go'nun V3'ü olarak deneyimde."),
    ("gone (to)", "gitmiş (ve hâlâ orada)", "He's gone to the shop. He's not here.", "Markete gitti, burada değil.", None),
    ("once", "bir kez", "I've been on a plane once.", "Bir kez uçağa bindim.", None),
    ("twice", "iki kez", "We've seen that film twice.", "O filmi iki kez izledik.", "three times, four times..."),
    ("try", "denemek", "Have you ever tried Indian food?", "Hiç Hint yemeği denedin mi?", "try → tried → tried"),
    ("climb", "tırmanmak", "I've climbed Mount Erciyes.", "Erciyes Dağı'na tırmandım.", "b okunmaz: /klaɪm/"),
    ("ride a horse", "ata binmek", "Have you ever ridden a horse?", "Hiç ata bindin mi?", "ride → rode → ridden"),
    ("fly", "uçmak", "I've never flown in a helicopter.", "Hiç helikopterle uçmadım.", "fly → flew → flown"),
    ("break", "kırmak", "Have you ever broken your arm?", "Hiç kolunu kırdın mı?", "break → broke → broken"),
    ("lose", "kaybetmek", "I've lost my keys twice this month.", "Bu ay iki kez anahtarlarımı kaybettim.", "lose → lost → lost"),
    ("meet", "tanışmak", "Have you ever met a famous person?", "Hiç ünlü biriyle tanıştın mı?", "meet → met → met"),
    ("win", "kazanmak", "She's won three gold medals.", "Üç altın madalya kazandı.", "win → won → won"),
    ("bungee jumping", "bungee jumping (yüksekten atlama)", "I've never been bungee jumping.", "Hiç bungee jumping yapmadım.", "go bungee jumping"),
    ("skydiving", "paraşütle atlama", "My brother has been skydiving twice.", "Erkek kardeşim iki kez paraşütle atladı.", None),
    ("scuba diving", "tüplü dalış", "We went scuba diving in Kaş.", "Kaş'ta tüplü dalış yaptık.", None),
    ("experience", "deneyim", "It was an amazing experience.", "Muhteşem bir deneyimdi.", None),
    ("achievement", "başarı", "Learning English is a big achievement.", "İngilizce öğrenmek büyük bir başarı.", None),
    ("prize", "ödül", "He's won a prize for his photos.", "Fotoğraflarıyla bir ödül kazandı.", None),
    ("abroad", "yurt dışı", "Have you ever lived abroad?", "Hiç yurt dışında yaşadın mı?", None),
    ("in my life", "hayatımda", "I've never been so happy in my life.", "Hayatımda hiç bu kadar mutlu olmadım.", None),
    ("bucket list", "ölmeden önce yapılacaklar listesi", "Visiting Iceland is on my bucket list.", "İzlanda'yı ziyaret etmek listemde var.", None),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Yaptım, gördüm", "Present perfect ile hayatımda yaşadığım deneyimleri söyleyebilirim.",
    {"kind": "text", "title": "Bir gezginin profili", "body": "Hi! I'm Ozan and I'm a travel blogger.\n\nI've visited 42 countries. I've slept in a tent in the Sahara Desert and I've swum with dolphins in Mexico. I've eaten some very strange food, too: I've tried insects in Thailand!\n\nI've met amazing people everywhere. My parents have travelled a lot too. My mother has been to every continent except Antarctica.\n\nBut there's one thing I haven't done yet: I haven't seen the Northern Lights. That's next!",
     "questions": [
        mc("How many countries has Ozan visited?", ["24", "42", "4"], 1, "\"I've visited 42 countries.\""),
        mc("What hasn't Ozan done?", ["Swum with dolphins", "Seen the Northern Lights", "Eaten insects"], 1, "\"I haven't seen the Northern Lights.\""),
     ]},
    {"explanation": "**Present perfect** hayatımızın herhangi bir zamanında yaşadığımız **deneyimleri** anlatır. **Ne zaman** olduğu önemli değildir ve söylenmez.\n\n**Yapı:** have / has + **V3** (past participle)\n\n| | |\n|---|---|\n| I / You / We / They **have** ('ve) | visited |\n| He / She / It **has** ('s) | visited |\n\n**V3 (past participle):**\n\n- Düzenli fiiller: V2 ile aynı → visit**ed**, tri**ed**, travel**led**\n- Düzensiz fiiller ayrıca öğrenilir:\n\n| V1 | V2 | V3 |\n|---|---|---|\n| eat | ate | **eaten** |\n| see | saw | **seen** |\n| swim | swam | **swum** |\n| meet | met | **met** |\n| sleep | slept | **slept** |\n| write | wrote | **written** |\n\n**Olumsuz:** haven't / hasn't + V3 → I **haven't seen** it.",
     "examples": [{"en": "I've been to Germany.", "tr": "Almanya'ya gittim (bulundum)."},
                  {"en": "She's written three books.", "tr": "Üç kitap yazdı."},
                  {"en": "We haven't seen the new film.", "tr": "Yeni filmi izlemedik."}],
     "turkishNote": "Türkçede deneyim için de \"-di\" kullanırız: \"Paris'e gittim.\" İngilizcede zaman belli değilse present perfect (I've been to Paris), zaman belliyse past simple (I went to Paris last year) kullanılır. \"He's\" hem \"he is\" hem \"he has\" olabilir: He's visited (has), He's visiting (is)."},
    [
        match([("eat", "eaten"), ("see", "seen"), ("write", "written"), ("swim", "swum"), ("meet", "met")], "Fiilleri V3 halleriyle eşleştirin."),
        mc("Hangisi doğru?", ["I have visit Rome.", "I have visited Rome.", "I have visiting Rome."], 1, "have + V3."),
        mc("Hangisi doğru?", ["She have seen it.", "She has seen it.", "She has saw it."], 1, "she → has + V3.", {2: "saw V2'dir; V3 seen olmalı."}),
        gap("We've ___ in a tent many times. (sleep)", ["slept"], "sleep → slept."),
        gap("My dad ___ never travelled by plane.", ["has", "'s"], "he → has."),
        gap("I've ___ some strange food in my life. (eat)", ["eaten"], "eat → eaten."),
        gap("They ___ seen the sea. They live in the mountains. (haven't)", ["haven't", "have not"], "Olumsuz: haven't."),
        listen("I've lived in three countries and I've learned four languages. But I've never learned to swim!", "Konuşan neyi hiç öğrenmedi?", ["Dil", "Yüzmek", "Araba kullanmak"], 1, "\"I've never learned to swim!\""),
        order(["has", "She", "written", "two", "books"], "She has written two books.", "Özne + has + V3 + nesne.", "İki kitap yazdı."),
        typ("İngilizce yazın: \"Yeni filmi izlemedim.\"", variants("I haven't seen the new film.", "I have not seen the new film.", "I haven't watched the new film.", "I haven't seen the new movie.", "I haven't watched the new movie."), "I haven't + seen + the new film."),
    ],
    {"kind": "speaking", "task": speak("Ozan gibi kendi deneyim profilinizi anlatın: yaptığınız 4 ilginç şeyi ve henüz yapmadığınız 1 şeyi present perfect ile söyleyin.",
                                       "I've visited eight cities in Turkey. I've climbed Uludağ and I've swum in Lake Van. I've met a famous footballer! But I haven't been abroad.",
                                       ["have/has + V3 doğru", "Düzensiz V3'ler doğru", "haven't/hasn't doğru"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "Hiç ... yaptın mı?", "Have you ever ...? ile deneyim sorabilir, never ile cevap verebilirim.",
    {"kind": "dialogue", "title": "Doğum günü yemeğinde", "lines": [
        {"speaker": "Bora", "text": "Have you ever done anything really dangerous?"},
        {"speaker": "Nil", "text": "Yes, I have! I've been skydiving."},
        {"speaker": "Bora", "text": "No way! I've never done anything like that. Have you ever been bungee jumping?"},
        {"speaker": "Nil", "text": "No, I haven't. I'm too scared!"},
        {"speaker": "Bora", "text": "Ha ha. Has your brother ever tried it?"},
        {"speaker": "Nil", "text": "Yes, he has. Twice! He loves it."}],
     "questions": [
        mc("Has Nil been skydiving?", ["Yes, she has.", "No, she hasn't."], 0, "\"Yes, I have! I've been skydiving.\""),
        mc("How many times has Nil's brother been bungee jumping?", ["Once", "Twice", "Never"], 1, "\"Twice!\""),
     ]},
    {"explanation": "**Soru:** Have / Has + özne + **ever** + V3?\n\n- **Have** you **ever been** to Italy? – Yes, I **have**. / No, I **haven't**.\n- **Has** she **ever met** a famous person? – Yes, she **has**. / No, she **hasn't**.\n\n**ever** (hiç) soruda, V3'ten önce gelir.\n\n**never** (hiç / asla) olumlu fiille kullanılır ve cümleye olumsuz anlam verir:\n\n- I**'ve never** eaten sushi. (~~I haven't never~~)\n- He**'s never** flown.\n\n**Kısa cevaplar:** Yes, I have. / No, I haven't. / No, never.",
     "examples": [{"en": "Have you ever lost your passport?", "tr": "Hiç pasaportunu kaybettin mi?"},
                  {"en": "I've never ridden a horse.", "tr": "Hiç ata binmedim."},
                  {"en": "Has your mum ever lived abroad? – No, she hasn't.", "tr": "Annen hiç yurt dışında yaşadı mı? – Hayır."}],
     "turkishNote": "Türkçede \"hiç\" hem soruda hem olumsuzda kullanılır; İngilizcede soruda ever, olumsuzda never ya da \"not ... ever\" denir. İngilizcede çift olumsuz yanlıştır: \"I haven't never\" değil, \"I've never\" ya da \"I haven't ever\"."},
    [
        mc("Hangisi doğru?", ["Did you ever been to Spain?", "Have you ever been to Spain?", "Have you ever went to Spain?"], 1, "Have + you + ever + V3?"),
        mc("Hangisi doğru?", ["I haven't never seen it.", "I've never seen it."], 1, "never + olumlu fiil (çift olumsuz yok)."),
        mc("\"Has he ever broken his leg?\" (Hayır.)", ["No, he hasn't.", "No, he didn't.", "No, he isn't."], 0, "No, he hasn't."),
        gap("Have you ___ eaten snails? (hiç)", ["ever"], "Soruda ever."),
        gap("I've ___ been on a boat. I'm scared of water. (hiç)", ["never"], "Olumsuz anlam → never."),
        gap("___ your parents ever visited London?", ["Have"], "parents → Have."),
        gap("Have you ever ___ a horse? (ride)", ["ridden"], "ride → ridden."),
        order(["you", "Have", "ever", "met", "a", "famous", "person", "?"], "Have you ever met a famous person?", "Have + you + ever + V3?", "Hiç ünlü biriyle tanıştın mı?"),
        listen("Have you ever flown in a hot-air balloon? – Yes, I have. In Kapadokya. It was amazing!", "Balona nerede bindi?", ["Pamukkale'de", "Kapadokya'da", "Bodrum'da"], 1, "\"In Kapadokya.\""),
        typ("İngilizce yazın: \"Hiç ata binmedim.\"", variants("I've never ridden a horse.", "I have never ridden a horse.", "I haven't ever ridden a horse."), "I've never + ridden a horse."),
    ],
    {"kind": "speaking", "task": speak("JAI ile 'Hiç ... yaptın mı?' oyunu oynayın: JAI'ye 5 tane Have you ever...? sorusu sorun, sonra JAI'nin sorularına Yes, I have / No, I've never... ile cevap verin.",
                                       "Have you ever been to Africa? Have you ever eaten snails? Have you ever won a prize? Have you ever climbed a mountain? Have you ever broken a bone? ... No, I've never been skydiving.",
                                       ["Have you ever + V3 doğru", "never ile cevap", "Kısa cevaplar doğru"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "Been mi, gone mu?", "been ve gone farkını bilir, bir şeyi kaç kez yaptığımı söyleyebilirim.",
    {"kind": "dialogue", "title": "Ofiste", "lines": [
        {"speaker": "Visitor", "text": "Hello, is Mr Yalçın here?"},
        {"speaker": "Secretary", "text": "Sorry, he's gone to Ankara for a meeting. He's back on Thursday."},
        {"speaker": "Visitor", "text": "Oh. Has he been to the new office in Izmir yet?"},
        {"speaker": "Secretary", "text": "Yes, he has. He's been there twice this month."},
        {"speaker": "Visitor", "text": "I've been there once. It's beautiful."}],
     "questions": [
        mc("Where is Mr Yalçın now?", ["In the office", "In Ankara", "In Izmir"], 1, "\"he's gone to Ankara\" → hâlâ orada."),
        mc("How many times has he been to the Izmir office this month?", ["Once", "Twice", "Never"], 1, "\"He's been there twice this month.\""),
     ]},
    {"explanation": "**go** fiilinin iki V3 hali vardır:\n\n| | Anlam | Örnek |\n|---|---|---|\n| **been to** | gitti ve **döndü** (deneyim) | She's **been to** Ankara. (Şimdi burada.) |\n| **gone to** | gitti, **hâlâ orada** | She's **gone to** Ankara. (Şimdi orada.) |\n\n**Kaç kez?**\n\n- **How many times** have you been to Istanbul?\n- once (bir kez), twice (iki kez), three times, many times, a few times\n\nSıklık ifadesi genellikle **cümlenin sonuna** gelir: I've seen that film **three times**.\n\n**Bu dönem içinde:** this week / this month / this year (dönem bitmedi → present perfect)\n\n- I've had three coffees **today**.",
     "examples": [{"en": "Where's Mum? – She's gone to the market.", "tr": "Annem nerede? – Pazara gitti."},
                  {"en": "I've been to Antalya many times.", "tr": "Antalya'ya birçok kez gittim."},
                  {"en": "How many times have you seen this film?", "tr": "Bu filmi kaç kez izledin?"}],
     "turkishNote": "Türkçede \"gitti\" kelimesi hem been hem gone anlamına gelebilir; bağlamdan anlarız. İngilizcede seçim zorunludur: Burada olmayan biri için \"He's gone to...\", deneyim için \"He's been to...\". \"Have you ever gone to...?\" yerine \"Have you ever been to...?\" denir."},
    [
        mc("Ali burada değil, hâlâ bankada:", ["He's been to the bank.", "He's gone to the bank."], 1, "Hâlâ orada → gone."),
        mc("Deneyim: \"Hiç Mısır'a gittin mi?\"", ["Have you ever gone to Egypt?", "Have you ever been to Egypt?"], 1, "Deneyim → been to."),
        gap("I've ___ to Rome twice. I loved it! (gittim, döndüm)", ["been"], "Deneyim → been."),
        gap("Where's Elif? – She's ___ to the gym. (hâlâ orada)", ["gone"], "Hâlâ orada → gone."),
        gap("How many ___ have you been to Bursa?", ["times"], "How many times."),
        mc("\"İki kez\"", ["two times", "twice", "second"], 1, "twice (two times da anlaşılır ama twice doğaldır)."),
        order(["seen", "I've", "that", "film", "three", "times"], "I've seen that film three times.", "Sıklık cümle sonunda.", "O filmi üç kez izledim."),
        listen("Where's Kerem? – He's gone to Germany for a conference. He's been there many times for work.", "Kerem şu an nerede?", ["Ofiste", "Almanya'da", "Evde"], 1, "\"He's gone to Germany\""),
        typ("İngilizce yazın: \"Bugün üç kahve içtim.\"", variants("I've had three coffees today.", "I have had three coffees today.", "I've drunk three coffees today.", "I have drunk three coffees today.", "Today I've had three coffees."), "I've had + three coffees + today."),
        mc("Hangisi doğru? (Şu an Bodrum'dasın ve telefonda konuşuyorsun.)", ["I've gone to Bodrum.", "I've been to Bodrum.", "I'm in Bodrum."], 2, "Konuşan kişi kendisi için gone kullanmaz: I'm in Bodrum."),
    ],
    {"kind": "speaking", "task": speak("Türkiye'de ya da yurt dışında gittiğiniz 3 yeri ve kaç kez gittiğinizi söyleyin. Sonra ailenizden şu an evde olmayan birinin nereye gittiğini 'gone' ile anlatın.",
                                       "I've been to Izmir many times and I've been to Trabzon once. I've been to Greece twice. My sister isn't at home now. She's gone to the cinema with her friends.",
                                       ["been to doğru", "once / twice / times doğru", "gone doğru"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Ne zaman, nerede?", "Bir deneyimden bahsedip ayrıntılarını past simple ile anlatabilirim.",
    {"kind": "dialogue", "title": "İş görüşmesi", "lines": [
        {"speaker": "Interviewer", "text": "Have you ever worked in a team?"},
        {"speaker": "Ayşe", "text": "Yes, I have. I worked in a team of eight at my last job."},
        {"speaker": "Interviewer", "text": "Have you ever lived abroad?"},
        {"speaker": "Ayşe", "text": "Yes. I lived in Dublin for a year."},
        {"speaker": "Interviewer", "text": "When did you go there?"},
        {"speaker": "Ayşe", "text": "In 2019. I studied English and worked in a café. It was a great experience."}],
     "questions": [
        mc("Where did Ayşe live abroad?", ["London", "Dublin", "Berlin"], 1, "\"I lived in Dublin for a year.\""),
        mc("When did she go there?", ["In 2019", "Last year", "In 2009"], 0, "\"In 2019.\""),
     ]},
    {"explanation": "Bir sohbette genellikle **present perfect ile başlarız** (deneyim var mı?), sonra **ayrıntılara past simple ile geçeriz** (ne zaman, nerede, nasıl?).\n\n- A: **Have** you ever **been** to Paris? (deneyim)\n- B: Yes, I **have**. I **went** there in 2020. (ayrıntı, zaman belli)\n- A: **Did** you **like** it?\n- B: Yes, I **loved** it.\n\n| Present perfect | Past simple |\n|---|---|\n| zaman belli değil / önemli değil | zaman belli: yesterday, last year, in 2019, ago, when I was ... |\n| I've met a famous singer. | I met him **at a concert last summer**. |\n\n**Dikkat:** belli bir geçmiş zamanla present perfect kullanılmaz: ~~I've been to Paris last year.~~",
     "examples": [{"en": "I've broken my arm. I broke it when I was nine.", "tr": "Kolumu kırdım. Dokuz yaşındayken kırdım."},
                  {"en": "Have you ever won anything? – Yes, I won a competition at school.", "tr": "Hiç bir şey kazandın mı? – Evet, okulda bir yarışma kazandım."},
                  {"en": "She's been to India. She went there two years ago.", "tr": "Hindistan'a gitti. İki yıl önce gitti."}],
     "turkishNote": "Türkçe konuşanların en sık hatası, past simple gereken yerde present perfect kullanmaktır: \"I have seen him yesterday\" yanlıştır. yesterday, last ..., ago, in + yıl gibi ifadeler gördüğünüzde past simple kullanın."},
    [
        mc("Hangisi doğru?", ["I've been to Paris last year.", "I went to Paris last year."], 1, "last year → past simple."),
        mc("Hangisi doğru?", ["I saw him yesterday.", "I've seen him yesterday."], 0, "yesterday → past simple."),
        mc("Zaman belli değil:", ["I've met a famous actor.", "I met a famous actor."], 0, "Deneyim, zaman yok → present perfect."),
        gap("Have you ever been to Spain? – Yes, I ___ there in 2018. (go)", ["went"], "Zaman belli → went."),
        gap("She ___ won three prizes in her life.", ["has", "'s"], "Deneyim → has + V3."),
        gap("When ___ you meet him?", ["did"], "When → past simple."),
        mc("\"Have you ever tried kokoreç?\" \"Yes. I ___ it in Izmir last week.\"", ["have tried", "tried"], 1, "last week → past simple."),
        listen("Have you ever been to a football match? – Yes, I went to a Fenerbahçe match two years ago. The atmosphere was incredible.", "Maça ne zaman gitti?", ["Geçen hafta", "İki yıl önce", "Hiç gitmedi"], 1, "\"two years ago\""),
        order(["did", "When", "you", "go", "there", "?"], "When did you go there?", "When + did + you + go?", "Oraya ne zaman gittin?"),
        typ("İngilizce yazın: \"Kolumu kırdım. Dokuz yaşındayken kırdım.\"", variants("I've broken my arm. I broke it when I was nine.", "I have broken my arm. I broke it when I was nine.", "I've broken my arm. I broke it when I was 9."), "I've broken my arm. + I broke it when I was nine."),
    ],
    {"kind": "speaking", "task": speak("JAI ile iş görüşmesi yapın. JAI Have you ever...? soruları soracak; önce present perfect ile cevap verin, sonra past simple ile ayrıntı ekleyin (ne zaman, nerede).",
                                       "Yes, I have. I've worked with international customers. I worked for a tourism company in Antalya from 2018 to 2021. I also lived in Germany for six months in 2022.",
                                       ["Present perfect ile başladı", "Ayrıntıda past simple", "Zaman ifadeleri doğru"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Başarılarım ve hayallerim", "Hayatımdaki başarıları anlatabilir ve henüz yapmadığım hayallerimi paylaşabilirim.",
    {"kind": "text", "title": "Forumda: Ölmeden önce yapılacaklar listesi", "body": "What's on your bucket list? Here's mine!\n\n✓ Run a marathon – I've done it! I ran the Istanbul Marathon in 2022. It was the hardest thing I've ever done.\n✓ Learn a musical instrument – I've learned to play the bağlama! I started three years ago.\n✗ See the pyramids – I've never been to Egypt, but I'm going to go next year!\n✗ Write a book – I haven't written one yet, but I've started.\n\nWhat about you? What have you done, and what haven't you done yet?\n— Emre_34",
     "questions": [
        mc("When did Emre run a marathon?", ["In 2020", "In 2022", "He hasn't done it"], 1, "\"I ran the Istanbul Marathon in 2022.\""),
        mc("What is Emre going to do next year?", ["Write a book", "See the pyramids", "Run a marathon"], 1, "\"I'm going to go next year!\" (Egypt)"),
     ]},
    {"explanation": "**Başarılar:**\n\n- I**'ve passed** my driving test.\n- She**'s won** a prize.\n- We**'ve learned** to dance.\n\n**yet** (henüz) olumsuz cümlede ve soruda, cümle sonunda:\n\n- I **haven't written** a book **yet**.\n- **Have** you **finished yet**?\n\n(yet, already ve just 7. ünitede ayrıntılı gelecek.)\n\n**Superlative + present perfect:** \"bugüne kadar ... -diğim en ...\"\n\n- It's **the best** film I**'ve ever seen**.\n- It was **the hardest** thing I**'ve ever done**.\n\n**Yaygın deneyimler ve V3'leri:** pass → passed, run → **run**, learn → learned/learnt, do → **done**, make → **made**, give → **given**, take → **taken**",
     "examples": [{"en": "It's the most beautiful place I've ever visited.", "tr": "Gördüğüm en güzel yer."},
                  {"en": "I haven't been to Van yet.", "tr": "Henüz Van'a gitmedim."},
                  {"en": "He's passed all his exams.", "tr": "Bütün sınavlarını geçti."}],
     "turkishNote": "\"Gördüğüm en güzel film\" Türkçede sıfat-fiille kurulur; İngilizcede \"the best film I've ever seen\" denir. Bu kalıp günlük dilde çok sık kullanılır ve kulağa çok doğal gelir. \"run\" fiilinin V3'ü yine run'dır: I've run a marathon."},
    [
        mc("\"Gördüğüm en iyi film\"", ["the best film I've ever seen", "the best film I ever have seen", "the best film I've ever saw"], 0, "the best + isim + I've ever + V3."),
        gap("I haven't finished my book ___. (henüz)", ["yet"], "Olumsuzda yet."),
        gap("She's ___ her driving test! (pass)", ["passed"], "pass → passed."),
        gap("I've ___ a marathon. (run)", ["run"], "run → run (V3)."),
        gap("It's the most delicious meal I've ever ___. (eat)", ["eaten", "had"], "eat → eaten."),
        mc("Hangisi doğru?", ["Have you done your homework yet?", "Have you done yet your homework?"], 0, "yet cümle sonunda."),
        order(["the", "It's", "best", "book", "I've", "ever", "read"], "It's the best book I've ever read.", "the best + isim + I've ever + V3.", "Okuduğum en iyi kitap."),
        listen("I've never been abroad, but I've visited almost every city in Turkey. My next dream is to see the Northern Lights.", "Konuşanın sıradaki hayali ne?", ["Türkiye'yi gezmek", "Kuzey Işıklarını görmek", "Yurt dışında yaşamak"], 1, "\"My next dream is to see the Northern Lights.\""),
        typ("İngilizce yazın: \"Henüz Van'a gitmedim.\"", variants("I haven't been to Van yet.", "I have not been to Van yet."), "I haven't been to Van + yet."),
        match([("do", "done"), ("take", "taken"), ("give", "given"), ("make", "made"), ("run", "run")], "V3 hallerini eşleştirin."),
    ],
    {"kind": "writing", "task": write("Foruma kendi 'bucket list' mesajınızı yazın (80–100 kelime): yaptığınız 2 şey (present perfect + past simple ayrıntı), henüz yapmadığınız 2 şey (yet / never) ve 'the best ... I've ever ...' kalıbını kullanın.",
                                      "Here's my bucket list!\n✓ Swim with turtles – I've done it! I swam with turtles in Dalyan in 2021. It was the best experience I've ever had.\n✓ Learn to drive – I've passed my driving test! I passed it last month.\n✗ Visit Japan – I've never been to Asia, but I'm saving money.\n✗ Climb Mount Ağrı – I haven't done it yet, but I'm going to try next summer.",
                                      ["Present perfect doğru", "Past simple ayrıntılar", "yet / never doğru", "the best ... I've ever ... kalıbı"])},
)

u.test([
    gap("I've ___ sushi. It was delicious. (eat)", ["eaten"], "eat → eaten"),
    mc("Hangisi doğru?", ["She has saw it.", "She has seen it."], 1, "has + V3"),
    gap("They ___ never been to London.", ["have", "'ve"], "have"),
    mc("Hangisi doğru?", ["Have you ever been to Italy?", "Did you ever been to Italy?"], 0, "Have you ever + V3?"),
    mc("Hangisi doğru?", ["I haven't never flown.", "I've never flown."], 1, "Çift olumsuz yok"),
    mc("\"Has she ever ridden a horse?\" (Evet.)", ["Yes, she has.", "Yes, she did."], 0, "Yes, she has."),
    mc("Ayşe şu an marketde:", ["She's been to the market.", "She's gone to the market."], 1, "Hâlâ orada → gone"),
    gap("I've been to Bodrum ___. (iki kez)", ["twice", "two times"], "twice"),
    mc("Hangisi doğru?", ["I've met him last year.", "I met him last year."], 1, "last year → past simple"),
    gap("Have you ever been to Rome? – Yes, I ___ there in 2015. (go)", ["went"], "Zaman belli → went"),
    gap("I haven't finished ___. (henüz)", ["yet"], "yet"),
    mc("\"Gördüğüm en güzel yer\"", ["the most beautiful place I've ever seen", "the most beautiful place I ever saw it"], 0, "the most + isim + I've ever + V3"),
    listen("Have you ever lost your phone? – Yes, twice! The first time I lost it on a bus in Ankara, and the second time I left it in a taxi.", "İkinci kez telefonu nerede unuttu?", ["Otobüste", "Takside", "Restoranda"], 1, "\"I left it in a taxi\""),
    typ("İngilizce yazın: \"Hiç ünlü biriyle tanıştın mı?\"", variants("Have you ever met a famous person?", "Have you ever met someone famous?", "Have you ever met anyone famous?", "Have you ever met somebody famous?"), "Have you ever met + a famous person?"),
    write("Hayatınızdaki en ilginç 3 deneyimi anlatın (80–100 kelime). Her birini present perfect ile tanıtın, sonra past simple ile ayrıntı verin. Hiç yapmadığınız bir şeyi de ekleyin.",
          "I've had some amazing experiences. I've been scuba diving. I went diving in Kaş three years ago and I saw a big turtle. I've also met a famous singer. I met him at the airport in Istanbul and he was very kind. And I've climbed Mount Erciyes. We climbed it in summer 2022. It was the hardest thing I've ever done! But I've never been skydiving. Maybe one day!",
          ["Present perfect ile tanıtım", "Past simple ile ayrıntı", "never doğru", "Düzensiz V3'ler doğru"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

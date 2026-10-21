"""A2 Ünite 2: Tatil anıları."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("A2", 2, "Tatil anıları", "Holiday Memories",
         "Bir tatil anımı arka planıyla birlikte anlatabilir, geçmişte bir olay olurken neler yaşandığını söyleyebilir ve başkasının anlattığına tepki verebilirim.",
         ["past continuous: was / were + -ing", "past continuous ile arka plan anlatımı", "past simple ve past continuous: when / while", "tepki ifadeleri: How awful! / Lucky you!"],
         ["seyahat ve tatil", "konaklama", "tatilde yaşanan sorunlar"],
         {"title": "Tatil felaketi", "durationMinutes": 45,
          "goal": "Her öğrenci gerçek ya da uydurma bir 'tatil felaketi' hikâyesi hazırlar (kayıp bavul, kaçan uçak...). Gruplar halinde hikâyeler anlatılır; dinleyenler tepki ifadeleri kullanır ve sorular sorar. Grup en komik hikâyeyi seçip sınıfa anlatır."})

u.vocab([
    ("book", "rezervasyon yapmak", "We booked a hotel near the beach.", "Plaja yakın bir otel ayırttık.", "book a room / a flight / a table"),
    ("pack", "bavul hazırlamak", "I packed my suitcase the night before.", "Bavulumu bir gece önceden hazırladım.", None),
    ("suitcase", "bavul", "My suitcase was too heavy.", "Bavulum çok ağırdı.", None),
    ("flight", "uçuş", "Our flight was two hours late.", "Uçuşumuz iki saat rötar yaptı.", None),
    ("miss", "kaçırmak (otobüs, uçak)", "We missed the last bus.", "Son otobüsü kaçırdık.", "Ayrıca: özlemek."),
    ("lose", "kaybetmek", "I lost my passport in Rome.", "Roma'da pasaportumu kaybettim.", "lose → lost"),
    ("passport", "pasaport", "Don't forget your passport!", "Pasaportunu unutma!", None),
    ("sightseeing", "gezip görme", "We went sightseeing in Prague.", "Prag'da gezip dolaştık.", "go sightseeing"),
    ("sunbathe", "güneşlenmek", "She sunbathed by the pool all day.", "Bütün gün havuz başında güneşlendi.", None),
    ("view", "manzara", "The view from our room was amazing.", "Odamızdan manzara muhteşemdi.", None),
    ("guide", "rehber", "Our guide spoke perfect English.", "Rehberimiz mükemmel İngilizce konuşuyordu.", None),
    ("abroad", "yurt dışı(na)", "I went abroad for the first time in 2019.", "İlk kez 2019'da yurt dışına çıktım.", "go abroad (to abroad değil)"),
    ("souvenir", "hediyelik eşya", "I bought souvenirs for my family.", "Ailem için hediyelik eşya aldım.", None),
    ("campsite", "kamp alanı", "The campsite was next to a lake.", "Kamp alanı bir gölün yanındaydı.", None),
    ("tent", "çadır", "It was raining and our tent was wet.", "Yağmur yağıyordu ve çadırımız ıslaktı.", None),
    ("crowded", "kalabalık", "The beach was very crowded.", "Plaj çok kalabalıktı.", None),
    ("shine", "parlamak", "The sun was shining.", "Güneş parlıyordu.", "shine → shone"),
    ("happen", "olmak, meydana gelmek", "What happened on your holiday?", "Tatilinde ne oldu?", None),
    ("suddenly", "aniden", "Suddenly, the lights went out.", "Aniden ışıklar söndü.", None),
    ("while", "-irken", "While we were swimming, it started to rain.", "Biz yüzerken yağmur başladı.", None),
    ("break down", "bozulmak (araç)", "Our car broke down on the motorway.", "Arabamız otoyolda bozuldu.", "break → broke"),
    ("How awful!", "Ne kötü!", "They lost your bag? How awful!", "Çantanı mı kaybettiler? Ne kötü!", None),
    ("Lucky you!", "Şanslısın!", "Two weeks in Bali? Lucky you!", "Bali'de iki hafta mı? Şanslısın!", None),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Tatilim nasıldı?", "Tatil ve seyahat kelimeleriyle geçmiş bir tatili özetleyebilirim.",
    {"kind": "dialogue", "title": "Tatil dönüşü", "lines": [
        {"speaker": "Derya", "text": "Welcome back! How was Greece?"},
        {"speaker": "Okan", "text": "Fantastic! We booked a small hotel on Naxos. The view from our room was amazing."},
        {"speaker": "Derya", "text": "Lucky you! What did you do there?"},
        {"speaker": "Okan", "text": "We sunbathed, swam a lot and went sightseeing in the old town."},
        {"speaker": "Derya", "text": "Any problems?"},
        {"speaker": "Okan", "text": "Just one. I lost my sunglasses on the first day! But I bought new ones."}],
     "questions": [
        mc("Where did Okan stay?", ["In a big hotel in Athens", "In a small hotel on Naxos", "At a campsite"], 1, "\"We booked a small hotel on Naxos.\""),
        mc("What was the problem?", ["He lost his passport.", "He lost his sunglasses.", "The hotel was crowded."], 1, "\"I lost my sunglasses on the first day!\""),
     ]},
    {"explanation": "Bir tatili özetlerken **past simple** kullanırız. Tatille ilgili sık kullanılan kalıplar:\n\n| Kalıp | Örnek |\n|---|---|\n| go + -ing | go sightseeing, go swimming, go shopping, go camping |\n| go + to + yer | go to the beach, go to Greece |\n| go abroad | We went abroad. (~~went to abroad~~) |\n| stay at / in | stay at a hotel, stay in a tent |\n| book | book a flight / a hotel |\n\n**Tatil soruları:**\n\n- How **was** your holiday? – It **was** great / terrible / OK.\n- Where **did** you **stay**?\n- What **did** you **do** there?\n- What **was** the weather **like**?",
     "examples": [{"en": "We went camping by a lake.", "tr": "Bir göl kenarında kamp yaptık."},
                  {"en": "Where did you stay? – At a lovely little hotel.", "tr": "Nerede kaldınız? – Şirin, küçük bir otelde."},
                  {"en": "What was the food like?", "tr": "Yemekler nasıldı?"}],
     "turkishNote": "\"Tatile gitmek\" = go on holiday (go to holiday değil). \"Tatildeyim\" = I'm on holiday. Amerikan İngilizcesinde holiday yerine vacation denir. \"abroad\" bir zarftır, önüne to gelmez: go abroad, live abroad."},
    [
        match([("book", "a flight"), ("go", "sightseeing"), ("stay", "at a hotel"), ("buy", "souvenirs"), ("miss", "the bus")], "Kalıpları eşleştirin."),
        mc("Hangisi doğru?", ["We went to abroad.", "We went abroad."], 1, "abroad önüne to almaz."),
        mc("Hangisi doğru?", ["I went to holiday.", "I went on holiday."], 1, "go on holiday."),
        gap("We went ___ in the old town. (gezip görmek)", ["sightseeing"], "go sightseeing."),
        gap("What was the weather ___? – Hot and sunny.", ["like"], "What was ... like?"),
        gap("I ___ my passport at the airport! (lose)", ["lost"], "lose → lost."),
        order(["did", "Where", "you", "stay", "in", "Rome", "?"], "Where did you stay in Rome?", "Where + did + you + stay?", "Roma'da nerede kaldınız?"),
        listen("The hotel was OK, but the beach was very crowded, so we went camping in the mountains for three days.", "Neden dağlara gittiler?", ["Otel kötüydü", "Plaj çok kalabalıktı", "Hava kötüydü"], 1, "\"the beach was very crowded, so we went camping\""),
        typ("İngilizce yazın: \"Tatilin nasıldı?\"", variants("How was your holiday?", "How was your vacation?"), "How was your holiday?"),
        mc("\"We spent two weeks in the Maldives.\" Uygun tepki:", ["How awful!", "Lucky you!", "I'm sorry."], 1, "Güzel bir haber → Lucky you!"),
    ],
    {"kind": "speaking", "task": speak("Son tatilinizi özetleyin: nereye gittiniz, nerede kaldınız, neler yaptınız, hava ve yemekler nasıldı?",
                                       "Last summer I went to Kaş with my family. We stayed at a small hotel near the sea. We swam every day and went sightseeing in the old town. The weather was very hot and the food was delicious.",
                                       ["Tatil kelimeleri ve kalıpları", "Past simple doğru", "What was ... like? bilgisi"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "O sırada ne yapıyordun?", "Geçmişte belirli bir anda devam eden eylemleri past continuous ile anlatabilirim.",
    {"kind": "dialogue", "title": "Otelde bir gece", "lines": [
        {"speaker": "Manager", "text": "Someone took a laptop from room 12 at ten o'clock last night. Where were you all at ten?"},
        {"speaker": "Ms Demir", "text": "I was having dinner in the restaurant with my husband."},
        {"speaker": "Mr Lee", "text": "I was swimming in the pool. The guard saw me."},
        {"speaker": "Sara", "text": "My friends and I were watching a film in our room."},
        {"speaker": "Manager", "text": "And you, Mr Brown?"},
        {"speaker": "Mr Brown", "text": "Er... I was sleeping. Alone."}],
     "questions": [
        mc("What was Mr Lee doing at ten?", ["Having dinner", "Swimming", "Sleeping"], 1, "\"I was swimming in the pool.\""),
        mc("Who doesn't have a witness?", ["Ms Demir", "Sara", "Mr Brown"], 2, "\"I was sleeping. Alone.\""),
     ]},
    {"explanation": "**Past continuous**, geçmişte belirli bir anda **devam etmekte olan** eylemi anlatır.\n\n**Yapı:** was / were + fiil-ing\n\n| Olumlu | Olumsuz | Soru |\n|---|---|---|\n| I / He / She / It **was** working | **wasn't** working | **Was** she working? |\n| You / We / They **were** working | **weren't** working | **Were** they working? |\n\n- At ten o'clock last night, I **was watching** TV.\n- What **were** you **doing** at 8 am? – I **was driving** to work.\n\nKısa cevap: Yes, I **was**. / No, they **weren't**.",
     "examples": [{"en": "At midnight we were dancing on the beach.", "tr": "Gece yarısı plajda dans ediyorduk."},
                  {"en": "What were you doing at this time yesterday?", "tr": "Dün bu saatte ne yapıyordun?"},
                  {"en": "She wasn't listening.", "tr": "Dinlemiyordu."}],
     "turkishNote": "Past continuous, Türkçedeki \"-iyordu\" ekine denk gelir: yüzüyordum = I was swimming. Ama Türkçede \"-iyordu\" bazen alışkanlık için de kullanılır (Çocukken her gün yüzüyordum); İngilizcede bu durumda past simple ya da used to kullanılır: When I was a child, I swam every day."},
    [
        mc("At 9 pm yesterday, I ___ dinner.", ["was having", "were having", "am having"], 0, "I → was + -ing."),
        mc("They ___ in the sea when we arrived.", ["was swimming", "were swimming"], 1, "they → were."),
        gap("What ___ you doing at 7 o'clock?", ["were"], "you → were."),
        gap("She ___ working yesterday. She was on holiday. (değildi)", ["wasn't", "was not"], "she → wasn't."),
        gap("At midnight, we ___ dancing. (were)", ["were"], "we → were."),
        mc("\"Were you sleeping?\" (Hayır.)", ["No, I wasn't.", "No, I weren't.", "No, I didn't."], 0, "No, I wasn't."),
        order(["was", "At", "eight", "I", "driving", "to", "work"], "At eight I was driving to work.", "Zaman + özne + was + -ing.", "Saat sekizde işe araba sürüyordum."),
        listen("At three o'clock I wasn't at the hotel. I was walking around the market with my sister.", "Saat üçte ne yapıyordu?", ["Otelde dinleniyordu", "Pazarda dolaşıyordu", "Kız kardeşini bekliyordu"], 1, "\"I was walking around the market\""),
        typ("İngilizce yazın: \"Dün bu saatte ne yapıyordun?\"", variants("What were you doing at this time yesterday?", "What were you doing this time yesterday?", "Yesterday at this time, what were you doing?"), "What were you doing + at this time yesterday?"),
        mc("Hangisi alışkanlık anlatır?", ["When I was a child, I swam every day.", "At ten o'clock, I was swimming."], 0, "Alışkanlık → past simple."),
    ],
    {"kind": "speaking", "task": speak("JAI dedektif ve size dün günün farklı saatlerinde (8:00, 13:00, 19:00, 23:00) ne yaptığınızı soracak. Past continuous ile cevap verin.",
                                       "At eight o'clock I was having breakfast. At one o'clock I was working in my office. At seven I was cooking dinner. At eleven I was sleeping.",
                                       ["was/were + -ing doğru", "Saat ifadeleri", "Soruya uygun kısa cevaplar"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "Sahneyi kurmak", "Bir hikâyenin arka planını past continuous ile tasvir edebilirim.",
    {"kind": "text", "title": "Bir gezi blogundan", "body": "It was our last evening in Kapadokya. The sun was going down and the sky was turning orange. Hundreds of people were walking to the hill to watch the sunset. Some children were playing football, and an old man was selling tea from a small cart.\n\nWe sat on a rock and drank our tea. Nobody was talking. Then, suddenly, a balloon appeared over the valley. It was the perfect end to a perfect holiday.",
     "questions": [
        mc("What was the old man doing?", ["Playing football", "Selling tea", "Taking photos"], 1, "\"an old man was selling tea from a small cart\""),
        mc("What appeared suddenly?", ["A bird", "A balloon", "A plane"], 1, "\"suddenly, a balloon appeared over the valley\""),
     ]},
    {"explanation": "Hikâye anlatırken iki zamanı birlikte kullanırız:\n\n- **Past continuous** → arka plan, sahne: o sırada neler oluyordu?\n- **Past simple** → hikâyedeki olaylar: ne oldu?\n\n| Arka plan (past continuous) | Olay (past simple) |\n|---|---|\n| The sun **was shining**. | We **arrived** at the beach. |\n| People **were swimming**. | A dog **took** my sandwich! |\n\n**Hikâye başlangıçları:**\n\n- It **was raining** and we **were waiting** for the bus...\n- It was a beautiful morning. The birds **were singing**...\n\nArka plan cümleleri sahneyi bir film gibi canlandırır; dinleyen olayı daha iyi hayal eder.",
     "examples": [{"en": "It was snowing and everybody was wearing hats.", "tr": "Kar yağıyordu ve herkes şapka takıyordu."},
                  {"en": "The music was playing and people were dancing.", "tr": "Müzik çalıyordu ve insanlar dans ediyordu."},
                  {"en": "We were sitting on the balcony. Then the phone rang.", "tr": "Balkonda oturuyorduk. Sonra telefon çaldı."}],
     "turkishNote": "Türkçe hikâyelerde de aynı ayrım vardır: \"Yağmur yağıyordu (arka plan), kapı çaldı (olay).\" İngilizcede bu ayrımı korumak hikâyeyi çok daha doğal yapar. Durum fiilleri (know, want, like) arka planda da -ing almaz: I wanted a coffee (I was wanting değil)."},
    [
        mc("Arka plan cümlesi hangisi?", ["The sun was shining.", "We arrived at the hotel."], 0, "Devam eden durum → past continuous."),
        mc("Olay cümlesi hangisi?", ["People were sleeping.", "A loud noise woke us up."], 1, "Ani olay → past simple."),
        gap("It ___ raining, so we stayed in the tent. (was)", ["was"], "Arka plan: was raining."),
        gap("The birds ___ singing and the sky was blue.", ["were"], "birds → were."),
        gap("We were sitting in the café. Then a famous actor ___ in! (walk)", ["walked"], "Olay → past simple."),
        mc("Hangisi doğru?", ["I was wanting a coffee.", "I wanted a coffee."], 1, "want → durum fiili."),
        order(["were", "People", "dancing", "and", "the", "music", "was", "playing"], "People were dancing and the music was playing.", "İki arka plan cümlesi.", "İnsanlar dans ediyordu ve müzik çalıyordu."),
        listen("It was a cold night. We were sitting around the fire and my uncle was telling a ghost story. Suddenly, we heard a noise in the trees.", "Amca ne yapıyordu?", ["Ateş yakıyordu", "Hayalet hikâyesi anlatıyordu", "Ağaçlara bakıyordu"], 1, "\"my uncle was telling a ghost story\""),
        typ("İngilizce yazın: \"Kar yağıyordu ve herkes mutluydu.\"", variants("It was snowing and everybody was happy.", "It was snowing and everyone was happy.", "It was snowing, and everybody was happy.", "It was snowing, and everyone was happy."), "It was snowing + and everybody was happy."),
        match([("The sun", "was going down."), ("Some children", "were playing."), ("Nobody", "was talking."), ("A balloon", "appeared.")], "Blogdaki cümleleri tamamlayın."),
    ],
    {"kind": "writing", "task": write("Bir tatil fotoğrafınızı ya da bir anınızı düşünün. Sahneyi past continuous ile 4 cümlede anlatın, sonra past simple ile bir olay ekleyin.",
                                      "It was a hot afternoon in Bodrum. The sun was shining and the sea was very calm. My children were building a sandcastle and my husband was reading. Suddenly, a big wave came and destroyed the sandcastle!",
                                      ["Past continuous ile arka plan", "Past simple ile olay", "Durum fiilleri doğru", "Sahne canlı ve anlaşılır"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "When ve while", "Bir eylem devam ederken araya giren olayı when ve while ile anlatabilirim.",
    {"kind": "dialogue", "title": "Havalimanında", "lines": [
        {"speaker": "Can", "text": "You look terrible! What happened?"},
        {"speaker": "Burcu", "text": "Oh, it was a nightmare. While we were flying to Madrid, the plane hit a storm."},
        {"speaker": "Can", "text": "How awful!"},
        {"speaker": "Burcu", "text": "And when we were waiting for our bags, I realised my wallet wasn't in my pocket."},
        {"speaker": "Can", "text": "Oh no! Did you find it?"},
        {"speaker": "Burcu", "text": "Yes! A nice man found it while he was walking to the exit."}],
     "questions": [
        mc("What happened while they were flying?", ["The plane hit a storm.", "She lost her bag.", "She met a nice man."], 0, "\"While we were flying ..., the plane hit a storm.\""),
        mc("When did Burcu notice her wallet was missing?", ["On the plane", "While they were waiting for bags", "At the exit"], 1, "\"when we were waiting for our bags, I realised...\""),
     ]},
    {"explanation": "Uzun (devam eden) bir eylem sırasında kısa bir olay olduğunda:\n\n- uzun eylem → **past continuous**\n- kısa olay → **past simple**\n\n**when** genellikle kısa olayın önüne gelir:\n\n- I **was having** a shower **when** the phone **rang**.\n\n**while** genellikle uzun eylemin önüne gelir:\n\n- **While** I **was having** a shower, the phone **rang**.\n\n**Cümle başı:** when / while ile başlayan kısım öndeyse araya **virgül** konur.\n\n- **When** the phone rang**,** I was having a shower.\n- I was having a shower **when** the phone rang. (virgül yok)\n\n**İki kısa olay art arda:** ikisi de past simple: **When** he **saw** me, he **smiled**.",
     "examples": [{"en": "While we were walking on the beach, we found a ring.", "tr": "Plajda yürürken bir yüzük bulduk."},
                  {"en": "I was reading when the lights went out.", "tr": "Işıklar söndüğünde kitap okuyordum."},
                  {"en": "When I opened the door, the cat ran out.", "tr": "Kapıyı açınca kedi dışarı koştu."}],
     "turkishNote": "Türkçede \"-irken\" (yürürken) while'a, \"-ince / -diğinde\" (açınca, söndüğünde) when'e denk gelir. Türkçede yan cümle hep başa gelir; İngilizcede iki sıra da mümkündür, ama yan cümle öndeyse virgül kullanılır."},
    [
        mc("I ___ TV when the lights went out.", ["watched", "was watching"], 1, "Uzun eylem → past continuous."),
        mc("While she was cooking, she ___ her finger.", ["cut", "was cutting"], 0, "Kısa olay → past simple."),
        mc("___ I was sleeping, someone knocked on the door.", ["While", "When"], 0, "Uzun eylemin önü → while."),
        mc("We were having lunch ___ it started to rain.", ["while", "when"], 1, "Kısa olayın önü → when."),
        gap("When I ___ the door, the cat ran out. (open)", ["opened"], "İki kısa olay → past simple."),
        gap("While we ___ walking to the hotel, we met an old friend.", ["were"], "we → were + -ing."),
        order(["was", "I", "reading", "when", "the", "phone", "rang"], "I was reading when the phone rang.", "Uzun eylem + when + kısa olay.", "Telefon çaldığında okuyordum."),
        listen("While I was taking a photo of the bridge, my phone fell into the river.", "Telefon ne zaman düştü?", ["Köprüde yürürken", "Köprünün fotoğrafını çekerken", "Nehirde yüzerken"], 1, "\"While I was taking a photo of the bridge\""),
        typ("İki cümleyi while ile birleştirin: \"We were driving. The car broke down.\"", variants("While we were driving, the car broke down.", "The car broke down while we were driving."), "While + past continuous, + past simple."),
        mc("Hangi cümlede virgül gerekli?", ["When I arrived I was tired.", "I was tired when I arrived."], 0, "When-cümlesi öndeyse virgül: When I arrived, I was tired."),
    ],
    {"kind": "speaking", "task": speak("JAI'ye tatilde başınıza gelen (ya da hayal ettiğiniz) beklenmedik 3 olayı anlatın. Her birinde when veya while kullanın.",
                                       "While I was swimming, I saw a turtle. When we were walking in the old town, it started to rain. I was having dinner when my boss called me!",
                                       ["while + past continuous", "when + past simple", "Olay ve arka plan ayrımı doğru"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Anını paylaş", "Bir tatil anısını akıcı anlatabilir ve dinlerken uygun tepkiler verebilirim.",
    {"kind": "dialogue", "title": "Kamp hikâyesi", "lines": [
        {"speaker": "Seda", "text": "Did I tell you about our camping trip to Abant?"},
        {"speaker": "Kerem", "text": "No! What happened?"},
        {"speaker": "Seda", "text": "Well, on the first night it was raining really hard. We were sleeping in the tent when water started coming in."},
        {"speaker": "Kerem", "text": "Oh no! What did you do?"},
        {"speaker": "Seda", "text": "We ran to the car and slept there. In the morning, while we were making breakfast, a big dog ate our bread!"},
        {"speaker": "Kerem", "text": "You're joking! That's so funny."},
        {"speaker": "Seda", "text": "It wasn't funny then! But now it's my favourite holiday story."}],
     "questions": [
        mc("Where did they sleep on the first night?", ["In the tent", "In the car", "In a hotel"], 1, "\"We ran to the car and slept there.\""),
        mc("What did the dog do?", ["It ate their bread.", "It slept in the tent.", "It ran away with a shoe."], 0, "\"a big dog ate our bread!\""),
     ]},
    {"explanation": "**Bir anıya başlamak:**\n\n- Did I tell you about...?\n- You won't believe what happened...\n- It was (last summer / two years ago)...\n\n**Hikâyeyi ilerletmek:** at first, then, after that, suddenly, in the end\n\n**Dinleyenin tepkileri:**\n\n| Durum | Tepki |\n|---|---|\n| İlgi | Really? / What happened? / And then? |\n| Kötü haber | Oh no! / How awful! / Poor you! |\n| İyi haber | Lucky you! / How amazing! / That's great! |\n| Şaşırtıcı | You're joking! / No way! |\n| Komik | That's so funny! |\n\n**How + sıfat!** yapısı: How awful! How lovely! How strange!",
     "examples": [{"en": "You won't believe what happened on our trip!", "tr": "Gezimizde ne olduğuna inanmayacaksın!"},
                  {"en": "In the end, we found a lovely little hotel.", "tr": "Sonunda şirin, küçük bir otel bulduk."},
                  {"en": "They cancelled your flight? Poor you!", "tr": "Uçuşunu iptal mi ettiler? Vah zavallım!"}],
     "turkishNote": "İngilizce sohbette dinleyenin sessiz kalması ilgisizlik gibi algılanabilir. Kısa tepkiler (Really? Oh no!) konuşmayı canlı tutar. \"In the end\" (sonunda) ile \"at the end\" (bir şeyin sonunda: at the end of the film) farklıdır."},
    [
        match([("Oh no!", "kötü haber"), ("Lucky you!", "iyi haber"), ("You're joking!", "şaşırtıcı"), ("That's so funny!", "komik")], "Tepkileri durumlarla eşleştirin."),
        mc("\"I lost my bag on the first day.\" Uygun tepki:", ["Lucky you!", "Poor you!", "How lovely!"], 1, "Kötü haber → Poor you!"),
        mc("\"We got a free upgrade to a suite!\" Uygun tepki:", ["How awful!", "Lucky you!", "Oh no!"], 1, "İyi haber → Lucky you!"),
        gap("How ___! A dog ate your bread? (komik / garip)", ["funny", "strange", "awful"], "How + sıfat!"),
        gap("___ the end, we found a nice hotel. (sonunda)", ["In"], "in the end = sonunda."),
        mc("Hangisi doğru?", ["at the end of the film", "in the end of the film"], 0, "at the end of + isim."),
        order(["you", "Did", "I", "tell", "about", "our", "trip", "?"], "Did I tell you about our trip?", "Anıya başlama kalıbı.", "Sana gezimizi anlattım mı?"),
        listen("We were walking in the forest when we saw a bear! – No way! What did you do? – We walked back very, very slowly.", "Ayıyı görünce ne yaptılar?", ["Koştular", "Çok yavaş geri yürüdüler", "Fotoğraf çektiler"], 1, "\"We walked back very, very slowly.\""),
        typ("İngilizce yazın: \"Gezimizde ne olduğuna inanmayacaksın!\"", variants("You won't believe what happened on our trip!", "You won't believe what happened on our trip."), "You won't believe what happened + on our trip!"),
        mc("Hikâyeyi dinlerken ilgi göstermek için:", ["And then?", "OK.", "Bye."], 0, "And then? = Sonra?"),
    ],
    {"kind": "speaking", "task": speak("JAI'ye en unutulmaz tatil anınızı anlatın: bir başlangıç kalıbı kullanın, arka planı past continuous ile verin, olayları past simple ile anlatın. JAI tepki verdikçe hikâyeye devam edin.",
                                       "Did I tell you about my trip to Rome? It was August and it was really hot. We were walking near the Colosseum when a man stopped us. He was looking for his daughter. Suddenly, she came running. In the end, everybody was happy!",
                                       ["Anı başlatma kalıbı", "Arka plan + olay ayrımı", "Sıralama ifadeleri", "Akıcılık"])},
)

u.test([
    mc("Hangisi doğru?", ["We went to abroad.", "We went abroad."], 1, "go abroad"),
    gap("We went ___ in the old town. (gezip görmek)", ["sightseeing"], "go sightseeing"),
    gap("I ___ my passport in Paris. (lose)", ["lost"], "lose → lost"),
    mc("At 8 pm, they ___ dinner.", ["was having", "were having"], 1, "they → were"),
    gap("What ___ you doing at midnight?", ["were"], "you → were"),
    mc("\"Was she sleeping?\" (Hayır.)", ["No, she wasn't.", "No, she didn't.", "No, she weren't."], 0, "No, she wasn't."),
    mc("I ___ a shower when the phone rang.", ["had", "was having"], 1, "Uzun eylem → continuous"),
    mc("While we were walking, it ___ to rain.", ["started", "was starting"], 0, "Kısa olay → simple"),
    mc("___ I was cooking, the lights went out.", ["While", "When"], 0, "Uzun eylem → while"),
    mc("Hangisi doğru?", ["I was knowing the answer.", "I knew the answer."], 1, "know → durum fiili"),
    mc("\"Our hotel was terrible.\" Uygun tepki:", ["Lucky you!", "Oh no!"], 1, "Kötü haber"),
    gap("___ the end, we had a great time. (sonunda)", ["In"], "in the end"),
    listen("It was raining and we were waiting for the bus. Suddenly, a car stopped and the driver offered us a ride.", "Ne oldu?", ["Otobüs geldi", "Bir araba durdu ve sürücü onları götürmeyi teklif etti", "Yağmur durdu"], 1, "\"a car stopped and the driver offered us a ride\""),
    typ("Birleştirin: \"I was sleeping. The alarm rang.\" (when)", variants("I was sleeping when the alarm rang.", "When the alarm rang, I was sleeping."), "past continuous + when + past simple"),
    write("Bir tatil anınızı anlatan bir e-posta yazın (80–100 kelime): arka planı past continuous ile verin, en az 3 olay past simple ile olsun, when ve while kullanın.",
          "Hi Mert,\nYou won't believe what happened in Antalya! On the second day, the sun was shining and we were swimming in the sea. While I was swimming, I lost my wedding ring! I was very upset. We looked for it for hours. Then, when we were leaving the beach, a little boy came to us. He was holding my ring! I gave him an ice cream. In the end, it was a great day.\nSee you soon,\nAyşe",
          ["Past continuous arka plan", "Past simple olaylar", "when / while doğru", "Tatil kelimeleri", "Anlamlı, sıralı bir hikâye"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

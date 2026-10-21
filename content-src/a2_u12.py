"""A2 Ünite 12: Hikâye anlatma."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("A2", 12, "Hikâye anlatma", "Telling Stories",
         "Başımdan geçen bir olayı duygularımla birlikte, sıralı ve bağlantılı bir şekilde anlatabilir; neden ve sonuçları açıklayabilirim.",
         ["-ed ve -ing sıfatları (bored / boring)", "bağlaçlar: and, but, because, so", "sıralama: first, then, after that, finally, in the end", "hikâye zarfları: suddenly, luckily, unfortunately", "past simple ve past continuous ile hikâye"],
         ["duygular", "olaylar ve tepkiler", "hikâye dili"],
         {"title": "Hikâye zinciri", "durationMinutes": 45,
          "goal": "Öğretmen bir hikâyenin ilk cümlesini verir ('It was a dark, rainy night and I was waiting for the last bus...'). Her öğrenci sırayla bir cümle ekler ve verilen bir kelimeyi kullanmak zorundadır (suddenly, luckily, so, because, embarrassed...). Sonra gruplar kendi gerçek ya da uydurma hikâyelerini hazırlayıp anlatır; dinleyenler tepki verir ve soru sorar."})

u.vocab([
    ("excited", "heyecanlı", "I was so excited about the trip.", "Gezi için çok heyecanlıydım.", "exciting = heyecan verici"),
    ("bored", "sıkılmış", "The children were bored.", "Çocuklar sıkılmıştı.", "boring = sıkıcı"),
    ("tired", "yorgun", "We were very tired after the walk.", "Yürüyüşten sonra çok yorgunduk.", "tiring = yorucu"),
    ("surprised", "şaşırmış", "I was surprised to see him there.", "Onu orada gördüğüme şaşırdım.", "surprising = şaşırtıcı"),
    ("embarrassed", "utanmış, mahcup", "I was so embarrassed!", "Çok utandım!", "embarrassing = utandırıcı"),
    ("frightened / scared", "korkmuş", "She was frightened of the dog.", "Köpekten korkmuştu.", "frightening = korkutucu"),
    ("worried", "endişeli", "My parents were worried about me.", "Ailem benim için endişelenmişti.", None),
    ("relieved", "rahatlamış", "I was relieved when I found my passport.", "Pasaportumu bulunca rahatladım.", None),
    ("disappointed", "hayal kırıklığına uğramış", "We were disappointed with the hotel.", "Otelden hayal kırıklığına uğradık.", "disappointing = hayal kırıklığı yaratan"),
    ("annoyed", "sinirlenmiş, canı sıkılmış", "He was annoyed because the bus was late.", "Otobüs geç kaldığı için sinirlenmişti.", "annoying = sinir bozucu"),
    ("proud", "gururlu", "I'm really proud of you!", "Seninle gurur duyuyorum!", "proud of + kişi"),
    ("because", "çünkü", "I stayed at home because I was ill.", "Evde kaldım çünkü hastaydım.", "Sebep"),
    ("so", "bu yüzden", "I was ill, so I stayed at home.", "Hastaydım, bu yüzden evde kaldım.", "Sonuç"),
    ("suddenly", "aniden", "Suddenly, the lights went out.", "Aniden ışıklar söndü.", None),
    ("luckily", "neyse ki", "Luckily, nobody was hurt.", "Neyse ki kimse yaralanmadı.", None),
    ("unfortunately", "maalesef, ne yazık ki", "Unfortunately, the shop was closed.", "Ne yazık ki dükkan kapalıydı.", None),
    ("finally", "sonunda, en sonunda", "Finally, we arrived at the hotel.", "Sonunda otele vardık.", None),
    ("in the end", "sonunda (her şeyden sonra)", "In the end, everything was fine.", "Sonunda her şey yolundaydı.", None),
    ("at first", "ilk başta", "At first I was scared, but then I enjoyed it.", "İlk başta korktum ama sonra keyif aldım.", None),
    ("happen", "olmak, yaşanmak", "You won't believe what happened!", "Ne olduğuna inanmayacaksın!", None),
    ("realise", "fark etmek", "Then I realised my bag was gone.", "Sonra çantamın gittiğini fark ettim.", "Amerikan yazımı: realize."),
    ("drop", "düşürmek", "I dropped my phone in the sea.", "Telefonumu denize düşürdüm.", None),
    ("shout", "bağırmak", "Someone shouted, \"Help!\"", "Biri \"İmdat!\" diye bağırdı.", None),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Nasıl hissettin?", "-ed ve -ing sıfatlarıyla duygularımı ve olayları tanımlayabilirim.",
    {"kind": "dialogue", "title": "Film çıkışı", "lines": [
        {"speaker": "Asya", "text": "So, what did you think of the film?"},
        {"speaker": "Ozan", "text": "Honestly? It was boring. I was bored after twenty minutes."},
        {"speaker": "Asya", "text": "Really? I thought it was exciting! The ending was so surprising."},
        {"speaker": "Ozan", "text": "Well, I was surprised too. Surprised that it was so long!"},
        {"speaker": "Asya", "text": "Ha ha. And I was embarrassed when my phone rang in the middle of it."},
        {"speaker": "Ozan", "text": "Yes, that was embarrassing! Everybody looked at us."}],
     "questions": [
        mc("What did Ozan think of the film?", ["Exciting", "Boring", "Surprising"], 1, "\"It was boring.\""),
        mc("Why was Asya embarrassed?", ["She fell asleep.", "Her phone rang.", "She laughed loudly."], 1, "\"my phone rang in the middle of it\""),
     ]},
    {"explanation": "Birçok duygu sıfatının iki hali vardır:\n\n| -ed → kişi ne **hissediyor** | -ing → şey / kişi nasıl **bir etki yaratıyor** |\n|---|---|\n| I was **bored**. (Sıkıldım.) | The film was **boring**. (Film sıkıcıydı.) |\n| She's **interested** in art. | Art is **interesting**. |\n| We were **tired**. | The walk was **tiring**. |\n| He was **surprised**. | The news was **surprising**. |\n| I was **embarrassed**. | It was **embarrassing**. |\n| They were **frightened**. | The story was **frightening**. |\n\n**Dikkat:** \"I'm boring\" = Ben sıkıcı biriyim! Sıkıldığınızı söylemek için **I'm bored** deyin.\n\n**Vurgulamak:** so / really / very / a bit: I was **so** excited! / It was **a bit** disappointing.",
     "examples": [{"en": "I was really excited about my first flight.", "tr": "İlk uçuşum için çok heyecanlıydım."},
                  {"en": "The museum was interesting, but the tour was tiring.", "tr": "Müze ilginçti ama tur yorucuydu."},
                  {"en": "We were disappointed because the beach was dirty.", "tr": "Plaj kirli olduğu için hayal kırıklığına uğradık."}],
     "turkishNote": "Türkçede \"sıkıldım\" ve \"sıkıcı\" farklı kelimeler olduğu için fark kolay anlaşılır, ama İngilizcede iki kelime birbirine çok benzediğinden karıştırılır. Kural: insanın içindeki duygu → -ed; bu duyguyu yaratan şey → -ing. \"I'm interesting in music\" yanlış; doğrusu \"I'm interested in music\"."},
    [
        mc("Sıkıldığınızı söylemek:", ["I'm boring.", "I'm bored."], 1, "Duygu → -ed."),
        mc("The film was very ___.", ["excited", "exciting"], 1, "Etkiyi yaratan → -ing."),
        mc("I'm ___ in history.", ["interested", "interesting"], 0, "Duygu → interested in."),
        gap("The ten-hour flight was very ___. (tire)", ["tiring"], "Etki → -ing."),
        gap("We were ___ when we saw the price. (surprise)", ["surprised"], "Duygu → -ed."),
        gap("Falling on the stage was so ___! (embarrass)", ["embarrassing"], "Etki → -ing."),
        gap("The children were ___ of the big dog. (frighten)", ["frightened", "scared"], "Duygu → -ed."),
        listen("The concert was a bit disappointing. The singer was very late and the sound was terrible. Everybody was annoyed.", "Konser nasıldı?", ["Heyecan vericiydi", "Biraz hayal kırıklığıydı", "Korkutucuydu"], 1, "\"a bit disappointing\""),
        match([("bored", "sıkılmış"), ("boring", "sıkıcı"), ("relieved", "rahatlamış"), ("annoying", "sinir bozucu"), ("proud", "gururlu")], "Sıfatları eşleştirin."),
        typ("İngilizce yazın: \"Seninle gurur duyuyorum!\"", variants("I'm proud of you!", "I'm so proud of you!", "I'm really proud of you!", "I am proud of you!", "I'm very proud of you!"), "I'm proud of + you!"),
    ],
    {"kind": "speaking", "task": speak("Son izlediğiniz bir film, gittiğiniz bir etkinlik ya da yaşadığınız bir gün hakkında konuşun. En az 3 -ed ve 3 -ing sıfatı kullanın.",
                                       "Last week I went to a football match. It was really exciting! At first I was a bit bored because nothing happened, but then our team scored. I was so excited! The journey home was tiring and the traffic was annoying.",
                                       ["-ed / -ing doğru seçildi", "so / really / a bit ile vurgu", "Geçmiş zaman doğru"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "Çünkü, bu yüzden, ama", "because, so, but ve and ile cümleleri bağlayıp neden ve sonuçları açıklayabilirim.",
    {"kind": "text", "title": "Kötü bir gün", "body": "Yesterday was a terrible day. My alarm didn't ring, so I woke up late. I didn't have time for breakfast and I ran to the bus stop. I missed the bus, so I took a taxi. The taxi was expensive, but I arrived at work on time.\n\nThen I realised that I didn't have my laptop because I left it at home! I called my brother and he brought it to the office. I was annoyed, but I was also grateful. In the evening I went to bed at nine because I was so tired.",
     "questions": [
        mc("Why did the writer wake up late?", ["The alarm didn't ring.", "The bus was late.", "He went to bed late."], 0, "\"My alarm didn't ring, so I woke up late.\""),
        mc("Who brought the laptop?", ["A colleague", "The taxi driver", "The writer's brother"], 2, "\"I called my brother and he brought it\""),
     ]},
    {"explanation": "**Bağlaçlar** iki cümleyi birleştirir:\n\n| Bağlaç | Anlam | Örnek |\n|---|---|---|\n| **and** | ve (ekleme) | I ran **and** I caught the bus. |\n| **but** | ama (zıtlık) | It was expensive, **but** it was fast. |\n| **because** | çünkü (**sebep**) | I was late **because** I missed the bus. |\n| **so** | bu yüzden (**sonuç**) | I missed the bus, **so** I was late. |\n\n**because ve so aynı durumu iki yönden anlatır:**\n\n- I was tired **because** I worked all day. (sebep → because'dan sonra)\n- I worked all day, **so** I was tired. (sonuç → so'dan sonra)\n\n**Virgül:** but ve so'dan önce genellikle virgül konur. because öndeyse: **Because** it was raining, we stayed at home.",
     "examples": [{"en": "It was raining, so we took a taxi.", "tr": "Yağmur yağıyordu, bu yüzden taksiye bindik."},
                  {"en": "We took a taxi because it was raining.", "tr": "Yağmur yağdığı için taksiye bindik."},
                  {"en": "The hotel was old, but it was very clean.", "tr": "Otel eskiydi ama çok temizdi."}],
     "turkishNote": "Türkçede sebep genellikle önce gelir (\"Yağmur yağdığı için taksiye bindik\"); İngilizcede because cümlesi çoğunlukla sonra gelir. \"So\" bağlacını \"so tired\" (çok yorgun) ile karıştırmayın: I was so tired (çok yorgundum) / I was tired, so I slept (yorgundum, bu yüzden uyudum)."},
    [
        mc("I was hungry, ___ I made a sandwich.", ["because", "so"], 1, "Sonuç → so."),
        mc("I made a sandwich ___ I was hungry.", ["because", "so"], 0, "Sebep → because."),
        mc("The film was long, ___ it was really good.", ["but", "so"], 0, "Zıtlık → but."),
        gap("We stayed at home ___ it was snowing.", ["because"], "Sebep → because."),
        gap("It was snowing, ___ we stayed at home.", ["so"], "Sonuç → so."),
        gap("The hotel was old, ___ it was very clean.", ["but"], "Zıtlık → but."),
        gap("I opened the door ___ I saw a big box. (ve)", ["and"], "Ekleme → and."),
        order(["missed", "I", "the", "bus", "so", "I", "took", "a", "taxi"], "I missed the bus so I took a taxi.", "Sebep + so + sonuç.", "Otobüsü kaçırdım, bu yüzden taksiye bindim."),
        listen("I didn't go to the party because I had an exam the next morning. But my friends sent me lots of photos, so I didn't feel left out.", "Neden partiye gitmedi?", ["Hastaydı", "Ertesi sabah sınavı vardı", "Davet edilmedi"], 1, "\"because I had an exam the next morning\""),
        typ("so ile birleştirin: \"I was tired. I went to bed early.\"", variants("I was tired, so I went to bed early.", "I was tired so I went to bed early."), "Sebep + , so + sonuç."),
    ],
    {"kind": "speaking", "task": speak("Kötü (ya da çok iyi) geçen bir gününüzü anlatın. Her olayı bir sonraki olaya bağlayın: en az 2 because, 2 so ve 1 but kullanın.",
                                       "Last Monday was a crazy day. I forgot my keys, so I couldn't get into my flat. I called my landlord, but he didn't answer because he was on holiday. So I went to my sister's house. I stayed there because it was too late to find a locksmith.",
                                       ["because = sebep", "so = sonuç", "but = zıtlık", "Olaylar mantıklı bağlandı"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "Önce, sonra, en sonunda", "Sıralama ifadeleriyle olayları doğru sırayla anlatabilirim.",
    {"kind": "dialogue", "title": "İlk yemek denemesi", "lines": [
        {"speaker": "Ela", "text": "How was your first dinner party?"},
        {"speaker": "Kuzey", "text": "A disaster! First, I burned the rice."},
        {"speaker": "Ela", "text": "Oh no!"},
        {"speaker": "Kuzey", "text": "Then I made new rice, but I forgot to put salt in it. After that, I dropped the salad on the floor!"},
        {"speaker": "Ela", "text": "What did you do?"},
        {"speaker": "Kuzey", "text": "Finally, I ordered pizza. In the end, everyone had a great time, and nobody remembered the rice!"}],
     "questions": [
        mc("What happened first?", ["He dropped the salad.", "He burned the rice.", "He ordered pizza."], 1, "\"First, I burned the rice.\""),
        mc("How did the evening end?", ["Badly", "Everyone had a great time.", "Everyone went home early."], 1, "\"In the end, everyone had a great time\""),
     ]},
    {"explanation": "**Sıralama ifadeleri** dinleyenin hikâyeyi takip etmesini kolaylaştırır.\n\n| Başlangıç | Orta | Son |\n|---|---|---|\n| **First,** ... | **Then** ... | **Finally,** ... |\n| **At first,** ... | **After that,** ... | **In the end,** ... |\n| **One day,** ... | **Next,** ... | |\n| | **Later,** ... | |\n\n- **At first** = ilk başta (sonra durum değişti): **At first** I was scared, but then I loved it.\n- **Finally** = bir listenin son adımı ya da uzun bekleyişin sonu: **Finally**, the bus came.\n- **In the end** = her şeyden sonra, sonuç olarak: **In the end**, we had a great time.\n\n**Zaman bağlaçları:**\n\n- **when**: **When** I got home, I had a shower.\n- **after** + isim / cümle: **After** dinner, we went for a walk.\n- **before** + isim / cümle: **Before** I left, I locked the door.",
     "examples": [{"en": "At first I didn't like him, but then we became friends.", "tr": "İlk başta ondan hoşlanmadım ama sonra arkadaş olduk."},
                  {"en": "After that, we went to a café.", "tr": "Ondan sonra bir kafeye gittik."},
                  {"en": "Before I went to bed, I checked my emails.", "tr": "Yatmadan önce e-postalarıma baktım."}],
     "turkishNote": "\"Then\" ile \"after that\" aynı anlamdadır; sürekli \"and then, and then\" demek yerine çeşitlilik hikâyeyi daha akıcı yapar. \"At the end\" bir şeyin sonunda (at the end of the film), \"in the end\" ise sonuç olarak anlamındadır."},
    [
        mc("Hikâyenin en başında:", ["Finally,", "First,", "In the end,"], 1, "First."),
        mc("İlk başta korktu, sonra sevdi:", ["At first I was scared, but then I loved it.", "In the end I was scared, but first I loved it."], 0, "At first ..., but then ..."),
        gap("___ that, we went to the beach. (Ondan sonra)", ["After"], "After that."),
        gap("___ I left the house, I locked the door. (-den önce)", ["Before"], "Before + cümle."),
        gap("___ I got home, I made dinner. (-dığımda)", ["When"], "When + cümle."),
        gap("We waited for two hours. ___, the bus came. (sonunda)", ["Finally"], "Finally = uzun bekleyişin sonu."),
        mc("Hangisi doğru?", ["at the end of the film", "in the end of the film"], 0, "at the end of + isim."),
        listen("First we visited the castle. Then we had lunch by the river. After that, it started to rain, so we went back to the hotel.", "Öğle yemeğinden sonra ne oldu?", ["Kaleyi gezdiler", "Yağmur başladı", "Nehirde yüzdüler"], 1, "\"After that, it started to rain\""),
        order(["After", "dinner", "we", "went", "for", "a", "walk"], "After dinner we went for a walk.", "After + isim + cümle.", "Akşam yemeğinden sonra yürüyüşe çıktık."),
        typ("İngilizce yazın: \"Sonunda her şey yolundaydı.\"", variants("In the end, everything was fine.", "In the end everything was fine.", "In the end, everything was OK.", "In the end everything was OK."), "In the end, + everything was fine."),
    ],
    {"kind": "writing", "task": write("Kuzey gibi, ilk kez denediğiniz bir şeyi (yemek yapmak, araba sürmek, bir sınav, yeni bir iş...) sıralama ifadeleriyle anlatın (70–90 kelime). En az 5 farklı sıralama ifadesi kullanın.",
                                      "My first driving lesson was terrible! At first, I was very nervous. First, the teacher showed me the car. Then I started the engine, but I pressed the wrong pedal. After that, I drove very slowly around the car park. Later, we went onto a real road. When a bus came behind us, I was so frightened! In the end, the teacher said I did well, and I felt proud.",
                                      ["Sıralama ifadeleri çeşitli ve doğru", "when / before / after", "Past simple doğru", "Duygu sıfatları"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Aniden!", "Hikâye zarflarıyla bir olayı daha canlı anlatabilir ve arka planla olayları ayırabilirim.",
    {"kind": "text", "title": "Kısa hikâye: Kayıp yüzük", "body": "It was a beautiful summer evening. My husband and I were walking along the beach in Çeşme. The sun was going down and children were playing in the sand.\n\nSuddenly, I realised that my wedding ring wasn't on my finger! I was so worried. We looked everywhere, but unfortunately it was getting dark.\n\nThen a little girl ran towards us. She was holding something shiny. \"Is this yours?\" she asked. Luckily, it was my ring! I was so relieved that I nearly cried. To say thank you, we bought her the biggest ice cream on the beach.",
     "questions": [
        mc("What were the children doing?", ["Swimming", "Playing in the sand", "Eating ice cream"], 1, "\"children were playing in the sand\""),
        mc("How did the writer feel when she got the ring back?", ["Worried", "Relieved", "Disappointed"], 1, "\"I was so relieved that I nearly cried\""),
     ]},
    {"explanation": "**Hikâye zarfları** dinleyene ne hissetmesi gerektiğini gösterir. Genellikle **cümle başında, virgülle** kullanılır.\n\n| Zarf | Anlam | Örnek |\n|---|---|---|\n| **Suddenly,** | aniden (beklenmedik olay) | **Suddenly,** the lights went out. |\n| **Luckily,** / **Fortunately,** | neyse ki (iyi haber) | **Luckily,** nobody was hurt. |\n| **Unfortunately,** | ne yazık ki (kötü haber) | **Unfortunately,** the shop was closed. |\n| **Amazingly,** | inanılmaz bir şekilde | **Amazingly,** we won! |\n\n**Hikâyenin zamanları (2. üniteyi hatırlayalım):**\n\n- **Arka plan:** past continuous → We **were walking** on the beach.\n- **Olaylar:** past simple → Suddenly, I **realised** ...\n- **Durum ve duygular:** was / were + sıfat → I **was** so worried.\n\n**so + sıfat + that** → o kadar ... ki: I was **so** relieved **that** I nearly cried.",
     "examples": [{"en": "Suddenly, someone shouted, \"Fire!\"", "tr": "Aniden biri \"Yangın!\" diye bağırdı."},
                  {"en": "Unfortunately, we missed the last train.", "tr": "Ne yazık ki son treni kaçırdık."},
                  {"en": "Luckily, a kind man helped us.", "tr": "Neyse ki nazik bir adam bize yardım etti."}],
     "turkishNote": "Türkçede \"neyse ki\", \"maalesef\" gibi ifadeler de cümle başında kullanılır, bu yüzden bu zarflar kolayca öğrenilir. En sık hata, hikâyede her şeyi past simple ile anlatmaktır; arka plan için past continuous kullanmak hikâyeyi çok daha canlı yapar."},
    [
        mc("İyi bir haber:", ["Unfortunately, we found the key.", "Luckily, we found the key."], 1, "İyi haber → Luckily."),
        mc("Kötü bir haber:", ["Unfortunately, it rained all week.", "Luckily, it rained all week."], 0, "Kötü haber → Unfortunately."),
        mc("Beklenmedik olay:", ["Suddenly, the door opened.", "Finally, the door opened."], 0, "Beklenmedik → Suddenly."),
        mc("Arka plan cümlesi:", ["The sun was shining.", "Suddenly, a dog appeared."], 0, "Arka plan → past continuous."),
        gap("We ___ walking home when it started to rain.", ["were"], "Arka plan → were + -ing."),
        gap("I was ___ happy that I started to dance. (o kadar)", ["so"], "so + sıfat + that."),
        gap("___, nobody was hurt in the accident. (neyse ki)", ["Luckily", "Fortunately"], "Luckily / Fortunately."),
        listen("We were having dinner in a restaurant when suddenly the lights went out. Unfortunately, it was a power cut in the whole area. Luckily, the waiters brought candles.", "Garsonlar ne getirdi?", ["Fener", "Mum", "Yeni yemek"], 1, "\"the waiters brought candles\""),
        order(["Suddenly", "I", "realised", "my", "wallet", "was", "gone"], "Suddenly I realised my wallet was gone.", "Suddenly + olay.", "Aniden cüzdanımın gittiğini fark ettim."),
        typ("İngilizce yazın: \"Ne yazık ki son treni kaçırdık.\"", variants("Unfortunately, we missed the last train.", "Unfortunately we missed the last train."), "Unfortunately, + we missed the last train."),
    ],
    {"kind": "speaking", "task": speak("JAI'ye kısa bir hikâye anlatın (gerçek ya da uydurma): arka planı past continuous ile verin, sonra Suddenly ile bir olay, Unfortunately ile bir sorun ve Luckily ile bir çözüm ekleyin. Duygularınızı da söyleyin.",
                                       "I was waiting for my flight in Rome. People were sleeping on the chairs. Suddenly, I heard my name on the speakers. Unfortunately, my flight was cancelled! I was so annoyed. Luckily, the airline gave me a free hotel room, and in the end I had an extra day in Rome.",
                                       ["Past continuous arka plan", "Suddenly / Unfortunately / Luckily", "Duygu sıfatları", "Akıcı sıralama"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Hikâyeni anlat", "A2'de öğrendiklerimi kullanarak başımdan geçen bir olayı baştan sona akıcı bir şekilde anlatabilirim.",
    {"kind": "dialogue", "title": "Kahve sohbeti", "lines": [
        {"speaker": "Melis", "text": "You won't believe what happened to me last week!"},
        {"speaker": "Arda", "text": "What happened?"},
        {"speaker": "Melis", "text": "Well, I was taking the metro to work. I was very tired, so I fell asleep."},
        {"speaker": "Arda", "text": "Oh no! Did you miss your stop?"},
        {"speaker": "Melis", "text": "Yes! When I woke up, I was at the last station. At first I was really worried, because I had an important meeting."},
        {"speaker": "Arda", "text": "So what did you do?"},
        {"speaker": "Melis", "text": "I called my boss. Luckily, the meeting was cancelled! In the end, I just had a coffee and went back. But I was so embarrassed!"},
        {"speaker": "Arda", "text": "Ha ha! That's so funny. That's happened to me too!"}],
     "questions": [
        mc("Why did Melis fall asleep?", ["She was bored.", "She was very tired.", "The metro was quiet."], 1, "\"I was very tired, so I fell asleep.\""),
        mc("What happened to the meeting?", ["It started late.", "It was cancelled.", "Melis missed it."], 1, "\"Luckily, the meeting was cancelled!\""),
     ]},
    {"explanation": "**İyi bir hikâyenin yapısı:**\n\n1. **Giriş (dikkat çek):** You won't believe what happened! / Did I tell you about ...?\n2. **Arka plan (ne zaman, nerede, ne oluyordu?):** Last week, I **was taking** the metro ...\n3. **Olaylar (sırayla):** First / Then / When / Suddenly + past simple\n4. **Sorun ve çözüm:** Unfortunately ... / Luckily ...\n5. **Son ve duygu:** In the end ... / I was so relieved!\n\n**Dinleyen olarak:**\n\n- Tepki: Oh no! / Really? / That's so funny!\n- Soru: What happened next? / So what did you do? / How did you feel?\n- Benzer deneyim: **That's happened to me too!** (present perfect, 6. ünite)\n\nA2 seviyesinde öğrendiğiniz her şey bu derste bir araya geliyor: past simple, past continuous, bağlaçlar, sıralama, duygu sıfatları ve tepki ifadeleri.",
     "examples": [{"en": "Did I tell you about my trip to Van?", "tr": "Sana Van gezimi anlattım mı?"},
                  {"en": "So what did you do?", "tr": "Peki ne yaptın?"},
                  {"en": "That's happened to me too!", "tr": "Bu benim de başıma geldi!"}],
     "turkishNote": "İngilizcede hikâye anlatırken dinleyenin araya girip soru sorması ve tepki vermesi beklenir; bu bir kabalık değil, ilgi göstergesidir. Hikâyeyi anlatan kişi de dinleyenin tepkilerine kısa cevaplarla karşılık verir (Yes! / I know!) ve hikâyeye devam eder."},
    [
        mc("Hikâyeye dikkat çekici bir başlangıç:", ["You won't believe what happened!", "The end.", "I'm bored."], 0, "Dikkat çekici giriş."),
        mc("Dinleyen olarak devamını sormak:", ["What happened next?", "I don't care.", "Stop."], 0, "What happened next?"),
        mc("Benzer deneyim:", ["That's happened to me too!", "That happens me too yesterday."], 0, "That's happened to me too!"),
        gap("I was ___ to work when I saw an old friend. (walk)", ["walking"], "Arka plan → past continuous."),
        gap("I was very tired, ___ I fell asleep.", ["so"], "Sonuç → so."),
        gap("___ first I was worried, but then I relaxed.", ["At"], "At first."),
        gap("So what ___ you do?", ["did"], "Past simple soru."),
        listen("Did I tell you about my first day at work? I was so nervous that I went to the wrong floor! I walked into a meeting and everybody looked at me. Luckily, a kind woman showed me my office.", "İlk iş gününde ne oldu?", ["Geç kaldı", "Yanlış kata gitti ve bir toplantıya girdi", "Ofisi bulamayıp eve döndü"], 1, "\"I went to the wrong floor! I walked into a meeting\""),
        order(["what", "You", "won't", "believe", "happened", "to", "me"], "You won't believe what happened to me.", "Hikâye giriş kalıbı.", "Başıma ne geldiğine inanmayacaksın."),
        match([("Introduction", "Did I tell you about...?"), ("Background", "I was waiting for the bus."), ("Problem", "Unfortunately, it didn't come."), ("Ending", "In the end, I walked home.")], "Hikâye bölümlerini eşleştirin."),
    ],
    {"kind": "speaking", "task": speak("A2 final görevi: JAI'ye başınızdan geçen gerçek bir olayı 1–2 dakika boyunca anlatın. Hikâye yapısının 5 bölümünü kullanın. JAI sorular soracak; cevap verip hikâyeye devam edin.",
                                       "Did I tell you about my trip to Kars? It was January and it was snowing heavily. We were driving to the hotel when suddenly our car stopped. Unfortunately, there was no signal on our phones, so we couldn't call anyone. We were so frightened because it was very cold. Then a farmer came with his tractor. Luckily, he pulled our car to his village. In the end, his family gave us hot soup and we stayed with them. It was the best night of the trip!",
                                       ["Hikâye yapısı tam (5 bölüm)", "Past simple + past continuous", "Bağlaçlar ve sıralama", "Duygu sıfatları", "Soruları cevaplayıp devam etti"])},
)

u.test([
    mc("Sıkıldığınızı söylemek:", ["I'm boring.", "I'm bored."], 1, "-ed = duygu"),
    mc("The trip was very ___.", ["tiring", "tired"], 0, "-ing = etki"),
    gap("I'm very ___ in photography. (interest)", ["interested"], "interested in"),
    gap("It was raining, ___ we stayed at home.", ["so"], "Sonuç → so"),
    gap("We stayed at home ___ it was raining.", ["because"], "Sebep → because"),
    mc("The hotel was old, ___ it was clean.", ["so", "but"], 1, "Zıtlık → but"),
    mc("Hikâyenin sonu (sonuç olarak):", ["In the end,", "At first,"], 0, "In the end"),
    gap("___ I went to bed, I brushed my teeth. (-den önce)", ["Before"], "Before"),
    mc("Hangisi doğru?", ["at the end of the day", "in the end of the day"], 0, "at the end of"),
    mc("İyi haber:", ["Luckily, we caught the train.", "Unfortunately, we caught the train."], 0, "Luckily"),
    gap("We ___ sitting in the garden when it started to rain.", ["were"], "Arka plan"),
    gap("I was ___ happy that I cried. (o kadar)", ["so"], "so ... that"),
    listen("At first I didn't want to go camping because I hate insects. But in the end I loved it. The stars were amazing and I wasn't frightened at all.", "Kamp hakkında sonunda ne düşündü?", ["Nefret etti", "Çok sevdi", "Korktu"], 1, "\"in the end I loved it\""),
    typ("İngilizce yazın: \"Başıma ne geldiğine inanmayacaksın!\"", variants("You won't believe what happened to me!", "You won't believe what happened to me.", "You will not believe what happened to me!"), "You won't believe + what happened to me!"),
    write("A2 final yazısı: Başınızdan geçen unutulmaz bir olayı anlatan bir hikâye yazın (100–120 kelime). Bir giriş kalıbı, past continuous ile arka plan, sıralama ifadeleri, because / so / but, Suddenly / Luckily / Unfortunately ve en az 3 duygu sıfatı kullanın.",
          "Did I tell you about my sister's wedding? It was a hot day in July and everyone was dancing in the garden. I was so excited because I had to give a speech. First, I drank some water. Then I took the microphone. Suddenly, I realised my notes were in the car! I was really embarrassed, and my hands were shaking. Unfortunately, the car was far away, so I decided to speak without notes. At first it was difficult, but then people started laughing at my stories. In the end, my sister hugged me and said it was the best speech of the night. I was so proud and relieved!",
          ["Hikâye yapısı", "Past simple + past continuous", "Bağlaçlar ve sıralama", "Hikâye zarfları", "Duygu sıfatları (-ed / -ing)"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

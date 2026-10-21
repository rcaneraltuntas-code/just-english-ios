"""C2 Ünite 7: Mizah ve ironi."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("C2", 7, "Mizah ve ironi", "Humour and Irony",
         "Hafife alma (understatement) ve litotes ile söyleneni anlayabilir, sözlü ironi ve alayı ses tonu ve bağlamdan fark edebilir, kelime oyunlarını ve espri yapısını çözebilir, kendini tiye alma, kuru mizah ve takılma (banter) gibi mizah türlerine uygun karşılık verebilir ve mizahi bir yazı yazabilirim.",
         ["hafife alma ve litotes: not bad, not exactly cheap", "sözlü ironi ve alay; durum ironisi", "kelime oyunları ve espri yapısı", "kendini tiye alma, kuru mizah ve takılma", "mizahi anı / köşe yazısı"],
         ["kültürlerarası iletişim", "komedi ve diziler", "arkadaşlık ve iş yeri"],
         {"title": "Ciddi mi, şaka mı?", "durationMinutes": 45,
          "goal": "Öğretmen aynı cümleyi (örneğin \"Oh, that's just perfect.\" ya da \"Well, that went well.\") farklı tonlarla okur; öğrenciler her seferinde cümlenin içten mi ironik mi olduğuna karar verir. Sonra ikili gruplar günlük bir aksiliği (kaybolan bavul, yağmurda piknik) önce hafife alma ve ironiyle, sonra abartıyla anlatan kısa bir sahne hazırlar. Son bölümde sınıf, Türk ve İngiliz mizahı arasındaki farkları tartışır."})

u.vocab([
    ("understatement", "hafife alma, olduğundan az gösterme", "\"It's a bit chilly\" was an understatement: it was minus ten.", "\"Biraz serin\" demek az kalırdı: eksi ondu.", None),
    ("litotes", "olumsuzla olumlu anlatma", "\"Not bad\" is a classic example of litotes.", "\"Fena değil\" klasik bir litotes örneğidir.", None),
    ("not exactly", "pek ... sayılmaz", "It's not exactly cheap.", "Pek ucuz sayılmaz.", None),
    ("irony", "ironi", "The irony is that the fire station burned down.", "İronik olan, itfaiye binasının yanmış olması.", None),
    ("ironic", "ironik", "It's ironic that the dentist has bad teeth.", "Diş hekiminin dişlerinin kötü olması ironik.", None),
    ("sarcasm", "alay, iğneleme", "\"Great job,\" he said with heavy sarcasm.", "\"Harika iş,\" dedi ağır bir alayla.", None),
    ("sarcastic", "alaycı", "Are you being sarcastic?", "Alay mı ediyorsun?", None),
    ("pun", "kelime oyunu, cinas", "The joke is based on a pun.", "Espri bir kelime oyununa dayanıyor.", None),
    ("punchline", "esprinin can alıcı son cümlesi", "I forgot the punchline.", "Esprinin son cümlesini unuttum.", None),
    ("deadpan", "kuru, ifadesiz (mizah)", "She has a deadpan sense of humour.", "Kuru bir mizah anlayışı var.", None),
    ("dry humour", "kuru mizah", "British dry humour can be hard to recognise.", "İngiliz kuru mizahını tanımak zor olabilir.", None),
    ("self-deprecating", "kendini tiye alan", "His self-deprecating jokes make people relax.", "Kendini tiye alan espriler insanları rahatlatıyor.", None),
    ("banter", "dostça takılma", "There's a lot of friendly banter in the office.", "Ofiste bolca dostça takılma var.", None),
    ("tease", "takılmak, şakayla iğnelemek", "Don't take it seriously; he's only teasing.", "Ciddiye alma, sadece takılıyor.", None),
    ("tongue-in-cheek", "şaka yollu, yarı ciddi", "The article is tongue-in-cheek.", "Makale şaka yollu yazılmış.", None),
    ("to take something the wrong way", "yanlış anlamak, alınmak", "Don't take this the wrong way, but ...", "Yanlış anlama ama ...", None),
    ("to get a joke", "espriyi anlamak", "I didn't get the joke.", "Espriyi anlamadım.", None),
    ("to crack a joke", "espri yapmak", "He's always cracking jokes.", "Sürekli espri yapıyor.", None),
    ("to keep a straight face", "gülmemek için kendini tutmak", "I couldn't keep a straight face.", "Gülmemek için kendimi tutamadım.", None),
    ("hilarious", "çok komik", "The film was absolutely hilarious.", "Film son derece komikti.", None),
    ("witty", "esprili, nükteli", "She's very witty.", "O çok nüktedan.", None),
    ("Well, that went well.", "Eh, ne güzel oldu. (ironik)", "Well, that went well. Everyone left early.", "Eh, ne güzel oldu. Herkes erken gitti.", None),
    ("a bit of a", "biraz (hafife alma)", "We had a bit of a problem with the car.", "Arabayla küçük (!) bir sorun yaşadık.", None),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Hafife alma ve litotes", "İngiliz İngilizcesinde çok yaygın olan hafife alma (a bit of a problem, not ideal, rather unfortunate) ve litotes (not bad, not exactly cheap) ifadelerinin gerçek anlamını çözebilir ve kullanabilirim.",
    {"kind": "dialogue", "title": "Tatil dönüşü", "lines": [
        {"speaker": "Rosie", "text": "So, how was the camping trip?"},
        {"speaker": "James", "text": "Well, it wasn't exactly relaxing. It rained a bit."},
        {"speaker": "Rosie", "text": "A bit?"},
        {"speaker": "James", "text": "Four days non-stop. Our tent was slightly flooded on the second night."},
        {"speaker": "Rosie", "text": "Oh no!"},
        {"speaker": "James", "text": "And then the car wouldn't start, which was a bit of a problem, since we were forty miles from the nearest town."},
        {"speaker": "Rosie", "text": "That sounds awful!"},
        {"speaker": "James", "text": "Oh, it wasn't too bad. The scenery was quite nice, when we could see it. Not ideal, but we survived."}],
     "questions": [
        mc("How much did it rain?", ["A little", "Four days without stopping", "Only one night"], 1, "\"Four days non-stop.\""),
        mc("What is James doing when he says \"It wasn't too bad\"?", ["Describing a pleasant trip", "Understating a very difficult trip"], 1, "Understatement."),
     ]},
    {"explanation": "**Hafife alma (understatement):** Bir durumu **olduğundan çok daha hafif** göstermek. İngiliz kültüründe çok yaygındır ve genellikle **mizah** ya da **soğukkanlılık** gösterir.\n\n| Söylenen | Gerçek anlam |\n|---|---|\n| *It rained **a bit**.* | Dört gün durmadan yağdı. |\n| *The tent was **slightly** flooded.* | Çadır su içinde kaldı. |\n| *That was **a bit of a problem**.* | Bu büyük bir sorundu. |\n| ***Not ideal**.* | Berbat. |\n| *It's **rather unfortunate**.* | Felaket. |\n| *I'm **not entirely convinced**.* | Hiç inanmıyorum. |\n| *That could have gone **better**.* | Çok kötü geçti. |\n| *We've had **one or two** complaints.* | Çok şikâyet aldık. |\n\n**Litotes:** Olumlu bir şeyi, **zıddını olumsuzlayarak** söylemek.\n\n| Litotes | Anlam |\n|---|---|\n| ***Not bad**.* | İyi, hatta çok iyi. |\n| *It's **not exactly cheap**.* | Çok pahalı. |\n| *She's **not unattractive**.* | Oldukça çekici. |\n| *I **wouldn't say no** to a coffee.* | Kahve çok isterim. |\n| *That's **no small achievement**.* | Bu büyük bir başarı. |\n| *He's **not the brightest** student.* | Pek zeki değil. (kibar eleştiri) |\n\n**Neden önemli?**\n\n- **Kibarlık:** Eleştiriyi yumuşatır (*not the brightest*).\n- **Mizah:** Felaket bir durumu hafife almak komik etki yaratır.\n- **Yanlış anlama riski:** Bir İngiliz *\"It's not bad\"* dediğinde aslında **çok beğenmiş** olabilir; *\"It's quite interesting\"* dediğinde ise **hiç beğenmemiş** olabilir!",
     "examples": [{"en": "\"How was the exam?\" \"Not bad, actually.\" (= It went well.)", "tr": "\"Sınav nasıldı?\" \"Fena değildi aslında.\" (= İyi geçti.)"},
                  {"en": "The hotel was not exactly luxurious.", "tr": "Otel pek lüks sayılmazdı."},
                  {"en": "We had a bit of a problem with the car: it caught fire.", "tr": "Arabayla küçük bir sorunumuz oldu: Alev aldı."}],
     "turkishNote": "Türkçede de \"Fena değil\" ya da \"Eh, idare eder\" gibi ifadeler vardır, ancak Türk iletişim kültürü genellikle duyguları daha açık ifade eder (\"Berbattı!\", \"Harikaydı!\"). İngiliz kültüründe ise hafife alma çok yaygındır ve Türk öğrenciler bunu bazen yanlış anlar. Bir İngiliz meslektaşınız \"That's a bit of a problem\" diyorsa, durum muhtemelen ciddidir. \"Not bad\" ise genellikle övgüdür. İngilizler arasında bu ifadeleri doğru yorumlamak, iş ve sosyal hayatta yanlış anlamaları önler."},
    [
        mc("\"It's not exactly cheap.\" anlamı:", ["Oldukça ucuz.", "Çok pahalı."], 1, "Litotes."),
        mc("\"Not bad!\" genellikle:", ["Kötü.", "İyi, hatta çok iyi."], 1, "Litotes."),
        mc("\"We had a bit of a problem.\" (Uçak acil iniş yaptı.) Bu:", ["Abartma", "Hafife alma"], 1, "Understatement."),
        mc("\"I wouldn't say no to a coffee.\" anlamı:", ["Kahve istemiyorum.", "Kahve çok isterim."], 1, "Litotes."),
        gap("\"How was the film?\" \"Not ___, actually. I quite enjoyed it.\"", ["bad"], "Not bad."),
        gap("The traffic was a ___ of a nightmare. It took us four hours. (biraz)", ["bit"], "a bit of a."),
        gap("Being late for your own wedding is not ___. (hiç iyi değil, hafife alma)", ["ideal", "great", "good"], "Not ideal."),
        gap("Winning the championship at sixteen is no ___ achievement.", ["small", "mean"], "no small achievement."),
        listen("So, we arrived at the hotel, and it was, shall we say, not quite what the website had promised. The pool was slightly empty, and the sea view was, well, a view of a car park. But the staff were lovely. Not a disaster, but not exactly paradise either.", "Otel nasıldı?", ["Mükemmeldi.", "Vaat edilenden çok daha kötüydü.", "Tam beklendiği gibiydi."], 1, "\"not quite what the website had promised\""),
        match([("Not bad.", "İyi"), ("It's not exactly cheap.", "Çok pahalı"), ("A bit of a problem", "Büyük bir sorun"), ("Not ideal", "Kötü"), ("I wouldn't say no.", "Çok isterim")], "Her ifadeyi gerçek anlamıyla eşleştirin."),
    ],
    {"kind": "speaking", "task": speak("Gerçekten kötü geçmiş bir günü, tatili ya da etkinliği (gerçek ya da hayali) bir İngiliz gibi anlatın (45 saniye). En az 5 hafife alma ya da litotes ifadesi kullanın (a bit, slightly, a bit of a problem, not ideal, not exactly, not bad, rather unfortunate, could have gone better). Sonra aynı olayı tek cümleyle açıkça ve doğrudan söyleyin.",
                                       "So, my first day at the new job was, shall we say, not exactly perfect. I was slightly late, about forty minutes, because the metro broke down. That was a bit of a problem, as I had a meeting with the director at nine. Then I spilled coffee on my laptop, which was rather unfortunate. And at lunch, I called my manager by the wrong name twice. Not ideal. But the people were lovely, and the canteen food was not bad at all. All in all, it could have gone better. Directly: It was a terrible first day, and almost everything went wrong.",
                                       ["En az 5 hafife alma / litotes", "Mizahi ve soğukkanlı ton", "Doğrudan versiyonla karşılaştırma", "Doğal anlatım"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "İroni ve alay", "Sözlü ironiyi ve alayı (Oh, great. / Lovely weather!) bağlam ve tonlamadan tanıyabilir, durum ironisini açıklayabilir ve gerektiğinde ironik bir yorumu doğal şekilde yapabilirim.",
    {"kind": "dialogue", "title": "Kötü bir pazartesi", "lines": [
        {"speaker": "Tom", "text": "Morning! Did you hear? The printer's broken again."},
        {"speaker": "Sara", "text": "Oh, great. Just what I needed. I've got forty pages to print before ten."},
        {"speaker": "Tom", "text": "And IT says it'll be fixed by Thursday."},
        {"speaker": "Sara", "text": "Wonderful. That's really helpful."},
        {"speaker": "Tom", "text": "Look outside. It's pouring again."},
        {"speaker": "Sara", "text": "Lovely. Perfect weather for my bike ride home."},
        {"speaker": "Tom", "text": "Ha! And guess what the email from the manager says? \"Please print all documents to reduce screen time.\""},
        {"speaker": "Sara", "text": "You couldn't make it up."}],
     "questions": [
        mc("Is Sara happy about the printer?", ["Yes, she is delighted.", "No, she is being sarcastic."], 1, "\"Oh, great. Just what I needed.\" (alay)"),
        mc("Why is the manager's email ironic?", ["It asks people to print while the printer is broken.", "It is too long."], 0, "Durum ironisi."),
     ]},
    {"explanation": "**1. Sözlü ironi (verbal irony):** Söylenenin, **kastedilenin tam tersi** olması.\n\n**2. Alay (sarcasm):** Genellikle birini ya da bir durumu **eleştirmek** veya **iğnelemek** için kullanılan sözlü ironi.\n\n| İronik / alaycı söz | Gerçek anlam |\n|---|---|\n| *Oh, **great**. Just what I needed.* | Berbat, hiç gerekmiyordu. |\n| ***Wonderful**. That's really helpful.* | Hiç yardımcı değil. |\n| ***Lovely** weather!* (yağmurda) | Berbat hava. |\n| *Well, **that went well**.* | Çok kötü geçti. |\n| *Thanks **a lot**.* | Hiç teşekkür etmiyorum. |\n| ***Nice one**.* (biri bir şey kırınca) | Aferin (!) |\n| *Tell me **something I don't know**.* | Bunu zaten biliyorum. |\n\n**Nasıl anlaşılır?**\n\n- **Bağlam:** Kötü bir durumda olumlu kelimeler\n- **Tonlama:** Düz, uzatılmış ya da abartılı tonlama (*Oh, grea-a-at.*)\n- **Yüz ifadesi:** Göz devirme, gülümsememe\n- **Yazıda:** Bağlam, bazen tırnak ya da emoji (🙄)\n\n**3. Durum ironisi (situational irony):** Beklenenin **tam tersi** bir şeyin olması.\n\n- *The manager asks everyone to print documents ... while the printer is broken.*\n- *A fire station burns down.*\n- *A traffic safety expert gets a speeding ticket.*\n\n**Dikkat:** *Ironic* kelimesi günlük dilde sık sık yanlış kullanılır. Sadece **talihsiz** bir durum (*rain on your wedding day*) her zaman ironik değildir; ironide **beklenti ile gerçek arasında bir zıtlık** olmalıdır.\n\n**4. Faydalı kalıp:** *You couldn't make it up.* (= Bu kadarını uyduramazsın; inanılmaz derecede absürt.)",
     "examples": [{"en": "\"I've lost my keys again.\" \"Oh, brilliant.\"", "tr": "\"Anahtarlarımı yine kaybettim.\" \"Ah, ne harika.\" (alaycı)"},
                  {"en": "Ironically, the expert on time management was late for his own talk.", "tr": "İronik bir şekilde, zaman yönetimi uzmanı kendi konuşmasına geç kaldı."},
                  {"en": "Well, that went well. Half the audience fell asleep.", "tr": "Eh, ne güzel geçti. Dinleyicilerin yarısı uyudu."}],
     "turkishNote": "Türkçede de ironi ve alay çok yaygındır: \"Ne güzel!\", \"Aferin sana!\", \"Bir bu eksikti!\" İngilizcede ironi genellikle daha düz ve ifadesiz bir tonla söylenir, bu yüzden Türk öğrenciler İngiliz ironisini bazen gerçek sanabilir. Ters durum da olabilir: İngilizce bilmeyen biriyle konuşurken ironi kullanmak yanlış anlaşılmaya yol açabilir. Özellikle yazılı iletişimde (e-posta, mesaj) ironi kolayca yanlış anlaşılır; iş yazışmalarında dikkatli olun."},
    [
        mc("Yağmurda: \"Lovely weather!\"", ["İçten", "İronik"], 1, "Verbal irony."),
        mc("\"Well, that went well.\" (Toplantı felaketti.)", ["Toplantı çok iyi geçti.", "Toplantı çok kötü geçti."], 1, "İroni."),
        mc("Durum ironisi:", ["A fire station burns down.", "It rains in London."], 0, "Beklentinin tersi."),
        mc("İroni yazıda nerede en kolay yanlış anlaşılır?", ["Yüz yüze konuşmada", "İş e-postalarında"], 1, "Yazılı iletişim."),
        gap("\"The train's cancelled.\" \"Oh, ___. Just what I needed.\" (alaycı: harika)", ["great", "brilliant", "wonderful", "perfect", "fantastic"], "Sarcasm."),
        gap("___, the nutrition expert lived on fast food. (İronik bir şekilde)", ["Ironically"], "Ironically."),
        gap("He's being ___. He doesn't really think it's a good idea. (alaycı)", ["sarcastic", "ironic"], "sarcastic."),
        gap("The manager wants us to work faster with fewer staff. You couldn't ___ it up.", ["make"], "You couldn't make it up."),
        listen("Oh, fantastic. My flight's delayed by six hours, the café's closed, and my phone's on two per cent. This is shaping up to be the best day of my life.", "Konuşanın gerçek duygusu nedir?", ["Çok mutlu", "Çok sinirli ve hayal kırıklığına uğramış"], 1, "Sarcasm."),
        match([("Oh, great.", "Berbat."), ("Thanks a lot.", "Hiç teşekkür etmiyorum."), ("Nice one.", "Aferin (!) / Ne yaptın sen?"), ("Tell me something I don't know.", "Bunu zaten biliyorum."), ("Well, that went well.", "Çok kötü geçti.")], "Her ironik ifadeyi gerçek anlamıyla eşleştirin."),
    ],
    {"kind": "speaking", "task": speak("Aşağıdaki durumların her birine, bir arkadaşınızla konuşurken söyleyeceğiniz ironik ya da alaycı bir yorum yapın (doğru tonlamayla!), sonra gerçekte ne demek istediğinizi açıklayın: (1) Yeni aldığınız telefonun ekranı ilk gün kırıldı. (2) Tatilinizin her günü yağmur yağdı. (3) Bir arkadaşınız size bir filmin sonunu anlattı (spoiler). (4) Toplu taşıma grevi var ve önemli bir sınava gitmeniz gerekiyor. Sonra bir durum ironisi örneği verin.",
                                       "One: Oh, brilliant. That's exactly how I wanted to start the week. I mean, I'm really annoyed. Two: Lovely weather we had. Perfect for the beach. I mean, it was terrible; it rained every single day. Three: Oh, thanks a lot. I really needed to know that. I mean, I'm annoyed because he ruined the film for me. Four: Great timing, as always. What a perfect day for a strike. I mean, it's the worst possible day. An example of situational irony: Last year, the company that organised a big conference on digital communication couldn't get the Wi-Fi to work for the whole event.",
                                       ["İronik yorumlar", "Doğru tonlama", "Gerçek anlamın açıklanması", "Durum ironisi örneği"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "Kelime oyunları ve espri yapısı", "Eşsesli ve çok anlamlı kelimelere dayanan kelime oyunlarını (puns) çözebilir, bir esprinin yapısını (setup + punchline) açıklayabilir ve basit bir İngilizce espri anlatabilirim.",
    {"kind": "text", "title": "Kelime oyunları", "body": "1. I'm reading a book about anti-gravity. It's impossible to put down.\n\n2. Why don't skeletons fight each other? They don't have the guts.\n\n3. I used to be a banker, but I lost interest.\n\n4. Time flies like an arrow. Fruit flies like a banana.\n\n5. Why was the maths book sad? It had too many problems.\n\n6. I told my friend she drew her eyebrows too high. She looked surprised.",
     "questions": [
        mc("In joke 3, what are the two meanings of \"interest\"?", ["Money from a bank and enthusiasm", "A hobby and a job"], 0, "interest: faiz / ilgi."),
        mc("In joke 5, what are the two meanings of \"problems\"?", ["Maths exercises and personal difficulties", "Mistakes and errors"], 0, "problems: matematik soruları / dertler."),
     ]},
    {"explanation": "**1. Kelime oyunu (pun):** Bir kelimenin **iki anlamından** ya da **benzer sesli** iki kelimeden yararlanan espri.\n\n| Espri | Kelime | Anlam 1 | Anlam 2 |\n|---|---|---|---|\n| *... impossible to **put down**.* | put down | elinden bırakmak (kitap) | yere indirmek (yerçekimsiz) |\n| *They don't have the **guts**.* | guts | cesaret | bağırsak, iç organlar |\n| *I lost **interest**.* | interest | ilgi | faiz |\n| *... too many **problems**.* | problems | matematik soruları | dertler |\n| *She looked **surprised**.* | surprised | şaşırmış görünmek | (kaşlar yüksek = şaşkın ifade) |\n| *Fruit **flies** like a banana.* | flies | uçar (fiil) | sinekler (isim) |\n\n**2. Espri yapısı:**\n\n| Bölüm | İşlev |\n|---|---|\n| **Setup** (hazırlık) | Bir beklenti yaratır: *I'm reading a book about anti-gravity.* |\n| **Punchline** (can alıcı cümle) | Beklentiyi beklenmedik şekilde bozar: *It's impossible to put down.* |\n\n**Zamanlama (timing):** Punchline'dan önce **kısa bir duraklama** espriyi daha etkili yapar.\n\n**3. Espri türleri:**\n\n- ***Knock-knock* espriler** (çocuksu, kelime oyunu): *Knock, knock. Who's there? Lettuce. Lettuce who? Lettuce in, it's cold!* (Let us in)\n- ***Dad jokes*** (bilerek kötü, kelime oyunlu espriler; genellikle inleme ile karşılanır)\n- **One-liners** (tek cümlelik espriler)\n\n**Neden zor?** Kelime oyunları neredeyse **hiç çevrilemez**. Bir dilin espri kültürünü anlamak, o dili gerçekten iyi bildiğinizin işaretidir.\n\n**Tepki:** İyi bir kelime oyununa *Ha! Very clever!*, kötü bir *dad joke*'a ise *Oh no. That's terrible!* (gülerek) denir.",
     "examples": [{"en": "\"That's a terrible pun!\" \"Thanks, I try.\"", "tr": "\"Berbat bir kelime oyunu!\" \"Teşekkürler, elimden geleni yapıyorum.\""},
                  {"en": "I didn't get the joke at first.", "tr": "Espriyi ilk başta anlamadım."},
                  {"en": "She delivered the punchline perfectly.", "tr": "Esprinin can alıcı cümlesini mükemmel söyledi."}],
     "turkishNote": "Türkçede de kelime oyunları çok sevilir; özellikle Nasreddin Hoca fıkraları ve cinaslar. Ancak İngilizce kelime oyunları neredeyse hiçbir zaman Türkçeye çevrilemez, çünkü iki anlam sadece İngilizcede aynı kelimede birleşir. Bir İngilizce espriyi anlamadıysanız, genellikle sorun çok anlamlı bir kelimededir. Kendinize sorun: Bu esprideki hangi kelimenin iki anlamı olabilir? İngilizce espri anlamak, ileri düzey kelime bilgisinin en iyi testlerinden biridir."},
    [
        mc("\"I used to be a baker, but I couldn't make enough dough.\" dough:", ["Hamur ve (argo) para", "Ekmek ve pasta"], 0, "dough = hamur / para."),
        mc("Esprinin son, can alıcı cümlesi:", ["Setup", "Punchline"], 1, "Punchline."),
        mc("\"Why did the scarecrow win an award? He was outstanding in his field.\" Kelime oyunu:", ["outstanding in his field: alanında üstün / tarlada duran", "award: ödül / çiftlik"], 0, "Pun."),
        mc("Kötü bir \"dad joke\"a tipik tepki:", ["Oh no. That's terrible! (gülerek)", "I'm offended."], 0, "Tepki."),
        gap("I didn't ___ the joke. Can you explain it? (anlamak)", ["get", "understand"], "get the joke."),
        gap("He's always ___ jokes at parties. (espri yapmak)", ["cracking", "telling", "making"], "cracking jokes."),
        gap("Wait for a short pause before the ___. (son cümle)", ["punchline"], "punchline."),
        gap("It was so funny that I couldn't keep a ___ face. (ciddi)", ["straight"], "keep a straight face."),
        listen("Why did the bicycle fall over? ... Because it was two tired.", "Bu espri hangi kelime oyununa dayanıyor?", ["two tired (iki tekerlek) / too tired (çok yorgun)", "bicycle / bike"], 0, "two / too + tyre / tired."),
        match([("I lost interest.", "interest: faiz / ilgi"), ("They don't have the guts.", "guts: cesaret / iç organlar"), ("It's impossible to put down.", "put down: elinden bırakmak / yere indirmek"), ("Too many problems.", "problems: sorular / dertler"), ("Not enough dough.", "dough: hamur / para")], "Her espriyi kelime oyunuyla eşleştirin."),
    ],
    {"kind": "speaking", "task": speak("(1) Ders metnindeki esprilerden ikisini doğru zamanlamayla (punchline'dan önce kısa bir duraklama) anlatın ve her birindeki kelime oyununu açıklayın. (2) Sonra çok anlamlı bir İngilizce kelimeden yararlanarak kendi kelime oyununuzu oluşturmaya çalışın (örneğin: bark, light, bright, current, break, match). Kötü olabilir, sorun değil!",
                                       "First joke: I'm reading a book about anti-gravity... It's impossible to put down. The pun is on \"put down\": you can't put a good book down because it's interesting, and you can't put an anti-gravity book down because it floats. Second: Why was the maths book sad?... It had too many problems. \"Problems\" means maths questions, but also personal difficulties. My own pun: I wanted to become an electrician, but I wasn't sure about the job, so I went with the current. Or: Why did the student eat his homework? Because the teacher said it was a piece of cake. OK, that's terrible, I know!",
                                       ["Doğru zamanlama", "Kelime oyununun açıklanması", "Kendi kelime oyunu denemesi", "Rahat ve eğlenceli ton"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Kendini tiye alma, kuru mizah ve takılma", "Kendini tiye alan mizahı, kuru (deadpan) mizahı ve dostça takılmayı (banter) tanıyıp uygun şekilde karşılık verebilir ve mizahın kültürler arası farklılıklarının farkında olabilirim.",
    {"kind": "dialogue", "title": "Ofiste bir sabah", "lines": [
        {"speaker": "Priya", "text": "Nice of you to join us, Ollie. Did you get lost on the way from the car park?"},
        {"speaker": "Ollie", "text": "As a matter of fact, I did. My sense of direction is legendary. I once got lost in my own flat."},
        {"speaker": "Priya", "text": "I believe it. Anyway, how was your presentation yesterday?"},
        {"speaker": "Ollie", "text": "Oh, it went brilliantly. Only three people fell asleep, and one of them was me."},
        {"speaker": "Priya", "text": "Well, you're getting better. Last time it was five."},
        {"speaker": "Ollie", "text": "Exactly. At this rate, I'll be giving keynote speeches by 2050."},
        {"speaker": "Priya", "text": "Steady on. Let's not get carried away."}],
     "questions": [
        mc("Is Priya really angry with Ollie?", ["Yes, she is very angry.", "No, it's friendly banter."], 1, "Banter."),
        mc("What kind of humour does Ollie use about himself?", ["Self-deprecating humour", "Aggressive humour"], 0, "\"I once got lost in my own flat.\""),
     ]},
    {"explanation": "**1. Kendini tiye alma (self-deprecating humour):** Kendi zayıflıklarınızla **şakalaşmak**. İngiliz kültüründe çok değerlidir; **alçakgönüllülük** ve **özgüven** gösterir.\n\n- *My sense of direction is legendary. I once got lost in my own flat.*\n- *Only three people fell asleep, and one of them was me.*\n- *I'm not saying I'm a bad cook, but my smoke alarm cheers when I enter the kitchen.*\n\n**2. Kuru mizah (deadpan / dry humour):** Komik bir şeyi **tamamen ciddi bir yüzle** ve **düz bir tonla** söylemek. Karşınızdaki kişinin şaka yaptığını anlamak zor olabilir.\n\n- *\"How was your holiday?\" \"Wonderful. I only lost my passport twice.\"*\n- *\"Is it raining?\" \"No, the sky is just crying for no reason.\"*\n\n**3. Dostça takılma (banter):** Arkadaşlar ya da iş arkadaşları arasında **karşılıklı, şakacı iğnelemeler**. Önemli olan **ilişkinin iyi** olması ve **karşılıklı** olmasıdır.\n\n| Takılma | Uygun karşılık |\n|---|---|\n| *Nice of you to join us!* (geç kalana) | *Well, I like to make an entrance.* |\n| *Did you get dressed in the dark?* | *It's called fashion. Look it up.* |\n| *You're getting better. Last time it was five.* | *Exactly. I'm a work in progress.* |\n\n**Faydalı ifadeler:**\n\n- ***I'm only teasing / joking / pulling your leg.*** (Sadece takılıyorum.)\n- ***Steady on.*** (Yavaş ol, abartma.)\n- ***Don't take it the wrong way.*** (Yanlış anlama.)\n- ***No offence (intended).*** (Kırıcı olmak istemem.)\n- ***None taken.*** (Alınmadım.)\n\n**Dikkat: Kültürler arası farklar!**\n\n- Banter **çizgiyi aşınca** zorbalığa (*bullying*) dönüşebilir.\n- Yeni tanıştığınız biriyle, bir yöneticiyle ya da hassas konularda (görünüş, aile, din, köken) **takılmayın**.\n- Emin değilseniz: Önce **kendinizi** tiye alın, başkasını değil.",
     "examples": [{"en": "I'm only pulling your leg!", "tr": "Sadece takılıyorum!"},
                  {"en": "\"No offence, but your singing is awful.\" \"None taken. I know.\"", "tr": "\"Kusura bakma ama şarkı söyleyişin berbat.\" \"Alınmadım. Biliyorum.\""},
                  {"en": "I'm not a morning person. Or an afternoon person, really.", "tr": "Sabah insanı değilim. Öğleden sonra insanı da değilim aslında."}],
     "turkishNote": "Türk kültüründe de arkadaşlar arasında takılma (\"laf sokma\", \"dalga geçme\") yaygındır, ama genellikle daha açık ve yüksek tonla yapılır. İngiliz banter'ı ise genellikle düz bir tonla ve hiç gülmeden yapılır, bu yüzden Türk öğrenciler ilk başta bunu gerçek bir eleştiri sanabilir. Kendini tiye alma da İngiliz kültüründe çok değer görür; Türkçede bazen özgüven eksikliği gibi algılanabilecek bu tür espriler, İngilizcede genellikle sempati ve özgüven işaretidir."},
    [
        mc("Kendini tiye alma:", ["I'm so talented that everyone envies me.", "I'm such a bad cook that my smoke alarm cheers when I cook."], 1, "Self-deprecating."),
        mc("\"I'm only pulling your leg.\" anlamı:", ["Bacağını çekiyorum.", "Sadece takılıyorum."], 1, "pull someone's leg."),
        mc("\"No offence, but ...\" sonrası uygun cevap:", ["None taken.", "No problem taken."], 0, "None taken."),
        mc("Banter ne zaman uygun değil?", ["Yakın arkadaşlarla", "Yeni tanışılan biriyle hassas bir konuda"], 1, "Dikkat."),
        gap("Don't take it the wrong ___. I'm just joking.", ["way"], "take it the wrong way."),
        gap("She has a very ___ sense of humour. She never smiles when she's joking. (kuru)", ["dry", "deadpan"], "dry / deadpan."),
        gap("There's a lot of friendly ___ in our team. (takılma)", ["banter"], "banter."),
        gap("Steady ___! Let's not get carried away. (Yavaş ol)", ["on"], "Steady on."),
        listen("\"So, how did the driving test go?\" \"Oh, really well. The examiner only screamed twice, and I only hit one cone. Well, three, but who's counting?\"", "Sürüş sınavı nasıl geçti?", ["Çok iyi geçti.", "Kötü geçti; konuşan kendini tiye alıyor."], 1, "Self-deprecating + irony."),
        match([("I'm only pulling your leg.", "Sadece takılıyorum."), ("No offence.", "Kırıcı olmak istemem."), ("None taken.", "Alınmadım."), ("Steady on.", "Yavaş ol, abartma."), ("Nice of you to join us!", "Geç kalana takılma")], "Her ifadeyi anlamıyla eşleştirin."),
    ],
    {"kind": "speaking", "task": speak("(1) Kendinizle ilgili kendini tiye alan, kısa ve komik 3 cümle söyleyin (örneğin yönelim duygunuz, yemek yapma beceriniz, sabahları uyanmanız, spor yeteneğiniz hakkında). (2) Bir arkadaşınızın size yaptığı şu takılmalara esprili ve dostça bir cevap verin: \"Nice of you to join us!\" (geç kaldınız) / \"Did you cut your hair yourself?\" / \"Wow, you actually cooked something?\" (3) Takılmanın ne zaman çizgiyi aştığını kısaca açıklayın.",
                                       "One: I have a fantastic sense of direction. I once got lost in a shopping centre for forty minutes, and it only has one floor. I'm also an excellent cook. My family have never been to hospital after one of my meals, well, not more than once. And I'm a real morning person, as long as morning starts at eleven. Two: \"Nice of you to join us!\" \"Well, I like to make an entrance.\" \"Did you cut your hair yourself?\" \"It's called a bold new look. You'll all be copying it next week.\" \"Wow, you actually cooked something?\" \"Don't sound so surprised. The fire brigade only came once.\" Three: Banter crosses the line when it's one-sided, when it's about sensitive topics like someone's appearance or background, or when the other person is clearly hurt and not laughing.",
                                       ["Kendini tiye alan espriler", "Takılmaya esprili cevaplar", "Kültürel farkındalık", "Doğal ve rahat ton"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Mizahi yazı", "Hafife alma, ironi, abartı, kendini tiye alma ve beklenmedik dönüşleri birleştirerek eğlenceli bir anı ya da mizahi bir köşe yazısı yazabilirim.",
    {"kind": "text", "title": "Mizahi köşe yazısı: \"My Brief Career as a Gardener\" (kurgusal)", "body": "Last spring, I decided to become a gardener. How hard could it be? You put a seed in the ground, add water and wait. Even I could manage that, or so I thought.\n\nI spent a small fortune at the garden centre: tomato plants, herbs, a lemon tree and a pair of gloves so expensive that I was afraid to get them dirty. The man at the till asked if I had any experience. \"Plenty,\" I said, which was technically true if you count killing three cactuses.\n\nWithin a week, the basil had died. Within two weeks, the tomatoes had given up. The lemon tree, to its credit, held on bravely for a month, before deciding that life with me was simply not worth it.\n\nMy neighbour, a retired teacher with a garden like a postcard, came round to offer advice. She looked at my balcony for a long time. \"Well,\" she said finally, \"it's certainly... a beginning.\"\n\nI have since discovered that the secret to gardening is patience, knowledge and the ability to tell the difference between a weed and a plant. I possess none of these qualities.\n\nStill, there is one survivor: a single, determined dandelion that appeared in a pot on its own. I didn't plant it. I don't water it. It is thriving. I have decided to take this as a compliment.",
     "questions": [
        mc("What happened to the lemon tree?", ["It grew lemons.", "It died after about a month.", "The neighbour took it."], 1, "\"held on bravely for a month, before deciding that life with me was simply not worth it\""),
        mc("What is ironic about the dandelion?", ["The writer planted it carefully.", "It's the only survivor, and the writer didn't plant or water it.", "It died first."], 1, "Durum ironisi."),
     ]},
    {"explanation": "**Mizahi yazının araçları (bu ünitedekiler + önceki üniteler):**\n\n| Araç | Örnek |\n|---|---|\n| **Retorik soru + ironi** | *How hard could it be?* (Çok zor olacak, okuyucu bunu sezer.) |\n| **Kendini tiye alma** | *Even I could manage that, or so I thought.* / *I possess none of these qualities.* |\n| **Abartma** | *gloves so expensive that I was afraid to get them dirty* |\n| **Hafife alma** | *\"It's certainly... a beginning.\"* |\n| **Kişileştirme** (C2 Ünite 5) | *The lemon tree ... deciding that life with me was simply not worth it.* |\n| **Teknik doğruluk esprisi** | *\"Plenty,\" ... which was technically true if you count killing three cactuses.* |\n| **Üçleme + beklenmedik son** | *patience, knowledge and the ability to tell the difference between a weed and a plant* |\n| **Durum ironisi** | Ekmediği karahindiba yaşıyor. |\n| **Kısa son cümle** | *I have decided to take this as a compliment.* |\n\n**Mizahi yazı için ipuçları:**\n\n1. **Gerçek bir deneyimden yola çıkın.** En komik hikâyeler genellikle gerçektir.\n2. **Kendinizi tiye alın**, başkalarını değil.\n3. **Ritim:** Uzun bir cümle kurup, kısa ve beklenmedik bir cümleyle bitirin.\n4. **Az, ama etkili:** Her cümlede espri olması gerekmez. Ciddi cümleler, komik cümlelerin etkisini artırır.\n5. **Abartı ve hafife almayı karıştırın:** Küçük şeyleri abartın, büyük felaketleri hafife alın.\n6. **Güçlü bir son:** Son cümle bir dönüş ya da ironik bir yorum olsun.\n\n**Dikkat:** İyi mizah **kimseyi aşağılamaz**. Din, köken, cinsiyet, engellilik gibi konularda espri yapmaktan kaçının.",
     "examples": [{"en": "How hard could it be? (Very hard, as it turned out.)", "tr": "Ne kadar zor olabilirdi ki? (Çok zormuş, sonradan anlaşıldı.)"},
                  {"en": "Even I could manage that, or so I thought.", "tr": "Bunu ben bile yapabilirdim, ya da öyle sanıyordum."},
                  {"en": "I have decided to take this as a compliment.", "tr": "Bunu bir iltifat olarak kabul etmeye karar verdim."}],
     "turkishNote": "Türk edebiyatında Aziz Nesin ve Haldun Taner gibi yazarlar mizahi öykü geleneğinin önemli temsilcileridir ve toplumsal hicivle tanınırlar. İngiliz mizahi yazısı ise genellikle kendini tiye alma, hafife alma ve günlük hayatın küçük absürtlükleri üzerine kuruludur. Türk öğrenciler İngilizce mizahi yazı yazarken genellikle çok fazla abartma kullanır. İngiliz tarzı için abartıyı hafife almayla dengelemek ve espriyi bazen okuyucunun kendisinin bulmasına bırakmak daha etkilidir."},
    [
        mc("\"How hard could it be?\" bir mizahi metinde genellikle:", ["Gerçekten kolay olduğunu gösterir.", "Çok zor olacağını ima eder."], 1, "İroni."),
        mc("İyi bir mizahi yazıda:", ["Her cümlede espri olmalıdır.", "Ciddi ve komik cümleler dengelenmelidir."], 1, "Denge."),
        mc("Güvenli mizah stratejisi:", ["Başkalarını tiye almak", "Kendini tiye almak"], 1, "Self-deprecating."),
        mc("Mizahi yazının sonu:", ["Uzun bir özet", "Kısa, ironik bir dönüş"], 1, "Güçlü son."),
        gap("Even I could manage that, or so I ___.", ["thought"], "or so I thought."),
        gap("How ___ could it be? (zor)", ["hard", "difficult"], "How hard could it be?"),
        gap("The gloves were ___ expensive that I was afraid to wear them. (abartma)", ["so"], "so ... that."),
        gap("I have decided to take this as a ___. (iltifat)", ["compliment"], "compliment."),
        listen("I've always considered myself a good driver. My family have a different opinion. My father calls me \"the one-way specialist\", because I once drove the wrong way down a one-way street for two kilometres. In my defence, nobody else was going my way.", "\"In my defence, nobody else was going my way\" neden komik?", ["Konuşan haklı olduğu için", "Ters yönde gittiği için kimsenin onunla aynı yöne gitmemesi doğal; ironik bir savunma"], 1, "İroni + kendini tiye alma."),
        typ("Kendini tiye alan bir son cümle yazın: \"Bütün bitkiler öldü, sadece bir kaktüs kaldı. Ama o da ...\" (But even the cactus ...)", variants("But even the cactus looks worried.", "But even the cactus is looking worried.", "But even the cactus seems worried.", "But even the cactus looks nervous.", "But even the cactus is thinking of leaving."), "But even the cactus looks worried."),
    ],
    {"kind": "writing", "task": write("Hayatınızdan (gerçek ya da biraz abartılmış) bir aksiliği ya da başarısız bir girişimi anlatan mizahi bir anı yazısı ya da köşe yazısı yazın (220–280 kelime). Konu önerileri: yemek yapmaya ya da yeni bir spora başlamak, bir mobilyayı kendi başınıza kurmak, bir yabancı dilde ilk konuşmanız, bir tatil planı. En az şu araçları kullanın: retorik soru + ironi, kendini tiye alma, abartma, hafife alma, bir durum ironisi ve kısa, ironik bir son cümle. Kimseyi aşağılamayın.",
                                      "My Adventure with Flat-Pack Furniture\n\nLast month, I decided to build a bookcase. The box said \"Easy assembly, 30 minutes\". How hard could it be? I have a university degree. I can follow instructions. Or so I thought.\n\nThe instructions consisted of twelve pages of drawings and no words. In the drawings, a smiling cartoon person assembled the bookcase with one hand while apparently drinking a cup of tea with the other. I did not have a cup of tea. I had forty-seven screws, nine wooden panels and a growing sense of despair.\n\nAfter two hours, I had built something. It was not exactly a bookcase. It was more of a leaning tower, with one shelf upside down and a mysterious extra piece that seemed to belong to a completely different universe.\n\nMy flatmate came home, looked at it for a long moment and said, \"Well, it's certainly... original.\" I chose to take this as praise.\n\nAt eleven o'clock that night, I finally admitted defeat and watched a video online. The man in the video built the same bookcase in exactly twenty-eight minutes. He was ten years old.\n\nThe bookcase is now standing, more or less, in the corner of my bedroom. It holds three books and a plant. I am afraid to add a fourth book. I have, however, learned one important lesson: always read the instructions, even when there are no words in them.\n\nNext month, I'm planning to build a wardrobe. What could possibly go wrong?",
                                      ["Retorik soru ve ironi", "Kendini tiye alma ve abartı", "Hafife alma ve durum ironisi", "Ritim ve zamanlama", "Güçlü, ironik son"])},
)

u.test([
    mc("\"It's not exactly cheap.\" anlamı:", ["Oldukça ucuz.", "Çok pahalı."], 1, "Litotes"),
    mc("\"Not bad!\" genellikle:", ["Kötü", "İyi, hatta çok iyi"], 1, "Litotes"),
    mc("Yağmurda: \"Lovely weather!\"", ["İçten", "İronik"], 1, "Verbal irony"),
    mc("Durum ironisi:", ["A fire station burns down.", "It's sunny in Antalya."], 0, "Situational irony"),
    mc("\"I'm only pulling your leg.\" anlamı:", ["Sadece takılıyorum.", "Bacağını çekiyorum."], 0, "pull someone's leg"),
    gap("We had a ___ of a problem: the plane's engine caught fire. (hafife alma)", ["bit"], "a bit of a"),
    gap("\"My car's broken down again.\" \"Oh, ___. Just what you needed.\" (alaycı: harika)", ["great", "brilliant", "wonderful", "perfect", "fantastic"], "Sarcasm"),
    gap("I didn't ___ the joke. (anlamak)", ["get", "understand"], "get the joke"),
    gap("She told the ___ perfectly, and everyone laughed. (son cümle)", ["punchline", "joke"], "punchline"),
    gap("\"No offence, but your tie is awful.\" \"___ taken.\"", ["None"], "None taken"),
    gap("Don't take it the wrong ___.", ["way"], "take it the wrong way"),
    gap("How hard could it ___? (ironik soru)", ["be"], "How hard could it be?"),
    listen("I used to work in a shoe recycling shop. It was sole destroying.", "Bu espri hangi kelime oyununa dayanıyor?", ["sole (ayakkabı tabanı) / soul (ruh): soul-destroying = ruhu öldüren", "shoe / show"], 0, "Pun: sole / soul."),
    typ("Hafife alarak yeniden söyleyin: \"The party was a complete disaster.\" (The party could have ...)", variants("The party could have gone better.", "The party could have gone a bit better.", "The party could have gone slightly better.", "The party could have been better."), "The party could have gone better."),
    write("Bir tatilde, bir düğünde, bir iş görüşmesinde ya da önemli bir günde yaşadığınız (gerçek ya da hayali) bir aksiliği anlatan mizahi bir yazı yazın (220–280 kelime). En az şunları kullanın: retorik soru + ironi (How hard could it be? / What could possibly go wrong?), kendini tiye alma, abartma, hafife alma (a bit of a problem, not ideal), bir durum ironisi ve kısa, ironik bir son cümle. Ciddi ve komik cümleleri dengeleyin; kimseyi aşağılamayın.",
          "The Day I Tried to Impress My Future In-Laws\n\nWhen my partner's parents invited me to dinner for the first time, I decided to make a good impression by bringing a homemade cake. I'd watched a baking show once. How hard could it be?\n\nThe recipe said \"simple chocolate cake, one hour\". Three hours later, my kitchen looked like a crime scene, and the cake looked like a small brown brick. I decorated it with strawberries to distract from the shape. It did not work.\n\nThe journey was also a bit of a challenge. The bus was late, and I had to run the last kilometre while holding the cake in front of me like a trophy. I arrived sweaty, out of breath and approximately forty minutes late. Not ideal.\n\nMy partner's father opened the door, looked at me, looked at the cake and said, very politely, \"Oh. You've brought... something.\"\n\nDinner was lovely, actually. Everyone was kind, and nobody mentioned the cake. Then it was time for dessert. I cut the first slice, or rather, I tried to. The knife bent.\n\nIn the end, we had ice cream from the freezer. My partner's mother laughed so hard she had to sit down, which, I'm told, she hadn't done since 1998.\n\nThe ironic thing is that they still talk about that evening. \"Remember the cake?\" they say, every single time I visit. Apparently, it was the best first impression anyone has ever made.\n\nI'm baking another one for their anniversary. What could possibly go wrong?",
          ["Retorik soru ve ironi", "Kendini tiye alma ve abartı", "Hafife alma", "Durum ironisi", "Ritim ve ironik son"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

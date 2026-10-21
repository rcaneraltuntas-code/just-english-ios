"""C1 Ünite 9: Üslup."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("C1", 9, "Üslup", "Register",
         "Bir metnin üslubunu (resmî, nötr, samimi) dil özelliklerinden tanıyabilir, aynı mesajı farklı üsluplarda yeniden yazabilir, resmî kelime ve bağlaçlar kullanabilir, günlük konuşmanın belirsizlik ve dolgu ifadelerini doğal bir şekilde anlayıp kullanabilir ve bağlama göre üslup değiştirebilirim.",
         ["üslup yelpazesi: resmî, nötr, samimi", "resmî kelime seçimi, isimleştirme ve bağlaçlar", "samimi konuşma: belirsiz dil ve dolgu ifadeleri", "farklı üsluplarda rica, şikâyet ve özür", "aynı içeriği farklı üsluplarda yazmak"],
         ["iş ve resmî yazışma", "günlük iletişim", "dijital iletişim"],
         {"title": "Üç farklı ses", "durationMinutes": 45,
          "goal": "Her gruba bir durum verilir (otelde kayıp bavul, iş yerinde terfi haberi, komşuyla gürültü sorunu). Grup aynı durumu üç farklı üslupta canlandırır: arkadaşa sesli mesaj, yöneticiye kısa e-posta, resmî şikâyet / duyuru. Sınıf her versiyonda hangi dil özelliklerinin üslubu değiştirdiğini not eder."})

u.vocab([
    ("register", "üslup, dil düzeyi", "The register of this email is too informal.", "Bu e-postanın üslubu fazla samimi.", None),
    ("formal", "resmî", "Use formal language in a cover letter.", "Ön yazıda resmî dil kullan.", None),
    ("informal", "samimi, gayri resmî", "Text messages are usually informal.", "Kısa mesajlar genellikle samimidir.", None),
    ("colloquial", "konuşma diline ait", "\"Gonna\" is a colloquial form.", "\"Gonna\" konuşma diline ait bir biçimdir.", None),
    ("tone", "ton", "The tone of the letter was polite but firm.", "Mektubun tonu kibar ama kararlıydı.", None),
    ("nominalisation", "isimleştirme", "Nominalisation makes writing more formal.", "İsimleştirme yazıyı daha resmî yapar.", None),
    ("thus", "böylece, bu nedenle (resmî)", "Costs fell, thus increasing profits.", "Maliyetler düştü, böylece kâr arttı.", None),
    ("hence", "bu yüzden (resmî)", "The road was closed; hence the delay.", "Yol kapalıydı; gecikme bu yüzden.", None),
    ("whereby", "ki bu yolla", "a system whereby customers can pay online", "müşterilerin çevrimiçi ödeme yapabildiği bir sistem", None),
    ("prior to", "-den önce (resmî)", "Please arrive 30 minutes prior to departure.", "Lütfen kalkıştan 30 dakika önce gelin.", None),
    ("subsequently", "daha sonra (resmî)", "He was subsequently promoted.", "Daha sonra terfi ettirildi.", None),
    ("commence", "başlamak (çok resmî)", "The ceremony will commence at 10 a.m.", "Tören saat 10'da başlayacak.", None),
    ("inquire / enquire", "bilgi almak (resmî)", "I am writing to enquire about the vacancy.", "Açık pozisyon hakkında bilgi almak için yazıyorum.", None),
    ("purchase", "satın almak (resmî)", "Tickets may be purchased online.", "Biletler çevrimiçi satın alınabilir.", None),
    ("stuff", "şeyler (samimi)", "I've got loads of stuff to do.", "Yapacak bir sürü işim var.", None),
    ("and so on / and stuff", "ve benzeri, falan", "We talked about work, family and so on.", "İşten, aileden falan konuştuk.", None),
    ("or something", "ya da öyle bir şey", "Let's get pizza or something.", "Pizza ya da öyle bir şey alalım.", None),
    ("kind of / sort of", "biraz, bir nevi (samimi)", "I'm kind of tired.", "Biraz yorgunum.", None),
    ("I mean", "yani, demek istediğim", "It's good. I mean, it's not perfect, but it's good.", "İyi. Yani mükemmel değil ama iyi.", None),
    ("you know", "bilirsin, hani", "It was, you know, a bit awkward.", "Hani biraz garipti.", None),
    ("cheers", "teşekkürler; şerefe (BrE, samimi)", "Cheers for your help!", "Yardımın için sağ ol!", None),
    ("regards", "saygılar (e-posta kapanışı)", "Kind regards, Ali", "Saygılarımla, Ali", None),
    ("code-switching", "duruma göre dil / üslup değiştirme", "Most people code-switch between work and home.", "Çoğu insan iş ve ev arasında üslup değiştirir.", None),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Üslup yelpazesi", "Bir metnin resmî, nötr ya da samimi olduğunu dil özelliklerinden tanıyabilir ve nedenlerini açıklayabilirim.",
    {"kind": "text", "title": "Aynı haber, üç üslup", "body": "Text 1:\n\"Hey! Guess what? The boss says we're getting Fridays off next month. No more Friday meetings! Can't wait 😄\"\n\nText 2:\n\"Hi all, just to let you know that we'll be trying out a four-day week next month. Fridays will be a day off for everyone. More details to follow.\"\n\nText 3:\n\"Dear colleagues,\nPlease be advised that, commencing 1 March, the company will be introducing a four-day working week on a trial basis. Accordingly, employees will not be required to attend the office on Fridays. Further information will be circulated in due course.\nKind regards,\nHuman Resources\"",
     "questions": [
        mc("Which text is the most formal?", ["Text 1", "Text 2", "Text 3"], 2, "Please be advised, commencing, accordingly."),
        mc("When does the four-day week start?", ["Next week", "Next month / 1 March", "Next year"], 1, "\"next month\" / \"commencing 1 March\""),
     ]},
    {"explanation": "**Register (üslup)**, konuşmacının **kime, nerede ve neden** konuştuğuna göre dil seçimidir.\n\n**Üslup yelpazesi:**\n\n| | Samimi (informal) | Nötr (neutral) | Resmî (formal) |\n|---|---|---|---|\n| **Kime?** | arkadaş, aile | iş arkadaşı, tanıdık | yönetici, kurum, yabancı |\n| **Kısaltmalar** | çok: *can't, we're, gonna* | bazen: *we'll* | yok: *cannot, we will* |\n| **Kelimeler** | günlük, phrasal verb: *get, find out* | genel | Latin kökenli: *receive, ascertain* |\n| **Cümleler** | kısa, eksik: *Can't wait!* | orta | uzun, karmaşık |\n| **Edilgen** | nadiren | bazen | sık: *will be circulated* |\n| **Kişi** | *I, you* | *we* | kişisiz: *Please be advised* |\n| **Emojiler, ünlemler** | evet | az | hayır |\n\n**Resmî metin işaretleri:**\n\n- *Please be advised that ...* (Bildiririz ki ...)\n- *commencing / prior to / subsequently / in due course*\n- *employees will not be required to ...*\n- Kişisiz edilgen\n\n**Samimi metin işaretleri:**\n\n- *Hey! / Guess what?*\n- Eksik cümleler: *Can't wait!*\n- Duygusal ifadeler ve emojiler\n\n**Nötr** üslup iş hayatında en yaygın olanıdır: kibar, açık, ama soğuk değil.",
     "examples": [{"en": "Informal: Can't make it tonight, sorry!", "tr": "Samimi: Bu akşam gelemiyorum, kusura bakma!"},
                  {"en": "Neutral: I'm afraid I won't be able to come tonight.", "tr": "Nötr: Maalesef bu akşam gelemeyeceğim."},
                  {"en": "Formal: I regret that I will be unable to attend this evening.", "tr": "Resmî: Bu akşam katılamayacağım için üzgünüm."}],
     "turkishNote": "Türkçede üslup farkı büyük ölçüde \"sen / siz\" ayrımıyla ve fiil ekleriyle yapılır. İngilizcede \"you\" her zaman aynıdır, bu yüzden üslup kelime seçimi, cümle yapısı ve kısaltmalarla belirlenir. Türk öğrencilerin sık yaptığı hata, İngilizcede \"sen\" ile \"siz\" farkı olmadığı için her şeyi aynı tonda yazmaktır. Oysa \"Can you send it?\" ile \"I would be grateful if you could send it\" arasındaki fark, Türkçedeki \"Gönderir misin?\" ile \"Göndermeniz rica olunur\" arasındaki farka benzer."},
    [
        mc("En resmî:", ["Can't come, sorry!", "I regret that I will be unable to attend."], 1, "Resmî."),
        mc("Nötr üslup:", ["Hey! Guess what?", "Just to let you know that the meeting has moved to 3 p.m."], 1, "Nötr."),
        mc("Resmî metin işareti:", ["Please be advised that ...", "Guess what?"], 0, "Resmî."),
        mc("Samimi metin işareti:", ["Eksik cümleler ve emojiler", "Kişisiz edilgen yapılar"], 0, "Samimi."),
        gap("Formal: \"Further information will be ___ in due course.\" (dağıtılmak)", ["circulated", "sent", "provided"], "will be circulated."),
        gap("Formal: \"Please be ___ that the office will close early.\"", ["advised"], "Please be advised."),
        gap("Neutral: \"Just to ___ you know, the meeting has been moved.\"", ["let"], "Just to let you know."),
        gap("Formal: \"I regret that I will be ___ to attend.\"", ["unable"], "unable to."),
        listen("Right, guys, quick one. Pizza's here, so grab a slice before it's gone. Oh, and don't forget, we're off early on Friday. Cheers!", "Bu mesajın üslubu nedir?", ["Resmî", "Samimi", "Akademik"], 1, "guys, quick one, grab, cheers."),
        match([("Hey! Can't wait!", "samimi"), ("Hi all, just to let you know ...", "nötr"), ("Please be advised that ...", "resmî"), ("Cheers for that!", "samimi"), ("Further information will be provided in due course.", "resmî")], "Her ifadeyi üslubuyla eşleştirin."),
    ],
    {"kind": "speaking", "task": speak("Aynı haberi üç farklı kişiye üç farklı üslupta söyleyin: \"Ofis gelecek hafta pazartesi kapalı olacak çünkü elektrik bakımı yapılacak.\" (1) En yakın arkadaşınıza sesli mesaj. (2) Ekip arkadaşlarınıza nötr bir mesaj. (3) Şirket adına müşterilere resmî bir duyuru.",
                                       "One: Hey! Good news, the office is closed next Monday. Something about electrical work. Long weekend for us! Two: Hi everyone, just to let you know that the office will be closed next Monday for electrical maintenance. Please plan to work from home that day. Thanks! Three: Dear customers, please be advised that our office will be closed on Monday 12 May due to scheduled electrical maintenance. We apologise for any inconvenience this may cause. Normal opening hours will resume on Tuesday.",
                                       ["Üç üslup arasında net fark", "Kelime seçimi", "Kısaltma ve cümle yapısı", "Uygun hitap"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "Resmî dilin araçları", "Resmî kelimeler, isimleştirme (nominalisation) ve resmî bağlaçlarla (thus, hence, whereby, prior to) metnimin üslubunu yükseltebilirim.",
    {"kind": "text", "title": "Bir şirket raporundan iki versiyon", "body": "Draft (too informal):\n\"We decided to change the way we deliver stuff because customers kept complaining that it took ages. So we started using a new app. Now people can see where their orders are. Because of this, we've got way fewer complaints.\"\n\nFinal version (formal):\n\"Following repeated complaints regarding delivery times, the decision was taken to restructure the company's delivery system. A new tracking application was subsequently introduced, whereby customers are able to monitor the status of their orders in real time. This has resulted in a significant reduction in the number of complaints received, thus improving overall customer satisfaction.\"",
     "questions": [
        mc("Why did the company change its delivery system?", ["To save money", "Because customers complained about delivery times", "Because of a new law"], 1, "\"Following repeated complaints regarding delivery times\""),
        mc("What can customers do with the new app?", ["Pay online", "Monitor the status of their orders", "Cancel orders"], 1, "\"monitor the status of their orders in real time\""),
     ]},
    {"explanation": "**1. Resmî kelime seçimi:**\n\n| Samimi | Resmî |\n|---|---|\n| get | receive / obtain |\n| buy | purchase |\n| start | commence / begin |\n| help | assist |\n| ask | enquire / request |\n| need | require |\n| before / after | prior to / following |\n| later | subsequently |\n| about | regarding / concerning |\n| so | therefore / thus / hence |\n| a lot of / way fewer | a significant number of / significantly fewer |\n\n**2. İsimleştirme (nominalisation):** Fiil ya da sıfatı isme çevirmek, metni daha **resmî, yoğun ve kişisiz** yapar.\n\n| Fiil / sıfat (samimi) | İsim (resmî) |\n|---|---|\n| We **decided** to change ... | **The decision** was taken to ... |\n| Customers **complained** a lot. | There were **repeated complaints**. |\n| Complaints **fell** a lot. | There was **a significant reduction** in complaints. |\n| It's **important** to ... | **The importance** of ... |\n| We **failed** to ... | **The failure** to ... |\n\n**3. Resmî bağlaçlar:**\n\n| Bağlaç | Kullanım |\n|---|---|\n| **thus** | ..., **thus** improving satisfaction. (böylece) |\n| **hence** | The road was closed; **hence** the delay. (bu yüzden; ardından isim gelebilir) |\n| **whereby** | a system **whereby** customers can ... (ki bu sistemle) |\n| **whereas** | X is ..., **whereas** Y is ... (oysa) |\n| **notwithstanding** | **Notwithstanding** the cost, ... (çok resmî: -e rağmen) |\n\n(İsimleştirmeyi C2 Ünite 3'te akademik yazı için ayrıntılı göreceğiz.)",
     "examples": [{"en": "Following a review of the budget, the decision was taken to reduce costs.", "tr": "Bütçenin gözden geçirilmesinin ardından maliyetleri azaltma kararı alındı."},
                  {"en": "The bridge was closed for repairs; hence the long queues.", "tr": "Köprü onarım için kapatılmıştı; uzun kuyruklar bu yüzden."},
                  {"en": "Tickets may be purchased prior to arrival.", "tr": "Biletler varıştan önce satın alınabilir."}],
     "turkishNote": "Türkçe resmî dilde de isimleştirme çok yaygındır: \"karar verdik\" yerine \"karar alınmıştır\", \"şikâyet ettiler\" yerine \"şikâyetler alınmıştır\". Bu nedenle İngilizce nominalisation Türkçe konuşanlar için tanıdık bir mantıktır. Ancak dikkatli olun: Aşırı isimleştirme metni ağırlaştırır ve anlaşılmasını zorlaştırır. İyi bir resmî metin hem profesyonel hem de açık olmalıdır."},
    [
        mc("\"buy\" resmî karşılığı:", ["purchase", "pursue"], 0, "purchase."),
        mc("\"later\" resmî karşılığı:", ["subsequently", "consequently"], 0, "subsequently."),
        mc("İsimleştirilmiş hali: \"We decided to close the shop.\"", ["The decision was taken to close the shop.", "We were deciding the shop to close."], 0, "Nominalisation."),
        mc("\"The road was closed; hence the delay.\" hence anlamı:", ["oysa", "bu yüzden"], 1, "hence."),
        gap("Please arrive 20 minutes ___ to your appointment. (önce, resmî)", ["prior"], "prior to."),
        gap("Costs were reduced, ___ increasing profits. (böylece)", ["thus"], "thus + -ing."),
        gap("We introduced a system ___ employees can work from home. (ki bu sistemle)", ["whereby"], "whereby."),
        gap("There has been a significant ___ in complaints. (azalma)", ["reduction", "decrease", "fall", "decline"], "a significant reduction."),
        listen("Following a review of last year's results, the board has approved a new strategy. Subsequently, a number of changes will be introduced, whereby each department will be responsible for its own budget. This is expected to result in greater efficiency.", "Yeni sistemde her departman neden sorumlu olacak?", ["Kendi bütçesinden", "Yeni çalışan almaktan", "Müşteri şikâyetlerinden"], 0, "\"each department will be responsible for its own budget\""),
        typ("Resmîleştirin (isimleştirme ile): \"Prices went up a lot last year.\" (There was a ...)", variants("There was a significant increase in prices last year.", "There was a sharp increase in prices last year.", "There was a considerable increase in prices last year.", "There was a significant rise in prices last year.", "Last year, there was a significant increase in prices."), "There was a significant increase in prices last year."),
    ],
    {"kind": "speaking", "task": speak("Aşağıdaki samimi cümleleri bir şirket toplantısında resmî bir dille yeniden söyleyin. Resmî kelimeler, isimleştirme ve thus / hence / whereby / prior to / subsequently gibi bağlaçlar kullanın: (1) We decided to hire three more people because we've got way more work. (2) After we talked to customers, we changed the website. (3) Lots of people complained, so we're giving them money back. (4) Before you start, you need to read the rules.",
                                       "One: Due to a significant increase in workload, the decision was taken to recruit three additional members of staff. Two: Following consultation with our customers, the website was subsequently redesigned. Three: A considerable number of complaints were received; hence, refunds are being offered to all affected customers. Four: Prior to commencing work, all employees are required to read the company regulations, thus ensuring that everyone is aware of their responsibilities.",
                                       ["Resmî kelime seçimi", "İsimleştirme", "Resmî bağlaçlar", "Edilgen yapı"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "Günlük konuşmanın dili", "Samimi konuşmadaki belirsiz dil (stuff, or something) ve dolgu ifadelerini (you know, I mean, like) anlayıp doğal ve ölçülü kullanabilirim.",
    {"kind": "dialogue", "title": "Kafede", "lines": [
        {"speaker": "Kaan", "text": "So, how was the trip?"},
        {"speaker": "Zeynep", "text": "Oh, it was amazing. I mean, the weather was kind of terrible, but, you know, we didn't really care."},
        {"speaker": "Kaan", "text": "What did you do?"},
        {"speaker": "Zeynep", "text": "Loads of stuff. We went hiking, visited a couple of villages, ate tons of food, that sort of thing."},
        {"speaker": "Kaan", "text": "Sounds great. Where did you stay?"},
        {"speaker": "Zeynep", "text": "In this little wooden house or something. It was, like, two hundred years old, I think."},
        {"speaker": "Kaan", "text": "Nice. Anyway, we should go somewhere together sometime."},
        {"speaker": "Zeynep", "text": "Definitely! Maybe in the spring or whatever."}],
     "questions": [
        mc("What was the weather like?", ["Perfect", "Quite bad", "Very hot"], 1, "\"the weather was kind of terrible\""),
        mc("What did Zeynep do on the trip?", ["Only stayed in the hotel", "Went hiking, visited villages and ate a lot", "Went to museums"], 1, "\"We went hiking, visited a couple of villages, ate tons of food\""),
     ]},
    {"explanation": "Doğal günlük konuşma, ders kitaplarındaki \"mükemmel\" cümlelerden çok farklıdır.\n\n**1. Belirsiz dil (vague language):** Kesin olmak gereksiz olduğunda.\n\n| İfade | Örnek |\n|---|---|\n| **stuff / things** | Loads of **stuff**. |\n| **and stuff / and things (like that)** | We went hiking **and stuff**. |\n| **that sort of thing / that kind of thing** | ..., **that sort of thing**. |\n| **or something (like that)** | a wooden house **or something** |\n| **or whatever** | in the spring **or whatever** |\n| **a couple of** | **a couple of** villages (2–3) |\n| **loads of / tons of** | **tons of** food |\n| **-ish** | six**-ish**, green**-ish** |\n| **kind of / sort of** | **kind of** terrible |\n\n**2. Dolgu ifadeleri ve söylem belirleyicileri (fillers / discourse markers):**\n\n| İfade | İşlev |\n|---|---|\n| **you know** | dinleyiciyi dahil etmek, düşünmek |\n| **I mean** | açıklamak, düzeltmek |\n| **like** | (gençler arasında) örnek vermek, yaklaşık, alıntı |\n| **well** | düşünmek, cevaba başlamak |\n| **anyway** | konuyu değiştirmek / kapatmak |\n| **so** | konuya başlamak |\n| **right / OK** | yeni bölüme geçmek |\n| **actually** | düzeltme, şaşırtıcı bilgi |\n\n**Ölçülü olun!** Bu ifadeler konuşmayı **doğal** gösterir, ama çok kullanılırsa **kararsız ya da özensiz** bir izlenim verir. **Resmî yazıda ve sunumlarda kullanmayın.**",
     "examples": [{"en": "We talked about work, family and stuff like that.", "tr": "İşten, aileden falan konuştuk."},
                  {"en": "I mean, it's not a bad idea, but it's kind of expensive.", "tr": "Yani kötü bir fikir değil ama biraz pahalı."},
                  {"en": "Anyway, I'd better go. See you later!", "tr": "Neyse, gitsem iyi olacak. Sonra görüşürüz!"}],
     "turkishNote": "Türkçede de günlük konuşmada \"falan filan\", \"şey\", \"yani\", \"hani\", \"işte\" gibi ifadeler çok kullanılır ve İngilizcedeki \"and stuff\", \"I mean\", \"you know\" ile benzer işlev görür. Türk öğrenciler İngilizce konuşurken genellikle çok \"resmî ve kitabi\" konuşur ya da Türkçedeki dolguları (\"şey\", \"yani\") İngilizce cümlenin ortasına katar. Birkaç İngilizce dolgu ifadesi öğrenmek, düşünürken doğal kalmanızı sağlar."},
    [
        mc("\"We went shopping and stuff.\" anlamı:", ["Alışverişe gittik ve eşya aldık.", "Alışverişe gittik falan."], 1, "Belirsiz dil."),
        mc("\"I mean\" işlevi:", ["Açıklamak / düzeltmek", "Konuyu kapatmak"], 0, "I mean."),
        mc("\"Anyway, I'd better go.\" anyway işlevi:", ["Konuyu kapatmak", "Örnek vermek"], 0, "anyway."),
        mc("Resmî bir sunumda uygun değil:", ["approximately 200", "200 or something"], 1, "Belirsiz dil samimi."),
        gap("We visited museums, galleries, that sort of ___.", ["thing"], "that sort of thing."),
        gap("Let's meet at seven or ___ like that.", ["something"], "or something."),
        gap("It was, you ___, a bit awkward.", ["know"], "you know."),
        gap("There were ___ of people at the party. (çok, samimi)", ["loads", "tons", "lots"], "loads of."),
        listen("So, yeah, the interview was OK, I guess. I mean, they asked loads of questions about my experience and stuff. Anyway, they said they'd call me next week or something.", "Konuşan görüşmeyi nasıl buldu?", ["Mükemmel", "Fena değil, idare eder", "Berbat"], 1, "\"the interview was OK, I guess\""),
        typ("Daha doğal ve samimi söyleyin (and stuff / that sort of thing): \"We ate, we danced and we talked.\"", variants("We ate, danced, talked and stuff.", "We ate, danced and talked, that sort of thing.", "We ate, danced and stuff.", "We ate, we danced, that sort of thing.", "We ate, danced, talked, that sort of thing."), "We ate, danced, talked and stuff."),
    ],
    {"kind": "speaking", "task": speak("Bir arkadaşınıza geçen hafta sonunuzu doğal ve samimi bir şekilde anlatın (1 dakika). En az 3 belirsiz dil ifadesi (stuff, or something, that sort of thing, loads of, a couple of, -ish) ve en az 3 dolgu / söylem belirleyicisi (you know, I mean, well, anyway, actually, so) kullanın. Ama ölçülü olun!",
                                       "So, my weekend was actually pretty good. On Saturday, I met a couple of friends from university for breakfast, at ten-ish. We ate loads of food, you know, eggs, cheese, that sort of thing. Then we went for a walk by the sea. I mean, it was a bit cold, but it was nice. On Sunday, I just stayed at home, did some cleaning and stuff. Oh, and I watched a film or something in the evening. Anyway, how was yours?",
                                       ["Belirsiz dil", "Dolgu ifadeleri", "Doğallık ve ölçü", "Samimi ton"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Aynı mesaj, farklı ton", "Rica, şikâyet ve özür gibi işlevleri bağlama uygun üslupta (samimi, nötr, resmî) ifade edebilir ve üsluplar arasında geçiş yapabilirim.",
    {"kind": "text", "title": "Üç özür", "body": "Text message to a friend:\n\"So sorry I missed your party!! Totally forgot, I'm the worst 🙈 Let me buy you dinner to make up for it?\"\n\nEmail to a colleague:\n\"Hi Elif, I'm really sorry I missed the meeting this morning. My train was delayed, and I couldn't get a signal to let you know. Could you fill me in on what I missed? Thanks, and apologies again.\"\n\nLetter from a company:\n\"Dear Mr Aksoy,\nWe would like to offer our sincere apologies for the delay in processing your refund. This was due to an unforeseen technical issue, which has now been resolved. As a gesture of goodwill, we have credited your account with a 20% discount on your next purchase. We trust this will be satisfactory and apologise once again for any inconvenience caused.\nYours sincerely,\nCustomer Relations\"",
     "questions": [
        mc("Why did the colleague miss the meeting?", ["They forgot.", "The train was delayed.", "They were ill."], 1, "\"My train was delayed\""),
        mc("What does the company offer?", ["A full refund", "A 20% discount on the next purchase", "Free delivery"], 1, "\"a 20% discount on your next purchase\""),
     ]},
    {"explanation": "Aynı işlevi farklı üsluplarda ifade etmek:\n\n**Özür dilemek:**\n\n| Samimi | Nötr | Resmî |\n|---|---|---|\n| So sorry! My bad! | I'm really sorry about ... | We would like to offer our sincere apologies for ... |\n| I'm the worst! | Apologies for ... | We apologise for any inconvenience caused. |\n\n**Rica etmek:**\n\n| Samimi | Nötr | Resmî |\n|---|---|---|\n| Can you ...? / Any chance you could ...? | Could you ...? / Would you mind ...? | I would be grateful if you could ... / We would appreciate it if ... |\n| Fill me in? | Could you fill me in on ...? | Could you kindly inform me of ...? |\n\n**Şikâyet etmek:**\n\n| Samimi | Nötr | Resmî |\n|---|---|---|\n| This is a joke! | I'm not very happy with ... | I wish to express my dissatisfaction with ... |\n| It's rubbish. | It isn't working properly. | The product does not meet the standards advertised. |\n\n**Teşekkür etmek:**\n\n| Samimi | Nötr | Resmî |\n|---|---|---|\n| Cheers! / Thanks a million! | Thanks for your help. | I would like to express my gratitude for ... |\n\n**Code-switching:** Çoğu insan gün içinde birçok kez üslup değiştirir: arkadaşa mesaj, yöneticiye e-posta, müşteriye resmî mektup. C1 seviyesinde amaç, bu geçişleri **doğal ve hızlı** yapabilmektir.\n\n**Dikkat:** Aşırı resmî dil de bir **hata** olabilir. Bir arkadaşa *\"I would like to express my gratitude\"* yazmak soğuk, hatta alaycı görünebilir.",
     "examples": [{"en": "Any chance you could lend me your notes?", "tr": "Notlarını bana ödünç verme şansın var mı?"},
                  {"en": "Could you fill me in on what I missed?", "tr": "Kaçırdıklarımı bana anlatabilir misin?"},
                  {"en": "As a gesture of goodwill, we have offered a discount.", "tr": "İyi niyet göstergesi olarak bir indirim sunduk."}],
     "turkishNote": "Türkçede de \"Kusura bakma ya!\" (samimi), \"Özür dilerim\" (nötr) ve \"Yaşanan aksaklıktan dolayı özür dileriz\" (resmî) arasında belirgin farklar vardır. İngilizcede bu fark daha çok kelime seçimi ve cümle uzunluğuyla yapılır. Türk öğrencilerin sık yaptığı bir hata, İngilizce iş e-postalarında aşırı resmî olmaktır (\"I kindly request you to...\"); modern İngilizce iş dünyası nötr ve samimi-profesyonel bir tonu tercih eder."},
    [
        mc("Arkadaşa samimi özür:", ["We would like to offer our sincere apologies.", "So sorry! Totally forgot!"], 1, "Samimi."),
        mc("İş arkadaşına nötr rica:", ["Could you fill me in on what I missed?", "I would be most grateful if you would kindly inform me."], 0, "Nötr."),
        mc("Resmî şikâyet:", ["This is rubbish!", "I wish to express my dissatisfaction with the service."], 1, "Resmî."),
        mc("Arkadaşa aşırı resmî bir mesaj nasıl görünür?", ["Çok kibar ve doğal", "Soğuk, hatta alaycı"], 1, "Uygunsuz üslup."),
        gap("Resmî: \"We apologise for any ___ caused.\" (rahatsızlık)", ["inconvenience"], "inconvenience."),
        gap("Samimi: \"Any ___ you could help me move on Saturday?\" (şans)", ["chance"], "Any chance."),
        gap("Resmî: \"As a gesture of ___, we have refunded your payment.\" (iyi niyet)", ["goodwill"], "gesture of goodwill."),
        gap("Resmî: \"I would like to express my ___ for your help.\" (minnettarlık)", ["gratitude"], "express my gratitude."),
        listen("Dear Ms Polat, thank you for bringing this matter to our attention. We sincerely apologise for the error on your invoice. The amount has now been corrected, and a revised invoice is attached. Please do not hesitate to contact us should you require any further assistance.", "Bu mesajın amacı nedir?", ["Bir ürün tanıtmak", "Fatura hatası için resmî özür dilemek", "Bir toplantı ayarlamak"], 1, "\"We sincerely apologise for the error on your invoice.\""),
        typ("Resmîleştirin: \"Sorry the order is late.\" (We apologise for)", variants("We apologise for the delay in your order.", "We apologise for the late delivery of your order.", "We apologise for the delay to your order.", "We apologise that your order is late.", "We apologise for the delay in delivering your order."), "We apologise for the delay in your order."),
    ],
    {"kind": "speaking", "task": speak("Şu üç durumu üç farklı üslupta canlandırın: (1) Bir arkadaşınızın doğum günü yemeğine gidemediniz; ona sesli mesajla özür dileyin. (2) İş arkadaşınızdan sunum slaytlarınıza göz atmasını rica edin. (3) Bir şirket adına, bir müşteriye ürününün geç teslim edilmesi nedeniyle resmî bir özür ve telafi teklifi sunun.",
                                       "One: Hey, I'm so, so sorry about last night! I totally lost track of time at work, and by the time I left, it was too late. I feel terrible. Let me take you out for dinner next week to make up for it? Two: Hi Can, would you mind having a quick look at my slides before the meeting tomorrow? I'd really appreciate any feedback. Thanks! Three: Dear Mrs Erol, we would like to offer our sincere apologies for the delay in delivering your order. This was due to an unforeseen problem with our supplier. As a gesture of goodwill, we would like to offer you free delivery on your next three orders. We apologise once again for any inconvenience caused.",
                                       ["Üç üslupta net fark", "İşleve uygun kalıplar", "Doğal geçiş", "Uygun ton"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "İki üslupta yazmak", "Aynı içeriği hem samimi bir blog yazısı hem de resmî bir şikâyet / rapor olarak, üslup özelliklerini bilinçli kullanarak yazabilirim.",
    {"kind": "text", "title": "Aynı deneyim, iki metin", "body": "Blog post:\n\"Worst. Hotel. Ever.\nSo, we finally got to Antalya after a nightmare flight, and guess what? Our 'sea view' room had a lovely view of... a car park. The air con was broken, the bathroom was, let's say, not exactly clean, and breakfast was cold toast and some sad-looking eggs. I mean, come on! For what we paid, I was expecting something a bit better. Anyway, we moved to a little guesthouse down the road, and it was brilliant. Lesson learned: always read the reviews!\"\n\nComplaint letter:\n\"Dear Sir or Madam,\nI am writing to express my dissatisfaction with my recent stay at your hotel from 10 to 14 July (booking reference 58412).\nAlthough I had reserved a room with a sea view, the room allocated to us overlooked the car park. Furthermore, the air conditioning was not functioning, and the standard of cleanliness in the bathroom was unacceptable. The breakfast provided also fell considerably below the standard advertised on your website.\nConsequently, we felt obliged to leave the hotel after the first night and to arrange alternative accommodation at our own expense.\nI would therefore be grateful if you could refund the cost of the remaining three nights. I have attached copies of my booking confirmation and photographs of the room.\nI look forward to your prompt reply.\nYours faithfully,\nOya Kaplan\"",
     "questions": [
        mc("What did the room overlook?", ["The sea", "A car park", "A garden"], 1, "\"overlooked the car park\""),
        mc("What does Oya ask for in the letter?", ["An apology only", "A refund for the remaining three nights", "A free stay"], 1, "\"refund the cost of the remaining three nights\""),
     ]},
    {"explanation": "**Aynı içerik, iki üslup: Karşılaştırma**\n\n| Özellik | Blog (samimi) | Şikâyet mektubu (resmî) |\n|---|---|---|\n| **Amaç** | Eğlendirmek, deneyim paylaşmak | Sorunu belgelemek, çözüm istemek |\n| **Başlık / açılış** | *Worst. Hotel. Ever.* | *Dear Sir or Madam, I am writing to ...* |\n| **Kelimeler** | *nightmare, sad-looking, brilliant* | *dissatisfaction, unacceptable, allocated* |\n| **Kısaltmalar** | evet: *I was, it's* | hayır |\n| **Mizah ve ironi** | evet: *a lovely view of... a car park* | hayır |\n| **Doğrudan hitap** | *guess what? come on!* | yok |\n| **Bağlaçlar** | *So, Anyway, I mean* | *Although, Furthermore, Consequently, therefore* |\n| **Kanıt / ayrıntı** | genel | kesin: tarih, rezervasyon numarası, ekler |\n| **Kapanış** | ders / tavsiye | net rica + *I look forward to ...* |\n\n**Üslubu bilinçli değiştirmek için kontrol listesi:**\n\n1. **Okuyucu kim?** (arkadaş, yabancı, kurum)\n2. **Amaç ne?** (eğlendirmek, bilgilendirmek, ikna etmek, çözüm istemek)\n3. **Kelimeler:** phrasal verb mi, Latin kökenli mi?\n4. **Yapı:** kısa ve eksik cümleler mi, uzun ve bağlı cümleler mi?\n5. **Ton:** duygusal mı, nesnel mi?\n\n**Resmî şikâyette bile kibar kalın:** Kızgın olsanız bile *\"unacceptable\"*, *\"I would be grateful if\"* gibi ifadeler, *\"This is a disgrace!\"* gibi ifadelerden çok daha etkilidir.",
     "examples": [{"en": "Blog: The air con was broken, and the bathroom was, let's say, not exactly clean.", "tr": "Blog: Klima bozuktu ve banyo, diyelim ki, pek temiz değildi."},
                  {"en": "Letter: The air conditioning was not functioning, and the standard of cleanliness was unacceptable.", "tr": "Mektup: Klima çalışmıyordu ve temizlik standardı kabul edilemezdi."},
                  {"en": "Letter: Consequently, we felt obliged to arrange alternative accommodation.", "tr": "Mektup: Sonuç olarak başka bir konaklama ayarlamak zorunda hissettik."}],
     "turkishNote": "Türk öğrencilerin İngilizce resmî yazılarında sık görülen bir sorun, Türkçedeki resmî kalıpları (\"arz ederim\", \"bilgilerinize sunarım\") birebir çevirmeye çalışmaktır. İngilizce resmî yazı daha sade ve doğrudandır. Samimi yazıda ise tersine, Türk öğrenciler genellikle fazla resmî kalır. Bu ünitede öğrendiğiniz araçlarla, aynı içeriği iki farklı üslupta yazabilmek C1 seviyesinin en önemli göstergelerinden biridir."},
    [
        mc("Resmî şikâyet mektubunda uygun:", ["Worst. Hotel. Ever.", "I am writing to express my dissatisfaction with ..."], 1, "Resmî."),
        mc("Blogda uygun:", ["Consequently, we felt obliged to leave.", "So we just packed our bags and left!"], 1, "Samimi."),
        mc("Şikâyet mektubunda olması gereken:", ["Tarih ve rezervasyon numarası gibi kesin ayrıntılar", "Mizah ve ironi"], 0, "Kanıt."),
        mc("Kızgın olsanız bile resmî mektupta:", ["This is a disgrace!", "The service was unacceptable."], 1, "Kibar ama kararlı."),
        gap("Resmî: \"The air conditioning was not ___.\" (çalışmak)", ["functioning", "working"], "not functioning."),
        gap("Resmî: \"The room ___ to us overlooked the car park.\" (tahsis edilen)", ["allocated", "given", "assigned"], "allocated."),
        gap("Resmî: \"___, we felt obliged to leave.\" (Sonuç olarak)", ["Consequently", "Therefore", "As a result"], "Consequently."),
        gap("Resmî: \"I look forward to your ___ reply.\" (hızlı)", ["prompt"], "prompt reply."),
        listen("OK, so the restaurant. Honestly? It was a bit of a disaster. We waited, like, an hour for our food, and when it came, it was cold. The waiter was nice, though, I'll give them that. Anyway, I probably won't go back.", "Bu konuşmayı resmî bir şikâyete çevirirseniz hangi bilgiler korunmalı?", ["\"like\" ve \"honestly\"", "Bir saat bekleme ve yemeğin soğuk gelmesi"], 1, "Olgular korunur, dolgu ifadeleri atılır."),
        typ("Resmîleştirin: \"The breakfast was really bad.\" (The breakfast provided ...)", variants("The breakfast provided was of a very poor standard.", "The breakfast provided was unacceptable.", "The breakfast provided was of a poor standard.", "The breakfast provided fell below the expected standard.", "The breakfast provided was very poor."), "The breakfast provided was of a very poor standard."),
    ],
    {"kind": "writing", "task": write("Yaşadığınız (ya da hayal ettiğiniz) kötü bir deneyimi (bir restoran, bir uçuş, bir online alışveriş) iki farklı üslupta yazın. (A) Samimi bir blog yazısı (100–130 kelime): mizah, doğrudan hitap, belirsiz dil ve samimi bağlaçlar kullanın. (B) Aynı deneyim hakkında resmî bir şikâyet e-postası (130–160 kelime): resmî kelimeler, isimleştirme, resmî bağlaçlar, kesin ayrıntılar ve net bir rica kullanın.",
                                      "(A) Blog post: Never ordering a sofa online again!\n\nSo, three months ago, I ordered this gorgeous green sofa online. The website said \"delivered in two weeks\". Two weeks? Ha! It finally turned up after nine weeks, and guess what? It was grey. Not green. Grey. And one of the legs was kind of wobbly. I called customer service about five times, waited ages on hold, and got passed around like a hot potato. Anyway, long story short, I'm still waiting for a refund. Lesson learned: if you want a sofa, go to a real shop, sit on it, and take it home yourself!\n\n(B) Formal email:\n\nSubject: Complaint regarding order no. 77219\n\nDear Sir or Madam,\n\nI am writing to complain about a sofa I ordered from your website on 2 March (order no. 77219).\n\nAlthough the website stated that delivery would take two weeks, the sofa did not arrive until 4 May, nine weeks after the order was placed. Furthermore, the item delivered was grey rather than the green model I had selected, and one of the legs was damaged.\n\nSince then, I have contacted your customer service department on five separate occasions. However, I have not yet received a satisfactory response.\n\nI would therefore be grateful if you could arrange the collection of the sofa and issue a full refund within fourteen days. I have attached photographs of the damage and a copy of my order confirmation.\n\nI look forward to your prompt reply.\n\nYours faithfully,\nSelin Uçar",
                                      ["İki üslup arasında net fark", "Blog: mizah ve samimi dil", "E-posta: resmî kelimeler ve bağlaçlar", "Kesin ayrıntılar ve net rica", "Doğru açılış ve kapanış"])},
)

u.test([
    mc("En resmî:", ["Can't come, sorry!", "I regret that I will be unable to attend."], 1, "Resmî"),
    mc("\"buy\" resmî karşılığı:", ["purchase", "pursue"], 0, "purchase"),
    mc("İsimleştirme:", ["We decided to close the office.", "The decision was taken to close the office."], 1, "Nominalisation"),
    mc("\"We talked about work and stuff.\"", ["İşten ve eşyalardan konuştuk.", "İşten falan konuştuk."], 1, "Belirsiz dil"),
    mc("Resmî bir şikâyette:", ["This is a joke!", "The service did not meet the standards advertised."], 1, "Resmî"),
    gap("Please arrive 15 minutes ___ to the start of the exam. (önce, resmî)", ["prior"], "prior to"),
    gap("Costs were reduced, ___ increasing profits. (böylece)", ["thus"], "thus"),
    gap("The road was closed; ___ the delay. (bu yüzden)", ["hence"], "hence"),
    gap("Resmî: \"We apologise for any ___ caused.\"", ["inconvenience"], "inconvenience"),
    gap("Samimi: \"Let's meet at eight or ___.\" (ya da öyle bir şey)", ["something"], "or something"),
    gap("Resmî: \"Please be ___ that the office will be closed on Friday.\"", ["advised"], "Please be advised"),
    mc("Arkadaşa mesajda aşırı resmî dil:", ["Doğal ve sıcak", "Soğuk, hatta alaycı"], 1, "Uygunsuz üslup"),
    listen("Dear residents, please be advised that, commencing Monday 3 June, the car park will be closed for resurfacing. Alternative parking will be available on Station Road. We apologise for any inconvenience this may cause.", "Bu duyurunun üslubu nedir ve ne bildiriliyor?", ["Samimi; parti duyurusu", "Resmî; otoparkın kapanacağı"], 1, "Resmî duyuru."),
    typ("Resmîleştirin: \"Sorry, but we can't give you your money back.\" (Unfortunately, we are unable ...)", variants("Unfortunately, we are unable to offer you a refund.", "Unfortunately, we are unable to refund your payment.", "Unfortunately, we are unable to provide a refund.", "Unfortunately, we are unable to give you a refund.", "Unfortunately, we are unable to refund you."), "Unfortunately, we are unable to offer you a refund."),
    write("Okulunuzun ya da şirketinizin yeni bir uygulamasını (örneğin esnek çalışma saatleri ya da yeni bir yemekhane) iki farklı üslupta duyurun. (A) Bir arkadaşınıza samimi bir mesaj (60–80 kelime). (B) Tüm çalışanlara / öğrencilere resmî bir duyuru (120–150 kelime): resmî kelimeler, isimleştirme, edilgen yapılar, resmî bağlaçlar ve uygun açılış-kapanış kullanın.",
          "(A) Message to a friend:\n\nHey! Big news at work. Starting next month, we can choose our own hours. Basically, as long as we're in between ten and three, we can come and go whenever we like. No more crazy rush hour for me! I'm thinking of starting at seven and finishing at three, so I can actually go to the gym and stuff. Coffee on Friday to celebrate?\n\n(B) Formal announcement:\n\nDear colleagues,\n\nPlease be advised that, commencing 1 September, the company will be introducing a flexible working hours policy on a six-month trial basis.\n\nUnder the new system, all employees will be required to be present during the core hours of 10:00 to 15:00. Outside these hours, staff will be permitted to determine their own start and finish times, provided that a total of 40 hours per week is completed.\n\nThe introduction of this policy follows a staff survey conducted earlier this year, in which a significant majority of respondents expressed a preference for greater flexibility. It is anticipated that the change will result in improved work-life balance and a reduction in commuting time.\n\nFurther details will be circulated by the Human Resources department in due course. Should you have any questions in the meantime, please do not hesitate to contact your line manager.\n\nKind regards,\nHuman Resources",
          ["İki üslup arasında net fark", "Samimi: doğal ve sıcak", "Resmî: kelime, isimleştirme, edilgen", "Resmî bağlaçlar ve yapı", "Uygun açılış ve kapanış"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

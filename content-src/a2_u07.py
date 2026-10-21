"""A2 Ünite 7: Teknoloji."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("A2", 7, "Teknoloji", "Technology",
         "Teknolojiyi nasıl kullandığımı anlatabilir, yeni yaptığım ya da henüz yapmadığım şeyleri söyleyebilir ve basit teknik sorunları açıklayabilirim.",
         ["present perfect + just", "present perfect + already / yet", "present perfect: şimdiki sonuç (I've lost my phone)", "teknik sorun ifadeleri: It doesn't work / Have you tried ...?"],
         ["cihazlar", "internet ve uygulamalar", "teknik sorunlar"],
         {"title": "Teknik destek hattı", "durationMinutes": 45,
          "goal": "Öğrenciler ikili çalışır: biri bir teknik sorun kartı çeker (Wi-Fi çalışmıyor, ekran dondu, şifre unutuldu), diğeri destek görevlisidir. Görevli 'Have you tried...?' ve 'Have you ... yet?' sorularıyla sorunu çözmeye çalışır. Sonra her ikili, teknolojinin hayatlarını nasıl değiştirdiğini kısaca anlatır."})

u.vocab([
    ("device", "cihaz", "How many devices do you have?", "Kaç cihazın var?", None),
    ("laptop", "dizüstü bilgisayar", "I do all my work on my laptop.", "Bütün işimi laptopumda yapıyorum.", None),
    ("tablet", "tablet", "My kids watch cartoons on the tablet.", "Çocuklarım tablette çizgi film izliyor.", None),
    ("charger", "şarj aleti", "Have you seen my charger?", "Şarj aletimi gördün mü?", None),
    ("charge", "şarj etmek", "I need to charge my phone.", "Telefonumu şarj etmem lazım.", None),
    ("battery", "pil, batarya", "My battery is almost dead.", "Şarjım bitmek üzere.", "The battery is dead = Şarj bitti."),
    ("app", "uygulama", "This app helps me learn English.", "Bu uygulama İngilizce öğrenmeme yardım ediyor.", "application'ın kısası"),
    ("download", "indirmek", "I've just downloaded a new app.", "Az önce yeni bir uygulama indirdim.", None),
    ("upload", "yüklemek", "She uploads videos every week.", "Her hafta video yüklüyor.", None),
    ("install", "kurmak", "Have you installed the update yet?", "Güncellemeyi kurdun mu?", None),
    ("update", "güncelleme; güncellemek", "There's a new update for your phone.", "Telefonun için yeni bir güncelleme var.", None),
    ("log in", "giriş yapmak", "I can't log in to my account.", "Hesabıma giriş yapamıyorum.", "log out = çıkış yapmak"),
    ("password", "şifre", "I've forgotten my password.", "Şifremi unuttum.", None),
    ("account", "hesap", "Create a free account.", "Ücretsiz bir hesap oluşturun.", None),
    ("screen", "ekran", "The screen has frozen.", "Ekran dondu.", None),
    ("freeze", "donmak (ekran)", "My laptop always freezes.", "Laptopum hep donuyor.", "freeze → froze → frozen"),
    ("crash", "çökmek", "The app crashed again.", "Uygulama yine çöktü.", None),
    ("restart", "yeniden başlatmak", "Have you tried restarting it?", "Yeniden başlatmayı denedin mi?", None),
    ("connection", "bağlantı", "The Wi-Fi connection is very slow.", "Wi-Fi bağlantısı çok yavaş.", None),
    ("delete", "silmek", "I've deleted all my old photos.", "Bütün eski fotoğraflarımı sildim.", None),
    ("just", "az önce, yeni", "I've just sent you an email.", "Sana az önce bir e-posta gönderdim.", None),
    ("already", "çoktan, zaten", "I've already paid.", "Zaten ödedim.", None),
    ("yet", "henüz; ... mı (soru)", "Have you replied yet?", "Cevap verdin mi?", "Soru ve olumsuzda, cümle sonunda."),
    ("online", "çevrimiçi", "I do my shopping online.", "Alışverişimi internetten yapıyorum.", None),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Dijital hayatım", "Hangi cihazları ve uygulamaları nasıl kullandığımı anlatabilirim.",
    {"kind": "text", "title": "Anket: Teknoloji ve biz", "body": "We asked 500 people in Turkey about their digital lives.\n\n• 92% use their phone first thing in the morning.\n• Most people spend about four hours a day online.\n• The most popular apps are messaging apps, social media and maps.\n• 65% do their shopping online at least once a month.\n• Only 20% switch off their phone at night.\n\n\"I can't live without my phone,\" says Merve, 22. \"I use it for everything: banking, shopping, music, and learning English!\"",
     "questions": [
        mc("How many people use their phone first thing in the morning?", ["20%", "65%", "92%"], 2, "\"92% use their phone first thing in the morning.\""),
        mc("What does Merve use her phone for?", ["Only music", "Everything", "Only calls"], 1, "\"I use it for everything\""),
     ]},
    {"explanation": "**Teknoloji fiilleri ve kalıplar:**\n\n| Kalıp | Örnek |\n|---|---|\n| download / upload + şey | download an app, upload a photo |\n| install / update | install an app, update the software |\n| log in to / log out of | log in to your account |\n| charge + cihaz | charge my phone |\n| switch on / switch off | switch off your phone (turn on / off da olur) |\n| send / receive | send a message, receive an email |\n| go online / be online | I'm online every evening. |\n\n**Kullanım anlatmak (present simple):**\n\n- I **use** my phone **for** banking. (use ... for + isim / -ing)\n- I **spend** two hours a day **on** social media.\n- I **can't live without** my laptop.",
     "examples": [{"en": "I use my tablet for reading.", "tr": "Tableti okumak için kullanıyorum."},
                  {"en": "I spend too much time on my phone.", "tr": "Telefonda çok fazla vakit geçiriyorum."},
                  {"en": "Switch off your phones, please.", "tr": "Telefonlarınızı kapatın lütfen."}],
     "turkishNote": "Türkçede \"telefonla oynamak\" deriz; İngilizcede \"be on my phone\" ya da \"use my phone\" denir. \"İnternette\" = online ya da on the internet (in the internet değil). \"Uygulama yüklemek\" (telefona) için download ya da install kullanılır; upload ise internete bir şey göndermektir."},
    [
        match([("download", "indirmek"), ("upload", "yüklemek (internete)"), ("log in", "giriş yapmak"), ("charge", "şarj etmek"), ("delete", "silmek")], "Fiilleri eşleştirin."),
        mc("Telefonunuza bir oyun indiriyorsunuz:", ["upload", "download"], 1, "Telefona → download."),
        mc("Instagram'a bir fotoğraf koyuyorsunuz:", ["upload", "download"], 0, "İnternete → upload."),
        gap("I use my phone ___ banking.", ["for"], "use ... for."),
        gap("I spend three hours a day ___ social media.", ["on"], "spend time on."),
        gap("Please switch ___ your phones in the cinema.", ["off"], "switch off = kapatmak."),
        mc("Hangisi doğru?", ["I'm in the internet.", "I'm online."], 1, "online / on the internet."),
        listen("I don't watch TV anymore. I use my laptop for films and my phone for music. I can't live without them!", "Konuşan film izlemek için ne kullanıyor?", ["Televizyon", "Laptop", "Telefon"], 1, "\"I use my laptop for films\""),
        order(["can't", "I", "live", "without", "my", "phone"], "I can't live without my phone.", "can't live without + isim.", "Telefonum olmadan yaşayamam."),
        typ("İngilizce yazın: \"Hesabıma giriş yapamıyorum.\"", variants("I can't log in to my account.", "I can't log into my account.", "I cannot log in to my account.", "I can't sign in to my account."), "I can't + log in to + my account."),
    ],
    {"kind": "speaking", "task": speak("Dijital hayatınızı anlatın: hangi cihazları kullanıyorsunuz, ne için kullanıyorsunuz, günde ne kadar vakit geçiriyorsunuz, en sevdiğiniz uygulama hangisi ve neden?",
                                       "I have a phone and a laptop. I use my laptop for work and my phone for everything else. I spend about three hours a day on my phone. My favourite app is a map app because I travel a lot.",
                                       ["Teknoloji kelimeleri", "use ... for / spend ... on doğru", "Present simple doğru"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "Az önce yaptım", "Present perfect ve just ile çok yakın zamanda olan şeyleri söyleyebilirim.",
    {"kind": "dialogue", "title": "Ofiste", "lines": [
        {"speaker": "Manager", "text": "Kerem, have you got the report?"},
        {"speaker": "Kerem", "text": "Yes, I've just finished it. I've just sent it to you by email."},
        {"speaker": "Manager", "text": "Great. Oh, and the client has just called. She wants a meeting tomorrow."},
        {"speaker": "Kerem", "text": "No problem. I've just checked my diary. I'm free at ten."},
        {"speaker": "Manager", "text": "Perfect."}],
     "questions": [
        mc("What has Kerem just done?", ["He's called the client.", "He's sent the report.", "He's had a meeting."], 1, "\"I've just sent it to you by email.\""),
        mc("Who has just called?", ["Kerem", "The client", "The manager's boss"], 1, "\"the client has just called\""),
     ]},
    {"explanation": "**just** + present perfect → **az önce, yeni** olmuş bir şey.\n\n**Yapı:** have / has + **just** + V3\n\n- I**'ve just sent** you a message.\n- She**'s just left**.\n- The film **has just started**.\n\njust, **have/has ile V3 arasına** gelir.\n\nSonuç genellikle şu anda önemlidir: I've just eaten. (Şimdi aç değilim.)\n\n**Teknoloji fiillerinin V3'leri:**\n\n| V1 | V3 |\n|---|---|\n| send | **sent** |\n| buy | **bought** |\n| forget | **forgotten** |\n| download | download**ed** |\n| leave | **left** |",
     "examples": [{"en": "I've just bought a new phone.", "tr": "Yeni bir telefon aldım (az önce)."},
                  {"en": "The battery has just died.", "tr": "Şarj az önce bitti."},
                  {"en": "We've just arrived at the hotel.", "tr": "Otele yeni vardık."}],
     "turkishNote": "Türkçede \"az önce\" ya da \"yeni\" kelimesini fiilden önce koyarız: yeni geldim. İngilizcede just have/has ile V3 arasına girer: I've just arrived (I just have arrived değil). Amerikan İngilizcesinde \"I just arrived\" (past simple) da yaygındır."},
    [
        mc("Hangisi doğru?", ["I just have arrived.", "I've just arrived.", "I've arrived just."], 1, "have + just + V3."),
        gap("She's ___ left. You can call her later. (az önce)", ["just"], "just."),
        gap("I've just ___ you an email. (send)", ["sent"], "send → sent."),
        gap("The film has just ___. Sit down! (start)", ["started"], "start → started."),
        gap("We've just ___ a new TV. (buy)", ["bought"], "buy → bought."),
        mc("\"I've just eaten.\" Anlamı:", ["Şimdi aç değilim.", "Yemek yemeyi planlıyorum.", "Hiç yemedim."], 0, "Az önce yedim → şu an tokum."),
        order(["just", "I've", "downloaded", "a", "new", "app"], "I've just downloaded a new app.", "have + just + V3 + nesne.", "Az önce yeni bir uygulama indirdim."),
        listen("Oh no! My laptop has just crashed and I haven't saved my work.", "Ne oldu?", ["Laptop yeni çöktü", "Laptop çalındı", "İşini kaydetti"], 0, "\"My laptop has just crashed\""),
        typ("İngilizce yazın: \"Şarjım az önce bitti.\"", variants("My battery has just died.", "My phone has just died.", "The battery has just died.", "My battery's just died."), "My battery + has just died."),
        match([("I've just woken up.", "Hâlâ uykulu."), ("I've just eaten.", "Aç değil."), ("She's just left.", "Burada değil."), ("It's just started.", "Başında.")], "Cümleleri sonuçlarıyla eşleştirin."),
    ],
    {"kind": "speaking", "task": speak("JAI ile ofis arkadaşı rolündesiniz. JAI size işleri soracak. Az önce yaptığınız 4 şeyi just ile söyleyin.",
                                       "I've just finished the presentation. I've just sent the email to the client. I've just had a coffee. And I've just booked the meeting room for tomorrow.",
                                       ["have + just + V3 doğru", "Düzensiz V3'ler doğru", "Doğal tonlama"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "Zaten mi, henüz mi?", "already ve yet ile tamamlanan ve henüz tamamlanmayan işleri anlatabilirim.",
    {"kind": "dialogue", "title": "Taşınma hazırlığı", "lines": [
        {"speaker": "Burcu", "text": "Have you set up the internet at the new flat yet?"},
        {"speaker": "Tarık", "text": "Yes, I've already called the company. They're coming tomorrow."},
        {"speaker": "Burcu", "text": "And have you changed our address on the bank app yet?"},
        {"speaker": "Tarık", "text": "Not yet. I haven't had time. Have you packed the computer yet?"},
        {"speaker": "Burcu", "text": "Yes, I've already packed it. And I've already backed up all our photos."},
        {"speaker": "Tarık", "text": "Great! You're so organised."}],
     "questions": [
        mc("Has Tarık changed the address on the bank app?", ["Yes, already.", "Not yet."], 1, "\"Not yet. I haven't had time.\""),
        mc("What has Burcu already done?", ["Called the company", "Packed the computer and backed up photos", "Changed the address"], 1, "\"I've already packed it. And I've already backed up all our photos.\""),
     ]},
    {"explanation": "**already** → zaten, çoktan (beklenenden önce yapıldı)\n\n- Olumlu cümlede, **have/has ile V3 arasına**: I**'ve already paid**.\n\n**yet** → henüz (olumsuz), ... mı? (soru)\n\n- Olumsuz ve soruda, **cümle sonunda**:\n- I **haven't** finished **yet**. (Henüz bitirmedim.)\n- **Have** you finished **yet**? (Bitirdin mi?)\n\n**Kısa cevaplar:** Not yet. (Henüz değil.) / Yes, I've already done it.\n\n| | Konum | Cümle türü |\n|---|---|---|\n| just | have + **just** + V3 | olumlu |\n| already | have + **already** + V3 | olumlu |\n| yet | ... **yet**. | olumsuz / soru |",
     "examples": [{"en": "I've already seen this video.", "tr": "Bu videoyu zaten izledim."},
                  {"en": "Has the package arrived yet?", "tr": "Paket geldi mi?"},
                  {"en": "I haven't installed the update yet.", "tr": "Güncellemeyi henüz kurmadım."}],
     "turkishNote": "\"Have you eaten yet?\" Türkçede \"Yemek yedin mi?\" gibidir; yet burada \"henüz\" diye çevrilmez ama sorunun beklenti içerdiğini gösterir. \"Daha yemedim\" = I haven't eaten yet. already olumsuz cümlede kullanılmaz: \"I haven't already\" yanlıştır."},
    [
        mc("Hangisi doğru?", ["I've already paid.", "I've paid already yet.", "I already have paid yet."], 0, "have + already + V3."),
        mc("Hangisi doğru?", ["Have you yet finished?", "Have you finished yet?"], 1, "yet cümle sonunda."),
        mc("Hangisi doğru?", ["I haven't already done it.", "I haven't done it yet."], 1, "Olumsuzda yet."),
        gap("Don't buy a ticket. I've ___ bought one for you. (zaten)", ["already"], "already."),
        gap("Has the package arrived ___?", ["yet"], "Soruda yet."),
        gap("I haven't replied to his email ___. (henüz)", ["yet"], "Olumsuzda yet."),
        mc("\"Have you installed the update?\" (Henüz değil.)", ["Not yet.", "Already not.", "Yet no."], 0, "Not yet."),
        order(["haven't", "I", "backed", "up", "my", "photos", "yet"], "I haven't backed up my photos yet.", "haven't + V3 + nesne + yet.", "Fotoğraflarımı henüz yedeklemedim."),
        listen("Have you charged the camera yet? – Yes, I've already charged it, and I've already packed the extra batteries.", "Kamera şarj edildi mi?", ["Evet, zaten edildi", "Henüz değil", "Pil yok"], 0, "\"I've already charged it\""),
        typ("İngilizce yazın: \"Bu videoyu zaten izledim.\"", variants("I've already seen this video.", "I have already seen this video.", "I've already watched this video.", "I have already watched this video."), "I've already + seen + this video."),
    ],
    {"kind": "writing", "task": write("Yarın tatile çıkıyorsunuz. Bir yapılacaklar listesi düşünün ve arkadaşınıza mesaj yazın: zaten yaptığınız 3 şey (already), henüz yapmadığınız 2 şey (yet) ve ona 1 soru (yet).",
                                      "Hi! I've already packed my suitcase and I've already printed our tickets. I've already charged my phone and my camera. But I haven't booked the taxi yet, and I haven't bought sun cream yet. Have you checked the weather yet?",
                                      ["already doğru konumda", "yet olumsuz ve soruda", "V3'ler doğru"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Şimdiki sonuç", "Geçmişte olan bir şeyin şu anki sonucunu present perfect ile anlatabilirim.",
    {"kind": "dialogue", "title": "Kayıp telefon", "lines": [
        {"speaker": "Eda", "text": "Help! I've lost my phone!"},
        {"speaker": "Mehmet", "text": "Oh no. When did you last see it?"},
        {"speaker": "Eda", "text": "I used it on the bus this morning. Maybe I left it there."},
        {"speaker": "Mehmet", "text": "Have you called it?"},
        {"speaker": "Eda", "text": "Yes, but nobody answered. And someone has changed my password! I can't log in to my account."},
        {"speaker": "Mehmet", "text": "OK, let's call the bus company and your bank right now."}],
     "questions": [
        mc("Where does Eda think her phone is?", ["At home", "On the bus", "At the bank"], 1, "\"Maybe I left it there.\" (on the bus)"),
        mc("Why can't Eda log in?", ["She's forgotten her password.", "Someone has changed her password.", "The internet is down."], 1, "\"someone has changed my password!\""),
     ]},
    {"explanation": "Present perfect, geçmişteki bir olayın **şu anki sonucunu** vurgular. Zaman söylenmez.\n\n| Present perfect (sonuç şimdi) | Anlamı |\n|---|---|\n| I**'ve lost** my phone. | Şu an telefonum yok. |\n| He**'s broken** his arm. | Kolu şu an kırık. |\n| The price **has gone up**. | Şu an daha pahalı. |\n\nAyrıntıya geçince **past simple**:\n\n- I**'ve lost** my phone. I **left** it on the bus **this morning**.\n\n**Haber verirken** de present perfect kullanılır:\n\n- **Have** you **heard**? Apple **has released** a new phone!\n- A new café **has opened** near my house.",
     "examples": [{"en": "I've forgotten my password. Can you help me?", "tr": "Şifremi unuttum. Bana yardım edebilir misin?"},
                  {"en": "Someone has taken my charger!", "tr": "Biri şarj aletimi almış!"},
                  {"en": "Have you heard? They've opened a new shopping centre.", "tr": "Duydun mu? Yeni bir AVM açmışlar."}],
     "turkishNote": "Türkçedeki \"-miş\" eki (almışlar, açmışlar) çoğu zaman present perfect'e denk gelir, çünkü sonuca bakarak konuşuruz. \"Şifremi unuttum\" İngilizcede \"I've forgotten my password\" olur, çünkü şu an hâlâ hatırlamıyoruz."},
    [
        mc("Şu an anahtarınız yok:", ["I lost my keys.", "I've lost my keys."], 1, "Şimdiki sonuç → present perfect."),
        mc("Ayrıntı: \"Dün akşam kaybettim.\"", ["I've lost them last night.", "I lost them last night."], 1, "last night → past simple."),
        gap("I've ___ my password. (forget)", ["forgotten"], "forget → forgotten."),
        gap("Someone has ___ my bike! (steal)", ["stolen"], "steal → stolen."),
        gap("Have you ___? Our team won! (hear)", ["heard"], "hear → heard."),
        gap("The price of phones ___ gone up again.", ["has", "'s"], "price → has."),
        mc("Haber vermek: \"Yeni bir kafe açılmış.\"", ["A new café has opened.", "A new café opens."], 0, "Haber → present perfect."),
        listen("I can't send any messages. I think I've used all my mobile data this month.", "Konuşan neden mesaj gönderemiyor?", ["Telefon bozuldu", "Bu ayki internet paketi bitti", "Şifreyi unuttu"], 1, "\"I've used all my mobile data this month\""),
        order(["broken", "has", "My", "son", "his", "tablet", "screen"], "My son has broken his tablet screen.", "Özne + has + V3 + nesne.", "Oğlum tabletinin ekranını kırmış."),
        typ("İngilizce yazın: \"Biri şarj aletimi almış!\"", variants("Someone has taken my charger!", "Somebody has taken my charger!", "Someone's taken my charger!", "Someone has taken my charger."), "Someone + has taken + my charger!"),
    ],
    {"kind": "speaking", "task": speak("JAI arkadaşınız. Ona kötü bir teknoloji haberinizi present perfect ile verin (bir şey kaybettiniz / kırdınız / unuttunuz). JAI sorular sorduğunda ayrıntıları past simple ile anlatın.",
                                       "I've broken my phone! I dropped it on the stairs this morning. The screen is completely black. I've already called the shop, but they can't fix it until Friday.",
                                       ["Haber present perfect ile", "Ayrıntılar past simple ile", "Teknoloji kelimeleri"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Teknik destek", "Bir teknik sorunu anlatabilir ve çözüm önerilerini anlayıp sunabilirim.",
    {"kind": "dialogue", "title": "Destek hattı", "lines": [
        {"speaker": "Agent", "text": "Hello, TechHelp. How can I help?"},
        {"speaker": "Ali", "text": "Hi. My internet doesn't work. The Wi-Fi light is red."},
        {"speaker": "Agent", "text": "OK. Have you tried restarting the modem?"},
        {"speaker": "Ali", "text": "Yes, I've already restarted it twice."},
        {"speaker": "Agent", "text": "Have you checked the cables?"},
        {"speaker": "Ali", "text": "Not yet. Hold on... Oh! The cable has come out. ... It's working now!"},
        {"speaker": "Agent", "text": "Great. Is there anything else I can help you with?"}],
     "questions": [
        mc("What was the problem?", ["The modem was broken.", "A cable came out.", "Ali forgot the password."], 1, "\"The cable has come out.\""),
        mc("How many times has Ali restarted the modem?", ["Once", "Twice", "Never"], 1, "\"I've already restarted it twice.\""),
     ]},
    {"explanation": "**Sorunu anlatmak:**\n\n- My laptop **doesn't work** / **isn't working**.\n- The screen **has frozen**. / The app **keeps crashing**.\n- I **can't** connect to the Wi-Fi / log in / open the file.\n- There's **something wrong with** my phone.\n\n**Çözüm önermek:**\n\n- **Have you tried** + -ing? → Have you tried restarting it?\n- **Try** + -ing → Try turning it off and on again.\n- You should update the app.\n\n**Kontrol soruları:**\n\n- Have you checked the cables / your password **yet**?\n- **Is it plugged in?** (Fişe takılı mı?)\n\n**Teşekkür ve kapanış:** It's working now. Thanks for your help! / Is there anything else I can help you with?",
     "examples": [{"en": "There's something wrong with my laptop.", "tr": "Laptopumda bir sorun var."},
                  {"en": "Have you tried turning it off and on again?", "tr": "Kapatıp açmayı denedin mi?"},
                  {"en": "The app keeps crashing.", "tr": "Uygulama sürekli çöküyor."}],
     "turkishNote": "\"Çalışmıyor\" İngilizcede \"doesn't work\" (genel) ya da \"isn't working\" (şu an) olabilir; ikisi de doğaldır. \"Have you tried...?\" sonrası fiil -ing alır: Have you tried restarting (Have you tried restart değil). \"keep + -ing\" = sürekli ... -mek."},
    [
        mc("Hangisi doğru?", ["Have you tried restart it?", "Have you tried restarting it?"], 1, "tried + -ing."),
        mc("\"Uygulama sürekli çöküyor.\"", ["The app keeps crashing.", "The app keeps crash.", "The app is keep crashing."], 0, "keep + -ing."),
        gap("There's something wrong ___ my phone.", ["with"], "something wrong with."),
        gap("I ___ connect to the Wi-Fi. (bağlanamıyorum)", ["can't", "cannot"], "can't + fiil."),
        gap("The screen has ___. I can't do anything. (freeze)", ["frozen"], "freeze → frozen."),
        gap("Try ___ it off and on again. (turn)", ["turning"], "Try + -ing."),
        order(["you", "Have", "checked", "the", "cables", "yet", "?"], "Have you checked the cables yet?", "Have you + V3 + nesne + yet?", "Kabloları kontrol ettin mi?"),
        listen("My laptop isn't working. I've tried restarting it, and I've checked the battery. But the screen is still black.", "Konuşan ne denedi?", ["Sadece pili", "Yeniden başlatmayı ve pili kontrol etmeyi", "Hiçbir şey"], 1, "\"I've tried restarting it, and I've checked the battery\""),
        typ("İngilizce yazın: \"Kapatıp açmayı denedin mi?\"", variants("Have you tried turning it off and on again?", "Have you tried turning it off and on?", "Have you tried switching it off and on again?", "Have you tried turning it off and back on again?"), "Have you tried + turning it off and on again?"),
        match([("The screen", "has frozen."), ("The app", "keeps crashing."), ("Is it", "plugged in?"), ("It's working", "now. Thanks!")], "Cümleleri tamamlayın."),
    ],
    {"kind": "speaking", "task": speak("JAI teknik destek görevlisi. Bir sorununuzu anlatın (yazıcı çalışmıyor, uygulama açılmıyor...). JAI'nin önerilerine already / not yet ile cevap verin ve sorun çözülünce teşekkür edin.",
                                       "Hi, my printer isn't working. ... Yes, I've already restarted it. ... No, I haven't checked the cable yet. Hold on. ... Oh, it wasn't plugged in! It's working now. Thanks for your help!",
                                       ["Sorunu net anlattı", "already / yet doğru", "Have you tried...? sorularını anladı", "Kibar kapanış"])},
)

u.test([
    mc("Telefona oyun indirmek:", ["upload", "download"], 1, "download"),
    gap("I spend two hours a day ___ social media.", ["on"], "spend ... on"),
    mc("Hangisi doğru?", ["I just have sent it.", "I've just sent it."], 1, "have + just + V3"),
    gap("She's just ___. You missed her. (leave)", ["left"], "leave → left"),
    mc("Hangisi doğru?", ["I've already paid.", "I've paid already yet."], 0, "already"),
    mc("Hangisi doğru?", ["Have you yet replied?", "Have you replied yet?"], 1, "yet sonda"),
    gap("I haven't installed the update ___.", ["yet"], "yet"),
    mc("\"Have you finished?\" (Henüz değil.)", ["Not yet.", "Yet not."], 0, "Not yet."),
    gap("I've ___ my password. (forget)", ["forgotten"], "forget → forgotten"),
    mc("Hangisi doğru?", ["I've lost my phone yesterday.", "I lost my phone yesterday."], 1, "yesterday → past simple"),
    mc("Hangisi doğru?", ["Have you tried restart it?", "Have you tried restarting it?"], 1, "tried + -ing"),
    gap("The app keeps ___. (crash)", ["crashing"], "keep + -ing"),
    listen("Have you heard? The new metro line has just opened. It goes from the airport to the city centre.", "Ne haber veriliyor?", ["Yeni havalimanı açıldı", "Yeni metro hattı açıldı", "Metro kapandı"], 1, "\"The new metro line has just opened.\""),
    typ("İngilizce yazın: \"Laptopumda bir sorun var.\"", variants("There's something wrong with my laptop.", "There is something wrong with my laptop.", "Something is wrong with my laptop.", "Something's wrong with my laptop."), "There's something wrong with + my laptop."),
    write("Bir teknik destek ekibine e-posta yazın (60–80 kelime): sorunu anlatın, zaten denediğiniz şeyleri (already) ve henüz yapmadığınızı (yet) söyleyin ve yardım isteyin.",
          "Dear TechHelp,\nI have a problem with my new laptop. The screen keeps freezing and the camera doesn't work. I've already restarted it many times and I've already installed the latest update. I haven't tried deleting any apps yet because I'm not sure which ones are important. Can you help me, please?\nBest wishes,\nSeda Arslan",
          ["Sorun net anlatıldı", "already / yet doğru", "Present perfect doğru", "Kibar e-posta yapısı"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

"""B2 Ünite 2: Kariyer."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("B2", 2, "Kariyer", "Careers",
         "Kariyer hedeflerimi ve gelecekteki belirli bir anda ne yapıyor olacağımı ya da neyi tamamlamış olacağımı future continuous ve future perfect ile anlatabilir, iş görüşmesinde kendimi ifade edebilir ve etkili bir ön yazı (cover letter) yazabilirim.",
         ["future continuous (will be doing)", "future continuous ile kibar sorular", "future perfect (will have done)", "future perfect continuous", "gelecek zaman yapılarının karşılaştırılması"],
         ["kariyer ve iş hayatı", "iş başvurusu ve mülakat", "beceriler ve nitelikler"],
         {"title": "Beş yıl sonra", "durationMinutes": 45,
          "goal": "Öğrenciler ikili olarak iş görüşmesi canlandırır: biri işveren, biri aday. Aday \"Where do you see yourself in five years?\" sorusuna future continuous ve future perfect ile cevap verir (In five years, I'll be leading a team... By then, I'll have completed...). Sonra roller değişir. Son bölümde her öğrenci 10 yıl sonraki kariyerini bir dakikada sunar."})

u.vocab([
    ("career path", "kariyer yolu", "She's not sure which career path to choose.", "Hangi kariyer yolunu seçeceğinden emin değil.", None),
    ("apply for", "başvurmak", "I'm applying for a job in marketing.", "Pazarlamada bir işe başvuruyorum.", "application (başvuru)"),
    ("CV", "özgeçmiş", "Send your CV to the HR department.", "Özgeçmişinizi İK departmanına gönderin.", "ABD'de résumé"),
    ("cover letter", "ön yazı", "A good cover letter can make a difference.", "İyi bir ön yazı fark yaratabilir.", None),
    ("candidate", "aday", "There were 200 candidates for the job.", "İş için 200 aday vardı.", None),
    ("shortlist", "kısa listeye almak", "You've been shortlisted for an interview.", "Mülakat için kısa listeye alındınız.", None),
    ("qualifications", "nitelikler, diplomalar", "What qualifications do you need?", "Hangi niteliklere ihtiyacın var?", None),
    ("experience", "deneyim", "She has five years' experience in sales.", "Satışta beş yıllık deneyimi var.", "Sayılamaz"),
    ("skills", "beceriler", "Communication skills are essential.", "İletişim becerileri şarttır.", None),
    ("strength", "güçlü yön", "What's your greatest strength?", "En büyük güçlü yönün ne?", None),
    ("weakness", "zayıf yön", "Talk about a weakness and how you deal with it.", "Bir zayıf yönünüzden ve onunla nasıl başa çıktığınızdan bahsedin.", None),
    ("promotion", "terfi", "He's hoping for a promotion this year.", "Bu yıl terfi bekliyor.", "get promoted"),
    ("salary", "maaş", "The salary is negotiable.", "Maaş pazarlığa açık.", None),
    ("full-time / part-time", "tam zamanlı / yarı zamanlı", "Is it a full-time position?", "Tam zamanlı bir pozisyon mu?", None),
    ("freelance", "serbest çalışan", "She works freelance as a translator.", "Serbest çevirmen olarak çalışıyor.", None),
    ("internship", "staj", "I did a six-month internship at a bank.", "Bir bankada altı aylık staj yaptım.", None),
    ("deadline", "son tarih", "The deadline for applications is Friday.", "Başvuruların son tarihi cuma.", None),
    ("in charge of", "-den sorumlu", "I'm in charge of a team of ten.", "On kişilik bir ekipten sorumluyum.", None),
    ("career ladder", "kariyer basamakları", "He climbed the career ladder quickly.", "Kariyer basamaklarını hızla tırmandı.", None),
    ("work-life balance", "iş-özel hayat dengesi", "Work-life balance is important to me.", "İş-özel hayat dengesi benim için önemli.", None),
    ("resign", "istifa etmek", "She resigned after ten years.", "On yıl sonra istifa etti.", "resignation (istifa)"),
    ("by then", "o zamana kadar", "By then, I'll have finished my degree.", "O zamana kadar diplomamı almış olacağım.", None),
    ("this time next year", "seneye bu zaman", "This time next year, I'll be working in Berlin.", "Seneye bu zaman Berlin'de çalışıyor olacağım.", None),
    ("in the long run", "uzun vadede", "In the long run, it's a good investment.", "Uzun vadede iyi bir yatırım.", None),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Seneye bu zaman", "Gelecekte belirli bir anda devam ediyor olacak eylemleri future continuous ile anlatabilirim.",
    {"kind": "dialogue", "title": "Mezuniyet sonrası", "lines": [
        {"speaker": "Aras", "text": "I can't believe we're graduating next week! What are your plans?"},
        {"speaker": "Beren", "text": "I've got a job at an engineering firm in Munich. This time next month, I'll be learning German in an intensive course."},
        {"speaker": "Aras", "text": "That's amazing! I'll be doing something completely different. I'll be travelling around South America for six months."},
        {"speaker": "Beren", "text": "Lucky you! While you're lying on a beach, I'll be sitting in an office."},
        {"speaker": "Aras", "text": "Ha! But I'll be working too. I'm volunteering at a school in Peru."},
        {"speaker": "Beren", "text": "Wow. Well, don't forget me. I'll be thinking of you!"}],
     "questions": [
        mc("What will Beren be doing this time next month?", ["Travelling", "Learning German", "Volunteering"], 1, "\"I'll be learning German in an intensive course\""),
        mc("Where will Aras be working?", ["In Munich", "At a school in Peru", "In an office"], 1, "\"I'm volunteering at a school in Peru\""),
     ]},
    {"explanation": "**Future continuous:** will be + fiil-**ing**\n\nGelecekte **belirli bir anda devam ediyor olacak** bir eylemi anlatır (\"-iyor olacağım\").\n\n| | Yapı | Örnek |\n|---|---|---|\n| Olumlu | will be + -ing | This time next year, I**'ll be working** in Munich. |\n| Olumsuz | won't be + -ing | I **won't be using** the car tomorrow. |\n| Soru | Will + özne + be + -ing? | **Will** you **be working** late tonight? |\n\n**Zaman çizgisi:**\n\n```\n  şimdi ─────────────── [....working....]\n                        ↑ this time next year\n```\n\n**Sık kullanılan zaman ifadeleri:**\n\n- **This time next week / month / year**\n- **At 10 o'clock tomorrow**\n- **In five years' time**\n- **While** you're relaxing, I'll be working.\n\n**Karşılaştırın:**\n\n- At 9 am tomorrow, I**'ll start** work. (O anda başlayacağım.)\n- At 9 am tomorrow, I**'ll be working**. (O sırada çalışıyor olacağım.)",
     "examples": [{"en": "Don't call me at eight. I'll be having dinner.", "tr": "Sekizde arama. Akşam yemeği yiyor olacağım."},
                  {"en": "In ten years' time, we'll be living by the sea.", "tr": "On yıl sonra deniz kenarında yaşıyor olacağız."},
                  {"en": "This time tomorrow, I'll be flying to Tokyo.", "tr": "Yarın bu saatte Tokyo'ya uçuyor olacağım."}],
     "turkishNote": "Türkçedeki \"-iyor olacağım\" (çalışıyor olacağım, uçuyor olacağım) yapısı future continuous'a birebir denk gelir. Türkçe konuşanlar bu yapıyı kolay anlar, ama konuşurken genellikle basit \"will\" ile yetinir. Gelecekteki belirli bir anda süren bir eylemden bahsederken will be + -ing kullanmak anlatımınızı daha doğal yapar."},
    [
        mc("Yarın saat 10'da toplantıda olacaksınız:", ["At 10 tomorrow, I'll have a meeting.", "At 10 tomorrow, I'll be having a meeting."], 1, "O anda süren → will be + -ing."),
        mc("Hangisi doğru?", ["I'll be work late tonight.", "I'll be working late tonight."], 1, "will be + -ing."),
        mc("This time next year, she ___ at university.", ["will study", "will be studying"], 1, "Belirli bir anda süren."),
        gap("Don't call me at seven. I ___ (drive) home.", ["'ll be driving", "will be driving"], "will be + -ing."),
        gap("In five years' ___, I'll be running my own company.", ["time"], "In five years' time."),
        gap("I ___ (not / use) my laptop tomorrow, so you can borrow it.", ["won't be using", "will not be using"], "Olumsuz."),
        gap("While you're relaxing on the beach, I'll be ___ (sit) in a meeting.", ["sitting"], "will be + -ing."),
        order(["be", "This", "time", "tomorrow", "I'll", "flying", "to", "Rome"], "This time tomorrow I'll be flying to Rome.", "Zaman ifadesi + will be + -ing.", "Yarın bu saatte Roma'ya uçuyor olacağım."),
        listen("Next September, I'll be starting a new job in Izmir. So this time next year, I'll probably be living by the sea and cycling to work every day.", "Konuşan gelecek yıl bu zaman ne yapıyor olacak?", ["İstanbul'da okuyor olacak", "Deniz kenarında yaşıyor ve işe bisikletle gidiyor olacak", "Yurt dışında seyahat ediyor olacak"], 1, "\"I'll probably be living by the sea and cycling to work\""),
        typ("İngilizce yazın: \"On yıl sonra deniz kenarında yaşıyor olacağız.\"", variants("In ten years' time, we'll be living by the sea.", "In ten years, we'll be living by the sea.", "In ten years' time, we will be living by the sea.", "In ten years, we will be living by the sea.", "We'll be living by the sea in ten years.", "We'll be living by the sea in ten years' time.", "In ten years we'll be living by the sea."), "In ten years' time, we'll be living by the sea."),
    ],
    {"kind": "speaking", "task": speak("JAI size zaman ifadeleri verecek (tomorrow at 9 am, this time next week, this time next year, in five years' time, when you're 60). Her biri için o anda ne yapıyor olacağınızı future continuous ile söyleyin ve bir ayrıntı ekleyin.",
                                       "Tomorrow at 9 am, I'll be sitting in my office and checking my emails. This time next week, I'll be visiting my parents in Eskişehir. This time next year, I'll be studying for a master's degree. In five years' time, I'll be working as a project manager. When I'm 60, I'll be living in a small house with a big garden.",
                                       ["will be + -ing doğru", "Zaman ifadeleri", "Ayrıntılı ve doğal"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "Kullanıyor olacak mısın?", "Future continuous ile kibarca plan sorabilir ve zaten planlanmış, sıradan gelecek olaylardan bahsedebilirim.",
    {"kind": "dialogue", "title": "Ofiste", "lines": [
        {"speaker": "Ece", "text": "Will you be using the meeting room this afternoon? I need it for an interview."},
        {"speaker": "Tolga", "text": "No, I won't be needing it. I'll be visiting a client in Kadıköy."},
        {"speaker": "Ece", "text": "Great, thanks. Oh, and will you be coming to Sinan's leaving party on Friday?"},
        {"speaker": "Tolga", "text": "Of course. I'll be seeing him tomorrow anyway, so I'll ask him what he wants as a present."},
        {"speaker": "Ece", "text": "Perfect. And will you be going past the post office? I need to send this contract."},
        {"speaker": "Tolga", "text": "Yes, I'll be passing it on my way. Give it to me."}],
     "questions": [
        mc("Why doesn't Tolga need the meeting room?", ["He's on holiday.", "He'll be visiting a client.", "He's in another meeting."], 1, "\"I'll be visiting a client in Kadıköy\""),
        mc("What will Tolga do for Ece?", ["Book the room", "Send her contract at the post office", "Buy Sinan's present"], 1, "\"I'll be passing it on my way. Give it to me.\""),
     ]},
    {"explanation": "Future continuous'ın iki önemli kullanımı daha vardır:\n\n**1. Kibar sorular (birinin planlarını sormak)**\n\n| Doğrudan (istek gibi) | Kibar (plan sorma) |\n|---|---|\n| **Will you use** the car tonight? | **Will you be using** the car tonight? |\n| **Are you coming** to the party? | **Will you be coming** to the party? |\n\nFuture continuous ile sorduğunuzda karşı tarafa bir şey **istediğinizi** değil, sadece **planlarını** sorduğunuzu belli edersiniz. Bu, bir şey isteme öncesi kibar bir girizgâhtır.\n\n**2. Normal akışında olacak olaylar**\n\nBir şey özel bir karar sonucu değil, **olayların doğal akışında** olacaksa:\n\n- I**'ll be seeing** him tomorrow anyway. (Zaten görüşeceğiz, ayrıca karar vermedim.)\n- I**'ll be passing** the post office on my way.\n- The plane **will be landing** in ten minutes. (Duyurularda sık kullanılır.)\n\n**Karşılaştırın:**\n\n- I**'ll call** him. (Şimdi karar verdim → anlık karar)\n- I**'ll be calling** him later anyway. (Zaten arayacaktım)",
     "examples": [{"en": "Will you be needing anything else, sir?", "tr": "Başka bir şeye ihtiyacınız olacak mı efendim?"},
                  {"en": "We'll be landing in Istanbul in approximately twenty minutes.", "tr": "Yaklaşık yirmi dakika içinde İstanbul'a iniyor olacağız."},
                  {"en": "I'll be going to the supermarket later. Do you need anything?", "tr": "Sonra süpermarkete gideceğim. Bir şeye ihtiyacın var mı?"}],
     "turkishNote": "Türkçede kibarlık genellikle \"-abilir misiniz\" ya da \"rica etsem\" ile yapılır. İngilizcede future continuous ile soru sormak, karşı tarafa baskı yapmadan plan sormanın çok doğal ve kibar bir yoludur: \"Will you be using the car?\" cümlesi \"Arabayı kullanacak mısın? (Kullanmayacaksan ben alabilir miyim?)\" anlamını taşır."},
    [
        mc("Daha kibar:", ["Will you use the printer?", "Will you be using the printer?"], 1, "Plan sorma → future continuous."),
        mc("Zaten olacak bir şey:", ["I'll see her tomorrow anyway.", "I'll be seeing her tomorrow anyway."], 1, "Normal akış → future continuous."),
        mc("Anlık karar:", ["OK, I'll help you.", "OK, I'll be helping you."], 0, "Anlık karar → will."),
        mc("Pilot anonsu:", ["We will be landing in ten minutes.", "We are land in ten minutes."], 0, "Anons → will be + -ing."),
        gap("___ you be coming to the meeting tomorrow?", ["Will"], "Will + özne + be + -ing?"),
        gap("I'll be ___ (pass) the bank on my way, so I can pay the bill.", ["passing"], "Normal akış."),
        gap("Will you be ___ (need) the car this evening?", ["needing"], "Kibar soru."),
        gap("I won't be ___ (come) to the office on Monday. I'm working from home.", ["coming"], "Olumsuz plan."),
        listen("Excuse me, will you be using this table? – No, go ahead. I'll be leaving in a minute anyway.", "Kişi masayı neden veriyor?", ["Masa kirli", "Zaten birazdan gidecek", "Başka masaya geçiyor"], 1, "\"I'll be leaving in a minute anyway\""),
        typ("Kibar bir soru yazın: Bir iş arkadaşınıza öğleden sonra toplantı odasını kullanıp kullanmayacağını sorun.", variants("Will you be using the meeting room this afternoon?", "Will you be using the meeting room in the afternoon?", "Will you be needing the meeting room this afternoon?", "Are you going to be using the meeting room this afternoon?"), "Will you be using the meeting room this afternoon?"),
    ],
    {"kind": "speaking", "task": speak("JAI ile ofiste kısa bir konuşma yapın. Ondan 3 şey ödünç almak ya da rica etmek istiyorsunuz (projektör, araba, park yeri). Önce future continuous ile kibarca planlarını sorun, sonra isteğinizi söyleyin. JAI size de soracak; zaten yapacağınız şeyleri \"I'll be ... anyway\" ile söyleyin.",
                                       "Will you be using the projector this afternoon? If not, could I borrow it for my presentation? ... Will you be driving to the office tomorrow? ... Oh, I'll be going past the bakery anyway, so I can get you some simit.",
                                       ["Kibar future continuous soruları", "anyway ile normal akış", "Doğal ofis dili"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "O zamana kadar bitirmiş olacağım", "Gelecekte belirli bir zamana kadar tamamlanmış olacak işleri future perfect ile anlatabilirim.",
    {"kind": "text", "title": "Bir girişimcinin 5 yıllık planı", "body": "Defne Yalın started her online language school in her living room two years ago. Today, she has 15 teachers and 800 students. Her goals for the next five years are ambitious.\n\n\"By the end of this year, we'll have launched our mobile app,\" she says. \"By 2028, we'll have opened offices in Germany and the Netherlands.\"\n\nShe's also thinking about her own development. \"I'm doing an MBA part-time. By the time I'm 35, I'll have finished it, and I'll have learned how to manage a much bigger company.\"\n\nIs she worried about failure? \"Of course. But in five years, even if everything goes wrong, I'll have gained more experience than in twenty years in a normal job.\"",
     "questions": [
        mc("What will Defne have done by the end of this year?", ["Opened offices in Germany", "Launched a mobile app", "Finished her MBA"], 1, "\"By the end of this year, we'll have launched our mobile app\""),
        mc("When will she have finished her MBA?", ["By the end of this year", "By 2028", "By the time she's 35"], 2, "\"By the time I'm 35, I'll have finished it\""),
     ]},
    {"explanation": "**Future perfect:** will have + **V3**\n\nGelecekte **belirli bir zamana kadar tamamlanmış olacak** bir eylemi anlatır (\"-mış olacağım\").\n\n| | Yapı | Örnek |\n|---|---|---|\n| Olumlu | will have + V3 | By 2028, we**'ll have opened** two offices. |\n| Olumsuz | won't have + V3 | I **won't have finished** by Friday. |\n| Soru | Will + özne + have + V3? | **Will** you **have finished** by six? |\n\n**Zaman çizgisi:**\n\n```\n  şimdi ──[opened]─────────── X 2028\n           (bu tarihten önce bitmiş olacak)\n```\n\n**Anahtar ifade: by** (-e kadar)\n\n- **by** Friday / **by** the end of the year / **by** 2030\n- **by the time** + present simple: **By the time** you **arrive**, I'll have cooked dinner.\n- **by then**: By then, I'll have saved enough money.\n\n**Dikkat:** by the time'dan sonra will kullanılmaz (B1'deki zaman bağlaçları kuralı):\n\n- By the time you **get** here (~~will get~~), we'll have left.",
     "examples": [{"en": "By the end of the month, I'll have worked here for ten years.", "tr": "Ay sonunda burada on yıldır çalışıyor olacağım."},
                  {"en": "Don't worry, I'll have finished the report by Monday.", "tr": "Merak etme, raporu pazartesiye kadar bitirmiş olacağım."},
                  {"en": "By the time you wake up, I'll have left for the airport.", "tr": "Sen uyandığında ben havalimanına gitmiş olacağım."}],
     "turkishNote": "Türkçedeki \"-mış olacağım\" (bitirmiş olacağım, gitmiş olacağım) yapısı future perfect'e tam olarak denk gelir. \"by\" kelimesini \"tarafından\" ile karıştırmayın: Burada \"-e kadar\" anlamındadır. \"until\" ise \"-e kadar (süre boyunca)\" anlamına gelir: I'll work until 6 (6'ya kadar çalışacağım) / I'll have finished by 6 (6'ya kadar bitirmiş olacağım)."},
    [
        mc("\"Cumaya kadar bitirmiş olacağım.\"", ["I'll finish until Friday.", "I'll have finished by Friday."], 1, "will have + V3 + by."),
        mc("Hangisi doğru?", ["By the time you will arrive, I'll have left.", "By the time you arrive, I'll have left."], 1, "by the time + present."),
        mc("by mı until mi? \"I'll be at work ___ 6 pm.\" (6'ya kadar orada olacağım)", ["by", "until"], 1, "Süre boyunca → until."),
        mc("by mı until mi? \"I'll have sent it ___ 6 pm.\" (en geç 6'da)", ["by", "until"], 0, "Son nokta → by."),
        gap("By 2030, scientists ___ (find) a cure.", ["will have found", "'ll have found"], "will have + V3."),
        gap("I ___ (not / finish) the project by Monday. I need more time.", ["won't have finished", "will not have finished"], "Olumsuz."),
        gap("Will you have ___ (read) the book by our next class?", ["read"], "V3."),
        gap("By the ___ you get home, I'll have cooked dinner.", ["time"], "By the time."),
        listen("I'm retiring next June. By then, I'll have worked for the same company for forty years. I'll have seen five different CEOs!", "Konuşan emekli olduğunda kaç yıl çalışmış olacak?", ["Beş", "Yirmi", "Kırk"], 2, "\"I'll have worked for the same company for forty years\""),
        typ("İngilizce yazın: \"Sen uyandığında ben havalimanına gitmiş olacağım.\"", variants("By the time you wake up, I'll have left for the airport.", "By the time you wake up, I will have left for the airport.", "By the time you wake up, I'll have gone to the airport.", "By the time you wake up, I will have gone to the airport.", "When you wake up, I'll have left for the airport.", "When you wake up, I'll have gone to the airport.", "I'll have left for the airport by the time you wake up."), "By the time you wake up, I'll have left for the airport."),
    ],
    {"kind": "speaking", "task": speak("Önümüzdeki 1, 5 ve 10 yıl için kariyer ve kişisel hedeflerinizi future perfect ile anlatın. Her dönem için en az iki şey söyleyin ve by, by the time ve by then kullanın. Gerçekleşmemiş olabilecek bir şeyi de won't have ile söyleyin.",
                                       "By the end of next year, I'll have finished my English course and I'll have got my first promotion. In five years' time, I'll have bought a flat and I'll have travelled to at least ten countries. By the time I'm 40, I'll have started my own business. By then, I probably won't have paid off my mortgage, but I'll have saved some money.",
                                       ["will have + V3 doğru", "by / by the time / by then", "won't have"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Yıldır çalışıyor olacağım", "Future perfect continuous ile gelecekteki bir ana kadar süren eylemleri anlatabilir ve gelecek zaman yapılarını karşılaştırabilirim.",
    {"kind": "dialogue", "title": "Yıl dönümü", "lines": [
        {"speaker": "HR Manager", "text": "Mr Arslan, next month you'll have been working here for twenty-five years. Congratulations!"},
        {"speaker": "Mr Arslan", "text": "Thank you! It's hard to believe. I'll have been doing the same journey to work for a quarter of a century."},
        {"speaker": "HR Manager", "text": "We'd like to organise a small celebration. Will you be working on the 15th?"},
        {"speaker": "Mr Arslan", "text": "Yes, but I'm going to be in meetings all morning."},
        {"speaker": "HR Manager", "text": "Then we'll do it at lunchtime. And what are your plans for the future?"},
        {"speaker": "Mr Arslan", "text": "I'm retiring in three years. By then, I'll have trained my replacement, I hope!"}],
     "questions": [
        mc("How long will Mr Arslan have been working there next month?", ["Fifteen years", "Twenty-five years", "Three years"], 1, "\"you'll have been working here for twenty-five years\""),
        mc("What does Mr Arslan hope he will have done before he retires?", ["Bought a house", "Trained his replacement", "Travelled the world"], 1, "\"I'll have trained my replacement, I hope!\""),
     ]},
    {"explanation": "**Future perfect continuous:** will have been + fiil-**ing**\n\nGelecekteki bir ana kadar **ne kadar süredir** bir şeyin süreceğini vurgular. Genellikle **for + süre** ile kullanılır.\n\n- Next month, I**'ll have been working** here **for 25 years**.\n- By 2030, they**'ll have been living** in Canada **for a decade**.\n\n**Gelecek zaman yapılarının karşılaştırması:**\n\n| Yapı | Kullanım | Örnek |\n|---|---|---|\n| **will** | anlık karar, tahmin, söz | I**'ll** help you. / It**'ll** rain. |\n| **be going to** | plan, kanıta dayalı tahmin | I**'m going to** apply. |\n| **present continuous** | kesinleşmiş plan | I**'m meeting** the CEO on Monday. |\n| **will be + -ing** | gelecekte süren eylem | This time tomorrow, I**'ll be flying**. |\n| **will have + V3** | gelecekteki bir zamana kadar tamamlanmış | By Friday, I**'ll have finished**. |\n| **will have been + -ing** | gelecekteki bir ana kadar süre | By June, I**'ll have been studying** for 3 years. |\n\nFuture perfect continuous, konuşmada nadiren kullanılır; ama yıl dönümleri, rekorlar ve uzun süreçler için çok etkilidir.",
     "examples": [{"en": "By the time we arrive, we'll have been driving for ten hours.", "tr": "Vardığımızda on saattir araba kullanıyor olacağız."},
                  {"en": "In June, she'll have been teaching for thirty years.", "tr": "Haziranda otuz yıldır öğretmenlik yapıyor olacak."},
                  {"en": "I'm meeting the director on Monday.", "tr": "Pazartesi müdürle görüşeceğim. (kesinleşmiş plan)"}],
     "turkishNote": "Türkçede \"Haziranda otuz yıldır öğretmenlik yapıyor olacak\" cümlesi future perfect continuous'ın tam karşılığıdır. Ancak bu yapı İngilizcede de az kullanılır; günlük konuşmada genellikle \"In June, it'll be thirty years since she started teaching\" gibi alternatifler tercih edilir."},
    [
        mc("Süre vurgusu: \"By June, I ___ English for five years.\"", ["will have studied", "will have been studying"], 1, "for + süre, süreç → future perfect continuous."),
        mc("Kesinleşmiş plan: \"I ___ the dentist at 4 tomorrow.\"", ["'m seeing", "'ll have seen"], 0, "Kesin plan → present continuous."),
        mc("Anlık karar: \"The phone's ringing. I ___ it.\"", ["'ll get", "'ll be getting"], 0, "Anlık karar → will."),
        mc("Kanıta dayalı tahmin: \"Look at those clouds! It ___ rain.\"", ["will have rained", "'s going to"], 1, "Kanıt → going to."),
        gap("By 2030, we'll have been ___ (live) here for twenty years.", ["living"], "will have been + -ing."),
        gap("By midnight, I'll ___ been working for 16 hours!", ["have"], "will have been."),
        gap("This time next week, I ___ (lie) on a beach in Bodrum.", ["'ll be lying", "will be lying"], "Gelecekte süren → will be + -ing."),
        gap("Don't worry, I ___ (finish) it by tomorrow.", ["'ll have finished", "will have finished"], "Tamamlanmış → will have + V3."),
        match([("will be + -ing", "gelecekte süren eylem"), ("will have + V3", "gelecekte tamamlanmış"), ("will have been + -ing", "gelecekteki bir ana kadar süre"), ("be going to", "plan, kanıt"), ("present continuous", "kesinleşmiş plan")], "Eşleştirin."),
        listen("When we land in Sydney, we'll have been travelling for almost twenty-four hours. I'm going to sleep for a whole day!", "Sydney'e vardıklarında ne kadar süredir yolculuk ediyor olacaklar?", ["On iki saat", "Yaklaşık yirmi dört saat", "İki gün"], 1, "\"we'll have been travelling for almost twenty-four hours\""),
    ],
    {"kind": "speaking", "task": speak("JAI size 6 durum verecek. Her biri için en uygun gelecek zaman yapısını seçerek bir cümle kurun (will, going to, present continuous, will be + -ing, will have + V3, will have been + -ing). Neden o yapıyı seçtiğinizi kısaca açıklayın.",
                                       "I'm meeting my manager at 3 tomorrow; it's in my calendar. Look at the traffic! We're going to be late. This time tomorrow, I'll be taking my exam. By Friday, I'll have finished all my reports. Next year, I'll have been working here for a decade. Oh, you need a pen? I'll lend you mine.",
                                       ["Doğru yapı seçimi", "Doğru biçim", "Açıklama"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "İşe başvuru", "Bir iş görüşmesinde kendimi ve hedeflerimi etkili şekilde anlatabilir ve profesyonel bir ön yazı yazabilirim.",
    {"kind": "dialogue", "title": "İş görüşmesi", "lines": [
        {"speaker": "Interviewer", "text": "So, tell us a little about yourself."},
        {"speaker": "Candidate", "text": "I've been working in digital marketing for four years. Currently, I'm in charge of social media campaigns for a mid-sized fashion brand."},
        {"speaker": "Interviewer", "text": "What would you say is your greatest strength?"},
        {"speaker": "Candidate", "text": "I'd say my ability to analyse data. For example, last year I increased our online sales by 30% by changing our ad strategy."},
        {"speaker": "Interviewer", "text": "Impressive. And where do you see yourself in five years?"},
        {"speaker": "Candidate", "text": "I hope I'll be leading a team. By then, I'll have gained experience in international markets, which is one reason I'm so interested in this position."}],
     "questions": [
        mc("What is the candidate's greatest strength?", ["Leadership", "Analysing data", "Design"], 1, "\"my ability to analyse data\""),
        mc("Where does the candidate see themselves in five years?", ["Running their own business", "Leading a team", "Working abroad"], 1, "\"I hope I'll be leading a team\""),
     ]},
    {"explanation": "**Mülakatta sık sorulan sorular ve yanıt kalıpları:**\n\n| Soru | Yanıt kalıpları |\n|---|---|\n| Tell us about yourself. | **I've been working in** ... **for** ... / **Currently, I'm in charge of** ... |\n| Why do you want this job? | **I'm particularly interested in** ... / **This role would allow me to** ... |\n| What's your greatest strength? | **I'd say** my ability to ... / **For example**, ... |\n| What's your biggest weakness? | **I sometimes** ..., **but I've been working on** it by ... |\n| Where do you see yourself in 5 years? | **I hope I'll be** -ing ... / **By then, I'll have** + V3 ... |\n| Do you have any questions? | **Could you tell me more about** ...? / **What would a typical day look like?** |\n\n**STAR yöntemi** (güçlü bir örnek vermek için):\n\n- **S**ituation (Durum): Last year, our sales were falling.\n- **T**ask (Görev): I had to find a solution.\n- **A**ction (Eylem): I analysed the data and changed our ad strategy.\n- **R**esult (Sonuç): Sales increased by 30%.\n\n**Ön yazı (cover letter) yapısı:**\n\n1. **Giriş**: Hangi pozisyona başvurduğunuz → *I am writing to apply for the position of ...*\n2. **Deneyim ve beceriler**: Somut örnekler\n3. **Neden bu şirket**: Şirket hakkında bir şey bilin\n4. **Kapanış**: *I look forward to hearing from you.* / *Yours sincerely,*",
     "examples": [{"en": "I am writing to apply for the position of Sales Manager.", "tr": "Satış Müdürü pozisyonuna başvurmak için yazıyorum."},
                  {"en": "I sometimes take on too much, but I've been learning to delegate.", "tr": "Bazen çok fazla iş üstlenirim ama görev dağıtmayı öğreniyorum."},
                  {"en": "I look forward to hearing from you.", "tr": "Sizden haber bekliyorum."}],
     "turkishNote": "Türkçe özgeçmiş ve ön yazılarda genellikle genel ifadeler (\"çalışkan\", \"sorumluluk sahibi\") kullanılır. İngilizce mülakatlarda ise somut örnekler ve sayılar beklenir: \"I'm hard-working\" yerine \"Last year I managed a project with a team of eight and delivered it two weeks early.\" Ayrıca \"I look forward to hear from you\" yanlıştır; look forward to + -ing kuralını hatırlayın."},
    [
        mc("Ön yazıya başlamak:", ["I am writing to apply for the position of ...", "Hi, I want this job."], 0, "Resmî giriş."),
        mc("Hangisi doğru?", ["I look forward to hear from you.", "I look forward to hearing from you."], 1, "look forward to + -ing."),
        mc("Zayıf yön sorusuna iyi bir cevap:", ["I don't have any weaknesses.", "I sometimes find it hard to say no, but I've been working on it."], 1, "Dürüst + gelişim."),
        mc("STAR yöntemindeki \"R\":", ["Reason", "Result", "Role"], 1, "Result."),
        gap("I've been working in sales ___ six years.", ["for"], "for + süre."),
        gap("Currently, I'm ___ charge of a team of five.", ["in"], "in charge of."),
        gap("In five years, I hope I'll be ___ (manage) my own department.", ["managing"], "will be + -ing."),
        gap("By then, I'll have ___ (gain) more international experience.", ["gained"], "will have + V3."),
        listen("Thank you for your time. Do you have any questions for us? – Yes. Could you tell me more about the training opportunities, and what a typical day would look like?", "Aday ne soruyor?", ["Maaşı", "Eğitim fırsatları ve tipik bir günü", "Tatil günlerini"], 1, "\"training opportunities, and what a typical day would look like\""),
        typ("İngilizce yazın: \"Pazarlama Müdürü pozisyonuna başvurmak için yazıyorum.\"", variants("I am writing to apply for the position of Marketing Manager.", "I'm writing to apply for the position of Marketing Manager.", "I am writing to apply for the Marketing Manager position.", "I'm writing to apply for the Marketing Manager position.", "I am writing to apply for the position of marketing manager.", "I am writing to apply for the post of Marketing Manager."), "I am writing to apply for the position of Marketing Manager."),
    ],
    {"kind": "writing", "task": write("Hayalinizdeki bir işe başvurmak için bir ön yazı (cover letter) yazın (180–220 kelime). Resmî giriş ve kapanış kullanın; deneyiminizi somut örneklerle (STAR) anlatın; şirkete neden ilgi duyduğunuzu açıklayın ve gelecek hedeflerinizi future continuous ve future perfect ile ifade edin.",
                                      "Dear Ms Kaplan,\n\nI am writing to apply for the position of Junior Project Manager, which I saw advertised on your website.\n\nI have been working as a project coordinator at a software company in Ankara for three years. Currently, I am in charge of planning and tracking projects for a team of twelve developers. Last year, our team was regularly missing deadlines. I introduced a new weekly planning system, and within six months we were delivering 90% of our projects on time.\n\nI am particularly interested in your company because of your work in educational technology. I have always been passionate about learning, and I would love to work on products that help students.\n\nI am currently completing a professional project management certificate, and by the end of this year I will have finished it. In five years' time, I hope I will be leading international projects and helping your company grow in new markets.\n\nI have attached my CV, and I would be happy to discuss my application in more detail.\n\nI look forward to hearing from you.\n\nYours sincerely,\nCan Erdoğan",
                                      ["Resmî ön yazı yapısı", "Somut örnek (STAR)", "Future continuous / perfect", "Şirkete özel ilgi", "Profesyonel üslup"])},
)

u.test([
    mc("This time tomorrow, I ___ to London.", ["will fly", "will be flying"], 1, "Future continuous"),
    mc("By Friday, I ___ the report.", ["will have finished", "will be finishing"], 0, "Future perfect"),
    mc("Daha kibar:", ["Will you use the car tonight?", "Will you be using the car tonight?"], 1, "Kibar plan sorusu"),
    mc("Hangisi doğru?", ["By the time you will arrive, we'll have eaten.", "By the time you arrive, we'll have eaten."], 1, "by the time + present"),
    mc("\"I'll be at work ___ 6.\" (6'ya kadar orada)", ["by", "until"], 1, "until"),
    gap("In June, she'll have been ___ (teach) for 30 years.", ["teaching"], "Future perfect continuous"),
    gap("Don't call at 8. I ___ (have) dinner.", ["'ll be having", "will be having"], "Future continuous"),
    gap("By 2030, I ___ (pay) off my loan.", ["will have paid", "'ll have paid"], "Future perfect"),
    gap("I'll be ___ (pass) the shop anyway. Do you need anything?", ["passing"], "Normal akış"),
    mc("Kesinleşmiş plan:", ["I'm meeting the CEO at 10 tomorrow.", "I'll have met the CEO at 10 tomorrow."], 0, "Present continuous"),
    gap("I'm in ___ of a team of ten.", ["charge"], "in charge of"),
    mc("Hangisi doğru?", ["I look forward to meet you.", "I look forward to meeting you."], 1, "look forward to + -ing"),
    listen("By the time I graduate next year, I'll have done three internships. And this time next year, I'll probably be working for one of those companies.", "Konuşan mezun olduğunda kaç staj yapmış olacak?", ["Bir", "İki", "Üç"], 2, "\"I'll have done three internships\""),
    typ("İngilizce yazın: \"Seneye bu zaman yurt dışında çalışıyor olacağım.\"", variants("This time next year, I'll be working abroad.", "This time next year, I will be working abroad.", "This time next year I'll be working abroad.", "I'll be working abroad this time next year."), "This time next year, I'll be working abroad."),
    write("\"10 yıl sonraki ben\" başlıklı bir yazı yazın (160–200 kelime). Kariyerinizde ve özel hayatınızda 10 yıl sonra ne yapıyor olacağınızı (future continuous), o zamana kadar neleri başarmış olacağınızı (future perfect) ve bir şeyi ne kadar süredir yapıyor olacağınızı (future perfect continuous) anlatın. Kariyer kelimelerini kullanın.",
          "Ten years from now, I'll be 38, and I hope my life will look very different. Professionally, I'll be working as a senior architect at an international firm, and I'll be designing eco-friendly buildings. By then, I'll have completed my master's degree in sustainable design, and I'll have worked on projects in at least three different countries. I'd also like to have my own small team. In fact, by the time I'm 38, I'll have been working in architecture for fifteen years, so I think I'll be ready to take on more responsibility. In my personal life, I'll probably be living in a house with a garden, maybe in a smaller city with a better work-life balance. I'll have learned to play the piano, which has always been a dream of mine. Of course, life doesn't always go to plan. But even if things change, I'm sure I'll have learned a lot along the way, and in the long run, that's what matters most.",
          ["Future continuous", "Future perfect", "Future perfect continuous", "Kariyer kelimeleri", "Akıcı ve düzenli metin"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

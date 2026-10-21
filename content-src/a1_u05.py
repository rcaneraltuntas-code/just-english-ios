"""A1 Ünite 5: Günüm."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("A1", 5, "Günüm", "My Day",
         "Günlük rutinimi saatleriyle anlatabilir, başkalarına günlerini sorabilirim.",
         ["present simple (I/you/we/they): olumlu, olumsuz, soru", "saatler ve at/in/on", "sıklık zarfları"],
         ["günlük eylemler", "saatler", "günler"],
         {"title": "Kimin günü?", "durationMinutes": 45,
          "goal": "Öğrenciler günlük rutinlerini birbirine sorar (What time do you get up?), sonra öğretmen anonim rutinler okur ve grup kimin olduğunu tahmin eder."})

u.vocab([
    ("get up", "kalkmak (yataktan)", "I get up at seven.", "Yedide kalkarım.", None),
    ("wake up", "uyanmak", "I wake up at six thirty.", "Altı buçukta uyanırım.", "wake up = gözünü açmak; get up = yataktan kalkmak."),
    ("have breakfast", "kahvaltı etmek", "We have breakfast together.", "Birlikte kahvaltı ederiz.", "have lunch / have dinner da aynı şekilde."),
    ("take a shower", "duş almak", "I take a shower in the morning.", "Sabah duş alırım.", None),
    ("go to work", "işe gitmek", "They go to work by bus.", "İşe otobüsle giderler.", "go to school, go to university ama go home (to yok)."),
    ("start", "başlamak", "I start work at nine.", "İşe dokuzda başlarım.", None),
    ("finish", "bitirmek", "We finish at five.", "Beşte bitiririz.", None),
    ("go home", "eve gitmek", "I go home at six.", "Altıda eve giderim.", "go to home değil, go home."),
    ("cook", "yemek pişirmek", "I cook dinner every day.", "Her gün akşam yemeği pişiririm.", None),
    ("watch TV", "televizyon izlemek", "We watch TV in the evening.", "Akşam televizyon izleriz.", None),
    ("go to bed", "yatmak", "I go to bed at eleven.", "On birde yatarım.", None),
    ("study", "ders çalışmak", "I study English every day.", "Her gün İngilizce çalışırım.", None),
    ("work", "çalışmak (işte)", "My parents work in a bank.", "Annemle babam bir bankada çalışır.", None),
    ("live", "yaşamak, oturmak", "We live in Istanbul.", "İstanbul'da yaşıyoruz.", None),
    ("o'clock", "saat (tam)", "It's three o'clock.", "Saat üç.", "Yalnızca tam saatlerde kullanılır."),
    ("half past", "buçuk", "It's half past seven.", "Saat yedi buçuk.", None),
    ("quarter", "çeyrek", "It's quarter past two.", "Saat ikiyi çeyrek geçiyor.", None),
    ("always", "her zaman", "I always have breakfast.", "Her zaman kahvaltı ederim.", None),
    ("usually", "genellikle", "I usually walk to work.", "Genellikle işe yürürüm.", None),
    ("sometimes", "bazen", "We sometimes eat out.", "Bazen dışarıda yeriz.", None),
    ("never", "asla, hiç", "I never drink coffee.", "Hiç kahve içmem.", "never ile olumsuz fiil kullanılmaz."),
    ("weekend", "hafta sonu", "What do you do at the weekend?", "Hafta sonu ne yaparsın?", "İngiliz: at the weekend, Amerikan: on the weekend."),
    ("Monday", "pazartesi", "I go to the gym on Mondays.", "Pazartesileri spora giderim.", "Günler büyük harfle yazılır."),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Günlük rutin", "Günlük yaptıklarımı present simple ile söyleyebilirim.",
    {"kind": "dialogue", "title": "Deniz'in sabahı", "lines": [
        {"speaker": "Deniz", "text": "I get up at seven every day."},
        {"speaker": "Deniz", "text": "I take a shower and I have breakfast with my family."},
        {"speaker": "Deniz", "text": "Then I go to work by metro. I work in an office in the city centre."},
        {"speaker": "Deniz", "text": "I start work at nine and I finish at six."},
        {"speaker": "Deniz", "text": "In the evening, I cook dinner and I study English."}],
     "questions": [
        mc("How does Deniz go to work?", ["By bus", "By metro", "By car"], 1, "\"I go to work by metro.\""),
        mc("What does Deniz do in the evening?", ["Watches TV", "Cooks and studies English", "Goes to the gym"], 1, "\"I cook dinner and I study English.\""),
     ]},
    {"explanation": "Her gün, düzenli olarak yaptığımız şeyler için **present simple** (geniş zaman) kullanılır.\n\nI, you, we, they ile fiil **yalın** halde kalır:\n\n- I **get up** at seven.\n- We **have** breakfast together.\n- They **work** in a bank.\n\nhe/she/it ile fiilin nasıl değiştiğini 6. ünitede göreceğiz.",
     "examples": [{"en": "I live in Ankara.", "tr": "Ankara'da yaşıyorum."},
                  {"en": "We go to bed at eleven.", "tr": "On birde yatarız."},
                  {"en": "You work very hard.", "tr": "Çok çalışıyorsun."}],
     "turkishNote": "Türkçede \"Ankara'da yaşıyorum\" (şimdiki zaman) deriz ama bu kalıcı bir durumdur. İngilizcede kalıcı durumlar ve alışkanlıklar için geniş zaman kullanılır: I live in Ankara (I'm living değil). Ayrıca \"go home\" denir, \"go to home\" değil."},
    [
        match([("get up", "kalkmak"), ("have breakfast", "kahvaltı etmek"), ("go to bed", "yatmak"), ("take a shower", "duş almak"), ("go home", "eve gitmek")], "Rutin eylemleri eşleştirin."),
        gap("I ___ up at seven.", ["get"], "kalkmak = get up."),
        gap("We ___ breakfast at eight.", ["have"], "kahvaltı etmek = have breakfast."),
        mc("Hangisi doğru?", ["I go to home at six.", "I go home at six.", "I go at home at six."], 1, "home'dan önce to gelmez.", {0: "\"go home\" kalıbında to yoktur."}),
        mc("\"Ankara'da yaşıyorum.\" (kalıcı durum)", ["I live in Ankara.", "I am live in Ankara.", "I living in Ankara."], 0, "Kalıcı durum → present simple: I live.", {1: "am ile live birlikte kullanılmaz."}),
        order(["work", "They", "a", "in", "bank"], "They work in a bank.", "Özne + fiil + yer.", "Onlar bir bankada çalışır."),
        gap("I ___ English every evening.", ["study"], "ders çalışmak = study."),
        listen("I wake up at six, but I get up at half past six. I have breakfast and I go to work at seven thirty.", "Konuşan kaçta işe gidiyor?", ["6:00", "6:30", "7:30"], 2, "\"I go to work at seven thirty.\""),
        typ("İngilizce yazın: \"Akşam yemeği pişiririm.\"", variants("I cook dinner.", "I cook dinner in the evening."), "I + cook + dinner."),
        mc("wake up ile get up arasındaki fark:", ["Aynı anlamdadır.", "wake up = uyanmak, get up = yataktan kalkmak", "wake up = kalkmak, get up = uyanmak"], 1, "Önce uyanırız (wake up), sonra kalkarız (get up)."),
    ],
    {"kind": "speaking", "task": speak("Sabah rutininizi 4 cümleyle anlatın.",
                                       "I get up at seven. I take a shower and I have breakfast. I go to work by bus. I start work at nine.",
                                       ["Rutin fiilleri doğru", "Fiil yalın halde (I + fiil)", "Sıralı ve anlaşılır"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "Saat kaç?", "Saati söyleyip bir şeyin hangi saatte olduğunu belirtebilirim.",
    {"kind": "dialogue", "title": "Sokakta", "lines": [
        {"speaker": "Ali", "text": "Excuse me, what time is it?"},
        {"speaker": "Woman", "text": "It's quarter to three."},
        {"speaker": "Ali", "text": "Oh no! My class starts at three."},
        {"speaker": "Woman", "text": "Don't worry, you have fifteen minutes."},
        {"speaker": "Ali", "text": "Thank you!"}],
     "questions": [
        mc("What time is it?", ["2:15", "2:45", "3:15"], 1, "quarter to three = üçe çeyrek var = 2:45"),
        mc("What time does Ali's class start?", ["2:45", "3:00", "3:15"], 1, "\"My class starts at three.\""),
     ]},
    {"explanation": "Saati sormak: **What time is it?** ya da **What's the time?**\n\n| Saat | İngilizce | Kolay yol |\n|---|---|---|\n| 7:00 | seven **o'clock** | seven |\n| 7:15 | **quarter past** seven | seven fifteen |\n| 7:30 | **half past** seven | seven thirty |\n| 7:45 | **quarter to** eight | seven forty-five |\n| 7:10 | ten **past** seven | seven ten |\n| 7:50 | ten **to** eight | seven fifty |\n\n**past** = geçiyor, **to** = var. Bir şeyin saati için **at**: at seven, at half past six.\n\nAM = öğleden önce, PM = öğleden sonra.",
     "examples": [{"en": "It's half past four.", "tr": "Saat dört buçuk."},
                  {"en": "The film starts at eight.", "tr": "Film sekizde başlıyor."},
                  {"en": "I get up at quarter to seven.", "tr": "Yediye çeyrek kala kalkarım."}],
     "turkishNote": "\"half past seven\" yedi buçuktur, sekiz buçuk değil: yediyi yarım geçiyor. \"quarter to\" ise Türkçedeki \"çeyrek var\" ile aynıdır. Saatten önce mutlaka \"at\" gelir: \"I get up seven\" değil, \"I get up at seven\"."},
    [
        match([("3:00", "three o'clock"), ("3:15", "quarter past three"), ("3:30", "half past three"), ("3:45", "quarter to four")], "Saatleri eşleştirin."),
        mc("half past seven kaçtır?", ["6:30", "7:30", "8:30"], 1, "yediyi yarım geçiyor = 7:30."),
        mc("ten to nine kaçtır?", ["8:50", "9:10", "9:50"], 0, "dokuza on var = 8:50."),
        gap("It's quarter ___ five. (5:15)", ["past"], "Geçiyor = past."),
        gap("It's twenty ___ six. (5:40)", ["to"], "Var = to."),
        gap("The lesson starts ___ ten o'clock.", ["at"], "Saatten önce at."),
        order(["time", "What", "it", "is", "?"], "What time is it?", "What time + is + it?", "Saat kaç?"),
        listen("The train leaves at twenty past eleven.", "Tren kaçta kalkıyor?", ["11:20", "11:40", "10:40"], 0, "twenty past eleven = 11:20"),
        typ("Rakamla yazın: \"quarter to ten\" (ss:dd)", ["9:45", "09:45"], "ona çeyrek var = 9:45"),
        mc("Hangisi doğru?", ["I get up seven.", "I get up at seven.", "I get up in seven."], 1, "Saatten önce at."),
    ],
    {"kind": "speaking", "task": speak("JAI size 5 farklı saat söyleyecek, siz de İngilizce okuyacaksınız (8:00, 8:15, 8:30, 8:45, 9:10).",
                                       "It's eight o'clock. It's quarter past eight. It's half past eight. It's quarter to nine. It's ten past nine.",
                                       ["past/to doğru", "quarter/half doğru", "It's ile başladı"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "Yapmam", "Yapmadığım şeyleri don't ile söyleyebilirim.",
    {"kind": "dialogue", "title": "İki kardeş", "lines": [
        {"speaker": "Mia", "text": "My brother and I are very different."},
        {"speaker": "Mia", "text": "I get up early. My brother? He loves his bed!"},
        {"speaker": "Mia", "text": "I don't drink coffee. I drink tea."},
        {"speaker": "Mia", "text": "We don't watch TV together because we don't like the same programmes."},
        {"speaker": "Mia", "text": "But we always have dinner together on Sundays."}],
     "questions": [
        mc("What does Mia drink?", ["Coffee", "Tea", "Juice"], 1, "\"I don't drink coffee. I drink tea.\""),
        mc("What do they do together on Sundays?", ["Watch TV", "Have dinner", "Get up early"], 1, "\"we always have dinner together on Sundays\""),
     ]},
    {"explanation": "I, you, we, they ile olumsuz cümle **don't** (do not) + fiil ile kurulur:\n\n- I **don't** drink coffee.\n- We **don't** watch TV.\n- They **don't** live here.\n\nFiil yalın halde kalır. **am/is/are** ile birlikte kullanılmaz.",
     "examples": [{"en": "I don't eat meat.", "tr": "Et yemem."},
                  {"en": "We don't work on Saturdays.", "tr": "Cumartesileri çalışmayız."},
                  {"en": "They don't speak Turkish.", "tr": "Onlar Türkçe konuşmaz."}],
     "turkishNote": "Türkçeden çevirirken \"I'm not drink coffee\" hatası çok yapılır. am/is/are yalnızca to be cümlelerinde (I'm not a student) kullanılır. Eylem fiilleri için don't gerekir: I don't drink coffee."},
    [
        gap("I ___ like coffee.", ["don't", "do not"], "Olumsuz → don't + fiil."),
        gap("We ___ work on Sundays.", ["don't", "do not"], "we → don't."),
        mc("Hangisi doğru?", ["I'm not drink tea.", "I don't drink tea.", "I not drink tea."], 1, "Eylem fiilinde olumsuzluk don't ile yapılır.", {0: "am + fiil olmaz. don't kullanın.", 2: "not tek başına kullanılmaz, don't gerekir."}),
        mc("Hangisi doğru?", ["I don't a student.", "I'm not a student."], 1, "to be cümlesinde → I'm not."),
        order(["don't", "They", "here", "live"], "They don't live here.", "Özne + don't + fiil.", "Onlar burada yaşamıyor."),
        typ("Olumsuz yapın: \"I watch TV in the morning.\"", variants("I don't watch TV in the morning."), "I + don't + watch ..."),
        mc("\"Et yemem.\"", ["I don't eat meat.", "I'm not eat meat.", "I eat not meat."], 0, "don't + eat."),
        listen("I don't have breakfast at home. I have a coffee and a simit on the way to work.", "Konuşan evde kahvaltı ediyor mu?", ["Evet", "Hayır"], 1, "\"I don't have breakfast at home.\""),
        gap("You ___ know my sister. (tanımıyorsun)", ["don't", "do not"], "you → don't."),
        match([("I'm not", "a teacher"), ("I don't", "work here"), ("We aren't", "from Izmir"), ("We don't", "speak French")], "to be cümlelerinde am/is/are not, eylem fiillerinde don't."),
    ],
    {"kind": "speaking", "task": speak("Yapmadığınız 3 şeyi söyleyin ve yerine ne yaptığınızı ekleyin.",
                                       "I don't drink coffee. I drink tea. I don't watch TV. I read books.",
                                       ["don't + fiil doğru", "am/is/are ile karıştırmadı", "Olumlu cümleyle tamamladı"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Sen ne yaparsın?", "Başkalarına günlük rutinlerini sorabilirim.",
    {"kind": "dialogue", "title": "Yeni iş arkadaşı", "lines": [
        {"speaker": "Tom", "text": "Do you live near the office?"},
        {"speaker": "Selin", "text": "No, I don't. I live in Kadıköy."},
        {"speaker": "Tom", "text": "What time do you get up?"},
        {"speaker": "Selin", "text": "At six. I take the ferry every morning."},
        {"speaker": "Tom", "text": "Do you like it?"},
        {"speaker": "Selin", "text": "Yes, I do! I have breakfast on the ferry."}],
     "questions": [
        mc("Where does Selin live?", ["Near the office", "In Kadıköy", "On a ferry"], 1, "\"I live in Kadıköy.\""),
        mc("Where does Selin have breakfast?", ["At home", "In the office", "On the ferry"], 2, "\"I have breakfast on the ferry.\""),
     ]},
    {"explanation": "**Evet/hayır sorusu:** Do + özne + fiil?\n\n- **Do you** live here? – Yes, I **do**. / No, I **don't**.\n- **Do they** work at night? – Yes, they **do**. / No, they **don't**.\n\n**Bilgi sorusu:** Soru kelimesi + do + özne + fiil?\n\n- **What time do you** get up?\n- **Where do you** work?\n- **What do you** do at the weekend?",
     "examples": [{"en": "Do you speak English? – Yes, I do.", "tr": "İngilizce konuşur musun? – Evet."},
                  {"en": "Where do you live?", "tr": "Nerede yaşıyorsun?"},
                  {"en": "What do you do? – I'm a nurse.", "tr": "Ne iş yaparsın? – Hemşireyim."}],
     "turkishNote": "\"What do you do?\" sorusu \"Ne iş yapıyorsun?\" demektir, \"şu an ne yapıyorsun\" değil. Ayrıca soruda do unutulmamalı: \"Where you live?\" yanlış, \"Where do you live?\" doğru."},
    [
        gap("___ you like tea? – Yes, I do.", ["Do"], "Evet/hayır sorusu: Do + you + fiil?"),
        mc("\"Do you work on Saturdays?\" (Çalışmıyorsunuz.)", ["No, I don't.", "No, I'm not.", "No, I not work."], 0, "Do ile sorulan soruya: No, I don't."),
        order(["do", "Where", "live", "you", "?"], "Where do you live?", "Soru kelimesi + do + özne + fiil?", "Nerede yaşıyorsun?"),
        order(["time", "What", "you", "do", "get", "up", "?"], "What time do you get up?", "What time + do + you + fiil?", "Kaçta kalkarsın?"),
        mc("Hangisi doğru?", ["Where you work?", "Where do you work?", "Where are you work?"], 1, "do eksik olmamalı.", {0: "Soru için do gerekir.", 2: "are + work olmaz."}),
        mc("\"What do you do?\" ne demektir?", ["Şu an ne yapıyorsun?", "Ne iş yapıyorsun?", "Ne yapmak istiyorsun?"], 1, "Meslek sorusudur."),
        gap("Do they speak English? – Yes, they ___.", ["do"], "Kısa cevap: Yes, they do."),
        listen("Do you have lunch at work? – Yes, I do. I usually have lunch at one o'clock.", "Konuşan kaçta öğle yemeği yiyor?", ["12:00", "13:00", "14:00"], 1, "\"at one o'clock\" = 13:00"),
        typ("Soru yapın: \"You play tennis.\"", variants("Do you play tennis?"), "Do + you + play tennis?"),
        mc("\"What time do you finish work?\" sorusuna uygun cevap:", ["Yes, I do.", "At half past five.", "I'm a teacher."], 1, "What time → bir saat."),
    ],
    {"kind": "speaking", "task": speak("JAI ile tanışıyorsunuz. Ona günlük rutini hakkında 4 soru sorun.",
                                       "Where do you live? What time do you get up? Do you work? What do you do in the evening?",
                                       ["do ile soru kurdu", "Soru kelimeleri doğru", "Fiil yalın halde"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Her zaman, bazen, asla", "Bir şeyi ne sıklıkla yaptığımı söyleyebilirim.",
    {"kind": "dialogue", "title": "Sağlıklı yaşam anketi", "lines": [
        {"speaker": "Interviewer", "text": "How often do you do sport?"},
        {"speaker": "Can", "text": "I usually go to the gym on Mondays and Thursdays."},
        {"speaker": "Interviewer", "text": "Do you eat fast food?"},
        {"speaker": "Can", "text": "Sometimes, at the weekend."},
        {"speaker": "Interviewer", "text": "And do you smoke?"},
        {"speaker": "Can", "text": "No, never! And I always go to bed before midnight."}],
     "questions": [
        mc("When does Can go to the gym?", ["Every day", "On Mondays and Thursdays", "At the weekend"], 1, "\"on Mondays and Thursdays\""),
        mc("How often does Can eat fast food?", ["Never", "Sometimes", "Always"], 1, "\"Sometimes, at the weekend.\""),
     ]},
    {"explanation": "**Sıklık zarfları** (en sıktan en seyreğe):\n\n**always** (%100) → **usually** → **often** → **sometimes** → **never** (%0)\n\n**Yeri:** Eylem fiilinin **önüne**, to be'nin **arkasına** gelir.\n\n- I **always** have breakfast. (fiilden önce)\n- I'm **always** tired. (be'den sonra)\n\n**Zaman edatları:** **at** + saat (at 7), **in** + günün bölümü (in the morning), **on** + gün (on Monday, on Mondays).\n\nSıklık sormak için: **How often** do you ...?",
     "examples": [{"en": "I usually walk to work.", "tr": "Genellikle işe yürürüm."},
                  {"en": "She's never late.", "tr": "O hiç geç kalmaz."},
                  {"en": "We often eat out on Fridays.", "tr": "Cumaları sık sık dışarıda yeriz."}],
     "turkishNote": "never zaten olumsuzdur, yanına don't eklenmez: \"I don't never drink coffee\" yanlış, \"I never drink coffee\" doğru. Ayrıca \"in the morning\" ama \"at night\" denir."},
    [
        match([("always", "her zaman"), ("usually", "genellikle"), ("often", "sık sık"), ("sometimes", "bazen"), ("never", "asla")], "Sıklık zarflarını eşleştirin."),
        mc("Hangisi doğru?", ["I have always breakfast.", "I always have breakfast.", "Always I have breakfast."], 1, "Zarf, eylem fiilinin önüne gelir."),
        mc("Hangisi doğru?", ["I always am tired.", "I am always tired."], 1, "to be'den sonra gelir."),
        mc("Hangisi doğru?", ["I don't never eat meat.", "I never eat meat."], 1, "never zaten olumsuz, don't eklenmez.", {0: "İki olumsuzluk olmaz. never yeterli."}),
        gap("I go to the gym ___ Mondays.", ["on"], "Günlerden önce on."),
        gap("I study ___ the evening.", ["in"], "Günün bölümü → in the evening."),
        gap("I go to bed ___ eleven o'clock.", ["at"], "Saat → at."),
        order(["often", "How", "you", "do", "cook", "?"], "How often do you cook?", "How often + do + you + fiil?", "Ne sıklıkla yemek yaparsın?"),
        listen("I never eat breakfast, but I always drink a big cup of coffee at eight.", "Konuşan kahvaltı yapıyor mu?", ["Her zaman", "Bazen", "Hiç"], 2, "\"I never eat breakfast\""),
        typ("Zarfı doğru yere koyarak yazın: \"I walk to work.\" (usually)", variants("I usually walk to work."), "Zarf fiilden önce: I usually walk."),
    ],
    {"kind": "writing", "task": write("Bir haftanızı anlatın: her zaman, genellikle, bazen ve asla yaptığınız birer şey yazın.",
                                      "I always get up at seven. I usually go to work by bus. I sometimes cook dinner on Fridays. I never watch TV in the morning.",
                                      ["Sıklık zarfları doğru yerde", "never ile olumsuz fiil kullanılmadı", "at/in/on doğru"])},
)

u.test([
    gap("I ___ up at half past six.", ["get"], "get up = kalkmak"),
    mc("Hangisi doğru?", ["I go to home at five.", "I go home at five."], 1, "go home (to yok)."),
    mc("quarter past four:", ["3:45", "4:15", "4:45"], 1, "dördü çeyrek geçiyor = 4:15"),
    mc("twenty to eight:", ["7:40", "8:20", "7:20"], 0, "sekize yirmi var = 7:40"),
    gap("The film starts ___ nine.", ["at"], "Saat → at."),
    mc("Hangisi doğru?", ["I'm not like coffee.", "I don't like coffee.", "I no like coffee."], 1, "Eylem fiili → don't."),
    gap("We ___ work on Sundays.", ["don't", "do not"], "Olumsuz → don't."),
    order(["you", "do", "Where", "work", "?"], "Where do you work?", "Soru kelimesi + do + you + fiil?", "Nerede çalışıyorsun?"),
    mc("\"Do you speak French?\" (Hayır.)", ["No, I don't.", "No, I'm not.", "No, I doesn't."], 0, "No, I don't."),
    mc("Hangisi doğru?", ["I have usually lunch at one.", "I usually have lunch at one."], 1, "Zarf fiilden önce."),
    gap("I play football ___ Saturdays.", ["on"], "Gün → on."),
    listen("I usually get up at seven, but on Sundays I get up at ten.", "Konuşan pazar günleri kaçta kalkıyor?", ["7:00", "10:00", "11:00"], 1, "\"on Sundays I get up at ten\""),
    mc("\"What do you do?\" sorusuna uygun cevap:", ["I'm a teacher.", "I'm watching TV.", "Yes, I do."], 0, "Meslek sorusudur."),
    typ("Doğru yazın: \"I don't never eat fish.\"", variants("I never eat fish."), "never zaten olumsuz."),
    write("Bir gününüzü 5 cümleyle saatleriyle anlatın.",
          "I get up at seven o'clock. I have breakfast at half past seven. I start work at nine. I usually go home at six. I go to bed at eleven.",
          ["Rutin fiilleri doğru", "Saatler ve at doğru", "Sıklık zarfı doğru yerde", "Fiiller yalın (I + fiil)"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

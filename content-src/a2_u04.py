"""A2 Ünite 4: Planlar."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("A2", 4, "Planlar", "Plans",
         "Gelecek planlarımı ve niyetlerimi anlatabilir, kesinleşmiş randevularımı söyleyebilir ve biriyle birlikte plan yapabilirim.",
         ["be going to: niyet ve plan", "be going to: olumsuz ve soru", "gelecek için present continuous (kesin planlar)", "be going to: kanıta dayalı tahmin", "gelecek zaman ifadeleri"],
         ["boş zaman etkinlikleri", "hedefler ve kararlar", "takvim ve randevular"],
         {"title": "Ajanda", "durationMinutes": 45,
          "goal": "Her öğrenciye gelecek haftanın dolu bir ajanda sayfası verilir. Öğrenciler What are you doing on...? / Are you free on...? sorularıyla, herkesin boş olduğu bir zamanı bulup ortak bir etkinlik planlamaya çalışır. Sonra herkes yeni yıl için 3 hedefini 'going to' ile paylaşır."})

u.vocab([
    ("plan", "plan; planlamak", "What are your plans for the summer?", "Yaz için planların neler?", None),
    ("going to", "-ecek (niyet)", "I'm going to learn to drive.", "Araba kullanmayı öğreneceğim.", "be + going to + yalın fiil"),
    ("tomorrow", "yarın", "I'm meeting Ali tomorrow.", "Yarın Ali'yle buluşuyorum.", None),
    ("the day after tomorrow", "öbür gün", "We're leaving the day after tomorrow.", "Öbür gün yola çıkıyoruz.", None),
    ("next week", "gelecek hafta", "I'm starting a new job next week.", "Gelecek hafta yeni bir işe başlıyorum.", "next month, next year (the yok)"),
    ("this weekend", "bu hafta sonu", "What are you doing this weekend?", "Bu hafta sonu ne yapıyorsun?", None),
    ("in two weeks", "iki hafta sonra", "My exam is in two weeks.", "Sınavım iki hafta sonra.", "in + süre (gelecek)"),
    ("save money", "para biriktirmek", "I'm going to save money for a car.", "Araba için para biriktireceğim.", None),
    ("give up", "bırakmak (alışkanlık)", "My dad is going to give up smoking.", "Babam sigarayı bırakacak.", None),
    ("take up", "başlamak (hobi)", "I'm going to take up yoga.", "Yogaya başlayacağım.", None),
    ("lose weight", "kilo vermek", "She wants to lose weight before the wedding.", "Düğünden önce kilo vermek istiyor.", None),
    ("get fit", "forma girmek", "I'm going to the gym to get fit.", "Forma girmek için spor salonuna gidiyorum.", None),
    ("learn to", "... öğrenmek", "We're going to learn to dance salsa.", "Salsa dans etmeyi öğreneceğiz.", "learn to + fiil"),
    ("appointment", "randevu", "I have a dentist's appointment at three.", "Saat üçte dişçi randevum var.", None),
    ("diary", "ajanda", "Let me check my diary.", "Ajandama bakayım.", "Amerikan: calendar / planner."),
    ("free", "boş, müsait", "Are you free on Friday evening?", "Cuma akşamı müsait misin?", None),
    ("busy", "meşgul", "Sorry, I'm busy on Saturday.", "Kusura bakma, cumartesi meşgulüm.", None),
    ("barbecue", "mangal", "We're having a barbecue on Sunday.", "Pazar günü mangal yapıyoruz.", "have a barbecue"),
    ("exhibition", "sergi", "There's a new photo exhibition at the museum.", "Müzede yeni bir fotoğraf sergisi var.", None),
    ("festival", "festival", "Are you going to the jazz festival?", "Caz festivaline gidiyor musun?", None),
    ("resolution", "(yeni yıl) kararı", "My New Year's resolution is to read more.", "Yeni yıl kararım daha çok okumak.", None),
    ("probably", "muhtemelen", "I'm probably going to stay at home.", "Muhtemelen evde kalacağım.", None),
    ("definitely", "kesinlikle", "I'm definitely going to come!", "Kesinlikle geleceğim!", None),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Niyetlerim", "be going to ile gelecek niyetlerimi ve planlarımı anlatabilirim.",
    {"kind": "text", "title": "Yeni yıl kararları", "body": "We asked three people about their plans for next year.\n\nHakan, 34: \"I'm going to give up smoking. I tried last year, but this time I'm going to do it!\"\n\nZehra, 19: \"I'm going to take up the guitar. My friends and I are going to start a band.\"\n\nMr and Mrs Aslan, 65 and 63: \"We're both retired now, so we're going to travel. First we're going to visit our son in Canada.\"",
     "questions": [
        mc("What is Zehra going to do?", ["Give up smoking", "Learn the guitar", "Travel to Canada"], 1, "\"I'm going to take up the guitar.\""),
        mc("Why are Mr and Mrs Aslan going to visit Canada?", ["Their son lives there.", "They want to work there.", "It's cheap."], 0, "\"visit our son in Canada\""),
     ]},
    {"explanation": "**be going to** + yalın fiil, önceden karar verilmiş **niyet ve planları** anlatır.\n\n| | |\n|---|---|\n| I **am** (I'm) | going to + fiil |\n| He / She / It **is** ('s) | going to + fiil |\n| You / We / They **are** ('re) | going to + fiil |\n\n- I**'m going to** learn Spanish.\n- She**'s going to** move to Berlin.\n- We**'re going to** buy a house.\n\n**go** fiiliyle: I'm going to go to the cinema. Günlük dilde sık sık kısaca: I'm going to the cinema.\n\n**Zaman ifadeleri:** tomorrow, next week/month/year, this weekend, in two days, one day (bir gün)",
     "examples": [{"en": "I'm going to save money for a new car.", "tr": "Yeni bir araba için para biriktireceğim."},
                  {"en": "They're going to get married next year.", "tr": "Gelecek yıl evlenecekler."},
                  {"en": "One day, I'm going to visit Japan.", "tr": "Bir gün Japonya'yı ziyaret edeceğim."}],
     "turkishNote": "Türkçede \"-ecek\" eki hem plan hem tahmin için kullanılır. İngilizcede önceden karar verilmiş niyetler için going to, anlık kararlar ve tahminler için will (9. ünite) kullanılır. be fiili unutulmamalı: \"I going to\" yanlıştır, \"I'm going to\" doğrudur."},
    [
        mc("Hangisi doğru?", ["I going to study.", "I'm going to study.", "I'm going study."], 1, "be + going to + fiil."),
        mc("Hangisi doğru?", ["She's going to moves.", "She's going to move.", "She going to move."], 1, "going to + yalın fiil."),
        gap("We ___ going to buy a new car. (are)", ["are", "'re"], "we → are."),
        gap("He's going ___ give up smoking.", ["to"], "going to."),
        gap("I'm going to ___ up yoga. (başlamak)", ["take"], "take up = hobiye başlamak."),
        mc("\"Kilo vermek\"", ["lose weight", "get weight", "give up weight"], 0, "lose weight."),
        order(["going", "I'm", "to", "learn", "to", "drive", "next", "year"], "I'm going to learn to drive next year.", "be going to + learn to + fiil.", "Gelecek yıl araba kullanmayı öğreneceğim."),
        listen("This summer I'm going to work in a hotel in Bodrum. I'm going to save money for university.", "Neden otelde çalışacak?", ["Tatil için", "Üniversite için para biriktirmek için", "İngilizce öğrenmek için"], 1, "\"save money for university\""),
        typ("İngilizce yazın: \"Bir gün Japonya'yı ziyaret edeceğim.\"", variants("One day, I'm going to visit Japan.", "One day I'm going to visit Japan.", "One day, I am going to visit Japan.", "One day I am going to visit Japan.", "I'm going to visit Japan one day."), "One day + I'm going to visit Japan."),
        match([("give up", "smoking"), ("take up", "the guitar"), ("save", "money"), ("get", "fit"), ("lose", "weight")], "Kalıpları eşleştirin."),
    ],
    {"kind": "speaking", "task": speak("Gelecek yıl için 3 yeni yıl kararınızı ve gelecekte bir gün yapmak istediğiniz bir şeyi going to ile anlatın.",
                                       "Next year I'm going to get fit. I'm going to go to the gym three times a week. I'm also going to save money and read more books. One day, I'm going to live by the sea.",
                                       ["be + going to + yalın fiil", "Zaman ifadeleri", "Kalıplar (take up, give up...)"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "Ne yapacaksın?", "going to ile soru sorup olumsuz cümle kurabilirim.",
    {"kind": "dialogue", "title": "Mezuniyetten sonra", "lines": [
        {"speaker": "Aunt", "text": "Congratulations on your graduation! So, what are you going to do now?"},
        {"speaker": "Deniz", "text": "Thanks! I'm not going to look for a job immediately."},
        {"speaker": "Aunt", "text": "Really? Are you going to travel?"},
        {"speaker": "Deniz", "text": "Yes, I am. I'm going to spend three months in South America."},
        {"speaker": "Aunt", "text": "Wow! Where are you going to stay?"},
        {"speaker": "Deniz", "text": "In hostels, mostly. I'm not going to spend much money!"}],
     "questions": [
        mc("Is Deniz going to look for a job immediately?", ["Yes", "No"], 1, "\"I'm not going to look for a job immediately.\""),
        mc("Where is Deniz going to stay?", ["In hotels", "In hostels", "With family"], 1, "\"In hostels, mostly.\""),
     ]},
    {"explanation": "**Olumsuz:** be + **not** + going to + fiil\n\n- I**'m not going to** buy it.\n- She **isn't going to** come.\n- They **aren't going to** move.\n\n**Soru:** Am / Is / Are + özne + going to + fiil?\n\n- **Are** you **going to** travel? – Yes, I **am**. / No, I**'m not**.\n- **Is** he **going to** call? – Yes, he **is**. / No, he **isn't**.\n\n**Bilgi sorusu:**\n\n- **What are** you **going to** do?\n- **Where is** she **going to** live?\n- **When are** they **going to** arrive?",
     "examples": [{"en": "What are you going to wear to the party?", "tr": "Partiye ne giyeceksin?"},
                  {"en": "We aren't going to stay long.", "tr": "Uzun kalmayacağız."},
                  {"en": "Is it going to be expensive?", "tr": "Pahalı olacak mı?"}],
     "turkishNote": "\"Ne yapacaksın?\" = What are you going to do? Kısa cevapta going to tekrar edilmez: \"Are you going to come? – Yes, I am.\" Soru do/does ile kurulmaz: \"Do you going to...?\" yanlıştır."},
    [
        mc("Hangisi doğru?", ["Do you going to travel?", "Are you going to travel?", "You are going to travel?"], 1, "Are + you + going to?"),
        mc("\"Is she going to call?\" (Hayır.)", ["No, she isn't.", "No, she doesn't.", "No, she won't going."], 0, "No, she isn't."),
        gap("I'm ___ going to tell anyone. (değil)", ["not"], "I'm not going to."),
        gap("They ___ going to move. They like their flat. (değil)", ["aren't", "are not", "'re not"], "they → aren't."),
        gap("What ___ you going to do this weekend?", ["are"], "you → are."),
        gap("Where is he going to ___? (live)", ["live"], "going to + yalın fiil."),
        order(["you", "When", "are", "going", "to", "arrive", "?"], "When are you going to arrive?", "Soru kelimesi + are + you + going to + fiil?", "Ne zaman varacaksın?"),
        listen("Are you going to cook tonight? – No, I'm not. I'm too tired. We're going to order a pizza.", "Bu akşam ne yapacaklar?", ["Yemek pişirecekler", "Pizza sipariş edecekler", "Dışarıda yiyecekler"], 1, "\"We're going to order a pizza.\""),
        typ("Soru yapın: \"She's going to study medicine.\" (What?)", variants("What is she going to study?", "What's she going to study?"), "What + is she + going to study?"),
        typ("İngilizce yazın: \"Partiye ne giyeceksin?\"", variants("What are you going to wear to the party?", "What are you going to wear for the party?"), "What are you going to wear + to the party?"),
    ],
    {"kind": "speaking", "task": speak("JAI yakında büyük bir değişiklik yapacak (taşınma, yeni iş, uzun bir yolculuk). Ona going to ile en az 5 soru sorun, sonra kendi bir planınızı olumsuz bir cümle de ekleyerek anlatın.",
                                       "Where are you going to live? When are you going to move? Are you going to sell your car? What are you going to do there? Is it going to be expensive? ... I'm going to change my job, but I'm not going to move.",
                                       ["Soru düzeni doğru", "Kısa cevaplar", "Olumsuz cümle doğru"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "Ajandam dolu", "Kesinleşmiş gelecek planlarımı present continuous ile anlatabilirim.",
    {"kind": "dialogue", "title": "Asistanla telefon", "lines": [
        {"speaker": "Ms Tan", "text": "What's in my diary for tomorrow, Burak?"},
        {"speaker": "Burak", "text": "You're meeting the new clients at nine. Then you're having lunch with Mr Kılıç at one."},
        {"speaker": "Ms Tan", "text": "And in the afternoon?"},
        {"speaker": "Burak", "text": "You're flying to Ankara at five. The car is picking you up at three thirty."},
        {"speaker": "Ms Tan", "text": "Am I staying at the usual hotel?"},
        {"speaker": "Burak", "text": "Yes, you are. And you're coming back on Friday morning."}],
     "questions": [
        mc("Who is Ms Tan having lunch with?", ["The new clients", "Mr Kılıç", "Burak"], 1, "\"you're having lunch with Mr Kılıç at one\""),
        mc("What time is the car picking her up?", ["At 3:30", "At 5:00", "At 1:00"], 0, "\"at three thirty\""),
     ]},
    {"explanation": "**Present continuous** gelecek için de kullanılır: zamanı ve yeri **belli, ayarlanmış** planlar (randevu, bilet, rezervasyon).\n\n- I**'m meeting** Ali at six tomorrow.\n- We**'re flying** to Rome on Friday.\n- What **are** you **doing** this weekend?\n\nBu kullanımda genellikle bir **gelecek zaman ifadesi** vardır; yoksa cümle \"şu an\" anlamına gelir.\n\n**going to ile farkı:**\n\n| going to | present continuous |\n|---|---|\n| niyet, karar | ayarlanmış plan |\n| I'm going to visit Paris one day. | I'm visiting Paris next week. (Bilet alındı.) |\n\nÇoğu durumda ikisi de doğrudur ve anlam çok az değişir.",
     "examples": [{"en": "I'm seeing the doctor at four.", "tr": "Saat dörtte doktora gidiyorum."},
                  {"en": "Are you doing anything on Saturday?", "tr": "Cumartesi bir şey yapıyor musun?"},
                  {"en": "My parents are coming for dinner tonight.", "tr": "Annemlerle babam bu akşam yemeğe geliyor."}],
     "turkishNote": "Türkçede de \"Yarın Ali'yle buluşuyorum\" deriz; İngilizcede de aynı mantık vardır: I'm meeting Ali tomorrow. Bu benzerlik Türkçe konuşanlar için büyük bir avantajdır. Ama tahminler için (Yarın yağmur yağıyor) present continuous kullanılmaz: It's going to rain tomorrow."},
    [
        mc("Bilet alındı, tarih belli:", ["I'm flying to Izmir on Monday.", "I fly to Izmir on Monday."], 0, "Ayarlanmış plan → present continuous."),
        mc("\"Bu hafta sonu ne yapıyorsun?\"", ["What do you do this weekend?", "What are you doing this weekend?"], 1, "Plan → present continuous."),
        gap("I'm ___ the dentist at three tomorrow. (see)", ["seeing"], "see → seeing."),
        gap("We ___ having a barbecue on Sunday. Can you come?", ["are", "'re"], "we → are."),
        gap("Are you doing anything ___ Saturday?", ["on"], "Günlerle on."),
        mc("Hangisi tahmindir (present continuous kullanılmaz)?", ["It's going to rain tomorrow.", "I'm meeting Ece tomorrow."], 0, "Tahmin → going to."),
        order(["coming", "My", "parents", "are", "for", "dinner", "tonight"], "My parents are coming for dinner tonight.", "Özne + are + -ing + zaman.", "Annemlerle babam bu akşam yemeğe geliyor."),
        listen("I can't come on Thursday. I'm working late, and on Friday I'm visiting my grandmother in Bursa.", "Cuma günü ne yapıyor?", ["Geç saate kadar çalışıyor", "Büyükannesini ziyaret ediyor", "Bursa'ya taşınıyor"], 1, "\"on Friday I'm visiting my grandmother\""),
        typ("İngilizce yazın: \"Yarın saat altıda Ali'yle buluşuyorum.\"", variants("I'm meeting Ali at six tomorrow.", "I'm meeting Ali tomorrow at six.", "I am meeting Ali at six tomorrow.", "Tomorrow I'm meeting Ali at six.", "I'm meeting Ali at 6 tomorrow."), "I'm meeting Ali + at six tomorrow."),
        mc("\"I'm meeting Ali.\" (zaman ifadesi yok) Anlamı büyük ihtimalle:", ["Şu an Ali'yle buluşuyorum / görüşüyorum.", "Yarın Ali'yle buluşacağım."], 0, "Zaman ifadesi yoksa → şu an."),
    ],
    {"kind": "writing", "task": write("Gelecek haftanın ajandasını yazın: en az 5 ayarlanmış plan (gün, saat, kiminle). Present continuous kullanın.",
                                      "On Monday I'm starting a new course at 7 pm. On Tuesday I'm having lunch with my boss. On Wednesday I'm seeing the dentist at 4. On Friday evening we're going to a concert. On Saturday my cousins are coming to stay.",
                                      ["Present continuous doğru", "Gün ve saat ifadeleri (on, at)", "Ayarlanmış planlar"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Olacak gibi görünüyor", "Gördüğüm kanıta dayanarak going to ile tahmin yapabilirim.",
    {"kind": "dialogue", "title": "Piknikte", "lines": [
        {"speaker": "Sibel", "text": "Look at those black clouds. It's going to rain!"},
        {"speaker": "Mert", "text": "Oh no. Quick, let's put the food in the car."},
        {"speaker": "Sibel", "text": "Careful! That glass is going to fall!"},
        {"speaker": "Mert", "text": "Got it. And look at the dog, it's going to eat our sandwiches!"},
        {"speaker": "Sibel", "text": "Ha ha! This isn't going to be a relaxing picnic."}],
     "questions": [
        mc("Why does Sibel think it's going to rain?", ["The weather forecast", "There are black clouds", "It's cold"], 1, "\"Look at those black clouds.\""),
        mc("What is the dog going to do?", ["Run away", "Eat the sandwiches", "Sleep"], 1, "\"it's going to eat our sandwiches!\""),
     ]},
    {"explanation": "**going to** ile bir şeyin olacağını **şu anda gördüğümüz kanıta** dayanarak tahmin ederiz.\n\n- Look at the clouds! It**'s going to** rain. (Bulutları görüyorum.)\n- Be careful! You**'re going to** fall! (Merdivende sallandığını görüyorum.)\n- She's very tired. She**'s going to** fall asleep.\n- We're late. We**'re going to** miss the train!\n\n**Karşılaştırın:**\n\n| Plan / niyet | Kanıta dayalı tahmin |\n|---|---|\n| I'm going to paint my room. | That ladder is old. It's going to break! |",
     "examples": [{"en": "Watch out! That car is going to hit you!", "tr": "Dikkat et! O araba sana çarpacak!"},
                  {"en": "It's 8:55 and the film starts at 9. We're going to be late.", "tr": "Saat 8:55, film 9'da başlıyor. Geç kalacağız."},
                  {"en": "The team is playing really well. They're going to win.", "tr": "Takım çok iyi oynuyor. Kazanacaklar."}],
     "turkishNote": "Türkçede \"Yağmur yağacak\" ve \"Düşeceksin!\" cümleleri kanıta dayalı tahmin içerir; İngilizcede bunlar going to ile söylenir. Uyarı ifadeleri: Look out! / Watch out! / Be careful! / Careful!"},
    [
        mc("Gökyüzü kapkara:", ["It's going to rain.", "It rains."], 0, "Kanıta dayalı tahmin."),
        mc("Bu cümle hangisi? \"I'm going to buy a car next year.\"", ["Plan / niyet", "Kanıta dayalı tahmin"], 0, "Karar verilmiş niyet."),
        mc("Bu cümle hangisi? \"Look at that ice! You're going to fall.\"", ["Plan / niyet", "Kanıta dayalı tahmin"], 1, "Buzu görüyor → tahmin."),
        gap("Watch out! That glass ___ going to fall!", ["is", "'s"], "glass → is."),
        gap("Hurry up! We're going to ___ the bus! (kaçırmak)", ["miss"], "miss the bus."),
        gap("The baby is yawning. She's going to ___ asleep.", ["fall"], "fall asleep = uykuya dalmak."),
        order(["going", "It's", "to", "be", "a", "hot", "day"], "It's going to be a hot day.", "It's going to be + sıfat + isim.", "Sıcak bir gün olacak."),
        listen("Oh no, the score is three-nil and there are only two minutes left. We're going to lose.", "Konuşan neden kaybedeceklerini düşünüyor?", ["Takım kötü oynuyor", "Skor 3-0 ve 2 dakika kaldı", "Hava kötü"], 1, "\"three-nil and there are only two minutes left\""),
        typ("İngilizce yazın: \"Dikkat et! Düşeceksin!\"", variants("Be careful! You're going to fall!", "Careful! You're going to fall!", "Be careful! You are going to fall!", "Watch out! You're going to fall!"), "Be careful! + You're going to fall!"),
        match([("Watch out!", "Dikkat et!"), ("Hurry up!", "Acele et!"), ("Careful!", "Dikkat!"), ("Look!", "Bak!")], "Uyarı ifadelerini eşleştirin."),
    ],
    {"kind": "speaking", "task": speak("JAI size bazı durumlar anlatacak (ör. \"Saat 8:58, toplantı 9'da ve hâlâ otobüstesiniz\"). Her durum için going to ile bir tahmin söyleyin.",
                                       "I'm going to be late for the meeting. ... It's going to snow. ... The battery is going to die. ... He's going to fall off the chair!",
                                       ["going to ile tahmin", "be + going to doğru", "Uyarı ifadeleri"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Birlikte plan yapmak", "Birinin müsaitliğini sorup birlikte bir etkinlik planlayabilirim.",
    {"kind": "dialogue", "title": "Hafta sonu planı", "lines": [
        {"speaker": "Aslı", "text": "Hi, Kaan! Are you free this weekend?"},
        {"speaker": "Kaan", "text": "I'm working on Saturday morning, but I'm free after two. Why?"},
        {"speaker": "Aslı", "text": "There's a food festival in the park. I'm going to go with Melis. Do you want to come?"},
        {"speaker": "Kaan", "text": "Sounds great! What time are you meeting?"},
        {"speaker": "Aslı", "text": "At three, at the main gate."},
        {"speaker": "Kaan", "text": "Perfect. I'm definitely going to come. See you there!"}],
     "questions": [
        mc("When is Kaan free?", ["Saturday morning", "After two on Saturday", "Sunday"], 1, "\"I'm free after two\""),
        mc("Where are they meeting?", ["At the main gate", "At Melis's house", "At a café"], 0, "\"At three, at the main gate.\""),
     ]},
    {"explanation": "**Müsaitlik sormak:**\n\n- **Are you free** on Saturday / this evening?\n- **What are you doing** on Friday?\n- **Are you doing anything** this weekend?\n\n**Öneri:**\n\n- Do you want to + fiil?\n- **How about** + -ing / isim? → How about going to the festival?\n- **Why don't we** + fiil? → Why don't we meet at three?\n\n**Ayarlamak:** What time shall we meet? / Where shall we meet? / Let's meet at...\n\n**Kesinlik derecesi:**\n\n- I'm **definitely** going to come. (kesin)\n- I'm **probably** going to come. (muhtemelen)\n- I'm **not sure** yet. (henüz emin değilim)\n\nprobably / definitely olumlu cümlede **be ile going to arasına**, olumsuzda **isn't/aren't'tan önce** gelir: He **probably** isn't going to come.",
     "examples": [{"en": "Are you free on Sunday afternoon?", "tr": "Pazar öğleden sonra müsait misin?"},
                  {"en": "How about going to the exhibition?", "tr": "Sergiye gitmeye ne dersin?"},
                  {"en": "What time shall we meet?", "tr": "Saat kaçta buluşalım?"}],
     "turkishNote": "\"How about\"tan sonra fiil -ing alır: How about going (How about go değil). \"Shall we...?\" kibar bir öneri sorusudur ve \"-elim mi?\" anlamı taşır: Shall we meet at six? = Altıda buluşalım mı?"},
    [
        mc("Hangisi doğru?", ["How about go to the cinema?", "How about going to the cinema?"], 1, "How about + -ing."),
        mc("\"Saat kaçta buluşalım?\"", ["What time shall we meet?", "What time we meet?", "When we shall meet?"], 0, "What time shall we + fiil?"),
        gap("Are you ___ on Friday evening? (müsait)", ["free"], "Are you free?"),
        gap("Why don't we ___ at the café? (meet)", ["meet"], "Why don't we + yalın fiil."),
        gap("I'm ___ going to come. I'm not 100% sure. (muhtemelen)", ["probably"], "probably = muhtemelen."),
        mc("Hangisi doğru?", ["I'm going definitely to come.", "I'm definitely going to come."], 1, "definitely be'den sonra, going'den önce."),
        order(["you", "Are", "doing", "anything", "this", "weekend", "?"], "Are you doing anything this weekend?", "Are you doing anything + zaman?", "Bu hafta sonu bir şey yapıyor musun?"),
        listen("I'm busy on Saturday, but I'm free on Sunday. How about having breakfast together at ten?", "Konuşan ne öneriyor?", ["Cumartesi akşam yemeği", "Pazar saat onda kahvaltı", "Pazar öğle yemeği"], 1, "\"How about having breakfast together at ten?\" (Sunday)"),
        typ("İngilizce yazın: \"Sergiye gitmeye ne dersin?\"", variants("How about going to the exhibition?", "What about going to the exhibition?"), "How about + going to the exhibition?"),
        match([("Are you free", "on Saturday?"), ("How about", "going to a concert?"), ("Why don't we", "meet at six?"), ("What time", "shall we meet?")], "Cümleleri tamamlayın."),
    ],
    {"kind": "speaking", "task": speak("JAI ile bu hafta sonu için bir buluşma ayarlayın: müsaitlik sorun, JAI'nin dolu olduğu zamanları dinleyin, bir etkinlik önerin, yer ve saat belirleyin.",
                                       "Are you free on Saturday? Oh, you're working. What are you doing on Sunday? Great. How about going to the food festival? What time shall we meet? Let's meet at the main gate at four.",
                                       ["Müsaitlik soruları", "How about / Why don't we", "Present continuous ve going to doğru", "Yer ve saat ayarlandı"])},
)

u.test([
    mc("Hangisi doğru?", ["I going to travel.", "I'm going to travel."], 1, "be + going to"),
    gap("She's going to ___ up the piano. (başlamak)", ["take"], "take up"),
    gap("We ___ going to sell our car. (değil)", ["aren't", "are not", "'re not"], "Olumsuz"),
    mc("Hangisi doğru?", ["Do you going to come?", "Are you going to come?"], 1, "Are you going to...?"),
    mc("\"Is he going to stay?\" (Hayır.)", ["No, he isn't.", "No, he doesn't."], 0, "No, he isn't."),
    gap("What ___ you going to do after university?", ["are"], "are"),
    mc("Uçak bileti alındı:", ["I'm flying to Van on Monday.", "I fly to Van on Monday."], 0, "Ayarlanmış plan"),
    gap("I'm ___ my grandma on Sunday. (visit)", ["visiting"], "Present continuous gelecek"),
    mc("Kara bulutlar var:", ["It's raining tomorrow.", "It's going to rain."], 1, "Kanıta dayalı tahmin"),
    gap("Hurry up! We're going to ___ late!", ["be"], "be late"),
    mc("Hangisi doğru?", ["How about meet at six?", "How about meeting at six?"], 1, "How about + -ing"),
    gap("Are you ___ on Saturday evening? (müsait)", ["free"], "free"),
    listen("I'm not going to come to the party. I'm having dinner with my husband's family that evening.", "Neden partiye gelmiyor?", ["Hasta", "Eşinin ailesiyle yemekte", "Çalışıyor"], 1, "\"I'm having dinner with my husband's family\""),
    typ("İngilizce yazın: \"Gelecek yıl sigarayı bırakacağım.\"", variants("I'm going to give up smoking next year.", "Next year I'm going to give up smoking.", "Next year, I'm going to give up smoking.", "I am going to give up smoking next year."), "be going to + give up smoking + next year"),
    write("Bir arkadaşınıza mesaj yazın: bu hafta sonu planlarınızı anlatın (en az 2 ayarlanmış plan, present continuous), gelecek ay için bir niyetinizi söyleyin (going to) ve onu bir etkinliğe davet edin (60–80 kelime).",
          "Hi Selin! This weekend is really busy. On Saturday morning I'm having a driving lesson, and in the afternoon I'm helping my sister with her new flat. But I'm free on Sunday! There's a jazz festival in the park. How about going together? We can meet at the gate at four. Also, next month I'm going to start a cooking course. Do you want to join me?",
          ["Present continuous (ayarlanmış planlar)", "going to (niyet)", "Davet / öneri ifadeleri", "Zaman ifadeleri doğru"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

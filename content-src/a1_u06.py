"""A1 Ünite 6: İş hayatı."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("A1", 6, "İş hayatı", "Work Life",
         "Başkalarının mesleğini ve günlük rutinini anlatabilir, onlara işlerini sorabilirim.",
         ["present simple (he/she/it): -s / -es / -ies", "doesn't", "Does...? / What does...?"],
         ["meslekler", "iş yerleri"],
         {"title": "Meslek tahmini", "durationMinutes": 45,
          "goal": "Bir öğrenci bir meslek seçer, diğerleri yalnızca evet/hayır sorularıyla tahmin eder (Does he work outside? Does she wear a uniform?)."})

u.vocab([
    ("doctor", "doktor", "She's a doctor at a hospital.", "O bir hastanede doktor.", None),
    ("nurse", "hemşire", "My brother is a nurse.", "Ağabeyim hemşire.", "Erkek hemşire de nurse'tür."),
    ("teacher", "öğretmen", "He's a maths teacher.", "O bir matematik öğretmeni.", None),
    ("engineer", "mühendis", "She's an engineer.", "O bir mühendis.", "Ünlüyle başladığı için an engineer."),
    ("lawyer", "avukat", "Her husband is a lawyer.", "Onun kocası avukat.", None),
    ("chef", "aşçı, şef", "He's a chef in a hotel.", "O bir otelde aşçı.", None),
    ("waiter", "garson", "The waiter brings the menu.", "Garson menüyü getirir.", "Kadın garson: waitress."),
    ("driver", "şoför, sürücü", "My uncle is a taxi driver.", "Amcam taksi şoförü.", None),
    ("police officer", "polis memuru", "She's a police officer.", "O bir polis memuru.", None),
    ("shop assistant", "satış danışmanı", "He's a shop assistant.", "O bir satış danışmanı.", None),
    ("farmer", "çiftçi", "Farmers get up very early.", "Çiftçiler çok erken kalkar.", None),
    ("hospital", "hastane", "Nurses work in a hospital.", "Hemşireler hastanede çalışır.", None),
    ("office", "ofis", "I work in an office.", "Bir ofiste çalışıyorum.", None),
    ("factory", "fabrika", "My father works in a factory.", "Babam bir fabrikada çalışıyor.", None),
    ("company", "şirket", "She works for a big company.", "O büyük bir şirkette çalışıyor.", "work for + şirket"),
    ("job", "iş, meslek", "I love my job.", "İşimi seviyorum.", None),
    ("uniform", "üniforma", "Police officers wear a uniform.", "Polisler üniforma giyer.", "a uniform: u \"yu\" diye okunur."),
    ("help", "yardım etmek", "Nurses help doctors.", "Hemşireler doktorlara yardım eder.", None),
    ("wear", "giymek, takmak", "She wears glasses.", "O gözlük takar.", None),
    ("earn", "kazanmak (para)", "He earns a lot of money.", "Çok para kazanır.", None),
    ("busy", "meşgul, yoğun", "Doctors are very busy.", "Doktorlar çok meşguldür.", None),
    ("outside", "dışarıda", "Farmers work outside.", "Çiftçiler dışarıda çalışır.", None),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Meslekler", "İnsanların mesleğini söyleyebilir ve sorabilirim.",
    {"kind": "dialogue", "title": "Düğünde", "lines": [
        {"speaker": "Tom", "text": "Who's that man next to your sister?"},
        {"speaker": "Elif", "text": "That's her husband, Kerem. He's an engineer."},
        {"speaker": "Tom", "text": "And what does your sister do?"},
        {"speaker": "Elif", "text": "She's a doctor. And my parents are teachers."},
        {"speaker": "Tom", "text": "Wow, a family of smart people!"}],
     "questions": [
        mc("What is Kerem's job?", ["Doctor", "Engineer", "Teacher"], 1, "\"He's an engineer.\""),
        mc("What do Elif's parents do?", ["They're doctors.", "They're teachers.", "They're engineers."], 1, "\"my parents are teachers\""),
     ]},
    {"explanation": "Meslek söylerken tekil isimden önce **a/an** gelir:\n\n- He's **a** doctor.\n- She's **an** engineer.\n- They're teachers. (çoğulda a/an yok)\n\nMeslek sormak için: **What do you do?** / **What does he/she do?** / **What's your job?**",
     "examples": [{"en": "I'm a nurse.", "tr": "Ben hemşireyim."},
                  {"en": "What does your father do? – He's a lawyer.", "tr": "Baban ne iş yapıyor? – Avukat."},
                  {"en": "They're police officers.", "tr": "Onlar polis memuru."}],
     "turkishNote": "Türkçede \"O doktor\" deriz, İngilizcede \"a\" zorunludur: He's a doctor. \"He's doctor\" yanlıştır. Çoğulda ise a/an kullanılmaz: They're doctors."},
    [
        match([("doctor", "doktor"), ("lawyer", "avukat"), ("chef", "aşçı"), ("engineer", "mühendis"), ("farmer", "çiftçi")], "Meslekleri eşleştirin."),
        gap("She's ___ engineer.", ["an"], "engineer ünlüyle başlar → an."),
        gap("He's ___ taxi driver.", ["a"], "taxi ünsüzle başlar → a."),
        mc("Hangisi doğru?", ["He's doctor.", "He's a doctor.", "He a doctor."], 1, "Meslekten önce a/an.", {0: "a eksik: He's a doctor."}),
        mc("Hangisi doğru?", ["They're a teachers.", "They're teachers."], 1, "Çoğulda a/an yok."),
        mc("Hastanede çalışan, doktorlara yardım eden kişi:", ["nurse", "waiter", "lawyer"], 0, "nurse = hemşire."),
        order(["do", "What", "you", "do", "?"], "What do you do?", "Meslek sorusu.", "Ne iş yapıyorsun?"),
        listen("My mother is a chef and my father is a police officer.", "Konuşanın babası ne iş yapıyor?", ["Aşçı", "Polis", "Doktor"], 1, "\"my father is a police officer\""),
        typ("İngilizce yazın: \"Ben bir öğretmenim.\"", variants("I'm a teacher."), "I'm + a + teacher."),
        mc("Restoranda yemek getiren kişi:", ["chef", "waiter", "driver"], 1, "waiter = garson. chef yemeği pişirir."),
    ],
    {"kind": "speaking", "task": speak("Kendi mesleğinizi ve ailenizden iki kişinin mesleğini söyleyin.",
                                       "I'm an engineer. My mother is a nurse and my brother is a student.",
                                       ["a/an doğru", "Meslek kelimeleri doğru", "his/her ya da 's kullandı"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "O çalışır", "he/she/it ile present simple'da fiile -s ekleyebilirim.",
    {"kind": "dialogue", "title": "Bir hemşirenin günü", "lines": [
        {"speaker": "Narrator", "text": "This is Ayşe. She's a nurse."},
        {"speaker": "Narrator", "text": "She works at a big hospital in Ankara."},
        {"speaker": "Narrator", "text": "She gets up at five and she starts work at seven."},
        {"speaker": "Narrator", "text": "She wears a blue uniform. She helps doctors and she watches the patients."},
        {"speaker": "Narrator", "text": "She finishes at three and she goes home by bus."}],
     "questions": [
        mc("What time does Ayşe start work?", ["5:00", "7:00", "3:00"], 1, "\"she starts work at seven\""),
        mc("How does Ayşe go home?", ["By car", "By bus", "On foot"], 1, "\"she goes home by bus\""),
     ]},
    {"explanation": "**he, she, it** ile present simple'da fiile **-s** eklenir:\n\n- I work → she work**s**\n\n| Kural | Örnek |\n|---|---|\n| çoğu fiil: **-s** | work → works, start → starts |\n| -s, -sh, -ch, -x, -o ile bitenler: **-es** | watch → watch**es**, go → go**es**, do → do**es**, finish → finish**es** |\n| ünsüz + y: **-ies** | study → stud**ies**, fly → fl**ies** |\n| düzensiz | have → **has** |\n\nünlü + y yalnızca -s alır: play → plays.",
     "examples": [{"en": "He lives in London.", "tr": "O Londra'da yaşıyor."},
                  {"en": "She watches TV every evening.", "tr": "O her akşam televizyon izler."},
                  {"en": "My father has a small shop.", "tr": "Babamın küçük bir dükkanı var."}],
     "turkishNote": "Bu -s, Türk öğrencilerin en sık unuttuğu ektir, çünkü Türkçede \"o çalışır\" ile \"ben çalışırım\" arasındaki fark sona gelir ve İngilizcede sadece he/she/it'te bir değişiklik olur. Kendinize şunu hatırlatın: he/she/it varsa -s var."},
    [
        match([("work", "works"), ("watch", "watches"), ("study", "studies"), ("go", "goes"), ("have", "has")], "Fiil → he/she/it biçimi"),
        gap("She ___ in a hospital. (work)", ["works"], "she → works"),
        gap("He ___ TV every night. (watch)", ["watches"], "-ch → -es"),
        gap("My sister ___ English at university. (study)", ["studies"], "ünsüz + y → -ies"),
        gap("He ___ two children. (have)", ["has"], "have → has"),
        mc("Hangisi doğru?", ["She work in a bank.", "She works in a bank.", "She workes in a bank."], 1, "she → works", {0: "she ile fiile -s eklenir."}),
        mc("Hangisi doğru?", ["He plaies football.", "He plays football."], 1, "ünlü + y (ay) → yalnızca -s."),
        listen("My brother lives in Izmir. He teaches English at a school.", "Konuşanın ağabeyi ne iş yapıyor?", ["Öğretmen", "Öğrenci", "Doktor"], 0, "\"He teaches English at a school.\""),
        typ("he ile yazın: \"I finish work at five.\"", variants("He finishes work at five."), "-sh ile biten → -es: finishes."),
        order(["goes", "She", "work", "to", "by", "car"], "She goes to work by car.", "she + goes", "O işe arabayla gider."),
    ],
    {"kind": "speaking", "task": speak("Ailenizden birinin sabah rutinini anlatın (he/she ile).",
                                       "My father gets up at six. He has breakfast and he goes to work by car. He starts work at eight.",
                                       ["Fiillere -s/-es eklendi", "has doğru", "Saatler doğru"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "O yapmaz", "he/she/it ile olumsuz cümle kurabilirim.",
    {"kind": "dialogue", "title": "İdeal iş mi?", "lines": [
        {"speaker": "Can", "text": "My cousin works from home. She doesn't go to an office."},
        {"speaker": "Mia", "text": "Lucky her! Does she work long hours?"},
        {"speaker": "Can", "text": "No, she doesn't. She works from nine to three."},
        {"speaker": "Mia", "text": "And she doesn't wear a uniform, right?"},
        {"speaker": "Can", "text": "No! She works in her pyjamas!"}],
     "questions": [
        mc("Where does Can's cousin work?", ["In an office", "At home", "In a shop"], 1, "\"My cousin works from home.\""),
        mc("Does she work long hours?", ["Yes, she does.", "No, she doesn't."], 1, "\"No, she doesn't. She works from nine to three.\""),
     ]},
    {"explanation": "he, she, it ile olumsuz: **doesn't** (does not) + **yalın fiil**\n\n- She work**s** → She **doesn't work**.\n- He ha**s** → He **doesn't have**.\n\n**Dikkat:** -s artık doesn't'ta olduğu için fiile tekrar eklenmez. \"She doesn't works\" yanlıştır.\n\n| | Olumsuz |\n|---|---|\n| I / you / we / they | don't work |\n| he / she / it | doesn't work |",
     "examples": [{"en": "He doesn't eat meat.", "tr": "O et yemez."},
                  {"en": "My mother doesn't drive.", "tr": "Annem araba kullanmaz."},
                  {"en": "It doesn't work.", "tr": "Çalışmıyor (bozuk)."}],
     "turkishNote": "En sık yapılan hata: \"She doesn't likes\". doesn't'tan sonra fiil her zaman yalındır: She doesn't like. Bir de \"She don't\" yanlıştır; he/she/it ile doesn't kullanılır."},
    [
        gap("She ___ work on Sundays.", ["doesn't", "does not"], "she → doesn't"),
        gap("They ___ live here.", ["don't", "do not"], "they → don't"),
        mc("Hangisi doğru?", ["He doesn't works here.", "He doesn't work here.", "He don't work here."], 1, "doesn't + yalın fiil.", {0: "doesn't'tan sonra -s yok.", 2: "he ile doesn't."}),
        mc("Hangisi doğru?", ["My sister doesn't has a car.", "My sister doesn't have a car."], 1, "doesn't + have (has değil)."),
        typ("Olumsuz yapın: \"He wears a uniform.\"", variants("He doesn't wear a uniform."), "doesn't + wear (yalın)."),
        typ("Olumsuz yapın: \"She watches TV.\"", variants("She doesn't watch TV."), "doesn't + watch."),
        order(["doesn't", "My", "drive", "father"], "My father doesn't drive.", "Özne + doesn't + fiil.", "Babam araba kullanmaz."),
        listen("My boss doesn't drink coffee. He drinks green tea all day.", "Patron ne içiyor?", ["Kahve", "Yeşil çay", "Su"], 1, "\"He drinks green tea all day.\""),
        match([("I", "don't"), ("she", "doesn't"), ("we", "don't"), ("it", "doesn't"), ("they", "don't")], "don't mu doesn't mu?"),
        mc("\"Bilgisayar çalışmıyor.\"", ["The computer doesn't work.", "The computer don't work.", "The computer isn't work."], 0, "it (the computer) → doesn't work."),
    ],
    {"kind": "speaking", "task": speak("Tanıdığınız birinin yapmadığı 3 şeyi söyleyin.",
                                       "My sister doesn't drink coffee. She doesn't watch TV. She doesn't get up early.",
                                       ["doesn't + yalın fiil", "Fiile -s eklemedi", "he/she doğru"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "O ne yapar?", "Birinin işi ve rutini hakkında soru sorabilirim.",
    {"kind": "dialogue", "title": "İş görüşmesi hazırlığı", "lines": [
        {"speaker": "Selin", "text": "Does your brother still work at the bank?"},
        {"speaker": "Ali", "text": "No, he doesn't. He works for a tech company now."},
        {"speaker": "Selin", "text": "Really? What does he do there?"},
        {"speaker": "Ali", "text": "He's a software engineer."},
        {"speaker": "Selin", "text": "Where does he work? In Istanbul?"},
        {"speaker": "Ali", "text": "Yes, but he works from home on Fridays."}],
     "questions": [
        mc("Where does Ali's brother work now?", ["At a bank", "For a tech company", "At a school"], 1, "\"He works for a tech company now.\""),
        mc("When does he work from home?", ["On Mondays", "On Fridays", "Every day"], 1, "\"he works from home on Fridays\""),
     ]},
    {"explanation": "**Evet/hayır sorusu:** **Does** + he/she/it + **yalın fiil**?\n\n- **Does** she **work** here? – Yes, she **does**. / No, she **doesn't**.\n\n**Bilgi sorusu:** Soru kelimesi + **does** + he/she/it + yalın fiil?\n\n- **What does** he **do**?\n- **Where does** she **live**?\n- **What time does** the shop **open**?\n\n-s yine **does**'ta: \"Does she works?\" yanlış.",
     "examples": [{"en": "Does your father speak English?", "tr": "Baban İngilizce konuşur mu?"},
                  {"en": "Where does your sister work?", "tr": "Kız kardeşin nerede çalışıyor?"},
                  {"en": "What time does the film start?", "tr": "Film kaçta başlıyor?"}],
     "turkishNote": "Soru kurarken does unutulursa cümle Türkçe gibi olur: \"Where your sister works?\" Doğrusu: \"Where does your sister work?\" Bir şirket için çalışmak \"work for\", bir yerde çalışmak \"work at/in\" ile söylenir."},
    [
        gap("___ she like her job? – Yes, she does.", ["Does"], "she → Does"),
        gap("Where ___ your parents live?", ["do"], "parents = they → do"),
        mc("Hangisi doğru?", ["Does he works here?", "Does he work here?", "Do he work here?"], 1, "Does + yalın fiil."),
        order(["does", "What", "she", "do", "?"], "What does she do?", "Meslek sorusu (she).", "O ne iş yapıyor?"),
        order(["time", "What", "the", "does", "open", "shop", "?"], "What time does the shop open?", "What time + does + özne + fiil?", "Dükkan kaçta açılıyor?"),
        mc("\"Does your brother drive?\" (Evet.)", ["Yes, he drives.", "Yes, he does.", "Yes, he is."], 1, "Kısa cevap: Yes, he does."),
        gap("He works ___ a big company.", ["for"], "Bir şirket için çalışmak: work for."),
        listen("Where does your mum work? – She works at a hospital. She's a nurse.", "Anne nerede çalışıyor?", ["Okulda", "Hastanede", "Bankada"], 1, "\"She works at a hospital.\""),
        typ("Soru yapın: \"She lives in Bursa.\" (Where ile)", variants("Where does she live?"), "Where + does + she + live?"),
        mc("Hangisi doğru?", ["Where your sister works?", "Where does your sister work?", "Where does your sister works?"], 1, "Soru kelimesi + does + özne + yalın fiil."),
    ],
    {"kind": "speaking", "task": speak("JAI bir arkadaşını anlatacak. Ona arkadaşının işi ve rutini hakkında 4 soru sorun (does ile).",
                                       "What does she do? Where does she work? What time does she start work? Does she like her job?",
                                       ["does ile soru kurdu", "Fiil yalın halde", "Soru kelimeleri doğru"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Bir iş günü", "Birinin iş gününü baştan sona anlatabilirim.",
    {"kind": "dialogue", "title": "Podcast: Mesleğim", "lines": [
        {"speaker": "Host", "text": "Today, Mehmet talks about his job. Mehmet, what do you do?"},
        {"speaker": "Mehmet", "text": "I'm a chef. I work in a restaurant in Bodrum."},
        {"speaker": "Host", "text": "What's a typical day like?"},
        {"speaker": "Mehmet", "text": "I start at two in the afternoon. I prepare the food and I cook for about 200 people every night."},
        {"speaker": "Host", "text": "Do you like your job?"},
        {"speaker": "Mehmet", "text": "I love it, but I don't have a lot of free time. I never work on Mondays, so Monday is my family day."}],
     "questions": [
        mc("Where does Mehmet work?", ["In a hotel in Bodrum", "In a restaurant in Bodrum", "In a café in Izmir"], 1, "\"I work in a restaurant in Bodrum.\""),
        mc("Which day doesn't Mehmet work?", ["Sunday", "Monday", "Friday"], 1, "\"I never work on Mondays\""),
     ]},
    {"explanation": "Birinin iş gününü anlatırken ünite 5 ve 6'yı birleştiririz:\n\n1. Meslek ve yer: He**'s** a chef. He work**s** in a restaurant.\n2. Saatler: He start**s** at two. He finish**es** at midnight.\n3. Görevler: He cook**s** for 200 people.\n4. Sıklık: He **never** work**s** on Mondays.\n5. Görüş: He love**s** his job, but he **doesn't** have a lot of free time.\n\nHer cümlede he/she için **-s** var mı, kontrol edin!",
     "examples": [{"en": "She usually starts work at eight.", "tr": "Genellikle sekizde işe başlar."},
                  {"en": "He doesn't work at the weekend.", "tr": "Hafta sonu çalışmaz."},
                  {"en": "She likes her job because she helps people.", "tr": "İşini seviyor çünkü insanlara yardım ediyor."}],
     "turkishNote": "Sıklık zarfı he/she cümlesinde de fiilden önce gelir ve -s fiilde kalır: She always gets up early (She always get değil)."},
    [
        mc("Hangisi doğru?", ["She always get up early.", "She always gets up early.", "She gets always up early."], 1, "Zarf fiilden önce, -s fiilde."),
        gap("He ___ (not / work) on Sundays.", ["doesn't work", "does not work"], "he → doesn't + yalın fiil."),
        gap("My aunt ___ (teach) maths.", ["teaches"], "-ch → -es."),
        gap("___ your uncle like his job?", ["Does"], "your uncle = he → Does."),
        mc("\"Mehmet hiç pazartesi çalışmaz.\"", ["Mehmet never works on Mondays.", "Mehmet doesn't never work on Mondays.", "Mehmet never work on Mondays."], 0, "never + fiil-s, ayrıca doesn't yok."),
        order(["usually", "She", "at", "finishes", "six"], "She usually finishes at six.", "Özne + zarf + fiil-es + saat.", "Genellikle altıda bitirir."),
        listen("Sara is a pilot. She flies to London three times a week. She loves her job, but she doesn't see her family very often.", "Sara ailesini sık görüyor mu?", ["Evet", "Hayır"], 1, "\"she doesn't see her family very often\""),
        mc("fly fiilinin she ile biçimi:", ["flys", "flies", "flyes"], 1, "ünsüz + y → -ies: flies."),
        typ("he ile yazın: \"I don't like my job.\"", variants("He doesn't like his job."), "I → he, don't → doesn't, my → his."),
        match([("He's", "a chef"), ("He works", "in a restaurant"), ("He doesn't", "work on Mondays"), ("Does he", "like his job?")], "Cümleleri tamamlayın."),
    ],
    {"kind": "writing", "task": write("Tanıdığınız birinin iş gününü 5 cümleyle anlatın: meslek, yer, saatler, görevler, görüşü.",
                                      "My aunt is a nurse. She works at a hospital in Izmir. She starts work at seven and she finishes at three. She helps doctors and patients. She loves her job, but she doesn't like the night shifts.",
                                      ["he/she ile -s doğru", "doesn't + yalın fiil", "Meslek a/an ile", "Saatler at ile"])},
)

u.test([
    gap("She's ___ engineer.", ["an"], "engineer → an"),
    mc("Hangisi doğru?", ["He's lawyer.", "He's a lawyer.", "He a lawyer."], 1, "a + meslek"),
    gap("My father ___ in a factory. (work)", ["works"], "he → works"),
    gap("She ___ TV every evening. (watch)", ["watches"], "-ch → -es"),
    gap("He ___ a big car. (have)", ["has"], "have → has"),
    mc("Hangisi doğru?", ["She doesn't likes coffee.", "She doesn't like coffee.", "She don't like coffee."], 1, "doesn't + yalın fiil"),
    mc("Hangisi doğru?", ["Does he lives here?", "Does he live here?", "Do he live here?"], 1, "Does + yalın fiil"),
    order(["does", "Where", "work", "she", "?"], "Where does she work?", "Where + does + she + work?", "O nerede çalışıyor?"),
    mc("\"Does your sister drive?\" (Hayır.)", ["No, she doesn't.", "No, she don't.", "No, she isn't."], 0, "No, she doesn't."),
    mc("study fiilinin he ile biçimi:", ["studys", "studies", "studyes"], 1, "ünsüz + y → -ies"),
    gap("He works ___ a big company.", ["for"], "work for + şirket"),
    listen("My neighbour is a farmer. He gets up at five every day and he works outside all day.", "Komşu nerede çalışıyor?", ["Ofiste", "Dışarıda", "Fabrikada"], 1, "\"he works outside all day\""),
    typ("Olumsuz yapın: \"He goes to the gym.\"", variants("He doesn't go to the gym."), "doesn't + go"),
    mc("\"What does she do?\" sorusuna uygun cevap:", ["She's a waiter.", "She does it.", "She's working."], 0, "Meslek sorusu."),
    write("Bir aile üyenizin ya da arkadaşınızın işini 5 cümleyle anlatın.",
          "My best friend is a teacher. She teaches English at a primary school. She starts work at eight. She doesn't work on Saturdays. She loves her job because she likes children.",
          ["he/she ile -s/-es/-ies doğru", "doesn't doğru", "a/an doğru", "Zaman ifadeleri doğru"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

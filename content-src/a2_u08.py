"""A2 Ünite 8: Kurallar."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("A2", 8, "Kurallar", "Rules",
         "Okulda, işte ve kamusal alanlarda kuralları anlatabilir, neyin zorunlu, neyin yasak, neyin gereksiz olduğunu ayırt edebilirim.",
         ["have to / has to", "don't have to ve Do you have to ...?", "must / mustn't", "mustn't ve don't have to farkı", "had to (geçmiş zorunluluk)"],
         ["iş hayatı", "okul", "tabelalar ve kamu kuralları"],
         {"title": "Kurallar kitabı", "durationMinutes": 45,
          "goal": "Gruplar hayali bir okul, ofis ya da apartman için 'kurallar kitabı' hazırlar: 3 tane must, 3 tane mustn't, 2 tane don't have to. Sonra diğer gruplar Do we have to...? / Can we...? diye sorular sorar ve kuralların adil olup olmadığını tartışır."})

u.vocab([
    ("have to", "zorunda olmak", "I have to wear a uniform at work.", "İşte üniforma giymek zorundayım.", "he/she → has to"),
    ("must", "-meli (kesin)", "You must wear a seatbelt.", "Emniyet kemeri takmalısınız.", "must + yalın fiil"),
    ("mustn't", "yasak, -memeli", "You mustn't use your phone here.", "Burada telefon kullanmamalısınız.", "Okunuşu: /ˈmʌsnt/"),
    ("don't have to", "zorunda değil", "You don't have to come if you're busy.", "Meşgulsen gelmek zorunda değilsin.", None),
    ("rule", "kural", "Every school has rules.", "Her okulun kuralları vardır.", None),
    ("allowed", "izin verilen", "Dogs aren't allowed in the shop.", "Mağazaya köpek alınmaz.", "be allowed to + fiil"),
    ("uniform", "üniforma", "Nurses have to wear a uniform.", "Hemşireler üniforma giymek zorunda.", None),
    ("on time", "zamanında", "You must be on time for the exam.", "Sınava zamanında gelmelisin.", None),
    ("deadline", "son teslim tarihi", "The deadline for the project is Friday.", "Projenin son teslim tarihi cuma.", None),
    ("shift", "vardiya", "I work the night shift this week.", "Bu hafta gece vardiyasındayım.", None),
    ("overtime", "fazla mesai", "We sometimes have to work overtime.", "Bazen fazla mesai yapmak zorundayız.", None),
    ("day off", "izin günü", "I have a day off on Wednesday.", "Çarşamba izin günüm.", None),
    ("boss", "patron", "My boss is very strict.", "Patronum çok katı.", None),
    ("strict", "katı, sıkı", "Our teacher is strict about homework.", "Öğretmenimiz ödev konusunda katı.", None),
    ("homework", "ödev", "Do we have to do the homework tonight?", "Ödevi bu akşam yapmak zorunda mıyız?", "Sayılamaz."),
    ("exam", "sınav", "You mustn't talk during the exam.", "Sınav sırasında konuşmamalısınız.", None),
    ("fine", "para cezası", "You have to pay a fine for parking here.", "Buraya park edersen ceza ödemek zorundasın.", None),
    ("seatbelt", "emniyet kemeri", "Always wear your seatbelt.", "Her zaman emniyet kemerini tak.", None),
    ("helmet", "kask", "Cyclists must wear a helmet.", "Bisikletliler kask takmalı.", None),
    ("sign", "tabela, işaret", "What does that sign mean?", "O tabela ne anlama geliyor?", None),
    ("smoke", "sigara içmek", "You mustn't smoke in the building.", "Binada sigara içmemelisiniz.", None),
    ("fill in", "doldurmak (form)", "You have to fill in this form.", "Bu formu doldurmanız gerekiyor.", None),
    ("ID card", "kimlik kartı", "You must show your ID card at the door.", "Kapıda kimlik kartınızı göstermelisiniz.", None),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Zorundayım", "have to / has to ile iş ve okuldaki zorunlulukları anlatabilirim.",
    {"kind": "text", "title": "Bir pilotun günü", "body": "Captain Selin Arslan is a pilot. She started flying ten years ago.\n\n\"My job is amazing, but there are a lot of rules. I have to arrive at the airport two hours before every flight. I have to check the weather and the plane carefully. Pilots also have to take a medical test every year.\n\nI often have to work at night and at weekends, and sometimes I have to sleep in hotels for three or four days. My husband has to look after our daughter when I'm away. It's not easy, but I love flying!\"",
     "questions": [
        mc("When does Selin have to arrive at the airport?", ["One hour before a flight", "Two hours before a flight", "At midnight"], 1, "\"I have to arrive at the airport two hours before every flight.\""),
        mc("What do pilots have to do every year?", ["Learn a new language", "Take a medical test", "Fly to a new country"], 1, "\"Pilots also have to take a medical test every year.\""),
     ]},
    {"explanation": "**have to** + yalın fiil → zorunluluk (genellikle kurallardan ya da durumdan gelir)\n\n| | |\n|---|---|\n| I / You / We / They **have to** | work |\n| He / She / It **has to** | work |\n\n- I **have to** get up at six.\n- She **has to** wear a uniform.\n- We **have to** finish this by Friday.\n\nhave to **bir kalıptır**: \"have\" burada \"sahip olmak\" anlamında değildir. Okunuşu genellikle /ˈhæftə/, has to ise /ˈhæstə/.\n\n**Zaman ifadeleri:** every day, on Mondays, sometimes, often → I often **have to** work late.",
     "examples": [{"en": "I have to take the bus at seven every morning.", "tr": "Her sabah yedide otobüse binmek zorundayım."},
                  {"en": "My brother has to study for his exam.", "tr": "Erkek kardeşim sınavına çalışmak zorunda."},
                  {"en": "Doctors often have to work at night.", "tr": "Doktorlar sık sık gece çalışmak zorunda kalır."}],
     "turkishNote": "\"-mek zorundayım\" ve \"-mem lazım / gerek\" yapılarının ikisi de have to ile söylenebilir: \"Gitmem lazım\" = I have to go. Günlük konuşmada \"I have to go\" bir vedalaşma ifadesi olarak da çok kullanılır (Gitmem lazım, görüşürüz)."},
    [
        mc("Hangisi doğru?", ["She have to work.", "She has to work.", "She has to works."], 1, "she → has to + yalın fiil."),
        mc("Hangisi doğru?", ["I have to get up early.", "I have get up early.", "I have to getting up early."], 0, "have to + yalın fiil."),
        gap("Nurses ___ to wear a uniform.", ["have"], "nurses → have to."),
        gap("My dad ___ to work on Saturdays.", ["has"], "he → has to."),
        gap("We have to ___ this report by Friday. (finish)", ["finish"], "have to + yalın fiil."),
        mc("\"Gitmem lazım, görüşürüz!\"", ["I have to go. See you!", "I must going. See you!", "I have go. See you!"], 0, "I have to go."),
        order(["have", "I", "to", "take", "the", "bus", "at", "seven"], "I have to take the bus at seven.", "have to + fiil + nesne + zaman.", "Yedide otobüse binmek zorundayım."),
        listen("I work in a hospital, so I often have to work at night. Next week I have to work four night shifts!", "Gelecek hafta kaç gece vardiyası var?", ["İki", "Dört", "Hiç"], 1, "\"I have to work four night shifts\""),
        typ("İngilizce yazın: \"İşte üniforma giymek zorundayım.\"", variants("I have to wear a uniform at work."), "I have to + wear a uniform + at work."),
        match([("Pilots", "have to check the weather."), ("Students", "have to do homework."), ("Drivers", "have to wear a seatbelt."), ("A waiter", "has to be polite.")], "Cümleleri tamamlayın."),
    ],
    {"kind": "speaking", "task": speak("İşinizde ya da okulunuzda yapmak zorunda olduğunuz 4 şeyi have to ile anlatın. Bir aile üyenizin zorunluluklarını da has to ile söyleyin.",
                                       "At work I have to start at eight. I have to answer a lot of emails and I sometimes have to work late. I also have to wear smart clothes. My wife is a teacher, so she has to get up very early.",
                                       ["have to / has to doğru", "Yalın fiil doğru", "Sıklık ifadeleri"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "Zorunda değilim", "don't have to ile gereksiz olan şeyleri anlatabilir, zorunlulukları sorabilirim.",
    {"kind": "dialogue", "title": "Yeni iş", "lines": [
        {"speaker": "Emre", "text": "So, how's the new job?"},
        {"speaker": "Damla", "text": "It's great! I don't have to wear a suit, and I don't have to start at nine. The hours are flexible."},
        {"speaker": "Emre", "text": "Lucky you! Do you have to go to the office every day?"},
        {"speaker": "Damla", "text": "No, I don't. I work from home on Mondays and Fridays."},
        {"speaker": "Emre", "text": "Does your boss have to check your work?"},
        {"speaker": "Damla", "text": "Yes, she does. But she's very nice."}],
     "questions": [
        mc("Does Damla have to wear a suit?", ["Yes, she does.", "No, she doesn't."], 1, "\"I don't have to wear a suit\""),
        mc("When does she work from home?", ["Every day", "On Mondays and Fridays", "Never"], 1, "\"I work from home on Mondays and Fridays.\""),
     ]},
    {"explanation": "**don't / doesn't have to** → zorunda değil, gerek yok (istersen yapabilirsin)\n\n- You **don't have to** come. (Gelmek zorunda değilsin.)\n- She **doesn't have to** work tomorrow.\n\n**Soru:** Do / Does + özne + have to + fiil?\n\n- **Do** you **have to** wear a uniform? – Yes, I **do**. / No, I **don't**.\n- **Does** he **have to** travel a lot? – Yes, he **does**. / No, he **doesn't**.\n- **What time do** you **have to** start?\n\nhave to normal bir fiil gibi davranır: soru ve olumsuzda **do / does** kullanılır. ~~Have you to...?~~ / ~~She hasn't to...~~ yanlıştır.",
     "examples": [{"en": "It's Saturday. I don't have to get up early.", "tr": "Cumartesi. Erken kalkmak zorunda değilim."},
                  {"en": "Do we have to bring anything?", "tr": "Bir şey getirmemiz gerekiyor mu?"},
                  {"en": "What time does she have to leave?", "tr": "Saat kaçta çıkması gerekiyor?"}],
     "turkishNote": "\"Gerek yok\" demek için \"You don't have to\" en doğal yoldur: \"Kusura bakma, gelmek zorunda değilsin\" = You don't have to come. Bu cümle yasak bildirmez; sadece zorunluluk olmadığını söyler. Yasak için mustn't kullanılır (sonraki ders)."},
    [
        mc("Hangisi doğru?", ["She doesn't have to work.", "She don't have to work.", "She hasn't to work."], 0, "doesn't have to."),
        mc("Hangisi doğru?", ["Have you to wear a uniform?", "Do you have to wear a uniform?"], 1, "Do + you + have to?"),
        mc("\"Do you have to work on Sundays?\" (Hayır.)", ["No, I don't.", "No, I haven't.", "No, I don't have."], 0, "No, I don't."),
        gap("It's a holiday. We ___ have to go to school. (değil)", ["don't", "do not"], "don't have to."),
        gap("___ your sister have to travel for work?", ["Does"], "she → Does."),
        gap("What time do you ___ to start work?", ["have"], "have to."),
        order(["I", "don't", "have", "to", "get", "up", "early", "tomorrow"], "I don't have to get up early tomorrow.", "don't have to + fiil.", "Yarın erken kalkmak zorunda değilim."),
        listen("You don't have to bring food to the party. We have a lot. But you have to bring something to drink.", "Partiye ne getirmek zorunlu?", ["Yemek", "İçecek", "Hiçbir şey"], 1, "\"you have to bring something to drink\""),
        typ("Soru yapın: \"He has to work late.\"", variants("Does he have to work late?"), "Does + he + have to work late?"),
        typ("İngilizce yazın: \"Bir şey getirmemiz gerekiyor mu?\"", variants("Do we have to bring anything?", "Do we need to bring anything?", "Do we have to bring something?"), "Do we have to + bring anything?"),
    ],
    {"kind": "speaking", "task": speak("JAI'ye işi hakkında 5 tane Do you have to...? sorusu sorun. Sonra kendi hayatınızda yapmak zorunda olmadığınız 2 şeyi söyleyin.",
                                       "Do you have to wear a uniform? Do you have to work at weekends? What time do you have to start? Do you have to travel? Does your boss have to check your work? ... I don't have to cook on Sundays because my mum cooks. I don't have to wear a tie.",
                                       ["Do/Does + have to doğru", "Kısa cevaplar", "don't have to doğru anlamda"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "Must ve mustn't", "must ve mustn't ile kuralları ve yasakları anlatabilirim.",
    {"kind": "text", "title": "Yüzme havuzu kuralları", "body": "CITY POOL – RULES\n\n1. You must have a shower before you swim.\n2. You must wear a swimming cap.\n3. You mustn't run near the pool.\n4. You mustn't eat or drink in the water.\n5. Children under 10 must swim with an adult.\n6. You mustn't dive in the shallow end.\n\nThank you. Have fun and stay safe!",
     "questions": [
        mc("What must you do before you swim?", ["Eat something", "Have a shower", "Dive"], 1, "\"You must have a shower before you swim.\""),
        mc("Who must swim with an adult?", ["Children under 10", "Everybody", "Children under 16"], 0, "\"Children under 10 must swim with an adult.\""),
     ]},
    {"explanation": "**must** + yalın fiil → güçlü zorunluluk, kural (genellikle yazılı kurallarda ya da konuşanın kendi kararında)\n\n- You **must** wear a helmet.\n- I **must** call my mum tonight. (Kendi kararım.)\n\n**mustn't** + yalın fiil → **yasak** (yapma!)\n\n- You **mustn't** smoke here.\n- You **mustn't** be late.\n\n**must** her özneyle aynıdır, -s ya da to almaz: ~~She musts~~ / ~~You must to~~\n\n**must ve have to:**\n\n| must | have to |\n|---|---|\n| yazılı kurallar, tabelalar, konuşanın kendi fikri | dışarıdan gelen zorunluluk, günlük konuşma |\n| Passengers **must** show their tickets. | I **have to** show my ticket on the bus. |\n\nGünlük konuşmada **have to** çok daha sık kullanılır.",
     "examples": [{"en": "Visitors must sign in at the reception.", "tr": "Ziyaretçiler resepsiyonda kayıt yaptırmalı."},
                  {"en": "You mustn't tell anyone. It's a secret!", "tr": "Kimseye söylememelisin. Bu bir sır!"},
                  {"en": "I must remember to buy bread.", "tr": "Ekmek almayı unutmamalıyım."}],
     "turkishNote": "mustn't'ün okunuşunda ilk t okunmaz: /ˈmʌsnt/. Türkçedeki \"-meli\" eki hem should (tavsiye) hem must (kural) karşılığı olabilir; kural ya da yasak söz konusuysa must/mustn't, tavsiye ise should kullanın."},
    [
        mc("Hangisi doğru?", ["You must to wear a helmet.", "You must wear a helmet.", "You musts wear a helmet."], 1, "must + yalın fiil."),
        mc("Tabelada \"No smoking\" yazıyor:", ["You mustn't smoke.", "You don't have to smoke.", "You must smoke."], 0, "Yasak → mustn't."),
        gap("You ___ run near the pool. It's dangerous. (yasak)", ["mustn't", "must not"], "Yasak → mustn't."),
        gap("Passengers ___ show their tickets. (kural)", ["must"], "Kural → must."),
        gap("You mustn't ___ late for the exam. (be)", ["be"], "mustn't + yalın fiil."),
        mc("Hangisi tavsiye, hangisi kural? \"You should drink more water.\"", ["Tavsiye", "Kural"], 0, "should → tavsiye."),
        order(["mustn't", "You", "use", "your", "phone", "in", "the", "exam"], "You mustn't use your phone in the exam.", "mustn't + fiil + nesne + yer.", "Sınavda telefon kullanmamalısınız."),
        listen("Welcome to the museum. You must leave your bags at the door, and you mustn't touch the paintings. Photos are OK.", "Müzede ne yasak?", ["Fotoğraf çekmek", "Tablolara dokunmak", "Çanta taşımak (girişte bırakılmalı)"], 1, "\"you mustn't touch the paintings\""),
        typ("İngilizce yazın: \"Kimseye söylememelisin!\"", variants("You mustn't tell anyone!", "You must not tell anyone!", "You mustn't tell anybody!", "You mustn't tell anyone."), "You mustn't + tell anyone!"),
        match([("No parking", "You mustn't park here."), ("Wear a helmet", "You must wear a helmet."), ("No dogs", "Dogs aren't allowed."), ("Silence", "You mustn't talk.")], "Tabelaları anlamlarıyla eşleştirin."),
    ],
    {"kind": "writing", "task": write("Bir kütüphane, spor salonu ya da apartmanınız için 6 kurallık bir liste yazın: 3 must ve 3 mustn't.",
                                      "APARTMENT RULES\n1. You must close the main door at night.\n2. You must put your rubbish in the bins.\n3. You must park only in your space.\n4. You mustn't make noise after 11 pm.\n5. You mustn't leave bikes on the stairs.\n6. You mustn't smoke in the lift.",
                                      ["must + yalın fiil", "mustn't + yalın fiil", "Gerçekçi kurallar"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Yasak mı, gereksiz mi?", "mustn't ile don't have to arasındaki önemli farkı doğru kullanabilirim.",
    {"kind": "dialogue", "title": "Sınav öncesi", "lines": [
        {"speaker": "Student", "text": "Do we have to answer all the questions?"},
        {"speaker": "Teacher", "text": "No, you don't have to. Answer five out of eight."},
        {"speaker": "Student", "text": "Can we use a dictionary?"},
        {"speaker": "Teacher", "text": "No, you can't. And you mustn't talk to other students."},
        {"speaker": "Student", "text": "Do we have to write in pen?"},
        {"speaker": "Teacher", "text": "No, you don't have to. A pencil is fine. But you mustn't leave before 10 o'clock."}],
     "questions": [
        mc("How many questions do students have to answer?", ["All eight", "Five", "Three"], 1, "\"Answer five out of eight.\""),
        mc("What mustn't students do?", ["Use a pencil", "Talk to other students", "Answer five questions"], 1, "\"you mustn't talk to other students\""),
     ]},
    {"explanation": "Bu iki yapı Türkçede birbirine benzese de **anlamları çok farklıdır**:\n\n| | Anlam | Örnek |\n|---|---|---|\n| **mustn't** | YASAK, yapma! | You **mustn't** use your phone. (Kullanamazsın.) |\n| **don't have to** | GEREK YOK, istersen yap | You **don't have to** use a pen. (Kalem de olur.) |\n\n**İzin için can / can't:**\n\n- **Can** we use a dictionary? – Yes, you **can**. / No, you **can't**.\n- You **can't** park here. (≈ mustn't, günlük dil)\n\n**be allowed to:** You **aren't allowed to** smoke here. (resmi)\n\n**Özet:**\n\n- zorunlu → must / have to\n- yasak → mustn't / can't / not allowed to\n- gereksiz → don't have to\n- izinli → can / be allowed to",
     "examples": [{"en": "You mustn't park here. It's for ambulances.", "tr": "Buraya park edemezsin. Ambulanslar için."},
                  {"en": "You don't have to park here. There's a free car park.", "tr": "Buraya park etmek zorunda değilsin. Ücretsiz bir otopark var."},
                  {"en": "Are we allowed to take photos?", "tr": "Fotoğraf çekmemize izin var mı?"}],
     "turkishNote": "Türkçe konuşanların en kritik hatası \"zorunda değilsin\" anlamında mustn't kullanmaktır. \"You mustn't come\" = Gelmemelisin (yasak!). \"You don't have to come\" = Gelmek zorunda değilsin (istersen gel). Yanlış kullanım ciddi bir yanlış anlaşılmaya yol açabilir."},
    [
        mc("Sınav ücretsiz, para getirmenize gerek yok:", ["You mustn't pay.", "You don't have to pay."], 1, "Gerek yok → don't have to."),
        mc("Hastanede sigara yasak:", ["You mustn't smoke.", "You don't have to smoke."], 0, "Yasak → mustn't."),
        mc("\"You don't have to come.\" Anlamı:", ["Gelmen yasak.", "Gelmek zorunda değilsin.", "Gelmelisin."], 1, "don't have to = gerek yok."),
        mc("\"You mustn't come.\" Anlamı:", ["Gelmen yasak / gelmemelisin.", "Gelmek zorunda değilsin."], 0, "mustn't = yasak."),
        gap("It's Sunday. You ___ have to get up early. (gerek yok)", ["don't", "do not"], "don't have to."),
        gap("You ___ swim here. There are sharks! (yasak)", ["mustn't", "must not", "can't", "cannot"], "Yasak → mustn't."),
        gap("Are we ___ to eat in the classroom? (izin var mı)", ["allowed"], "be allowed to."),
        listen("You don't have to wear a tie, but you mustn't wear jeans or trainers to the meeting.", "Toplantıda ne yasak?", ["Kravat takmamak", "Kot ve spor ayakkabı giymek", "Takım elbise giymek"], 1, "\"you mustn't wear jeans or trainers\""),
        typ("İngilizce yazın: \"Bunu bugün bitirmek zorunda değilsin.\"", variants("You don't have to finish this today.", "You don't have to finish it today.", "You do not have to finish this today."), "You don't have to + finish this today."),
        match([("must", "zorunlu"), ("mustn't", "yasak"), ("don't have to", "gerek yok"), ("can", "izinli")], "Yapıları anlamlarıyla eşleştirin."),
    ],
    {"kind": "speaking", "task": speak("JAI ilk kez sizin şehrinize/ülkenize geliyor. Ona 2 tane must/have to, 2 tane mustn't ve 2 tane don't have to ile pratik bilgiler verin (toplu taşıma, müzeler, camiler, bahşiş...).",
                                       "You have to buy an Istanbulkart for the metro. You must take off your shoes in a mosque. You mustn't smoke on public transport. You mustn't forget your passport. You don't have to tip a lot, ten percent is fine. You don't have to speak Turkish; many people speak English.",
                                       ["must / have to doğru", "mustn't (yasak) doğru", "don't have to (gerek yok) doğru"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Eskiden zorundaydık", "had to ile geçmişteki zorunlulukları anlatabilir ve bugünle karşılaştırabilirim.",
    {"kind": "dialogue", "title": "Büyükbabayla sohbet", "lines": [
        {"speaker": "Can", "text": "Grandpa, what was school like when you were young?"},
        {"speaker": "Grandpa", "text": "Very strict! We had to wear black uniforms and we had to stand up when the teacher came in."},
        {"speaker": "Can", "text": "Did you have to walk to school?"},
        {"speaker": "Grandpa", "text": "Yes, I did. Five kilometres! In the snow!"},
        {"speaker": "Can", "text": "Wow. We don't have to wear uniforms now, and I go by bus."},
        {"speaker": "Grandpa", "text": "Lucky you! But I didn't have to do homework on a computer. We just had books."}],
     "questions": [
        mc("What did Grandpa have to do when the teacher came in?", ["Sit down", "Stand up", "Say hello"], 1, "\"we had to stand up when the teacher came in\""),
        mc("How did Grandpa get to school?", ["By bus", "He walked", "By car"], 1, "\"Yes, I did. Five kilometres!\""),
     ]},
    {"explanation": "**must** ve **have to**'nun geçmiş hali **had to**'dur. (must'ın geçmiş hali yoktur.)\n\n- I **had to** work late yesterday.\n- We **had to** wear uniforms at school.\n\n**Olumsuz:** didn't have to → gerek yoktu\n\n- I **didn't have to** pay. It was free.\n\n**Soru:** Did + özne + have to + fiil?\n\n- **Did** you **have to** wait long? – Yes, I **did**. / No, I **didn't**.\n\n**Geçmiş yasak** için genellikle **couldn't** ya da **weren't allowed to** kullanılır:\n\n- We **couldn't** use phones at school. / We **weren't allowed to** talk.",
     "examples": [{"en": "I had to get up at five for my flight.", "tr": "Uçuşum için beşte kalkmak zorunda kaldım."},
                  {"en": "We didn't have to queue. There was nobody there.", "tr": "Sıra beklememiz gerekmedi. Kimse yoktu."},
                  {"en": "Did you have to show your passport?", "tr": "Pasaportunu göstermek zorunda kaldın mı?"}],
     "turkishNote": "\"-mek zorunda kaldım\" = I had to. \"musted\" diye bir kelime yoktur; geçmişte her zaman had to kullanılır. \"Didn't have to\" da \"zorunda kalmadım / gerek olmadı\" anlamına gelir."},
    [
        mc("Hangisi doğru?", ["I musted work yesterday.", "I had to work yesterday.", "I have to worked yesterday."], 1, "Geçmiş → had to."),
        mc("Hangisi doğru?", ["Did you had to wait?", "Did you have to wait?"], 1, "Did + have to."),
        gap("We ___ to wear uniforms at my old school.", ["had"], "had to."),
        gap("I didn't ___ to pay. It was free.", ["have"], "didn't have to."),
        gap("___ you have to show your ID at the door?", ["Did"], "Geçmiş soru → Did."),
        mc("Geçmiş yasak: \"Okulda telefon kullanamazdık.\"", ["We couldn't use phones at school.", "We mustn't use phones at school.", "We didn't must use phones."], 0, "Geçmiş yasak → couldn't."),
        order(["had", "I", "to", "get", "up", "at", "five"], "I had to get up at five.", "had to + fiil + zaman.", "Beşte kalkmak zorunda kaldım."),
        listen("The flight was cancelled, so we had to stay at the airport hotel. But we didn't have to pay for it.", "Otel için para ödediler mi?", ["Evet", "Hayır, ödemek zorunda kalmadılar", "Yarısını ödediler"], 1, "\"we didn't have to pay for it\""),
        typ("İngilizce yazın: \"Dün geç saate kadar çalışmak zorunda kaldım.\"", variants("I had to work late yesterday.", "Yesterday I had to work late.", "Yesterday, I had to work late."), "I had to + work late + yesterday."),
        mc("\"Did you have to wait long?\" (Hayır.)", ["No, I didn't.", "No, I hadn't.", "No, I don't."], 0, "No, I didn't."),
    ],
    {"kind": "speaking", "task": speak("Çocukluğunuzdaki okul ya da ev kurallarını bugünle karşılaştırın: eskiden yapmak zorunda olduğunuz 3 şey (had to), yapmak zorunda olmadığınız 1 şey (didn't have to), yasak olan 1 şey (couldn't) ve bugün nasıl olduğu.",
                                       "When I was at primary school, we had to wear a blue uniform. We had to be in bed at nine and we had to help with the cleaning. I didn't have to cook. We couldn't watch TV on school nights. Now my kids don't have to wear uniforms, and they can watch TV.",
                                       ["had to doğru", "didn't have to doğru", "couldn't (geçmiş yasak)", "Bugünle karşılaştırma"])},
)

u.test([
    mc("Hangisi doğru?", ["He have to work.", "He has to work."], 1, "has to"),
    gap("I have to ___ a uniform at work. (wear)", ["wear"], "have to + yalın fiil"),
    mc("Hangisi doğru?", ["Have you to go?", "Do you have to go?"], 1, "Do you have to...?"),
    gap("She ___ have to work tomorrow. It's a holiday.", ["doesn't", "does not"], "doesn't have to"),
    mc("Hangisi doğru?", ["You must to stop.", "You must stop."], 1, "must + yalın fiil"),
    gap("You ___ smoke in the hospital. (yasak)", ["mustn't", "must not", "can't", "cannot"], "mustn't"),
    mc("Müze ücretsiz:", ["You mustn't pay.", "You don't have to pay."], 1, "Gerek yok"),
    mc("\"You mustn't open that door.\" Anlamı:", ["O kapıyı açmak yasak.", "O kapıyı açmak zorunda değilsin."], 0, "mustn't = yasak"),
    gap("Are we ___ to take photos here? (izin)", ["allowed"], "allowed to"),
    mc("Hangisi doğru?", ["I musted leave early.", "I had to leave early."], 1, "had to"),
    gap("We didn't ___ to wait. (have)", ["have"], "didn't have to"),
    mc("\"Did you have to pay?\" (Evet.)", ["Yes, I did.", "Yes, I had."], 0, "Yes, I did."),
    listen("At my new job I don't have to wear a suit, but I have to be in the office by half past eight.", "Yeni işinde ne zorunlu?", ["Takım elbise giymek", "Sekiz buçukta ofiste olmak", "Evden çalışmak"], 1, "\"I have to be in the office by half past eight\""),
    typ("İngilizce yazın: \"Gelmek zorunda değilsin.\"", variants("You don't have to come.", "You do not have to come."), "You don't have to come."),
    write("Bir arkadaşınız sizin iş yerinizde ya da okulunuzda başlayacak. Ona bir e-posta yazın (70–90 kelime): yapmak zorunda olduğu şeyler, yasak olan şeyler, yapmak zorunda olmadığı şeyler. Geçen yıl sizin yapmak zorunda kaldığınız bir şeyi de ekleyin (had to).",
          "Hi Murat,\nWelcome to the team! Here are some things you need to know. You have to arrive by nine and you must wear your ID card all the time. You mustn't eat at your desk, but there's a nice kitchen. You don't have to wear a suit; smart clothes are fine. You don't have to work at weekends. Last year we had to work late every Friday, but now it's better.\nSee you on Monday!\nSevgi",
          ["have to / must doğru", "mustn't doğru (yasak)", "don't have to doğru (gerek yok)", "had to doğru"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

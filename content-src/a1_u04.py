"""A1 Ünite 4: Evim."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("A1", 4, "Evim", "My Home",
         "Evimi anlatabilir, eşyaların nerede olduğunu söyleyip sorabilirim.",
         ["there is / there are", "Is there...? / Are there any...?", "yer edatları"],
         ["odalar", "mobilya ve ev eşyaları"],
         {"title": "Hayalimdeki ev", "durationMinutes": 45,
          "goal": "Öğrenciler hayallerindeki evi çizip anlatır; eşleri sorularla (Is there a garden? Where's the TV?) evi kendi kâğıdına çizmeye çalışır."})

u.vocab([
    ("house", "ev (müstakil)", "Their house is big.", "Onların evi büyük.", None),
    ("flat", "daire", "I live in a small flat.", "Küçük bir dairede oturuyorum.", "Amerikan İngilizcesinde: apartment."),
    ("living room", "oturma odası, salon", "The TV is in the living room.", "Televizyon salonda.", None),
    ("bedroom", "yatak odası", "There are two bedrooms.", "İki yatak odası var.", None),
    ("kitchen", "mutfak", "The kitchen is small.", "Mutfak küçük.", None),
    ("bathroom", "banyo", "Is there a bathroom upstairs?", "Üst katta banyo var mı?", None),
    ("garden", "bahçe", "There's a garden behind the house.", "Evin arkasında bir bahçe var.", None),
    ("balcony", "balkon", "We have a big balcony.", "Büyük bir balkonumuz var.", None),
    ("sofa", "kanepe", "The cat is on the sofa.", "Kedi kanepenin üstünde.", None),
    ("table", "masa", "The keys are on the table.", "Anahtarlar masanın üstünde.", None),
    ("chair", "sandalye", "There are four chairs.", "Dört sandalye var.", None),
    ("bed", "yatak", "My bed is next to the window.", "Yatağım pencerenin yanında.", None),
    ("window", "pencere", "Open the window, please.", "Pencereyi aç lütfen.", None),
    ("door", "kapı", "The door is blue.", "Kapı mavi.", None),
    ("fridge", "buzdolabı", "The milk is in the fridge.", "Süt buzdolabında.", None),
    ("lamp", "lamba", "There's a lamp on the desk.", "Masanın üstünde bir lamba var.", None),
    ("in", "içinde", "The phone is in my bag.", "Telefon çantamda.", None),
    ("on", "üstünde", "Your book is on the chair.", "Kitabın sandalyenin üstünde.", None),
    ("under", "altında", "The shoes are under the bed.", "Ayakkabılar yatağın altında.", None),
    ("next to", "yanında", "The bank is next to the café.", "Banka kafenin yanında.", None),
    ("behind", "arkasında", "The garden is behind the house.", "Bahçe evin arkasında.", None),
    ("in front of", "önünde", "The car is in front of the house.", "Araba evin önünde.", None),
    ("opposite", "karşısında", "The bank is opposite the school.", "Banka okulun karşısında.", None),
    ("between", "arasında", "The sofa is between the lamp and the window.", "Kanepe lambayla pencerenin arasında.", None),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Evimde neler var?", "there is / there are ile evimde neler olduğunu söyleyebilirim.",
    {"kind": "dialogue", "title": "Yeni daire", "lines": [
        {"speaker": "Deniz", "text": "Welcome to my new flat!"},
        {"speaker": "Mia", "text": "Wow, it's lovely. How many bedrooms are there?"},
        {"speaker": "Deniz", "text": "There are two bedrooms and there's one bathroom."},
        {"speaker": "Mia", "text": "And there's a big balcony!"},
        {"speaker": "Deniz", "text": "Yes, I love it. There are a lot of plants on it."}],
     "questions": [
        mc("How many bedrooms are there?", ["One", "Two", "Three"], 1, "\"There are two bedrooms.\""),
        mc("What's on the balcony?", ["A lot of plants", "Two chairs", "A table"], 0, "\"There are a lot of plants on it.\""),
     ]},
    {"explanation": "Bir yerde bir şeyin **var** olduğunu söylemek için:\n\n- tekil: **There is** (There's) a kitchen.\n- çoğul: **There are** two bedrooms.\n\nKaç tane olduğunu sormak için: **How many** bedrooms **are there**?",
     "examples": [{"en": "There's a sofa in the living room.", "tr": "Salonda bir kanepe var."},
                  {"en": "There are three chairs in the kitchen.", "tr": "Mutfakta üç sandalye var."},
                  {"en": "How many rooms are there?", "tr": "Kaç oda var?"}],
     "turkishNote": "\"var\" iki şekilde çevrilir: Bir yerde bulunuyorsa there is/are (\"Mutfakta bir masa var\" = There's a table in the kitchen). Birine aitse have (\"Bir arabam var\" = I have a car). \"In the kitchen have a table\" yanlıştır."},
    [
        match([("kitchen", "mutfak"), ("bedroom", "yatak odası"), ("bathroom", "banyo"), ("living room", "salon"), ("garden", "bahçe")], "Odaları eşleştirin."),
        gap("There ___ a sofa in the living room.", ["is", "'s"], "Tekil → there is."),
        gap("There ___ four chairs in the kitchen.", ["are"], "Çoğul → there are."),
        mc("\"Bahçede bir ağaç var.\"", ["In the garden has a tree.", "There's a tree in the garden.", "There are a tree in the garden."], 1, "Bir yerde bulunma → there is.", {0: "Bir yerde bulunmayı have ile değil, there is ile söyleriz."}),
        mc("\"Bir köpeğim var.\"", ["There's a dog.", "I have a dog.", "I'm a dog."], 1, "Sahiplik → have."),
        order(["many", "How", "are", "there", "rooms", "?"], "How many rooms are there?", "How many + çoğul isim + are there?", "Kaç oda var?"),
        mc("Hangisi doğru?", ["There is two bathrooms.", "There are two bathrooms."], 1, "two bathrooms çoğul → are."),
        listen("In my flat, there's a small kitchen, a living room and there are two bedrooms.", "Dairede kaç yatak odası var?", ["Bir", "İki", "Üç"], 1, "\"there are two bedrooms\""),
        typ("İngilizce yazın: \"Salonda bir televizyon var.\"", variants("There's a TV in the living room.", "There is a TV in the living room.", "There's a television in the living room."), "There's + a TV + in the living room."),
        gap("There ___ a lot of books in my room.", ["are"], "a lot of books çoğul → are."),
    ],
    {"kind": "speaking", "task": speak("Evinizi anlatın: kaç oda var, hangi odalar var?",
                                       "I live in a flat. There are three bedrooms. There's a big living room and a small kitchen.",
                                       ["there is/are doğru seçildi", "Oda isimleri doğru", "a/an ve çoğullar doğru"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "... var mı?", "Bir yerde bir şey olup olmadığını sorup cevaplayabilirim.",
    {"kind": "dialogue", "title": "Otel resepsiyonu", "lines": [
        {"speaker": "Guest", "text": "Is there a fridge in the room?"},
        {"speaker": "Receptionist", "text": "Yes, there is. There's a small fridge."},
        {"speaker": "Guest", "text": "Are there any towels?"},
        {"speaker": "Receptionist", "text": "Yes, there are. They're in the bathroom."},
        {"speaker": "Guest", "text": "Is there a TV?"},
        {"speaker": "Receptionist", "text": "No, there isn't, sorry. But there's free Wi-Fi."}],
     "questions": [
        mc("Is there a TV in the room?", ["Yes, there is.", "No, there isn't."], 1, "\"No, there isn't, sorry.\""),
        mc("Where are the towels?", ["In the bathroom", "In the fridge", "At the reception"], 0, "\"They're in the bathroom.\""),
     ]},
    {"explanation": "**Soru:** is/are başa gelir.\n\n- **Is there** a fridge? – Yes, there is. / No, there isn't.\n- **Are there any** towels? – Yes, there are. / No, there aren't.\n\n**Olumsuz:**\n\n- There **isn't** a TV.\n- There **aren't any** chairs.\n\nÇoğul soru ve olumsuzlarda isimden önce genellikle **any** kullanılır.",
     "examples": [{"en": "Is there a garden?", "tr": "Bahçe var mı?"},
                  {"en": "Are there any shops near here?", "tr": "Buralarda hiç dükkan var mı?"},
                  {"en": "There aren't any windows in the bathroom.", "tr": "Banyoda hiç pencere yok."}],
     "turkishNote": "Türkçede \"yok\" ayrı bir kelimedir. İngilizcede olumsuzluk there is/are'a not eklenerek yapılır: there isn't, there aren't. Kısa cevapta da \"there\" kalır: \"Yes, there is.\" (\"Yes, is\" değil.)"},
    [
        gap("___ there a garden? – Yes, there is.", ["Is"], "Tekil soru → Is there...?"),
        gap("Are there ___ chairs in the kitchen?", ["any"], "Çoğul soruda any."),
        mc("\"Is there a lift?\" (Asansör yok.)", ["No, there isn't.", "No, there aren't.", "No, isn't."], 0, "Tekil → No, there isn't."),
        mc("\"Are there any shops?\" (Var.)", ["Yes, there is.", "Yes, there are.", "Yes, are."], 1, "Çoğul → Yes, there are."),
        gap("There ___ any towels in the bathroom.", ["aren't", "are not"], "Çoğul olumsuz → there aren't any."),
        mc("\"Odada televizyon yok.\"", ["There isn't a TV in the room.", "There's no have TV.", "In the room isn't TV."], 0, "Tekil olumsuz → There isn't a ..."),
        order(["there", "Is", "a", "near", "here", "bank", "?"], "Is there a bank near here?", "Is there + a + isim + yer?", "Buralarda banka var mı?"),
        listen("Is there a car park at the hotel? – No, there isn't. But there's a car park next to the station.", "Otelde otopark var mı?", ["Evet", "Hayır"], 1, "\"No, there isn't.\""),
        typ("Olumsuz yapın: \"There are some chairs.\"", variants("There aren't any chairs."), "there are → there aren't, some → any."),
        mc("Hangisi doğru?", ["Are there a balcony?", "Is there a balcony?", "Is there any balcony?"], 1, "Tekil sayılabilen isim → Is there a ...?"),
    ],
    {"kind": "speaking", "task": speak("Bir otele telefon ediyorsunuz. JAI resepsiyonist. Odada neler olduğunu sorun (en az 3 soru).",
                                       "Is there a fridge in the room? Are there any towels? Is there free Wi-Fi?",
                                       ["Is there / Are there any doğru seçildi", "Tekil ve çoğul isimler doğru", "Kısa cevapları anladı"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "İçinde, üstünde, altında", "in, on, under ile bir şeyin nerede olduğunu söyleyebilirim.",
    {"kind": "dialogue", "title": "Anahtarlarım nerede?", "lines": [
        {"speaker": "Can", "text": "Mum, where are my keys?"},
        {"speaker": "Mum", "text": "Are they in your bag?"},
        {"speaker": "Can", "text": "No, they aren't."},
        {"speaker": "Mum", "text": "Look on the table in the kitchen."},
        {"speaker": "Can", "text": "No... Oh, here they are! They're under the newspaper."}],
     "questions": [
        mc("Where are the keys?", ["In Can's bag", "On the sofa", "Under the newspaper"], 2, "\"They're under the newspaper.\""),
        mc("Which room is the table in?", ["The kitchen", "The bedroom", "The living room"], 0, "\"the table in the kitchen\""),
     ]},
    {"explanation": "Yeri sormak için: **Where is** (Where's) the ...? / **Where are** the ...?\n\n- **in** = içinde: in the bag, in the kitchen\n- **on** = üstünde (temas ederek): on the table, on the wall\n- **under** = altında: under the bed\n\nBelirli bir eşyadan bahsederken **the** kullanırız: \"the keys\" = (bildiğimiz) anahtarlar.",
     "examples": [{"en": "Where's my phone? – It's on the sofa.", "tr": "Telefonum nerede? – Kanepenin üstünde."},
                  {"en": "The milk is in the fridge.", "tr": "Süt buzdolabında."},
                  {"en": "The cat is under the table.", "tr": "Kedi masanın altında."}],
     "turkishNote": "Türkçede yer ismin sonuna ek olarak gelir (masa-da, çanta-nın içinde). İngilizcede edat ismin önüne gelir: on the table. Duvardaki bir resim de \"on the wall\" olur, çünkü duvara değiyor."},
    [
        match([("in", "içinde"), ("on", "üstünde"), ("under", "altında")], "Edatları eşleştirin."),
        gap("The milk is ___ the fridge.", ["in"], "Buzdolabının içinde → in."),
        gap("The picture is ___ the wall.", ["on"], "Duvara asılı (temas var) → on."),
        gap("The shoes are ___ the bed.", ["under"], "Yatağın altında → under."),
        mc("\"Telefonum nerede?\"", ["Where's my phone?", "Where my phone is?", "My phone where?"], 0, "Where + is + özne?"),
        mc("Where are your books?", ["It's on the desk.", "They're on the desk.", "There on the desk."], 1, "books çoğul → They're."),
        order(["is", "The", "on", "cat", "the", "sofa"], "The cat is on the sofa.", "Özne + is + edat + the + yer.", "Kedi kanepenin üstünde."),
        listen("Your glasses? They're on the table in the living room, next to the TV remote.", "Gözlük nerede?", ["Mutfak masasında", "Salondaki masada", "Yatağın altında"], 1, "\"on the table in the living room\""),
        typ("İngilizce yazın: \"Anahtarlar çantada.\"", variants("The keys are in the bag.", "The keys are in my bag."), "The keys + are + in + the bag."),
        mc("Hangisi doğru?", ["The keys is in the bag.", "The keys are in the bag.", "The keys in the bag."], 1, "keys çoğul → are; fiil eksik olmamalı."),
    ],
    {"kind": "speaking", "task": speak("JAI evinizdeki 3 eşyanın yerini soracak (Where's your phone? ...). in, on, under ile cevaplayın.",
                                       "My phone is on the table. My keys are in my bag. My shoes are under the bed.",
                                       ["in/on/under doğru", "is/are doğru", "the kullandı"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Yanında, arkasında, önünde", "next to, behind, in front of, between ile yer tarif edebilirim.",
    {"kind": "dialogue", "title": "Mahallem", "lines": [
        {"speaker": "Tom", "text": "Is there a supermarket near your flat?"},
        {"speaker": "Elif", "text": "Yes. It's next to the bus stop."},
        {"speaker": "Tom", "text": "And the park?"},
        {"speaker": "Elif", "text": "It's behind my building. There's a café in front of the park, too."},
        {"speaker": "Tom", "text": "And where's the pharmacy?"},
        {"speaker": "Elif", "text": "It's between the bank and the bakery."}],
     "questions": [
        mc("Where is the supermarket?", ["Next to the bus stop", "Behind the building", "In front of the park"], 0, "\"It's next to the bus stop.\""),
        mc("Where is the pharmacy?", ["Next to the café", "Between the bank and the bakery", "Behind the park"], 1, "\"It's between the bank and the bakery.\""),
     ]},
    {"explanation": "- **next to** = yanında\n- **behind** = arkasında\n- **in front of** = önünde\n- **between** A **and** B = A ile B'nin arasında\n- **opposite** = karşısında\n\nHepsi ismin **önüne** gelir: next to **the** window, behind **the** house.",
     "examples": [{"en": "The lamp is next to the bed.", "tr": "Lamba yatağın yanında."},
                  {"en": "There's a car in front of the door.", "tr": "Kapının önünde bir araba var."},
                  {"en": "The bank is opposite the school.", "tr": "Banka okulun karşısında."}],
     "turkishNote": "\"in front of\" üç kelimedir ve \"of\" unutulmamalı: in front of the house. \"next to\"dan sonra \"of\" gelmez: next to the house (next of değil). between iki şeyle kullanılır ve aralarına \"and\" girer."},
    [
        match([("next to", "yanında"), ("behind", "arkasında"), ("in front of", "önünde"), ("between", "arasında"), ("opposite", "karşısında")], "Edatları eşleştirin."),
        gap("The car is in front ___ the house.", ["of"], "in front of: of unutulmamalı."),
        gap("The bank is between the café ___ the school.", ["and"], "between A and B"),
        mc("Hangisi doğru?", ["next of the door", "next to the door", "next the door"], 1, "next to + isim."),
        mc("\"Bahçe evin arkasında.\"", ["The garden is behind the house.", "The garden is in front of the house.", "The garden is between the house."], 0, "arkasında = behind."),
        order(["is", "The", "opposite", "park", "the", "school"], "The park is opposite the school.", "Özne + is + opposite + the + yer.", "Park okulun karşısında."),
        gap("My desk is ___ to the window.", ["next"], "yanında = next to."),
        listen("The bakery is between the bank and the post office. It's opposite the park.", "Fırın neyin karşısında?", ["Bankanın", "Postanenin", "Parkın"], 2, "\"It's opposite the park.\""),
        typ("İngilizce yazın: \"Lamba kanepenin yanında.\"", variants("The lamp is next to the sofa."), "The lamp + is + next to + the sofa."),
        mc("Hangisi doğru?", ["between the bank", "between the bank and the café", "between of the bank and café"], 1, "between iki şeyle ve and ile kullanılır."),
    ],
    {"kind": "speaking", "task": speak("Mahallenizi anlatın: evinizin yakınında hangi yerler var ve neredeler?",
                                       "There's a supermarket next to my building. The park is behind it. There's a bakery opposite the bus stop.",
                                       ["Yer edatları doğru", "there is/are doğru", "the kullandı"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Benim odam", "Odamı ayrıntılı olarak anlatabilirim.",
    {"kind": "dialogue", "title": "Video görüşmesi", "lines": [
        {"speaker": "Yuki", "text": "Is that your room, Deniz?"},
        {"speaker": "Deniz", "text": "Yes, it is. It's small but I love it."},
        {"speaker": "Yuki", "text": "What's on the wall behind you?"},
        {"speaker": "Deniz", "text": "It's a map of the world. And there's a guitar next to my desk."},
        {"speaker": "Yuki", "text": "Is there a window in your room?"},
        {"speaker": "Deniz", "text": "Yes, there's a big window. My bed is under it."}],
     "questions": [
        mc("What's on the wall?", ["A guitar", "A map", "A window"], 1, "\"It's a map of the world.\""),
        mc("Where's Deniz's bed?", ["Under the window", "Next to the desk", "Behind the door"], 0, "\"My bed is under it.\" (it = the window)"),
     ]},
    {"explanation": "Bir odayı anlatırken bu ünitede öğrendiklerimizi birleştiririz:\n\n1. Genel bilgi: My room **is** small/big.\n2. Neler var: **There's** a desk. **There are** two lamps.\n3. Nerede: The desk **is next to** the window.\n4. Nasıl: The walls **are** white. It's **a big blue** sofa.\n\nAynı şeyi tekrar etmemek için **it** ve **them** kullanılır: There's a window. My bed is under **it**.",
     "examples": [{"en": "My room is small but bright.", "tr": "Odam küçük ama aydınlık."},
                  {"en": "There's a big desk next to the window.", "tr": "Pencerenin yanında büyük bir masa var."},
                  {"en": "My books are on the shelf above the bed.", "tr": "Kitaplarım yatağın üstündeki rafta."}],
     "turkishNote": "İlk kez bahsettiğimiz şey için a/an, ikinci kez bahsederken the kullanılır: \"There's a desk in my room. The desk is white.\" Türkçede bu ayrım yoktur, dikkat edin."},
    [
        mc("Hangisi doğru sıra?", ["There's a desk. The desk is white.", "There's the desk. A desk is white."], 0, "İlk kez a, sonra the."),
        gap("There's a lamp in my room. ___ lamp is on the desk.", ["The"], "İkinci kez bahsedilen → the."),
        gap("There's a big window. My bed is under ___.", ["it"], "the window yerine it."),
        mc("\"Duvarlar beyaz.\"", ["The walls is white.", "The walls are white.", "The walls are whites."], 1, "walls çoğul → are; sıfat çoğul olmaz."),
        order(["a", "There's", "desk", "next", "to", "window", "the"], "There's a desk next to the window.", "There's + a + isim + edat + the + yer.", "Pencerenin yanında bir masa var."),
        mc("Hangisi bir odayı anlatmak için uygun DEĞİL?", ["There's a sofa in front of the TV.", "My bedroom has a big bed.", "There are a lamp on the desk."], 2, "a lamp tekil → There's a lamp."),
        listen("In my bedroom, there's a bed, a desk and two chairs. The desk is between the bed and the window.", "Masa nerede?", ["Yatağın altında", "Yatakla pencerenin arasında", "Kapının arkasında"], 1, "\"between the bed and the window\""),
        gap("My shoes ___ under the bed.", ["are"], "shoes çoğul → are."),
        typ("İngilizce yazın: \"Odamda iki pencere var.\"", variants("There are two windows in my room.", "My room has two windows."), "There are + two windows + in my room."),
        match([("a desk", "ilk kez bahsediliyor"), ("the desk", "daha önce bahsedildi"), ("it", "the desk'in yerine")], "a, the ve it ne zaman kullanılır?"),
    ],
    {"kind": "writing", "task": write("Odanızı 5 cümleyle anlatın: büyüklüğü, içindeki eşyalar ve nerede oldukları.",
                                      "My room is small but nice. There's a bed and a desk. The desk is next to the window. There are a lot of books on the shelf. My guitar is behind the door.",
                                      ["there is/are doğru", "Yer edatları doğru", "a/the doğru", "Sıfatlar doğru yerde"])},
)

u.test([
    gap("There ___ two bathrooms in our house.", ["are"], "Çoğul → there are."),
    mc("\"Bahçede bir ağaç var.\"", ["There's a tree in the garden.", "The garden has there a tree.", "In the garden is have a tree."], 0, "Bir yerde bulunma → there is."),
    mc("\"Is there a lift?\" (Yok.)", ["No, there isn't.", "No, it isn't.", "No, there aren't."], 0, "Tekil → No, there isn't."),
    gap("Are there ___ shops near here?", ["any"], "Çoğul soruda any."),
    order(["many", "How", "are", "there", "bedrooms", "?"], "How many bedrooms are there?", "How many + çoğul + are there?", "Kaç yatak odası var?"),
    mc("Kitap masanın üstünde:", ["The book is in the table.", "The book is on the table.", "The book is under the table."], 1, "üstünde = on."),
    gap("The car is in front ___ the house.", ["of"], "in front of"),
    mc("Hangisi doğru?", ["The bank is next of the café.", "The bank is next to the café.", "The bank is next the café."], 1, "next to"),
    mc("\"Eczane bankayla fırının arasında.\"", ["The pharmacy is between the bank and the bakery.", "The pharmacy is between the bank or the bakery.", "The pharmacy is opposite the bank and the bakery."], 0, "between A and B"),
    gap("There's a sofa in the living room. ___ sofa is grey.", ["The"], "İkinci kez → the."),
    mc("Where are my glasses?", ["It's on the desk.", "They're on the desk.", "There on the desk."], 1, "glasses çoğul → They're."),
    listen("There's a small garden behind the house and there are two big trees in it.", "Bahçe nerede?", ["Evin önünde", "Evin arkasında", "Evin yanında"], 1, "\"behind the house\""),
    typ("İngilizce yazın: \"Mutfakta buzdolabı yok.\"", variants("There isn't a fridge in the kitchen.", "There's no fridge in the kitchen."), "There isn't a + fridge + in the kitchen."),
    mc("\"Bir arabam var.\"", ["There's my car.", "I have a car.", "There is a car of me."], 1, "Sahiplik → have."),
    write("Evinizi ya da dairenizi 5 cümleyle anlatın: odalar, eşyalar, nerede oldukları.",
          "I live in a flat with my family. There are three bedrooms and a big living room. There's a balcony next to the kitchen. In the living room, there's a sofa in front of the TV. My room is small but I love it.",
          ["there is/are doğru", "Oda ve eşya kelimeleri", "Yer edatları doğru", "a/the doğru"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

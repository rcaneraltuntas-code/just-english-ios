"""A1 Ünite 3: Eşyalarım."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("A1", 3, "Eşyalarım", "My Things",
         "Eşyalarımın adını, rengini ve kime ait olduğunu söyleyebilir, \"Bu ne?\" diye sorabilirim.",
         ["a / an", "çoğul isimler (düzenli ve düzensiz)", "this / that / these / those", "renkler ve sıfat sırası"],
         ["günlük eşyalar", "renkler"],
         {"title": "Çantamda ne var?", "durationMinutes": 45,
          "goal": "Öğrenciler çantalarından eşyalar çıkarıp eşlerine sorar (What's this? What colour is it? Whose is it?), sonra kayıp eşya oyunu oynanır."})

u.vocab([
    ("bag", "çanta", "My bag is black.", "Çantam siyah.", None),
    ("phone", "telefon", "Is this your phone?", "Bu senin telefonun mu?", None),
    ("key", "anahtar", "Where are my keys?", "Anahtarlarım nerede?", None),
    ("wallet", "cüzdan", "His wallet is brown.", "Onun cüzdanı kahverengi.", None),
    ("umbrella", "şemsiye", "Take an umbrella!", "Bir şemsiye al!", "Ünlü sesle başladığı için an umbrella."),
    ("watch", "kol saati", "This is a new watch.", "Bu yeni bir kol saati.", "Çoğulu: watches. Duvar saati ise clock."),
    ("glasses", "gözlük", "Her glasses are on the table.", "Gözlüğü masanın üstünde.", "Her zaman çoğul: my glasses are..."),
    ("book", "kitap", "That's an English book.", "Şu bir İngilizce kitabı.", None),
    ("pen", "tükenmez kalem", "Can I use your pen?", "Kalemini kullanabilir miyim?", None),
    ("laptop", "dizüstü bilgisayar", "My laptop is old.", "Dizüstü bilgisayarım eski.", None),
    ("bottle", "şişe", "a bottle of water", "bir şişe su", None),
    ("box", "kutu", "These boxes are heavy.", "Bu kutular ağır.", "Çoğulu: boxes."),
    ("man / men", "adam / adamlar", "Those men are my uncles.", "Şu adamlar amcalarım.", "Düzensiz çoğul."),
    ("woman / women", "kadın / kadınlar", "Two women are at the door.", "Kapıda iki kadın var.", "Düzensiz çoğul. women /ˈwɪmɪn/ diye okunur."),
    ("person / people", "kişi / insanlar", "Ten people are here.", "Burada on kişi var.", "Düzensiz çoğul."),
    ("new", "yeni", "a new phone", "yeni bir telefon", None),
    ("old", "eski; yaşlı", "an old car", "eski bir araba", "an old: old ünlüyle başlar."),
    ("big", "büyük", "a big box", "büyük bir kutu", None),
    ("small", "küçük", "a small bag", "küçük bir çanta", None),
    ("red", "kırmızı", "a red umbrella", "kırmızı bir şemsiye", None),
    ("blue", "mavi", "Her eyes are blue.", "Onun gözleri mavi.", None),
    ("black / white", "siyah / beyaz", "a black and white photo", "siyah beyaz bir fotoğraf", None),
    ("colour", "renk", "What colour is your car?", "Araban ne renk?", "Amerikan İngilizcesinde: color."),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "a ve an", "Tekil eşyaları a/an ile söyleyebilirim.",
    {"kind": "dialogue", "title": "Kayıp eşya bürosu", "lines": [
        {"speaker": "Officer", "text": "Good morning. Can I help you?"},
        {"speaker": "Selin", "text": "Yes, please. My bag is lost."},
        {"speaker": "Officer", "text": "OK. What's in your bag?"},
        {"speaker": "Selin", "text": "A phone, a wallet, an umbrella and a book."},
        {"speaker": "Officer", "text": "Is this your umbrella?"},
        {"speaker": "Selin", "text": "Yes, it is! Thank you!"}],
     "questions": [
        mc("What is lost?", ["Selin's phone", "Selin's bag", "Selin's book"], 1, "\"My bag is lost.\""),
        mc("What does the officer find?", ["A wallet", "An umbrella", "A phone"], 1, "\"Is this your umbrella?\" – \"Yes, it is!\""),
     ]},
    {"explanation": "Tekil ve sayılabilen bir ismin önüne **a** ya da **an** gelir. Türkçedeki \"bir\" gibidir.\n\n- Ünsüz **sesle** başlayan kelimeler: **a** book, **a** phone, **a** university\n- Ünlü **sesle** başlayan kelimeler: **an** apple, **an** umbrella, **an** hour\n\nKural harfe değil **sese** bakar. university \"yu\" sesiyle başlar → a university. hour'da h okunmaz → an hour.",
     "examples": [{"en": "It's a pen.", "tr": "O bir kalem."},
                  {"en": "It's an orange.", "tr": "O bir portakal."},
                  {"en": "She's an English teacher.", "tr": "O bir İngilizce öğretmeni."}],
     "turkishNote": "Türkçede \"Bu kalem\" deriz, \"bir\" çoğu zaman söylenmez. İngilizcede tekil sayılabilen isimden önce a/an zorunludur: \"This is pen\" yanlış, \"This is a pen\" doğrudur."},
    [
        match([("phone", "a"), ("umbrella", "an"), ("apple", "an"), ("key", "a"), ("hour", "an")], "Ünlü sesle başlayan kelimeler an alır. hour'da h okunmaz."),
        gap("It's ___ umbrella.", ["an"], "umbrella ünlü sesle başlar → an."),
        gap("It's ___ wallet.", ["a"], "wallet ünsüz sesle başlar → a."),
        mc("Hangisi doğru?", ["an university", "a university"], 1, "university \"yu\" sesiyle başlar, yani ünsüz ses → a.", {0: "Harfe değil sese bakın: \"yu-niversity\" → a."}),
        mc("Hangisi doğru?", ["a hour", "an hour"], 1, "hour'daki h okunmaz, kelime ünlü sesle başlar → an."),
        mc("Hangisi doğru?", ["This is pen.", "This is a pen.", "This is an pen."], 1, "Tekil sayılabilen isimden önce a/an gerekir; pen ünsüzle başlar → a.", {0: "a/an eksik! Tekil isimden önce zorunludur."}),
        order(["is", "It", "old", "an", "watch"], "It is an old watch.", "Sıfat ünlüyle başlıyorsa an: an old watch.", "O eski bir kol saati."),
        listen("In my bag there's a phone, an apple and a book.", "Çantada hangisi yok?", ["Telefon", "Elma", "Şemsiye"], 2, "Telefon, elma ve kitap var; şemsiye yok."),
        typ("a mı an mı? ___ egg", ["an", "An"], "egg ünlü sesle başlar → an egg."),
        mc("\"Bu bir anahtar.\"", ["This is a key.", "This is key.", "This is an key."], 0, "key ünsüz sesle başlar → a key."),
    ],
    {"kind": "speaking", "task": speak("Çantanızda ya da masanızda olan 4 eşyayı a/an ile söyleyin.",
                                       "In my bag, I have a phone, a wallet, an umbrella and a book.",
                                       ["a/an doğru seçildi", "Eşya isimleri doğru", "Telaffuz anlaşılır"])},
)
# ---------------- Ders 2 ----------------
u.lesson(
    "Çoğullar", "Eşyaları ve insanları çoğul olarak söyleyebilirim.",
    {"kind": "dialogue", "title": "Taşınma günü", "lines": [
        {"speaker": "Mum", "text": "How many boxes are in the car?"},
        {"speaker": "Can", "text": "Six boxes and two bags."},
        {"speaker": "Mum", "text": "And where are the glasses and the knives?"},
        {"speaker": "Can", "text": "They're in the big box."},
        {"speaker": "Mum", "text": "Great. Two men from the company are here to help."}],
     "questions": [
        mc("How many boxes are in the car?", ["Two", "Six", "Eight"], 1, "\"Six boxes and two bags.\""),
        mc("Who is here to help?", ["Two women", "Two men", "Can's friends"], 1, "\"Two men from the company are here.\""),
     ]},
    {"explanation": "Çoğul yapmak için çoğu isme **-s** eklenir: book → book**s**, key → key**s**.\n\n| Kural | Örnek |\n|---|---|\n| -s, -ss, -sh, -ch, -x ile bitenler: **-es** | box → box**es**, watch → watch**es**, glass → glass**es** |\n| ünsüz + y ile bitenler: **-ies** | city → cit**ies**, baby → bab**ies** |\n| -f / -fe ile bitenlerin çoğu: **-ves** | knife → kni**ves**, wife → wi**ves** |\n| düzensiz | man → **men**, woman → **women**, child → **children**, person → **people** |\n\nünlü + y ile bitenler yalnızca -s alır: key → keys, boy → boys.",
     "examples": [{"en": "two watches", "tr": "iki kol saati"},
                  {"en": "three cities", "tr": "üç şehir"},
                  {"en": "five people", "tr": "beş kişi"}],
     "turkishNote": "Türkçede sayıdan sonra isim tekil kalır: \"iki kitap\". İngilizcede sayı birden büyükse isim çoğul olur: two books. \"two book\" yanlıştır."},
    [
        match([("box", "boxes"), ("city", "cities"), ("man", "men"), ("knife", "knives"), ("child", "children")], "Tekil → çoğul"),
        gap("one watch, two ___", ["watches"], "-ch ile biten isim -es alır."),
        gap("one key, three ___", ["keys"], "ünlü + y (ey) ile bitiyor → yalnızca -s."),
        gap("one baby, two ___", ["babies"], "ünsüz + y → -ies."),
        mc("\"İki kitap\" İngilizcede:", ["two book", "two books", "two bookes"], 1, "Sayı birden büyükse isim çoğul olur: two books.", {0: "Türkçeden farklı olarak sayıdan sonra çoğul gerekir."}),
        mc("person kelimesinin çoğulu:", ["persons", "people", "peoples"], 1, "person → people (düzensiz)."),
        mc("Hangisi doğru?", ["Three womans are here.", "Three women are here.", "Three woman are here."], 1, "woman → women (düzensiz)."),
        listen("I have two brothers, three sisters and four cousins.", "Konuşanın kaç kız kardeşi var?", ["İki", "Üç", "Dört"], 1, "\"three sisters\""),
        typ("Çoğulunu yazın: glass", ["glasses", "Glasses"], "-ss ile biten → -es: glasses."),
        order(["people", "Ten", "are", "here"], "Ten people are here.", "Sayı + çoğul isim (people) + are.", "Burada on kişi var."),
    ],
    {"kind": "writing", "task": write("Odanızda kaçar tane olan 4 eşyayı yazın (sayı + çoğul).",
                                      "In my room, I have two lamps, three bags, ten books and one laptop.",
                                      ["Sayıdan sonra çoğul isim", "-es/-ies kuralları doğru", "Tekil eşya için a/an ya da one"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "Bu ve şu", "this ve that ile yakındaki ve uzaktaki bir şeyi gösterebilirim.",
    {"kind": "dialogue", "title": "Mağazada", "lines": [
        {"speaker": "Ece", "text": "Excuse me, how much is this bag?"},
        {"speaker": "Assistant", "text": "It's 40 pounds."},
        {"speaker": "Ece", "text": "And that umbrella over there?"},
        {"speaker": "Assistant", "text": "That's 15 pounds."},
        {"speaker": "Ece", "text": "OK. This bag, please."}],
     "questions": [
        mc("How much is the bag?", ["15 pounds", "40 pounds", "14 pounds"], 1, "\"It's 40 pounds.\""),
        mc("What does Ece buy?", ["The bag", "The umbrella", "Both"], 0, "\"This bag, please.\""),
     ]},
    {"explanation": "Tekil bir şeyi gösterirken:\n\n- **this** = bu (yakında, elimizde)\n- **that** = şu, o (uzakta)\n\nSorusu: **What's this?** / **What's that?** Cevapta \"it\" kullanılır: **It's** a key.\n\nthis ve that ismin önünde de kullanılır: **this** phone, **that** car.",
     "examples": [{"en": "What's this? – It's a pen.", "tr": "Bu ne? – Bir kalem."},
                  {"en": "Is that your car?", "tr": "Şu senin araban mı?"},
                  {"en": "This book is very good.", "tr": "Bu kitap çok iyi."}],
     "turkishNote": "Cevap verirken this/that tekrarlanmaz, \"it\" kullanılır: \"What's this?\" – \"It's a watch.\" (\"This is a watch\" da doğru ama daha az doğal.)"},
    [
        mc("Elinizdeki telefonu gösteriyorsunuz:", ["This is my phone.", "That is my phone."], 0, "Yakındaki için this."),
        mc("Karşı yoldaki arabayı gösteriyorsunuz:", ["This is my car.", "That's my car."], 1, "Uzaktaki için that."),
        gap("What's ___? (elinizdeki bir şey)", ["this"], "Yakındaki → this."),
        mc("\"What's this?\" sorusuna en doğal cevap:", ["It's a key.", "This a key.", "Is a key."], 0, "Cevapta it kullanılır: It's a key.", {2: "Özne eksik: It's a key."}),
        gap("Is ___ your umbrella over there?", ["that"], "over there (orada) → uzak → that."),
        order(["your", "Is", "this", "wallet", "?"], "Is this your wallet?", "Soru: Is + this + ...?", "Bu senin cüzdanın mı?"),
        mc("Hangisi doğru?", ["This book is good.", "This is book good.", "Book this is good."], 0, "this + isim + is + sıfat."),
        listen("What's that? – It's a bottle of water.", "Uzaktaki şey ne?", ["Bir şişe su", "Bir kutu", "Bir telefon"], 0, "\"a bottle of water\""),
        typ("İngilizce yazın: \"Şu benim kol saatim.\"", variants("That's my watch.", "That is my watch."), "Uzak → that + is + my watch."),
        mc("\"Bu ne?\" İngilizcede:", ["What's this?", "What this is?", "This what?"], 0, "Soru kelimesi + is + this: What's this?"),
    ],
    {"kind": "speaking", "task": speak("JAI size bir eşya resmi gösterip \"What's this?\" diye soracak. Cevaplayın ve kime ait olduğunu söyleyin.",
                                       "It's a watch. It's my father's watch.",
                                       ["It's a/an ... ile cevap verdi", "a/an doğru", "'s ya da iyelik sıfatı kullandı"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Bunlar ve şunlar", "these ve those ile birden fazla şeyi gösterebilirim.",
    {"kind": "dialogue", "title": "Pazarda", "lines": [
        {"speaker": "Tom", "text": "What are these?"},
        {"speaker": "Seller", "text": "They're figs from Aydın. They're very sweet."},
        {"speaker": "Tom", "text": "And what are those red things?"},
        {"speaker": "Seller", "text": "Those are pomegranates."},
        {"speaker": "Tom", "text": "OK, these figs and two of those, please."}],
     "questions": [
        mc("Where are the figs from?", ["Aydın", "Antalya", "Ankara"], 0, "\"They're figs from Aydın.\""),
        mc("What colour are the pomegranates?", ["Black", "Red", "White"], 1, "\"those red things\""),
     ]},
    {"explanation": "Çoğul şeyleri gösterirken:\n\n| | Tekil | Çoğul |\n|---|---|---|\n| yakın | this | **these** |\n| uzak | that | **those** |\n\nSorusu: **What are these/those?** Cevapta **they** kullanılır: **They're** keys.",
     "examples": [{"en": "These are my keys.", "tr": "Bunlar benim anahtarlarım."},
                  {"en": "What are those?", "tr": "Şunlar ne?"},
                  {"en": "Those people are my cousins.", "tr": "Şu insanlar benim kuzenlerim."}],
     "turkishNote": "this/that'in çoğulu ayrı kelimelerdir: these/those. \"This are\" ya da \"these is\" yanlıştır. Ayrıca \"glasses\" (gözlük) her zaman çoğul olduğu için \"These are my glasses\" denir."},
    [
        match([("this", "these"), ("that", "those"), ("it", "they"), ("is", "are")], "Tekil → çoğul"),
        gap("___ are my books. (elimde)", ["These"], "Yakın + çoğul → these."),
        gap("Are ___ your children over there?", ["those"], "Uzak + çoğul → those."),
        mc("Hangisi doğru?", ["These is my keys.", "These are my keys.", "This are my keys."], 1, "these + are.", {0: "these çoğul olduğu için are gerekir.", 2: "Çoğul için this değil these."}),
        mc("\"What are these?\" sorusuna cevap:", ["It's pens.", "They're pens.", "There pens."], 1, "Çoğul cevap: They're ..."),
        mc("Hangisi doğru?", ["This is my glasses.", "These are my glasses."], 1, "glasses (gözlük) her zaman çoğuldur."),
        order(["are", "those", "What", "?"], "What are those?", "What + are + those?", "Şunlar ne?"),
        listen("These are my new shoes and those are my old shoes.", "Konuşanın yakınındaki ayakkabılar:", ["Yeni", "Eski"], 0, "these (yakın) = new shoes."),
        typ("Çoğul yapın: \"That is my bag.\"", variants("Those are my bags."), "that → those, is → are, bag → bags."),
        mc("Masanızdaki iki kalemi gösteriyorsunuz:", ["These are my pens.", "Those are my pens.", "This is my pens."], 0, "Yakın + çoğul → these."),
    ],
    {"kind": "speaking", "task": speak("Odanızdaki çoğul eşyaları gösterin: yakındakiler için these, uzaktakiler için those.",
                                       "These are my books. Those are my shoes.",
                                       ["these/those doğru seçildi", "are kullandı", "İsimler çoğul"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Renkler", "Eşyaların rengini ve boyutunu söyleyip sorabilirim.",
    {"kind": "dialogue", "title": "Kayıp çanta", "lines": [
        {"speaker": "Officer", "text": "What colour is your bag?"},
        {"speaker": "Ali", "text": "It's blue. It's a big blue bag."},
        {"speaker": "Officer", "text": "Is this your bag?"},
        {"speaker": "Ali", "text": "No, it isn't. My bag is dark blue, and it's new."},
        {"speaker": "Officer", "text": "What about that one?"},
        {"speaker": "Ali", "text": "Yes! That's my bag!"}],
     "questions": [
        mc("What colour is Ali's bag?", ["Black", "Dark blue", "Red"], 1, "\"My bag is dark blue.\""),
        mc("Is Ali's bag old?", ["Yes, it is.", "No, it isn't. It's new."], 1, "\"it's new\""),
     ]},
    {"explanation": "Renk sormak için: **What colour is it?** / **What colour are they?**\n\nRenkler: red, blue, green, yellow, black, white, brown, grey, orange, pink, purple\n\nSıfatlar ismin **önüne** gelir. Boyut, renkten önce söylenir:\n\n- a **big blue** bag\n- a **small red** car\n- **new black** shoes\n\nAçık ve koyu: **light** blue (açık mavi), **dark** blue (koyu mavi).",
     "examples": [{"en": "What colour is your phone? – It's white.", "tr": "Telefonun ne renk? – Beyaz."},
                  {"en": "I have a small black bag.", "tr": "Küçük siyah bir çantam var."},
                  {"en": "Her eyes are green.", "tr": "Onun gözleri yeşil."}],
     "turkishNote": "Türkçede de sıfat isimden önce gelir, bu yüzden sıra kolaydır: \"büyük mavi çanta\" = big blue bag. Ama \"What colour\" sorusunda \"is\" unutulmamalı: \"What colour your car?\" yanlış, \"What colour is your car?\" doğru."},
    [
        match([("red", "kırmızı"), ("green", "yeşil"), ("yellow", "sarı"), ("brown", "kahverengi"), ("grey", "gri")], "Renkleri eşleştirin."),
        mc("Hangisi doğru?", ["a blue big bag", "a big blue bag", "a bag big blue"], 1, "Boyut + renk + isim: a big blue bag."),
        gap("What colour ___ your car?", ["is"], "What colour + is + tekil isim?"),
        gap("What colour ___ her eyes?", ["are"], "eyes çoğul → are."),
        mc("\"koyu yeşil\" İngilizcede:", ["dark green", "light green", "deep green"], 0, "Koyu = dark, açık = light."),
        order(["a", "car", "small", "red", "It's"], "It's a small red car.", "a + boyut + renk + isim", "Küçük kırmızı bir araba."),
        mc("Hangisi doğru?", ["My shoes are blacks.", "My shoes are black.", "My blacks shoes."], 1, "Sıfatlar çoğul eki almaz."),
        listen("My umbrella is small and yellow. It's in my bag.", "Şemsiye ne renk?", ["Sarı", "Yeşil", "Kırmızı"], 0, "\"small and yellow\""),
        typ("İngilizce yazın: \"Benim büyük siyah bir köpeğim var.\"", variants("I have a big black dog.", "I've got a big black dog."), "a + big + black + dog"),
        mc("\"What colour are your keys?\"", ["It's grey.", "They're grey.", "Are grey."], 1, "keys çoğul → They're."),
    ],
    {"kind": "speaking", "task": speak("Kayıp eşya bürosundasınız. Kaybolan eşyanızı anlatın: ne, ne renk, büyük mü küçük mü, yeni mi eski mi?",
                                       "I have a lost bag. It's a big black bag. It's new.",
                                       ["Eşya ismi ve a/an", "Sıfat sırası (boyut + renk + isim)", "What colour sorusuna doğru cevap"])},
)

u.test([
    gap("It's ___ orange.", ["an"], "orange ünlüyle başlar → an."),
    mc("Hangisi doğru?", ["a hour", "an hour", "an university"], 1, "hour'da h okunmaz → an hour."),
    gap("one city, two ___", ["cities"], "ünsüz + y → -ies"),
    mc("child kelimesinin çoğulu:", ["childs", "children", "childrens"], 1, "Düzensiz: children."),
    mc("\"Beş kitap\":", ["five book", "five books", "five a books"], 1, "Sayıdan sonra çoğul."),
    mc("Uzaktaki bir arabayı gösteriyorsunuz:", ["This is my car.", "That's my car.", "These are my car."], 1, "Uzak + tekil → that."),
    gap("___ are my keys. (elimde)", ["These"], "Yakın + çoğul → these."),
    mc("\"What are those?\"", ["It's apples.", "They're apples.", "Those apple."], 1, "Çoğul → They're."),
    order(["a", "bag", "big", "It's", "brown"], "It's a big brown bag.", "boyut + renk + isim", "Büyük kahverengi bir çanta."),
    gap("What colour ___ your shoes?", ["are"], "shoes çoğul → are."),
    mc("Hangisi doğru?", ["These is my glasses.", "These are my glasses.", "This is my glasses."], 1, "glasses her zaman çoğul: These are."),
    listen("Excuse me, is this your wallet? – No, it isn't. My wallet is red.", "Konuşanın cüzdanı ne renk?", ["Kırmızı", "Kahverengi", "Siyah"], 0, "\"My wallet is red.\""),
    typ("Çoğulunu yazın: knife", ["knives", "Knives"], "-fe → -ves: knives."),
    mc("Hangisi doğru?", ["Three persons are here.", "Three people are here.", "Three peoples are here."], 1, "person → people."),
    write("Çantanızda ne olduğunu 4 cümleyle anlatın: eşyalar, renkleri, boyutları.",
          "In my bag, I have a small black wallet and two pens. I have an old phone. These are my keys. They're grey.",
          ["a/an doğru", "Çoğullar doğru", "Sıfat sırası doğru", "this/these doğru"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

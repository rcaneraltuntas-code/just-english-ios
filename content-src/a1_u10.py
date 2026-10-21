"""A1 Ünite 10: Alışveriş."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("A1", 10, "Alışveriş", "Shopping",
         "Mağazada fiyat sorabilir, beden ve renk isteyebilir, bir şeyi deneyip satın alabilirim.",
         ["sayılar 20–1000 ve fiyatlar", "How much / How many", "nesne zamirleri: it / them", "too + sıfat", "Which one? / one / ones"],
         ["kıyafetler", "beden ve fiyat", "mağaza ifadeleri"],
         {"title": "Pazar yeri", "durationMinutes": 45,
          "goal": "Sınıf iki gruba ayrılır: satıcılar ve müşteriler. Her müşterinin bir alışveriş listesi ve 1000 liralık bütçesi vardır. Fiyat sorup beden ve renk isteyerek listedeki her şeyi bütçeyi aşmadan almaya çalışırlar; sonra roller değişir."})

u.vocab([
    ("clothes", "kıyafetler", "I need some new clothes.", "Yeni kıyafetlere ihtiyacım var.", "Her zaman çoğul; tekili yok."),
    ("shirt", "gömlek", "He's wearing a white shirt.", "Beyaz bir gömlek giyiyor.", None),
    ("T-shirt", "tişört", "This T-shirt is cotton.", "Bu tişört pamuklu.", None),
    ("trousers", "pantolon", "These trousers are too long.", "Bu pantolon çok uzun.", "Her zaman çoğul: a pair of trousers. Amerikan: pants."),
    ("jeans", "kot pantolon", "I usually wear jeans.", "Genelde kot giyerim.", "Çoğul: these jeans."),
    ("dress", "elbise", "That's a beautiful dress.", "Çok güzel bir elbise.", None),
    ("skirt", "etek", "She has a long black skirt.", "Uzun siyah bir eteği var.", None),
    ("jacket", "ceket, mont", "Take your jacket. It's cold.", "Montunu al, hava soğuk.", None),
    ("coat", "palto", "I need a warm coat for winter.", "Kış için sıcak bir paltoya ihtiyacım var.", None),
    ("jumper", "kazak", "This jumper is very warm.", "Bu kazak çok sıcak tutuyor.", "Amerikan: sweater."),
    ("shoes", "ayakkabı", "Where are my shoes?", "Ayakkabılarım nerede?", None),
    ("trainers", "spor ayakkabı", "I wear trainers at the gym.", "Spor salonunda spor ayakkabı giyerim.", "Amerikan: sneakers."),
    ("hat", "şapka", "Wear a hat in the sun.", "Güneşte şapka tak.", None),
    ("wear", "giymek, giyinik olmak", "I wear a uniform at work.", "İşte üniforma giyerim.", None),
    ("size", "beden, numara", "What size are you? – Medium.", "Bedenin ne? – Orta.", "small (S), medium (M), large (L)"),
    ("try on", "denemek (kıyafet)", "Can I try it on?", "Deneyebilir miyim?", "try it on (it ortada)."),
    ("fitting room", "deneme kabini", "The fitting rooms are over there.", "Deneme kabinleri şurada.", None),
    ("price", "fiyat", "The price is on the label.", "Fiyat etikette yazıyor.", None),
    ("expensive", "pahalı", "These shoes are too expensive.", "Bu ayakkabılar çok pahalı.", None),
    ("cheap", "ucuz", "This market is cheap.", "Bu pazar ucuz.", None),
    ("sale", "indirim", "Everything is 50% off in the sale.", "İndirimde her şey %50 indirimli.", "on sale / in the sale"),
    ("pay", "ödemek", "Can I pay by card?", "Kartla ödeyebilir miyim?", "pay by card / pay in cash"),
    ("hundred", "yüz", "It's two hundred lira.", "İki yüz lira.", "two hundred (two hundreds değil)."),
    ("thousand", "bin", "A thousand people work here.", "Burada bin kişi çalışıyor.", None),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Kıyafetler", "Kıyafetlerin adını söyleyip ne giydiğimi anlatabilirim.",
    {"kind": "text", "title": "Moda blogu: Bir haftam", "body": "Hi, I'm Defne and I'm a teacher. People often ask me: \"What do you wear to work?\"\n\nFrom Monday to Thursday I usually wear trousers, a shirt and comfortable shoes. I stand all day!\n\nOn Fridays our school is casual, so I wear jeans, a T-shirt and trainers.\n\nAt the weekend I love wearing dresses. In winter I always wear my big red coat and a hat.",
     "questions": [
        mc("What does Defne wear on Fridays?", ["Trousers and a shirt", "Jeans, a T-shirt and trainers", "A dress"], 1, "\"On Fridays ... I wear jeans, a T-shirt and trainers.\""),
        mc("Why does she wear comfortable shoes?", ["She walks to school.", "She stands all day.", "They're cheap."], 1, "\"I stand all day!\""),
     ]},
    {"explanation": "**wear** = giymek / üzerinde olmak. Kıyafet, ayakkabı, şapka, gözlük, saat için de kullanılır.\n\n- I **wear** jeans at the weekend.\n- She **wears** glasses.\n\n**Hep çoğul olan kıyafetler:** trousers, jeans, shorts, shoes, trainers, glasses. Bunlarla **are** ve **these/those** kullanılır:\n\n- My jeans **are** blue. (~~My jeans is~~)\n- **These** trousers are nice.\n\nTek bir tane için: **a pair of** trousers / shoes (bir pantolon, bir çift ayakkabı).",
     "examples": [{"en": "I always wear a jacket in autumn.", "tr": "Sonbaharda hep ceket giyerim."},
                  {"en": "Your shoes are dirty!", "tr": "Ayakkabıların kirli!"},
                  {"en": "I want to buy a pair of jeans.", "tr": "Bir kot pantolon almak istiyorum."}],
     "turkishNote": "Türkçede \"pantolon\" tekildir (bu pantolon), İngilizcede trousers çoğuldur (these trousers are). \"Şapka takmak\", \"gözlük takmak\" İngilizcede de wear: wear a hat, wear glasses."},
    [
        match([("jumper", "kazak"), ("skirt", "etek"), ("coat", "palto"), ("trainers", "spor ayakkabı"), ("dress", "elbise")], "Kıyafetleri eşleştirin."),
        mc("Hangisi doğru?", ["My jeans is new.", "My jeans are new."], 1, "jeans hep çoğul → are."),
        mc("Hangisi doğru?", ["This trousers are nice.", "These trousers are nice."], 1, "trousers çoğul → these."),
        gap("She ___ glasses. (takar)", ["wears"], "wear + -s (she)."),
        gap("I need a ___ of shoes for the wedding.", ["pair"], "a pair of shoes = bir çift ayakkabı."),
        mc("Kışın ne giyilir?", ["a coat", "shorts", "a T-shirt"], 0, "Soğukta palto."),
        order(["usually", "I", "wear", "jeans", "at", "the", "weekend"], "I usually wear jeans at the weekend.", "Sıklık zarfı fiilden önce.", "Hafta sonu genelde kot giyerim."),
        listen("Today I'm in a hurry, so I wear my black jeans, a grey jumper and my old trainers.", "Kazak ne renk?", ["Siyah", "Gri", "Beyaz"], 1, "\"a grey jumper\""),
        typ("İngilizce yazın: \"İşte üniforma giyerim.\"", variants("I wear a uniform at work."), "wear a uniform + at work."),
        mc("\"What do you wear to work?\" cevabı:", ["A shirt and trousers.", "By bus.", "At nine."], 0, "Ne giyiyorsun → kıyafet."),
    ],
    {"kind": "speaking", "task": speak("Hafta içi ve hafta sonu genelde ne giydiğinizi anlatın. En az 4 kıyafet ve renk kullanın.",
                                       "On weekdays I wear a white shirt, black trousers and black shoes. At the weekend I usually wear jeans, a blue jumper and trainers.",
                                       ["Kıyafet isimleri doğru", "Çoğul kıyafetlerde are/these", "wear ve sıklık zarfı doğru"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "Büyük sayılar ve fiyatlar", "20'den 1000'e kadar sayıları ve fiyatları söyleyip anlayabilirim.",
    {"kind": "dialogue", "title": "Pazarda", "lines": [
        {"speaker": "Customer", "text": "Excuse me, how much is this scarf?"},
        {"speaker": "Seller", "text": "It's one hundred and fifty lira."},
        {"speaker": "Customer", "text": "And how much are those gloves?"},
        {"speaker": "Seller", "text": "They're ninety-five lira."},
        {"speaker": "Customer", "text": "OK, I'll take the scarf and the gloves, please."},
        {"speaker": "Seller", "text": "That's two hundred and forty-five lira."}],
     "questions": [
        mc("How much is the scarf?", ["115 lira", "150 lira", "250 lira"], 1, "\"one hundred and fifty\""),
        mc("How much is everything?", ["245 lira", "195 lira", "205 lira"], 0, "\"two hundred and forty-five lira\""),
     ]},
    {"explanation": "**Onluklar:** twenty (20), thirty (30), forty (40), fifty (50), sixty (60), seventy (70), eighty (80), ninety (90)\n\n- 21 = twenty**-**one, 47 = forty**-**seven (tire ile)\n- Dikkat: **forty** (fourty değil)\n\n**Yüzler ve binler:**\n\n- 100 = **a / one hundred**\n- 350 = three hundred **and** fifty\n- 999 = nine hundred **and** ninety-nine\n- 1000 = **a / one thousand**\n\nİngiliz İngilizcesinde yüzlerden sonra **and** söylenir. hundred ve thousand çoğul -s almaz: ~~two hundreds~~.\n\n**Fiyat sormak:** How much **is** this hat? / How much **are** these shoes? – **It's** / **They're** 300 lira.",
     "examples": [{"en": "It's sixty-five lira.", "tr": "65 lira."},
                  {"en": "These boots are four hundred and twenty lira.", "tr": "Bu botlar 420 lira."},
                  {"en": "How much is it altogether?", "tr": "Hepsi ne kadar?"}],
     "turkishNote": "thirteen (13) ile thirty (30) dinlerken kolay karışır: -teen'de vurgu sondadır (thir-TEEN), -ty'de baştadır (THIR-ty). Türkçedeki gibi İngilizcede de sayıdan sonra para birimi tekil kalabilir: 50 lira; ama dollar ve pound çoğul olur: 50 dollars, 20 pounds."},
    [
        match([("40", "forty"), ("15", "fifteen"), ("50", "fifty"), ("90", "ninety"), ("13", "thirteen")], "Sayıları eşleştirin."),
        mc("78", ["seventy-eight", "seventeen-eight", "eighty-seven"], 0, "70 = seventy, + eight."),
        mc("Hangisi doğru yazılmış?", ["fourty", "forty"], 1, "forty (u yok)."),
        mc("300", ["three hundreds", "three hundred", "thirty hundred"], 1, "hundred -s almaz."),
        typ("Rakamla yazın: \"five hundred and sixty\"", variants("560"), "500 + 60 = 560"),
        typ("Yazıyla yazın: 250", variants("two hundred and fifty", "two hundred fifty", "two-hundred and fifty"), "two hundred and fifty"),
        gap("How much ___ these shoes?", ["are"], "shoes çoğul → are."),
        gap("How much is this hat? – ___ eighty lira.", ["It's", "It is"], "Tekil → It's."),
        listen("The jacket is seven hundred and thirty lira.", "Ceket kaç lira?", ["370", "730", "713"], 1, "seven hundred and thirty = 730."),
        listen("These are thirteen pounds, and those are thirty pounds.", "\"those\" kaç pound?", ["13", "30", "33"], 1, "THIR-ty = 30."),
    ],
    {"kind": "speaking", "task": speak("JAI pazarcı. Üç ürünün fiyatını sorun (biri çoğul olsun) ve toplamı sorun.",
                                       "How much is this T-shirt? How much are those socks? OK, I'll take them. How much is it altogether?",
                                       ["How much is / are doğru", "Sayıları anladı ve tekrar etti", "I'll take ... ile satın aldı"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "How much? How many?", "Miktar ve sayı sorularını doğru kurabilirim.",
    {"kind": "dialogue", "title": "Alışveriş listesi", "lines": [
        {"speaker": "Ece", "text": "We need T-shirts for the volleyball team. How many players are there?"},
        {"speaker": "Kerem", "text": "There are twelve players."},
        {"speaker": "Ece", "text": "OK, twelve T-shirts. How much money do we have?"},
        {"speaker": "Kerem", "text": "We have two thousand lira."},
        {"speaker": "Ece", "text": "And how much is one T-shirt?"},
        {"speaker": "Kerem", "text": "It's one hundred and fifty lira. So that's one thousand eight hundred lira."}],
     "questions": [
        mc("How many players are in the team?", ["Ten", "Twelve", "Twenty"], 1, "\"There are twelve players.\""),
        mc("How much money do they have?", ["1,800 lira", "2,000 lira", "1,500 lira"], 1, "\"two thousand lira\""),
     ]},
    {"explanation": "7. ünitede sayılabilen ve sayılamayan isimleri gördük. Soru kelimesi bu farka göre değişir:\n\n| | Ne ile? | Örnek |\n|---|---|---|\n| **How many** | sayılabilen çoğul | How many **shirts** do you have? |\n| **How much** | sayılamayan | How much **money** / **time** / **water**? |\n| **How much** | fiyat | How much **is** it? |\n\n- How many **people**? (people çoğul: kişiler)\n- How much **milk** do we need?",
     "examples": [{"en": "How many brothers do you have?", "tr": "Kaç erkek kardeşin var?"},
                  {"en": "How much time do we have?", "tr": "Ne kadar vaktimiz var?"},
                  {"en": "How many people work here?", "tr": "Burada kaç kişi çalışıyor?"}],
     "turkishNote": "Türkçede \"kaç\" ve \"ne kadar\" ayrımı İngilizcedeki ayrıma çok benzer: kaç tişört = how many T-shirts, ne kadar para = how much money. Dikkat: Türkçede \"kaç\"tan sonra isim tekildir (kaç tişört), İngilizcede çoğuldur (how many T-shirts)."},
    [
        mc("How ___ apples do you want?", ["much", "many"], 1, "apples sayılabilen → many."),
        mc("How ___ water do you drink?", ["much", "many"], 0, "water sayılamayan → much."),
        mc("How ___ people are at the party?", ["much", "many"], 1, "people çoğul → many."),
        mc("How ___ is this jacket? (fiyat)", ["much", "many"], 0, "Fiyat → how much."),
        gap("How many ___ do you have? (shoe)", ["shoes", "pairs of shoes"], "how many + çoğul."),
        gap("How ___ money is in your bag?", ["much"], "money sayılamayan."),
        order(["time", "How", "much", "do", "we", "have", "?"], "How much time do we have?", "How much + isim + do + özne + fiil?", "Ne kadar vaktimiz var?"),
        listen("How many jumpers do you have? – I have five, but I only wear two.", "Konuşanın kaç kazağı var?", ["İki", "Beş", "Yedi"], 1, "\"I have five\""),
        typ("İngilizce yazın: \"Burada kaç kişi çalışıyor?\"", variants("How many people work here?"), "How many people + work here?"),
        mc("\"How much milk do we need?\" cevabı:", ["Two litres.", "Two milks.", "Twelve people."], 0, "Sayılamayan → miktar birimi."),
    ],
    {"kind": "writing", "task": write("Bir doğum günü partisi planlıyorsunuz. Arkadaşınıza How much / How many ile 4 soru yazın.",
                                      "How many people can come? How much cake do we need? How many bottles of juice do we need? How much money do we have?",
                                      ["How many + çoğul doğru", "How much + sayılamayan doğru", "Soru düzeni doğru"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Mağazada", "Beden isteyip kıyafet deneyebilir ve sorun olduğunda bunu söyleyebilirim.",
    {"kind": "dialogue", "title": "Giyim mağazasında", "lines": [
        {"speaker": "Assistant", "text": "Hello. Can I help you?"},
        {"speaker": "Zeynep", "text": "Yes, I like this jacket. Can I try it on?"},
        {"speaker": "Assistant", "text": "Of course. What size are you?"},
        {"speaker": "Zeynep", "text": "Medium, I think. ... Hmm, it's too small."},
        {"speaker": "Assistant", "text": "Here's a large. Try it on."},
        {"speaker": "Zeynep", "text": "Perfect! I'll take it. Can I pay by card?"},
        {"speaker": "Assistant", "text": "Yes, of course."}],
     "questions": [
        mc("What's the problem with the medium jacket?", ["It's too big.", "It's too small.", "It's too expensive."], 1, "\"it's too small\""),
        mc("What size does Zeynep buy?", ["Small", "Medium", "Large"], 2, "\"Here's a large.\" ... \"I'll take it.\""),
     ]},
    {"explanation": "**Nesne zamirleri:** fiilden sonra isim yerine kullanılır.\n\n| Tekil | Çoğul |\n|---|---|\n| this jacket → **it** | these shoes → **them** |\n\n- Can I try **it** on? (try on **it** değil, zamir ortaya gelir)\n- I like these jeans. I'll take **them**.\n\n**too + sıfat:** gereğinden fazla, bir sorun var.\n\n- It's **too** big. (Çok büyük, olmuyor.)\n- They're **too** expensive.\n\n**Have you got ...?** = Do you have ...? (... var mı?). Mağazada çok kullanılır: Have you got this in a medium? – Yes, we have. / Sorry, we haven't.\n\n**Mağaza ifadeleri:** Can I help you? / What size are you? / Where are the fitting rooms? / I'll take it.",
     "examples": [{"en": "These boots are too small. Have you got them in a 40?", "tr": "Bu botlar küçük. 40 numarası var mı?"},
                  {"en": "Can I try them on?", "tr": "Onları deneyebilir miyim?"},
                  {"en": "Have you got this in blue?", "tr": "Bunun mavisi var mı?"}],
     "turkishNote": "\"very\" ile \"too\" farklıdır: very expensive = çok pahalı (belki yine alırım); too expensive = fazla pahalı (alamam). \"Try on it\" yanlıştır; zamirler try ile on'un arasına girer: try it on."},
    [
        mc("Bu ayakkabılar çok büyük, ayağınıza olmuyor:", ["They're very big.", "They're too big."], 1, "Sorun var → too."),
        mc("Hangisi doğru?", ["Can I try on it?", "Can I try it on?"], 1, "try it on (zamir ortada)."),
        gap("I love these trainers. I'll take ___.", ["them"], "trainers çoğul → them."),
        gap("This dress is nice. Can I try ___ on?", ["it"], "dress tekil → it."),
        gap("This coat is ___ expensive. I can't buy it.", ["too"], "Alamıyorum → too."),
        mc("Satış danışmanının ilk sorusu:", ["Can I help you?", "Can you help me?", "Do you help?"], 0, "Yardım edebilir miyim?"),
        order(["got", "Have", "you", "this", "in", "blue", "?"], "Have you got this in blue?", "Have you got + this + in + renk?", "Bunun mavisi var mı?"),
        listen("These jeans are too long. Have you got them in a smaller size?", "Sorun ne?", ["Kot çok kısa", "Kot çok uzun", "Kot çok pahalı"], 1, "\"too long\""),
        typ("İngilizce yazın: \"Deneme kabinleri nerede?\"", variants("Where are the fitting rooms?", "Where's the fitting room?", "Where is the fitting room?"), "Where are the fitting rooms?"),
        mc("\"What size are you?\" cevabı:", ["Medium.", "Blue.", "Fifty lira."], 0, "Beden → small / medium / large."),
    ],
    {"kind": "speaking", "task": speak("JAI satış danışmanı. Bir kıyafet seçin, denemek isteyin, bir sorun söyleyin (too ...), başka beden veya renk isteyin ve satın alın.",
                                       "I like these trousers. Can I try them on? ... They're too long. Have you got them in a smaller size? ... Great, I'll take them. Can I pay by card?",
                                       ["try it/them on doğru", "too + sıfat doğru", "Have you got ... ? / I'll take it doğru"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Hangisi?", "Which one? diye sorup the red one / the blue ones gibi seçim yapabilirim.",
    {"kind": "dialogue", "title": "Hediye seçmek", "lines": [
        {"speaker": "Can", "text": "It's Mum's birthday. Let's buy her a bag."},
        {"speaker": "Aslı", "text": "Good idea. Which one? The brown one or the black one?"},
        {"speaker": "Can", "text": "The black one is nice, but it's too big."},
        {"speaker": "Aslı", "text": "OK, the brown one. And what about some earrings?"},
        {"speaker": "Can", "text": "Which ones? These silver ones are beautiful."},
        {"speaker": "Aslı", "text": "Yes, but the gold ones are cheaper. Mum likes gold too."}],
     "questions": [
        mc("Which bag do they choose?", ["The black one", "The brown one", "Both"], 1, "\"OK, the brown one.\""),
        mc("Why does Aslı like the gold earrings?", ["They're bigger.", "They're cheaper.", "They're silver."], 1, "\"the gold ones are cheaper\""),
     ]},
    {"explanation": "Aynı ismi tekrar etmemek için **one / ones** kullanırız.\n\n- **Which** bag? → **Which one**? – The red **one**. (tekil)\n- **Which** shoes? → **Which ones**? – The black **ones**. (çoğul)\n\n**Seçim yaparken:**\n\n- this one / that one\n- these ones / those ones (ya da sadece these / those)\n- the big one, the cheap ones, the one on the left\n\n**Which** seçenekler belli olduğunda kullanılır; **What** seçenekler belli değilse: What colour do you like? / Which colour, red or blue?",
     "examples": [{"en": "I don't like this one. Can I see that one?", "tr": "Bunu beğenmedim. Şunu görebilir miyim?"},
                  {"en": "Which ones do you want? – The small ones.", "tr": "Hangilerini istiyorsun? – Küçük olanları."},
                  {"en": "The blue one is cheaper.", "tr": "Mavi olan daha ucuz."}],
     "turkishNote": "Türkçede \"mavi olan\", \"mavisi\" deriz; İngilizcede sıfat tek başına kalamaz: \"the blue\" değil \"the blue one\" denir. \"cheaper\" (daha ucuz) karşılaştırma yapısını A2'de ayrıntılı göreceğiz."},
    [
        mc("I don't like this shirt. Can I see the white ___?", ["one", "ones"], 0, "shirt tekil → one."),
        mc("These shoes are too small. Have you got bigger ___?", ["one", "ones"], 1, "shoes çoğul → ones."),
        mc("Hangisi doğru?", ["I want the red.", "I want the red one."], 1, "Sıfat yalnız kalmaz: the red one."),
        gap("___ one do you like, the blue one or the green one?", ["Which"], "Seçenek belli → Which."),
        gap("Which ___ do you want? – The black ones.", ["ones"], "Cevap çoğul → ones."),
        mc("Seçenekler belli değil: \"___ is your favourite colour?\"", ["What", "Which"], 0, "Seçenek yok → What."),
        order(["one", "The", "on", "the", "left", "is", "cheaper"], "The one on the left is cheaper.", "The one + yer + is + sıfat.", "Soldaki daha ucuz."),
        listen("Which jacket do you want? – Not the long one. The short one, please.", "Konuşan hangisini istiyor?", ["Uzun olanı", "Kısa olanı", "İkisini de"], 1, "\"The short one, please.\""),
        typ("İngilizce yazın: \"Şunu görebilir miyim?\"", variants("Can I see that one?", "Can I see that one, please?", "Can I see that?"), "Can I see that one?"),
        match([("Which bag?", "Which one?"), ("Which shoes?", "Which ones?"), ("the black bag", "the black one"), ("the cheap socks", "the cheap ones")], "Eşleştirin."),
    ],
    {"kind": "speaking", "task": speak("Bir aile üyenize hediye seçiyorsunuz. JAI satış danışmanı iki seçenek gösterecek. Which one ile sorun, one/ones ile seçiminizi ve nedenini söyleyin, fiyatı sorup satın alın.",
                                       "Which one is better for a man, the grey one or the blue one? I like the blue one. How much is it? Great, I'll take it.",
                                       ["Which one(s) doğru", "the + sıfat + one(s) doğru", "Fiyat sordu ve satın aldı"])},
)

u.test([
    mc("Hangisi doğru?", ["My trousers is black.", "My trousers are black."], 1, "trousers çoğul."),
    gap("She ___ a uniform at work.", ["wears"], "wear + -s"),
    mc("40", ["fourty", "forty", "fourteen"], 1, "forty"),
    typ("Rakamla yazın: \"three hundred and eighty-five\"", variants("385"), "385"),
    mc("600", ["six hundreds", "six hundred"], 1, "hundred -s almaz."),
    gap("How much ___ these gloves?", ["are"], "Çoğul → are."),
    mc("How ___ brothers do you have?", ["much", "many"], 1, "brothers sayılabilen."),
    mc("How ___ sugar do you want?", ["much", "many"], 0, "sugar sayılamayan."),
    mc("Hangisi doğru?", ["Can I try on them?", "Can I try them on?"], 1, "try them on"),
    gap("I like this hat. I'll take ___.", ["it"], "Tekil → it."),
    mc("Ceket fazla pahalı, alamıyorsunuz:", ["It's very expensive.", "It's too expensive."], 1, "too"),
    gap("These boots are too small. Have you got bigger ___?", ["ones"], "Çoğul → ones."),
    listen("How much is the dress? – It's eight hundred and fifty lira, but it's in the sale. Now it's four hundred.", "Elbisenin indirimli fiyatı ne?", ["850", "400", "450"], 1, "\"Now it's four hundred.\""),
    order(["you", "Have", "got", "this", "in", "a", "small", "?"], "Have you got this in a small?", "Have you got + this + in + beden?", "Bunun small'u var mı?"),
    write("Bir mağaza diyaloğu yazın (6–8 satır): selamlama, ürün ve beden isteme, deneme, bir sorun (too ...), fiyat sorma ve satın alma.",
          "A: Hello. Can I help you?\nB: Yes. Have you got this shirt in a medium?\nA: Here you are.\nB: Can I try it on? ... It's too long.\nA: Try this one.\nB: Perfect. How much is it?\nA: It's three hundred lira.\nB: I'll take it. Can I pay by card?",
          ["Mağaza ifadeleri doğru", "it/them ve one/ones doğru", "Sayılar ve fiyat doğru", "too + sıfat doğru"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

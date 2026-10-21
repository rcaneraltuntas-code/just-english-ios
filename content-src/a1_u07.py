"""A1 Ünite 7: Kafede."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("A1", 7, "Kafede", "At the Café",
         "Bir kafede ya da restoranda kibarca sipariş verebilir, fiyat sorup hesabı isteyebilirim.",
         ["sayılabilen / sayılamayan isimler", "some / any", "would like / Can I have...?", "How much...?"],
         ["yiyecek ve içecek", "kafe ve restoran ifadeleri", "fiyatlar"],
         {"title": "Just Café", "durationMinutes": 45,
          "goal": "Sınıf bir kafeye dönüşür: öğrenciler sırayla garson ve müşteri olur, menüden sipariş verir, fiyat sorar ve hesap ister."})

u.vocab([
    ("water", "su", "Can I have some water, please?", "Biraz su alabilir miyim lütfen?", "Sayılamaz: a water değil, some water / a glass of water."),
    ("coffee", "kahve", "A black coffee, please.", "Sade bir kahve lütfen.", "Siparişte \"a coffee\" (bir fincan kahve) denebilir."),
    ("tea", "çay", "Would you like some tea?", "Biraz çay ister misin?", None),
    ("milk", "süt", "Do you have any milk?", "Hiç sütün var mı?", None),
    ("juice", "meyve suyu", "An orange juice, please.", "Bir portakal suyu lütfen.", None),
    ("bread", "ekmek", "There's some bread on the table.", "Masada biraz ekmek var.", "Sayılamaz: a bread değil, some bread / a loaf of bread."),
    ("cheese", "peynir", "I'd like a cheese sandwich.", "Peynirli bir sandviç istiyorum.", None),
    ("egg", "yumurta", "two eggs", "iki yumurta", None),
    ("sandwich", "sandviç", "A chicken sandwich, please.", "Tavuklu bir sandviç lütfen.", None),
    ("salad", "salata", "Would you like a salad?", "Salata ister misiniz?", None),
    ("soup", "çorba", "The soup is hot.", "Çorba sıcak.", None),
    ("cake", "kek, pasta", "a piece of chocolate cake", "bir dilim çikolatalı pasta", None),
    ("sugar", "şeker", "No sugar, thanks.", "Şekersiz, teşekkürler.", None),
    ("menu", "menü", "Can I see the menu, please?", "Menüyü görebilir miyim lütfen?", None),
    ("bill", "hesap", "Can we have the bill, please?", "Hesabı alabilir miyiz lütfen?", "Amerikan İngilizcesinde: check."),
    ("order", "sipariş vermek", "Are you ready to order?", "Sipariş vermeye hazır mısınız?", None),
    ("would like", "istemek (kibarca)", "I'd like a tea, please.", "Bir çay rica ediyorum.", "I want'ten daha kibar."),
    ("small / medium / large", "küçük / orta / büyük", "A large latte, please.", "Büyük bir latte lütfen.", None),
    ("a cup of", "bir fincan", "a cup of tea", "bir fincan çay", None),
    ("a glass of", "bir bardak", "a glass of water", "bir bardak su", None),
    ("a bottle of", "bir şişe", "a bottle of water", "bir şişe su", None),
    ("a piece of", "bir parça, bir dilim", "a piece of cake", "bir dilim pasta", None),
    ("delicious", "çok lezzetli", "This soup is delicious!", "Bu çorba çok lezzetli!", None),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Sayılabilen ve sayılamayan", "Yiyecek ve içecekleri a/an ya da some ile söyleyebilirim.",
    {"kind": "dialogue", "title": "Kahvaltı masası", "lines": [
        {"speaker": "Mum", "text": "Breakfast is ready! There's some bread, some cheese and some olives."},
        {"speaker": "Can", "text": "Is there an egg for me?"},
        {"speaker": "Mum", "text": "Yes, there are two eggs. And there's some tea in the pot."},
        {"speaker": "Can", "text": "Can I have some orange juice, too?"},
        {"speaker": "Mum", "text": "Sure, there's a bottle in the fridge."}],
     "questions": [
        mc("How many eggs are there?", ["One", "Two", "Three"], 1, "\"there are two eggs\""),
        mc("Where's the orange juice?", ["On the table", "In the fridge", "In the pot"], 1, "\"there's a bottle in the fridge\""),
     ]},
    {"explanation": "**Sayılabilen** isimler tek tek sayılır: **an** egg, **two** eggs, **a** sandwich.\n\n**Sayılamayan** isimler sayılmaz ve çoğul olmaz: water, bread, milk, cheese, sugar, rice, money.\n\n- Sayılamayanla **a/an kullanılmaz**: ~~a bread~~ → **some** bread\n- Miktar için kap ya da ölçü kullanılır: **a glass of** water, **a cup of** tea, **a piece of** cake, **a bottle of** milk.",
     "examples": [{"en": "I'd like an apple and some water.", "tr": "Bir elma ve biraz su istiyorum."},
                  {"en": "There's some milk in the fridge.", "tr": "Buzdolabında biraz süt var."},
                  {"en": "Two cups of coffee, please.", "tr": "İki fincan kahve lütfen."}],
     "turkishNote": "Türkçede \"bir ekmek\" deriz ama İngilizcede bread sayılamaz: \"a bread\" yanlıştır. \"some bread\" ya da \"a loaf of bread\" (bir somun ekmek) denir. Aynı şekilde \"money\" de sayılamaz: \"moneys\" denmez."},
    [
        match([("apple", "an"), ("water", "some"), ("sandwich", "a"), ("bread", "some"), ("egg", "an")], "Sayılabilen tekil → a/an, sayılamayan → some."),
        mc("Hangisi doğru?", ["a bread", "some bread", "breads"], 1, "bread sayılamaz → some bread.", {0: "bread sayılamaz, a ile kullanılmaz."}),
        mc("Hangisi sayılabilir?", ["milk", "sugar", "egg"], 2, "egg tek tek sayılır: one egg, two eggs."),
        gap("a ___ of water (bardak)", ["glass"], "bir bardak = a glass of"),
        gap("a ___ of cake (dilim)", ["piece"], "bir dilim = a piece of"),
        gap("two ___ of tea (fincan)", ["cups"], "two → cups"),
        mc("\"Biraz para\" İngilizcede:", ["some moneys", "some money", "a money"], 1, "money sayılamaz."),
        listen("For breakfast I have two eggs, some bread and a glass of milk.", "Konuşan kahvaltıda ne içiyor?", ["Çay", "Süt", "Meyve suyu"], 1, "\"a glass of milk\""),
        typ("İngilizce yazın: \"bir şişe su\"", ["a bottle of water", "A bottle of water"], "a bottle of + water"),
        order(["some", "There's", "cheese", "the", "in", "fridge"], "There's some cheese in the fridge.", "There's + some + sayılamaz isim.", "Buzdolabında biraz peynir var."),
    ],
    {"kind": "speaking", "task": speak("Bu sabah kahvaltıda ne yediğinizi ve içtiğinizi söyleyin (a/an, some, a cup of...).",
                                       "I have some bread, some cheese and an egg. I have a cup of tea.",
                                       ["a/an ve some doğru", "Sayılamayanlarla a/an kullanmadı", "Ölçü ifadesi kullandı"])},
)
# ---------------- Ders 2 ----------------
u.lesson(
    "Biraz, hiç", "some ve any ile miktar söyleyip sorabilirim.",
    {"kind": "dialogue", "title": "Alışveriş listesi", "lines": [
        {"speaker": "Elif", "text": "Do we have any milk?"},
        {"speaker": "Ali", "text": "No, we don't have any milk. And we don't have any eggs."},
        {"speaker": "Elif", "text": "OK. Is there any coffee?"},
        {"speaker": "Ali", "text": "Yes, there's some coffee. And there are some apples."},
        {"speaker": "Elif", "text": "So, milk and eggs. Let's go to the shop."}],
     "questions": [
        mc("What do they need to buy?", ["Coffee and apples", "Milk and eggs", "Milk and coffee"], 1, "Süt ve yumurta yok."),
        mc("Is there any coffee?", ["Yes, there is.", "No, there isn't."], 0, "\"Yes, there's some coffee.\""),
     ]},
    {"explanation": "**some** ve **any** hem sayılamayan hem çoğul sayılabilen isimlerle kullanılır.\n\n| | some / any |\n|---|---|\n| olumlu | There's **some** milk. There are **some** eggs. |\n| olumsuz | There isn't **any** milk. There aren't **any** eggs. |\n| soru | Is there **any** milk? Are there **any** eggs? |\n\n**İstisna:** Bir şey teklif ederken ya da isterken soruda da **some** kullanılır: **Would you like some** tea? **Can I have some** water?",
     "examples": [{"en": "We have some time.", "tr": "Biraz vaktimiz var."},
                  {"en": "I don't have any money.", "tr": "Hiç param yok."},
                  {"en": "Would you like some cake?", "tr": "Biraz pasta ister misin?"}],
     "turkishNote": "Türkçede \"Hiç süt var mı?\" sorusunda \"hiç\" kullanmak zorunlu değildir, İngilizcede ise any doğal olarak eklenir: \"Is there any milk?\" Olumsuzda \"I don't have some money\" yanlıştır, any gerekir."},
    [
        gap("There's ___ juice in the fridge.", ["some"], "Olumlu → some."),
        gap("We don't have ___ bread.", ["any"], "Olumsuz → any."),
        gap("Are there ___ eggs?", ["any"], "Soru → any."),
        gap("Would you like ___ coffee?", ["some"], "Teklif → some."),
        mc("Hangisi doğru?", ["I don't have some money.", "I don't have any money."], 1, "Olumsuz → any."),
        mc("Bir misafire çay teklif ediyorsunuz:", ["Would you like any tea?", "Would you like some tea?"], 1, "Teklifte some."),
        order(["any", "Is", "there", "sugar", "?"], "Is there any sugar?", "Is there + any + sayılamaz?", "Hiç şeker var mı?"),
        listen("Sorry, we don't have any chocolate cake today, but we have some apple pie.", "Bugün hangi tatlı var?", ["Çikolatalı pasta", "Elmalı turta", "İkisi de"], 1, "\"we have some apple pie\""),
        typ("Olumsuz yapın: \"There are some apples.\"", variants("There aren't any apples."), "aren't + any"),
        mc("\"Can I have ___ water, please?\"", ["some", "any", "a"], 0, "Rica → some."),
    ],
    {"kind": "speaking", "task": speak("Buzdolabınızda ne var, ne yok? 4 cümle söyleyin (some/any).",
                                       "There's some milk and some cheese. There are some eggs. There isn't any juice.",
                                       ["Olumluda some", "Olumsuzda any", "is/are doğru"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "Ne istersiniz?", "would like ile kibarca isteyip teklif edebilirim.",
    {"kind": "dialogue", "title": "Misafir", "lines": [
        {"speaker": "Selin", "text": "Come in! Would you like something to drink?"},
        {"speaker": "Tom", "text": "Yes, please. I'd like a glass of water."},
        {"speaker": "Selin", "text": "Would you like some Turkish coffee, too?"},
        {"speaker": "Tom", "text": "Oh, yes please! I love Turkish coffee."},
        {"speaker": "Selin", "text": "How would you like it? With sugar?"},
        {"speaker": "Tom", "text": "A little sugar, please. Thanks!"}],
     "questions": [
        mc("What does Tom ask for first?", ["Coffee", "Water", "Tea"], 1, "\"I'd like a glass of water.\""),
        mc("How does Tom like his coffee?", ["Without sugar", "With a little sugar", "With milk"], 1, "\"A little sugar, please.\""),
     ]},
    {"explanation": "**would like** = istemek (kibarca). **want**'tan daha naziktir.\n\n- **I'd like** (I would like) a tea, please.\n- **Would you like** some cake? – Yes, please. / No, thank you.\n- **What would you like?** – I'd like a sandwich.\n\nwould like'tan sonra fiil gelirse **to** eklenir: I'd like **to** order.",
     "examples": [{"en": "I'd like a coffee, please.", "tr": "Bir kahve rica ediyorum."},
                  {"en": "Would you like a biscuit? – No, thank you.", "tr": "Bisküvi ister misin? – Hayır, teşekkürler."},
                  {"en": "I'd like to pay, please.", "tr": "Ödemek istiyorum lütfen."}],
     "turkishNote": "\"I want a coffee\" dilbilgisi olarak doğrudur ama bir kafede kaba duyulabilir. \"I'd like\" ya da \"Can I have\" kullanın. Ayrıca \"Would you like...?\" sorusuna \"Yes, I would like\" yerine kısaca \"Yes, please.\" denir."},
    [
        mc("Garsona en kibar istek:", ["I want a tea.", "Give me a tea.", "I'd like a tea, please."], 2, "I'd like ... please en kibarıdır."),
        gap("I'___ like a sandwich, please.", ["d"], "I'd = I would."),
        gap("___ you like some cake?", ["Would"], "Teklif: Would you like...?"),
        mc("\"Would you like some tea?\" (Evet.)", ["Yes, please.", "Yes, I like.", "Yes, I would like."], 0, "Kısa ve doğal: Yes, please."),
        mc("\"Would you like some tea?\" (Hayır.)", ["No, thank you.", "No, I don't like.", "No, please."], 0, "Kibar ret: No, thank you."),
        mc("Hangisi doğru?", ["I'd like order now.", "I'd like to order now."], 1, "would like + to + fiil."),
        order(["would", "What", "like", "you", "?"], "What would you like?", "What + would + you + like?", "Ne istersiniz?"),
        listen("What would you like? – I'd like a cheese sandwich and a small orange juice, please.", "Müşteri ne içecek istiyor?", ["Büyük portakal suyu", "Küçük portakal suyu", "Su"], 1, "\"a small orange juice\""),
        typ("Kibar yapın: \"I want a coffee.\"", variants("I'd like a coffee.", "I'd like a coffee, please.", "Can I have a coffee, please?", "Could I have a coffee, please?"), "I'd like a coffee, please."),
        match([("Would you like a tea?", "Yes, please."), ("What would you like?", "A latte, please."), ("Anything else?", "No, thanks.")], "Soruyla cevabı eşleştirin."),
    ],
    {"kind": "speaking", "task": speak("JAI evinize gelen bir misafir. Ona iki şey teklif edin ve ne istediğini sorun.",
                                       "Would you like some tea? Would you like some cake? What would you like?",
                                       ["Would you like doğru", "some kullandı", "Kibar tonda"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Sipariş vermek", "Kafede başından sonuna sipariş verebilirim.",
    {"kind": "dialogue", "title": "Just Café", "lines": [
        {"speaker": "Barista", "text": "Hi! What can I get you?"},
        {"speaker": "Deniz", "text": "Can I have a latte, please?"},
        {"speaker": "Barista", "text": "Sure. Small, medium or large?"},
        {"speaker": "Deniz", "text": "Medium, please."},
        {"speaker": "Barista", "text": "Anything else?"},
        {"speaker": "Deniz", "text": "Yes, a piece of carrot cake."},
        {"speaker": "Barista", "text": "Is that for here or to take away?"},
        {"speaker": "Deniz", "text": "For here, please."}],
     "questions": [
        mc("What size is Deniz's latte?", ["Small", "Medium", "Large"], 1, "\"Medium, please.\""),
        mc("Where does Deniz eat?", ["In the café", "At home", "In the office"], 0, "\"For here, please.\""),
     ]},
    {"explanation": "**Garsonun / baristanın soruları:**\n\n- What can I get you? / Are you ready to order? (Ne alırsınız?)\n- Small, medium or large? (Boyu?)\n- Anything else? (Başka bir şey?)\n- For here or to take away? (Burada mı, paket mi?)\n\n**Müşterinin cevapları:**\n\n- **Can I have** a latte, please? / **I'd like** a latte, please.\n- That's all, thanks. (Hepsi bu, teşekkürler.)\n- For here, please. / To take away, please.",
     "examples": [{"en": "Can I have a tea, please?", "tr": "Bir çay alabilir miyim lütfen?"},
                  {"en": "Can I see the menu, please?", "tr": "Menüyü görebilir miyim lütfen?"},
                  {"en": "That's all, thank you.", "tr": "Hepsi bu, teşekkür ederim."}],
     "turkishNote": "\"please\" İngilizcede çok önemlidir; istek cümlesinin sonunda olmazsa kaba duyulabilir. Türkçedeki \"bir çay\" kısalığında \"A tea\" demek yerine \"A tea, please\" deyin."},
    [
        mc("\"Anything else?\" ne demek?", ["Başka bir şey?", "Her şey yolunda mı?", "Bir şey mi istediniz?"], 0, "Başka bir şey ister misiniz?"),
        mc("\"For here or to take away?\" (Paket istiyorsunuz.)", ["For here, please.", "To take away, please.", "Take, please."], 1, "Paket = to take away."),
        gap("___ I have a hot chocolate, please?", ["Can"], "Rica: Can I have...?"),
        gap("That's ___, thank you.", ["all"], "Hepsi bu = That's all."),
        mc("\"Small, medium or large?\"", ["Large, please.", "Yes, please.", "I'd like."], 0, "Boyu söyleyin."),
        order(["Can", "see", "I", "menu", "the", "please", "?"], "Can I see the menu, please?", "Can I + fiil + ...?", "Menüyü görebilir miyim lütfen?"),
        listen("Hi, are you ready to order? – Yes. Can I have the tomato soup and a green salad, please?", "Müşteri ne sipariş ediyor?", ["Çorba ve salata", "Sandviç ve salata", "Çorba ve sandviç"], 0, "\"the tomato soup and a green salad\""),
        typ("İngilizce yazın: \"Bir çay alabilir miyim lütfen?\"", variants("Can I have a tea, please?", "Can I have a cup of tea, please?", "Could I have a tea, please?"), "Can I have + a tea + please?"),
        match([("What can I get you?", "A cappuccino, please."), ("Small or large?", "Small, please."), ("Anything else?", "That's all, thanks."), ("For here or to take away?", "For here, please.")], "Soruyla cevabı eşleştirin."),
        mc("Kafede sipariş için en uygun cümle:", ["Give me a coffee.", "Can I have a coffee, please?", "I want coffee."], 1, "Kibar istek: Can I have..., please?"),
    ],
    {"kind": "speaking", "task": speak("JAI bir barista. Kafede bir içecek ve bir yiyecek sipariş edin; boyutu ve paket mi burada mı olduğunu söyleyin.",
                                       "Can I have a large cappuccino, please? And a piece of chocolate cake. To take away, please.",
                                       ["Can I have / I'd like kullandı", "please kullandı", "Baristanın sorularına doğru cevap"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Hesap lütfen", "Fiyat sorup hesabı isteyebilirim.",
    {"kind": "dialogue", "title": "Londra'da bir kafe", "lines": [
        {"speaker": "Ali", "text": "Excuse me, how much is a cup of tea?"},
        {"speaker": "Waiter", "text": "It's two pounds fifty."},
        {"speaker": "Ali", "text": "And how much are the muffins?"},
        {"speaker": "Waiter", "text": "They're three pounds each."},
        {"speaker": "Ali", "text": "OK, one tea and one muffin, please."},
        {"speaker": "Waiter", "text": "That's five pounds fifty, please."},
        {"speaker": "Ali", "text": "Can I pay by card?"},
        {"speaker": "Waiter", "text": "Of course."}],
     "questions": [
        mc("How much is a muffin?", ["£2.50", "£3.00", "£5.50"], 1, "\"They're three pounds each.\""),
        mc("How does Ali pay?", ["By card", "In cash", "By phone"], 0, "\"Can I pay by card?\" – \"Of course.\""),
     ]},
    {"explanation": "**Fiyat sormak:**\n\n- **How much is** the cake? (tekil) – **It's** £3.\n- **How much are** the muffins? (çoğul) – **They're** £3 each.\n\n**Fiyat okumak:** £2.50 = two pounds fifty, €4.99 = four euros ninety-nine, 120 TL = a hundred and twenty lira.\n\n**Ödeme:**\n\n- **Can I have the bill, please?** (Hesap lütfen.)\n- **Can I pay by card?** / **in cash?**",
     "examples": [{"en": "How much is this sandwich?", "tr": "Bu sandviç ne kadar?"},
                  {"en": "That's twelve euros, please.", "tr": "On iki avro lütfen."},
                  {"en": "Can we have the bill, please?", "tr": "Hesabı alabilir miyiz lütfen?"}],
     "turkishNote": "Türkçedeki \"Hesap lütfen\" yerine \"The bill, please\" denebilir, ama \"Can I have the bill, please?\" daha kibardır. Fiyat söylerken para birimi sayıdan sonra okunur: £5 = five pounds (pounds five değil)."},
    [
        gap("How much ___ the coffee?", ["is"], "Tekil → is."),
        gap("How much ___ these cookies?", ["are"], "Çoğul → are."),
        mc("£4.50 nasıl okunur?", ["four pounds fifty", "pounds four fifty", "four fifty pounds"], 0, "Sayı + para birimi + kuruş."),
        mc("Hesabı istemek için:", ["Can I have the bill, please?", "Give me money.", "How much are you?"], 0, "Can I have the bill, please?"),
        gap("Can I pay ___ card?", ["by"], "Kartla = by card. Nakit = in cash."),
        order(["much", "How", "is", "the", "soup", "?"], "How much is the soup?", "How much + is + tekil isim?", "Çorba ne kadar?"),
        listen("That's eight euros and forty cents, please.", "Toplam ne kadar?", ["€4.80", "€8.40", "€8.14"], 1, "eight euros and forty cents = €8.40"),
        listen("The sandwiches are four pounds each, and the drinks are two pounds.", "Bir sandviç ne kadar?", ["£2", "£4", "£6"], 1, "\"four pounds each\""),
        typ("İngilizce yazın: \"Nakit ödeyebilir miyim?\"", variants("Can I pay in cash?", "Can I pay cash?", "Could I pay in cash?"), "Can I pay + in cash?"),
        mc("\"How much are the apples?\"", ["It's two euros a kilo.", "They're two euros a kilo."], 1, "apples çoğul → They're."),
    ],
    {"kind": "speaking", "task": speak("Restorandasınız. Bir yemeğin fiyatını sorun, sipariş verin ve sonunda hesabı isteyip kartla ödeyin.",
                                       "Excuse me, how much is the soup? OK, I'd like the soup, please. ... Can I have the bill, please? Can I pay by card?",
                                       ["How much is/are doğru", "Sipariş kibar", "Hesap ve ödeme ifadeleri doğru"])},
)

u.test([
    mc("Hangisi doğru?", ["a bread", "some bread", "a breads"], 1, "bread sayılamaz."),
    gap("a ___ of tea (fincan)", ["cup"], "a cup of tea"),
    gap("We don't have ___ milk.", ["any"], "Olumsuz → any."),
    gap("There are ___ apples on the table.", ["some"], "Olumlu → some."),
    mc("Teklif: \"___ you like some cake?\"", ["Do", "Would", "Are"], 1, "Would you like...?"),
    mc("\"Would you like a coffee?\" (Evet.)", ["Yes, please.", "Yes, I like.", "Yes, I'd."], 0, "Yes, please."),
    mc("Hangisi doğru?", ["I'd like order.", "I'd like to order."], 1, "would like + to + fiil"),
    order(["I", "Can", "have", "a", "water", "of", "glass", "?"], "Can I have a glass of water?", "Can I have + miktar + isim?", "Bir bardak su alabilir miyim?"),
    mc("\"For here or to take away?\" (Burada.)", ["For here, please.", "Take away.", "Here, I'd like."], 0, "For here, please."),
    gap("How much ___ the sandwiches?", ["are"], "Çoğul → are."),
    mc("£6.20 nasıl okunur?", ["six pounds twenty", "pounds six twenty", "sixty-two pounds"], 0, "six pounds twenty"),
    listen("Are you ready to order? – Yes, I'd like the chicken salad and a bottle of water, please.", "Müşteri ne içecek istiyor?", ["Bir bardak su", "Bir şişe su", "Meyve suyu"], 1, "\"a bottle of water\""),
    typ("İngilizce yazın: \"Hesabı alabilir miyim lütfen?\"", variants("Can I have the bill, please?", "Could I have the bill, please?"), "Can I have the bill, please?"),
    mc("Garsona en kibar istek:", ["I want soup.", "I'd like the soup, please.", "Soup."], 1, "I'd like ..., please."),
    write("Bir kafede geçen kısa bir konuşma yazın: garson ve sizin aranızda en az 6 satır.",
          "Waiter: Hi, what can I get you? Me: Can I have a large tea, please? Waiter: Anything else? Me: Yes, a piece of cake. How much is it? Waiter: It's four pounds. Me: OK. Can I pay by card?",
          ["Kibar istek (Can I have / I'd like)", "a/an, some, a piece of doğru", "How much is/are doğru", "please kullandı"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

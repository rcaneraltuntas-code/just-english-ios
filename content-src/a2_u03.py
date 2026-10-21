"""A2 Ünite 3: Karşılaştırma."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("A2", 3, "Karşılaştırma", "Comparing Things",
         "Şehirleri, ürünleri ve insanları karşılaştırabilir, en iyisini seçip nedenini açıklayabilirim.",
         ["comparatives: -er / more ... than", "düzensiz: better, worse, further", "superlatives: the -est / the most", "(not) as ... as", "much / a bit + comparative"],
         ["şehir hayatı", "sıfatlar ve zıt anlamlıları", "ürün özellikleri"],
         {"title": "Hangi şehir?", "durationMinutes": 45,
          "goal": "Gruplar, bir şirketin yeni ofisi için üç şehir arasında seçim yapar. Her grup bir şehrin bilgi kartını alır (nüfus, kira, hava, ulaşım) ve şehrini diğerleriyle karşılaştırarak savunur. Sınıf karşılaştırmalı cümleler duyduğu sürece puan verir ve sonunda kazanan şehri seçer."})

u.vocab([
    ("busy", "kalabalık, hareketli; meşgul", "Istanbul is busier than Bursa.", "İstanbul, Bursa'dan daha hareketli.", "busy → busier → the busiest"),
    ("quiet", "sessiz, sakin", "Villages are quieter than cities.", "Köyler şehirlerden daha sakin.", None),
    ("noisy", "gürültülü", "My street is very noisy at night.", "Sokağım geceleri çok gürültülü.", None),
    ("safe", "güvenli", "Is it safe to walk here at night?", "Burada gece yürümek güvenli mi?", None),
    ("dangerous", "tehlikeli", "This road is more dangerous in winter.", "Bu yol kışın daha tehlikeli.", None),
    ("polluted", "kirli (hava, su)", "The air is more polluted in the city centre.", "Şehir merkezinde hava daha kirli.", "pollution (kirlilik)"),
    ("clean", "temiz", "The sea is cleaner in the north.", "Kuzeyde deniz daha temiz.", None),
    ("modern", "modern", "The new airport is very modern.", "Yeni havalimanı çok modern.", None),
    ("ancient", "antik, çok eski", "Ephesus is an ancient city.", "Efes antik bir şehir.", None),
    ("crowded", "kalabalık", "The metro is crowded in the morning.", "Metro sabahları kalabalık.", None),
    ("expensive", "pahalı", "Rents are more expensive in London.", "Londra'da kiralar daha pahalı.", None),
    ("cheap", "ucuz", "Food is cheaper at the market.", "Pazarda yiyecek daha ucuz.", None),
    ("population", "nüfus", "Ankara has a population of nearly 6 million.", "Ankara'nın nüfusu yaklaşık 6 milyon.", None),
    ("rent", "kira", "The rent is too high in the centre.", "Merkezde kira çok yüksek.", None),
    ("public transport", "toplu taşıma", "Public transport is better in Izmir.", "İzmir'de toplu taşıma daha iyi.", None),
    ("traffic", "trafik", "The traffic is terrible on Fridays.", "Cuma günleri trafik berbat.", "Sayılamaz: a traffic değil."),
    ("nightlife", "gece hayatı", "Bodrum has great nightlife.", "Bodrum'un gece hayatı harika.", None),
    ("light", "hafif", "This laptop is lighter than my old one.", "Bu laptop eskisinden daha hafif.", None),
    ("heavy", "ağır", "The new phone is heavier.", "Yeni telefon daha ağır.", None),
    ("comfortable", "rahat", "These shoes are more comfortable.", "Bu ayakkabılar daha rahat.", None),
    ("reliable", "güvenilir, sağlam", "This car is very reliable.", "Bu araba çok sağlam.", None),
    ("than", "-den / -dan (daha)", "My brother is taller than me.", "Erkek kardeşim benden daha uzun.", None),
    ("in the world", "dünyada", "It's the biggest city in the world.", "Dünyanın en büyük şehri.", "the + superlative + in"),
    ("prefer", "tercih etmek", "I prefer small towns to big cities.", "Küçük kasabaları büyük şehirlere tercih ederim.", "prefer A to B"),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Daha büyük, daha sakin", "Kısa sıfatlarla iki şeyi karşılaştırabilirim.",
    {"kind": "dialogue", "title": "Taşınma kararı", "lines": [
        {"speaker": "Gül", "text": "So, are you moving from Istanbul to Eskişehir?"},
        {"speaker": "Ahmet", "text": "Yes! Eskişehir is smaller and quieter. The streets are cleaner, too."},
        {"speaker": "Gül", "text": "But Istanbul is bigger. There are more jobs."},
        {"speaker": "Ahmet", "text": "That's true. But rents in Eskişehir are much cheaper, and life is easier."},
        {"speaker": "Gül", "text": "What about the weather?"},
        {"speaker": "Ahmet", "text": "Well, winters are colder there. But summers are drier, and I like that."}],
     "questions": [
        mc("Why does Ahmet like Eskişehir?", ["It's bigger.", "It's quieter and cheaper.", "It has more jobs."], 1, "\"smaller and quieter... rents are much cheaper\""),
        mc("What's worse in Eskişehir?", ["The rents", "The winters", "The streets"], 1, "\"winters are colder there\""),
     ]},
    {"explanation": "**Kısa sıfatlar** (tek heceli ve -y ile biten iki heceli) karşılaştırmada **-er** alır, ardından **than** gelir.\n\n| Kural | Örnek |\n|---|---|\n| + -er | small → small**er**, cheap → cheap**er** |\n| -e ile biten: + -r | safe → safe**r**, nice → nice**r** |\n| ünsüz + y: y → -ier | busy → bus**ier**, easy → eas**ier**, dry → dr**ier** |\n| ünlü + ünsüz (tek heceli): ikile | big → bi**gg**er, hot → ho**tt**er, wet → we**tt**er |\n\n- Eskişehir is small**er than** Istanbul.\n- My bag is heavi**er than** yours.\n\n**than**'dan sonra zamir: than **me** / than **him** / than **her** (konuşma dilinde).",
     "examples": [{"en": "August is hotter than June.", "tr": "Ağustos, hazirandan daha sıcak."},
                  {"en": "The new road is safer.", "tr": "Yeni yol daha güvenli."},
                  {"en": "My sister is younger than me.", "tr": "Kız kardeşim benden küçük."}],
     "turkishNote": "Türkçede \"-den daha\" yapısı vardır: İstanbul'dan daha büyük. İngilizcede sıra farklıdır: bigger than Istanbul (sıfat + than + karşılaştırılan). \"More bigger\" hatası çok yaygındır: -er zaten \"daha\" anlamı taşır, more eklenmez."},
    [
        gap("A car is ___ than a bike. (fast)", ["faster"], "fast + -er."),
        gap("Today is ___ than yesterday. (hot)", ["hotter"], "hot → hotter (t ikilenir)."),
        gap("This exercise is ___ than the last one. (easy)", ["easier"], "y → -ier."),
        gap("Small towns are ___ than big cities. (safe)", ["safer"], "-e → + -r."),
        mc("Hangisi doğru?", ["Ankara is more bigger than Izmir.", "Ankara is bigger than Izmir.", "Ankara is big than Izmir."], 1, "-er + than (more yok).", {0: "-er ile more birlikte kullanılmaz."}),
        mc("Hangisi doğru?", ["My brother is taller than me.", "My brother is taller from me.", "My brother is taller that me."], 0, "taller than me."),
        order(["is", "quieter", "My", "village", "than", "the", "city"], "My village is quieter than the city.", "Özne + is + -er + than + karşılaştırılan.", "Köyüm şehirden daha sakin."),
        listen("I prefer Kadıköy to Beşiktaş. It's cheaper and the people are friendlier.", "Kadıköy'ü neden tercih ediyor?", ["Daha büyük ve modern", "Daha ucuz ve insanlar daha samimi", "Daha sakin"], 1, "\"It's cheaper and the people are friendlier.\""),
        typ("İngilizce yazın: \"Bu çanta seninkinden daha ağır.\"", variants("This bag is heavier than yours.", "This bag is heavier than your bag."), "heavy → heavier + than yours."),
        match([("big", "bigger"), ("busy", "busier"), ("nice", "nicer"), ("cold", "colder"), ("wet", "wetter")], "Sıfatları karşılaştırma halleriyle eşleştirin."),
    ],
    {"kind": "speaking", "task": speak("Yaşadığınız şehri ya da semti, bildiğiniz başka bir yerle karşılaştırın. En az 5 farklı kısa sıfat kullanın.",
                                       "Bursa is smaller than Istanbul and it's quieter. The air is cleaner and the winters are colder. But Istanbul is busier and the nightlife is better.",
                                       ["-er yazımı doğru", "than doğru kullanıldı", "more + -er hatası yok"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "Daha pahalı, daha iyi", "Uzun ve düzensiz sıfatlarla karşılaştırma yapabilirim.",
    {"kind": "dialogue", "title": "Telefon mağazasında", "lines": [
        {"speaker": "Customer", "text": "What's the difference between these two phones?"},
        {"speaker": "Assistant", "text": "The X20 is more expensive, but the camera is better."},
        {"speaker": "Customer", "text": "Is it more reliable?"},
        {"speaker": "Assistant", "text": "Yes, and the battery is better too. The Z5 is cheaper, but it's a bit slower."},
        {"speaker": "Customer", "text": "Hmm. My old phone was worse than both! I'll take the X20."}],
     "questions": [
        mc("Which phone has a better camera?", ["The X20", "The Z5", "Both are the same"], 0, "\"The X20 is more expensive, but the camera is better.\""),
        mc("What's the problem with the Z5?", ["It's more expensive.", "It's slower.", "It's heavier."], 1, "\"it's a bit slower\""),
     ]},
    {"explanation": "**Uzun sıfatlar** (iki ve daha çok heceli, -y ile bitmeyenler) **more** ya da **less** alır.\n\n- expensive → **more** expensive than\n- comfortable → **more** comfortable than\n- interesting → **less** interesting than (daha az ilginç)\n\n**Düzensiz sıfatlar:**\n\n| Sıfat | Karşılaştırma |\n|---|---|\n| good | **better** |\n| bad | **worse** |\n| far | **further** / farther |\n\n**Derece belirtmek:**\n\n- **much / a lot** + comparative: much cheaper, a lot more expensive (çok daha)\n- **a bit / a little** + comparative: a bit slower (biraz daha)",
     "examples": [{"en": "This hotel is more comfortable than the last one.", "tr": "Bu otel bir öncekinden daha rahat."},
                  {"en": "My English is much better now.", "tr": "İngilizcem şimdi çok daha iyi."},
                  {"en": "The traffic is worse on Fridays.", "tr": "Cuma günleri trafik daha kötü."}],
     "turkishNote": "\"Çok daha iyi\" derken very kullanılmaz: \"very better\" yanlıştır; \"much better\" doğrudur. \"gooder\" ya da \"more good\" da yanlıştır; good → better düzensizdir."},
    [
        gap("This sofa is ___ comfortable than that one. (daha)", ["more"], "Uzun sıfat → more."),
        gap("My new job is ___ than my old one. (good)", ["better"], "good → better."),
        gap("The weather today is ___ than yesterday. (bad)", ["worse"], "bad → worse."),
        mc("Hangisi doğru?", ["very better", "much better", "more better"], 1, "much + comparative."),
        mc("Hangisi doğru?", ["Rome is more interesting than Milan.", "Rome is interestinger than Milan."], 0, "Uzun sıfat → more."),
        mc("Hangisi \"biraz daha yavaş\"?", ["a bit slower", "very slower", "much slow"], 0, "a bit + comparative."),
        order(["is", "much", "The", "train", "more", "comfortable", "than", "the", "bus"], "The train is much more comfortable than the bus.", "much + more + uzun sıfat + than.", "Tren otobüsten çok daha rahat."),
        listen("The flat in the centre is more expensive, but it's much closer to my office. The other one is further away.", "Merkezdeki dairenin avantajı ne?", ["Daha ucuz", "Ofise çok daha yakın", "Daha büyük"], 1, "\"it's much closer to my office\""),
        typ("İngilizce yazın: \"Bu film kitaptan daha kötü.\"", variants("This film is worse than the book.", "The film is worse than the book.", "This movie is worse than the book.", "The movie is worse than the book."), "bad → worse + than."),
        match([("good", "better"), ("bad", "worse"), ("far", "further"), ("beautiful", "more beautiful")], "Eşleştirin."),
    ],
    {"kind": "writing", "task": write("İki ürünü karşılaştıran kısa bir değerlendirme yazın (iki telefon, iki laptop, iki araba...). Kısa ve uzun sıfatlar, good/bad ve much/a bit kullanın.",
                                      "I compared two laptops. The Pro 14 is more expensive, but it's much faster and lighter. The battery is better too. The Air 13 is a bit cheaper, but the screen is worse. I think the Pro 14 is more reliable.",
                                      ["-er / more doğru", "better / worse doğru", "much / a bit kullanıldı", "Net bir sonuç"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "En büyüğü, en iyisi", "Bir grubun içinde en uç olanı superlative ile söyleyebilirim.",
    {"kind": "text", "title": "Türkiye'nin rekorları", "body": "Did you know?\n\nThe biggest city in Turkey is Istanbul, with a population of more than 15 million people.\n\nThe highest mountain is Mount Ağrı (5,137 metres).\n\nThe longest river that starts and ends in Turkey is the Kızılırmak (1,355 km).\n\nThe largest lake is Lake Van. It's also one of the most beautiful places in the country.\n\nAnd the best thing about Turkey? Most visitors say the food!",
     "questions": [
        mc("What's the highest mountain in Turkey?", ["Mount Erciyes", "Mount Ağrı", "Mount Uludağ"], 1, "\"The highest mountain is Mount Ağrı\""),
        mc("What do most visitors say is the best thing about Turkey?", ["The weather", "The food", "The mountains"], 1, "\"Most visitors say the food!\""),
     ]},
    {"explanation": "**Superlative**, bir grubun içinde \"en\" olanı anlatır. Önüne **the** gelir.\n\n| Sıfat | Comparative | Superlative |\n|---|---|---|\n| small | smaller | **the smallest** |\n| big | bigger | **the biggest** |\n| busy | busier | **the busiest** |\n| expensive | more expensive | **the most expensive** |\n| good | better | **the best** |\n| bad | worse | **the worst** |\n| far | further | **the furthest** |\n\n**Yer veya grup:**\n\n- the biggest city **in** Turkey / **in** the world / **in** my family (yer, grup)\n- the best day **of** my life / **of** the year (zaman dilimi)\n\n**one of the** + superlative + **çoğul isim**: one of the most beautiful **places**",
     "examples": [{"en": "It's the most expensive restaurant in the city.", "tr": "Şehrin en pahalı restoranı."},
                  {"en": "That was the worst day of my life.", "tr": "Hayatımın en kötü günüydü."},
                  {"en": "She's one of the best teachers in our school.", "tr": "Okulumuzun en iyi öğretmenlerinden biri."}],
     "turkishNote": "Türkçede \"dünyanın en büyük şehri\" deriz; İngilizcede \"the biggest city in the world\" denir (of the world değil). \"one of the\" sonrası isim çoğuldur: one of the best restaurants (restaurant değil). Superlative önünde the unutulmamalıdır."},
    [
        gap("Istanbul is the ___ city in Turkey. (big)", ["biggest"], "big → the biggest."),
        gap("This is the ___ expensive hotel in town. (en)", ["most"], "Uzun sıfat → the most."),
        gap("It was the ___ day of my life! (good)", ["best"], "good → the best."),
        gap("That was the ___ film of the year. (bad)", ["worst"], "bad → the worst."),
        mc("Hangisi doğru?", ["the biggest city of the world", "the biggest city in the world"], 1, "Yer → in."),
        mc("Hangisi doğru?", ["one of the best restaurant", "one of the best restaurants"], 1, "one of the + çoğul."),
        mc("Hangisi doğru?", ["She's tallest girl in the class.", "She's the tallest girl in the class."], 1, "the unutulmaz."),
        order(["the", "is", "This", "most", "beautiful", "beach", "in", "Turkey"], "This is the most beautiful beach in Turkey.", "the most + uzun sıfat + isim + in + yer.", "Bu, Türkiye'nin en güzel plajı."),
        listen("The busiest day at our restaurant is Saturday. The quietest day is Monday, so we close on Mondays.", "Restoran neden pazartesi kapalı?", ["En kalabalık gün", "En sakin gün", "Tatil günü"], 1, "\"The quietest day is Monday, so we close\""),
        typ("İngilizce yazın: \"Ailemin en yaşlı kişisi büyükbabam.\"", variants("The oldest person in my family is my grandfather.", "My grandfather is the oldest person in my family.", "The oldest person in my family is my grandpa.", "My grandpa is the oldest person in my family."), "the oldest person + in my family."),
    ],
    {"kind": "speaking", "task": speak("Ülkenizi ya da şehrinizi tanıtın: en güzel yer, en iyi yemek, en kalabalık semt, en ilginç müze... En az 5 superlative kullanın.",
                                       "The most beautiful place in Izmir is Alaçatı. The best food is boyoz. The busiest area is Konak. One of the most interesting museums is the Ephesus Museum. And the hottest month is July.",
                                       ["the + -est / the most doğru", "in / of doğru", "one of the + çoğul"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Aynı mı, farklı mı?", "as ... as ile eşitliği ve not as ... as ile farkı anlatabilirim.",
    {"kind": "dialogue", "title": "İkizler", "lines": [
        {"speaker": "Reporter", "text": "You're twins, but are you very different?"},
        {"speaker": "Ece", "text": "Well, I'm as tall as Ela, but she's much sportier."},
        {"speaker": "Ela", "text": "And Ece is the cleverest! I'm not as good at maths as her."},
        {"speaker": "Ece", "text": "But Ela's room is cleaner than mine. My room isn't as tidy as hers!"},
        {"speaker": "Reporter", "text": "Who's funnier?"},
        {"speaker": "Ela", "text": "We're both as funny as each other!"}],
     "questions": [
        mc("Who is taller?", ["Ece", "Ela", "They're the same height."], 2, "\"I'm as tall as Ela\""),
        mc("Whose room is tidier?", ["Ece's", "Ela's"], 1, "\"My room isn't as tidy as hers!\" (Ece)"),
     ]},
    {"explanation": "**as + sıfat + as** → eşitlik (… kadar)\n\n- Ece is **as tall as** Ela. (Aynı boyda.)\n- This phone is **as good as** the expensive one.\n\n**not as + sıfat + as** → daha az (… kadar değil)\n\n- My room **isn't as tidy as** hers. (= Her room is tidier.)\n- The bus **isn't as fast as** the metro.\n\nSıfat **yalın** halde kalır: as tall as (~~as taller as~~).\n\n**Karşılaştırın:** Izmir isn't as big as Istanbul. = Istanbul is bigger than Izmir.",
     "examples": [{"en": "My son is now as tall as me.", "tr": "Oğlum artık benim kadar uzun."},
                  {"en": "This hotel isn't as nice as the last one.", "tr": "Bu otel bir önceki kadar güzel değil."},
                  {"en": "Is Antalya as hot as Adana in summer?", "tr": "Antalya yazın Adana kadar sıcak mı?"}],
     "turkishNote": "\"... kadar\" yapısı İngilizcede iki as ile kurulur ve sıfat ortada kalır. Olumsuz \"not as ... as\" cümleleri günlük dilde \"-er than\" kadar yaygındır ve daha kibar duyulur: \"Your cake isn't as sweet as mine\" demek, \"My cake is sweeter\" demekten daha yumuşaktır."},
    [
        mc("Ali ve Can aynı yaşta: Ali is ___ Can.", ["as old as", "older than", "as older as"], 0, "Eşitlik → as + sıfat + as."),
        mc("Hangisi doğru?", ["as taller as", "as tall as", "so tall than"], 1, "Sıfat yalın kalır."),
        gap("The bus isn't ___ fast as the train.", ["as"], "not as ... as."),
        gap("My English is as good ___ yours.", ["as"], "as ... as."),
        mc("\"Bursa isn't as big as Ankara.\" Anlamı:", ["Bursa is bigger.", "Ankara is bigger.", "They're the same."], 1, "not as big as → Ankara daha büyük."),
        typ("Aynı anlamda yazın (not as ... as): \"Istanbul is busier than Izmir.\"", variants("Izmir isn't as busy as Istanbul.", "Izmir is not as busy as Istanbul."), "Izmir + isn't as busy as + Istanbul."),
        order(["isn't", "as", "This", "film", "good", "as", "the", "book"], "This film isn't as good as the book.", "not as + sıfat + as.", "Bu film kitap kadar iyi değil."),
        listen("The new café is nice, but the coffee isn't as good as at Kahve Dünyası, and it's twice as expensive!", "Yeni kafede sorun ne?", ["Kahve daha iyi ama pahalı", "Kahve o kadar iyi değil ve daha pahalı", "Kafe çok küçük"], 1, "\"the coffee isn't as good as ... and it's twice as expensive\""),
        mc("Kibar bir eleştiri:", ["Your cake is worse than mine.", "Your cake isn't as sweet as mine."], 1, "not as ... as daha yumuşak."),
        gap("Is Antalya as hot ___ Adana in summer?", ["as"], "as ... as soru."),
    ],
    {"kind": "speaking", "task": speak("Kendinizi bir kardeşiniz, arkadaşınız ya da eşinizle karşılaştırın. 2 tane as ... as, 2 tane not as ... as ve 2 tane -er/more than kullanın.",
                                       "My brother is as tall as me, and he's as funny as me. But I'm not as sporty as him, and my room isn't as tidy as his. I'm more patient than him, and I'm a better cook!",
                                       ["as ... as doğru", "not as ... as doğru", "Comparative doğru"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Karar vermek", "Seçenekleri karşılaştırıp bir tercih yapabilir ve nedenini açıklayabilirim.",
    {"kind": "dialogue", "title": "Tatil planı", "lines": [
        {"speaker": "Nazlı", "text": "So, Bodrum or Kaş? Which do you prefer?"},
        {"speaker": "Emir", "text": "I prefer Kaş. It's quieter, and the sea is the cleanest in the area."},
        {"speaker": "Nazlı", "text": "But Bodrum has the best nightlife. And it's easier to get to."},
        {"speaker": "Emir", "text": "That's true, but Kaş isn't as crowded as Bodrum in August."},
        {"speaker": "Nazlı", "text": "Hmm, I think you're right. Hotels are a bit cheaper too."},
        {"speaker": "Emir", "text": "Great. Kaş it is!"}],
     "questions": [
        mc("Why does Emir prefer Kaş?", ["Better nightlife", "Quieter, cleaner sea", "Easier to get to"], 1, "\"It's quieter, and the sea is the cleanest\""),
        mc("Where do they decide to go?", ["Bodrum", "Kaş", "Neither"], 1, "\"Kaş it is!\""),
     ]},
    {"explanation": "**Tercih sormak ve söylemek:**\n\n- **Which** do you **prefer**, A or B?\n- I **prefer** A **to** B. / I prefer A **because** ...\n- **I'd rather** go to Kaş. (Kaş'a gitmeyi tercih ederim.)\n\n**Fikir belirtmek:**\n\n- **I think** A is better **because** ...\n- **In my opinion**, B is the best option.\n\n**Katılmak ve katılmamak:**\n\n- That's true. / I think you're right. / I agree.\n- That's true, **but** ... / I'm not sure. / I don't agree.\n\nİyi bir karşılaştırma için hem **comparative** (iki seçenek) hem **superlative** (üç ve daha fazla seçenek) kullanılır.",
     "examples": [{"en": "I prefer the train to the bus. It's more comfortable.", "tr": "Treni otobüse tercih ederim. Daha rahat."},
                  {"en": "In my opinion, this is the best option.", "tr": "Bence bu en iyi seçenek."},
                  {"en": "That's true, but it's more expensive.", "tr": "Doğru ama daha pahalı."}],
     "turkishNote": "\"prefer\" ile karşılaştırma yaparken than değil to kullanılır: I prefer tea to coffee (than coffee değil). İki seçenek varken \"Which is better?\", ikiden fazla seçenek varken \"Which is the best?\" denir."},
    [
        mc("Hangisi doğru?", ["I prefer tea than coffee.", "I prefer tea to coffee."], 1, "prefer A to B."),
        mc("Üç seçenek var:", ["Which is better?", "Which is the best?"], 1, "3+ seçenek → superlative."),
        gap("Which do you ___, the red one or the blue one?", ["prefer"], "Tercih sorusu."),
        gap("I prefer Kaş ___ it's quieter.", ["because"], "Neden → because."),
        gap("___ my opinion, the train is the best option.", ["In"], "In my opinion."),
        mc("Kısmen katılmak:", ["That's true, but it's expensive.", "No.", "Yes, I'm agree."], 0, "That's true, but ...", {2: "agree bir fiildir: I agree (I'm agree değil)."}),
        order(["prefer", "I", "the", "mountains", "to", "the", "sea"], "I prefer the mountains to the sea.", "prefer A to B.", "Dağları denize tercih ederim."),
        listen("Option A is the cheapest, but it's the furthest from the centre. Option B is more expensive, but it's the closest. I think B is better.", "Konuşan neden B'yi seçiyor?", ["En ucuz", "Merkeze en yakın", "En büyük"], 1, "\"it's the closest\""),
        typ("İngilizce yazın: \"Bence bu en iyi seçenek.\"", variants("I think this is the best option.", "In my opinion, this is the best option.", "In my opinion this is the best option.", "I think it's the best option."), "I think / In my opinion + the best option."),
        mc("\"I'm agree\" yerine doğrusu:", ["I agree.", "I'm agreeing.", "I am agree with."], 0, "agree fiil → I agree."),
    ],
    {"kind": "speaking", "task": speak("JAI ile hafta sonu için üç seçenek arasında karar verin (sinema, piknik, müze). Her seçeneği karşılaştırın, JAI'nin fikirlerine katılın ya da katılmayın ve birlikte karar verin.",
                                       "I think the picnic is the best option because the weather is nice. That's true, but the museum is more interesting. Hmm, the cinema is the most expensive. OK, I agree, let's have a picnic.",
                                       ["Comparative ve superlative", "prefer / I think / because", "Katılma ve katılmama ifadeleri"])},
)

u.test([
    gap("My car is ___ than yours. (old)", ["older"], "old + -er"),
    gap("August is ___ than May. (hot)", ["hotter"], "hot → hotter"),
    gap("This test is ___ than the last one. (easy)", ["easier"], "y → -ier"),
    mc("Hangisi doğru?", ["more cheaper", "cheaper"], 1, "-er + more olmaz."),
    gap("This hotel is ___ comfortable than that one.", ["more"], "Uzun sıfat → more"),
    mc("good → ___", ["gooder", "better", "more good"], 1, "Düzensiz"),
    mc("Hangisi doğru?", ["very better", "much better"], 1, "much + comparative"),
    gap("It's the ___ restaurant in town. (good)", ["best"], "the best"),
    mc("Hangisi doğru?", ["the highest mountain of Turkey", "the highest mountain in Turkey"], 1, "Yer → in"),
    mc("Hangisi doğru?", ["one of the best city", "one of the best cities"], 1, "Çoğul"),
    mc("\"My flat isn't as big as yours.\" Anlamı:", ["My flat is bigger.", "Your flat is bigger."], 1, "not as ... as"),
    mc("Hangisi doğru?", ["I prefer cats than dogs.", "I prefer cats to dogs."], 1, "prefer A to B"),
    listen("Of the three hotels, the Grand is the most expensive and the Star is the cheapest. But the Sun has the best view.", "Hangi otelin manzarası en iyi?", ["The Grand", "The Star", "The Sun"], 2, "\"the Sun has the best view\""),
    typ("Aynı anlamda yazın (not as ... as): \"The metro is faster than the bus.\"", variants("The bus isn't as fast as the metro.", "The bus is not as fast as the metro."), "The bus isn't as fast as the metro."),
    write("Yaşamak için iki şehri karşılaştırın ve hangisini tercih ettiğinizi açıklayın (80–100 kelime). Comparative, superlative ve as ... as kullanın.",
          "I live in Ankara, but I sometimes think about moving to Izmir. Izmir is smaller than Ankara, but it's much more relaxed. The weather is warmer and the sea is beautiful. Ankara isn't as expensive as Izmir, and public transport is better. But in my opinion, Izmir has the friendliest people and the best food in Turkey. I prefer Izmir to Ankara because life is slower and happier there.",
          ["Comparative doğru", "Superlative doğru", "as ... as doğru", "Tercih ve neden açık"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

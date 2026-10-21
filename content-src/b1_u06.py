"""B1 Ünite 6: İcatlar."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("B1", 6, "İcatlar", "Inventions",
         "Bir şeyin nasıl yapıldığını ve kim tarafından icat edildiğini edilgen yapıyla anlatabilir, etken ve edilgen yapı arasında uygun olanı seçebilir ve bir ürünü ya da icadı tanıtabilirim.",
         ["passive: present simple (is made)", "passive: past simple (was invented)", "by + eylemi yapan", "etken mi edilgen mi?", "edilgen sorular ve olumsuzlar", "made of / made from / used for"],
         ["icatlar ve keşifler", "malzemeler", "üretim ve teknoloji"],
         {"title": "Büyük icat yarışması", "durationMinutes": 45,
          "goal": "Gruplar hayali bir icat tasarlar ve 2 dakikalık bir tanıtım hazırlar: It is made of..., It is used for..., It was designed by... Sunumların ardından diğer gruplar edilgen sorular sorar (How is it powered? Where will it be sold?) ve sınıf en kullanışlı icadı oylar."})

u.vocab([
    ("invent", "icat etmek", "Who invented the telephone?", "Telefonu kim icat etti?", None),
    ("invention", "icat", "The wheel is one of the oldest inventions.", "Tekerlek en eski icatlardan biridir.", None),
    ("inventor", "mucit", "She's a young inventor from Konya.", "Konyalı genç bir mucit.", None),
    ("discover", "keşfetmek", "Penicillin was discovered in 1928.", "Penisilin 1928'de keşfedildi.", "discovery (keşif)"),
    ("design", "tasarlamak; tasarım", "The bridge was designed by a famous architect.", "Köprü ünlü bir mimar tarafından tasarlandı.", None),
    ("develop", "geliştirmek", "The company developed a new app.", "Şirket yeni bir uygulama geliştirdi.", None),
    ("produce", "üretmek", "Millions of cars are produced every year.", "Her yıl milyonlarca araba üretilir.", "product (ürün)"),
    ("grow", "yetiştirmek", "Tea is grown in Rize.", "Rize'de çay yetiştirilir.", "grow → grew → grown"),
    ("made of", "-den yapılmış (malzeme görünür)", "This table is made of wood.", "Bu masa ahşaptan yapılmış.", None),
    ("made from", "-den yapılmış (malzeme dönüşmüş)", "Paper is made from wood.", "Kâğıt ağaçtan yapılır.", None),
    ("used for", "... için kullanılır", "This tool is used for cutting glass.", "Bu alet cam kesmek için kullanılır.", "used for + -ing"),
    ("material", "malzeme", "What material is it made of?", "Hangi malzemeden yapılmış?", None),
    ("plastic", "plastik", "Plastic is used in almost everything.", "Plastik neredeyse her şeyde kullanılır.", None),
    ("metal", "metal", "The frame is made of metal.", "Çerçeve metalden yapılmış.", None),
    ("glass", "cam", "Glass is made from sand.", "Cam kumdan yapılır.", None),
    ("device", "cihaz", "A smartwatch is a small device.", "Akıllı saat küçük bir cihazdır.", None),
    ("battery", "pil, batarya", "The battery lasts two days.", "Pil iki gün dayanıyor.", None),
    ("by accident", "kazara, tesadüfen", "Many things were discovered by accident.", "Pek çok şey tesadüfen keşfedildi.", None),
    ("sell", "satmak", "These phones are sold all over the world.", "Bu telefonlar bütün dünyada satılıyor.", "sell → sold → sold"),
    ("build", "inşa etmek", "The bridge was built in 1973.", "Köprü 1973'te inşa edildi.", "build → built → built"),
    ("replace", "yerini almak, değiştirmek", "Emails have replaced letters.", "E-postalar mektupların yerini aldı.", None),
    ("powered by", "... ile çalışan", "The car is powered by electricity.", "Araba elektrikle çalışıyor.", None),
    ("useful", "kullanışlı, faydalı", "It's a really useful invention.", "Gerçekten faydalı bir icat.", "useless (işe yaramaz)"),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Nasıl yapılır?", "Bir ürünün nasıl yapıldığını present simple edilgen yapıyla anlatabilirim.",
    {"kind": "text", "title": "Çay: Tarladan bardağa", "body": "Turkey is one of the biggest tea producers in the world, and most Turkish tea is grown in Rize and the Black Sea region.\n\nFirst, the young green leaves are picked by hand or with special scissors. Then they are taken to a factory.\n\nAt the factory, the leaves are dried for a few hours. After that, they are rolled and cut into small pieces.\n\nNext, the tea is left in the air, and it slowly turns dark brown. Finally, it is dried again, packed and sent to shops all over the country.\n\nEvery day, millions of glasses of tea are drunk in Turkey.",
     "questions": [
        mc("Where is most Turkish tea grown?", ["In Istanbul", "In Rize and the Black Sea region", "In Antalya"], 1, "\"most Turkish tea is grown in Rize and the Black Sea region\""),
        mc("What happens to the leaves first?", ["They are dried.", "They are picked.", "They are packed."], 1, "\"First, the young green leaves are picked\""),
     ]},
    {"explanation": "**Edilgen yapı (passive)**, eylemi **kimin yaptığı önemli değilse** ya da bilinmiyorsa kullanılır. Odak **eylemin kendisi** ya da **etkilenen şey**dir.\n\n**Present simple passive:** am / is / are + **V3**\n\n| Etken (active) | Edilgen (passive) |\n|---|---|\n| They **grow** tea in Rize. | Tea **is grown** in Rize. |\n| Workers **pick** the leaves. | The leaves **are picked**. |\n| People **drink** millions of glasses. | Millions of glasses **are drunk**. |\n\n**Olumsuz:** isn't / aren't + V3\n\n- Coffee **isn't grown** in Turkey.\n\n**Süreç anlatırken** sıralama kelimeleri kullanılır: **First**, ... **Then** ... **After that**, ... **Next**, ... **Finally**, ...",
     "examples": [{"en": "Glass is made from sand.", "tr": "Cam kumdan yapılır."},
                  {"en": "English is spoken in many countries.", "tr": "İngilizce birçok ülkede konuşulur."},
                  {"en": "The rooms are cleaned every day.", "tr": "Odalar her gün temizlenir."}],
     "turkishNote": "Türkçedeki \"-ılır / -ilir\" (yapılır, konuşulur, yetiştirilir) eki present simple passive'e denk gelir. Türkçe konuşanlar sık sık \"be\" fiilini unutur: \"Tea grown in Rize\" yanlış, \"Tea is grown in Rize\" doğru. Fiilin mutlaka V3 halinde olmasına da dikkat edin."},
    [
        mc("\"Çay Rize'de yetiştirilir.\"", ["Tea grows in Rize.", "Tea is grown in Rize.", "Tea is grow in Rize."], 1, "is + V3."),
        mc("Hangisi doğru?", ["Cars are produce here.", "Cars are produced here."], 1, "are + V3."),
        mc("English ___ in Australia.", ["is spoken", "are spoken", "speaks"], 0, "Tekil → is + V3."),
        gap("Paper ___ made from wood.", ["is"], "is + V3."),
        gap("The leaves are ___ by hand. (pick)", ["picked"], "V3."),
        gap("Millions of emails are ___ every second. (send)", ["sent"], "send → sent."),
        gap("Coffee ___ grown in Turkey. (olumsuz)", ["isn't", "is not"], "Olumsuz passive."),
        order(["is", "Glass", "made", "from", "sand"], "Glass is made from sand.", "Özne + is + V3.", "Cam kumdan yapılır."),
        listen("Olive oil is produced in many parts of Turkey. First, the olives are picked in autumn. Then they are washed and pressed.", "Zeytinler ne zaman toplanır?", ["İlkbaharda", "Sonbaharda", "Yazın"], 1, "\"the olives are picked in autumn\""),
        typ("İngilizce yazın: \"İngilizce birçok ülkede konuşulur.\"", variants("English is spoken in many countries.", "English is spoken in lots of countries.", "In many countries English is spoken.", "English is spoken in a lot of countries."), "English is spoken in many countries."),
    ],
    {"kind": "speaking", "task": speak("Şehrinizde ya da ülkenizde üretilen bir yiyeceğin ya da ürünün nasıl yapıldığını anlatın (ekmek, peynir, halı, zeytinyağı...). Sıralama kelimeleri ve en az 5 edilgen cümle kullanın.",
                                       "Turkish delight is made from sugar, starch and water. First, the sugar and water are boiled. Then the starch is added. After that, the mixture is cooked for hours. Next, nuts or rose water are added. Finally, it is cut into small pieces and covered with powdered sugar.",
                                       ["is / are + V3", "Sıralama kelimeleri", "V3 biçimleri doğru"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "Kim icat etti?", "Tarihteki icatları ve keşifleri past simple edilgen yapı ve by ile anlatabilirim.",
    {"kind": "text", "title": "Tesadüfen bulunan icatlar", "body": "Some of the most useful inventions in history were discovered by accident.\n\nPENICILLIN\nIn 1928, a Scottish scientist, Alexander Fleming, came back from holiday and noticed something strange in his lab. A type of mould had killed the bacteria in one of his dishes. This was the start of penicillin, and millions of lives were saved.\n\nTHE MICROWAVE OVEN\nIn 1945, an American engineer, Percy Spencer, was working with radar equipment when he realised that a chocolate bar in his pocket had melted. The first microwave oven was built soon after.\n\nVELCRO\nThe idea for Velcro came from nature. In 1941, a Swiss engineer, George de Mestral, was walking his dog when he saw small seeds stuck in the dog's fur. Velcro was designed using the same idea.",
     "questions": [
        mc("When was penicillin discovered?", ["In 1928", "In 1945", "In 1941"], 0, "\"In 1928\""),
        mc("What gave Percy Spencer the idea for the microwave oven?", ["A broken radar", "A melted chocolate bar", "A cold lunch"], 1, "\"a chocolate bar in his pocket had melted\""),
     ]},
    {"explanation": "**Past simple passive:** was / were + **V3**\n\n| Etken | Edilgen |\n|---|---|\n| Fleming **discovered** penicillin. | Penicillin **was discovered** by Fleming. |\n| They **built** the bridge in 1973. | The bridge **was built** in 1973. |\n| Penicillin **saved** millions of lives. | Millions of lives **were saved**. |\n\n**by + eylemi yapan**: Kimin yaptığı **önemliyse** by ile eklenir.\n\n- The telephone **was invented by** Alexander Graham Bell.\n- The World Wide Web **was invented by** Tim Berners-Lee in 1989.\n\nKimin yaptığı **belli değilse ya da önemsizse** by kullanılmaz:\n\n- My bike **was stolen** last night. (~~by someone~~)\n\n**Olumsuz:** wasn't / weren't + V3 → The car **wasn't damaged**.",
     "examples": [{"en": "The Galata Bridge was rebuilt many times.", "tr": "Galata Köprüsü defalarca yeniden inşa edildi."},
                  {"en": "Paper was invented in China about 2,000 years ago.", "tr": "Kâğıt yaklaşık 2.000 yıl önce Çin'de icat edildi."},
                  {"en": "The first emails were sent in the 1970s.", "tr": "İlk e-postalar 1970'lerde gönderildi."}],
     "turkishNote": "\"-ıldı / -ildi\" eki (icat edildi, inşa edildi) past simple passive'e denk gelir. \"Tarafından\" ise by ile verilir: \"Bell tarafından icat edildi\" → \"was invented by Bell\". Türkçede olduğu gibi İngilizcede de eylemi yapan çoğu zaman söylenmez."},
    [
        mc("\"Telefon Bell tarafından icat edildi.\"", ["The telephone invented by Bell.", "The telephone was invented by Bell."], 1, "was + V3 + by."),
        mc("The first microwave oven ___ in the 1940s.", ["was built", "were built", "built"], 0, "Tekil → was + V3."),
        mc("Millions of lives ___ by penicillin.", ["was saved", "were saved"], 1, "Çoğul → were."),
        gap("Penicillin was ___ by Alexander Fleming. (discover)", ["discovered"], "V3."),
        gap("The bridge was ___ in 1973. (build)", ["built"], "build → built."),
        gap("My car ___ stolen last week.", ["was"], "Tekil → was."),
        gap("Luckily, nobody ___ hurt. (nobody → tekil fiil)", ["was"], "nobody + was."),
        mc("Gereksiz \"by\" olan cümle:", ["My phone was stolen.", "My phone was stolen by someone."], 1, "Bilinmeyen kişi → by gereksiz."),
        listen("The Hagia Sophia was built in the sixth century. It was used as a church for nearly a thousand years.", "Ayasofya ne zaman inşa edildi?", ["Altıncı yüzyılda", "On altıncı yüzyılda", "Bin yıl önce"], 0, "\"in the sixth century\""),
        typ("İngilizce yazın: \"Kâğıt Çin'de icat edildi.\"", variants("Paper was invented in China.", "Paper was first invented in China.", "In China paper was invented."), "Paper was invented in China."),
    ],
    {"kind": "speaking", "task": speak("En önemli bulduğunuz 3 icadı seçin ve anlatın: Ne zaman, nerede, kim tarafından icat edildi ya da keşfedildi? Hayatımızı nasıl değiştirdi? Bilmediğiniz bilgileri uydurmayın; \"I'm not sure who it was invented by\" diyebilirsiniz.",
                                       "I think the World Wide Web is the most important invention. It was invented by Tim Berners-Lee in 1989. Penicillin was also very important. It was discovered by Alexander Fleming in 1928, and millions of lives were saved. And the wheel. I'm not sure who it was invented by, but it was invented thousands of years ago.",
                                       ["was / were + V3", "by doğru kullanımı", "İcat kelimeleri"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "Etken mi, edilgen mi?", "Bir cümlede neyin önemli olduğuna göre etken ya da edilgen yapıyı seçebilirim.",
    {"kind": "dialogue", "title": "Müze turu", "lines": [
        {"speaker": "Guide", "text": "This beautiful vase was made in İznik in the sixteenth century."},
        {"speaker": "Visitor", "text": "Who made it?"},
        {"speaker": "Guide", "text": "We don't know the artist's name, unfortunately. But İznik tiles were used in many mosques and palaces."},
        {"speaker": "Visitor", "text": "Are they still produced today?"},
        {"speaker": "Guide", "text": "Yes, some local artists still make them by hand, using the old methods."},
        {"speaker": "Visitor", "text": "Amazing. Can we take photos?"},
        {"speaker": "Guide", "text": "Sorry, photos aren't allowed in this room."}],
     "questions": [
        mc("Where was the vase made?", ["In Istanbul", "In İznik", "In Konya"], 1, "\"This beautiful vase was made in İznik\""),
        mc("Can the visitor take photos?", ["Yes", "No"], 1, "\"photos aren't allowed in this room\""),
     ]},
    {"explanation": "**Etken (active):** Eylemi **yapan** önemli ve biliniyor.\n\n- Local artists **make** the tiles by hand.\n- My grandmother **made** this cake.\n\n**Edilgen (passive):** **Eylem ya da etkilenen şey** önemli; yapan bilinmiyor, belli ya da önemsiz.\n\n| Neden passive? | Örnek |\n|---|---|\n| Yapan bilinmiyor | The vase **was made** in the 16th century. |\n| Yapan belli / önemsiz | The rubbish **is collected** on Mondays. |\n| Kurallar, resmî dil | Photos **aren't allowed**. |\n| Süreçler | The leaves **are dried**. |\n\n**Etkenden edilgene:**\n\n1. Nesne → özne olur: *the tiles*\n2. be (zamana göre) + V3: *are made*\n3. Gerekirse **by** + yapan\n\n→ Local artists make **the tiles**. → **The tiles are made** by local artists.",
     "examples": [{"en": "Smoking isn't allowed in the building.", "tr": "Binada sigara içmek yasaktır."},
                  {"en": "The rubbish is collected on Mondays.", "tr": "Çöpler pazartesileri toplanır."},
                  {"en": "My uncle built this house.", "tr": "Bu evi amcam yaptı."}],
     "turkishNote": "Türkçede de \"Bu evi amcam yaptı\" (etken) ile \"Bu ev 1980'de yapıldı\" (edilgen) arasında benzer bir seçim yaparız. İngilizcede passive Türkçeden biraz daha sık kullanılır, özellikle haberlerde, kurallarda ve bilimsel metinlerde."},
    [
        mc("Yapan önemli: Annenizin yaptığı bir kek.", ["My mum made this cake.", "This cake was made."], 0, "Yapan önemli → active."),
        mc("Kural:", ["Photos aren't allowed.", "People don't allow photos."], 0, "Kurallar → passive."),
        mc("\"They clean the rooms every day.\" → Edilgen:", ["The rooms are cleaned every day.", "The rooms were cleaned every day.", "The rooms clean every day."], 0, "Present → are + V3."),
        mc("\"Someone stole my wallet.\" → Edilgen:", ["My wallet is stolen.", "My wallet was stolen."], 1, "Past → was + V3."),
        gap("Edilgen yapın: \"They speak Spanish in Mexico.\" → Spanish ___ spoken in Mexico.", ["is"], "is + V3."),
        gap("Edilgen yapın: \"Picasso painted this.\" → This was painted ___ Picasso.", ["by"], "by + yapan."),
        gap("Smoking isn't ___ here. (allow)", ["allowed"], "V3."),
        gap("The tiles ___ made by hand. (present, çoğul)", ["are"], "are + V3."),
        listen("This mosque was designed by Mimar Sinan, the great Ottoman architect. It was finished in 1557.", "Cami kim tarafından tasarlandı?", ["Mimar Sinan", "Bilinmiyor", "Bir sultan"], 0, "\"designed by Mimar Sinan\""),
        typ("Edilgen yapın: \"They built the stadium in 2010.\"", variants("The stadium was built in 2010.", "In 2010 the stadium was built.", "The stadium was built in 2010 by them."), "The stadium was built in 2010."),
    ],
    {"kind": "speaking", "task": speak("Evinizden ya da şehrinizden 4 nesneyi ya da yeri tanıtın. Bazılarında yapanı bilin (active), bazılarında bilmeyin (passive). Bir de evinizin ya da işyerinizin kurallarını passive ile söyleyin.",
                                       "This rug was made in Kayseri about fifty years ago. My grandmother bought it. That bridge was built in the 1970s. My father painted this picture. At my office, food isn't allowed near the computers, and the doors are locked at 8 pm.",
                                       ["Active / passive doğru seçimi", "Zamana uygun be + V3", "Kurallar için passive"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Neyden yapılmış?", "Bir nesnenin malzemesini, kullanım amacını ve üretim bilgilerini sorup anlatabilirim.",
    {"kind": "dialogue", "title": "El yapımı ürünler pazarında", "lines": [
        {"speaker": "Customer", "text": "This bag is lovely. What's it made of?"},
        {"speaker": "Seller", "text": "It's made of recycled plastic. Believe it or not, it's made from old water bottles."},
        {"speaker": "Customer", "text": "Really? Where was it made?"},
        {"speaker": "Seller", "text": "Here in Eskişehir, by a small group of women."},
        {"speaker": "Customer", "text": "And what's this little thing used for?"},
        {"speaker": "Seller", "text": "It's used for keeping your keys together. It's made of wood, so it's very light."}],
     "questions": [
        mc("What is the bag made from?", ["Old water bottles", "Wood", "Cotton"], 0, "\"it's made from old water bottles\""),
        mc("What is the small wooden thing used for?", ["Opening bottles", "Keeping keys together", "Decoration"], 1, "\"It's used for keeping your keys together.\""),
     ]},
    {"explanation": "**Malzeme:**\n\n| Kalıp | Anlam | Örnek |\n|---|---|---|\n| **made of** | malzeme **görünür**, değişmemiş | The table is **made of** wood. |\n| **made from** | malzeme **dönüşmüş** | Paper is **made from** wood. / Cheese is made from milk. |\n| **made in** | üretim **yeri** | It was **made in** Italy. |\n| **made by** | **yapan** | It was **made by** hand / by a local artist. |\n\n**Amaç:** **used for** + -ing / isim\n\n- It's **used for cutting** glass.\n- It's **used for** cooking.\n\n**Edilgen sorular:** (Soru kelimesi) + be + özne + V3?\n\n| Soru | Cevap |\n|---|---|\n| What **is** it **made of**? | It's made of glass. |\n| Where **was** it **made**? | It was made in Japan. |\n| What **is** it **used for**? | It's used for opening tins. |\n| When **was** it **invented**? | It was invented in 1876. |\n| **Is** it **made** by hand? | Yes, it is. / No, it isn't. |",
     "examples": [{"en": "What's this jacket made of? – It's made of leather.", "tr": "Bu ceket neden yapılmış? – Deriden."},
                  {"en": "Yoghurt is made from milk.", "tr": "Yoğurt sütten yapılır."},
                  {"en": "What was this tool used for?", "tr": "Bu alet ne için kullanılıyordu?"}],
     "turkishNote": "Türkçede \"-dan yapılmış\" tek bir yapıyla ifade edilir, İngilizcede ise made of (malzeme görünüyor) ve made from (malzeme dönüşmüş) ayrımı vardır. Masaya bakınca ahşabı görürsünüz → made of wood. Kâğıda bakınca ağacı göremezsiniz → made from wood."},
    [
        mc("The chair is ___ metal. (metal görünüyor)", ["made of", "made from"], 0, "Görünür → made of."),
        mc("Wine is ___ grapes.", ["made of", "made from"], 1, "Dönüşmüş → made from."),
        mc("These shoes were made ___ Italy.", ["in", "by", "of"], 0, "Yer → made in."),
        mc("Hangisi doğru soru?", ["What it is made of?", "What is it made of?"], 1, "What + is + özne + V3?"),
        gap("This knife is used ___ cutting bread.", ["for"], "used for + -ing."),
        gap("Where ___ your phone made? (geçmiş)", ["was"], "Where was it made?"),
        gap("Cheese is made ___ milk.", ["from"], "made from."),
        gap("This scarf was made ___ hand.", ["by"], "made by hand."),
        listen("This is a traditional coffee pot. It's made of copper and it's used for making Turkish coffee. This one was made in Gaziantep about forty years ago.", "Cezve neden yapılmış?", ["Bakırdan", "Gümüşten", "Çelikten"], 0, "\"It's made of copper\""),
        typ("Soru sorun: Bir nesnenin ne için kullanıldığını öğrenmek istiyorsunuz.", variants("What is it used for?", "What's it used for?", "What is this used for?", "What's this used for?", "What is this thing used for?", "What's this thing used for?"), "What is it used for?"),
    ],
    {"kind": "speaking", "task": speak("Evinizdeki 3 nesneyi JAI'ye tanıtın. Her biri için neden yapıldığını, nerede ve kim tarafından yapıldığını, ne için kullanıldığını söyleyin. Sonra JAI size bir nesne tarif edecek; edilgen sorular sorarak ne olduğunu bulun.",
                                       "This is my tea glass. It's made of glass, and it was made in Turkey. It's used for drinking tea, of course! This rug is made of wool. It was made by hand in Isparta. ... Is it made of metal? What is it used for? Was it invented a long time ago?",
                                       ["made of / from / in / by", "used for + -ing", "Edilgen sorular doğru"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Yeni bir icat", "Bir ürünü ya da icadı edilgen ve etken yapıları bir arada kullanarak tanıtabilirim.",
    {"kind": "text", "title": "Genç mucit yarışmasının kazananı", "body": "This year's Young Inventor Prize was won by 16-year-old Ada Çelik from Trabzon.\n\nAda designed a small device that warns older people when they forget to turn off the cooker. \"My grandmother lives alone, and once she left the cooker on all night,\" Ada explained. \"Luckily, nothing happened, but I was really worried.\"\n\nThe device is attached to the wall near the cooker. It is powered by a small battery and it is connected to the family's phones. If the cooker is left on for too long, a message is sent to the family.\n\nThe first 100 devices were produced last month, and they will be tested in homes in Trabzon this winter.",
     "questions": [
        mc("Why did Ada design the device?", ["For a school project", "Because her grandmother once left the cooker on", "To win money"], 1, "\"once she left the cooker on all night\""),
        mc("What happens if the cooker is left on for too long?", ["The cooker turns off.", "A message is sent to the family.", "An alarm calls the police."], 1, "\"a message is sent to the family\""),
     ]},
    {"explanation": "**Bir ürünü tanıtırken** passive ve active birlikte kullanılır:\n\n| Bilgi | Kalıp |\n|---|---|\n| Ne olduğu | It's a small device **that** warns people when ... |\n| Kim tasarladı | It **was designed by** ... |\n| Nasıl çalışıyor | It **is powered by** a battery. / It **is connected to** ... |\n| Malzeme | It**'s made of** ... |\n| Amaç | It**'s used for** + -ing |\n| Avantaj | It **saves** time / money. It's **easy to use**. |\n\n**Gelecekle ilgili bir bilgi** için (will be + V3) bir sonraki seviyelerde ayrıntılı göreceğiz; şimdilik kalıp olarak bilin:\n\n- They **will be tested** this winter. (Bu kış test edilecekler.)\n\n**Ürünü övmek:**\n\n- It's **really useful / practical / easy to use**.\n- It **makes life easier** for ...\n- **The best thing about it is** ...",
     "examples": [{"en": "It's powered by solar energy.", "tr": "Güneş enerjisiyle çalışır."},
                  {"en": "The best thing about it is that it's very light.", "tr": "En iyi yanı çok hafif olması."},
                  {"en": "It makes life easier for people who live alone.", "tr": "Yalnız yaşayan insanların hayatını kolaylaştırıyor."}],
     "turkishNote": "\"... ile çalışır\" (pille, elektrikle, güneş enerjisiyle) için İngilizcede \"works with\" yerine \"is powered by\" ya da \"runs on\" kullanılır: It's powered by a battery / It runs on batteries."},
    [
        mc("\"Pille çalışıyor.\"", ["It works with battery.", "It's powered by a battery."], 1, "powered by."),
        mc("The prize ___ by a 16-year-old girl.", ["won", "was won"], 1, "Passive → was won."),
        mc("Ada ___ the device herself.", ["designed", "was designed"], 0, "Yapan önemli → active."),
        gap("It's connected ___ your phone.", ["to"], "connected to."),
        gap("The best thing ___ it is the price.", ["about"], "The best thing about..."),
        gap("It makes life ___ for older people. (kolay)", ["easier"], "makes life easier."),
        gap("The first devices ___ produced last month.", ["were"], "Çoğul past → were."),
        match([("designed by", "tarafından tasarlanmış"), ("powered by", "... ile çalışan"), ("made of", "-den yapılmış"), ("used for", "için kullanılan"), ("easy to use", "kullanımı kolay")], "Eşleştirin."),
        listen("Our new bottle is made from recycled glass. It's designed for people who exercise. The best thing about it is that it keeps water cold for 24 hours.", "Şişenin en iyi özelliği ne?", ["Çok ucuz olması", "Suyu 24 saat soğuk tutması", "Çok büyük olması"], 1, "\"it keeps water cold for 24 hours\""),
        typ("İngilizce yazın: \"Güneş enerjisiyle çalışır.\"", variants("It's powered by solar energy.", "It is powered by solar energy.", "It runs on solar energy.", "It's powered by the sun.", "It is powered by the sun."), "It's powered by solar energy."),
    ],
    {"kind": "writing", "task": write("Hayali bir icadı tanıtan kısa bir yazı yazın (120–150 kelime): Ne olduğu, kim tarafından ve neden tasarlandığı, neden yapıldığı, nasıl çalıştığı ve ne için kullanıldığı. En az 6 edilgen cümle kullanın ve etken yapıyla karıştırın.",
                                      "The Smart Umbrella\n\nThe Smart Umbrella was designed by a team of students in Ankara. The idea came from one of the students. She often left her umbrella on buses.\n\nThe umbrella is made of strong, light plastic, and the handle is made from recycled metal. It is powered by a tiny battery, and it is connected to your phone. If you leave it somewhere, a message is sent to your phone immediately. The umbrella also checks the weather. When rain is expected, a small light on the handle turns blue.\n\nThe first 500 umbrellas were produced in September, and they were sold out in two days. The best thing about it is that you'll never lose your umbrella again!",
                                      ["Present / past passive doğru", "Active ile karışık kullanım", "made of / powered by / used for", "Tanıtım üslubu", "Düzenli metin"])},
)

u.test([
    mc("\"Pirinç Asya'da yetiştirilir.\"", ["Rice grows in Asia.", "Rice is grown in Asia.", "Rice is grow in Asia."], 1, "is + V3"),
    mc("The telephone ___ by Bell.", ["invented", "was invented", "is invent"], 1, "was + V3"),
    mc("These cars ___ in Germany.", ["is made", "are made"], 1, "Çoğul → are"),
    mc("Penicillin was discovered ___ Fleming.", ["from", "by", "of"], 1, "by"),
    mc("Glass is made ___ sand.", ["of", "from"], 1, "made from"),
    gap("The bridge was ___ in 1988. (build)", ["built"], "V3"),
    gap("My bike ___ stolen yesterday.", ["was"], "was"),
    gap("This tool is used ___ opening bottles.", ["for"], "used for"),
    gap("Where ___ these shoes made? (geçmiş, çoğul)", ["were"], "were"),
    mc("Yapan önemli:", ["My grandfather built this house.", "This house was built."], 0, "Active"),
    mc("\"They clean the office every evening.\" → Edilgen:", ["The office is cleaned every evening.", "The office was cleaned every evening."], 0, "Present passive"),
    mc("Doğru soru:", ["What it is made of?", "What is it made of?"], 1, "Soru sırası"),
    listen("This watch was made in Switzerland in 1960. It was given to my grandfather when he retired. It's made of gold.", "Saat ne zaman yapıldı?", ["1960'ta", "Dedesi emekli olunca", "Geçen yıl"], 0, "\"made in Switzerland in 1960\""),
    typ("Edilgen yapın: \"Someone stole my phone last night.\"", variants("My phone was stolen last night.", "Last night my phone was stolen.", "My phone was stolen last night by someone."), "My phone was stolen last night."),
    write("Ülkenizden ünlü bir ürünü, yapıyı ya da yemeği tanıtan bir yazı yazın (120–150 kelime): Nerede ve nasıl yapılır, ne zaman ve kim tarafından yapıldı ya da icat edildi, ne için kullanılır? Present ve past passive, made of / from ve by kullanın.",
          "Turkish carpets are famous all over the world. They are made in many parts of Turkey, but some of the most famous ones are made in Hereke, Kayseri and Uşak. A traditional carpet is made of wool or silk, and the colours are made from plants. Every carpet is made by hand, and a large one can take more than a year. Each carpet is different, and its patterns often tell a story about the place where it was made. In the past, carpets were used for sitting and sleeping, but today they are mainly used for decoration. Many old carpets were sold to museums, and some of them are shown in Istanbul's Turkish and Islamic Arts Museum.",
          ["Present / past passive", "made of / from / by / in", "Doğru bilgi ya da belirsizlik ifadesi", "Active ile denge", "Düzenli metin"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

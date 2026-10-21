"""B1 Ünite 8: İnsanlar ve yerler."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("B1", 8, "İnsanlar ve yerler", "People and Places",
         "İnsanları, nesneleri ve yerleri who, which, that, where ve whose ile tanımlayabilir, bilmediğim bir kelimeyi açıklayarak anlatabilir ve sevdiğim bir yeri ayrıntılı bir şekilde tanıtabilirim.",
         ["defining relative clauses: who / which", "that ve ilgi zamirinin atlanması", "where ve whose", "tanımlama ve açıklama stratejileri", "ilgi cümleleriyle yer tanıtma"],
         ["insanlar ve roller", "şehirdeki yerler", "tanımlama dili"],
         {"title": "Tabu!", "durationMinutes": 45,
          "goal": "Öğrenciler takımlar halinde \"Tabu\" oynar: Kartlardaki kelimeyi söylemeden It's a person who... / It's a thing which... / It's a place where... kalıplarıyla anlatırlar. İkinci turda herkes kendi şehrinden bir yeri ya da tanıdığı ilginç bir kişiyi ilgi cümleleriyle tanıtır ve diğerleri tahmin eder."})

u.vocab([
    ("neighbour", "komşu", "My neighbour is a man who plays the violin.", "Komşum keman çalan bir adam.", None),
    ("colleague", "iş arkadaşı", "She's a colleague who helps everyone.", "Herkese yardım eden bir iş arkadaşı.", None),
    ("stranger", "yabancı (tanınmayan kişi)", "A stranger helped me with my bag.", "Bir yabancı çantama yardım etti.", "foreigner = başka ülkeden"),
    ("flatmate", "ev arkadaşı", "My flatmate is the person who cooks.", "Ev arkadaşım yemek yapan kişi.", None),
    ("owner", "sahip", "He's the owner of the café.", "Kafenin sahibi o.", None),
    ("local", "yerel; yöre halkı", "Ask a local for directions.", "Yol tarifi için yöre halkından birine sor.", None),
    ("tourist", "turist", "It's a place which is full of tourists.", "Turist dolu bir yer.", None),
    ("square", "meydan", "There's a square where people meet.", "İnsanların buluştuğu bir meydan var.", None),
    ("market", "pazar", "It's the market where I buy vegetables.", "Sebze aldığım pazar bu.", None),
    ("neighbourhood", "mahalle", "I grew up in a quiet neighbourhood.", "Sakin bir mahallede büyüdüm.", None),
    ("harbour", "liman", "We had dinner at a restaurant by the harbour.", "Limanın yanındaki bir restoranda yemek yedik.", None),
    ("hidden", "gizli, saklı", "It's a hidden beach that only locals know.", "Sadece yerlilerin bildiği saklı bir plaj.", None),
    ("crowded", "kalabalık", "The streets are crowded in summer.", "Yazın sokaklar kalabalık.", None),
    ("peaceful", "huzurlu", "It's a peaceful village.", "Huzurlu bir köy.", None),
    ("lively", "canlı, hareketli", "Kadıköy is a lively area.", "Kadıköy hareketli bir semt.", None),
    ("view", "manzara", "It's a café with an amazing view.", "Harika manzaralı bir kafe.", None),
    ("whose", "-in (sahiplik; ilgi zamiri)", "That's the man whose dog bit me.", "Köpeği beni ısıran adam o.", None),
    ("where", "-dığı yer (ilgi zamiri)", "This is the house where I was born.", "Bu, doğduğum ev.", None),
    ("thing", "şey", "It's a thing which you use for cooking.", "Yemek yapmak için kullandığın bir şey.", None),
    ("kind of", "bir çeşit", "It's a kind of bread.", "Bir çeşit ekmek.", None),
    ("tool", "alet", "It's a tool that you use to open bottles.", "Şişe açmak için kullandığın bir alet.", None),
    ("remind (of)", "hatırlatmak", "This place reminds me of my childhood.", "Bu yer bana çocukluğumu hatırlatıyor.", None),
    ("worth visiting", "görülmeye değer", "The old town is worth visiting.", "Eski şehir görülmeye değer.", None),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Kim? Hangisi?", "who ve which ile insanları ve nesneleri tanımlayabilirim.",
    {"kind": "dialogue", "title": "Düğün fotoğrafları", "lines": [
        {"speaker": "Pınar", "text": "Who's the woman who's wearing the red dress?"},
        {"speaker": "Onur", "text": "That's my aunt Nesrin. She's the one who organised the whole wedding."},
        {"speaker": "Pınar", "text": "And the man who's dancing?"},
        {"speaker": "Onur", "text": "My cousin Batu. He's a chef. He made the cake which everyone loved."},
        {"speaker": "Pınar", "text": "It looks amazing! What's that thing which the children are holding?"},
        {"speaker": "Onur", "text": "They're little bags which have sweets inside. It's a tradition in our family."}],
     "questions": [
        mc("Who organised the wedding?", ["Onur's cousin", "Onur's aunt", "Pınar"], 1, "\"She's the one who organised the whole wedding.\""),
        mc("What did Batu make?", ["The bags", "The cake", "The dresses"], 1, "\"He made the cake which everyone loved.\""),
     ]},
    {"explanation": "**İlgi cümleleri (relative clauses)**, hangi kişiden ya da şeyden bahsettiğimizi **tanımlar**. İki cümleyi birleştirir.\n\n| İlgi zamiri | Ne için? | Örnek |\n|---|---|---|\n| **who** | **insanlar** | The woman **who** organised the wedding is my aunt. |\n| **which** | **nesneler, hayvanlar** | He made the cake **which** everyone loved. |\n\n**İki cümleyi birleştirmek:**\n\n- The man is a chef. **He** is dancing. → The man **who** is dancing is a chef.\n- I bought a phone. **It** has a great camera. → I bought a phone **which** has a great camera.\n\n**Dikkat:** who / which, he / she / it'in **yerine** geçer. Tekrar etmeyin:\n\n- The man who ~~he~~ is dancing...\n\nBu tür tanımlayıcı ilgi cümlelerinde **virgül kullanılmaz**.",
     "examples": [{"en": "A pilot is a person who flies planes.", "tr": "Pilot, uçak uçuran kişidir."},
                  {"en": "I've lost the keys which were on the table.", "tr": "Masanın üstündeki anahtarları kaybettim."},
                  {"en": "The people who live next door are very friendly.", "tr": "Yan evde oturan insanlar çok cana yakın."}],
     "turkishNote": "Türkçede ilgi cümlesi ismin önüne gelir ve ekle yapılır: \"dans eden adam\", \"herkesin sevdiği pasta\". İngilizcede sıralama tersine döner: isim önce, ilgi cümlesi sonra gelir: \"the man who is dancing\", \"the cake which everyone loved\". Türkçe sırayı korumaya çalışmak (\"the dancing who man\") en sık yapılan hatadır."},
    [
        mc("A doctor is a person ___ helps sick people.", ["who", "which"], 0, "İnsan → who."),
        mc("This is the bus ___ goes to the airport.", ["who", "which"], 1, "Nesne → which."),
        mc("Hangisi doğru?", ["The man who he lives here is a teacher.", "The man who lives here is a teacher."], 1, "who + fiil (zamir tekrarı yok)."),
        gap("The girl ___ won the race is my sister.", ["who", "that"], "İnsan → who."),
        gap("I like films ___ make me laugh.", ["which", "that"], "Nesne → which."),
        gap("The people ___ live upstairs are very noisy.", ["who", "that"], "who."),
        mc("\"Dans eden adam\"", ["the dancing who man", "the man who is dancing"], 1, "İsim + who + fiil."),
        order(["who", "The", "woman", "lives", "next", "door", "is", "a", "doctor"], "The woman who lives next door is a doctor.", "İsim + who + fiil + ana fiil.", "Yan evde oturan kadın doktor."),
        listen("My best friend is someone who always tells me the truth. She's also the person who taught me to swim.", "Konuşanın en iyi arkadaşı ona ne öğretmiş?", ["Yüzmeyi", "Yemek yapmayı", "Araba kullanmayı"], 0, "\"the person who taught me to swim\""),
        typ("Birleştirin: \"I have a friend. He speaks five languages.\"", variants("I have a friend who speaks five languages.", "I've got a friend who speaks five languages.", "I have a friend that speaks five languages.", "I've got a friend that speaks five languages."), "I have a friend who speaks five languages."),
    ],
    {"kind": "speaking", "task": speak("Hayatınızdaki 5 önemli kişiyi ve 2 önemli nesneyi who ve which ile tanıtın. (\"My uncle is the person who...\", \"My bike is the thing which...\")",
                                       "My mother is the person who taught me to read. My friend Ece is someone who always makes me laugh. Mr Akın was the teacher who changed my life. My grandfather is a man who loves gardening. My phone is the thing which I use most, and my old guitar is something which I'll never sell.",
                                       ["who / which doğru seçimi", "Zamir tekrarı yok", "İsim + ilgi cümlesi sırası"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "That ve atlama", "that kullanabilir, ilgi zamirini ne zaman atlayabileceğimi bilirim.",
    {"kind": "text", "title": "Bir şehrin unutulmaz insanları", "body": "Every neighbourhood has people that everyone knows.\n\nIn our street, there's Hüseyin Bey, the shoe repairer. He's the man that fixes everything: shoes, bags, even suitcases. The shop he works in is tiny, but it's always busy.\n\nThen there's Fatma Hanım, the woman who sells simit at the corner every morning. The simit she sells are the best in the city, and she knows everyone's name.\n\nAnd there's Rıza, the cat that sleeps on the bakery window. He's the only cat I know that has his own Instagram account!",
     "questions": [
        mc("What does Hüseyin Bey do?", ["He sells simit.", "He repairs shoes and bags.", "He owns the bakery."], 1, "\"the shoe repairer... fixes everything\""),
        mc("Who is Rıza?", ["A baker", "A cat", "A neighbour"], 1, "\"Rıza, the cat that sleeps on the bakery window\""),
     ]},
    {"explanation": "**that**, tanımlayıcı ilgi cümlelerinde **who ve which yerine** kullanılabilir. Günlük konuşmada çok yaygındır.\n\n- The man **that** (= who) fixes everything.\n- The cat **that** (= which) sleeps on the window.\n\n**İlgi zamirini atlamak:**\n\nİlgi zamiri cümlenin **nesnesi** ise (ondan sonra **bir özne** geliyorsa) atlanabilir.\n\n| Özne (atlanamaz) | Nesne (atlanabilir) |\n|---|---|\n| The woman **who sells** simit. | The simit (**that**) **she** sells. |\n| The man **that fixes** shoes. | The shop (**which**) **he** works in. |\n| who / that + **fiil** | (who / that) + **özne** + fiil |\n\n- The book (that) **I** bought is great. ✓\n- The book ~~bought~~... → The book **that** is on the table. (Burada that öznedir, atlanamaz.)",
     "examples": [{"en": "The film we saw last night was brilliant.", "tr": "Dün gece izlediğimiz film harikaydı."},
                  {"en": "Is this the phone you lost?", "tr": "Kaybettiğin telefon bu mu?"},
                  {"en": "She's the person that told me the news.", "tr": "Bana haberi veren kişi o."}],
     "turkishNote": "Türkçedeki \"izlediğimiz film\", \"kaybettiğin telefon\" gibi yapılar İngilizcede çoğunlukla ilgi zamiri olmadan kurulur: the film we saw, the phone you lost. Bu yapı konuşmada çok doğal ve yaygındır; dinlerken fark etmeye çalışın."},
    [
        mc("\"that\" hangisinin yerine kullanılabilir?", ["Sadece who", "Sadece which", "Hem who hem which"], 2, "Tanımlayıcı cümlelerde ikisi de."),
        mc("İlgi zamiri atlanabilir mi? \"The book that I read was boring.\"", ["Evet", "Hayır"], 0, "that'ten sonra özne (I) var → atlanabilir."),
        mc("İlgi zamiri atlanabilir mi? \"The man that lives here is old.\"", ["Evet", "Hayır"], 1, "that öznedir → atlanamaz."),
        mc("Hangisi doğru?", ["The film we saw was great.", "The film saw was great."], 0, "Nesne → atlanabilir, özne kalır."),
        gap("Is this the bag ___ you lost? (boş bırakılabilir; bir kelime yazın)", ["that", "which"], "that / which."),
        gap("The man ___ helped me was very kind.", ["who", "that"], "Özne → atlanamaz."),
        gap("The pizza ___ made was delicious. (biz)", ["we"], "the pizza (that) we made."),
        order(["the", "This", "is", "restaurant", "I", "told", "you", "about"], "This is the restaurant I told you about.", "Nesne ilgi cümlesi, that atlanmış.", "Sana bahsettiğim restoran bu."),
        listen("Do you remember the café we found last summer? The one that had the amazing cheesecake? It's closed now.", "Kafeye ne olmuş?", ["Taşınmış", "Kapanmış", "Yenilenmiş"], 1, "\"It's closed now.\""),
        typ("İngilizce yazın (that kullanmadan): \"Dün gece izlediğimiz film harikaydı.\"", variants("The film we saw last night was great.", "The film we watched last night was great.", "The film we saw last night was brilliant.", "The film we watched last night was brilliant.", "The movie we saw last night was great.", "The movie we watched last night was great.", "The film we saw last night was amazing.", "The film we watched last night was amazing."), "The film we saw last night was great."),
    ],
    {"kind": "speaking", "task": speak("Mahallenizdeki ya da iş yerinizdeki \"unutulmaz\" 3 kişiyi tanıtın. that kullanın ve ilgi zamirini atladığınız en az 2 cümle kurun (\"The bread he makes...\", \"The songs she sings...\").",
                                       "In my office there's Recep, the man that knows everything about computers. The coffee he makes is terrible, but everyone loves him. There's also Nihan, the woman that organises all the parties. The cakes she brings on Fridays are famous!",
                                       ["that doğru", "Nesne ilgi cümlesinde atlama", "Özne cümlesinde atlamama"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "Nerede, kimin?", "where ile yerleri, whose ile sahipliği tanımlayabilirim.",
    {"kind": "dialogue", "title": "Eski mahallede", "lines": [
        {"speaker": "Hande", "text": "This is the street where I grew up!"},
        {"speaker": "Levent", "text": "Really? Which house was yours?"},
        {"speaker": "Hande", "text": "The blue one. And that's the park where I learned to ride a bike."},
        {"speaker": "Levent", "text": "Who lives in the big house on the corner?"},
        {"speaker": "Hande", "text": "That's the family whose son was my best friend at school. Oh, and look! That's the bakery where we bought bread every morning."},
        {"speaker": "Levent", "text": "It's like a museum of your childhood!"}],
     "questions": [
        mc("What did Hande learn in the park?", ["To swim", "To ride a bike", "To play football"], 1, "\"the park where I learned to ride a bike\""),
        mc("Who lives in the big house on the corner?", ["Hande's aunt", "The family of her school best friend", "The baker"], 1, "\"the family whose son was my best friend\""),
     ]},
    {"explanation": "**where** → **yerler** için (-dığı yer)\n\n- This is the street **where** I grew up. (Büyüdüğüm sokak)\n- That's the bakery **where** we bought bread.\n\n**where** = in which / at which. Ondan sonra **özne + fiil** gelir.\n\n**Dikkat:** Yer bir **nesne** gibi kullanılıyorsa **which / that** gelir:\n\n| where (orada bir şey olur) | which / that (yer özne ya da nesne) |\n|---|---|\n| The city **where** I live. | The city **which** has the best food. |\n| The hotel **where** we stayed. | The hotel **that** we chose. |\n\n**whose** → **sahiplik** (-in, -ın)\n\n- That's the family **whose** son was my friend. (Oğlu benim arkadaşım olan aile)\n- I have a friend **whose** father is a famous actor.\n\n**whose + isim** birlikte kullanılır.\n\n**Not:** Dinlediğiniz ve okuduğunuz metinlerde virgülle ayrılmış ilgi cümleleri de göreceksiniz: *My cousin, whose family owns a hotel, ...* Bunlar kişiyi tanımlamaz, sadece **ek bilgi** verir. Ayrıntılarını B2'de göreceğiz.",
     "examples": [{"en": "Rize is the city where most Turkish tea is grown.", "tr": "Rize, Türk çayının çoğunun yetiştirildiği şehir."},
                  {"en": "That's the woman whose car was stolen.", "tr": "Arabası çalınan kadın o."},
                  {"en": "Do you know a place where we can park?", "tr": "Park edebileceğimiz bir yer biliyor musun?"}],
     "turkishNote": "Türkçede \"büyüdüğüm sokak\", \"arabası çalınan kadın\" gibi yapılar ek ile kurulur. İngilizcede yer için where, sahiplik için whose kullanılır. \"The woman who her car was stolen\" yanlıştır; whose zaten \"onun\" anlamını içerir: \"the woman whose car was stolen\"."},
    [
        mc("This is the hotel ___ we stayed last year.", ["where", "which", "whose"], 0, "Yer + özne + fiil → where."),
        mc("That's the man ___ dog barks all night.", ["who", "whose", "which"], 1, "Sahiplik → whose."),
        mc("Hangisi doğru?", ["The woman who her son is a doctor.", "The woman whose son is a doctor."], 1, "whose + isim."),
        mc("Istanbul is a city ___ is on two continents.", ["where", "which"], 1, "Şehir özne → which."),
        gap("The café ___ we met is closed now.", ["where"], "where."),
        gap("I have a friend ___ mother is a pilot.", ["whose"], "whose."),
        gap("Is there a shop ___ I can buy a charger?", ["where"], "where."),
        gap("The student ___ phone rang had to leave the room.", ["whose"], "whose + phone."),
        listen("Bodrum is the town where I spend every summer. My cousin, whose family owns a small hotel there, always finds me a room.", "Kuzeninin ailesi neyin sahibi?", ["Bir restoranın", "Küçük bir otelin", "Bir teknenin"], 1, "\"whose family owns a small hotel there\""),
        typ("İngilizce yazın: \"Bu, doğduğum ev.\"", variants("This is the house where I was born.", "This is the house I was born in.", "This is the house that I was born in.", "This is the house which I was born in."), "This is the house where I was born."),
    ],
    {"kind": "speaking", "task": speak("Çocukluğunuzun geçtiği mahalleyi ya da şehri JAI'ye bir \"tur\" gibi anlatın. En az 4 where ve 2 whose cümlesi kurun.",
                                       "This is the school where I studied for eight years. That's the corner where we played football every evening. There's the shop where I bought my first comic. And that's the house of Mrs Kılıç, whose cakes were famous in the whole neighbourhood. My friend Taner, whose father was a fisherman, lived next to the harbour.",
                                       ["where doğru", "whose + isim", "Akıcı tur anlatımı"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Kelimeyi unuttum!", "Bilmediğim ya da unuttuğum bir kelimeyi ilgi cümleleriyle tarif edip anlatabilirim.",
    {"kind": "dialogue", "title": "Hırdavatçıda", "lines": [
        {"speaker": "Customer", "text": "Hi, I'm looking for... I don't know the word in English. It's a tool that you use to put nails into wood."},
        {"speaker": "Assistant", "text": "Oh, a hammer?"},
        {"speaker": "Customer", "text": "Yes, a hammer! And I also need a thing which holds pictures on the wall."},
        {"speaker": "Assistant", "text": "Do you mean a hook?"},
        {"speaker": "Customer", "text": "I'm not sure. It's a kind of small metal thing. It's similar to a nail, but it's curved at the end."},
        {"speaker": "Assistant", "text": "Yes, that's a hook. They're over there, next to the person who's wearing a red jacket."}],
     "questions": [
        mc("What is a hammer used for?", ["Putting nails into wood", "Cutting wood", "Painting walls"], 0, "\"a tool that you use to put nails into wood\""),
        mc("What did the customer describe as \"similar to a nail, but curved\"?", ["A screw", "A hook", "A hammer"], 1, "\"Yes, that's a hook.\""),
     ]},
    {"explanation": "Bir kelimeyi bilmediğinizde **durmayın, tarif edin!** Bu, iyi konuşanların en önemli becerilerinden biridir.\n\n| Ne? | Kalıp |\n|---|---|\n| Kişi | It's **a person who** ... / It's **someone who** ... |\n| Nesne | It's **a thing which / that** ... / It's **something you use to / for** ... |\n| Yer | It's **a place where** ... |\n| Tür | It's **a kind of** ... / It's **a type of** ... |\n| Benzerlik | It's **similar to** ... / It's **like** a ..., **but** ... |\n| Görünüş | It's **made of** ... / It **looks like** ... |\n\n**Yardım istemek:**\n\n- **What's the word for** ...?\n- **What do you call** a person who ...?\n- **I don't know the word in English, but** ...\n- **Do you know what I mean?**\n\n**Karşı taraf:** Do you mean ...? / Oh, you mean a ...!",
     "examples": [{"en": "What do you call a person who designs buildings?", "tr": "Bina tasarlayan kişiye ne denir?"},
                  {"en": "It's a place where you can borrow books.", "tr": "Kitap ödünç alabileceğin bir yer."},
                  {"en": "It's a kind of soup which is made from lentils.", "tr": "Mercimekten yapılan bir çeşit çorba."}],
     "turkishNote": "Türkçe konuşanlar İngilizce konuşurken bir kelimeyi bilmediklerinde genellikle duraklar ya da Türkçe kelimeyi söyler. Bunun yerine \"It's a thing which...\" ile tarif etmek hem iletişimi sürdürür hem de pratik yapmanızı sağlar. \"What do you call...?\" sorusu kelime öğrenmenin en kolay yollarından biridir."},
    [
        mc("Kitap ödünç alınan yer:", ["It's a person who lends books.", "It's a place where you can borrow books."], 1, "Yer → a place where."),
        mc("\"Bina tasarlayan kişiye ne denir?\"", ["What do you say a person who designs buildings?", "What do you call a person who designs buildings?"], 1, "What do you call...?"),
        mc("It's a person who designs buildings.", ["architect", "engineer", "builder"], 0, "architect."),
        mc("It's a place where you can see old and valuable things.", ["museum", "market", "harbour"], 0, "museum."),
        gap("It's a ___ of bread which is popular in Turkey. (bir çeşit)", ["kind", "type", "sort"], "a kind of."),
        gap("It's ___ to a sofa, but smaller. (benzer)", ["similar"], "similar to."),
        gap("It's something you use ___ cut paper.", ["to"], "use to + fiil."),
        gap("Do you ___ a hook? (demek istemek)", ["mean"], "Do you mean...?"),
        listen("It's a person who works on a plane. They help passengers, serve food and drinks and explain the safety rules.", "Tarif edilen kişi kim?", ["Pilot", "Kabin görevlisi", "Mühendis"], 1, "Uçakta yolculara yardım eden, yemek servis eden → flight attendant."),
        typ("Tarif edin (kelimeyi kullanmadan): \"umbrella\" (It's a thing...)", variants("It's a thing which you use when it rains.", "It's a thing that you use when it rains.", "It's a thing you use when it rains.", "It's a thing which you use when it's raining.", "It's a thing that you use when it's raining.", "It's a thing you use when it's raining.", "It's a thing which keeps you dry in the rain.", "It's a thing that keeps you dry in the rain.", "It's a thing which you use in the rain.", "It's a thing you use in the rain."), "It's a thing which you use when it rains."),
    ],
    {"kind": "speaking", "task": speak("Tabu oyunu: JAI size 6 kelime verecek (dentist, airport, scissors, librarian, kitchen, fridge). Kelimeyi söylemeden who / which / where, a kind of ve similar to ile tarif edin. JAI tahmin edecek.",
                                       "It's a person who looks after your teeth. ... It's a place where planes take off and land. ... It's a thing which you use to cut paper. It's made of metal. ... It's a kind of big cold box which keeps food fresh.",
                                       ["who / which / where doğru", "Tarif kalıpları çeşitli", "Kelimeyi söylemeden anlaşılır tarif"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Benim yerim", "Sevdiğim bir yeri ilgi cümleleri ve betimleyici kelimelerle canlı bir şekilde tanıtabilirim.",
    {"kind": "text", "title": "Gezgin blogu: Saklı bir köy", "body": "Last spring I discovered a village that I'll never forget.\n\nIt's a small place in the mountains above Fethiye, where only about 200 people live. The road which goes up to the village is narrow and steep, but the view from the top is worth it.\n\nThe heart of the village is a little square with an old plane tree, where the men play backgammon and drink tea all day. Next to it, there's a café whose owner, Gülsüm Teyze, makes the best gözleme I've ever eaten.\n\nWhat I loved most were the people. Strangers who I'd never met invited me into their homes. It's the kind of place that reminds you how kind people can be.",
     "questions": [
        mc("How many people live in the village?", ["About 200", "About 2,000", "About 20"], 0, "\"only about 200 people live\""),
        mc("What does the writer say about the people?", ["They were unfriendly.", "They invited the writer into their homes.", "They didn't speak to tourists."], 1, "\"Strangers... invited me into their homes.\""),
     ]},
    {"explanation": "**Bir yeri tanıtırken:**\n\n| Bilgi | Kalıp |\n|---|---|\n| Genel | It's a **small / lively / peaceful** place **where** ... |\n| Konum | It's **in the mountains / by the sea / near** ... |\n| Öne çıkan | **The heart of** the town is ... / **The best thing about** it is ... |\n| Kişiler | There's a café **whose owner** ... / The people **who live there** ... |\n| Duygu | It's **the kind of place that** ... / It **reminds me of** ... |\n| Tavsiye | It's **worth visiting**. / **If you go there**, don't miss ... |\n\n**Betimleyici sıfatlar:**\n\n| Olumlu | Olumsuz |\n|---|---|\n| peaceful, lively, charming, picturesque | crowded, noisy, dirty, touristy |\n\n**Virgüllü ilgi cümleleri:** Yeri zaten belli olan bir şeye **ek bilgi** eklerken virgül kullanılır: *a village above Fethiye, where only 200 people live*. Bu kullanımda **that** kullanılmaz.\n\n**İlgi cümleleriyle zenginleştirme:**\n\n- There's a café. → There's **a tiny café whose owner** makes the best gözleme **I've ever eaten**.",
     "examples": [{"en": "It's the kind of place that you never want to leave.", "tr": "Hiç ayrılmak istemeyeceğin türden bir yer."},
                  {"en": "This town reminds me of my grandparents' village.", "tr": "Bu kasaba bana büyükannemlerin köyünü hatırlatıyor."},
                  {"en": "If you go there, don't miss the fish market.", "tr": "Oraya gidersen balık pazarını kaçırma."}],
     "turkishNote": "\"Bana ... hatırlatıyor\" için \"It remembers me\" demek yaygın bir hatadır. Doğrusu \"It reminds me of ...\". remember (hatırlamak) ile remind (hatırlatmak) farklı fiillerdir."},
    [
        mc("\"Bana çocukluğumu hatırlatıyor.\"", ["It remembers me my childhood.", "It reminds me of my childhood."], 1, "remind of."),
        mc("Huzurlu bir köy:", ["a peaceful village", "a crowded village", "a noisy village"], 0, "peaceful."),
        mc("Turist dolu, doğallığını kaybetmiş:", ["charming", "touristy", "hidden"], 1, "touristy."),
        gap("It's a town ___ you can eat fresh fish every day.", ["where"], "where."),
        gap("There's a shop ___ owner speaks five languages.", ["whose"], "whose."),
        gap("The old town is worth ___. (ziyaret)", ["visiting", "seeing"], "worth + -ing."),
        gap("It's the kind of place ___ you never forget.", ["that", "which"], "the kind of place that."),
        match([("peaceful", "huzurlu"), ("lively", "hareketli"), ("crowded", "kalabalık"), ("hidden", "saklı"), ("view", "manzara")], "Eşleştirin."),
        listen("My favourite place in Istanbul is a small tea garden in Üsküdar. It's a place where you can watch the boats and the sunset. It reminds me of summer evenings with my father.", "Bu yer konuşana neyi hatırlatıyor?", ["Okul günlerini", "Babasıyla yaz akşamlarını", "İlk işini"], 1, "\"It reminds me of summer evenings with my father.\""),
        typ("İngilizce yazın: \"Oraya gidersen balık pazarını kaçırma.\"", variants("If you go there, don't miss the fish market.", "If you go there, do not miss the fish market.", "Don't miss the fish market if you go there.", "If you go there don't miss the fish market."), "If you go there, don't miss the fish market."),
    ],
    {"kind": "writing", "task": write("Sevdiğiniz bir yeri (şehir, köy, semt, kafe, park) tanıtan bir blog yazısı yazın (130–160 kelime). En az 5 ilgi cümlesi (who, which, that, where, whose) ve en az 4 betimleyici sıfat kullanın. Sonunda okuyucuya bir tavsiye verin.",
                                      "Kuzguncuk: Istanbul's Hidden Village\n\nKuzguncuk is a small neighbourhood on the Asian side of Istanbul which feels like a village. It's a peaceful place where old wooden houses stand next to each other on narrow streets.\n\nThe heart of the neighbourhood is the main street, where you can find little cafés, a bakery and a bookshop whose owner always recommends great novels. On Sundays, the street is lively but never too crowded.\n\nWhat I love most are the people who live there. Neighbours still say hello to each other and chat outside their doors. It's the kind of place that reminds me of the Istanbul my grandparents talked about.\n\nIf you go there, don't miss the small garden by the sea, which is perfect for a cup of tea at sunset. It's definitely worth visiting!",
                                      ["En az 5 ilgi cümlesi", "who / which / where / whose doğru", "Betimleyici sıfatlar", "Tavsiye", "Blog üslubu ve düzen"])},
)

u.test([
    mc("A teacher is a person ___ helps students learn.", ["who", "which", "where"], 0, "who"),
    mc("This is the train ___ goes to Ankara.", ["who", "which"], 1, "which"),
    mc("That's the café ___ we first met.", ["which", "where"], 1, "where"),
    mc("I have a friend ___ brother is a famous singer.", ["who", "whose"], 1, "whose"),
    mc("Hangisi doğru?", ["The man who he called me was angry.", "The man who called me was angry."], 1, "Zamir tekrarı yok"),
    mc("İlgi zamiri atlanabilir mi? \"The cake that she made was delicious.\"", ["Evet", "Hayır"], 0, "Nesne → atlanabilir"),
    gap("The people ___ live next door are from Japan.", ["who", "that"], "who / that"),
    gap("Is this the phone ___ you were looking for?", ["that", "which"], "that / which"),
    gap("This is the town ___ my father was born.", ["where"], "where"),
    gap("It reminds me ___ my holiday in Greece.", ["of"], "remind of"),
    mc("\"Kitap ödünç alınan yer\" →", ["a library", "a bookshop"], 0, "library"),
    gap("What do you ___ a person who repairs cars? (ne denir)", ["call"], "What do you call...?"),
    listen("The best teacher I ever had was Ms Sevim, whose lessons were always full of music. She's the person who made me love English.", "Konuşanın en iyi öğretmeninin dersleri nasıldı?", ["Çok sessizdi", "Müzikle doluydu", "Çok zordu"], 1, "\"whose lessons were always full of music\""),
    typ("Birleştirin: \"That's the woman. Her car was stolen.\"", variants("That's the woman whose car was stolen.", "That is the woman whose car was stolen."), "That's the woman whose car was stolen."),
    write("Hayatınızda önemli bir yere sahip bir kişiyi ve onunla ilgili bir yeri anlatan bir paragraf yazın (130–160 kelime). En az 6 ilgi cümlesi (who, which, that, where, whose, atlanmış zamir) kullanın.",
          "The person who has influenced me most is my grandmother, Saniye. She's a woman who has always worked hard and never complains. She lives in a small village near Bolu, where she has a garden that's full of fruit trees. When I was a child, I spent every summer there. The house where she lives is more than a hundred years old, and the kitchen is the room I remember best. That's the place where she taught me to make bread. She has a neighbour, Hasan Amca, whose stories made us laugh every evening. The food she cooks still tastes better than anything I've eaten in restaurants. She's the kind of person who makes everyone feel at home.",
          ["En az 6 ilgi cümlesi", "Doğru ilgi zamiri seçimi", "Zamir atlama", "Betimleme", "Akıcı paragraf"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

"""A1 Ünite 11: Şu an."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("A1", 11, "Şu an", "Right Now",
         "Hava durumunu söyleyebilir, şu an ne yaptığımı ve çevremde neler olduğunu anlatabilirim.",
         ["present continuous: olumlu", "present continuous: olumsuz, soru, kısa cevaplar", "present simple ve present continuous karşılaştırması", "What's the weather like?"],
         ["hava durumu", "mevsimler", "günlük eylemler"],
         {"title": "Ne yapıyorlar?", "durationMinutes": 45,
          "goal": "Öğretmen kalabalık bir park fotoğrafı paylaşır. Öğrenciler sırayla bir kişiyi present continuous ile anlatır ('She's wearing a red hat and she's feeding the birds'); diğerleri kim olduğunu bulur. Sonra herkes kendi penceresinden gördüğünü ve havayı anlatır."})

u.vocab([
    ("weather", "hava (durumu)", "What's the weather like today?", "Bugün hava nasıl?", "Sayılamaz: a weather değil."),
    ("sunny", "güneşli", "It's sunny and warm.", "Hava güneşli ve ılık.", None),
    ("cloudy", "bulutlu", "It's cloudy this morning.", "Bu sabah hava bulutlu.", None),
    ("windy", "rüzgarlı", "It's very windy by the sea.", "Deniz kenarında çok rüzgar var.", None),
    ("rain", "yağmur; yağmur yağmak", "It's raining. Take an umbrella.", "Yağmur yağıyor. Şemsiye al.", "It's rainy (sıfat) / It's raining (şu an)."),
    ("snow", "kar; kar yağmak", "Look! It's snowing!", "Bak! Kar yağıyor!", None),
    ("hot", "sıcak", "It's very hot in August.", "Ağustosta hava çok sıcak.", None),
    ("warm", "ılık", "It's warm in spring.", "İlkbaharda hava ılık.", None),
    ("cold", "soğuk", "It's cold. Wear a coat.", "Hava soğuk. Palto giy.", None),
    ("degrees", "derece", "It's twenty-five degrees.", "Hava 25 derece.", None),
    ("spring", "ilkbahar", "I love spring.", "İlkbaharı çok severim.", None),
    ("summer", "yaz", "We go to Bodrum in summer.", "Yazın Bodrum'a gideriz.", "in summer"),
    ("autumn", "sonbahar", "The trees are beautiful in autumn.", "Sonbaharda ağaçlar çok güzel.", "Amerikan: fall."),
    ("winter", "kış", "It snows in winter.", "Kışın kar yağar.", None),
    ("umbrella", "şemsiye", "Have you got an umbrella?", "Şemsiyen var mı?", None),
    ("at the moment", "şu anda", "I'm busy at the moment.", "Şu anda meşgulüm.", "right now = tam şu an"),
    ("now", "şimdi", "What are you doing now?", "Şimdi ne yapıyorsun?", None),
    ("wait", "beklemek", "I'm waiting for the bus.", "Otobüs bekliyorum.", "wait for + kişi/şey"),
    ("sit", "oturmak", "She's sitting in the garden.", "Bahçede oturuyor.", "sit → sitting"),
    ("talk", "konuşmak", "Who are you talking to?", "Kiminle konuşuyorsun?", None),
    ("look at", "bakmak", "Look at the sky!", "Gökyüzüne bak!", None),
    ("feed", "beslemek, yem vermek", "The children are feeding the ducks.", "Çocuklar ördeklere yem veriyor.", None),
    ("photo", "fotoğraf", "In this photo, we're on holiday.", "Bu fotoğrafta tatildeyiz.", "in the photo (fotoğrafta)"),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Hava nasıl?", "Hava durumunu sorup söyleyebilirim.",
    {"kind": "text", "title": "Bugünün hava durumu", "body": "Good morning! Here's today's weather.\n\nIstanbul: It's cloudy and windy this morning, and it's raining in the afternoon. 14 degrees.\n\nAntalya: It's sunny and hot. Perfect for the beach! 30 degrees.\n\nErzurum: It's very cold. It's snowing in the mountains. Minus 5 degrees.\n\nAnkara: It's sunny but cold. 8 degrees.",
     "questions": [
        mc("Where is it snowing?", ["Ankara", "Erzurum", "Istanbul"], 1, "\"Erzurum: ... It's snowing in the mountains.\""),
        mc("What's the weather like in Antalya?", ["Sunny and hot", "Cloudy and windy", "Sunny but cold"], 0, "\"Antalya: It's sunny and hot.\""),
     ]},
    {"explanation": "**Hava sormak:** What's the weather like (today / in Antalya)?\n\n**Cevap her zaman It ile başlar:**\n\n- **It's** sunny / cloudy / windy / foggy. (sıfat)\n- **It's** hot / warm / cold. (sıfat)\n- **It's raining.** / **It's snowing.** (şu an oluyor)\n- **It's** twenty degrees. / **It's** minus five.\n\n**Mevsimler:** in spring, in summer, in autumn, in winter\n\n- It **rains** a lot in autumn. (genel)\n- It's **raining** now. (şu an)",
     "examples": [{"en": "It's sunny but windy.", "tr": "Hava güneşli ama rüzgarlı."},
                  {"en": "It's raining in London.", "tr": "Londra'da yağmur yağıyor."},
                  {"en": "It's very hot in summer.", "tr": "Yazın hava çok sıcak."}],
     "turkishNote": "Türkçede özne olmadan \"Yağmur yağıyor\" ya da \"Soğuk\" deriz. İngilizcede cümlenin bir öznesi olmalıdır, bu yüzden It kullanılır: It's cold (Is cold değil). \"Hava\" kelimesini çevirmeye gerek yok: \"The weather is cold\" da doğrudur ama \"It's cold\" çok daha yaygındır."},
    [
        match([("sunny", "güneşli"), ("cloudy", "bulutlu"), ("windy", "rüzgarlı"), ("cold", "soğuk"), ("warm", "ılık")], "Hava kelimelerini eşleştirin."),
        mc("Hangisi doğru?", ["Is cold today.", "It's cold today.", "Cold is today."], 1, "Özne gerekli: It's."),
        mc("\"What's the weather like?\" cevabı:", ["It's sunny.", "I like sun.", "Yes, it is."], 0, "It's + hava sıfatı."),
        gap("Take an umbrella. It's ___. (rain)", ["raining"], "Şu an → It's raining."),
        gap("It's very hot ___ summer.", ["in"], "Mevsimlerle in."),
        match([("spring", "ilkbahar"), ("summer", "yaz"), ("autumn", "sonbahar"), ("winter", "kış")], "Mevsimleri eşleştirin."),
        order(["the", "What's", "weather", "like", "today", "?"], "What's the weather like today?", "What's the weather like + zaman?", "Bugün hava nasıl?"),
        listen("In Izmir it's sunny and warm today, about twenty-two degrees.", "İzmir'de hava kaç derece?", ["12", "22", "32"], 1, "\"about twenty-two degrees\""),
        listen("Don't forget your coat. It's cloudy and very cold outside.", "Hava nasıl?", ["Güneşli ve sıcak", "Bulutlu ve çok soğuk", "Yağmurlu ve ılık"], 1, "\"cloudy and very cold\""),
        typ("İngilizce yazın: \"Kar yağıyor!\"", variants("It's snowing!", "It is snowing!"), "It's snowing!"),
    ],
    {"kind": "speaking", "task": speak("Bugün şehrinizde hava nasıl? Anlatın, sonra en sevdiğiniz mevsimi ve o mevsimde havanın nasıl olduğunu söyleyin.",
                                       "Today in Bursa it's cloudy and a little cold. It's about twelve degrees. My favourite season is spring. It's warm and sunny, and it doesn't rain a lot.",
                                       ["It's + hava sıfatı", "Derece söyledi", "in + mevsim doğru"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "Şu an ne yapıyorum?", "Şu an olan eylemleri present continuous ile anlatabilirim.",
    {"kind": "dialogue", "title": "Telefonda", "lines": [
        {"speaker": "Ayla", "text": "Hi, Mum! Where are you?"},
        {"speaker": "Mum", "text": "Hi, darling. I'm at the market. I'm buying some fruit."},
        {"speaker": "Ayla", "text": "Is Dad with you?"},
        {"speaker": "Mum", "text": "No, he's at home. He's cooking dinner."},
        {"speaker": "Ayla", "text": "Great! And Deniz?"},
        {"speaker": "Mum", "text": "Deniz is in the garden. The dog and Deniz are playing with a ball."}],
     "questions": [
        mc("What's Mum doing?", ["She's cooking.", "She's buying fruit.", "She's playing."], 1, "\"I'm buying some fruit.\""),
        mc("Where is Dad?", ["At the market", "At home", "In the garden"], 1, "\"he's at home. He's cooking dinner.\""),
     ]},
    {"explanation": "**Present continuous**, şu an (konuşma anında) olan eylemleri anlatır.\n\n**Yapı:** am / is / are + fiil**-ing**\n\n| | |\n|---|---|\n| I **am** (I'm) | read**ing** |\n| He / She / It **is** ('s) | read**ing** |\n| You / We / They **are** ('re) | read**ing** |\n\n**-ing yazımı** (9. ünitede gördük):\n\n- cook → cook**ing**\n- make → mak**ing** (-e düşer)\n- sit → si**tt**ing, swim → swi**mm**ing (ünsüz ikilenir)\n\nam / is / are **unutulmamalı**: ~~I cooking~~ → I**'m** cooking.",
     "examples": [{"en": "I'm waiting for the bus.", "tr": "Otobüs bekliyorum."},
                  {"en": "She's talking on the phone.", "tr": "Telefonda konuşuyor."},
                  {"en": "We're having lunch.", "tr": "Öğle yemeği yiyoruz."}],
     "turkishNote": "Türkçedeki \"-yor\" eki çoğu zaman present continuous'a denk gelir: okuyorum = I'm reading. Ama dikkat: Türkçede \"Her gün işe gidiyorum\" deriz; İngilizcede tekrar eden işler için present simple kullanılır: I go to work every day. Bunu 4. derste ayrıntılı göreceğiz."},
    [
        mc("Hangisi doğru?", ["I reading a book.", "I'm reading a book.", "I'm read a book."], 1, "am + -ing", {0: "am unutulmuş."}),
        mc("Hangisi doğru?", ["She are sleeping.", "She's sleeping.", "She sleeping."], 1, "she → is."),
        gap("They ___ watching a film. (are)", ["are", "'re"], "they → are."),
        gap("He's ___ dinner. (make)", ["making"], "make → making."),
        gap("The kids are ___ in the pool. (swim)", ["swimming"], "swim → swimming."),
        gap("I'm ___ for my friend. (wait)", ["waiting"], "wait for = beklemek."),
        order(["is", "The", "cat", "sleeping", "on", "the", "sofa"], "The cat is sleeping on the sofa.", "Özne + is + -ing + yer.", "Kedi kanepede uyuyor."),
        listen("Hi, I can't talk now. I'm driving. Call you later!", "Konuşan şu an ne yapıyor?", ["Yemek yapıyor", "Araba kullanıyor", "Yürüyor"], 1, "\"I'm driving.\""),
        typ("İngilizce yazın: \"Telefonda konuşuyor.\" (she)", variants("She's talking on the phone.", "She is talking on the phone.", "She's speaking on the phone.", "She is speaking on the phone."), "She's + talking on the phone."),
        mc("Fotoğrafta iki kişi kahve içiyor:", ["They're drinking coffee.", "They drink coffee.", "They drinking coffee."], 0, "Şu an / resimde → present continuous."),
    ],
    {"kind": "speaking", "task": speak("Şu an neredesiniz ve ne yapıyorsunuz? Sonra evinizde ya da yanınızdaki diğer iki kişinin şu an ne yaptığını tahmin edin.",
                                       "I'm at home. I'm sitting on the sofa and I'm practising English. My brother is playing a computer game, and my mum is talking on the phone.",
                                       ["am/is/are + -ing", "-ing yazımı doğru", "Farklı öznelerle kullandı"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "Ne yapıyorsun?", "Present continuous ile soru sorup olumsuz cümle kurabilirim.",
    {"kind": "dialogue", "title": "Mesajlaşma", "lines": [
        {"speaker": "Onur", "text": "Hey, are you watching the match?"},
        {"speaker": "Ece", "text": "No, I'm not. I'm studying for my exam."},
        {"speaker": "Onur", "text": "Oh, sorry! Is your sister watching it?"},
        {"speaker": "Ece", "text": "Yes, she is. She's screaming in the living room!"},
        {"speaker": "Onur", "text": "Ha ha! What's the score?"},
        {"speaker": "Ece", "text": "I don't know. I'm not listening. Good luck with the match!"}],
     "questions": [
        mc("Is Ece watching the match?", ["Yes, she is.", "No, she isn't."], 1, "\"No, I'm not. I'm studying.\""),
        mc("Who is watching the match?", ["Ece's sister", "Ece's dad", "Nobody"], 0, "\"Is your sister watching it? – Yes, she is.\""),
     ]},
    {"explanation": "**Olumsuz:** am / is / are + **not** + -ing\n\n- I**'m not** sleeping.\n- He **isn't** working today.\n- They **aren't** listening.\n\n**Soru:** Am / Is / Are + özne + -ing?\n\n- **Are you** watching TV? – Yes, I **am**. / No, I**'m not**.\n- **Is she** working? – Yes, she **is**. / No, she **isn't**.\n\n**Bilgi sorusu:** Soru kelimesi + am/is/are + özne + -ing?\n\n- **What are you doing**?\n- **Where is** he **going**?\n- **Who are** you **talking** to?",
     "examples": [{"en": "What are you doing? – I'm cooking.", "tr": "Ne yapıyorsun? – Yemek yapıyorum."},
                  {"en": "Is it raining? – No, it isn't.", "tr": "Yağmur yağıyor mu? – Hayır."},
                  {"en": "Where are you going?", "tr": "Nereye gidiyorsun?"}],
     "turkishNote": "Kısa cevapta Yes'ten sonra kısaltma yapılmaz: Yes, I am (Yes, I'm değil). Soru do/does ile kurulmaz: \"Do you watching?\" yanlıştır; \"Are you watching?\" doğrudur."},
    [
        mc("Hangisi doğru?", ["Do you sleeping?", "Are you sleeping?", "You are sleeping?"], 1, "Are + you + -ing?"),
        mc("\"Is your dad working today?\" (Hayır.)", ["No, he doesn't.", "No, he isn't.", "No, he not."], 1, "No, he isn't."),
        mc("\"Are you listening?\" (Evet.)", ["Yes, I'm.", "Yes, I am.", "Yes, I do."], 1, "Yes, I am (kısaltma yok)."),
        gap("I'm ___ watching TV. I'm reading. (not)", ["not"], "Olumsuz: I'm not."),
        gap("She ___ working today. It's Sunday. (değil)", ["isn't", "is not", "'s not"], "she → isn't."),
        gap("What ___ you doing?", ["are"], "you → are."),
        order(["are", "Where", "you", "going", "?"], "Where are you going?", "Soru kelimesi + are + özne + -ing?", "Nereye gidiyorsun?"),
        listen("Are the kids sleeping? – No, they aren't. They're playing in their room.", "Çocuklar ne yapıyor?", ["Uyuyorlar", "Odalarında oynuyorlar", "Ders çalışıyorlar"], 1, "\"They're playing in their room.\""),
        typ("Soru yapın: \"He is cooking.\"", variants("Is he cooking?"), "Is + he + cooking?"),
        typ("İngilizce yazın: \"Kiminle konuşuyorsun?\"", variants("Who are you talking to?", "Who are you talking with?", "Who are you speaking to?", "Who are you speaking with?"), "Who are you talking to?"),
    ],
    {"kind": "speaking", "task": speak("JAI'yi arıyorsunuz. Ona şu an ne yaptığını, nerede olduğunu ve kiminle olduğunu sorun (en az 3 soru). Bir sorusuna olumsuz cevap verin.",
                                       "Hi! What are you doing? Are you working? Where are you going? Who are you with? ... No, I'm not busy. I'm sitting in a café.",
                                       ["Am/Is/Are + özne + -ing? düzeni", "Kısa cevap doğru", "Olumsuz cümle doğru"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Her gün mü, şu an mı?", "Alışkanlıkları ve şu an olanları doğru zamanla ayırt edebilirim.",
    {"kind": "text", "title": "Bir pilotun kartpostalı", "body": "Hi Tom,\n\nI usually fly to European cities like Paris and Rome. I normally work four days a week and I get home in the evening.\n\nBut this week is different! I'm working in Japan. At the moment I'm sitting in a beautiful garden in Kyoto and I'm drinking green tea. It's warm and sunny.\n\nSee you next week!\nSevgi",
     "questions": [
        mc("Where does Sevgi usually fly?", ["To Japan", "To European cities", "To America"], 1, "\"I usually fly to European cities\""),
        mc("What is she doing at the moment?", ["Flying to Rome", "Drinking green tea in Kyoto", "Working in Paris"], 1, "\"At the moment I'm sitting in a beautiful garden in Kyoto and I'm drinking green tea.\""),
     ]},
    {"explanation": "| Present simple | Present continuous |\n|---|---|\n| Alışkanlık, rutin, genel gerçek | Şu an olan, geçici durum |\n| I **work** in an office. | I**'m working** at home **today**. |\n| She usually **drinks** coffee. | She**'s drinking** tea **now**. |\n| every day, usually, often, never, on Mondays | now, at the moment, today, this week, Look! |\n\n**Bazı fiiller -ing almaz** (durum fiilleri): like, love, hate, want, know, understand, need\n\n- I **want** a coffee now. (~~I'm wanting~~)\n- Do you **understand**? (~~Are you understanding~~)",
     "examples": [{"en": "He usually walks to work, but today he's taking a taxi.", "tr": "Genelde işe yürüyerek gider ama bugün taksiye biniyor."},
                  {"en": "It snows in winter. Look! It's snowing now.", "tr": "Kışın kar yağar. Bak! Şu an kar yağıyor."},
                  {"en": "I know the answer.", "tr": "Cevabı biliyorum."}],
     "turkishNote": "Türkçede \"biliyorum\", \"anlıyorum\", \"istiyorum\" -yor ekiyle söylenir; İngilizcede bunlar present simple'dır: I know, I understand, I want. Ayrıca Türkçede \"Her gün spor yapıyorum\" doğaldır; İngilizcede \"every day\" ile present simple kullanılır: I do sport every day."},
    [
        mc("I ___ to work every day.", ["drive", "am driving"], 0, "every day → present simple."),
        mc("Look! The baby ___.", ["walks", "is walking"], 1, "Look! → şu an."),
        mc("She usually ___ tea, but today she's drinking coffee.", ["drinks", "is drinking"], 0, "usually → present simple."),
        mc("Hangisi doğru?", ["I'm knowing the answer.", "I know the answer."], 1, "know -ing almaz."),
        mc("Hangisi doğru?", ["Are you understanding?", "Do you understand?"], 1, "understand -ing almaz."),
        gap("We ___ English at the moment. (study)", ["are studying", "'re studying"], "at the moment → continuous."),
        gap("My dad never ___ coffee. (drink)", ["drinks"], "never → present simple (he → -s)."),
        order(["is", "this", "week", "working", "from", "home", "He"], "He is working from home this week.", "Geçici durum → continuous.", "Bu hafta evden çalışıyor."),
        listen("I usually go to the gym after work, but today I'm staying at home. I'm very tired.", "Konuşan bugün ne yapıyor?", ["Spor salonuna gidiyor", "Evde kalıyor", "Çalışıyor"], 1, "\"today I'm staying at home\""),
        typ("İngilizce yazın: \"Şu an bir kahve istiyorum.\"", variants("I want a coffee now.", "I want a coffee at the moment.", "I want coffee now.", "Now I want a coffee."), "want -ing almaz: I want a coffee now."),
    ],
    {"kind": "writing", "task": write("Sevgi'nin kartpostalına benzer bir kartpostal yazın: normalde ne yaparsınız (2 cümle), bu hafta ya da şu an ne farklı (2–3 cümle), hava nasıl.",
                                      "Hi Elif,\nI usually get up at seven and go to the office by metro. I normally have lunch at my desk.\nBut this week I'm on holiday in Fethiye! At the moment I'm lying on the beach and I'm reading a book. It's hot and sunny.\nSee you soon!",
                                      ["Present simple + sıklık zarfı", "Present continuous + now/this week", "Durum fiilleri doğru", "Hava durumu"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Bir fotoğrafı anlatmak", "Bir fotoğrafta kimin ne yaptığını ve ne giydiğini anlatabilirim.",
    {"kind": "dialogue", "title": "Tatil fotoğrafları", "lines": [
        {"speaker": "Melis", "text": "Look at this photo. It's from our holiday in Kaş."},
        {"speaker": "Arda", "text": "Nice! Who's the man in the blue T-shirt?"},
        {"speaker": "Melis", "text": "That's my uncle. He's fishing. He loves fishing."},
        {"speaker": "Arda", "text": "And who are the girls on the left?"},
        {"speaker": "Melis", "text": "They're my cousins. They're eating ice cream and laughing."},
        {"speaker": "Arda", "text": "And where are you?"},
        {"speaker": "Melis", "text": "I'm not in the photo. I'm taking it!"}],
     "questions": [
        mc("What's Melis's uncle doing?", ["Swimming", "Fishing", "Eating ice cream"], 1, "\"He's fishing.\""),
        mc("Why isn't Melis in the photo?", ["She's swimming.", "She's taking the photo.", "She's at home."], 1, "\"I'm taking it!\""),
     ]},
    {"explanation": "Bir fotoğrafı anlatırken **present continuous** kullanırız.\n\n**Yer:** in the photo, on the left, on the right, in the middle, at the front, at the back\n\n**Kişiyi tanımlamak:** the man **in** the blue T-shirt, the woman **with** long hair, the girl **on** the left\n\n**Kalıplar:**\n\n- **In this photo**, we're at the beach.\n- **Who's** the woman **in** the red dress?\n- **There's** a boy **on the right**. He's playing football.\n- She**'s wearing** a hat.",
     "examples": [{"en": "In the middle, a man is selling simit.", "tr": "Ortada bir adam simit satıyor."},
                  {"en": "The woman with the dog is running.", "tr": "Köpekli kadın koşuyor."},
                  {"en": "The children at the front are smiling.", "tr": "Öndeki çocuklar gülümsüyor."}],
     "turkishNote": "Türkçede \"mavi tişörtlü adam\" deriz; İngilizcede tanımlayıcı ifade isimden sonra gelir: the man in the blue T-shirt. \"Fotoğrafta\" = in the photo (on the photo değil)."},
    [
        match([("on the left", "solda"), ("on the right", "sağda"), ("in the middle", "ortada"), ("at the back", "arkada")], "Yer ifadelerini eşleştirin."),
        mc("\"Mavi tişörtlü adam\"", ["the blue T-shirt man", "the man in the blue T-shirt", "the man with blue T-shirt in"], 1, "isim + in + kıyafet."),
        mc("Hangisi doğru?", ["on the photo", "in the photo"], 1, "Fotoğrafta = in the photo."),
        gap("The girl ___ long hair is reading.", ["with"], "Fiziksel özellik → with."),
        gap("Who's the woman ___ the green dress?", ["in"], "Kıyafet → in."),
        gap("In this photo, my parents ___ dancing.", ["are", "'re"], "parents → are."),
        order(["wearing", "is", "She", "a", "big", "hat"], "She is wearing a big hat.", "Özne + is + wearing + kıyafet.", "Büyük bir şapka takıyor."),
        listen("In this photo, my brother is on the right. He's wearing a yellow jacket and he's holding a cat.", "Kardeşi ne tutuyor?", ["Bir köpek", "Bir kedi", "Bir top"], 1, "\"he's holding a cat\""),
        typ("İngilizce yazın: \"Bu fotoğrafta tatildeyiz.\"", variants("In this photo, we're on holiday.", "In this photo we're on holiday.", "In this photo, we are on holiday.", "In this photo we are on holiday.", "We're on holiday in this photo."), "In this photo, we're on holiday."),
        mc("Fotoğraftaki kişiyi sormak:", ["Who's the man on the left?", "What's the man on the left?", "Who the man on the left?"], 0, "Kişi → Who's."),
    ],
    {"kind": "speaking", "task": speak("Telefonunuzdan sevdiğiniz bir fotoğrafı seçin ve JAI'ye anlatın: nerede, kimler var, ne giyiyorlar, ne yapıyorlar, hava nasıl.",
                                       "In this photo, we're in my grandmother's garden. My grandma is in the middle. She's wearing a white dress and she's smiling. On the left, my cousins are playing football. It's sunny and hot.",
                                       ["Present continuous doğru", "Yer ifadeleri", "in/with ile kişi tanımı", "Hava durumu"])},
)

u.test([
    mc("Hangisi doğru?", ["Is hot today.", "It's hot today."], 1, "It's + hava."),
    gap("Take your umbrella. It's ___. (rain)", ["raining"], "It's raining."),
    mc("We go skiing ___ winter.", ["in", "on", "at"], 0, "in winter"),
    mc("Hangisi doğru?", ["She cooking now.", "She's cooking now."], 1, "is + -ing"),
    gap("They're ___ in the sea. (swim)", ["swimming"], "swim → swimming"),
    mc("\"Are you working?\" (Hayır.)", ["No, I don't.", "No, I'm not.", "No, I amn't."], 1, "No, I'm not."),
    mc("\"Is it snowing?\" (Evet.)", ["Yes, it is.", "Yes, it's.", "Yes, it does."], 0, "Yes, it is."),
    gap("What ___ you doing?", ["are"], "are"),
    mc("I usually ___ by bus, but today I'm walking.", ["go", "am going"], 0, "usually → present simple."),
    mc("Look! The children ___ the ducks.", ["feed", "are feeding"], 1, "Look! → continuous."),
    mc("Hangisi doğru?", ["I'm wanting a tea.", "I want a tea."], 1, "want -ing almaz."),
    mc("\"Siyah ceketli kadın\"", ["the woman in the black jacket", "the black jacket woman"], 0, "isim + in + kıyafet."),
    listen("What's the weather like in Trabzon? – It's raining and it's quite cold, about ten degrees.", "Trabzon'da hava nasıl?", ["Güneşli ve sıcak", "Yağmurlu ve soğukça", "Karlı"], 1, "\"It's raining and it's quite cold\""),
    order(["is", "Who", "she", "talking", "to", "?"], "Who is she talking to?", "Soru kelimesi + is + özne + -ing + to?", "Kiminle konuşuyor?"),
    write("Pencerenizden dışarı bakın. Havayı ve gördüğünüz 3 kişinin ya da hayvanın ne yaptığını anlatın. Sonra bu insanların genelde ne yaptığını tahmin edin (5–6 cümle).",
          "It's cloudy and windy today. A woman is walking her dog. Two boys are playing football in the street. A man is waiting for the bus. He probably goes to work by bus every day.",
          ["Hava durumu doğru", "Present continuous doğru", "Present simple ile karşılaştırma", "Yer ifadeleri"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

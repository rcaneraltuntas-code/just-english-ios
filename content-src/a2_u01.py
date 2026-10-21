"""A2 Ünite 1: Hayat hikâyeleri."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("A2", 1, "Hayat hikâyeleri", "Life Stories",
         "Kendi hayatımın ve tanınmış birinin hayatının önemli olaylarını sırayla anlatabilir, başkalarına geçmişleri hakkında soru sorabilirim.",
         ["past simple: düzensiz fiiller", "past simple: Did ...? ve Wh- soruları", "was / were born", "özne soruları: Who wrote ...?", "zaman ifadeleri: in 1998, when I was ten, later, at the age of"],
         ["yaşam olayları", "biyografi dili", "eğitim ve iş"],
         {"title": "Hayat çizgisi", "durationMinutes": 45,
          "goal": "Her öğrenci kendi hayatından 6 olayı (biri uydurma) bir zaman çizgisine yazar. Eşi Did you...? / When did you...? sorularıyla her olayı sorar ve uydurma olanı bulmaya çalışır. Sonra öğrenciler eşlerinin hayat hikâyesini sınıfa üçüncü tekil kişiyle anlatır."})

u.vocab([
    ("be born", "doğmak", "I was born in Trabzon in 1995.", "1995'te Trabzon'da doğdum.", "Her zaman was/were born: I born değil."),
    ("grow up", "büyümek (çocukluğunu geçirmek)", "She grew up in a small village.", "Küçük bir köyde büyüdü.", "Düzensiz: grow → grew."),
    ("move", "taşınmak", "We moved to Istanbul when I was ten.", "On yaşındayken İstanbul'a taşındık.", "move to + yer"),
    ("leave school", "okulu bitirmek / bırakmak", "He left school at sixteen.", "On altı yaşında okulu bıraktı.", "leave → left"),
    ("go to university", "üniversiteye gitmek", "I went to university in Ankara.", "Ankara'da üniversiteye gittim.", None),
    ("graduate", "mezun olmak", "She graduated from Boğaziçi in 2015.", "2015'te Boğaziçi'nden mezun oldu.", "graduate from + okul"),
    ("get a job", "iş bulmak", "I got my first job at nineteen.", "İlk işimi on dokuz yaşında buldum.", "get → got"),
    ("meet", "tanışmak, buluşmak", "My parents met at work.", "Annemle babam iş yerinde tanıştı.", "meet → met"),
    ("fall in love", "aşık olmak", "They fell in love in Paris.", "Paris'te birbirlerine aşık oldular.", "fall → fell"),
    ("get married", "evlenmek", "We got married in 2020.", "2020'de evlendik.", "get married to + kişi (with değil)"),
    ("have a baby", "bebek sahibi olmak", "They had a baby last year.", "Geçen yıl bebekleri oldu.", "have → had"),
    ("become", "olmak (bir şey haline gelmek)", "She became a famous writer.", "Ünlü bir yazar oldu.", "become → became"),
    ("win", "kazanmak", "He won a gold medal.", "Altın madalya kazandı.", "win → won"),
    ("write", "yazmak", "Orhan Pamuk wrote 'Snow'.", "Orhan Pamuk 'Kar'ı yazdı.", "write → wrote"),
    ("begin", "başlamak", "The war began in 1914.", "Savaş 1914'te başladı.", "begin → began"),
    ("die", "ölmek", "Atatürk died in 1938.", "Atatürk 1938'de öldü.", "die → died (düzenli)"),
    ("retire", "emekli olmak", "My dad retired last year.", "Babam geçen yıl emekli oldu.", None),
    ("childhood", "çocukluk", "I had a happy childhood.", "Mutlu bir çocukluğum oldu.", None),
    ("famous", "ünlü", "She's famous all over the world.", "Tüm dünyada ünlü.", None),
    ("century", "yüzyıl", "He lived in the 16th century.", "16. yüzyılda yaşadı.", None),
    ("later", "sonra, daha sonra", "Two years later, they moved to London.", "İki yıl sonra Londra'ya taşındılar.", "süre + later"),
    ("at the age of", "... yaşında", "Mozart wrote music at the age of five.", "Mozart beş yaşında müzik yazdı.", None),
    ("when I was ...", "... iken / ... yaşındayken", "When I was a child, I lived in Izmir.", "Çocukken İzmir'de yaşıyordum.", None),
    ("biography", "biyografi", "I'm reading a biography of Atatürk.", "Bir Atatürk biyografisi okuyorum.", None),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Düzensiz fiiller (1)", "En sık kullanılan düzensiz fiillerle geçmişi anlatabilirim.",
    {"kind": "text", "title": "Bir ödülün hikâyesi", "body": "Aylin Kaya was born in Kars in 1990. Her family didn't have much money, but her mother gave her a camera for her tenth birthday.\n\nAylin took photos of everything: animals, people, the snow. At eighteen she went to Istanbul to study art. She didn't know anybody there, but she made friends quickly.\n\nIn 2019 she saw a competition online. She sent three photos of her village. Six months later she won first prize. Today her photos are in museums in Paris and New York.",
     "questions": [
        mc("Who gave Aylin her first camera?", ["Her father", "Her mother", "Her teacher"], 1, "\"her mother gave her a camera\""),
        mc("What did she send to the competition?", ["Photos of Istanbul", "Photos of her village", "A painting"], 1, "\"She sent three photos of her village.\""),
     ]},
    {"explanation": "A1'de düzenli fiilleri (-ed) ve iki düzensiz fiili (went, had) gördük. İngilizcede yaklaşık 100 sık kullanılan düzensiz fiil vardır ve ezberlenmeleri gerekir. Bu ünitede en sık kullanılan 20'siyle başlıyoruz.\n\n| Fiil | Geçmiş | | Fiil | Geçmiş |\n|---|---|---|---|---|\n| go | **went** | | see | **saw** |\n| have | **had** | | take | **took** |\n| get | **got** | | give | **gave** |\n| make | **made** | | send | **sent** |\n| do | **did** | | know | **knew** |\n| come | **came** | | think | **thought** |\n\nDüzensiz fiiller de **her özne için aynıdır**: I went, she went, they went.\n\n**Olumsuz ve soruda** yine did + yalın fiil: She **didn't know** anybody. / **Did** you **see** it?",
     "examples": [{"en": "We took a taxi to the airport.", "tr": "Havalimanına taksiyle gittik."},
                  {"en": "I thought it was a good idea.", "tr": "İyi bir fikir olduğunu düşündüm."},
                  {"en": "She didn't come to the party.", "tr": "Partiye gelmedi."}],
     "turkishNote": "Düzensiz fiilleri ezberlemenin en iyi yolu onları anlamlı cümlelerle tekrar etmektir. Uygulamadaki kelime kartları her fiili bir örnek cümleyle verir; aralıklı tekrar sistemi unutmaya başladığınız fiilleri size tekrar gösterir. \"didn't went\" A2'de bile çok sık yapılan bir hatadır: did geçmişi zaten gösterir, fiil yalın kalır."},
    [
        match([("go", "went"), ("see", "saw"), ("take", "took"), ("give", "gave"), ("think", "thought")], "Fiillerin geçmiş hallerini eşleştirin."),
        gap("I ___ my keys at home this morning. (leave)", ["left"], "leave → left."),
        gap("She ___ a lovely cake for my birthday. (make)", ["made"], "make → made."),
        gap("We ___ the Eiffel Tower last summer. (see)", ["saw"], "see → saw."),
        gap("He ___ home at midnight. (come)", ["came"], "come → came."),
        mc("Hangisi doğru?", ["She didn't knew the answer.", "She didn't know the answer.", "She not knew the answer."], 1, "didn't + yalın fiil."),
        mc("\"get\" fiilinin geçmiş hali:", ["getted", "got", "gotten"], 1, "get → got. (gotten past simple değildir.)"),
        listen("Last year I got a new job, so I sent my old boss a thank-you card. He gave me some great advice.", "Konuşan eski patronuna ne gönderdi?", ["Hediye", "Teşekkür kartı", "E-posta"], 1, "\"I sent my old boss a thank-you card\""),
        order(["took", "She", "photos", "of", "everything"], "She took photos of everything.", "Özne + geçmiş fiil + nesne.", "Her şeyin fotoğrafını çekti."),
        typ("İngilizce yazın: \"İyi bir fikir olduğunu düşündüm.\"", variants("I thought it was a good idea.", "I thought that it was a good idea."), "think → thought."),
    ],
    {"kind": "speaking", "task": speak("Hayatınızdaki önemli bir günü anlatın (ilk iş günü, mezuniyet, bir yolculuk...). En az 5 düzensiz fiil kullanın.",
                                       "My first day at university was in September 2012. I got up very early and took the bus. I didn't know anybody, but I met a girl in the café. We had lunch together and she became my best friend.",
                                       ["Düzensiz fiiller doğru", "didn't + yalın fiil", "Olaylar sıralı"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "Düzensiz fiiller (2)", "Yaşam olaylarını düzensiz fiillerle anlatabilirim.",
    {"kind": "dialogue", "title": "Büyükannemin hikâyesi", "lines": [
        {"speaker": "Elif", "text": "Grandma, how did you and Grandpa meet?"},
        {"speaker": "Grandma", "text": "We met at a wedding in 1968. He wore a terrible brown suit!"},
        {"speaker": "Elif", "text": "Ha ha! And did you fall in love immediately?"},
        {"speaker": "Grandma", "text": "No! I thought he was boring. But he wrote me a letter every week."},
        {"speaker": "Elif", "text": "That's so romantic! When did you get married?"},
        {"speaker": "Grandma", "text": "Two years later. Then we bought a little house and your father was born in 1972."}],
     "questions": [
        mc("Where did Elif's grandparents meet?", ["At work", "At a wedding", "At school"], 1, "\"We met at a wedding\""),
        mc("When did they get married?", ["1968", "1970", "1972"], 1, "\"Two years later\" → 1968 + 2 = 1970."),
     ]},
    {"explanation": "**Yaşam olaylarında sık kullanılan düzensiz fiiller:**\n\n| Fiil | Geçmiş | | Fiil | Geçmiş |\n|---|---|---|---|---|\n| meet | **met** | | grow up | **grew up** |\n| become | **became** | | leave | **left** |\n| buy | **bought** | | begin | **began** |\n| write | **wrote** | | win | **won** |\n| fall | **fell** | | wear | **wore** |\n| find | **found** | | sell | **sold** |\n\n**Gruplar halinde öğrenmek kolaylaştırır:**\n\n- -ought / -aught: buy → bought, think → thought, bring → brought, teach → taught\n- i → a: begin → began, swim → swam, sing → sang, drink → drank\n- değişmeyenler: put → put, cut → cut, cost → cost",
     "examples": [{"en": "They bought a flat in Kadıköy.", "tr": "Kadıköy'de bir daire aldılar."},
                  {"en": "He became a doctor in 2010.", "tr": "2010'da doktor oldu."},
                  {"en": "The concert began at eight.", "tr": "Konser sekizde başladı."}],
     "turkishNote": "Türkçede \"olmak\" fiili çok geniş kullanılır; İngilizcede karşılığı duruma göre değişir: doktor oldu = became a doctor, evlendi = got married, bebeği oldu = had a baby. \"Evlendi\" için \"married with\" değil, \"got married to\" kullanılır."},
    [
        match([("buy", "bought"), ("meet", "met"), ("become", "became"), ("write", "wrote"), ("begin", "began")], "Fiilleri eşleştirin."),
        gap("My parents ___ at university. (meet)", ["met"], "meet → met."),
        gap("She ___ a famous singer at 20. (become)", ["became"], "become → became."),
        gap("We ___ a new car last month. (buy)", ["bought"], "buy → bought."),
        gap("I ___ up in a small town near Bursa. (grow)", ["grew"], "grow → grew."),
        mc("Hangisi doğru?", ["She got married with a pilot.", "She got married to a pilot.", "She married with a pilot."], 1, "get married to + kişi."),
        mc("\"teach\" fiilinin geçmiş hali:", ["teached", "taught", "tought"], 1, "teach → taught (-aught grubu)."),
        listen("My uncle left school at sixteen and found a job in a factory. Later he bought the factory!", "Amca sonunda ne yaptı?", ["Fabrikadan ayrıldı", "Fabrikayı satın aldı", "Okula döndü"], 1, "\"Later he bought the factory!\""),
        order(["fell", "They", "in", "love", "in", "Paris"], "They fell in love in Paris.", "fall → fell + in love.", "Paris'te aşık oldular."),
        typ("İngilizce yazın: \"2015'te evlendik.\"", variants("We got married in 2015.", "In 2015 we got married.", "In 2015, we got married."), "got married + in 2015."),
    ],
    {"kind": "speaking", "task": speak("Ailenizden yaşlı bir kişinin (büyükanne, büyükbaba, anne, baba) hayat hikâyesini 6 cümleyle anlatın.",
                                       "My grandfather was born in Rize in 1945. He grew up on a tea farm. He left school at fourteen and became a fisherman. He met my grandmother in 1965 and they got married a year later. They had five children.",
                                       ["Yaşam olayı kelimeleri", "Düzensiz fiiller doğru", "Yıllar ve zaman ifadeleri"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "Geçmişi sormak", "Birine hayatı hakkında Did ...? ve Wh- soruları sorabilirim.",
    {"kind": "dialogue", "title": "Radyo röportajı", "lines": [
        {"speaker": "Host", "text": "Welcome, Chef Murat. Where were you born?"},
        {"speaker": "Murat", "text": "I was born in Gaziantep, but I grew up in Mersin."},
        {"speaker": "Host", "text": "When did you start cooking?"},
        {"speaker": "Murat", "text": "When I was seven. My grandmother taught me."},
        {"speaker": "Host", "text": "Did you go to a cooking school?"},
        {"speaker": "Murat", "text": "No, I didn't. I learned in restaurant kitchens. I washed dishes for two years!"},
        {"speaker": "Host", "text": "Why did you open your restaurant in London?"},
        {"speaker": "Murat", "text": "Because I wanted to show Turkish food to the world."}],
     "questions": [
        mc("Who taught Murat to cook?", ["His mother", "His grandmother", "A teacher"], 1, "\"My grandmother taught me.\""),
        mc("Did Murat go to a cooking school?", ["Yes, he did.", "No, he didn't."], 1, "\"No, I didn't. I learned in restaurant kitchens.\""),
     ]},
    {"explanation": "**Evet/hayır sorusu:** Did + özne + yalın fiil?\n\n- **Did** you **grow up** here? – Yes, I **did**. / No, I **didn't**.\n\n**Bilgi sorusu:** Soru kelimesi + did + özne + yalın fiil?\n\n| Soru kelimesi | Örnek |\n|---|---|\n| Where | Where **did** you **go** to school? |\n| When | When **did** she **move** to Ankara? |\n| Why | Why **did** they **leave**? |\n| How | How **did** you **meet**? |\n| What | What **did** you **study**? |\n| How long | How long **did** you **live** there? |\n\n**Doğum:** be born bir be yapısıdır, did kullanılmaz:\n\n- **Where were** you **born**? (~~Where did you born?~~)\n- **When was** he **born**?",
     "examples": [{"en": "What did you study at university?", "tr": "Üniversitede ne okudun?"},
                  {"en": "How long did you live in Germany?", "tr": "Almanya'da ne kadar yaşadın?"},
                  {"en": "When was your mother born?", "tr": "Annen ne zaman doğdu?"}],
     "turkishNote": "Türkçede \"doğdum\" etken bir fiil gibidir; İngilizcede \"be born\" edilgendir: I was born. Bu yüzden \"Where did you born?\" yanlıştır, \"Where were you born?\" doğrudur. Ayrıca \"üniversitede ne okudun?\" sorusunda read değil study kullanılır."},
    [
        mc("Hangisi doğru?", ["Where did you born?", "Where were you born?", "Where you were born?"], 1, "be born → were you born?"),
        mc("Hangisi doğru?", ["When did you moved here?", "When did you move here?", "When you moved here?"], 1, "did + yalın fiil."),
        gap("What ___ you study at university?", ["did"], "Geçmiş bilgi sorusu → did."),
        gap("When ___ your father born?", ["was"], "he → was born."),
        gap("How did you ___ your wife? (meet)", ["meet"], "did + yalın fiil."),
        mc("\"Did you grow up in Izmir?\" (Hayır.)", ["No, I didn't.", "No, I wasn't.", "No, I don't."], 0, "Did → No, I didn't."),
        order(["long", "How", "did", "you", "live", "in", "Germany", "?"], "How long did you live in Germany?", "How long + did + özne + yalın fiil?", "Almanya'da ne kadar yaşadın?"),
        listen("Why did you leave your job? – Because I wanted to start my own company.", "Konuşan işini neden bıraktı?", ["Maaşı düşüktü", "Kendi şirketini kurmak istedi", "Taşındı"], 1, "\"Because I wanted to start my own company.\""),
        typ("Cümle için soru yazın: \"She moved to London in 2018.\" (When?)", variants("When did she move to London?"), "When + did + she + move + to London?"),
        typ("İngilizce yazın: \"Üniversitede ne okudun?\"", variants("What did you study at university?", "What did you study at uni?"), "What did you study + at university?"),
    ],
    {"kind": "speaking", "task": speak("JAI ünlü bir kişiyi canlandıracak. Ona hayatı hakkında en az 6 soru sorun: doğum yeri, çocukluk, eğitim, kariyer, ve en az bir Why sorusu.",
                                       "Where were you born? Where did you grow up? Did you go to university? What did you study? When did you become famous? Why did you choose this job?",
                                       ["was/were born doğru", "did + yalın fiil düzeni", "Farklı soru kelimeleri kullandı"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Kim yaptı?", "Özne soruları ile nesne sorularını ayırt edebilirim.",
    {"kind": "text", "title": "Bilgi yarışması", "body": "QUIZ NIGHT – Round 3: Famous people\n\n1. Who painted the Mona Lisa?\n2. Who discovered penicillin?\n3. What happened in Turkey in 1923?\n4. Who wrote 'The Black Book'?\n5. Who did Mimar Sinan build the Süleymaniye Mosque for?\n\nAnswers: 1. Leonardo da Vinci painted it. 2. Alexander Fleming discovered it in 1928. 3. The Republic of Turkey began. 4. Orhan Pamuk wrote it. 5. He built it for Sultan Süleyman.",
     "questions": [
        mc("Who discovered penicillin?", ["Leonardo da Vinci", "Alexander Fleming", "Orhan Pamuk"], 1, "\"Alexander Fleming discovered it in 1928.\""),
        mc("What happened in Turkey in 1923?", ["The Republic began.", "A mosque was built.", "A book was written."], 0, "\"The Republic of Turkey began.\""),
     ]},
    {"explanation": "**Who** ve **What** iki farklı soru sorabilir:\n\n**1. Özne sorusu** (yapanı soruyoruz): did **kullanılmaz**, fiil geçmiş halde kalır.\n\n- **Who wrote** 'Snow'? – Orhan Pamuk wrote it.\n- **What happened**? – I lost my wallet.\n\n**2. Nesne sorusu** (eylemin yapıldığı kişiyi/şeyi soruyoruz): did **kullanılır**.\n\n- **Who did** you **see** at the party? – I saw Ayşe.\n- **What did** she **buy**? – She bought a coat.\n\n**Karşılaştırın:**\n\n| Özne sorusu | Nesne sorusu |\n|---|---|\n| Who called you? (Seni kim aradı?) | Who did you call? (Sen kimi aradın?) |\n| Who met Ali? (Ali'yle kim buluştu?) | Who did Ali meet? (Ali kiminle buluştu?) |",
     "examples": [{"en": "Who invented the telephone?", "tr": "Telefonu kim icat etti?"},
                  {"en": "What happened at the meeting?", "tr": "Toplantıda ne oldu?"},
                  {"en": "Who did you invite?", "tr": "Kimi davet ettin?"}],
     "turkishNote": "Türkçede \"kim\" ve \"kimi\" farklı kelimelerdir, bu yüzden fark kolay anlaşılır: \"Kim aradı?\" = Who called? (özne), \"Kimi aradın?\" = Who did you call? (nesne). \"What did happen?\" yanlıştır; happen her zaman özne sorusudur: What happened?"},
    [
        mc("\"Seni kim aradı?\"", ["Who called you?", "Who did you call?", "Who did call you?"], 0, "Özne sorusu → did yok."),
        mc("\"Sen kimi aradın?\"", ["Who called you?", "Who did you call?"], 1, "Nesne sorusu → did var."),
        mc("Hangisi doğru?", ["What did happen?", "What happened?", "What did happened?"], 1, "happen → özne sorusu."),
        gap("Who ___ the Mona Lisa? (paint)", ["painted"], "Özne sorusu → painted."),
        gap("What ___ you buy at the market?", ["did"], "Nesne sorusu → did."),
        mc("\"Who won the match?\" cevabı:", ["Galatasaray won.", "Galatasaray did win it the match.", "I won Galatasaray."], 0, "Özne sorusuna cevap: kim kazandı."),
        order(["did", "Who", "you", "meet", "at", "the", "party", "?"], "Who did you meet at the party?", "Nesne sorusu: Who + did + özne + fiil?", "Partide kiminle tanıştın?"),
        listen("Who broke the window? – I don't know. But I know who did it... the cat!", "Pencereyi kim kırdı?", ["Çocuk", "Kedi", "Konuşan"], 1, "\"the cat!\""),
        typ("Özne sorusu yazın: \"Alexander Graham Bell invented the telephone.\" (Who?)", variants("Who invented the telephone?"), "Who + invented + the telephone?"),
        typ("Nesne sorusu yazın: \"Mert invited Leyla.\" (Who? → Leyla'yı soruyoruz)", variants("Who did Mert invite?"), "Who + did + Mert + invite?"),
    ],
    {"kind": "writing", "task": write("Arkadaşlarınız için 5 soruluk bir bilgi yarışması yazın: en az 3 özne sorusu (Who wrote/invented...?) ve 2 nesne sorusu (What did...?). Cevapları da yazın.",
                                      "1. Who wrote 'Romeo and Juliet'? – Shakespeare wrote it.\n2. Who invented the light bulb? – Edison invented it.\n3. What happened in 1969? – People walked on the moon.\n4. What did Marie Curie discover? – She discovered radium.\n5. Which city did Mehmed II conquer in 1453? – He conquered Istanbul.",
                                      ["Özne sorularında did yok", "Nesne sorularında did + yalın fiil", "Cevaplarda doğru geçmiş fiiller"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Bir hayat hikâyesi", "Bir hayat hikâyesini zaman ifadeleriyle sıralı ve akıcı bir şekilde anlatabilirim.",
    {"kind": "text", "title": "Kısa biyografi: Sabiha Gökçen", "body": "Sabiha Gökçen was born in Bursa in 1913. When she was twelve, she met Atatürk and he adopted her.\n\nIn 1935 she went to a flying school and fell in love with planes. Only a year later, at the age of 23, she became the first Turkish woman pilot. In 1937 she flew military planes, and she became the world's first woman combat pilot.\n\nLater, she flew to many Balkan countries. She taught young pilots for many years. She died in 2001, but today one of Istanbul's airports has her name.",
     "questions": [
        mc("How old was Sabiha Gökçen when she became a pilot?", ["Twelve", "Twenty-three", "Thirty-five"], 1, "\"at the age of 23, she became the first Turkish woman pilot\""),
        mc("What has her name today?", ["A school", "An airport", "A plane"], 1, "\"one of Istanbul's airports has her name\""),
     ]},
    {"explanation": "Bir hayat hikâyesini akıcı anlatmak için zaman ifadeleri kullanırız:\n\n| İfade | Örnek |\n|---|---|\n| in + yıl | She was born **in** 1913. |\n| on + tarih | He died **on** 10 November 1938. |\n| when + I/she was ... | **When she was** twelve, she met Atatürk. |\n| at the age of ... | **At the age of** 23, she became a pilot. |\n| ... later | Two years **later**, they got married. |\n| after + isim / -ing | **After** university, he moved to London. |\n| then / after that | **Then** she started teaching. |\n| from ... to ... | He lived in Paris **from** 1990 **to** 2005. |\n\n**Yıl okumak:** 1913 = nineteen thirteen, 2001 = two thousand and one, 2015 = twenty fifteen",
     "examples": [{"en": "When I was a teenager, I wanted to be a pilot.", "tr": "Ergenken pilot olmak istiyordum."},
                  {"en": "After school, she worked in a bank.", "tr": "Okuldan sonra bir bankada çalıştı."},
                  {"en": "A year later, he won the Nobel Prize.", "tr": "Bir yıl sonra Nobel ödülü kazandı."}],
     "turkishNote": "Türkçede \"iki yıl sonra\" deriz; İngilizcede geçmişi anlatırken \"two years later\" ya da \"after two years\" denir. \"on iki yaşındayken\" = when she was twelve (when she was twelve years old da olur)."},
    [
        mc("She was born ___ 1998.", ["in", "on", "at"], 0, "Yıl → in."),
        mc("He died ___ 3 March 2010.", ["in", "on", "at"], 1, "Tarih → on."),
        mc("___ the age of 18, she left home.", ["In", "On", "At"], 2, "at the age of."),
        gap("Three years ___, they had a baby.", ["later"], "süre + later."),
        gap("___ I was a child, I lived in Konya.", ["When"], "When I was a child."),
        gap("He lived in Rome ___ 2001 to 2008.", ["from"], "from ... to ..."),
        mc("2007 nasıl okunur?", ["twenty seven", "two thousand and seven", "two hundred seven"], 1, "two thousand and seven."),
        listen("After university, I worked in a hotel in Antalya. Two years later, I moved to Istanbul and opened my own café.", "Konuşan İstanbul'a ne zaman taşındı?", ["Üniversiteden hemen sonra", "Otelde iki yıl çalıştıktan sonra", "Antalya'ya gitmeden önce"], 1, "\"Two years later, I moved to Istanbul\""),
        order(["the", "At", "age", "of", "twenty", "she", "became", "a", "teacher"], "At the age of twenty she became a teacher.", "At the age of + yaş + cümle.", "Yirmi yaşında öğretmen oldu."),
        typ("İngilizce yazın: \"Çocukken İzmir'de yaşıyordum.\"", variants("When I was a child, I lived in Izmir.", "When I was a child I lived in Izmir.", "I lived in Izmir when I was a child.", "When I was a kid, I lived in Izmir."), "When I was a child, I lived in Izmir."),
    ],
    {"kind": "writing", "task": write("Kendi hayat hikâyenizi ya da hayran olduğunuz birinin kısa biyografisini yazın (80–100 kelime). En az 4 farklı zaman ifadesi ve 6 düzensiz fiil kullanın.",
                                      "I was born in Samsun in 1994. When I was eight, my family moved to Ankara because my father got a new job there. I grew up in Çankaya and went to a great school. At the age of eighteen, I began university in Izmir and studied engineering. After university, I found a job in a big company. In 2021 I met my wife, and two years later we got married. Last year we bought our first flat.",
                                      ["Zaman ifadeleri doğru (in/on/at, when, later, after)", "Düzensiz fiiller doğru", "Olaylar mantıklı sırada", "Akıcı paragraflar"])},
)

u.test([
    gap("She ___ a letter to her grandma. (write)", ["wrote"], "write → wrote"),
    gap("We ___ a lot of photos in Rome. (take)", ["took"], "take → took"),
    gap("They ___ a house by the sea. (buy)", ["bought"], "buy → bought"),
    mc("Hangisi doğru?", ["I didn't saw him.", "I didn't see him."], 1, "didn't + yalın fiil."),
    mc("Hangisi doğru?", ["Where did you born?", "Where were you born?"], 1, "were you born"),
    mc("Hangisi doğru?", ["She got married with Ali.", "She got married to Ali."], 1, "get married to"),
    gap("How did you ___ your husband? (meet)", ["meet"], "did + yalın fiil"),
    mc("\"Seni kim aradı?\"", ["Who did call you?", "Who called you?", "Who did you call?"], 1, "Özne sorusu."),
    mc("Hangisi doğru?", ["What did happen?", "What happened?"], 1, "What happened?"),
    mc("He was born ___ 1985.", ["in", "on", "at"], 0, "in + yıl"),
    gap("Two years ___, she became a manager.", ["later"], "later"),
    order(["did", "What", "you", "study", "at", "university", "?"], "What did you study at university?", "What + did + you + study?", "Üniversitede ne okudun?"),
    listen("My mother grew up in a village. She left school at fifteen, but later she went back and became a teacher at forty.", "Anne kaç yaşında öğretmen oldu?", ["15", "30", "40"], 2, "\"became a teacher at forty\""),
    typ("İngilizce yazın: \"Telefonu kim icat etti?\"", variants("Who invented the telephone?", "Who invented the phone?"), "Özne sorusu: Who invented ...?"),
    write("Bir arkadaşınızın ya da aile üyenizin hayatını anlatan 6–8 cümlelik bir metin yazın. Doğum, çocukluk, eğitim, iş ve önemli bir olay olsun.",
          "My best friend Selin was born in Eskişehir in 1996. She grew up with three brothers. When she was ten, she won a painting competition. She went to university in Istanbul and studied architecture. After university, she got a job in Berlin. Two years later she started her own company. Last summer she came back to Turkey and opened an office in Izmir.",
          ["Düzensiz fiiller doğru", "Zaman ifadeleri çeşitli", "Yaşam olayı kelimeleri", "Anlamlı sıralama"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

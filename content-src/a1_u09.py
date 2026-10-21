"""A1 Ünite 9: Yeteneklerim."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("A1", 9, "Yeteneklerim", "Abilities and Free Time",
         "Neler yapabildiğimi ve boş zamanımda neler yapmayı sevdiğimi anlatabilir, birini bir etkinliğe davet edebilirim.",
         ["can / can't (yetenek)", "Can you ...? soruları ve kısa cevaplar", "like / love / hate + -ing", "Do you want to ...? / Let's ..."],
         ["sporlar", "hobiler", "müzik aletleri"],
         {"title": "Yetenek avı", "durationMinutes": 45,
          "goal": "Her öğrenciye 'Find someone who can...' kartı verilir. Öğrenciler birbirine Can you...? soruları sorarak kartı doldurur; sonra sınıfa 'Elif can play the guitar, but she can't swim' gibi cümlelerle rapor verir."})

u.vocab([
    ("swim", "yüzmek", "I can swim, but not very well.", "Yüzebilirim ama çok iyi değil.", None),
    ("ride a bike", "bisiklete binmek", "My son can ride a bike.", "Oğlum bisiklete binebiliyor.", None),
    ("drive", "araba sürmek", "Can you drive?", "Araba kullanabilir misin?", None),
    ("cook", "yemek yapmak", "My dad cooks very well.", "Babam çok iyi yemek yapar.", None),
    ("sing", "şarkı söylemek", "She can sing beautifully.", "Çok güzel şarkı söyleyebiliyor.", None),
    ("dance", "dans etmek", "I can't dance!", "Dans edemem!", None),
    ("draw", "çizmek, resim yapmak", "Can you draw a cat?", "Kedi çizebilir misin?", None),
    ("speak", "konuşmak (bir dili)", "I can speak Turkish and a little English.", "Türkçe ve biraz İngilizce konuşabiliyorum.", None),
    ("play football / basketball / tennis", "futbol / basketbol / tenis oynamak", "We play football on Sundays.", "Pazarları futbol oynarız.", "Top oyunlarıyla play (the yok)."),
    ("play the guitar / the piano", "gitar / piyano çalmak", "He can play the guitar.", "Gitar çalabiliyor.", "Müzik aletleriyle play the."),
    ("go swimming / running / cycling", "yüzmeye / koşuya / bisiklete gitmek", "I go running every morning.", "Her sabah koşuya giderim.", "-ing ile biten etkinliklerle go."),
    ("do yoga / karate", "yoga / karate yapmak", "My sister does yoga.", "Kız kardeşim yoga yapıyor.", None),
    ("chess", "satranç", "Can you play chess?", "Satranç oynayabilir misin?", None),
    ("hobby", "hobi", "My hobby is photography.", "Hobim fotoğrafçılık.", "Çoğul: hobbies."),
    ("free time", "boş zaman", "What do you do in your free time?", "Boş zamanında ne yaparsın?", None),
    ("team", "takım", "I'm in the school volleyball team.", "Okulun voleybol takımındayım.", None),
    ("well", "iyi (bir şekilde)", "She speaks English very well.", "Çok iyi İngilizce konuşuyor.", "good sıfat, well zarf: a good singer / sing well."),
    ("love", "çok sevmek, bayılmak", "I love dancing.", "Dans etmeye bayılırım.", None),
    ("hate", "nefret etmek", "I hate running.", "Koşmaktan nefret ederim.", None),
    ("enjoy", "keyif almak", "I enjoy cooking for my friends.", "Arkadaşlarıma yemek yapmaktan keyif alırım.", "enjoy + -ing"),
    ("join", "katılmak", "Do you want to join our team?", "Takımımıza katılmak ister misin?", None),
    ("practise", "pratik yapmak, çalışmak", "I practise the piano every day.", "Her gün piyano çalışırım.", "Amerikan yazımı: practice."),
    ("Let's ...", "Hadi ...", "Let's play tennis!", "Hadi tenis oynayalım!", "Let's + yalın fiil."),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Sporlar ve hobiler", "Yaptığım sporları ve hobileri play / go / do ile söyleyebilirim.",
    {"kind": "text", "title": "Spor merkezi duyurusu", "body": "CITY SPORTS CENTRE – What's on this week?\n\nMonday: Play basketball with our coach, Ali. 7 pm.\nTuesday: Do yoga in the garden. 8 am.\nWednesday: Go swimming in the big pool. All day.\nThursday: Play tennis. Rackets are free!\nSaturday: Go cycling by the sea. Meet at the door at 10 am.\n\nAll activities are free for students.",
     "questions": [
        mc("When can you do yoga?", ["On Monday evening", "On Tuesday morning", "On Saturday"], 1, "\"Tuesday: Do yoga in the garden. 8 am.\""),
        mc("What's free on Thursday?", ["The rackets", "The bikes", "The pool"], 0, "\"Rackets are free!\""),
     ]},
    {"explanation": "Spor ve etkinliklerle üç fiil kullanılır:\n\n| Fiil | Ne ile? | Örnek |\n|---|---|---|\n| **play** | top ve karşılıklı oyunlar | play football, play tennis, play chess |\n| **go** | -ing ile biten etkinlikler | go swimming, go running, go cycling |\n| **do** | bireysel sporlar, dövüş sanatları | do yoga, do karate, do exercise |\n\nMüzik aletlerinde **play the**: play **the** guitar, play **the** piano.\nSporlarda **the yok**: play football (~~play the football~~).",
     "examples": [{"en": "I play volleyball at school.", "tr": "Okulda voleybol oynarım."},
                  {"en": "We go swimming in summer.", "tr": "Yazın yüzmeye gideriz."},
                  {"en": "My mum does yoga.", "tr": "Annem yoga yapar."}],
     "turkishNote": "Türkçede \"gitar çalmak\" ve \"futbol oynamak\" farklı fiillerdir; İngilizcede ikisi de play. \"Yüzmeye gitmek\" = go swimming (go to swimming değil)."},
    [
        match([("play", "tennis"), ("go", "running"), ("do", "karate"), ("play the", "piano")], "Fiilleri eşleştirin."),
        mc("___ swimming", ["play", "go", "do"], 1, "-ing etkinlik → go."),
        mc("___ chess", ["play", "go", "do"], 0, "Karşılıklı oyun → play."),
        mc("___ yoga", ["play", "go", "do"], 2, "Bireysel spor → do."),
        mc("Hangisi doğru?", ["She plays the football.", "She plays football.", "She does football."], 1, "Sporda the yok: play football."),
        gap("He plays ___ guitar in a band.", ["the"], "Müzik aleti → play the."),
        gap("We ___ cycling on Sundays.", ["go"], "go cycling"),
        listen("In my free time I play basketball and I do karate. I don't go swimming. I hate water!", "Konuşan hangisini yapmıyor?", ["Basketbol", "Karate", "Yüzme"], 2, "\"I don't go swimming.\""),
        typ("İngilizce yazın: \"Her sabah koşuya giderim.\"", variants("I go running every morning."), "go running + every morning."),
        mc("\"What do you do in your free time?\" cevabı:", ["I play the piano.", "I'm a doctor.", "At nine o'clock."], 0, "Boş zaman → hobi."),
    ],
    {"kind": "speaking", "task": speak("Boş zamanınızda yaptığınız 3 etkinliği play, go ve do ile anlatın.",
                                       "In my free time I play tennis with my friends. On Sundays I go cycling. I also do yoga at home.",
                                       ["play/go/do doğru", "the doğru kullanıldı", "Geniş zaman doğru"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "Yapabilirim, yapamam", "can / can't ile neler yapabildiğimi anlatabilirim.",
    {"kind": "dialogue", "title": "Yeni oda arkadaşı", "lines": [
        {"speaker": "Selin", "text": "So, tell me about you. What can you do?"},
        {"speaker": "Emma", "text": "Well, I can cook. I can make great pasta!"},
        {"speaker": "Selin", "text": "Great! I can't cook at all."},
        {"speaker": "Emma", "text": "And I can play the piano, but I can't sing."},
        {"speaker": "Selin", "text": "I can sing! We can make music together."},
        {"speaker": "Emma", "text": "Perfect!"}],
     "questions": [
        mc("What can Emma cook?", ["Pizza", "Pasta", "Soup"], 1, "\"I can make great pasta!\""),
        mc("Who can sing?", ["Emma", "Selin", "Both"], 1, "Selin: \"I can sing!\""),
     ]},
    {"explanation": "**can** yetenek de anlatır (8. ünitede rica ve izin için gördük).\n\n| Olumlu | Olumsuz |\n|---|---|\n| I **can** swim. | I **can't** swim. |\n| She **can** drive. | She **can't** drive. |\n\n- Her özneyle aynıdır: he can (~~he cans~~).\n- Ardından **yalın fiil** gelir: can swim (~~can swims~~, ~~can to swim~~).\n- Derece: very well (çok iyi), well (iyi), a little (biraz), not at all (hiç).\n\n**Telaffuz:** Olumlu cümlede can zayıf okunur (/kən/), can't ise vurguludur (/kɑːnt/). Bu fark dinlerken çok önemli.",
     "examples": [{"en": "I can speak English a little.", "tr": "Biraz İngilizce konuşabiliyorum."},
                  {"en": "My grandma can't use a computer.", "tr": "Büyükannem bilgisayar kullanamıyor."},
                  {"en": "He can swim very well.", "tr": "Çok iyi yüzebiliyor."}],
     "turkishNote": "Türkçede \"-ebil\" fiile eklenir; İngilizcede can ayrı bir kelimedir ve fiilin önüne gelir. \"I can't cook at all\" = Hiç yemek yapamam. \"Very well\" cümlenin sonuna gelir: I can very well swim değil, I can swim very well."},
    [
        mc("Hangisi doğru?", ["She cans swim.", "She can swim.", "She can swims."], 1, "can + yalın fiil, -s yok."),
        mc("Hangisi doğru?", ["I can to drive.", "I can drive.", "I can driving."], 1, "can + yalın fiil (to yok)."),
        gap("I ___ swim. I'm afraid of water. (yüzemem)", ["can't", "cannot"], "Olumsuz: can't."),
        gap("My brother can play the piano very ___.", ["well"], "çok iyi = very well."),
        order(["can", "My", "sister", "speak", "French", "a", "little"], "My sister can speak French a little.", "Özne + can + fiil + nesne + derece.", "Kız kardeşim biraz Fransızca konuşabiliyor."),
        listen("I can ride a bike, but I can't drive a car.", "Konuşan ne yapamıyor?", ["Bisiklete binmek", "Araba sürmek", "İkisini de"], 1, "\"I can't drive a car\" (can't vurgulu)."),
        listen("My dad can cook very well. He can make fantastic kebabs.", "Baba yemek yapabiliyor mu?", ["Evet, çok iyi", "Hayır", "Biraz"], 0, "\"can cook very well\""),
        mc("\"Hiç dans edemem.\"", ["I can't dance at all.", "I can dance at all.", "I don't can dance."], 0, "not at all = hiç."),
        typ("İngilizce yazın: \"Gitar çalabiliyorum ama şarkı söyleyemiyorum.\"", variants("I can play the guitar, but I can't sing.", "I can play the guitar but I can't sing."), "can play the guitar, but can't sing."),
        mc("good mi well mi? \"She is a ___ singer.\"", ["good", "well"], 0, "İsimden önce sıfat: a good singer."),
    ],
    {"kind": "speaking", "task": speak("Yapabildiğiniz 3 şeyi ve yapamadığınız 2 şeyi söyleyin. En az birine derece ekleyin (very well, a little).",
                                       "I can swim very well. I can cook and I can speak English a little. I can't drive and I can't play the guitar.",
                                       ["can + yalın fiil", "can't doğru", "Derece ifadesi doğru yerde"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "Can you ...?", "Birine neler yapabildiğini sorup kısa cevap verebilirim.",
    {"kind": "dialogue", "title": "Yaz kampı başvurusu", "lines": [
        {"speaker": "Coach", "text": "Hi, Mert. Can you swim?"},
        {"speaker": "Mert", "text": "Yes, I can."},
        {"speaker": "Coach", "text": "Can you play any instruments?"},
        {"speaker": "Mert", "text": "No, I can't. But I can sing."},
        {"speaker": "Coach", "text": "Great. And what sports can you play?"},
        {"speaker": "Mert", "text": "I can play volleyball and basketball."}],
     "questions": [
        mc("Can Mert play an instrument?", ["Yes, he can.", "No, he can't."], 1, "\"No, I can't.\""),
        mc("What sports can Mert play?", ["Football and tennis", "Volleyball and basketball", "Only swimming"], 1, "\"volleyball and basketball\""),
     ]},
    {"explanation": "**Soru:** **Can** + özne + fiil?\n\n- **Can you** swim? – Yes, I **can**. / No, I **can't**.\n- **Can she** drive? – Yes, she **can**. / No, she **can't**.\n\n**Bilgi sorusu:** Soru kelimesi + can + özne + fiil?\n\n- **What** can you cook?\n- **How many** languages can you speak?\n\nKısa cevapta fiil tekrar edilmez: ~~Yes, I can swim~~ değil, **Yes, I can.** (Uzun cevap da yanlış değil ama doğal olan kısa cevaptır.)",
     "examples": [{"en": "Can your mum speak English? – Yes, she can.", "tr": "Annen İngilizce konuşabiliyor mu? – Evet."},
                  {"en": "What instruments can you play?", "tr": "Hangi enstrümanları çalabiliyorsun?"},
                  {"en": "How many languages can you speak?", "tr": "Kaç dil konuşabiliyorsun?"}],
     "turkishNote": "\"Do you can swim?\" Türkçe konuşanların sık yaptığı bir hatadır. can soruyu kendisi kurar, do gerekmez."},
    [
        mc("Hangisi doğru?", ["Do you can swim?", "Can you swim?", "You can swim?"], 1, "Can + özne + fiil?", {0: "can ile do kullanılmaz."}),
        mc("\"Can your brother drive?\" (Evet.)", ["Yes, he can.", "Yes, he does.", "Yes, he drives."], 0, "Kısa cevap: Yes, he can."),
        mc("\"Can you play chess?\" (Hayır.)", ["No, I don't.", "No, I can't.", "No, I not."], 1, "No, I can't."),
        gap("___ you speak German? – No, I can't.", ["Can"], "Can ile soru."),
        gap("What ___ you cook? – Pasta and soup.", ["can"], "Soru kelimesi + can."),
        order(["languages", "How", "many", "can", "you", "speak", "?"], "How many languages can you speak?", "How many + isim + can + özne + fiil?", "Kaç dil konuşabiliyorsun?"),
        listen("Can you ride a horse? – No, I can't. But I can ride a bike.", "Konuşan neye binebiliyor?", ["Ata", "Bisiklete", "İkisine de"], 1, "\"I can ride a bike\""),
        typ("Soru yapın: \"She can play the violin.\"", variants("Can she play the violin?"), "Can + she + play the violin?"),
        mc("\"Can they dance?\" (Evet.)", ["Yes, they can.", "Yes, they do.", "Yes, can they."], 0, "Yes, they can."),
        gap("Can Ayşe swim? – No, she ___.", ["can't", "cannot"], "Olumsuz kısa cevap."),
    ],
    {"kind": "speaking", "task": speak("JAI ile yaz kampı görüşmesi yapın. JAI'ye 4 tane Can you...? sorusu sorun.",
                                       "Can you swim? Can you play the guitar? Can you cook? What sports can you play?",
                                       ["Can + özne + fiil düzeni", "do kullanmadı", "Bilgi sorusu (What/How many) kurdu"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Sevdiklerim", "like / love / hate + -ing ile neyi yapmayı sevdiğimi anlatabilirim.",
    {"kind": "text", "title": "Bir forum mesajı", "body": "Hi everyone! I'm Kaan from İzmir. I'm 24 and I'm a nurse.\n\nIn my free time I love reading, especially science fiction. I like cooking too, and I often cook for my friends at the weekend. I don't like watching TV. It's boring! And I hate shopping. Crowded shops are terrible.\n\nWhat do you like doing? Write to me!",
     "questions": [
        mc("What does Kaan love?", ["Watching TV", "Reading", "Shopping"], 1, "\"I love reading\""),
        mc("Why doesn't Kaan like watching TV?", ["It's boring.", "It's expensive.", "He doesn't have a TV."], 0, "\"It's boring!\""),
     ]},
    {"explanation": "Sevme fiillerinden sonra genellikle fiilin **-ing** hali gelir:\n\n| | |\n|---|---|\n| ❤️❤️ | I **love** dancing. |\n| ❤️ | I **like** cooking. / I **enjoy** cooking. |\n| 😐 | I **don't like** running. |\n| 💔 | I **hate** shopping. |\n\n**-ing yazım kuralları:**\n\n- Çoğu fiil: read → read**ing**, play → play**ing**\n- Sondaki -e düşer: dance → danc**ing**, ride → rid**ing**\n- Kısa fiilde son ünsüz ikilenir: swim → swi**mm**ing, run → ru**nn**ing\n\nSoru: **Do you like** swimming? – Yes, I **do**. / No, I **don't**.",
     "examples": [{"en": "I love listening to music.", "tr": "Müzik dinlemeye bayılırım."},
                  {"en": "My dad doesn't like flying.", "tr": "Babam uçmayı sevmez."},
                  {"en": "Do you enjoy cooking?", "tr": "Yemek yapmaktan keyif alır mısın?"}],
     "turkishNote": "Türkçede \"okumayı severim\" deriz; İngilizcede \"I like read\" yanlıştır, \"I like reading\" doğrudur. can sorusunun aksine like sorusunda do / does kullanılır: Do you like...? / Does she like...?"},
    [
        mc("Hangisi doğru?", ["I like read.", "I like reading.", "I like to reading."], 1, "like + -ing."),
        gap("She loves ___. (dance)", ["dancing"], "dance → dancing (-e düşer)."),
        gap("We enjoy ___ in the sea. (swim)", ["swimming"], "swim → swimming (m ikilenir)."),
        gap("My kids hate ___ up early. (get)", ["getting"], "get → getting."),
        match([("❤️❤️", "love"), ("❤️", "like"), ("😐", "don't like"), ("💔", "hate")], "Sembolleri eşleştirin."),
        mc("\"Does your sister like cooking?\" (Evet.)", ["Yes, she can.", "Yes, she does.", "Yes, she likes."], 1, "Does ile soru → Yes, she does."),
        order(["Do", "you", "like", "watching", "football", "?"], "Do you like watching football?", "Do + özne + like + -ing?", "Futbol izlemeyi sever misin?"),
        listen("I love swimming and I like running, but I hate going to the gym.", "Konuşan neyden nefret ediyor?", ["Yüzmekten", "Koşmaktan", "Spor salonuna gitmekten"], 2, "\"I hate going to the gym\""),
        typ("İngilizce yazın: \"Müzik dinlemeyi severim.\"", variants("I like listening to music.", "I enjoy listening to music."), "like + listening to music."),
        mc("Kaan'ın mesajına göre doğru olan:", ["He enjoys shopping.", "He doesn't like watching TV.", "He hates cooking."], 1, "\"I don't like watching TV.\""),
    ],
    {"kind": "writing", "task": write("Kaan'ın mesajına cevap yazın: kendinizi tanıtın, sevdiğiniz 2 şeyi, sevmediğiniz 1 şeyi ve nefret ettiğiniz 1 şeyi yazın.",
                                      "Hi Kaan! I'm Zeynep from Bursa. I love reading too, but I prefer novels. I like going for walks with my dog. I don't like cooking, and I hate cleaning the house!",
                                      ["like/love/hate + -ing doğru", "-ing yazımı doğru", "Kendini tanıttı"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Davet etmek", "Birini bir etkinliğe davet edebilir, daveti kabul edip kibarca reddedebilirim.",
    {"kind": "dialogue", "title": "Telefonda", "lines": [
        {"speaker": "Burak", "text": "Hi, Leyla! Do you want to play tennis on Saturday?"},
        {"speaker": "Leyla", "text": "Sorry, I can't. I'm busy on Saturday."},
        {"speaker": "Burak", "text": "What about Sunday?"},
        {"speaker": "Leyla", "text": "Sunday is fine. But I can't play very well!"},
        {"speaker": "Burak", "text": "No problem. I can teach you. Let's meet at the sports centre at ten."},
        {"speaker": "Leyla", "text": "Great idea! See you on Sunday."}],
     "questions": [
        mc("When do they play tennis?", ["On Saturday", "On Sunday", "On Monday"], 1, "\"Sunday is fine.\""),
        mc("Where do they meet?", ["At the park", "At the sports centre", "At Leyla's house"], 1, "\"Let's meet at the sports centre at ten.\""),
     ]},
    {"explanation": "**Davet etmek / öneri:**\n\n- **Do you want to** + fiil? → Do you want to go swimming?\n- **Let's** + fiil. → Let's play chess.\n- **What about** + gün / -ing? → What about Sunday? / What about going to the cinema?\n\n**Kabul etmek:** Great idea! / Sure! / I'd love to. / OK, why not?\n\n**Reddetmek:** Sorry, I can't. I'm busy. / Sorry, I don't really like ...\n\nReddederken bir sebep ve başka bir öneri vermek kibar ve doğaldır.",
     "examples": [{"en": "Do you want to come to my party?", "tr": "Partime gelmek ister misin?"},
                  {"en": "Let's go cycling this afternoon.", "tr": "Bu öğleden sonra bisiklete binelim."},
                  {"en": "Sorry, I can't. I have a lesson.", "tr": "Kusura bakma, yapamam. Dersim var."}],
     "turkishNote": "\"Let's\" = let us; ardından yalın fiil gelir: Let's go (Let's going değil, Let's to go değil). \"Do you want to\" da yalın fiil alır."},
    [
        mc("Hangisi doğru?", ["Let's to go swimming.", "Let's go swimming.", "Let's going swimming."], 1, "Let's + yalın fiil."),
        mc("Bir daveti kibarca reddetmek:", ["No.", "Sorry, I can't. I'm busy.", "I don't want."], 1, "Özür + sebep."),
        mc("Daveti kabul etmek:", ["Great idea!", "No problem, I'm busy.", "Sorry."], 0, "Great idea! / Sure!"),
        gap("Do you want ___ play chess?", ["to"], "want to + fiil."),
        gap("What ___ Saturday? (Cumartesiye ne dersin?)", ["about"], "What about + gün?"),
        order(["you", "Do", "want", "to", "come", "to", "the", "cinema", "?"], "Do you want to come to the cinema?", "Do you want to + fiil?", "Sinemaya gelmek ister misin?"),
        listen("Let's go running tomorrow morning. – Sorry, I can't. I work in the morning. What about the evening?", "İkinci konuşan ne öneriyor?", ["Sabah koşmak", "Akşam koşmak", "Hiç koşmamak"], 1, "\"What about the evening?\""),
        typ("İngilizce yazın: \"Hadi tenis oynayalım!\"", variants("Let's play tennis!"), "Let's + play tennis."),
        match([("Do you want to", "go cycling?"), ("Let's", "meet at six."), ("What about", "Friday?"), ("Sorry,", "I can't.")], "Cümleleri tamamlayın."),
        mc("\"Do you want to play football?\" Futboldan hoşlanmıyorsunuz:", ["Sorry, I don't really like football. Let's go swimming.", "Yes, I do.", "I can football."], 0, "Sebep + yeni öneri."),
    ],
    {"kind": "speaking", "task": speak("JAI'yi hafta sonu bir etkinliğe davet edin. JAI ilk öneriyi reddedecek; başka bir gün ya da etkinlik önerin ve buluşma yeri/saati belirleyin.",
                                       "Do you want to go cycling on Saturday? ... Oh, OK. What about Sunday? ... Great! Let's meet at the park at eleven.",
                                       ["Do you want to / Let's doğru", "What about ile yeni öneri", "Yer ve saat belirtti"])},
)

u.test([
    mc("___ the piano", ["play", "go", "do"], 0, "Müzik aleti → play the."),
    mc("___ swimming", ["play", "go", "do"], 1, "go swimming"),
    mc("Hangisi doğru?", ["He cans drive.", "He can drive.", "He can drives."], 1, "can + yalın fiil."),
    gap("I ___ swim. (yüzemem)", ["can't", "cannot"], "can't"),
    mc("Hangisi doğru?", ["Do you can cook?", "Can you cook?"], 1, "Can + özne + fiil?"),
    mc("\"Can your sister sing?\" (Evet.)", ["Yes, she does.", "Yes, she can.", "Yes, she sings."], 1, "Yes, she can."),
    gap("She speaks English very ___.", ["well"], "very well"),
    mc("Hangisi doğru?", ["I love read.", "I love reading.", "I love to reading."], 1, "love + -ing"),
    gap("We enjoy ___ in the park. (run)", ["running"], "run → running"),
    mc("\"Does he like dancing?\" (Hayır.)", ["No, he can't.", "No, he doesn't.", "No, he isn't."], 1, "Does → No, he doesn't."),
    mc("Hangisi doğru?", ["Let's going.", "Let's go.", "Let's to go."], 1, "Let's + yalın fiil."),
    order(["want", "Do", "you", "to", "play", "chess", "?"], "Do you want to play chess?", "Do you want to + fiil?", "Satranç oynamak ister misin?"),
    listen("I can play the guitar, but I can't play the piano. I love singing too.", "Konuşan neyi çalamıyor?", ["Gitar", "Piyano", "İkisini de"], 1, "\"I can't play the piano\""),
    typ("İngilizce yazın: \"Boş zamanında ne yaparsın?\"", variants("What do you do in your free time?"), "What do you do + in your free time?"),
    write("Kendinizi bir spor kulübüne tanıtın: neler yapabildiğiniz, neler yapamadığınız, ne yapmayı sevdiğiniz (5 cümle).",
          "Hi, I'm Can. I can swim very well and I can play volleyball. I can't play tennis, but I want to learn. I love running in the morning. I don't like going to the gym.",
          ["can / can't doğru", "like/love + -ing doğru", "play/go/do doğru", "Anlamlı bir tanıtım"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

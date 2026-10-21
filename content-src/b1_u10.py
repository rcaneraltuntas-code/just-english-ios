"""B1 Ünite 10: Boş zaman."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("B1", 10, "Boş zaman", "Free Time",
         "Hobilerim ve boş zaman etkinliklerim hakkında konuşurken fiilden sonra -ing ya da to + fiil kullanmayı doğru seçebilir, edat + -ing yapısını ve amaç bildiren to'yu kullanabilir, remember / stop / try fiillerinin iki anlamını ayırt edebilirim.",
         ["-ing (gerund) özne olarak ve like / enjoy / mind sonrası", "fiil + to + fiil (want, decide, hope...)", "edat + -ing (good at, interested in...)", "amaç bildiren to ve sıfat + to", "remember / stop / try + -ing ya da to"],
         ["hobiler", "spor ve etkinlikler", "boş zaman alışkanlıkları"],
         {"title": "Hobi kulübü", "durationMinutes": 45,
          "goal": "Öğrenciler hayali bir \"hobi kulübü\" kurar. Her grup bir kulüp seçer (fotoğraf, doğa yürüyüşü, satranç...) ve diğer öğrencileri ikna etmeye çalışır: Joining our club is..., You'll learn to..., If you're interested in..., We go there to... Sonunda herkes hangi kulübe katılmaya karar verdiğini ve nedenini I've decided to... çünkü I enjoy... ile açıklar."})

u.vocab([
    ("hobby", "hobi", "My hobby is photography.", "Hobim fotoğrafçılık.", None),
    ("enjoy", "-den keyif almak", "I enjoy cooking for my friends.", "Arkadaşlarıma yemek yapmaktan keyif alırım.", "enjoy + -ing"),
    ("can't stand", "dayanamamak, hiç sevmemek", "I can't stand waiting in queues.", "Kuyrukta beklemeye dayanamam.", "can't stand + -ing"),
    ("don't mind", "sorun etmemek", "I don't mind getting up early.", "Erken kalkmayı dert etmem.", "mind + -ing"),
    ("be keen on", "-e meraklı olmak", "She's keen on hiking.", "Doğa yürüyüşüne meraklı.", "keen on + -ing"),
    ("be good at", "-de iyi olmak", "He's good at drawing.", "Resim çizmede iyi.", None),
    ("be interested in", "-e ilgi duymak", "I'm interested in learning Spanish.", "İspanyolca öğrenmekle ilgileniyorum.", None),
    ("be fond of", "-i sevmek", "My uncle is fond of fishing.", "Amcam balık tutmayı sever.", None),
    ("take up", "(hobiye) başlamak", "I took up yoga last year.", "Geçen yıl yogaya başladım.", None),
    ("hiking", "doğa yürüyüşü", "We go hiking every weekend.", "Her hafta sonu doğa yürüyüşüne gideriz.", None),
    ("knitting", "örgü", "My grandmother taught me knitting.", "Büyükannem bana örgü öğretti.", None),
    ("gardening", "bahçıvanlık", "Gardening helps me relax.", "Bahçıvanlık rahatlamama yardım ediyor.", None),
    ("board game", "kutu oyunu", "We play board games on Friday nights.", "Cuma akşamları kutu oyunu oynarız.", None),
    ("chess", "satranç", "Is chess difficult to learn?", "Satranç öğrenmek zor mu?", None),
    ("volunteer", "gönüllü; gönüllü olmak", "I volunteer at an animal shelter.", "Bir hayvan barınağında gönüllüyüm.", None),
    ("relax", "rahatlamak", "Reading helps me relax.", "Okumak rahatlamama yardımcı oluyor.", None),
    ("spare time", "boş zaman", "What do you do in your spare time?", "Boş zamanında ne yaparsın?", "free time ile aynı"),
    ("manage", "başarmak, becermek", "I managed to finish the marathon.", "Maratonu bitirmeyi başardım.", "manage + to"),
    ("refuse", "reddetmek", "He refused to play.", "Oynamayı reddetti.", "refuse + to"),
    ("afford", "(parası) yetmek", "I can't afford to join the gym.", "Spor salonuna yazılmaya param yetmiyor.", "afford + to"),
    ("give up", "bırakmak", "I gave up playing the piano.", "Piyano çalmayı bıraktım.", "give up + -ing"),
    ("instead of", "yerine", "Let's walk instead of taking the bus.", "Otobüse binmek yerine yürüyelim.", "instead of + -ing"),
    ("look forward to", "dört gözle beklemek", "I'm looking forward to seeing you.", "Seni görmeyi dört gözle bekliyorum.", "to + -ing!"),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Yapmayı severim", "Sevdiğim ve sevmediğim etkinlikleri -ing ile anlatabilir, -ing'i cümle öznesi olarak kullanabilirim.",
    {"kind": "dialogue", "title": "Yeni ev arkadaşları", "lines": [
        {"speaker": "Ayça", "text": "So, what do you enjoy doing in your spare time?"},
        {"speaker": "Kerem", "text": "I love cooking, and I enjoy playing board games. What about you?"},
        {"speaker": "Ayça", "text": "I'm into running. Running in the morning gives me energy for the whole day."},
        {"speaker": "Kerem", "text": "Wow. I can't stand getting up early!"},
        {"speaker": "Ayça", "text": "Don't worry, I don't mind running alone. But I hate doing the washing-up."},
        {"speaker": "Kerem", "text": "Perfect. I'll cook and wash up, and you can buy the coffee!"}],
     "questions": [
        mc("What does Kerem enjoy?", ["Running and cooking", "Cooking and board games", "Getting up early"], 1, "\"I love cooking, and I enjoy playing board games.\""),
        mc("What does Ayça hate?", ["Running", "Cooking", "Doing the washing-up"], 2, "\"I hate doing the washing-up\""),
     ]},
    {"explanation": "**-ing (gerund)**, fiili bir **isim gibi** kullanmamızı sağlar.\n\n**1. Bazı fiillerden sonra -ing gelir:**\n\n| Fiil | Örnek |\n|---|---|\n| **enjoy** | I enjoy **cooking**. |\n| **like / love / hate** | I love **reading**. |\n| **don't mind** | I don't mind **waiting**. |\n| **can't stand** | I can't stand **getting** up early. |\n| **finish** | Have you finished **eating**? |\n| **give up** | She gave up **smoking**. |\n| **spend (time)** | I spend hours **reading**. |\n\n(like / love / hate'ten sonra **to + fiil** de olabilir: I like **to read**. İkisi de doğru.)\n\n**2. -ing cümlenin öznesi olabilir:**\n\n- **Running** gives me energy.\n- **Learning** a language takes time.\n- **Swimming** is good for your back.\n\nÖzne olarak kullanılan -ing **tekil** sayılır: Swimming **is** ... (~~are~~)",
     "examples": [{"en": "I enjoy spending time with my family.", "tr": "Ailemle vakit geçirmekten keyif alırım."},
                  {"en": "Cooking for friends is my favourite thing.", "tr": "Arkadaşlara yemek yapmak en sevdiğim şey."},
                  {"en": "Do you mind closing the window?", "tr": "Pencereyi kapatır mısın? (Sakıncası var mı?)"}],
     "turkishNote": "Türkçede \"koşmak bana enerji veriyor\" derken mastar (-mak) kullanırız. İngilizcede bunun karşılığı \"to run\" değil, çoğunlukla -ing'dir: Running gives me energy. \"I enjoy to cook\" da yaygın bir hatadır; enjoy'dan sonra her zaman -ing gelir."},
    [
        mc("Hangisi doğru?", ["I enjoy to cook.", "I enjoy cooking."], 1, "enjoy + -ing."),
        mc("___ is good for your health.", ["Swim", "Swimming", "To swimming"], 1, "Özne → -ing."),
        mc("I can't stand ___ in traffic.", ["sit", "sitting", "to sitting"], 1, "can't stand + -ing."),
        gap("I don't mind ___ (wait) for a few minutes.", ["waiting"], "mind + -ing."),
        gap("She gave up ___ (eat) sugar.", ["eating"], "give up + -ing."),
        gap("___ (learn) a language takes time.", ["Learning"], "Özne → -ing."),
        gap("I spend hours ___ (read) every weekend.", ["reading"], "spend time + -ing."),
        mc("Hangisi doğru?", ["Reading books are relaxing.", "Reading books is relaxing."], 1, "-ing özne → tekil."),
        listen("I really enjoy gardening. Growing my own tomatoes makes me so happy. But I can't stand cutting the grass!", "Konuşan neye dayanamıyor?", ["Domates yetiştirmeye", "Çim biçmeye", "Bahçede çalışmaya"], 1, "\"I can't stand cutting the grass\""),
        typ("İngilizce yazın: \"Kuyrukta beklemeye dayanamam.\"", variants("I can't stand waiting in queues.", "I can't stand waiting in line.", "I can't stand waiting in a queue.", "I cannot stand waiting in queues.", "I hate waiting in queues."), "I can't stand waiting in queues."),
    ],
    {"kind": "speaking", "task": speak("Boş zamanınızı anlatın: enjoy, love, don't mind, can't stand, hate ve spend time + -ing kullanarak 6 cümle kurun. Sonra -ing ile başlayan 2 cümle söyleyin (\"Walking by the sea is...\").",
                                       "I enjoy watching documentaries. I love playing chess with my father. I don't mind cleaning the house. I can't stand shopping in crowded malls. I spend a lot of time reading. Walking by the sea is my favourite way to relax. Playing the guitar helps me forget my problems.",
                                       ["Fiil + -ing doğru", "-ing özne ve tekil fiil", "Çeşitli fiiller"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "Yapmaya karar verdim", "want, decide, hope, plan, learn gibi fiillerden sonra to + fiil kullanabilirim.",
    {"kind": "text", "title": "Yeni yıl kararları", "body": "We asked our readers about their plans for this year.\n\n\"I've decided to learn the guitar. I've always wanted to play in a band.\" – Emre, 24\n\n\"I'm hoping to run my first half marathon in April. I need to train more!\" – Hilal, 31\n\n\"Last year I promised to spend less time on my phone, but I didn't manage to do it. This year I'm planning to try again.\" – Cansu, 19\n\n\"My wife and I would like to visit Japan. We're saving up, but we can't afford to go yet.\" – Hasan, 45\n\n\"I've agreed to teach chess to the children in my building. They're learning to play really quickly!\" – Nevin, 68",
     "questions": [
        mc("What has Emre decided to do?", ["Join a gym", "Learn the guitar", "Visit Japan"], 1, "\"I've decided to learn the guitar.\""),
        mc("What didn't Cansu manage to do last year?", ["Run a marathon", "Spend less time on her phone", "Save money"], 1, "\"I promised to spend less time on my phone, but I didn't manage to do it.\""),
     ]},
    {"explanation": "Bazı fiillerden sonra **to + yalın fiil (infinitive)** gelir. Bu fiiller çoğunlukla **gelecek, plan, istek ve karar** anlatır.\n\n| Fiil | Örnek |\n|---|---|\n| **want** | I want **to learn** the guitar. |\n| **would like** | We'd like **to visit** Japan. |\n| **decide** | I've decided **to join** a gym. |\n| **hope** | I'm hoping **to run** a marathon. |\n| **plan** | They're planning **to move**. |\n| **need** | I need **to train** more. |\n| **learn** | They're learning **to play** chess. |\n| **promise** | He promised **to call**. |\n| **agree / refuse** | She agreed **to help**. He refused **to come**. |\n| **manage** | I managed **to finish**. |\n| **afford** | We can't afford **to go**. |\n| **try** | Try **to relax**. |\n\n**Olumsuz:** **not to** + fiil → I decided **not to go**.",
     "examples": [{"en": "I've decided to take up swimming.", "tr": "Yüzmeye başlamaya karar verdim."},
                  {"en": "She refused to lend me her car.", "tr": "Arabasını bana ödünç vermeyi reddetti."},
                  {"en": "We decided not to go out because of the rain.", "tr": "Yağmur yüzünden dışarı çıkmamaya karar verdik."}],
     "turkishNote": "Türkçede \"gitmemeye karar verdim\" derken olumsuzluk fiile eklenir. İngilizcede \"not\" to'dan önce gelir: I decided not to go (~~I decided to not go~~ günlük dilde duyulsa da). \"I didn't decide to go\" ise farklı bir anlama gelir: Gitmeye ben karar vermedim."},
    [
        mc("Hangisi doğru?", ["I want learning the piano.", "I want to learn the piano."], 1, "want + to."),
        mc("I've decided ___ a new hobby.", ["to start", "starting"], 0, "decide + to."),
        mc("\"Gitmemeye karar verdim.\"", ["I didn't decide to go.", "I decided not to go."], 1, "decide not to."),
        gap("We're planning ___ (move) to the coast.", ["to move"], "plan + to."),
        gap("He refused ___ (help) us.", ["to help"], "refuse + to."),
        gap("I finally managed ___ (finish) the book.", ["to finish"], "manage + to."),
        gap("They can't afford ___ (buy) a new car.", ["to buy"], "afford + to."),
        gap("She promised ___ (not be) late again.", ["not to be"], "promise not to."),
        listen("I'd love to learn to dance. My friend has agreed to come to a salsa class with me next week, so I'm really excited.", "Arkadaşı neyi kabul etti?", ["Dans öğretmeyi", "Salsa dersine birlikte gelmeyi", "Parti vermeyi"], 1, "\"My friend has agreed to come to a salsa class with me\""),
        typ("İngilizce yazın: \"Yüzmeye başlamaya karar verdim.\"", variants("I've decided to take up swimming.", "I have decided to take up swimming.", "I decided to take up swimming.", "I've decided to start swimming.", "I decided to start swimming.", "I have decided to start swimming."), "I've decided to take up swimming."),
    ],
    {"kind": "speaking", "task": speak("Bu yıl için hobi ve boş zaman planlarınızı anlatın. want, would like, hope, plan, decide, need ve en az bir \"not to\" kullanın. Geçen yıl başardığınız bir şeyi manage to ile söyleyin.",
                                       "This year I want to read twenty books. I'd like to learn to cook Indian food, and I'm hoping to go on a hiking trip in the Kaçkar Mountains. I'm planning to join a photography club. I've decided not to buy any new clothes for six months! Last year I managed to run 10 kilometres without stopping.",
                                       ["Fiil + to doğru", "not to", "manage to"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "İyi misin, ilgili misin?", "Edatlardan sonra -ing kullanarak ilgi alanlarımı ve yeteneklerimi anlatabilirim.",
    {"kind": "dialogue", "title": "Gönüllü başvurusu", "lines": [
        {"speaker": "Coordinator", "text": "Thanks for coming. Why are you interested in volunteering with us?"},
        {"speaker": "Melike", "text": "I'm really keen on working with children, and I'm good at organising games."},
        {"speaker": "Coordinator", "text": "Great. Is it OK for you to work at weekends?"},
        {"speaker": "Melike", "text": "Yes, no problem. Actually, I'm tired of spending my weekends at home doing nothing."},
        {"speaker": "Coordinator", "text": "Wonderful. Before starting, you'll do a short training day."},
        {"speaker": "Melike", "text": "I'm looking forward to meeting the kids!"}],
     "questions": [
        mc("What is Melike good at?", ["Teaching English", "Organising games", "Cooking"], 1, "\"I'm good at organising games\""),
        mc("What is Melike tired of?", ["Working with children", "Spending her weekends at home doing nothing", "Training"], 1, "\"I'm tired of spending my weekends at home doing nothing\""),
     ]},
    {"explanation": "**Edatlardan (in, at, of, on, about, for, before, after, without...) sonra fiil gelirse -ing olur.**\n\n| Kalıp | Örnek |\n|---|---|\n| be **good at** | She's good at **drawing**. |\n| be **interested in** | I'm interested in **learning** Italian. |\n| be **keen on** | He's keen on **cycling**. |\n| be **fond of** | My aunt is fond of **knitting**. |\n| be **tired of** | I'm tired of **waiting**. |\n| be **afraid of** | She's afraid of **flying**. |\n| **think about** | I'm thinking about **joining** a club. |\n| **instead of** | Let's walk instead of **driving**. |\n| **before / after** | Before **starting**, read the rules. |\n| **without** | He left without **saying** goodbye. |\n| **How about** | How about **going** to the cinema? |\n\n**Dikkat: look forward to**'daki **to** bir edattır, bu yüzden -ing gelir:\n\n- I'm looking forward to **seeing** you. (~~to see~~)",
     "examples": [{"en": "I'm thinking about taking up tennis.", "tr": "Tenise başlamayı düşünüyorum."},
                  {"en": "He's afraid of swimming in the sea.", "tr": "Denizde yüzmekten korkuyor."},
                  {"en": "How about having a picnic on Sunday?", "tr": "Pazar günü pikniğe ne dersin?"}],
     "turkishNote": "\"Seni görmeyi dört gözle bekliyorum\" cümlesi için \"I'm looking forward to see you\" demek Türkçe konuşanların en sık yaptığı hatalardan biridir. look forward to'dan sonra her zaman -ing gelir: I'm looking forward to seeing you."},
    [
        mc("I'm good at ___.", ["swim", "swimming", "to swim"], 1, "at + -ing."),
        mc("Hangisi doğru?", ["I'm looking forward to see you.", "I'm looking forward to seeing you."], 1, "look forward to + -ing."),
        mc("How about ___ to the beach?", ["go", "to go", "going"], 2, "How about + -ing."),
        gap("She's interested ___ learning Japanese.", ["in"], "interested in."),
        gap("I'm tired of ___ (wait) for the bus.", ["waiting"], "of + -ing."),
        gap("He left without ___ (say) goodbye.", ["saying"], "without + -ing."),
        gap("Let's cook at home instead of ___ (eat) out.", ["eating"], "instead of + -ing."),
        gap("My son is afraid ___ swimming in deep water.", ["of"], "afraid of."),
        match([("good", "at"), ("interested", "in"), ("keen", "on"), ("tired", "of"), ("look forward", "to")], "Edatları eşleştirin."),
        listen("I'm thinking about joining a choir. I'm not very good at singing, but I'm keen on meeting new people.", "Konuşan neyi düşünüyor?", ["Koroya katılmayı", "Şarkı dersi vermeyi", "Konsere gitmeyi"], 0, "\"I'm thinking about joining a choir\""),
    ],
    {"kind": "speaking", "task": speak("Bir gönüllü kuruluşu ya da hobi kulübüyle mülakat yaptığınızı düşünün. JAI sorular soracak. Cevaplarınızda good at, interested in, keen on, tired of, thinking about ve looking forward to + -ing kullanın.",
                                       "I'm interested in helping older people because I'm good at listening. I'm also keen on cooking, so I could cook for them. To be honest, I'm tired of sitting in front of a computer all day. I've been thinking about volunteering for a long time, and I'm really looking forward to starting!",
                                       ["Edat + -ing doğru", "look forward to + -ing", "Doğal mülakat dili"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Ne için?", "Amaç bildirmek için to kullanabilir, sıfat + to + fiil yapısıyla etkinlikleri değerlendirebilirim.",
    {"kind": "text", "title": "Neden satranç?", "body": "Chess is one of the oldest board games in the world, and millions of people play it to train their brains.\n\nIs it difficult to learn? Not really. It's easy to learn the rules, but it's hard to become a good player. Many people use apps to practise, and some join clubs to meet other players.\n\nIt's important to start slowly. Play against friends first, and don't be afraid of losing. It's normal to lose a lot at the beginning.\n\nThe best thing about chess? It's cheap to play. All you need is a board, and you can play it anywhere: in a park, on a train or online.",
     "questions": [
        mc("Why do many people play chess, according to the text?", ["To make money", "To train their brains", "To relax on trains"], 1, "\"to train their brains\""),
        mc("What is hard about chess?", ["Learning the rules", "Becoming a good player", "Finding a board"], 1, "\"it's hard to become a good player\""),
     ]},
    {"explanation": "**1. Amaç bildiren to** (= in order to, \"-mek için\")\n\n- I go to the gym **to keep** fit.\n- She uses apps **to practise**.\n- **Why** do you go there? – **To meet** friends.\n\n**Dikkat:** Amaç için ~~for + fiil~~ kullanılmaz:\n\n- I went to the shop **to buy** bread. (~~for buy~~ / ~~for buying~~)\n- Ama **for + isim** olur: I went to the shop **for** bread.\n\n**2. It's + sıfat + to + fiil** (… yapmak … dır)\n\n| Kalıp | Örnek |\n|---|---|\n| It's **easy to** ... | It's easy to learn the rules. |\n| It's **hard / difficult to** ... | It's hard to become a good player. |\n| It's **important to** ... | It's important to start slowly. |\n| It's **cheap / expensive to** ... | It's cheap to play. |\n| It's **fun / boring to** ... | It's fun to play with friends. |\n\n**Kişiyle:** It's difficult **for me to** wake up early.",
     "examples": [{"en": "I'm learning English to travel more easily.", "tr": "Daha kolay seyahat etmek için İngilizce öğreniyorum."},
                  {"en": "It's important to warm up before running.", "tr": "Koşmadan önce ısınmak önemli."},
                  {"en": "It's hard for me to sit still for long.", "tr": "Uzun süre kıpırdamadan oturmak benim için zor."}],
     "turkishNote": "\"Ekmek almak için markete gittim\" cümlesindeki \"için\" yüzünden Türkçe konuşanlar sık sık \"for to buy\" ya da \"for buying\" der. İngilizcede amaç için sadece to yeterlidir: I went to the shop to buy bread."},
    [
        mc("Hangisi doğru?", ["I went out for buy milk.", "I went out to buy milk."], 1, "Amaç → to + fiil."),
        mc("Hangisi doğru?", ["I went out for milk.", "I went out for to buy milk."], 0, "for + isim olur."),
        mc("It's ___ to learn the rules of chess.", ["easy", "easily"], 0, "It's + sıfat + to."),
        gap("I go running ___ stay fit.", ["to"], "Amaç → to."),
        gap("It's important ___ drink water when you exercise.", ["to"], "It's important to."),
        gap("It's difficult ___ me to get up early.", ["for"], "for me to."),
        gap("Why are you learning Italian? – ___ talk to my grandmother.", ["To"], "To + fiil."),
        order(["easy", "It's", "to", "learn", "but", "hard", "to", "master"], "It's easy to learn but hard to master.", "It's + sıfat + to + fiil.", "Öğrenmesi kolay ama ustalaşması zor."),
        listen("I joined a hiking club to meet new people. It's not expensive to join, and it's a great way to see the countryside.", "Konuşan kulübe neden katıldı?", ["Kilo vermek için", "Yeni insanlarla tanışmak için", "Para kazanmak için"], 1, "\"to meet new people\""),
        typ("İngilizce yazın: \"Koşmadan önce ısınmak önemli.\"", variants("It's important to warm up before running.", "It is important to warm up before running.", "It's important to warm up before you run.", "It is important to warm up before you run."), "It's important to warm up before running."),
    ],
    {"kind": "speaking", "task": speak("Bir hobiyi ya da sporu yeni başlayan birine tanıtın. Neden yapıldığını amaç bildiren to ile, zorluk ve kolaylıklarını It's easy / hard / important / cheap to ile anlatın (en az 6 cümle).",
                                       "I do yoga to relax and to improve my posture. It's easy to start. You only need a mat. It's important to listen to your body and not to push too hard. It's hard to do some of the positions at first, but it gets easier. It's not expensive to practise at home with videos. Many people do it to sleep better.",
                                       ["Amaç bildiren to (for değil)", "It's + sıfat + to", "Tavsiye ve değerlendirme"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Hatırla, dur, dene", "remember, stop ve try fiillerinin -ing ve to ile değişen anlamlarını kullanabilirim.",
    {"kind": "dialogue", "title": "Bisiklet turunda", "lines": [
        {"speaker": "Sinan", "text": "Did you remember to bring the water?"},
        {"speaker": "Gizem", "text": "Yes, I've got two bottles. Oh, I remember cycling here with my dad when I was little!"},
        {"speaker": "Sinan", "text": "That's nice. Shall we stop to have a rest? My legs hurt."},
        {"speaker": "Gizem", "text": "OK. You should stop eating so much chocolate before cycling!"},
        {"speaker": "Sinan", "text": "Ha ha. My chain keeps making a noise. I've tried to fix it, but it's still noisy."},
        {"speaker": "Gizem", "text": "Try putting some oil on it. That usually works."}],
     "questions": [
        mc("What did Gizem remember from her childhood?", ["Swimming with her mum", "Cycling there with her dad", "Eating chocolate"], 1, "\"I remember cycling here with my dad\""),
        mc("What does Gizem suggest for the chain?", ["Buying a new bike", "Putting some oil on it", "Cycling faster"], 1, "\"Try putting some oil on it.\""),
     ]},
    {"explanation": "Bazı fiillerden sonra hem **-ing** hem **to** gelebilir, ama **anlam değişir**:\n\n| Fiil | + to | + -ing |\n|---|---|---|\n| **remember** | yapmayı **unutmamak** (önce hatırla, sonra yap) | yaptığını **hatırlamak** (anı) |\n| | Remember **to bring** water. | I remember **cycling** here as a child. |\n| **forget** | yapmayı **unutmak** | yaptığını **unutmak** (çoğunlukla \"I'll never forget\") |\n| | I forgot **to lock** the door. | I'll never forget **meeting** her. |\n| **stop** | bir şey **yapmak için durmak** | bir şeyi **yapmayı bırakmak** |\n| | We stopped **to have** a rest. | Stop **eating** chocolate! |\n| **try** | **çabalamak** (zor bir şey) | **denemek** (çözüm olarak) |\n| | I tried **to fix** it, but I couldn't. | Try **putting** some oil on it. |\n\n**İpucu:** remember / forget + **to** → gelecekteki görev; + **-ing** → geçmişteki anı.",
     "examples": [{"en": "Please remember to turn off the lights.", "tr": "Lütfen ışıkları kapatmayı unutma."},
                  {"en": "I'll never forget seeing the sea for the first time.", "tr": "Denizi ilk kez gördüğümü asla unutmayacağım."},
                  {"en": "He stopped to answer his phone.", "tr": "Telefonunu açmak için durdu."}],
     "turkishNote": "\"Sigarayı bıraktı\" ile \"Sigara içmek için durdu\" Türkçede çok farklı cümlelerdir; İngilizcede ikisi de stop ile kurulur: He stopped smoking (bıraktı) / He stopped to smoke (sigara içmek için durdu). Anlamı belirleyen, stop'tan sonraki -ing ya da to'dur."},
    [
        mc("\"Sigarayı bıraktı.\"", ["He stopped to smoke.", "He stopped smoking."], 1, "stop + -ing = bırakmak."),
        mc("\"Benzin almak için durduk.\"", ["We stopped to get petrol.", "We stopped getting petrol."], 0, "stop + to = ... için durmak."),
        mc("\"Kapıyı kilitlemeyi unuttum.\"", ["I forgot locking the door.", "I forgot to lock the door."], 1, "forget + to = görevi unutmak."),
        mc("\"Çocukken burada oynadığımı hatırlıyorum.\"", ["I remember to play here as a child.", "I remember playing here as a child."], 1, "remember + -ing = anı."),
        gap("Please remember ___ (call) your grandmother.", ["to call"], "Görev → to."),
        gap("Your computer is slow? Try ___ (restart) it.", ["restarting"], "Çözüm denemek → -ing."),
        gap("I tried ___ (open) the jar, but it was too tight.", ["to open"], "Çabalamak → to."),
        gap("I'll never forget ___ (meet) my favourite singer.", ["meeting"], "Anı → -ing."),
        listen("I remember learning to ride a bike in this park. My dad tried to hold the bike, but I kept falling! In the end, he told me to stop looking at my feet.", "Babası ona neyi bırakmasını söyledi?", ["Ayaklarına bakmayı", "Hızlı sürmeyi", "Ağlamayı"], 0, "\"stop looking at my feet\""),
        typ("İngilizce yazın: \"Lütfen ışıkları kapatmayı unutma.\" (remember)", variants("Please remember to turn off the lights.", "Please remember to switch off the lights.", "Remember to turn off the lights, please.", "Remember to switch off the lights, please.", "Please remember to turn the lights off.", "Please remember to switch the lights off."), "Please remember to turn off the lights."),
    ],
    {"kind": "writing", "task": write("Bir forumda \"En sevdiğim boş zaman etkinliği\" konulu bir gönderi yazın (130–160 kelime). Etkinliği nasıl başladığınızı, neden yaptığınızı ve yeni başlayanlar için tavsiyelerinizi anlatın. enjoy / can't stand + -ing, decide / want + to, edat + -ing, amaç bildiren to, It's easy / important to ve remember / stop / try'dan en az birini doğru kullanın.",
                                      "My favourite free-time activity is photography. I took it up three years ago after I found my grandfather's old camera. I remember taking my first photo with it. It was a picture of a cat on a wall, and it was terrible!\n\nI enjoy walking around the city to find interesting people and places. I'm especially interested in taking photos of old buildings. I can't stand using filters; I prefer natural colours.\n\nLast year I decided to join a photography club to learn from other people, and it was the best decision.\n\nIf you want to start, here's my advice. It's easy to take photos with your phone, so you don't need an expensive camera. It's important to practise every day. Try looking at the light before you take a photo. And remember to stop worrying about perfect photos. Just have fun!",
                                      ["-ing / to doğru seçimi", "Edat + -ing", "Amaç bildiren to", "remember / stop / try anlamı", "Forum üslubu ve düzen"])},
)

u.test([
    mc("Hangisi doğru?", ["I enjoy to read.", "I enjoy reading."], 1, "enjoy + -ing"),
    mc("I've decided ___ a new language.", ["learning", "to learn"], 1, "decide + to"),
    mc("I'm good at ___.", ["cook", "cooking"], 1, "at + -ing"),
    mc("Hangisi doğru?", ["I'm looking forward to hear from you.", "I'm looking forward to hearing from you."], 1, "look forward to + -ing"),
    mc("Amaç: \"I went to the library ___ a book.\"", ["for borrow", "to borrow", "for borrowing"], 1, "to + fiil"),
    gap("___ (swim) is my favourite sport.", ["Swimming"], "Özne → -ing"),
    gap("He refused ___ (pay) the bill.", ["to pay"], "refuse + to"),
    gap("I don't mind ___ (work) at weekends.", ["working"], "mind + -ing"),
    gap("It's important ___ sleep eight hours.", ["to"], "It's important to"),
    gap("How about ___ (go) for a walk?", ["going"], "How about + -ing"),
    mc("\"Sigarayı bıraktım.\"", ["I stopped to smoke.", "I stopped smoking."], 1, "stop + -ing"),
    mc("\"Ekmek almayı unuttum.\"", ["I forgot to buy bread.", "I forgot buying bread."], 0, "forget + to"),
    listen("I've always wanted to learn to paint. Last month I finally managed to find a class near my office. It's hard to paint well, but I really enjoy trying.", "Konuşan geçen ay neyi başardı?", ["Bir resim satmayı", "Ofisine yakın bir kurs bulmayı", "Bir sergi açmayı"], 1, "\"I finally managed to find a class near my office\""),
    typ("İngilizce yazın: \"Tenise başlamayı düşünüyorum.\"", variants("I'm thinking about taking up tennis.", "I am thinking about taking up tennis.", "I'm thinking of taking up tennis.", "I'm thinking about starting tennis.", "I'm thinking of starting tennis.", "I'm thinking about playing tennis.", "I'm thinking of playing tennis."), "I'm thinking about taking up tennis."),
    write("Bir arkadaşınıza, yeni başladığınız bir hobiyi anlatan ve onu da katılmaya davet eden bir e-posta yazın (120–150 kelime). -ing ve to + fiil yapılarını çeşitli fiillerle doğru kullanın; edat + -ing, amaç bildiren to ve It's + sıfat + to ekleyin.",
          "Hi Selin,\n\nGuess what? I've taken up rock climbing! I decided to try it after I watched a documentary about it. I wanted to do something different, because I was tired of sitting at home every evening.\n\nThere's a climbing centre near my office, and I go there twice a week to practise. At first I was afraid of falling, but the instructors are great. It's not difficult to learn the basics, and it's a fantastic way to get fit. I really enjoy solving the routes; it's like a puzzle!\n\nWhy don't you come with me next Thursday? You don't need to buy anything, because you can rent shoes there. Remember to wear comfortable clothes. I'm sure you'll love it.\n\nI'm looking forward to hearing from you!\n\nLove,\nDuygu",
          ["-ing / to doğru", "Edat + -ing", "Amaç bildiren to", "It's + sıfat + to", "Davet ve e-posta üslubu"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

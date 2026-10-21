"""C2 Ünite 1: Üslup ustalığı."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("C2", 1, "Üslup ustalığı", "Stylistic Mastery",
         "Öne alma (fronting), yer ve yön bildiren devrik yapılar, Such was / So great was gibi ileri vurgu yapıları, Were it not for / Had it not been for gibi şart devriklikleri ve Be that as it may gibi kalıplaşmış dilek kipi ifadelerini anlayıp yerinde kullanabilir, cümle çeşitliliği ve ritimle etkileyici bir metin yazabilirim.",
         ["öne alma: Tired as she was / Strange though it may seem", "yer ve yön devrikliği: In the corner stood ... / Down came ...", "ileri vurgu: Such was ..., So great was ..., Nowhere / On no account", "Were it not for / Had it not been for ve kalıplaşmış dilek kipi", "cümle çeşitliliği ve ritim"],
         ["edebiyat", "konuşma sanatı", "köşe yazıları"],
         {"title": "Aynı cümle, beş ses", "durationMinutes": 45,
          "goal": "Öğretmen sade bir paragraf verir (örneğin bir şehirde yaşanan büyük bir fırtına). Gruplar paragrafı önce bir roman sahnesi (yer devrikliği, öne alma), sonra bir anma konuşması (Such was ..., Never before ..., Come what may) olarak yeniden yazar ve okur. Sınıf her versiyonda hangi yapının en etkili olduğunu tartışır ve aşırı kullanımın etkisini değerlendirir."})

u.vocab([
    ("fronting", "öne alma", "Fronting puts important information first.", "Öne alma, önemli bilgiyi başa koyar.", None),
    ("stylistic", "üslupla ilgili", "The change is purely stylistic.", "Değişiklik tamamen üslupla ilgili.", None),
    ("Tired as she was, ...", "Ne kadar yorgun olsa da ...", "Tired as she was, she kept working.", "Ne kadar yorgun olsa da çalışmaya devam etti.", None),
    ("Strange though it may seem, ...", "Garip görünse de ...", "Strange though it may seem, I enjoy the rain.", "Garip görünse de yağmurdan hoşlanırım.", None),
    ("Much as I ..., ...", "Ne kadar ... -sam da", "Much as I like him, I can't agree.", "Onu ne kadar sevsem de katılamam.", None),
    ("Such was ...", "O kadar ... idi ki", "Such was the noise that nobody could sleep.", "Gürültü o kadar fazlaydı ki kimse uyuyamadı.", None),
    ("So great was ...", "O kadar büyüktü ki", "So great was the demand that tickets sold out.", "Talep o kadar büyüktü ki biletler tükendi.", None),
    ("Nowhere ...", "Hiçbir yerde ...", "Nowhere have I seen such beauty.", "Hiçbir yerde böyle bir güzellik görmedim.", None),
    ("On no account", "hiçbir surette", "On no account should you open this door.", "Bu kapıyı hiçbir surette açmamalısın.", None),
    ("Not once", "bir kez bile", "Not once did she complain.", "Bir kez bile şikâyet etmedi.", None),
    ("Were it not for ...", "... olmasaydı", "Were it not for your help, I would fail.", "Yardımın olmasaydı başarısız olurdum.", None),
    ("Had it not been for ...", "... olmasaydı (geçmiş)", "Had it not been for the rain, we would have won.", "Yağmur olmasaydı kazanırdık.", None),
    ("Be that as it may, ...", "Her ne olursa olsun, yine de", "Be that as it may, we must decide today.", "Her ne olursa olsun bugün karar vermeliyiz.", None),
    ("Come what may, ...", "Ne olursa olsun", "Come what may, I'll be there.", "Ne olursa olsun orada olacağım.", None),
    ("Suffice it to say ...", "Şu kadarını söyleyeyim ki", "Suffice it to say, he wasn't pleased.", "Şu kadarını söyleyeyim, memnun değildi.", None),
    ("Far be it from me to ...", "-mek bana düşmez ama", "Far be it from me to criticise, but ...", "Eleştirmek bana düşmez ama ...", None),
    ("If need be", "gerekirse", "I'll work all night if need be.", "Gerekirse bütün gece çalışırım.", None),
    ("So be it.", "Öyle olsun.", "If that's your decision, so be it.", "Kararın buysa öyle olsun.", None),
    ("rhythm", "ritim", "Varying sentence length improves rhythm.", "Cümle uzunluğunu değiştirmek ritmi iyileştirir.", None),
    ("rhetorical effect", "retorik etki", "Inversion is used for rhetorical effect.", "Devrik yapı retorik etki için kullanılır.", None),
    ("overwrought", "aşırı süslü, abartılı", "The style is rather overwrought.", "Üslup biraz abartılı.", None),
    ("understated", "sade, abartısız", "Her writing is elegant and understated.", "Onun yazısı zarif ve sade.", None),
    ("cadence", "ahenk, ritim (konuşma)", "The speech had a beautiful cadence.", "Konuşmanın güzel bir ahengi vardı.", None),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Öne alma (fronting)", "Sıfat, zarf ya da nesneyi cümle başına alarak (Tired as she was, Strange though it may seem, This I cannot accept) vurgu ve üslup katabilirim.",
    {"kind": "text", "title": "Bir romandan", "body": "Exhausted as she was, Nehir refused to stop. The last train had long gone, and the city was silent. Strange though it may seem, she felt no fear, only a quiet determination. The letter she had promised to deliver was still in her coat pocket. That letter she would deliver, whatever it cost. Much as she wanted to sleep, she knew that by morning it would be too late. So she walked on, through the empty streets, towards the old harbour.",
     "questions": [
        mc("How did Nehir feel?", ["Frightened and confused", "Exhausted but determined", "Happy and relaxed"], 1, "\"Exhausted as she was\" ... \"quiet determination\""),
        mc("Why couldn't she wait until morning?", ["The harbour would close.", "It would be too late to deliver the letter.", "She had to catch a train."], 1, "\"by morning it would be too late\""),
     ]},
    {"explanation": "**Öne alma (fronting),** normalde cümlenin sonunda olan bir öğeyi başa taşıyarak **vurgu** ya da **bağlam** oluşturmaktır.\n\n**1. Sıfat / zarf + as / though + özne + fiil (= Although ...):**\n\n| Normal | Öne alınmış |\n|---|---|\n| Although she was exhausted, ... | **Exhausted as / though she was**, ... |\n| Although it may seem strange, ... | **Strange though / as it may seem**, ... |\n| Although he tried hard, ... | **Hard as he tried**, ... |\n| Although I like him a lot, ... | **Much as I like him**, ... |\n\n**Dikkat:**\n\n- Öne alınan sıfattan önce **a / an** kullanılmaz: ✓ *Brilliant scientist though he was*.\n- Bu yapıda **as**, \"çünkü\" değil **\"-e rağmen\"** anlamındadır!\n- *Much as* özellikle *like, love, admire, want, hate* ile kullanılır.\n\n**2. Nesneyi öne alma (object fronting):** Konuşmada ve edebiyatta güçlü vurgu ya da karşıtlık için.\n\n- ***That letter** she would deliver, whatever it cost.*\n- ***This** I cannot accept.*\n- ***What he did next**, nobody could have predicted.*\n- *Some of the songs I loved; **others** I couldn't stand.*\n\n**3. Tamamlayıcıyı öne alma:**\n\n- ***Gone** are the days when ...* (... günler geride kaldı)\n- ***Equally important** is the question of cost.*\n- ***More worrying** is the lack of evidence.*\n\nBu son yapılarda **özne ile fiil yer değiştirir** (devrik).",
     "examples": [{"en": "Hard as he tried, he couldn't remember her name.", "tr": "Ne kadar uğraşsa da adını hatırlayamadı."},
                  {"en": "Gone are the days when a letter took weeks to arrive.", "tr": "Bir mektubun haftalarca sürdüğü günler geride kaldı."},
                  {"en": "More worrying is the fact that nobody noticed.", "tr": "Daha endişe verici olan, kimsenin fark etmemiş olmasıydı."}],
     "turkishNote": "Türkçede öğe sırası esnektir ve vurgulanan öğe genellikle yüklemin hemen önüne konur (\"O mektubu teslim edecekti\" / \"Teslim edecekti o mektubu\"). İngilizcede ise öğe sırası katıdır; bu yüzden öne alma güçlü ve dikkat çekici bir üslup tercihidir. Türk öğrencilerin en sık karıştırdığı nokta, \"Tired as she was\" yapısındaki \"as\"in \"çünkü\" değil \"-e rağmen\" anlamına gelmesidir. Türkçedeki \"Ne kadar yorgun olsa da\" yapısıyla eşleştirin."},
    [
        mc("\"Tired as she was, she kept going.\" anlamı:", ["Yorgun olduğu için devam etti.", "Ne kadar yorgun olsa da devam etti."], 1, "as = -e rağmen."),
        mc("Doğru olan:", ["Much as I admire her, I disagree.", "Much I admire her, I disagree."], 0, "Much as."),
        mc("\"Gone are the days ...\" anlamı:", ["Günler gitti, yorgunum.", "... günler geride kaldı."], 1, "Gone are the days."),
        mc("Doğru devrik yapı:", ["More worrying is the cost.", "More worrying the cost is."], 0, "Tamamlayıcı + fiil + özne."),
        gap("___ though it may sound, I've never seen the sea. (Garip)", ["Strange"], "Strange though it may sound."),
        gap("Hard ___ he tried, he couldn't open the box.", ["as", "though"], "Hard as he tried."),
        gap("___ as I love my job, I need a holiday.", ["Much"], "Much as."),
        gap("___ are the days when people wrote letters by hand. (geride kalmış)", ["Gone"], "Gone are the days."),
        listen("Brilliant though the plan was, it had one serious flaw: nobody had asked the residents what they wanted. Equally important was the question of cost, which the council had barely considered.", "Planın ciddi kusuru neydi?", ["Çok pahalıydı.", "Kimse sakinlere ne istediklerini sormamıştı.", "Çok geç başlamıştı."], 1, "\"nobody had asked the residents what they wanted\""),
        typ("Öne alın (as ile): \"Although he was rich, he lived simply.\"", variants("Rich as he was, he lived simply.", "Rich though he was, he lived simply.", "Rich as he was he lived simply."), "Rich as he was, he lived simply."),
    ],
    {"kind": "speaking", "task": speak("Zor bir dönemde azimle bir şey başardığınız bir deneyimi (sınav, spor, iş, taşınma) kısa ve etkileyici bir hikâye olarak anlatın (1 dakika). En az 3 öne alma yapısı kullanın: Tired / Hard / Much as ..., Strange though it may seem, Gone are the days ..., That I would never forget, More surprising was ...",
                                       "Three years ago, I decided to run my first half-marathon. Busy as I was with work, I trained every morning at six. Hard as I tried, I couldn't get faster than twelve kilometres an hour, and I nearly gave up. Strange though it may seem, it was a stranger who changed everything. An older runner saw me struggling one day and gave me a simple tip about breathing. That advice I will never forget. On race day, I finished in just under two hours. More surprising than my time was how happy I felt. Gone are the days when I thought I wasn't a sporty person.",
                                       ["Öne alma yapıları", "Doğru anlam (as = -e rağmen)", "Hikâye anlatımı", "Vurgu ve tonlama"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "Yer ve yön devrikliği", "Edebi ve betimleyici metinlerde yer, yön ve hareket bildiren ifadelerle devrik yapıyı (In the corner stood a piano / Down came the rain / Here comes the bus) anlayıp kullanabilirim.",
    {"kind": "text", "title": "Bir öyküden", "body": "At the end of the narrow street stood an old stone house. Above the door hung a rusty lantern, swinging gently in the wind. Inside, the air was cold. In the corner sat an old man, wrapped in a blanket, staring at the fire. On the table lay a pile of yellowed letters. Suddenly, there was a crash of thunder, and down came the rain. The door flew open, and in rushed a young woman, soaking wet. \"There you are!\" said the old man. \"I've been waiting for you.\"",
     "questions": [
        mc("What was on the table?", ["A lantern", "A pile of old letters", "A blanket"], 1, "\"On the table lay a pile of yellowed letters.\""),
        mc("What happened when the rain started?", ["The old man left.", "A young woman rushed in.", "The fire went out."], 1, "\"in rushed a young woman, soaking wet\""),
     ]},
    {"explanation": "**Yer / yön devrikliği (locative inversion),** edebi ve betimleyici metinlerde, okuyucunun dikkatini önce **mekâna**, sonra **özneye** çekmek için kullanılır.\n\n**Yapı:** Yer / yön ifadesi + **fiil** + özne\n\n**1. Yer ifadeleriyle (durum fiilleri: stand, sit, lie, hang, live):**\n\n| Normal | Devrik |\n|---|---|\n| An old house stood at the end of the street. | **At the end of the street stood** an old house. |\n| A lantern hung above the door. | **Above the door hung** a lantern. |\n| A pile of letters lay on the table. | **On the table lay** a pile of letters. |\n\n**2. Yön zarflarıyla (hareket fiilleri: come, go, run, fly, rush):**\n\n| Normal | Devrik |\n|---|---|\n| The rain came down. | **Down came** the rain. |\n| A young woman rushed in. | **In rushed** a young woman. |\n| The balloon went up. | **Up went** the balloon. |\n\n**3. Here / There ile (konuşmada çok yaygın):**\n\n- ***Here comes** the bus!*\n- ***There goes** my last chance.*\n- ***Here's** your coffee.*\n\n**Önemli kural: Özne zamir ise devrik yapılmaz!**\n\n| İsim özne | Zamir özne |\n|---|---|\n| ✓ *Here comes **the bus**.* | ✓ *Here **it comes**.* (✗ *Here comes it.*) |\n| ✓ *Down came **the rain**.* | ✓ *Down **it came**.* |\n| ✓ *There goes **Ali**.* | ✓ *There **he goes**.* |\n\n**Not:** Bu yapı genellikle yardımcı fiil olmadan, **basit geçmiş** ya da **geniş zamanla** kullanılır.",
     "examples": [{"en": "In the middle of the garden stood a huge oak tree.", "tr": "Bahçenin ortasında kocaman bir meşe ağacı duruyordu."},
                  {"en": "Out jumped a small black cat.", "tr": "Dışarı küçük siyah bir kedi fırladı."},
                  {"en": "Here comes the bride!", "tr": "İşte gelin geliyor!"}],
     "turkishNote": "Türkçede yer ifadesini başa almak çok doğaldır: \"Sokağın sonunda eski bir ev vardı.\" Bu nedenle İngilizce yer devrikliği Türk öğrencilere mantıklı gelir. Ancak iki noktaya dikkat edin: (1) İngilizcede bu yapı edebi ve betimleyicidir; günlük yazışmalarda kullanılmaz (\"Here comes the bus\" gibi kalıplar hariç). (2) Özne zamir olduğunda devrik yapılmaz: \"Here it comes\", ✗ \"Here comes it\"."},
    [
        mc("Doğru olan:", ["Here comes it!", "Here it comes!"], 1, "Zamir özne: devrik yok."),
        mc("Doğru devrik yapı:", ["On the wall hung a painting.", "On the wall a painting hung it."], 0, "Yer + fiil + özne."),
        mc("Doğru olan:", ["Out ran the children.", "Out the children ran they."], 0, "Yön + fiil + özne."),
        mc("Bu yapı en çok nerede kullanılır?", ["İş e-postalarında", "Edebi ve betimleyici metinlerde"], 1, "Edebi."),
        gap("At the top of the hill ___ a small chapel. (durmak, geçmiş)", ["stood"], "stood."),
        gap("Down ___ the rain, and everyone ran for cover. (gelmek, geçmiş)", ["came"], "came."),
        gap("Here ___ the train. Quick, get your bags! (gelmek)", ["comes"], "Here comes."),
        gap("\"Where's the taxi?\" \"Look, here it ___!\"", ["comes"], "Here it comes."),
        listen("Behind the old library was a small courtyard. In the centre stood a fountain, and around it grew wild roses. Every afternoon, out came the same elderly couple, who sat on the bench and fed the pigeons.", "Her öğleden sonra avluya kim geliyordu?", ["Bir grup öğrenci", "Aynı yaşlı çift", "Kütüphaneci"], 1, "\"out came the same elderly couple\""),
        typ("Devrik yapın: \"A small boat lay on the beach.\" (On the beach ...)", variants("On the beach lay a small boat."), "On the beach lay a small boat."),
    ],
    {"kind": "speaking", "task": speak("Gözlerinizi kapatın ve çok sevdiğiniz bir yeri (çocukluk eviniz, bir kafe, bir köy meydanı) hayal edin. Bu yeri bir romanın açılış sahnesi gibi betimleyin (1 dakika). En az 4 yer devrikliği (In the corner stood ..., On the wall hung ..., Above the door ...) ve en az 1 yön devrikliği (In came ..., Out ran ..., Down came ...) kullanın.",
                                       "At the end of a narrow street in my grandparents' village stood a small white house. Above the blue door hung a basket of red geraniums. Inside, the kitchen smelled of fresh bread. In the corner stood an old wooden cupboard, full of my grandmother's jars of jam. On the wall hung a black-and-white photograph of my grandparents on their wedding day. Every evening at six, in came my grandfather from the fields, with mud on his boots and a huge smile on his face. And out ran all of us children to greet him.",
                                       ["Yer devrikliği", "Yön devrikliği", "Zamir kuralı", "Betimleyici ve edebi ton"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "İleri vurgu yapıları", "Such was ..., So great was ..., Nowhere ..., Not once ..., On no account ..., In no way ... gibi ileri devrik vurgu yapılarını resmî konuşma ve yazıda kullanabilirim.",
    {"kind": "text", "title": "Bir anma konuşmasından", "body": "Such was her dedication to her students that she rarely left the school before eight in the evening. So great was her influence that many of them became teachers themselves. Not once in forty years did she miss a day of work. Nowhere else have I met a person so generous with her time. On no account would she accept praise; she always insisted that the credit belonged to her students. In no way can words express how much we will miss her.",
     "questions": [
        mc("How long did the teacher work?", ["Twenty years", "Forty years", "Eight years"], 1, "\"Not once in forty years\""),
        mc("How did she react to praise?", ["She enjoyed it.", "She refused to accept it.", "She asked for more."], 1, "\"On no account would she accept praise\""),
     ]},
    {"explanation": "C1 Ünite 1'de *Never, Rarely, Not only, No sooner, Little did* gibi devrik yapıları gördük. C2'de daha ileri ve resmî yapılara geçiyoruz.\n\n**1. Such was / were + isim + that ...:** (O kadar ... idi ki)\n\n| Normal | Devrik |\n|---|---|\n| Her dedication was so great that ... | **Such was her dedication that** ... |\n| The crowds were so large that ... | **Such were the crowds that** ... |\n\n**2. So + sıfat + was / were + özne + that ...:**\n\n| Normal | Devrik |\n|---|---|\n| The demand was so great that ... | **So great was the demand that** ... |\n| He was so tired that ... | **So tired was he that** ... |\n\n**3. Olumsuz ve kısıtlayıcı ifadelerle devrik yapı:**\n\n| İfade | Örnek |\n|---|---|\n| **Nowhere** | **Nowhere** else **have I** met such a person. |\n| **Not once** | **Not once did** she complain. |\n| **On no account** | **On no account should** you leave. |\n| **In no way** | **In no way can** words express ... |\n| **At no time** | **At no time was** the public in danger. |\n| **Under no circumstances** | **Under no circumstances will** we accept late work. |\n| **Only then** | **Only then did** I understand. |\n| **Not a single ...** | **Not a single word did** he say. |\n\n**Kural:** Bu ifadelerden sonra soru düzeni gelir: **yardımcı fiil + özne + ana fiil**. Yardımcı fiil yoksa **do / does / did** eklenir.\n\n**Kullanım:** Resmî konuşma, anma, haber, edebi metin. Günlük konuşmada **abartılı** gelir.",
     "examples": [{"en": "Such was the noise that we couldn't hear ourselves think.", "tr": "Gürültü o kadar fazlaydı ki kendi düşüncemizi bile duyamıyorduk."},
                  {"en": "At no time was the public in any danger.", "tr": "Halk hiçbir zaman tehlikede değildi."},
                  {"en": "Not a single word did he say all evening.", "tr": "Bütün akşam tek bir kelime bile etmedi."}],
     "turkishNote": "Türkçede vurgu genellikle \"o kadar ... ki\", \"hiçbir surette\", \"bir kez bile\" gibi ifadelerle ve tonlamayla yapılır, cümle yapısı değişmez. İngilizcede ise bu ifadeler başa geldiğinde soru düzeni zorunludur. Türk öğrencilerin sık yaptığı hata, devrik yapıyı unutmaktır: ✗ \"Not once she complained.\" ✓ \"Not once did she complain.\" Ayrıca \"Such was\" ile \"So + sıfat + was\" yapısını karıştırmayın: Such + isim, So + sıfat."},
    [
        mc("Doğru olan:", ["Not once she complained.", "Not once did she complain."], 1, "Devrik."),
        mc("Doğru olan:", ["Such was the demand that ...", "So was the demand great that ..."], 0, "Such + isim."),
        mc("Doğru olan:", ["So tired was he that he fell asleep.", "Such tired was he that he fell asleep."], 0, "So + sıfat."),
        mc("Doğru olan:", ["At no time the public was in danger.", "At no time was the public in danger."], 1, "Devrik."),
        gap("___ was the heat that the roads began to melt. (O kadar)", ["Such"], "Such was."),
        gap("So ___ was the crowd that the police closed the street. (büyük)", ["large", "big", "great"], "So + sıfat."),
        gap("Nowhere else ___ I seen such a beautiful sunset.", ["have"], "Nowhere else have I."),
        gap("On no account ___ you share your password with anyone.", ["should", "must"], "On no account should."),
        listen("Ladies and gentlemen, I want to reassure you. At no time were passengers in any danger. Such was the skill of the crew that the plane landed safely within minutes. On no account should anyone panic. Updates will follow shortly.", "Konuşmanın amacı nedir?", ["Yolcuları korkutmak", "Yolcuları rahatlatmak", "Uçuşu iptal etmek"], 1, "\"I want to reassure you\""),
        typ("Devrik yapın (Such was ...): \"Her talent was so great that she won every competition.\"", variants("Such was her talent that she won every competition.", "Such was her talent, that she won every competition."), "Such was her talent that she won every competition."),
    ],
    {"kind": "speaking", "task": speak("Hayatınızda önemli bir yeri olan bir kişiyi (öğretmen, aile büyüğü, bir lider) onurlandıran kısa bir resmî konuşma yapın (1 dakika). En az 5 ileri vurgu yapısı kullanın: Such was ..., So great / generous was ..., Not once did ..., Nowhere else have I ..., In no way can ..., Only then did I ..., At no time ...",
                                       "Today, I would like to pay tribute to my grandfather, who passed away last year. Such was his kindness that our door was always open to neighbours in need. So generous was he that he often gave away more than he could afford. Not once did I hear him speak badly of anyone. Nowhere else have I met a person who listened so patiently. When I was young, I didn't understand his quiet strength. Only later did I realise how much he had taught me. In no way can these few words do justice to the man he was, but I hope they remind us of how he lived.",
                                       ["İleri devrik yapılar", "Such / So doğru", "Resmî ve duygusal ton", "Ritim ve tonlama"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Şart devrikliği ve kalıplaşmış dilek kipi", "Were it not for / Had it not been for gibi şart devriklikleri ve Be that as it may, Come what may, Suffice it to say, Far be it from me gibi kalıplaşmış dilek kipi (subjunctive) ifadelerini yerinde kullanabilirim.",
    {"kind": "text", "title": "Bir yöneticinin mektubundan", "body": "Dear team,\n\nWere it not for your hard work this year, we would not be celebrating our best results in a decade. Had it not been for your patience during the difficult spring months, many of our clients would have left us.\n\nI am aware that some of you have concerns about the planned reorganisation. Be that as it may, I believe it is the right decision for the company's future. Far be it from me to pretend that change is easy, but I am confident that, come what may, we will face it together.\n\nSuffice it to say that I am extremely proud of what we have achieved. If need be, I will meet each of you individually to discuss your concerns.\n\nWith warm regards,\nDefne Arslan, Managing Director",
     "questions": [
        mc("Why does the director thank the team?", ["For the best results in a decade", "For accepting lower salaries", "For finding new clients"], 0, "\"best results in a decade\""),
        mc("What does the director offer to do?", ["Cancel the reorganisation", "Meet each person individually if necessary", "Give everyone a bonus"], 1, "\"If need be, I will meet each of you individually\""),
     ]},
    {"explanation": "**1. Were it not for / Had it not been for (= If it weren't for / If it hadn't been for):**\n\n| Normal | Devrik (resmî) | Zaman |\n|---|---|---|\n| If it weren't for your help, I would fail. | **Were it not for** your help, I would fail. | şimdi |\n| If it hadn't been for the rain, we would have won. | **Had it not been for** the rain, we would have won. | geçmiş |\n| If it hadn't been for you, I would be lost now. | **Had it not been for** you, I would be lost now. | karışık |\n\n**Not:** *But for* (C1 Ünite 3) de aynı anlamdadır ve daha kısadır: *But for your help, ...*\n\n**2. Kalıplaşmış dilek kipi (formulaic subjunctive):** Fiilin yalın hali (*be, come, suffice*) kullanılan, eski İngilizceden kalma sabit ifadeler.\n\n| İfade | Anlam | Örnek |\n|---|---|---|\n| **Be that as it may, ...** | Her ne olursa olsun, yine de | **Be that as it may**, we must decide today. |\n| **Come what may, ...** | Ne olursa olsun | **Come what may**, I'll support you. |\n| **Suffice it to say (that) ...** | Şu kadarını söyleyeyim ki | **Suffice it to say** he wasn't happy. |\n| **Far be it from me to ...** | -mek bana düşmez ama | **Far be it from me to** criticise, but ... |\n| **If need be, ...** | Gerekirse | I'll stay late **if need be**. |\n| **So be it.** | Öyle olsun. | If that's what you want, **so be it**. |\n| **God / Heaven forbid!** | Allah korusun! | **Heaven forbid** anything should go wrong. |\n| **Long live ...!** | Çok yaşa ...! | **Long live** the king! |\n\n**Not:** *Far be it from me to ...* genellikle tam da \"bana düşmez\" dediğiniz şeyi yapacağınızı gösterir (ironik): *Far be it from me to tell you what to do, but ...*\n\n**3. Önceden gördüğümüz dilek kipi (B2):** *I suggest that he **be** informed. It is essential that she **attend**.*",
     "examples": [{"en": "Were it not for the internet, I would never have met my best friend.", "tr": "İnternet olmasaydı en iyi arkadaşımla asla tanışmazdım."},
                  {"en": "Far be it from me to interfere, but are you sure that's a good idea?", "tr": "Karışmak bana düşmez ama bunun iyi bir fikir olduğundan emin misin?"},
                  {"en": "Suffice it to say that the meeting did not go well.", "tr": "Şu kadarını söyleyeyim ki toplantı iyi geçmedi."}],
     "turkishNote": "Bu kalıpların çoğunun Türkçede de sabit karşılıkları vardır: \"Ne olursa olsun\" (Come what may), \"Allah korusun\" (Heaven forbid), \"Öyle olsun\" (So be it). Bu ifadeler kalıplaşmış oldukları için kelimeleri değiştirilmez: ✗ \"Comes what may\", ✗ \"Be it that as it may\". Türk öğrencilerin dikkat etmesi gereken bir nokta, \"Far be it from me\" ifadesinin genellikle ironik kullanıldığıdır: \"Karışmak bana düşmez ama...\" deyip aslında karışmak gibi."},
    [
        mc("\"Were it not for your help\" anlamı:", ["Yardımın olmasaydı", "Yardımın olduğu için"], 0, "If it weren't for."),
        mc("Geçmiş zaman için doğru:", ["Were it not for the storm, we would have arrived.", "Had it not been for the storm, we would have arrived."], 1, "Had it not been for."),
        mc("\"Come what may\" anlamı:", ["Gelecek ne olacak?", "Ne olursa olsun"], 1, "Come what may."),
        mc("\"Far be it from me to criticise, but ...\" genellikle:", ["Konuşan eleştirmeyecek.", "Konuşan aslında eleştirecek."], 1, "İronik."),
        gap("___ it not for her support, I would give up.", ["Were"], "Were it not for."),
        gap("Had it not ___ for the map, we would have got lost.", ["been"], "Had it not been for."),
        gap("___ that as it may, we still need to finish by Friday.", ["Be"], "Be that as it may."),
        gap("___ it to say, the party was a disaster. (Şu kadarını söyleyeyim)", ["Suffice"], "Suffice it to say."),
        listen("Look, I know the deadline is tight. Be that as it may, the client won't wait. We'll work through the weekend if need be. And if that means cancelling our plans, so be it. Come what may, this project goes out on Monday.", "Proje ne zaman teslim edilecek?", ["Cuma", "Pazartesi", "Hafta sonu"], 1, "\"this project goes out on Monday\""),
        match([("Be that as it may", "yine de, her ne olursa olsun"), ("Come what may", "ne olursa olsun"), ("If need be", "gerekirse"), ("So be it", "öyle olsun"), ("Suffice it to say", "şu kadarını söyleyeyim ki")], "Her kalıbı anlamıyla eşleştirin."),
    ],
    {"kind": "speaking", "task": speak("Ekibinize zor bir kararı açıklayan kısa bir konuşma yapın (örneğin bir projenin ertelenmesi ya da yeni bir çalışma düzeni) (1 dakika). Were it not for / Had it not been for yapılarından birini ve en az 3 kalıplaşmış ifadeyi (Be that as it may, Come what may, Suffice it to say, Far be it from me, If need be, So be it) kullanın.",
                                       "Good morning, everyone. I'll be brief. Had it not been for the problems with our supplier, we would have launched the new product next month. Unfortunately, that is no longer possible. Suffice it to say that we've done everything we can to avoid a delay. I know many of you are disappointed, and I understand why. Be that as it may, launching a product that isn't ready would damage our reputation. Far be it from me to promise that the next few weeks will be easy, but we'll get through them. If need be, we'll bring in extra help. Come what may, we will launch in the spring.",
                                       ["Şart devrikliği", "Kalıplaşmış ifadeler doğru", "Resmî ve güven veren ton", "Akıcılık"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Cümle çeşitliliği ve ritim", "Kısa ve uzun cümleleri, öne almayı, devrik yapıları ve kalıplaşmış ifadeleri bilinçli ve ölçülü kullanarak etkileyici ve ritmik bir metin yazabilirim.",
    {"kind": "text", "title": "İki versiyon", "body": "Version A:\n\"The storm arrived at night. The storm was very strong. Many trees fell down. The electricity went off. People were scared. The next morning, the city was very quiet. Many streets were closed. The damage was very bad. People started to clean up.\"\n\nVersion B:\n\"The storm arrived at night. Such was its force that trees that had stood for a century were torn from the ground, and, one by one, the lights of the city went out. Nobody slept. By morning, an eerie silence had fallen over the streets. Gone were the cars, the buses, the usual morning noise. In their place lay broken branches and shattered glass. Shocked as they were, people began, slowly, to clean up.\"",
     "questions": [
        mc("Which version is more effective?", ["Version A", "Version B"], 1, "Çeşitli cümleler ve yapılar."),
        mc("What replaced the usual morning noise?", ["Music", "An eerie silence", "Thunder"], 1, "\"an eerie silence had fallen over the streets\""),
     ]},
    {"explanation": "C2 seviyesinde iyi bir yazar sadece doğru değil, **etkileyici** yazar. Bunun anahtarı **çeşitlilik** ve **ritimdir**.\n\n**Version A neden zayıf?**\n\n- Bütün cümleler aynı uzunlukta ve aynı yapıda (Özne + Fiil)\n- Tekrar: *The storm ..., The storm ...*\n- Zayıf sıfatlar: *very strong, very bad*\n\n**Version B neden güçlü?**\n\n| Araç | Örnek |\n|---|---|\n| **Kısa cümle (vurgu)** | *Nobody slept.* |\n| **Uzun, akan cümle** | *Such was its force that trees ... were torn from the ground, and, one by one, ...* |\n| **İleri vurgu** | *Such was its force that ...* |\n| **Tamamlayıcıyı öne alma** | *Gone were the cars, ...* |\n| **Yer devrikliği** | *In their place lay broken branches ...* |\n| **Sıfat öne alma** | *Shocked as they were, ...* |\n| **Güçlü kelimeler** | *torn, eerie, shattered* (very strong / very bad yerine) |\n| **Üçleme (triplet)** | *the cars, the buses, the usual morning noise* |\n\n**Ritim için ipuçları:**\n\n1. **Uzun cümleden sonra kısa cümle**, vurgu yaratır.\n2. Cümleleri **farklı öğelerle** başlatın: zarf, yan cümle, öne alınmış öğe.\n3. **Üçlemeler** akılda kalır: *the cars, the buses, the noise*.\n4. **very + sıfat** yerine güçlü tek kelimeler: *very bad → devastating*, *very quiet → silent*.\n\n**Ölçü önemli!** Bu ünitedeki yapılar **tuz gibidir**: az kullanıldığında lezzet katar, çok kullanıldığında metni **overwrought** (abartılı, aşırı süslü) yapar. Bir paragrafta 1–2 devrik yapı genellikle yeterlidir.",
     "examples": [{"en": "The meeting lasted six hours. Nothing was decided.", "tr": "Toplantı altı saat sürdü. Hiçbir şeye karar verilmedi."},
                  {"en": "Gone were the crowds, the music, the laughter.", "tr": "Kalabalık, müzik, kahkahalar geride kalmıştı."},
                  {"en": "Her style is elegant and understated.", "tr": "Onun üslubu zarif ve sade."}],
     "turkishNote": "Türkçe yazıda uzun ve çok yan cümleli yapılar yaygındır, bazen tek bir cümle bir paragraf kadar uzun olabilir. İngilizce yazıda ise ritim için kısa ve uzun cümleler dengeli kullanılır; özellikle bir uzun cümleden sonra gelen çok kısa bir cümle (\"Nobody slept.\") güçlü bir etki yaratır. Türk öğrencilerin İngilizce yazılarında görülen bir başka sorun, \"very\" kelimesinin aşırı kullanımıdır. C2 seviyesinde \"very bad\" yerine \"devastating\", \"very tired\" yerine \"exhausted\" gibi güçlü kelimeler tercih edilir."},
    [
        mc("Hangisi daha güçlü bir ritim yaratır?", ["Bütün cümleleri aynı uzunlukta yazmak", "Uzun cümleden sonra kısa bir cümle kullanmak"], 1, "Ritim."),
        mc("\"very tired\" yerine güçlü kelime:", ["exhausted", "very very tired"], 0, "Güçlü sıfat."),
        mc("Bir paragrafta devrik yapı sayısı:", ["Mümkün olduğunca çok", "Genellikle 1–2 yeterli"], 1, "Ölçü."),
        mc("\"overwrought\" bir metin:", ["Aşırı süslü ve abartılı", "Sade ve zarif"], 0, "overwrought."),
        gap("Gone ___ the days when we could leave our doors unlocked.", ["are"], "Gone are the days."),
        gap("Such ___ the silence that we could hear our own hearts.", ["was"], "Such was."),
        gap("In the middle of the square ___ a statue of the town's founder. (durmak)", ["stood"], "stood."),
        gap("Exhausted ___ she was, she finished the race.", ["as", "though"], "Exhausted as she was."),
        listen("For years, the factory had been the heart of the town. Then, one winter, it closed. Gone were the jobs, the noise, the sense of purpose. So deep was the shock that some families left within months. Those who stayed, however, refused to give up.", "Fabrika kapandıktan sonra ne oldu?", ["Herkes kasabada kaldı ve hiçbir şey değişmedi.", "Bazı aileler kısa sürede ayrıldı ama kalanlar pes etmedi.", "Yeni bir fabrika açıldı."], 1, "\"some families left within months. Those who stayed, however, refused to give up.\""),
        typ("Güçlü kısa cümleyle bitirin: \"We had planned everything for months: the venue, the music, the food. Then it rained. ___ (Hiçbir şey planlandığı gibi gitmedi)\"", variants("Nothing went to plan.", "Nothing went according to plan.", "Nothing went as planned."), "Nothing went to plan."),
    ],
    {"kind": "writing", "task": write("Hayatınızı ya da bir topluluğu değiştiren bir olayı (bir doğal olay, bir taşınma, bir kayıp, büyük bir başarı) anlatan bir anı yazısı ya da köşe yazısı yazın (200–250 kelime). Uzun ve kısa cümleleri dengeli kullanın ve şu yapılardan en az 5 farklı türü ölçülü bir şekilde kullanın: öne alma (Tired as I was / Gone are the days), yer devrikliği, Such was / So + sıfat + was, olumsuz devrik (Not once / Nowhere / Only then), Had it not been for, kalıplaşmış ifade (Be that as it may / Come what may / Suffice it to say). very + sıfat kullanmayın.",
                                      "The Summer the River Rose\n\nI was twelve when the river burst its banks. It had been raining for nine days. On the tenth, the water came.\n\nSuch was its speed that within an hour, the ground floor of our house had disappeared. My father carried my little brother on his shoulders; my mother held my hand so tightly that it hurt. Not once did she let go. We spent the night on the roof of the school, along with half the village, wrapped in blankets and watching the dark water rise.\n\nBy morning, the rain had stopped. Gone were the gardens, the market stalls, the small wooden bridge where we used to fish. In their place lay mud, broken furniture and an extraordinary, unbearable silence.\n\nHad it not been for our neighbours, I am not sure how we would have survived the weeks that followed. Exhausted as they were, they shared food, dried each other's clothes and rebuilt each other's walls. Only then did I understand what the word \"community\" really meant.\n\nSuffice it to say that the village was never quite the same. Nowhere else have I seen people so devastated and yet so generous. Thirty years later, the river is calm. I am not. Every time it rains for more than a day, I remember the roof, the blankets, and my mother's hand.",
                                      ["En az 5 farklı ileri yapı", "Ölçülü kullanım (abartısız)", "Cümle çeşitliliği ve ritim", "Güçlü kelime seçimi", "Etkileyici giriş ve son"])},
)

u.test([
    mc("\"Tired as he was, he kept working.\" anlamı:", ["Yorgun olduğu için çalıştı.", "Ne kadar yorgun olsa da çalışmaya devam etti."], 1, "as = -e rağmen"),
    mc("Doğru olan:", ["Here comes it!", "Here it comes!"], 1, "Zamir özne"),
    mc("Doğru olan:", ["Not once she apologised.", "Not once did she apologise."], 1, "Devrik"),
    mc("Doğru olan:", ["So great was the noise that ...", "Such great was the noise that ..."], 0, "So + sıfat"),
    mc("\"Far be it from me to judge, but ...\" genellikle:", ["Konuşan yargılamayacak.", "Konuşan aslında yargılayacak."], 1, "İronik"),
    gap("___ as I like her, I can't support her plan.", ["Much"], "Much as"),
    gap("On the hill ___ an old windmill. (durmak, geçmiş)", ["stood"], "Yer devrikliği"),
    gap("___ was the crowd that the doors had to be closed.", ["Such"], "Such was"),
    gap("Nowhere else ___ I tasted such delicious bread.", ["have"], "Nowhere have I"),
    gap("Had it not ___ for the doctor, he would have died.", ["been"], "Had it not been for"),
    gap("___ that as it may, the decision is final.", ["Be"], "Be that as it may"),
    gap("___ are the days when a phone was just a phone.", ["Gone"], "Gone are the days"),
    listen("Such was the success of the first festival that the town decided to make it an annual event. Not once in the twenty years since has it been cancelled, and come what may, the organisers say, it never will be.", "Festival kaç yıldır iptal edilmedi?", ["On yıl", "Yirmi yıl", "Hiç düzenlenmedi"], 1, "\"Not once in the twenty years since\""),
    typ("Devrik yapın (Were it not for ...): \"If it weren't for my sister, I wouldn't have a job.\"", variants("Were it not for my sister, I wouldn't have a job.", "Were it not for my sister, I would not have a job.", "Were it not for my sister I wouldn't have a job."), "Were it not for my sister, I wouldn't have a job."),
    write("Bir şehrin, mahallenin ya da okulun zaman içinde nasıl değiştiğini anlatan bir köşe yazısı ya da anı yazısı yazın (200–250 kelime). Uzun ve kısa cümleleri dengeli kullanın ve en az 5 farklı ileri yapıyı ölçülü bir şekilde kullanın (öne alma, yer devrikliği, Such was / So + sıfat, olumsuz devrik, Had it not been for / Were it not for, kalıplaşmış dilek kipi). very + sıfat kullanmayın.",
          "The Street Where I Grew Up\n\nWhen I was a child, our street was the whole world. At one end stood the bakery, where Mr Yücel sold warm simit at six every morning. At the other was the small mosque, its courtyard full of pigeons and old men playing backgammon.\n\nSuch was the sense of community that nobody locked their doors. Not once do I remember feeling unsafe. Children played football until the street lights came on, and every adult was, in a sense, everyone's parent.\n\nThen, slowly, things changed. Gone are the bakery, the tailor and the little shop that sold everything from batteries to rose water. In their place stand glass towers, a car park and a chain coffee shop. Modern as the new buildings are, they have no character. Few of the families I knew still live there.\n\nFar be it from me to romanticise the past. Life was not always easy, and many of the old houses were cold and damp. Be that as it may, something important has been lost. Were it not for a handful of residents who still meet every Friday in the mosque courtyard, the street would have no memory at all.\n\nI went back last month. The pigeons were still there. So, remarkably, was one of the old men, still playing backgammon. He recognised me at once. Only then did I realise how much I had missed it.",
          ["En az 5 farklı ileri yapı", "Ölçülü ve doğal kullanım", "Cümle çeşitliliği ve ritim", "Güçlü kelimeler", "Bütünlük ve etkileyici son"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

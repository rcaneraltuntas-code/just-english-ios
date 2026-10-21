"""C2 Ünite 2: İnce anlamlar."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("C2", 2, "İnce anlamlar", "Shades of Meaning",
         "Eşanlamlı kelimeler arasındaki olumlu, nötr ve olumsuz çağrışımları (connotation) ayırt edebilir, bakma, konuşma ve yürüme gibi eylemleri kesin fiillerle anlatabilir, örtmeceleri ve yüklü dili fark edebilir, yoğunlaştırıcıları doğru eşdizimlerle kullanabilir ve aynı olguları farklı bir bakış açısıyla yazabilirim.",
         ["çağrışım: olumlu, nötr, olumsuz eşanlamlılar", "kesin fiiller: glance / stare / gaze, mutter / insist, stroll / stride", "örtmece ve yüklü dil", "yoğunlaştırıcılar ve eşdizimler: bitterly disappointed, highly unlikely", "aynı olgular, farklı bakış açısı"],
         ["medya", "insan ilişkileri", "edebiyat"],
         {"title": "Kelimelerin rengi", "durationMinutes": 45,
          "goal": "Gruplar aynı olayı (bir mahallede yeni bir alışveriş merkezi açılması) iki farklı gazete için yazar: biri destekleyen, biri karşı çıkan. Olgular aynı kalmalı, sadece kelime seçimi değişmeli. Gruplar metinlerini okur ve sınıf hangi kelimelerin bakış açısını değiştirdiğini işaretler. Son bölümde öğrenciler bir fotoğrafı kesin fiiller (glance, stroll, mutter) kullanarak betimler."})

u.vocab([
    ("connotation", "çağrışım, yan anlam", "\"Skinny\" has a negative connotation.", "\"Skinny\" olumsuz bir çağrışıma sahip.", None),
    ("denotation", "temel anlam, düz anlam", "The denotation of \"home\" is simply a place to live.", "\"Home\" kelimesinin düz anlamı sadece yaşanan yerdir.", None),
    ("slim", "ince, narin (olumlu)", "She has a slim figure.", "İnce bir vücudu var.", None),
    ("skinny", "sıska (olumsuz)", "He was a skinny little boy.", "Sıska küçük bir çocuktu.", None),
    ("thrifty", "tutumlu (olumlu)", "My grandmother was very thrifty.", "Büyükannem çok tutumluydu.", None),
    ("stingy", "cimri (olumsuz)", "Don't be so stingy!", "Bu kadar cimri olma!", None),
    ("assertive", "kendinden emin, iddialı (olumlu)", "You need to be more assertive in meetings.", "Toplantılarda daha kendinden emin olmalısın.", None),
    ("pushy", "ısrarcı, saldırgan (olumsuz)", "The salesman was really pushy.", "Satıcı gerçekten çok ısrarcıydı.", None),
    ("glance", "göz atmak", "She glanced at her watch.", "Saatine göz attı.", None),
    ("stare", "dik dik bakmak", "It's rude to stare.", "Dik dik bakmak kabalıktır.", None),
    ("gaze", "uzun uzun / hayranlıkla bakmak", "They gazed at the stars.", "Yıldızlara uzun uzun baktılar.", None),
    ("peer", "gözlerini kısarak bakmak", "He peered through the fog.", "Sisin içinden gözlerini kısarak baktı.", None),
    ("mutter", "mırıldanmak (genellikle şikâyetle)", "He muttered something under his breath.", "Kendi kendine bir şey mırıldandı.", None),
    ("stroll", "gezinmek, ağır ağır yürümek", "We strolled along the beach.", "Sahil boyunca ağır ağır yürüdük.", None),
    ("stride", "uzun adımlarla yürümek", "She strode confidently into the room.", "Kendinden emin uzun adımlarla odaya girdi.", None),
    ("stagger", "sendelemek", "He staggered under the weight of the box.", "Kutunun ağırlığı altında sendeledi.", None),
    ("euphemism", "örtmece", "\"Passed away\" is a euphemism for \"died\".", "\"Passed away\" \"öldü\" için bir örtmecedir.", None),
    ("loaded language", "yüklü dil, taraflı dil", "The article is full of loaded language.", "Makale taraflı dille dolu.", None),
    ("bitterly disappointed", "derin hayal kırıklığına uğramış", "We were bitterly disappointed by the result.", "Sonuçtan derin hayal kırıklığına uğradık.", None),
    ("highly unlikely", "hiç olası değil", "It's highly unlikely that he'll come.", "Gelmesi hiç olası değil.", None),
    ("deeply moved", "derinden etkilenmiş", "I was deeply moved by her speech.", "Konuşmasından derinden etkilendim.", None),
    ("utterly", "tamamen, büsbütün", "I was utterly exhausted.", "Tamamen bitkindim.", None),
    ("slant", "bakış açısı, eğilim (haberde)", "The article had a clear political slant.", "Makalenin açık bir siyasi eğilimi vardı.", None),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Çağrışım", "Aynı temel anlama sahip kelimelerin olumlu, nötr ve olumsuz çağrışımlarını (slim / thin / skinny, thrifty / careful / stingy) ayırt edip bilinçli seçebilirim.",
    {"kind": "dialogue", "title": "İki arkadaş, bir yeni komşu", "lines": [
        {"speaker": "Melis", "text": "Have you met our new neighbour? She's lovely. Very slim, very elegant."},
        {"speaker": "Okan", "text": "Elegant? I'd say she's rather skinny. And a bit pushy, too. She asked me three times to move my car."},
        {"speaker": "Melis", "text": "Pushy? She's just assertive. She knows what she wants."},
        {"speaker": "Okan", "text": "Hmm. And did you notice she refused to give anything for the street party?"},
        {"speaker": "Melis", "text": "That's not stingy, Okan. She's thrifty. She told me she's saving for a house."},
        {"speaker": "Okan", "text": "Well, you clearly like her more than I do!"}],
     "questions": [
        mc("Why does Okan think the neighbour is pushy?", ["She shouted at him.", "She asked him three times to move his car.", "She took his parking space."], 1, "\"She asked me three times to move my car.\""),
        mc("What do Melis and Okan disagree about?", ["The facts", "How to describe the neighbour"], 1, "Aynı olgular, farklı kelimeler."),
     ]},
    {"explanation": "Her kelimenin bir **düz anlamı (denotation)** ve bir **çağrışımı (connotation)** vardır. Aynı kişiyi ya da durumu tarif eden kelimeler, konuşanın **tutumunu** açığa çıkarır.\n\n| Olumlu | Nötr | Olumsuz |\n|---|---|---|\n| slim, slender | thin | skinny, scrawny, bony |\n| thrifty, economical | careful with money | stingy, mean, tight-fisted |\n| assertive, confident | direct | pushy, aggressive, arrogant |\n| curious, inquisitive | interested | nosy, prying |\n| determined, persistent | firm | stubborn, obstinate, pig-headed |\n| youthful | young | childish, immature |\n| relaxed, easy-going | calm | lazy, careless |\n| frank, honest | direct | blunt, tactless |\n| unique, unconventional | unusual | weird, odd, peculiar |\n| aroma, fragrance, scent | smell | odour, stench, stink |\n| cosy, compact | small | cramped, poky |\n| mature, experienced | old, elderly (kibar) | past it, ancient (alaycı) |\n\n**Nasıl kullanılır?**\n\n- **İkna** ederken: *Our compact flat* (emlak ilanı) vs. *a cramped flat* (eleştiri)\n- **Diplomasi** gerektiğinde: *He's very direct.* (= *He's blunt.*)\n- **Edebiyatta** karakter betimlemesinde: yazarın tutumunu açığa çıkarır.\n\n**Dikkat:** Bazı kelimeler **bağlama göre** çağrışım değiştirir: *ambitious* (olumlu: hırslı ve başarılı / olumsuz: aşırı hırslı), *proud* (gururlu / kibirli).",
     "examples": [{"en": "The estate agent described the flat as \"cosy\". It was cramped.", "tr": "Emlakçı daireyi \"şirin ve sıcak\" diye tanımladı. Sıkış tıkıştı."},
                  {"en": "She's not stubborn; she's determined.", "tr": "O inatçı değil, kararlı."},
                  {"en": "I'd rather be called frank than blunt.", "tr": "Kaba yerine dürüst denmesini tercih ederim."}],
     "turkishNote": "Türkçede de benzer çağrışım farkları vardır: \"ince / zayıf / sıska\", \"tutumlu / cimri\", \"kararlı / inatçı\", \"meraklı / burnunu sokan\". Ancak İngilizcede bu farklar daha geniş bir kelime yelpazesiyle ifade edilir ve yanlış seçim istemeden kaba görünmenize yol açabilir. Örneğin bir arkadaşınızın annesine \"She's very thin\" yerine \"skinny\" demek kabalık olur. Özellikle \"old\" yerine \"elderly\" ya da \"older\" kullanmak daha kibar kabul edilir."},
    [
        mc("Olumlu çağrışım:", ["slim", "skinny"], 0, "slim."),
        mc("Olumsuz çağrışım:", ["thrifty", "stingy"], 1, "stingy."),
        mc("\"nosy\" anlamı:", ["Meraklı ve ilgili (olumlu)", "Başkasının işine burnunu sokan (olumsuz)"], 1, "nosy."),
        mc("Emlak ilanında olumlu kelime:", ["cramped", "cosy"], 1, "cosy."),
        gap("He's not stubborn; he's ___. He never gives up. (olumlu: kararlı)", ["determined", "persistent"], "determined."),
        gap("What a lovely ___! Is that jasmine? (olumlu: koku)", ["fragrance", "scent", "aroma"], "fragrance."),
        gap("She's very ___; she always tells you exactly what she thinks. (olumlu: açık sözlü)", ["frank", "honest", "direct"], "frank."),
        gap("There was a terrible ___ coming from the bin. (olumsuz: koku)", ["stench", "smell", "odour", "stink"], "stench."),
        listen("I wouldn't call him lazy. He's just very relaxed. And he's not childish, he's youthful. OK, he's a bit stubborn sometimes. Fine, he's my brother, and I love him.", "Konuşan kardeşini nasıl tanıtıyor?", ["Olumsuz kelimelerle eleştiriyor", "Olumsuz özellikleri olumlu kelimelerle yumuşatıyor"], 1, "lazy → relaxed, childish → youthful."),
        match([("slim", "skinny"), ("thrifty", "stingy"), ("assertive", "pushy"), ("curious", "nosy"), ("frank", "blunt")], "Her olumlu kelimeyi olumsuz karşılığıyla eşleştirin."),
    ],
    {"kind": "speaking", "task": speak("Tanıdığınız bir kişiyi (ya da hayali birini) iki kez tanıtın (her biri 30 saniye): (1) Onu çok seven bir arkadaşı gibi, olumlu çağrışımlı kelimelerle. (2) Ondan hoşlanmayan biri gibi, aynı özellikler için olumsuz çağrışımlı kelimelerle. Olgular aynı kalsın, sadece kelimeler değişsin.",
                                       "Positive: My colleague Ece is one of the most determined people I know. She's very assertive in meetings and always frank about what she thinks. She's quite thrifty, too; she brings her own lunch every day and is saving to travel the world. She's slim, energetic and has a wonderfully unconventional sense of style. Negative: Honestly, Ece is incredibly stubborn. She's pushy in meetings and can be really blunt, even rude. She's also a bit stingy; she never joins us for lunch. And her clothes? Let's just say they're rather odd.",
                                       ["Olumlu çağrışımlı kelimeler", "Olumsuz çağrışımlı kelimeler", "Aynı olgular", "Çeşitlilik"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "Kesin fiiller", "Bakma (glance, stare, gaze, peer, glimpse), konuşma (mutter, whisper, insist, snap, mumble) ve yürüme (stroll, stride, stagger, wander, tiptoe) eylemlerini kesin fiillerle anlatabilirim.",
    {"kind": "text", "title": "Bir öyküden", "body": "Kemal strode into the station, glanced at the board and groaned. The train was delayed again. He wandered over to a bench and sat down. Across the platform, a little girl was staring at him. Her mother whispered something to her, and the girl quickly looked away. An old man shuffled past, muttering about the weather. Kemal peered down the tunnel. In the distance, he glimpsed a faint light. \"Finally,\" he mumbled, and staggered to his feet, his heavy bag over his shoulder.",
     "questions": [
        mc("What did Kemal see on the board?", ["His train was cancelled.", "His train was delayed.", "His train had left."], 1, "\"The train was delayed again.\""),
        mc("What was the old man doing?", ["Shouting", "Muttering about the weather", "Running"], 1, "\"muttering about the weather\""),
     ]},
    {"explanation": "C2 seviyesinde *look, say, walk* gibi genel fiiller yerine, **nasıl** yapıldığını da anlatan **kesin fiiller** kullanılır.\n\n**1. Bakma fiilleri:**\n\n| Fiil | Anlam |\n|---|---|\n| **glance** (at) | kısa bir an bakmak |\n| **glimpse** / catch a glimpse of | bir an için görmek (istemeden) |\n| **stare** (at) | uzun süre, dik dik bakmak (çoğu zaman kaba) |\n| **gaze** (at) | uzun uzun, hayranlıkla ya da dalgın bakmak |\n| **peer** (at / into) | zor görünen bir şeye gözlerini kısarak bakmak |\n| **glare** (at) | öfkeyle bakmak |\n| **scan** | hızla gözden geçirmek |\n\n**2. Konuşma fiilleri:**\n\n| Fiil | Anlam |\n|---|---|\n| **whisper** | fısıldamak |\n| **mutter** | mırıldanmak (genellikle şikâyet) |\n| **mumble** | anlaşılmaz şekilde konuşmak |\n| **insist** | ısrar etmek |\n| **snap** | sinirle, sert bir şekilde söylemek |\n| **groan** | inlemek, söylenmek (hayal kırıklığı) |\n| **stammer** / **stutter** | kekelemek |\n| **exclaim** | heyecanla söylemek |\n\n**3. Yürüme fiilleri:**\n\n| Fiil | Anlam |\n|---|---|\n| **stroll** | keyifle, ağır ağır yürümek |\n| **stride** | kararlı, uzun adımlarla yürümek |\n| **wander** | amaçsızca dolaşmak |\n| **stagger** | sendeleyerek yürümek |\n| **shuffle** | ayaklarını sürüyerek yürümek |\n| **tiptoe** | parmak uçlarında yürümek |\n| **march** | kararlı / öfkeli yürümek |\n| **limp** | topallamak |\n\n**Etki:** *\"He walked into the room\"* bilgi verir; *\"He strode into the room\"* karakteri ve ruh halini de anlatır.",
     "examples": [{"en": "She glared at me when I interrupted her.", "tr": "Sözünü kestiğimde bana öfkeyle baktı."},
                  {"en": "We tiptoed past the baby's room.", "tr": "Bebeğin odasının önünden parmak uçlarımızda geçtik."},
                  {"en": "\"Leave me alone!\" he snapped.", "tr": "\"Beni rahat bırak!\" diye çıkıştı."}],
     "turkishNote": "Türkçede bu ayrımlar genellikle zarflarla yapılır: \"dik dik bakmak\", \"göz ucuyla bakmak\", \"ağır ağır yürümek\", \"sendeleyerek yürümek\". İngilizcede ise tek bir fiil hem eylemi hem de biçimini anlatır. Türk öğrenciler genellikle \"look\", \"say\" ve \"walk\" fiillerini aşırı kullanır. Hikâye ve betimleme yazarken bu kesin fiilleri kullanmak, yazınızı çok daha canlı ve C2 seviyesine uygun hale getirir."},
    [
        mc("Kısa bir an bakmak:", ["glance", "gaze"], 0, "glance."),
        mc("Öfkeyle bakmak:", ["glare", "glimpse"], 0, "glare."),
        mc("Kendinden emin, uzun adımlarla yürümek:", ["stride", "shuffle"], 0, "stride."),
        mc("Sinirle, sert bir şekilde söylemek:", ["snap", "whisper"], 0, "snap."),
        gap("We ___ along the river, enjoying the sunshine. (keyifle yürümek)", ["strolled", "wandered"], "strolled."),
        gap("She ___ at the stars for hours. (hayranlıkla bakmak)", ["gazed"], "gazed."),
        gap("He ___ through the dirty window, trying to see inside. (gözlerini kısarak bakmak)", ["peered"], "peered."),
        gap("\"I didn't do it,\" he ___, looking at the floor. (anlaşılmaz konuşmak)", ["mumbled", "muttered"], "mumbled."),
        listen("She tiptoed down the stairs, careful not to wake anyone. In the kitchen, she glimpsed a shadow by the window. Her heart was racing. \"Who's there?\" she whispered. A familiar voice muttered, \"It's only me. I couldn't sleep.\"", "Mutfakta kim vardı?", ["Bir hırsız", "Evden tanıdık biri", "Bir kedi"], 1, "\"A familiar voice ... It's only me.\""),
        match([("glance", "kısa bir an bakmak"), ("stare", "dik dik bakmak"), ("stagger", "sendelemek"), ("whisper", "fısıldamak"), ("wander", "amaçsızca dolaşmak")], "Her fiili anlamıyla eşleştirin."),
    ],
    {"kind": "speaking", "task": speak("Kalabalık bir yeri (havalimanı, pazar, hastane bekleme salonu, park) bir romandan bir sahne gibi betimleyin (1 dakika). Gördüğünüz en az 4 kişinin ne yaptığını anlatın ve en az 2 bakma, 2 konuşma ve 2 yürüme fiili kullanın (look, say, walk kullanmadan!).",
                                       "It's Saturday morning at the market. An elderly woman shuffles between the stalls, peering at the tomatoes as if they've personally offended her. A young couple stroll past, hand in hand, gazing at each other rather than the vegetables. Behind the cheese stall, a tired seller is muttering about the prices to anyone who'll listen. Suddenly, a man in a suit strides through the crowd, glancing at his watch and snapping at his phone. A small boy stares at him, open-mouthed, until his mother whispers, \"Don't stare,\" and gently pulls him away.",
                                       ["Kesin bakma fiilleri", "Kesin konuşma fiilleri", "Kesin yürüme fiilleri", "Canlı betimleme"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "Örtmece ve yüklü dil", "Örtmeceleri (passed away, let go, between jobs) ve medyada / siyasette kullanılan yüklü dili fark edip yorumlayabilir, gerektiğinde nazik bir dil kullanabilirim.",
    {"kind": "text", "title": "İki gazete, bir haber", "body": "Newspaper A:\n\"Hundreds of peaceful protesters gathered outside the town hall yesterday to defend their local park from a controversial building project. Campaigners say the scheme will destroy one of the last green spaces in the area.\"\n\nNewspaper B:\n\"A crowd of angry activists blocked the entrance to the town hall yesterday in an attempt to halt a new housing development. Supporters say the project will provide much-needed homes for local families.\"",
     "questions": [
        mc("Which newspaper seems to support the protest?", ["Newspaper A", "Newspaper B"], 0, "\"peaceful protesters\", \"defend\", \"destroy\""),
        mc("What is the project, according to Newspaper B?", ["A shopping centre", "A housing development", "A new road"], 1, "\"a new housing development\""),
     ]},
    {"explanation": "**1. Örtmece (euphemism):** Hoş olmayan, utandırıcı ya da hassas bir şeyi **yumuşatarak** söylemek.\n\n| Örtmece | Doğrudan anlam |\n|---|---|\n| **pass away** | die |\n| **let someone go / downsize / make redundant** | fire people |\n| **between jobs** | unemployed |\n| **senior citizens / older people** | old people |\n| **economical with the truth** | lying |\n| **under the weather** | ill |\n| **a little on the heavy side** | fat |\n| **the restroom / the bathroom** | the toilet |\n| **financially challenged** (genellikle şaka) | poor |\n\n**İş dünyası ve siyasette örtmeceler:**\n\n- *restructuring* (çoğu zaman = işten çıkarma)\n- *price adjustment* (= zam)\n- *collateral damage* (= sivil kayıplar)\n- *negative growth* (= küçülme)\n\n**2. Yüklü dil (loaded language):** Okuyucunun **duygusal tepkisini** yönlendirmek için seçilen kelimeler.\n\n| Olumlu / sempatik | Olumsuz / eleştirel |\n|---|---|\n| peaceful protesters / campaigners | angry activists / a mob |\n| defend the park | block the entrance / halt the development |\n| tax relief | tax cuts for the rich |\n| reform | shake-up / upheaval |\n| a bold decision | a reckless gamble |\n| revealed | admitted / confessed |\n\n**Eleştirel okuma soruları:**\n\n1. Hangi kelimeler **duygusal** tepki yaratmak için seçilmiş?\n2. Kim **etken**, kim **edilgen** olarak gösteriliyor?\n3. Hangi bilgiler **eksik**?\n4. Aynı olay **nötr** kelimelerle nasıl anlatılırdı?",
     "examples": [{"en": "I'm afraid her grandfather passed away last week.", "tr": "Maalesef dedesi geçen hafta vefat etti."},
                  {"en": "The company is restructuring, which means around 200 jobs will go.", "tr": "Şirket yeniden yapılanıyor, bu da yaklaşık 200 kişinin işini kaybedeceği anlamına geliyor."},
                  {"en": "The minister was being economical with the truth.", "tr": "Bakan gerçeği tam söylemiyordu."}],
     "turkishNote": "Türkçede de çok sayıda örtmece vardır: \"vefat etmek\", \"rahatsızlanmak\", \"işten ayrılmak\", \"tuvalet\" yerine \"lavabo\" demek. Medyadaki yüklü dil de evrenseldir: Aynı grup bir gazetede \"göstericiler\", diğerinde \"provokatörler\" olarak adlandırılabilir. İngilizce haber okurken bu kelimelere dikkat etmek, eleştirel okuma becerinizi geliştirir. Sınavlarda (IELTS, CPE) \"Yazarın tutumu nedir?\" sorularının cevabı genellikle bu yüklü kelimelerde gizlidir."},
    [
        mc("\"He passed away last year.\" anlamı:", ["Geçen yıl taşındı.", "Geçen yıl vefat etti."], 1, "pass away."),
        mc("\"I'm between jobs at the moment.\" anlamı:", ["İki işte çalışıyorum.", "Şu an işsizim."], 1, "between jobs."),
        mc("Sempatik bir haber dili:", ["a mob of angry activists", "peaceful campaigners"], 1, "Olumlu yüklü dil."),
        mc("\"The company is restructuring.\" genellikle:", ["İşten çıkarmalar olacak.", "Ofis yenilenecek."], 0, "Örtmece."),
        gap("I'm feeling a bit under the ___ today. I think I've got a cold.", ["weather"], "under the weather."),
        gap("The company had to let 50 employees ___. (işten çıkarmak)", ["go"], "let go."),
        gap("The politician was being economical with the ___. (yalan söylemek)", ["truth"], "economical with the truth."),
        gap("Supporters called it a bold decision; critics called it a reckless ___. (kumar)", ["gamble"], "a reckless gamble."),
        listen("The government has announced what it calls a modest price adjustment for public transport. In practice, this means that a monthly travel card will go up by twenty per cent from January.", "\"Price adjustment\" aslında ne anlama geliyor?", ["İndirim", "%20 zam", "Fiyat değişmeyecek"], 1, "\"go up by twenty per cent\""),
        match([("pass away", "die"), ("let go", "fire"), ("under the weather", "ill"), ("between jobs", "unemployed"), ("economical with the truth", "lying")], "Her örtmeceyi doğrudan anlamıyla eşleştirin."),
    ],
    {"kind": "speaking", "task": speak("Aynı olayı iki farklı haber spikeri gibi sunun (her biri 30 saniye). Olay: \"Şehir belediyesi, eski bir pazar yerini kapatıp yerine bir otopark yapmaya karar verdi. Yaklaşık 80 esnaf yer değiştirmek zorunda kalacak.\" (1) Kararı destekleyen bir kanal. (2) Karara karşı çıkan bir kanal. Olgular aynı kalsın, sadece kelimeler değişsin.",
                                       "Supportive: The city council has announced a bold plan to modernise the city centre. The old market, which has long suffered from poor facilities, will be replaced by a new car park, easing traffic for thousands of shoppers. Around 80 traders will be relocated to a new site. Critical: In a controversial move, the city council has decided to demolish the historic market, a beloved local landmark, to make way for yet another car park. Around 80 traders, many of whom have worked there for decades, will be forced out of their stalls.",
                                       ["Olumlu yüklü dil", "Olumsuz yüklü dil", "Aynı olgular", "Haber üslubu"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Yoğunlaştırıcılar ve eşdizimler", "Derecelendirilebilir ve derecelendirilemez sıfatlarla doğru yoğunlaştırıcıları (very / absolutely) ve doğal eşdizimleri (bitterly disappointed, highly unlikely, deeply moved) kullanabilirim.",
    {"kind": "text", "title": "Bir film eleştirisinden", "body": "I went into the cinema with high expectations and came out bitterly disappointed. The first half is painfully slow, and the dialogue is utterly unconvincing. It is highly unlikely that anyone will remember the plot a week later. That said, the lead actor gives a deeply moving performance, and the final scene is absolutely stunning. It is a great pity that the rest of the film does not live up to it. Overall, it is a seriously flawed film with one or two genuinely brilliant moments.",
     "questions": [
        mc("What did the reviewer think of the lead actor?", ["The performance was deeply moving.", "The performance was unconvincing.", "The actor was absent."], 0, "\"a deeply moving performance\""),
        mc("What is the reviewer's overall opinion?", ["A perfect film", "A seriously flawed film with some brilliant moments", "A terrible film with nothing good"], 1, "\"seriously flawed ... genuinely brilliant moments\""),
     ]},
    {"explanation": "**1. Derecelendirilebilir ve derecelendirilemez sıfatlar:**\n\n| Derecelendirilebilir (gradable) | Derecelendirilemez (ungradable / extreme) |\n|---|---|\n| good, tired, cold, big, interesting | brilliant, exhausted, freezing, enormous, fascinating |\n| **very, extremely, really, fairly, quite** | **absolutely, utterly, completely, totally, really** |\n| ✓ *very tired* ✗ *absolutely tired* | ✓ *absolutely exhausted* ✗ *very exhausted* |\n\n**Not:** *really* her iki türle de kullanılabilir. *quite* ise uç sıfatlarla \"tamamen\" anlamına gelir: *quite brilliant, quite impossible*.\n\n**2. Doğal eşdizimler (collocations):** Bazı zarf + sıfat kombinasyonları kalıplaşmıştır. C2 seviyesinde bunları kullanmak çok doğal görünür.\n\n| Zarf | Sıfat |\n|---|---|\n| **bitterly** | disappointed, cold, opposed |\n| **deeply** | moved, concerned, offended, grateful |\n| **highly** | unlikely, recommended, successful, controversial |\n| **painfully** | slow, shy, obvious, aware |\n| **utterly** | ridiculous, convinced, exhausted |\n| **seriously** | ill, injured, flawed |\n| **strongly** | opposed, recommended |\n| **fully** | aware, booked, understand |\n| **perfectly** | clear, normal, capable |\n| **wide** | awake, open |\n| **fast** | asleep |\n| **genuinely** | interested, surprised |\n\n**Doğal olmayanlar:** ✗ *highly disappointed*, ✗ *bitterly unlikely*, ✗ *deeply slow*.\n\n**3. Dikkat: understatement (C2 Ünite 7):** Bazen yoğunlaştırıcıların tersi de etkilidir: *It's not exactly cheap* (= çok pahalı).",
     "examples": [{"en": "I'm fully aware of the risks.", "tr": "Risklerin tamamen farkındayım."},
                  {"en": "The restaurant is highly recommended.", "tr": "Restoran şiddetle tavsiye ediliyor."},
                  {"en": "By midnight, the children were fast asleep.", "tr": "Gece yarısı çocuklar derin uykudaydı."}],
     "turkishNote": "Türkçede \"çok\" kelimesi hemen her sıfatla kullanılabilir: \"çok yorgun\", \"çok bitkin\", \"çok harika\". İngilizcede ise \"very\" sadece derecelendirilebilir sıfatlarla kullanılır; \"very exhausted\" ya da \"very fantastic\" doğal değildir. Türk öğrencilerin C2'de dikkat etmesi gereken asıl nokta eşdizimlerdir: \"derin hayal kırıklığı\" İngilizcede \"deeply disappointed\" olabilir ama \"bitterly disappointed\" çok daha yaygın ve doğaldır. \"Derin uykuda\" ise \"fast asleep\" olur, \"deeply asleep\" değil."},
    [
        mc("Doğru olan:", ["very exhausted", "absolutely exhausted"], 1, "Uç sıfat + absolutely."),
        mc("Doğru olan:", ["absolutely tired", "extremely tired"], 1, "Derecelendirilebilir + extremely."),
        mc("Doğal eşdizim:", ["highly disappointed", "bitterly disappointed"], 1, "bitterly disappointed."),
        mc("Doğal eşdizim:", ["fast asleep", "deeply asleep"], 0, "fast asleep."),
        gap("It's ___ unlikely that the flight will leave on time. (hiç)", ["highly"], "highly unlikely."),
        gap("I was ___ moved by her story. (derinden)", ["deeply"], "deeply moved."),
        gap("The hotel is fully ___ for the whole of August. (dolu)", ["booked"], "fully booked."),
        gap("He's ___ shy; he can hardly speak to strangers. (acı verecek kadar)", ["painfully"], "painfully shy."),
        listen("I'd highly recommend the new exhibition. The paintings are absolutely stunning, and the guide was genuinely interesting. My only complaint is that the café was painfully slow.", "Konuşanın tek şikâyeti neydi?", ["Resimler", "Rehber", "Kafenin çok yavaş olması"], 2, "\"the café was painfully slow\""),
        match([("bitterly", "disappointed"), ("highly", "unlikely"), ("deeply", "grateful"), ("wide", "awake"), ("seriously", "injured")], "Her zarfı en doğal sıfatla eşleştirin."),
    ],
    {"kind": "speaking", "task": speak("Son izlediğiniz bir filmi, okuduğunuz bir kitabı ya da gittiğiniz bir restoranı bir eleştirmen gibi değerlendirin (1 dakika). En az 6 doğal zarf + sıfat eşdizimi kullanın (bitterly disappointed, highly recommended, deeply moving, painfully slow, utterly ridiculous, absolutely stunning, genuinely funny, seriously flawed ...). very kullanmayın!",
                                       "Last weekend, I finally watched a film that everyone had been talking about, and I have to say, I was bitterly disappointed. The opening scenes are absolutely stunning, but after that, the story becomes painfully slow. Some of the dialogue is utterly ridiculous, and the ending is highly predictable. To be fair, the lead actress is genuinely talented, and there's one deeply moving scene with her father. But overall, it's a seriously flawed film. I wouldn't say it's terrible, but it's certainly not as brilliant as the critics claimed.",
                                       ["Doğal eşdizimler", "Doğru yoğunlaştırıcılar", "Eleştirel ton", "Akıcılık"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Aynı olgular, farklı bakış açısı", "Aynı olguları kelime seçimi, çağrışım, kesin fiiller ve yoğunlaştırıcılarla farklı bakış açılarından yazabilir ve bir metnin tarafını eleştirel olarak analiz edebilirim.",
    {"kind": "text", "title": "Bir şirket olayı, iki rapor", "body": "Report A (from the company):\n\"Following a thorough review, the company has made the difficult decision to streamline its operations. A small number of roles will be affected, and every effort will be made to support colleagues through this transition. These changes will allow us to invest in innovation and secure our long-term future.\"\n\nReport B (from the workers' union):\n\"Despite record profits, the company has announced plans to cut 300 jobs. Many of the workers affected have been with the firm for over twenty years. The union is deeply concerned that the cuts are being driven by short-term financial targets rather than by the needs of the business.\"",
     "questions": [
        mc("How many jobs will be lost, according to the union?", ["A small number", "300", "20"], 1, "\"cut 300 jobs\""),
        mc("Which fact does Report A NOT mention?", ["That the company is making record profits", "That changes will allow investment"], 0, "Report A omits profits."),
     ]},
    {"explanation": "Aynı olaylar, yazarın **amacına** ve **bakış açısına** göre çok farklı anlatılabilir. Bu derste ünitedeki tüm araçları birleştiriyoruz.\n\n**Bakış açısını belirleyen araçlar:**\n\n| Araç | Rapor A (şirket) | Rapor B (sendika) |\n|---|---|---|\n| **Örtmece** | *streamline, roles affected, transition* | — |\n| **Doğrudan dil** | — | *cut 300 jobs* |\n| **Sayıların sunumu** | *a small number* (belirsiz) | *300* (kesin) |\n| **Seçici bilgi** | geleceğe yatırım | rekor kâr, 20 yıllık çalışanlar |\n| **Çağrışım** | *difficult decision, thorough review* | *short-term financial targets* |\n| **Yoğunlaştırıcı** | *every effort* | *deeply concerned* |\n| **Edilgen / etken** | *roles will be affected* (kim yapıyor?) | *the company has announced plans to cut* |\n\n**Kendi yazınızda bakış açısını kontrol etmek için:**\n\n1. **Kelime seçimi:** Olumlu / nötr / olumsuz çağrışım (Ders 1)\n2. **Fiiller:** *walked* mı, *strode* mu, *staggered* mı? (Ders 2)\n3. **Örtmece veya doğrudan dil:** Yumuşatmak mı, açık olmak mı? (Ders 3)\n4. **Yoğunlaştırıcılar:** *slightly concerned* mı, *deeply concerned* mı? (Ders 4)\n5. **Seçici bilgi:** Hangi olguları öne çıkarıyorsunuz, hangilerini atlıyorsunuz?\n6. **Edilgen yapı:** Sorumluyu gizlemek mi, göstermek mi?\n\n**Etik not:** Bakış açısı yaratmak meşru bir yazı becerisidir (reklam, köşe yazısı, kampanya). Ancak **olguları çarpıtmak** ya da **yalan söylemek** değildir. C2 seviyesinde bir yazar, hem bu araçları kullanabilmeli hem de başkalarının kullanımını fark edebilmelidir.",
     "examples": [{"en": "Company: A small number of roles will be affected.", "tr": "Şirket: Az sayıda pozisyon etkilenecek."},
                  {"en": "Union: The company plans to cut 300 jobs.", "tr": "Sendika: Şirket 300 kişiyi işten çıkarmayı planlıyor."},
                  {"en": "Neutral: The company plans to reduce its workforce by 300.", "tr": "Nötr: Şirket iş gücünü 300 kişi azaltmayı planlıyor."}],
     "turkishNote": "Türk medyasında da aynı olay farklı kaynaklarda çok farklı kelimelerle anlatılır. İngilizce okurken bu farkı görmek, sınavlardaki \"yazarın tutumu\" (writer's attitude) ve \"ima edilen anlam\" (implied meaning) sorularını çözmenin anahtarıdır. Yazarken ise Türk öğrencilerin İngilizce metinlerinde genellikle tek bir \"nötr\" ton kullandığı görülür. Bu dersteki araçlarla, aynı içeriği bilinçli olarak farklı tonlarda yazabilirsiniz."},
    [
        mc("\"The company will streamline its operations.\" büyük ihtimalle:", ["İşten çıkarmalar olacak.", "Yeni çalışanlar alınacak."], 0, "Örtmece."),
        mc("Hangisi sorumluyu gizler?", ["Mistakes were made.", "The manager made a mistake."], 0, "Edilgen."),
        mc("Hangisi daha nötr?", ["The company plans to reduce its workforce by 300.", "The greedy company is throwing 300 loyal workers onto the street."], 0, "Nötr."),
        mc("\"a small number of roles\" ile \"300 jobs\" arasındaki fark:", ["Belirsiz ve yumuşatıcı vs. kesin ve doğrudan", "Hiçbir fark yok"], 0, "Sayıların sunumu."),
        gap("The union is ___ concerned about the job cuts. (derinden)", ["deeply"], "deeply concerned."),
        gap("Every ___ will be made to support staff. (çaba)", ["effort"], "every effort."),
        gap("The writer's ___ is clearly in favour of the plan. (bakış açısı, eğilim)", ["slant", "bias", "attitude"], "slant."),
        gap("By leaving out the profits, the report gives a ___ picture. (seçici, taraflı)", ["one-sided", "selective", "biased", "misleading"], "one-sided."),
        listen("Neutral version: Yesterday, the council voted to close two of the city's five public libraries. The decision will save around two million lira a year. Around forty staff will be moved to other council departments.", "Bu nötr haberde kaç kütüphane kapanacak?", ["İki", "Beş", "Kırk"], 0, "\"close two of the city's five public libraries\""),
        typ("Nötr dille yeniden yazın: \"The reckless council has destroyed our beloved park.\" (The council has ...)", variants("The council has removed the park.", "The council has closed the park.", "The council has demolished the park.", "The council has built on the park.", "The council has redeveloped the park."), "The council has closed the park."),
    ],
    {"kind": "writing", "task": write("Aşağıdaki olgulara dayanarak iki farklı kısa haber / rapor yazın (her biri 90–120 kelime). Olgular: Bir şehir, merkezdeki ana caddeyi araç trafiğine kapatıp yayalara açtı. Esnafın bir kısmı müşteri kaybından şikâyetçi. Hava kirliliği ilk üç ayda %25 azaldı. Bazı sakinler otobüs güzergâhlarının uzadığını söylüyor. (A) Kararı destekleyen bir belediye basın bülteni. (B) Karara karşı çıkan bir esnaf derneği açıklaması. Olguları değiştirmeyin; kelime seçimi, çağrışım, örtmece, yoğunlaştırıcılar ve seçici vurgu kullanın. Sonra 2–3 cümleyle iki metni karşılaştırın.",
                                      "(A) Council press release:\n\nThree months after the city transformed its main street into a vibrant pedestrian zone, the results are highly encouraging. Air pollution in the city centre has fallen by an impressive 25%, making the area cleaner and safer for families. Residents can now stroll freely, enjoy outdoor cafés and rediscover the historic heart of their city. While some bus routes have been adjusted, the council is fully committed to working with local businesses during this exciting period of transition.\n\n(B) Traders' association statement:\n\nThe association is deeply concerned about the impact of the council's decision to close the main street to traffic. Many long-established shops have reported a painful drop in customers, and some owners fear they may be forced to close. Residents, particularly older people, have complained that bus journeys now take considerably longer. While cleaner air is, of course, welcome, it should not come at the cost of local livelihoods.\n\nComparison:\n\nBoth texts use the same facts, but each one selects and frames them differently. The council emphasises the 25% fall in pollution and uses euphemisms such as \"adjusted\" and \"transition\", while the traders highlight lost customers and longer journeys, using emotionally charged language such as \"deeply concerned\" and \"painful drop\".",
                                      ["İki net bakış açısı", "Olgular değişmemiş", "Çağrışım ve yüklü dil", "Örtmece ve yoğunlaştırıcılar", "Karşılaştırma analizi"])},
)

u.test([
    mc("Olumsuz çağrışım:", ["slim", "skinny"], 1, "skinny"),
    mc("\"She's very nosy.\" anlamı:", ["Başkasının işine burnunu sokuyor.", "Çok meraklı ve araştırmacı."], 0, "nosy"),
    mc("Öfkeyle bakmak:", ["glare", "gaze"], 0, "glare"),
    mc("Doğru olan:", ["very exhausted", "absolutely exhausted"], 1, "Uç sıfat"),
    mc("\"The company is downsizing.\" anlamı:", ["Şirket işçi çıkarıyor.", "Şirket küçük bir ofise taşınıyor."], 0, "Örtmece"),
    gap("She's not stubborn; she's ___. (olumlu)", ["determined", "persistent"], "determined"),
    gap("We ___ along the beach at sunset. (keyifle yürümek)", ["strolled", "wandered"], "strolled"),
    gap("\"Go away!\" he ___. (sinirle söylemek)", ["snapped"], "snapped"),
    gap("I'm sorry to hear that your grandmother passed ___.", ["away"], "passed away"),
    gap("We were ___ disappointed by the result. (derin)", ["bitterly", "deeply"], "bitterly disappointed"),
    gap("It's highly ___ that it will snow in July. (olası değil)", ["unlikely"], "highly unlikely"),
    gap("By ten o'clock, the children were ___ asleep.", ["fast", "sound"], "fast asleep"),
    listen("The minister described the new policy as a minor adjustment to the pension system. Critics, however, say it means that millions of people will have to work three years longer before they can retire.", "Eleştirmenlere göre yeni politika ne anlama geliyor?", ["Küçük bir değişiklik", "Milyonlarca kişinin üç yıl daha uzun çalışması", "Emekli maaşlarının artması"], 1, "\"work three years longer\""),
    typ("Nötr dille yeniden yazın: \"A mob of angry protesters blocked the road.\" (A group of ...)", variants("A group of protesters blocked the road.", "A group of people blocked the road.", "A group of demonstrators blocked the road.", "A group of campaigners blocked the road."), "A group of protesters blocked the road."),
    write("Aşağıdaki olgulara dayanarak iki kısa metin yazın (her biri 90–120 kelime): Bir üniversite, ders ücretlerini %15 artırdı. Ek gelir yeni laboratuvarlara ve bursa harcanacak. Bazı öğrenciler okulu bırakmayı düşündüğünü söylüyor. (A) Üniversite yönetiminin öğrencilere e-postası (olumlu bakış açısı, örtmece). (B) Öğrenci birliğinin bir açıklaması (eleştirel bakış açısı, yüklü dil). Olguları değiştirmeyin. Çağrışım, kesin fiiller, örtmece ve doğal yoğunlaştırıcı eşdizimleri kullanın.",
          "(A) University email:\n\nDear students,\n\nWe are writing to inform you of a modest adjustment to tuition fees for the coming academic year. Fees will rise by 15%, a decision that was not taken lightly. This additional investment will allow us to build state-of-the-art laboratories and significantly expand our scholarship programme, ensuring that talented students from all backgrounds can continue to thrive here. We are fully aware that any increase can be challenging, and our student support team is ready to help anyone who has concerns.\n\nKind regards,\nThe University Management\n\n(B) Student union statement:\n\nThe student union is bitterly disappointed by the university's decision to raise tuition fees by a staggering 15%. Many students, already struggling with the rising cost of living, have told us they are now seriously considering dropping out. While new laboratories and scholarships are welcome, it is utterly unacceptable that current students should be forced to pay for them. We strongly urge the management to reconsider this deeply unfair decision and to meet with student representatives without delay.",
          ["İki net bakış açısı", "Olgular aynı", "Örtmece ve yüklü dil", "Doğal yoğunlaştırıcı eşdizimleri", "Uygun üslup"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

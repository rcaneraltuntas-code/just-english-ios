"""B1 Ünite 5: Haberler."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("B1", 5, "Haberler", "In the News",
         "Haberleri ve geçmişteki olayları anlatırken olayların sırasını past perfect ile netleştirebilir, past simple, past continuous ve past perfect'i bir arada kullanarak bir hikâye ya da haber aktarabilirim.",
         ["past perfect (had + V3)", "past simple ve past perfect (olay sırası)", "by the time / already / before / after / when", "anlatı zamanları (simple, continuous, perfect)", "haberlere tepki verme"],
         ["haberler", "olaylar ve kazalar", "haber fiilleri"],
         {"title": "Son dakika!", "durationMinutes": 45,
          "goal": "Gruplar, öğretmenin verdiği üç başlıktan birini seçip bir haber programı hazırlar. Bir öğrenci spiker, diğerleri muhabir ve görgü tanığı olur; olayı anlatı zamanlarıyla (was doing, had done, did) aktarırlar. Diğer gruplar Did you hear about...? / Really? What happened next? kalıplarıyla tepki verip soru sorar."})

u.vocab([
    ("headline", "manşet, başlık", "Did you see the headline this morning?", "Bu sabahki manşeti gördün mü?", None),
    ("article", "makale, haber yazısı", "I read an interesting article about sleep.", "Uyku hakkında ilginç bir yazı okudum.", None),
    ("journalist", "gazeteci", "The journalist interviewed the mayor.", "Gazeteci belediye başkanıyla röportaj yaptı.", None),
    ("report", "haber vermek, bildirmek; rapor", "The TV channel reported the story live.", "Kanal haberi canlı verdi.", None),
    ("witness", "görgü tanığı", "A witness saw the whole accident.", "Bir görgü tanığı bütün kazayı gördü.", None),
    ("accident", "kaza", "There was a car accident on the motorway.", "Otoyolda bir trafik kazası oldu.", None),
    ("injured", "yaralı", "Two people are injured.", "İki kişi yaralı.", "injury (yara, sakatlık)"),
    ("rescue", "kurtarmak", "Firefighters rescued a cat from the tree.", "İtfaiyeciler ağaçtan bir kediyi kurtardı.", None),
    ("escape", "kaçmak", "The prisoner escaped through a window.", "Mahkûm pencereden kaçtı.", None),
    ("steal", "çalmak", "Someone had stolen her bag.", "Biri çantasını çalmıştı.", "steal → stole → stolen"),
    ("thief", "hırsız", "The police caught the thief.", "Polis hırsızı yakaladı.", "çoğul: thieves"),
    ("arrest", "tutuklamak", "The police arrested two men.", "Polis iki adamı tutukladı.", None),
    ("disappear", "ortadan kaybolmak", "The dog disappeared last Monday.", "Köpek geçen pazartesi kayboldu.", None),
    ("flood", "sel", "The flood destroyed many houses.", "Sel birçok evi yıktı.", None),
    ("storm", "fırtına", "The storm lasted all night.", "Fırtına bütün gece sürdü.", None),
    ("destroy", "yok etmek, yıkmak", "The fire destroyed the old factory.", "Yangın eski fabrikayı yok etti.", None),
    ("survive", "hayatta kalmak", "Everyone survived the crash.", "Kazadan herkes sağ kurtuldu.", "survivor (hayatta kalan)"),
    ("break out", "patlak vermek (yangın vb.)", "A fire broke out in the kitchen.", "Mutfakta yangın çıktı.", None),
    ("by the time", "-diği zamana kadar, -diğinde (çoktan)", "By the time we arrived, the film had started.", "Biz vardığımızda film çoktan başlamıştı.", None),
    ("already", "çoktan, zaten", "The thief had already left.", "Hırsız çoktan gitmişti.", None),
    ("apparently", "anlaşılan, söylenene göre", "Apparently, nobody saw anything.", "Söylenene göre kimse bir şey görmemiş.", None),
    ("luckily", "neyse ki, şans eseri", "Luckily, nobody was hurt.", "Neyse ki kimse yaralanmadı.", None),
    ("suddenly", "aniden", "Suddenly, the lights went out.", "Aniden ışıklar söndü.", None),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Çoktan olmuştu", "Geçmişteki bir andan daha önce olmuş olayları past perfect ile anlatabilirim.",
    {"kind": "dialogue", "title": "Kötü bir sabah", "lines": [
        {"speaker": "Defne", "text": "You look stressed. What happened?"},
        {"speaker": "Kerem", "text": "What a morning! When I got to the station, the train had left."},
        {"speaker": "Defne", "text": "Oh no! Did you take a taxi?"},
        {"speaker": "Kerem", "text": "Yes, but when I arrived at the office, I realised I had left my laptop on the train platform."},
        {"speaker": "Defne", "text": "Seriously? Did you go back?"},
        {"speaker": "Kerem", "text": "Yes, and luckily a cleaner had found it and given it to the station manager."}],
     "questions": [
        mc("What had happened when Kerem got to the station?", ["The train was late.", "The train had left.", "The station was closed."], 1, "\"the train had left\""),
        mc("Who had found the laptop?", ["A cleaner", "The station manager", "A taxi driver"], 0, "\"a cleaner had found it\""),
     ]},
    {"explanation": "**Past perfect**, geçmişteki bir andan **daha önce** olmuş bir olayı anlatır (\"-mıştı\").\n\n**Yapı:** **had** + V3 (tüm kişilerde aynı)\n\n| | |\n|---|---|\n| Olumlu | I / she / they **had left** ('d left) |\n| Olumsuz | I **hadn't** seen the film. |\n| Soru | **Had** you **eaten** before you came? |\n\n**İki geçmiş olay:**\n\n```\n1. olay (daha önce)        2. olay\n  had left        ←        got to the station\n```\n\n- When I **got** to the station, the train **had left**. (Önce tren gitti, sonra ben vardım.)\n- When I **got** to the station, the train **left**. (Ben vardım, sonra tren kalktı.)\n\nPast perfect, **hangi olayın önce olduğunu** netleştirir.",
     "examples": [{"en": "When we got home, someone had broken the window.", "tr": "Eve geldiğimizde biri camı kırmıştı."},
                  {"en": "I hadn't eaten all day, so I was very hungry.", "tr": "Bütün gün yemek yememiştim, bu yüzden çok açtım."},
                  {"en": "Had you met her before the party?", "tr": "Onunla partiden önce tanışmış mıydın?"}],
     "turkishNote": "Türkçedeki \"-mıştı\" eki (gitmişti, yemişti) past perfect'e denk gelir. Türkçe konuşanlar \"had\" i bazen atlar ya da past perfect'i sadece \"uzun zaman önce\" anlamında kullanır. Past perfect'in amacı süreyi değil, iki geçmiş olay arasındaki sırayı göstermektir."},
    [
        mc("\"Tren gitmişti.\"", ["The train left.", "The train had left.", "The train has left."], 1, "-mıştı → had + V3."),
        mc("Hangisi doğru?", ["She had went home.", "She had gone home."], 1, "had + V3 (gone)."),
        mc("When I got to the cinema, the film ___. (önce film başladı)", ["started", "had started"], 1, "Daha önce → had started."),
        gap("When we arrived, everyone ___ (leave).", ["had left", "'d left"], "had + V3."),
        gap("I was hungry because I ___ (not eat) all day.", ["hadn't eaten", "had not eaten"], "Olumsuz."),
        gap("___ you seen the film before? (geçmişteki bir andan önce)", ["Had"], "Had + özne + V3?"),
        gap("Someone had ___ my bike. (steal)", ["stolen"], "steal → stolen."),
        listen("When I opened the fridge, I saw that my flatmate had eaten all my cheese. I was so angry!", "Konuşan buzdolabını açtığında ne olmuştu?", ["Peynir bozulmuştu", "Ev arkadaşı peynirin hepsini yemişti", "Buzdolabı bozulmuştu"], 1, "\"my flatmate had eaten all my cheese\""),
        order(["had", "When", "I", "woke", "up", "the", "snow", "stopped"], "When I woke up the snow had stopped.", "When + past simple, had + V3.", "Uyandığımda kar durmuştu."),
        typ("İngilizce yazın: \"Eve geldiğimde biri camı kırmıştı.\"", variants("When I got home, someone had broken the window.", "When I came home, someone had broken the window.", "When I arrived home, someone had broken the window.", "Someone had broken the window when I got home.", "When I got home someone had broken the window."), "When I got home, someone had broken the window."),
    ],
    {"kind": "speaking", "task": speak("Kötü geçen bir gününüzü anlatın. En az 4 past perfect cümlesi kullanın: Bir yere vardığınızda ne olmuştu? Neyi unutmuştunuz? Daha önce ne yapmamıştınız?",
                                       "Last Friday was terrible. When I woke up, my alarm hadn't rung. When I got to the bus stop, the bus had already left. At work, I realised I had forgotten my lunch at home. And when I got home, my brother had eaten the last piece of cake!",
                                       ["had + V3 doğru", "Olay sırası net", "Past simple ile birlikte kullanım"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "Hangisi önce oldu?", "by the time, already, before, after ile iki geçmiş olayın sırasını doğru zamanla anlatabilirim.",
    {"kind": "text", "title": "Kayıp köpek eve döndü", "body": "A dog called Pamuk has returned home after six weeks.\n\nPamuk disappeared on 3 March. His owners, the Yıldız family, had taken him to a park outside the city for a picnic. He ran after a rabbit and didn't come back.\n\nThe family looked everywhere. They had already put up hundreds of posters when, last Tuesday, they received a phone call. A farmer had found Pamuk in his barn, 40 kilometres away.\n\n\"By the time we got to the farm, the farmer's children had given him a bath and a big dinner,\" said Mrs Yıldız. \"He'd lost a bit of weight, but he was happy and healthy.\"",
     "questions": [
        mc("Why had the family gone to the park?", ["For a picnic", "To walk the dog", "To look for a rabbit"], 0, "\"had taken him to a park... for a picnic\""),
        mc("What had the farmer's children done before the family arrived?", ["Called the police", "Given Pamuk a bath and dinner", "Taken Pamuk home"], 1, "\"had given him a bath and a big dinner\""),
     ]},
    {"explanation": "Olaylar **sırasıyla** anlatılıyorsa past simple yeterlidir:\n\n- Pamuk **ran** after a rabbit, and he **didn't come** back.\n\nSıra **bozulduğunda** (daha önceki bir olaydan bahsederken) past perfect kullanılır:\n\n- Pamuk **disappeared**. The family **had taken** him to a park.\n\n**Sık kullanılan bağlaçlar:**\n\n| Bağlaç | Örnek |\n|---|---|\n| **by the time** | **By the time** we arrived, they **had eaten**. (Biz vardığımızda çoktan yemişlerdi.) |\n| **already** | The thief **had already** left. |\n| **before** | She **had** never **flown before** that trip. |\n| **after** | **After** he **had finished** work, he went home. |\n| **because** | I was tired **because** I **hadn't slept**. |\n\n**before / after** kullanılırsa sıra zaten belli olduğu için past simple de olur:\n\n- After he **finished** work, he went home. ✓",
     "examples": [{"en": "By the time the police came, the thieves had escaped.", "tr": "Polis geldiğinde hırsızlar çoktan kaçmıştı."},
                  {"en": "I had never seen snow before I moved to Erzurum.", "tr": "Erzurum'a taşınmadan önce hiç kar görmemiştim."},
                  {"en": "She was nervous because she hadn't driven for years.", "tr": "Yıllardır araba kullanmadığı için gergindi."}],
     "turkishNote": "\"By the time\" Türkçede \"-dığında (çoktan)\" ya da \"-ene kadar\" diye çevrilir ve neredeyse her zaman past perfect ile kullanılır: By the time I arrived, they had left. Bu cümlede \"left\" demek, ben varınca gittiler anlamına gelebilir."},
    [
        mc("By the time we arrived, the party ___.", ["finished", "had finished"], 1, "by the time → past perfect."),
        mc("I was nervous because I ___ on a plane before.", ["never was", "had never been"], 1, "Daha önceki deneyim → past perfect."),
        mc("İki olay sırayla: \"I opened the door and ___ in.\"", ["walked", "had walked"], 0, "Sıralı → past simple."),
        gap("By the time the police came, the thief had ___ escaped. (çoktan)", ["already"], "had already + V3."),
        gap("I'd never ___ (see) the sea before that holiday.", ["seen"], "had never + V3."),
        gap("She was tired because she ___ (not sleep) well.", ["hadn't slept", "had not slept"], "because + past perfect."),
        gap("___ the time I got to the shop, it had closed.", ["By"], "By the time."),
        listen("By the time the firefighters arrived, the neighbours had already rescued the old man from the building.", "İtfaiye gelmeden önce ne olmuştu?", ["Yangın sönmüştü", "Komşular yaşlı adamı kurtarmıştı", "Bina yıkılmıştı"], 1, "\"the neighbours had already rescued the old man\""),
        order(["the", "time", "By", "we", "arrived", "they", "had", "eaten"], "By the time we arrived they had eaten.", "By the time + past simple, past perfect.", "Biz vardığımızda onlar çoktan yemişti."),
        typ("İngilizce yazın: \"Erzurum'a taşınmadan önce hiç kar görmemiştim.\"", variants("I had never seen snow before I moved to Erzurum.", "I'd never seen snow before I moved to Erzurum.", "Before I moved to Erzurum, I had never seen snow.", "Before I moved to Erzurum, I'd never seen snow.", "I hadn't seen snow before I moved to Erzurum.", "Before I moved to Erzurum I had never seen snow."), "I had never seen snow before I moved to Erzurum."),
    ],
    {"kind": "speaking", "task": speak("Hayatınızda ilk kez yaptığınız bir şeyi anlatın (ilk uçuş, ilk iş görüşmesi, ilk yurt dışı seyahati). Daha önce ne yapmamıştınız, oraya vardığınızda ne olmuştu? by the time, already ve never ... before kullanın.",
                                       "My first job interview was in 2019. I had never worn a suit before, so I felt strange. I had prepared answers to all the usual questions. By the time I got to the office, I'd already drunk three coffees, so I was very nervous! But it went well, and they offered me the job.",
                                       ["Past perfect ile önceki olaylar", "by the time / already / never before", "Akıcı anlatım"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "Hikâye zamanları", "Past simple, past continuous ve past perfect'i bir arada kullanarak bir olayı canlı bir şekilde anlatabilirim.",
    {"kind": "text", "title": "Kahraman garson", "body": "It was a busy Saturday evening at a small restaurant in Antalya. The waiters were running between the tables and the kitchen was full of noise.\n\nSuddenly, a customer stood up and shouted for help. A man at the next table was holding his throat. He had been fine a minute earlier, but now he couldn't breathe.\n\nA young waiter, Barış Aydın, ran to the table. Luckily, he had learned first aid in a course the year before. He helped the man, and after a few seconds the man started breathing again.\n\nWhen the ambulance arrived, the man was sitting calmly and drinking water. Everyone in the restaurant was clapping.",
     "questions": [
        mc("What were the waiters doing when the problem started?", ["Sitting down", "Running between the tables", "Cooking"], 1, "\"The waiters were running between the tables\""),
        mc("Why did Barış know what to do?", ["He was a doctor.", "He had learned first aid the year before.", "He had seen it on TV."], 1, "\"he had learned first aid in a course the year before\""),
     ]},
    {"explanation": "Bir hikâye anlatırken **üç geçmiş zaman** birlikte kullanılır:\n\n| Zaman | Görevi | Örnek |\n|---|---|---|\n| **Past continuous** | Arka plan, sahne | The waiters **were running** between the tables. |\n| **Past simple** | Ana olaylar, sırasıyla | A customer **stood up** and **shouted**. |\n| **Past perfect** | Daha önce olanlar | He **had learned** first aid the year before. |\n\n**Hikâyeyi canlı yapan ifadeler:**\n\n- **Suddenly**, ... / **All of a sudden**, ...\n- **Luckily**, ... / **Unfortunately**, ...\n- **At first**, ... **Then** ... **In the end**, ...\n- **A minute earlier** / **the day before** / **the year before**\n\n**Dikkat:** Past perfect'i **her cümlede** kullanmayın; sadece zaman çizgisinde geriye gittiğinizde kullanın.",
     "examples": [{"en": "It was raining and I was walking home when I saw something strange.", "tr": "Yağmur yağıyordu ve eve yürüyordum, o sırada tuhaf bir şey gördüm."},
                  {"en": "Unfortunately, I had left my umbrella at the office.", "tr": "Ne yazık ki şemsiyemi ofiste unutmuştum."},
                  {"en": "In the end, a kind stranger gave me a lift.", "tr": "Sonunda nazik bir yabancı beni arabasıyla bıraktı."}],
     "turkishNote": "Türkçede hikâye anlatırken \"-yordu\" (past continuous), \"-dı\" (past simple) ve \"-mıştı\" (past perfect) eklerini kullanırız; İngilizcedeki üç zaman bunlara oldukça iyi denk gelir. \"When I arrived, the man was sitting\" (oturuyordu) ile \"had sat\" (oturmuştu) arasındaki farka dikkat edin."},
    [
        mc("Arka plan: \"It ___ heavily that night.\"", ["rained", "was raining", "had rained"], 1, "Arka plan → past continuous."),
        mc("Ana olay: \"Suddenly, the lights ___ out.\"", ["went", "were going", "had gone"], 0, "Ana olay → past simple."),
        mc("Daha önce: \"I couldn't get in because I ___ my keys.\"", ["lost", "was losing", "had lost"], 2, "Önceki olay → past perfect."),
        gap("I was walking home when I ___ (see) a fox.", ["saw"], "when + past simple."),
        gap("When the ambulance came, the man ___ (sit) calmly.", ["was sitting"], "O sırada süren → continuous."),
        gap("She was upset because someone ___ (take) her seat.", ["had taken", "'d taken"], "Önceki olay → past perfect."),
        gap("___, nobody was hurt. (neyse ki)", ["Luckily", "Fortunately"], "Luckily."),
        match([("were running", "arka plan"), ("stood up", "ana olay"), ("had learned", "daha önceki olay"), ("suddenly", "aniden"), ("in the end", "sonunda")], "Eşleştirin."),
        listen("I was sitting in a café when a woman came in. She looked worried. She had lost her little boy in the market. We all went out to help, and in the end we found him eating ice cream.", "Kadın neden endişeliydi?", ["Çantasını kaybetmişti", "Küçük oğlunu kaybetmişti", "Otobüsü kaçırmıştı"], 1, "\"She had lost her little boy in the market.\""),
        typ("İngilizce yazın: \"Ne yazık ki şemsiyemi ofiste unutmuştum.\"", variants("Unfortunately, I had left my umbrella at the office.", "Unfortunately, I'd left my umbrella at the office.", "Unfortunately, I had forgotten my umbrella at the office.", "Unfortunately, I'd forgotten my umbrella at the office.", "Unfortunately, I had left my umbrella in the office.", "Unfortunately I had left my umbrella at the office.", "Unfortunately, I'd left my umbrella in the office."), "Unfortunately, I had left my umbrella at the office."),
    ],
    {"kind": "speaking", "task": speak("Başınızdan geçen ilginç ya da komik bir olayı anlatın. Arka planı past continuous ile, ana olayları past simple ile, öncesini past perfect ile verin. suddenly, luckily ve in the end kullanın.",
                                       "It was a hot afternoon and I was waiting for a bus. Suddenly, a dog ran up to me and took my sandwich! I had bought it five minutes earlier, and I was really hungry. I ran after the dog, but it was too fast. Luckily, a woman at the bus stop had two sandwiches, and she gave me one. In the end, we became friends!",
                                       ["Üç anlatı zamanı doğru", "Bağlayıcı ifadeler", "Hikâye sırası net"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Bugünkü manşetler", "Haber manşetlerini anlayabilir, haber fiilleri ve olay kelimeleriyle kısa haberleri anlatabilirim.",
    {"kind": "text", "title": "Yerel haber bülteni", "body": "STORM HITS COAST\nA strong storm hit the Black Sea coast last night. Strong winds destroyed several roofs, and some roads are closed. Luckily, everyone survived.\n\nTHIEF RETURNS STOLEN BIKE\nA thief who had stolen a bike from a student in Eskişehir brought it back two days later. He left a note: \"Sorry. My mother told me to bring it back.\"\n\nFIRE BREAKS OUT IN SHOPPING CENTRE\nA fire broke out in a shopping centre in Bursa yesterday afternoon. Staff helped hundreds of people leave the building safely. Firefighters rescued two workers from the roof.",
     "questions": [
        mc("Why did the thief return the bike?", ["The police arrested him.", "His mother told him to.", "The bike was broken."], 1, "\"My mother told me to bring it back.\""),
        mc("Where did the firefighters rescue two workers from?", ["The car park", "The roof", "A shop"], 1, "\"from the roof\""),
     ]},
    {"explanation": "**Haber manşetlerinin dili** kısa ve özeldir:\n\n| Manşette | Anlamı |\n|---|---|\n| **Present simple** = geçmiş olay | STORM **HITS** COAST → A storm **hit** the coast. |\n| **to + fiil** = gelecek | PRESIDENT **TO VISIT** JAPAN → The president **will visit** Japan. |\n| **a / the** yok | THIEF RETURNS BIKE → **A** thief returned **a** bike. |\n\n**Haber ve olay fiilleri:**\n\n| Fiil | Örnek |\n|---|---|\n| **hit** (hit) | A storm hit the city. |\n| **break out** (broke out) | A fire broke out. |\n| **rescue** | Firefighters rescued two people. |\n| **escape** | Three prisoners escaped. |\n| **arrest** | The police arrested a man. |\n| **destroy** | The flood destroyed 50 houses. |\n| **survive** | Everyone survived. |\n\n**Haberde yer ve zaman** genellikle cümlenin sonundadır: A fire broke out **in Bursa yesterday afternoon**.",
     "examples": [{"en": "A strong earthquake hit the region on Monday.", "tr": "Pazartesi bölgeyi şiddetli bir deprem vurdu."},
                  {"en": "Police arrested two men after a robbery in the city centre.", "tr": "Polis şehir merkezindeki bir soygunun ardından iki adamı tutukladı."},
                  {"en": "All the passengers survived the crash.", "tr": "Bütün yolcular kazadan sağ kurtuldu."}],
     "turkishNote": "Türkçe manşetlerde geçmiş olaylar genellikle geçmiş zamanla verilir (\"Fırtına sahili vurdu\"), ama İngilizce manşetlerde geçmiş olaylar için present simple neredeyse kuraldır. Haberi okurken ya da anlatırken past simple'a çevirin: STORM HITS COAST → A storm hit the coast."},
    [
        mc("\"STORM HITS COAST\" ne anlatır?", ["Şu anda olan bir fırtına", "Geçmişte olmuş bir fırtına", "Gelecekte olacak bir fırtına"], 1, "Manşette present = geçmiş olay."),
        mc("\"MAYOR TO OPEN NEW BRIDGE\" ne anlatır?", ["Belediye başkanı köprüyü açtı.", "Belediye başkanı köprüyü açacak."], 1, "to + fiil = gelecek."),
        mc("A fire ___ out in the kitchen last night.", ["broke", "broken", "breaks"], 0, "break out → broke out."),
        gap("Firefighters ___ two children from the building. (kurtardı)", ["rescued"], "rescue."),
        gap("The police ___ the thief at the airport. (tutukladı)", ["arrested", "caught"], "arrest."),
        gap("Luckily, all the passengers ___ the accident. (sağ kurtuldu)", ["survived"], "survive."),
        gap("The flood ___ more than 100 homes. (yok etti)", ["destroyed"], "destroy."),
        match([("hit", "vurmak"), ("break out", "patlak vermek"), ("escape", "kaçmak"), ("arrest", "tutuklamak"), ("survive", "hayatta kalmak")], "Eşleştirin."),
        listen("And now the local news. Three people escaped from a burning bus on the motorway this morning. The driver had noticed smoke and stopped the bus just in time.", "Şoför neden otobüsü durdurdu?", ["Yolcular bağırdı", "Duman fark etmişti", "Lastik patladı"], 1, "\"The driver had noticed smoke\""),
        typ("Manşeti cümleye çevirin: \"POLICE ARREST TWO MEN\" (geçmiş)", variants("The police arrested two men.", "Police arrested two men.", "The police have arrested two men.", "Police have arrested two men."), "The police arrested two men."),
    ],
    {"kind": "speaking", "task": speak("Bu hafta duyduğunuz gerçek ya da hayali 2 haberi spiker gibi sunun. Bir manşetle başlayın, sonra olayı past simple ile anlatın ve bir past perfect cümlesi ekleyin.",
                                       "Good evening. Our first story: DOG SAVES FAMILY FROM FIRE. A fire broke out in a house in Izmir last night. The family's dog started barking and woke everyone up. They had all gone to bed early, so nobody had noticed the smoke. Luckily, everyone escaped safely.",
                                       ["Manşet dili doğru", "Haber fiilleri", "Past simple + past perfect"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Duydun mu?", "Bir haberi arkadaşıma aktarabilir, haberlere doğal tepkiler verebilir ve soru sorarak konuşmayı sürdürebilirim.",
    {"kind": "dialogue", "title": "İnanılmaz bir haber", "lines": [
        {"speaker": "Zeynep", "text": "Did you hear about the man who found a ring in a fish?"},
        {"speaker": "Hakan", "text": "No! What happened?"},
        {"speaker": "Zeynep", "text": "Apparently, he was cooking dinner when he found a gold ring inside the fish."},
        {"speaker": "Hakan", "text": "You're joking! Whose ring was it?"},
        {"speaker": "Zeynep", "text": "It belonged to a woman who had lost it on a boat trip ten years before!"},
        {"speaker": "Hakan", "text": "That's incredible! How did they find her?"}],
     "questions": [
        mc("What was the man doing when he found the ring?", ["Fishing", "Cooking dinner", "Eating at a restaurant"], 1, "\"he was cooking dinner\""),
        mc("When had the woman lost the ring?", ["Last week", "Ten years before", "The day before"], 1, "\"ten years before\""),
     ]},
    {"explanation": "**Bir haberi açmak:**\n\n- **Did you hear about** ...? / **Have you heard about** ...?\n- **Guess what!** / **You'll never believe this!**\n- **Apparently**, ... (Söylenene göre ...)\n- **I read / saw (online) that** ...\n\n**Tepki vermek:**\n\n| Duygu | İfade |\n|---|---|\n| Şaşkınlık | **Really?** / **You're joking!** / **No way!** |\n| Hayranlık | **That's incredible / amazing!** |\n| Üzüntü | **Oh no! That's awful / terrible.** |\n| Rahatlama | **Thank goodness!** / **What a relief!** |\n| Komik | **That's hilarious!** |\n\n**Konuşmayı sürdürmek:**\n\n- **What happened next?** / **And then what?**\n- **How did they ...?** / **Was anyone hurt?**\n\nHikâyeyi aktarırken **anlatı zamanlarını** kullanın: He **was cooking** when he **found** a ring. The woman **had lost** it.",
     "examples": [{"en": "Guess what! Our neighbour won a car in a competition.", "tr": "Bil bakalım ne oldu! Komşumuz bir yarışmada araba kazandı."},
                  {"en": "Apparently, the shop had closed years ago.", "tr": "Söylenene göre dükkân yıllar önce kapanmış."},
                  {"en": "Oh no! Was anyone hurt?", "tr": "Eyvah! Yaralanan var mı?"}],
     "turkishNote": "Türkçedeki \"-mış\" eki (duyulan geçmiş: \"kapanmış\") İngilizcede ayrı bir zamanla değil, \"apparently\", \"I heard that\" ya da \"they say\" gibi ifadelerle verilir. \"Apparently\" kelimesini cümlenin başına koymak, bilginin başkasından duyulduğunu gösterir."},
    [
        mc("Bir haberi açmak:", ["Did you hear about the fire?", "Did you listen the fire?"], 0, "hear about."),
        mc("Şaşkınlık:", ["You're joking!", "Thank goodness!", "That's awful."], 0, "You're joking!"),
        mc("Kötü bir haber: \"The bus crashed.\"", ["That's hilarious!", "Oh no! Was anyone hurt?", "No way, how fun!"], 1, "Endişe + soru."),
        mc("İyi bir sonuç: \"Everyone survived.\"", ["What a relief!", "That's terrible."], 0, "Rahatlama."),
        gap("___, the shop had closed years ago. (söylenene göre)", ["Apparently"], "Apparently."),
        gap("Guess ___! I've got a new job!", ["what"], "Guess what!"),
        gap("What happened ___? (sonra)", ["next", "then"], "What happened next?"),
        gap("She was swimming when she ___ (see) a dolphin.", ["saw"], "Anlatı zamanları."),
        listen("You'll never believe this! My grandmother has just started a YouTube channel, and she already has ten thousand followers! – No way! That's amazing!", "Dinleyen kişinin tepkisi nasıl?", ["Üzgün", "Şaşkın ve hayran", "Kızgın"], 1, "\"No way! That's amazing!\""),
        typ("İngilizce yazın: \"Eyvah! Yaralanan var mı?\"", variants("Oh no! Was anyone hurt?", "Oh no! Was anybody hurt?", "Oh no! Is anyone hurt?", "Oh no, was anyone hurt?", "Oh no! Was anyone injured?", "Oh no! Is anybody hurt?"), "Oh no! Was anyone hurt?"),
    ],
    {"kind": "writing", "task": write("Yerel bir gazete için kısa bir haber yazın (120–150 kelime). Bir manşetle başlayın, olayı anlatı zamanlarıyla (past continuous, past simple, past perfect) anlatın, bir görgü tanığından alıntı ekleyin ve sonucu belirtin. Gerçek ya da hayali olabilir.",
                                      "STUDENT RETURNS LOST WALLET WITH 20,000 LIRA\n\nA university student in Konya returned a lost wallet to its owner yesterday.\n\nElif Demir, 20, was walking to class on Tuesday morning when she saw a brown wallet on the ground. When she opened it, she found 20,000 lira and an ID card. The owner, a 68-year-old man, had dropped it while he was getting off the bus.\n\nElif took the wallet to the police station immediately. The police found the owner's phone number, and he came to the station an hour later.\n\n\"I had looked everywhere and I was very worried,\" he said. \"This young woman is a hero.\"\n\nThe man wanted to give Elif some of the money, but she said no. \"I just did the right thing,\" she said.",
                                      ["Manşet dili", "Anlatı zamanları doğru", "Haber fiilleri ve kelimeleri", "Alıntı ve sonuç", "Haber üslubu"])},
)

u.test([
    mc("\"Film başlamıştı.\"", ["The film started.", "The film had started.", "The film has started."], 1, "had + V3"),
    mc("Hangisi doğru?", ["They had went home.", "They had gone home."], 1, "V3"),
    mc("By the time we got there, the shop ___.", ["closed", "had closed"], 1, "by the time"),
    mc("Arka plan: \"The sun ___ and the birds were singing.\"", ["shone", "was shining", "had shone"], 1, "Past continuous"),
    gap("I couldn't pay because I ___ (leave) my wallet at home.", ["had left", "'d left"], "Önceki olay"),
    gap("I'd never ___ (be) to Paris before 2020.", ["been"], "had never been"),
    gap("A fire ___ out in the factory last night.", ["broke"], "broke out"),
    gap("The police ___ the robber yesterday. (tutukladı)", ["arrested", "caught"], "arrest"),
    mc("\"MINISTER TO VISIT SCHOOL\"", ["Bakan okulu ziyaret etti.", "Bakan okulu ziyaret edecek."], 1, "to + fiil = gelecek"),
    mc("Kötü haber tepkisi:", ["That's awful!", "That's hilarious!"], 0, "Üzüntü"),
    gap("___, nobody saw the thief. (söylenene göre)", ["Apparently"], "Apparently"),
    mc("When I arrived, she ___. (Ben varınca o çıktı.)", ["left", "had left"], 0, "Sıralı olay → past simple"),
    listen("I was driving to work when I heard the news on the radio. A small plane had landed on the motorway! Luckily, nobody was hurt.", "Konuşan haberi nerede duydu?", ["Televizyonda", "Arabada radyoda", "İnternette"], 1, "\"I was driving to work when I heard the news on the radio\""),
    typ("İngilizce yazın: \"Polis geldiğinde hırsızlar çoktan kaçmıştı.\"", variants("When the police came, the thieves had already escaped.", "By the time the police came, the thieves had already escaped.", "When the police arrived, the thieves had already escaped.", "By the time the police arrived, the thieves had already escaped.", "When the police came, the thieves had already run away.", "By the time the police arrived, the thieves had escaped.", "When the police arrived the thieves had already escaped."), "When the police came, the thieves had already escaped."),
    write("\"Hiç unutmadığım bir gün\" başlıklı bir hikâye yazın (120–150 kelime). Past continuous ile sahneyi kurun, past simple ile olayları anlatın, past perfect ile öncesini verin. suddenly, luckily, by the time ve in the end kullanın.",
          "I'll never forget the day of my sister's wedding. It was a beautiful summer morning and everyone was getting ready at my parents' house. My mother was cooking and my father was looking for his tie. Suddenly, my sister started crying. She had left her wedding dress at the dressmaker's the day before! I jumped into the car and drove across the city. By the time I got to the shop, the dressmaker had already gone home. Luckily, her neighbour had a key, and she opened the shop for me. I got back just in time. In the end, it was a perfect day, and now we laugh about it every year.",
          ["Üç anlatı zamanı", "Bağlayıcılar (suddenly, by the time...)", "Olay sırası net", "Canlı anlatım", "Düzenli paragraf"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

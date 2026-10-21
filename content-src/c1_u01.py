"""C1 Ünite 1: Vurgu."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("C1", 1, "Vurgu", "Emphasis",
         "Olumsuz ve kısıtlayıcı zarflardan sonra devrik yapı (inversion) kullanarak konuşmamı ve yazımı vurgulu ve etkileyici hale getirebilir, bu yapıların hangi üslupta uygun olduğunu bilebilir ve vurgulu do, so ... that, such ... that gibi diğer vurgu araçlarını kullanabilirim.",
         ["Never / Rarely / Seldom + devrik yapı", "Not only ... but also, No sooner ... than, Hardly ... when", "Only after / Not until / Under no circumstances", "Little did I know, So / Such ... that devrik yapısı", "vurgulu do / did ve üslup seçimi"],
         ["etkileyici deneyimler", "konuşma ve hitabet", "vurgu ve anlatım"],
         {"title": "Unutulmaz anlar", "durationMinutes": 45,
          "goal": "Her öğrenci hayatındaki unutulmaz bir anı devrik yapılarla dramatik bir şekilde anlatır (Never had I felt so..., No sooner had we arrived than..., Little did I know that...). Sınıf en etkileyici cümleleri seçer; ardından aynı anı sade dille anlatarak devrik yapının ne zaman fazla geldiği tartışılır."})

u.vocab([
    ("seldom", "nadiren (resmî)", "Seldom have I seen such talent.", "Nadiren böyle bir yetenek gördüm.", None),
    ("scarcely", "ancak, henüz ... ki", "Scarcely had we sat down when the phone rang.", "Daha yeni oturmuştuk ki telefon çaldı.", None),
    ("no sooner ... than", "-er -mez", "No sooner had I left than it started to rain.", "Çıkar çıkmaz yağmur başladı.", None),
    ("under no circumstances", "hiçbir koşulda", "Under no circumstances should you open this door.", "Bu kapıyı hiçbir koşulda açmamalısınız.", None),
    ("on no account", "asla, hiçbir surette", "On no account must the money be spent.", "Para hiçbir surette harcanmamalı.", None),
    ("by no means", "hiç de, katiyen", "It is by no means certain.", "Hiç de kesin değil.", None),
    ("little did I know", "hiç bilmiyordum ki", "Little did I know that my life was about to change.", "Hayatımın değişmek üzere olduğunu hiç bilmiyordum.", None),
    ("unprecedented", "eşi benzeri görülmemiş", "The storm caused unprecedented damage.", "Fırtına eşi benzeri görülmemiş hasara yol açtı.", None),
    ("remarkable", "dikkat çekici, olağanüstü", "She made a remarkable recovery.", "Olağanüstü bir iyileşme gösterdi.", None),
    ("astonishing", "hayret verici", "The results were astonishing.", "Sonuçlar hayret vericiydi.", None),
    ("utterly", "tamamen, büsbütün", "I was utterly exhausted.", "Tamamen bitkindim.", None),
    ("profound", "derin, köklü", "The book had a profound effect on me.", "Kitabın üzerimde derin bir etkisi oldu.", None),
    ("vividly", "canlı bir şekilde", "I remember that day vividly.", "O günü canlı bir şekilde hatırlıyorum.", None),
    ("striking", "çarpıcı", "There is a striking similarity between them.", "Aralarında çarpıcı bir benzerlik var.", None),
    ("compelling", "ikna edici, karşı konulmaz", "She made a compelling argument.", "İkna edici bir argüman sundu.", None),
    ("emphasise", "vurgulamak", "I must emphasise how important this is.", "Bunun ne kadar önemli olduğunu vurgulamalıyım.", "AmE: emphasize"),
    ("underestimate", "hafife almak", "Never underestimate your opponent.", "Rakibini asla hafife alma.", None),
    ("acknowledge", "kabul etmek", "He finally acknowledged his mistake.", "Sonunda hatasını kabul etti.", None),
    ("overwhelmed", "bunalmış, duygulanmış", "I was overwhelmed by their kindness.", "Nezaketleri karşısında duygulandım.", None),
    ("breathtaking", "nefes kesici", "The view was absolutely breathtaking.", "Manzara kesinlikle nefes kesiciydi.", None),
    ("turning point", "dönüm noktası", "That meeting was a turning point in my career.", "O toplantı kariyerimde bir dönüm noktasıydı.", None),
    ("in vain", "boşuna", "We searched for hours, but in vain.", "Saatlerce aradık ama boşuna.", None),
    ("at no time", "hiçbir zaman, hiçbir an", "At no time did I feel unsafe.", "Hiçbir an kendimi güvensiz hissetmedim.", None),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Hiç böyle bir şey görmemiştim", "Never, Rarely, Seldom gibi olumsuz zarflarla devrik yapı kurarak bir deneyimi vurgulu anlatabilirim.",
    {"kind": "text", "title": "Bir konuşmadan: Ödül töreni", "body": "Thank you all so much. I have to say, never in my life have I felt so honoured.\n\nWhen I started this project ten years ago, I had no money, no team and no office. Rarely did anyone take us seriously. Seldom have I worked so hard, or doubted myself so much.\n\nBut never did I imagine that our small idea would one day reach two million students.\n\nNor could I have done it without my team. They are the real winners tonight. Rarely do you find people who believe in an idea so completely.\n\nThank you.",
     "questions": [
        mc("How did people react to the project at the beginning?", ["They supported it enthusiastically.", "Few people took it seriously.", "They offered money."], 1, "\"Rarely did anyone take us seriously.\""),
        mc("Who does the speaker say are the real winners?", ["The students", "The team", "The judges"], 1, "\"They are the real winners tonight.\""),
     ]},
    {"explanation": "**Devrik yapı (inversion)**, olumsuz ya da kısıtlayıcı bir zarf **cümlenin başına** geldiğinde **yardımcı fiil öznenin önüne** geçer. Tıpkı soru cümlesi gibi:\n\n| Normal | Devrik (vurgulu) |\n|---|---|\n| I have **never** felt so honoured. | **Never have I** felt so honoured. |\n| People **rarely** took us seriously. | **Rarely did people** take us seriously. |\n| We **seldom** see such talent. | **Seldom do we** see such talent. |\n| I had **hardly ever** been abroad. | **Hardly ever had I** been abroad. |\n\n**Yardımcı fiil kuralı:**\n\n- Cümlede yardımcı fiil varsa (have, had, can, will, is) → o fiil öne geçer: *Never **have** I seen ...*\n- Yardımcı fiil yoksa (present / past simple) → **do / does / did** eklenir: *Rarely **did** anyone take us seriously.*\n\n**Never before / Never in my life:**\n\n- ***Never before had*** *the city seen such crowds.*\n- ***Never in my life have I*** *been so scared.*\n\n**Nor / Neither** (olumsuz ekleme):\n\n- *I didn't see it, **nor did** I hear anything.*\n\n**Üslup:** Devrik yapı **resmî, edebi ya da dramatik** bir etki yaratır: konuşmalar, makaleler, edebiyat. Günlük sohbette fazla kullanmak **yapay** durur.",
     "examples": [{"en": "Never have I seen such a beautiful sunset.", "tr": "Hiç böyle güzel bir gün batımı görmemiştim."},
                  {"en": "Rarely does the city experience such heavy snow.", "tr": "Şehir nadiren bu kadar yoğun kar görür."},
                  {"en": "Seldom had she felt so alone.", "tr": "Nadiren kendini bu kadar yalnız hissetmişti."}],
     "turkishNote": "Türkçede vurgu genellikle kelime sırasıyla değil, tonlama ve \"hiç\", \"asla\" gibi kelimelerle yapılır: \"Hayatımda hiç bu kadar onurlandırılmamıştım.\" İngilizcede bu etki devrik yapıyla sağlanır. Türkçe konuşanların en sık hatası, zarfı başa alıp yardımcı fiili öne almamaktır: \"Never I have seen\" yanlıştır; \"Never have I seen\" doğrudur."},
    [
        mc("Hangisi doğru?", ["Never I have seen such a thing.", "Never have I seen such a thing."], 1, "Yardımcı fiil öne."),
        mc("Hangisi doğru?", ["Rarely we go out these days.", "Rarely do we go out these days."], 1, "do eklenir."),
        mc("\"Seldom did she complain.\" normal hali:", ["She seldom complained.", "She seldom complains."], 0, "did → past."),
        mc("Devrik yapı hangi bağlamda en doğal?", ["Arkadaşla mesajlaşma", "Resmî bir konuşma ya da makale"], 1, "Resmî / dramatik."),
        gap("Never ___ I been so embarrassed in my life. (have)", ["have"], "Never have I."),
        gap("Rarely ___ he arrive on time. (geçmiş)", ["did"], "did + yalın fiil."),
        gap("Seldom ___ we see such commitment.", ["do"], "Present → do."),
        gap("I didn't call her, ___ did I send a message.", ["nor"], "nor + devrik."),
        listen("Never before had the small town seen so many visitors. Rarely did a day pass without a tour bus arriving. And never did the locals imagine that their quiet streets would appear in a famous film.", "Kasabada ne oldu?", ["Ziyaretçi sayısı azaldı", "Daha önce hiç olmadığı kadar ziyaretçi geldi", "Kasaba boşaldı"], 1, "\"Never before had the small town seen so many visitors.\""),
        typ("Devrik yapıyla yeniden yazın: \"I have never tasted such delicious food.\"", variants("Never have I tasted such delicious food.", "Never have I tasted such delicious food!", "Never before have I tasted such delicious food."), "Never have I tasted such delicious food."),
    ],
    {"kind": "speaking", "task": speak("Bir ödül töreninde ya da bir veda partisinde kısa bir konuşma yaptığınızı hayal edin (1 dakika). Never have I / Never in my life / Rarely do / Seldom have / Never did I imagine yapılarından en az 4'ünü kullanın. Devrik yapıları vurgulu bir tonla söyleyin.",
                                       "Thank you so much, everyone. Never in my life have I felt so lucky. When I joined this company eight years ago, never did I imagine that I would make such wonderful friends. Rarely do you find a team that supports each other like this. Seldom have I laughed as much as I have in this office. I'm going to miss you all, and I hope we stay in touch.",
                                       ["Devrik yapı doğruluğu", "do / did / have doğru seçimi", "Vurgulu tonlama", "Bağlama uygunluk"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "Yalnızca değil, -er -mez", "Not only ... but also, No sooner ... than ve Hardly / Scarcely ... when yapılarını doğru zaman ve devrik yapıyla kullanabilirim.",
    {"kind": "text", "title": "Bir romandan: Fırtına", "body": "No sooner had we left the harbour than the wind began to rise.\n\nWithin minutes, the sky had turned black. Hardly had the captain given the order to turn back when a huge wave crashed over the deck.\n\nNot only did we lose our sails, but the engine also stopped working. For three hours, the little boat was thrown from side to side.\n\nScarcely had the storm passed when we saw the lights of a fishing boat coming towards us. Not only had they seen our signal, but they had also called the coast guard.\n\nWe reached land just before midnight, cold, wet and utterly exhausted, but alive.",
     "questions": [
        mc("When did the wind begin to rise?", ["Just after they left the harbour", "At midnight", "When they reached land"], 0, "\"No sooner had we left the harbour than the wind began to rise.\""),
        mc("What did the fishing boat do?", ["It ignored them.", "It saw their signal and called the coast guard.", "It also lost its engine."], 1, "\"Not only had they seen our signal, but they had also called the coast guard.\""),
     ]},
    {"explanation": "**1. Not only ... but (also) ...**\n\n| Normal | Devrik |\n|---|---|\n| We **not only** lost our sails **but also** our engine. | **Not only did we** lose our sails, **but** the engine **also** stopped. |\n| She is **not only** talented **but also** hard-working. | **Not only is she** talented, **but** she is **also** hard-working. |\n\nDevrik yapı **sadece \"Not only\" kısmında** olur; \"but\" kısmı normal kalır.\n\n**2. No sooner ... than / Hardly ... when / Scarcely ... when** (= -er -mez, tam ... ki)\n\nİki geçmiş olay **hemen arka arkaya** olur. İlk olay **past perfect + devrik**, ikinci olay **past simple**.\n\n| Yapı | Örnek |\n|---|---|\n| **No sooner had** + özne + V3 + **than** + past simple | **No sooner had** we left **than** it started to rain. |\n| **Hardly had** + özne + V3 + **when** + past simple | **Hardly had** I sat down **when** the phone rang. |\n| **Scarcely had** + özne + V3 + **when** + past simple | **Scarcely had** she arrived **when** she was asked to leave. |\n\n**Dikkat:** **No sooner** → **than** / **Hardly, Scarcely** → **when**\n\n- ~~No sooner had I arrived when~~ ✗\n- ~~Hardly had I arrived than~~ ✗ (bazen duyulur ama standart değil)\n\n**Normal (devrik olmayan) hali de mümkün:** *I had **no sooner** left **than** it started to rain.* / *I had **hardly** sat down **when** ...*",
     "examples": [{"en": "No sooner had I paid than I realised I'd forgotten my wallet.", "tr": "Ödemeyi yapar yapmaz cüzdanımı unuttuğumu fark ettim."},
                  {"en": "Hardly had the film started when the power went off.", "tr": "Film başlar başlamaz elektrikler kesildi."},
                  {"en": "Not only did he apologise, but he also offered to pay.", "tr": "Sadece özür dilemekle kalmadı, ödemeyi de teklif etti."}],
     "turkishNote": "Türkçedeki \"-er -mez\" yapısı (\"eve girer girmez\") İngilizcede \"No sooner had I entered the house than\" ya da \"Hardly had I entered the house when\" ile karşılanır. Bu yapı Türkçede günlük dildir, ama İngilizcede edebi ve resmîdir; günlük konuşmada \"As soon as I got home, ...\" daha doğaldır. En sık hata \"No sooner ... when\" kullanmaktır: \"No sooner\" her zaman \"than\" ile eşleşir."},
    [
        mc("Hangisi doğru?", ["No sooner had I arrived when it started.", "No sooner had I arrived than it started."], 1, "No sooner ... than."),
        mc("Hangisi doğru?", ["Hardly had we sat down when the bell rang.", "Hardly we had sat down when the bell rang."], 0, "Hardly had + özne."),
        mc("Hangisi doğru?", ["Not only she is clever, but also kind.", "Not only is she clever, but she is also kind."], 1, "Not only + devrik."),
        mc("Günlük konuşmada en doğal:", ["No sooner had I got home than he called.", "As soon as I got home, he called."], 1, "Devrik yapı edebi."),
        gap("No sooner ___ she finished her speech than everyone applauded.", ["had"], "No sooner had."),
        gap("Hardly had the game started ___ it began to rain.", ["when"], "Hardly ... when."),
        gap("Not only ___ he forget my birthday, but he also forgot our anniversary.", ["did"], "Not only did."),
        gap("Scarcely had we arrived when we ___ (be) asked to leave.", ["were"], "Past simple (edilgen)."),
        listen("Scarcely had the new manager started when the problems began. Not only did half the team resign, but the company also lost its biggest client. No sooner had they found a new client than the office flooded.", "Yeni müdür başlar başlamaz ne oldu?", ["Şirket büyüdü", "Sorunlar başladı", "Herkes terfi aldı"], 1, "\"Scarcely had the new manager started when the problems began.\""),
        order(["No", "sooner", "had", "we", "arrived", "than", "the", "rain", "started"], "No sooner had we arrived than the rain started.", "No sooner had + özne + V3 + than + past simple.", "Biz varır varmaz yağmur başladı."),
    ],
    {"kind": "speaking", "task": speak("Her şeyin ters gittiği bir günü bir romancı gibi dramatik bir şekilde anlatın. En az bir No sooner ... than, bir Hardly / Scarcely ... when ve iki Not only ... but also yapısı kullanın. Zaman uyumuna (past perfect + past simple) dikkat edin.",
                                       "It was the worst day of my life. No sooner had I left the house than I realised I'd forgotten my keys. Hardly had I reached the bus stop when the bus drove past without stopping. Not only was I late for my exam, but I had also left my calculator at home. And scarcely had I sat down in the exam room when my phone started ringing. Not only did everyone turn around and stare, but the teacher also asked me to leave!",
                                       ["No sooner ... than", "Hardly / Scarcely ... when", "Not only + devrik", "Zaman uyumu"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "Ancak o zaman, hiçbir koşulda", "Only after / Only when / Not until ile kısıtlayıcı devrik yapıları ve Under no circumstances / On no account gibi kesin yasakları kullanabilirim.",
    {"kind": "text", "title": "Laboratuvar güvenlik kuralları", "body": "SAFETY RULES – PLEASE READ CAREFULLY\n\nUnder no circumstances should food or drink be brought into the laboratory.\n\nOn no account must chemicals be removed from the building.\n\nOnly after receiving full safety training will students be allowed to use the equipment.\n\nNot until the supervisor has checked your work should you leave the lab.\n\nOnly in an emergency may the side doors be used.\n\nAt no time should students work alone in the lab.\n\nAny student who breaks these rules will be asked to leave immediately.",
     "questions": [
        mc("When can students use the equipment?", ["Whenever they want", "Only after full safety training", "Only with a friend"], 1, "\"Only after receiving full safety training\""),
        mc("When may the side doors be used?", ["At the end of the day", "Only in an emergency", "Never"], 1, "\"Only in an emergency may the side doors be used.\""),
     ]},
    {"explanation": "**1. Only + zaman / koşul ifadesi → devrik yapı**\n\n**Dikkat:** Devrik yapı **ana cümlede** olur, \"Only\" kısmında değil!\n\n| Yapı | Örnek |\n|---|---|\n| **Only after** + isim / -ing / cümle | **Only after** the meeting **did I** understand. |\n| **Only when** + cümle | **Only when** I got home **did I** notice. |\n| **Only if** + cümle | **Only if** you work hard **will you** succeed. |\n| **Only then** | **Only then did** she realise. |\n| **Only by** + -ing | **Only by** working together **can we** solve this. |\n| **Only in** + isim | **Only in** an emergency **may** the doors be used. |\n\n**2. Not until** (= ancak ... -ince, ... -e kadar değil)\n\n- *I didn't realise until I got home.* → ***Not until** I got home **did I** realise.*\n\n**3. Kesin yasaklar (çok resmî, kurallar ve uyarılar):**\n\n| Yapı | Örnek |\n|---|---|\n| **Under no circumstances** | **Under no circumstances should** you open this. |\n| **On no account** | **On no account must** the door be left open. |\n| **In no way** | **In no way is** this my fault. |\n| **At no time** | **At no time did** I feel unsafe. |\n\n**Not:** \"No\" ile başlayan ifadelerde devrik yapı zorunludur; \"Not until\" ve \"Only\" ile başlayan cümlelerde de öyle.",
     "examples": [{"en": "Only after the results were published did they realise their mistake.", "tr": "Sonuçlar yayımlandıktan sonra hatalarını ancak fark ettiler."},
                  {"en": "Not until she spoke did I recognise her.", "tr": "Konuşana kadar onu tanımadım. / Ancak konuşunca tanıdım."},
                  {"en": "Under no circumstances should you share your password.", "tr": "Şifrenizi hiçbir koşulda paylaşmamalısınız."}],
     "turkishNote": "Türkçedeki \"ancak ... -ince\" yapısı (\"ancak eve gelince fark ettim\") İngilizcede \"Only when I got home did I notice\" ya da \"Not until I got home did I notice\" ile karşılanır. En sık hata, devrik yapıyı yanlış yere koymaktır: \"Only when did I get home I noticed\" yanlıştır. Devrik yapı her zaman ana cümlede, yani virgülden sonraki kısımdadır."},
    [
        mc("Hangisi doğru?", ["Only when did I arrive, I understood.", "Only when I arrived did I understand."], 1, "Devrik ana cümlede."),
        mc("Hangisi doğru?", ["Not until he left I relaxed.", "Not until he left did I relax."], 1, "Not until + devrik ana cümle."),
        mc("\"Under no circumstances should you ...\" anlamı:", ["Bazı durumlarda ...", "Hiçbir koşulda ...-meyin"], 1, "Kesin yasak."),
        mc("\"At no time did I feel unsafe.\"", ["Bazen güvensiz hissettim.", "Hiçbir an kendimi güvensiz hissetmedim."], 1, "At no time."),
        gap("Only after the storm ___ we see the damage. (geçmiş)", ["did"], "Ana cümlede devrik."),
        gap("Only by working together ___ we solve this problem.", ["can"], "Only by + devrik."),
        gap("On no ___ must you tell anyone.", ["account"], "On no account."),
        gap("___ until the end of the film did I understand the title.", ["Not"], "Not until."),
        listen("Only after I had lived abroad for a year did I really appreciate my home country. Not until I was far away did I realise how much I missed my family's Sunday breakfasts.", "Konuşan ülkesinin değerini ne zaman anladı?", ["Yurt dışına gitmeden önce", "Bir yıl yurt dışında yaşadıktan sonra", "Hiç anlamadı"], 1, "\"Only after I had lived abroad for a year\""),
        typ("Devrik yapıyla yeniden yazın: \"You should not leave the building under any circumstances.\" (Under no circumstances)", variants("Under no circumstances should you leave the building.", "Under no circumstances should you leave the building!", "Under no circumstances must you leave the building."), "Under no circumstances should you leave the building."),
    ],
    {"kind": "speaking", "task": speak("(1) Bir müze, kütüphane ya da sınav salonu için 4 kuralı resmî bir dille duyurun (Under no circumstances, On no account, Only ... may, At no time). (2) Hayatınızda geç fark ettiğiniz bir şeyi Only when / Only after / Not until ile anlatın.",
                                       "Ladies and gentlemen, welcome to the museum. Please note the following rules. Under no circumstances should photographs be taken with a flash. On no account must visitors touch the paintings. Only in the café may food and drink be consumed. At no time should children be left alone. Now, something I realised too late: only when I started working did I understand how hard my parents had worked. Not until I paid my first rent did I appreciate everything they had done for me.",
                                       ["Kesin yasak yapıları", "Only / Not until + doğru devrik yeri", "Resmî duyuru tonu"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Hiç bilmiyordum ki", "Little did I know, So ... that, Such ... that devrik yapılarını ve vurgulu do / did yapısını kullanabilirim.",
    {"kind": "text", "title": "Kişisel deneme: Yanlış tren", "body": "It was a cold morning in March when I got on the train in Ankara. I was going to Konya. Or so I thought.\n\nLittle did I know that I was on a train to Kars, more than twenty hours away.\n\nSo tired was I that I fell asleep almost immediately. When I woke up, the landscape outside was covered in snow, and the passengers around me were sharing tea and bread.\n\nSuch was their kindness that within an hour I felt like part of the family. An elderly woman did warn me that I was going the wrong way, but by then it was too late to get off.\n\nI did eventually reach Konya, three days late. But I've never regretted that journey. It was the best mistake I've ever made.",
     "questions": [
        mc("Where was the train actually going?", ["To Konya", "To Kars", "To Istanbul"], 1, "\"I was on a train to Kars\""),
        mc("How does the writer feel about the journey now?", ["Angry", "It was the best mistake they've ever made.", "Embarrassed"], 1, "\"It was the best mistake I've ever made.\""),
     ]},
    {"explanation": "**1. Little did I know / Little did they realise** (= hiç bilmiyordum ki ...)\n\n- *I didn't know at all that ...* → ***Little did I know** that I was on the wrong train.*\n- ***Little did she realise** how important that day would be.*\n\nHikâye anlatımında **merak ve gerilim** yaratmak için çok kullanılır.\n\n**2. So + sıfat / zarf + devrik + that** (= o kadar ... ki)\n\n| Normal | Devrik |\n|---|---|\n| I was **so tired that** I fell asleep. | **So tired was I that** I fell asleep. |\n| He spoke **so quickly that** nobody understood. | **So quickly did he speak that** nobody understood. |\n\n**3. Such + be + isim + that** (= öyle ... idi ki)\n\n| Normal | Devrik |\n|---|---|\n| Their kindness was **so great that** ... | **Such was their kindness that** ... |\n| The noise was so loud that ... | **Such was the noise that** ... |\n\n**4. Vurgulu do / does / did** (olumlu cümlede)\n\nBir şeyin **gerçekten** olduğunu vurgular, özellikle beklentiye ters düştüğünde ya da itiraz ederken:\n\n- *She **did warn** me.* (Gerçekten uyardı, ben dinlemedim.)\n- *I **do like** your idea, but ...* (Gerçekten seviyorum, ama ...)\n- ***Do** sit down.* (Lütfen oturun. → çok kibar, resmî davet)\n\nKonuşmada **do / did** vurgulu söylenir.",
     "examples": [{"en": "Little did we know that the restaurant was about to close for good.", "tr": "Restoranın tamamen kapanmak üzere olduğunu hiç bilmiyorduk."},
                  {"en": "So beautiful was the music that several people cried.", "tr": "Müzik o kadar güzeldi ki birkaç kişi ağladı."},
                  {"en": "I did lock the door. I'm sure I did!", "tr": "Kapıyı kilitledim, gerçekten! Eminim!"}],
     "turkishNote": "Türkçede \"Hiç bilmiyordum ki...\" ifadesi, hikâyelerde merak yaratmak için kullanılır ve \"Little did I know\" ile birebir örtüşür. \"O kadar yorgundum ki\" ise günlük dilde \"I was so tired that\" olarak kalabilir; \"So tired was I that\" daha edebidir. Vurgulu \"did\" ise Türkçedeki \"Ama gerçekten kilitledim!\" ya da \"Söyledim ya!\" tonuna karşılık gelir; olumlu cümlede \"did\" görünce şaşırmayın."},
    [
        mc("\"Hiç bilmiyordum ki ...\"", ["Little I knew that ...", "Little did I know that ..."], 1, "Little did I know."),
        mc("Hangisi doğru?", ["So tired I was that I fell asleep.", "So tired was I that I fell asleep."], 1, "So + sıfat + be + özne."),
        mc("\"I did tell you!\" vurgusu:", ["Sana söylemedim.", "Sana gerçekten söyledim!"], 1, "Vurgulu did."),
        mc("Hangisi doğru?", ["Such was the noise that we couldn't sleep.", "Such the noise was that we couldn't sleep."], 0, "Such + be + isim."),
        gap("Little ___ they realise what was about to happen.", ["did"], "Little did."),
        gap("So loud ___ the music that the neighbours complained.", ["was"], "So + sıfat + was."),
        gap("___ was the demand that tickets sold out in minutes. (Öyle)", ["Such"], "Such was."),
        gap("I ___ like your plan, but I think it's too expensive. (vurgulu, present)", ["do"], "Vurgulu do."),
        listen("I know you think I forgot, but I did send the email. I sent it on Monday morning. Look, here it is in my sent folder. Little did I know that it had gone to your spam folder!", "Konuşan ne iddia ediyor?", ["E-postayı göndermeyi unuttuğunu", "E-postayı gerçekten gönderdiğini", "E-postanın hiç gelmediğini"], 1, "\"I did send the email.\""),
        typ("Devrik yapıyla yeniden yazın: \"The view was so beautiful that we stayed for hours.\" (So beautiful)", variants("So beautiful was the view that we stayed for hours.", "So beautiful was the view that we stayed there for hours."), "So beautiful was the view that we stayed for hours."),
    ],
    {"kind": "speaking", "task": speak("Beklenmedik bir şekilde gelişen bir hikâye anlatın (gerçek ya da hayalî). Little did I know ile gerilim yaratın; en az bir So ... that ve bir Such was ... that devrik yapısı kullanın; bir yerde de vurgulu did ile birinin size gerçekten bir şey söylediğini ya da yaptığını vurgulayın.",
                                       "Five years ago, I applied for a job I didn't really want, just for practice. Little did I know that it would change my life. On the day of the interview, so nervous was I that I spilled coffee on my shirt. But the manager just laughed. Such was her warmth that I immediately relaxed. My friends did tell me to wear a dark shirt, and I should have listened! I got the job, and now that manager is one of my closest friends.",
                                       ["Little did I know", "So / Such ... that devrik", "Vurgulu do / did", "Hikâye akışı"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Ölçülü vurgu", "Devrik yapıyı ve diğer vurgu araçlarını bağlama uygun ve ölçülü kullanarak etkileyici bir konuşma metni ya da makale yazabilirim.",
    {"kind": "text", "title": "Mezuniyet konuşması (alıntı)", "body": "Dear graduates, dear families, dear teachers,\n\nFour years ago, many of you walked into this building nervous, unsure and, let's be honest, a little lost. Today, you are leaving as confident young adults.\n\nNever have I been prouder of a group of students.\n\nThe last four years were not easy. Not only did you have to adapt to online classes during difficult times, but many of you also worked part-time to support your families. Rarely have I seen such determination.\n\nAnd yet, this is just the beginning. Only by continuing to learn will you keep growing. Only by staying curious will you find work that you love.\n\nYou will make mistakes. You will fail sometimes. But under no circumstances should you let failure stop you.\n\nI do believe that each of you has something unique to offer the world. Go and offer it.\n\nCongratulations.",
     "questions": [
        mc("What extra challenge did many students face?", ["They studied abroad.", "They worked part-time to support their families.", "They changed schools."], 1, "\"many of you also worked part-time to support your families\""),
        mc("What is the speaker's main message?", ["Avoid mistakes.", "Keep learning and don't let failure stop you.", "Find a well-paid job."], 1, "\"Only by continuing to learn... under no circumstances should you let failure stop you\""),
     ]},
    {"explanation": "**Devrik yapıyı ne zaman kullanmalı?**\n\n| Uygun ✓ | Uygun değil ✗ |\n|---|---|\n| Resmî konuşmalar, törenler | Arkadaşla sohbet |\n| Makaleler, köşe yazıları | Kısa mesajlar |\n| Edebi metinler, hikâyeler | Günlük e-postalar |\n| Kurallar ve uyarılar | Basit bilgi verme |\n| Sınav yazıları (C1 / C2, ölçülü) | Her paragrafta birkaç kez |\n\n**Altın kural: Az ama etkili.** Bir konuşmada ya da makalede **2–4 devrik yapı** yeterlidir. Fazlası yapay ve tekrarlı durur.\n\n**Diğer vurgu araçlarıyla dengeleyin:**\n\n| Araç | Örnek |\n|---|---|\n| **Üçleme (rule of three)** | *nervous, unsure and a little lost* |\n| **Tekrar (anaphora)** | ***Only by** continuing to learn ... **Only by** staying curious ...* |\n| **Kısa vurucu cümle** | *Go and offer it.* |\n| **Vurgulu do** | *I **do** believe that ...* |\n| **Güçlü zarflar** | *utterly, deeply, truly, absolutely* |\n| **Doğrudan hitap** | *Dear graduates, ...* |\n\n**Yapı:** Etkileyici bir açılış → bir hikâye ya da örnek → ana mesaj → çağrı (call to action) → kısa kapanış",
     "examples": [{"en": "Rarely have I seen such determination.", "tr": "Nadiren böyle bir kararlılık gördüm."},
                  {"en": "I do believe that each of you can make a difference.", "tr": "Her birinizin bir fark yaratabileceğine gerçekten inanıyorum."},
                  {"en": "We came, we learned, we grew.", "tr": "Geldik, öğrendik, büyüdük. (üçleme)"}],
     "turkishNote": "Türkçe hitabette tekrar ve üçleme çok güçlü bir gelenektir (\"Ey Türk gençliği!\" gibi). İngilizce hitabette de bu araçlar etkilidir; devrik yapı ise ekstra bir \"resmiyet ve dram\" katmanı ekler. C1 seviyesinde amaç, bu yapıları bildiğinizi göstermek değil, onları doğru anda ve ölçülü kullanmaktır. Her cümlede devrik yapı kullanan bir metin, hiç kullanmayan bir metinden daha zayıf olabilir."},
    [
        mc("Devrik yapı için en uygun bağlam:", ["Arkadaşa WhatsApp mesajı", "Mezuniyet konuşması"], 1, "Resmî / dramatik."),
        mc("Bir konuşmada kaç devrik yapı ideal?", ["2–4 tane, ölçülü", "Her cümlede"], 0, "Az ama etkili."),
        mc("\"Only by working hard ... Only by being kind ...\" hangi araç?", ["Tekrar (anaphora)", "Edilgen"], 0, "Anaphora."),
        mc("Hangisi bir üçleme?", ["We laughed, we cried and we learned.", "We laughed."], 0, "Rule of three."),
        gap("Rarely ___ I seen such talent in one room.", ["have"], "Rarely have I."),
        gap("Only by staying curious ___ you find work you love.", ["will"], "Only by + will you."),
        gap("Under no circumstances ___ you give up. (should)", ["should"], "should you."),
        gap("I ___ believe that you will succeed. (vurgulu)", ["do"], "Vurgulu do."),
        listen("Friends, never has our community faced a greater challenge. Not only have prices risen, but many local shops have also closed. But only by working together can we protect the place we call home. So tonight, I ask you: join us.", "Konuşmanın amacı ne?", ["Bilgi vermek", "Topluluğu birlikte çalışmaya çağırmak", "Bir dükkânı tanıtmak"], 1, "\"only by working together... join us\""),
        typ("Devrik yapıyla yeniden yazın: \"We can only succeed by working together.\" (Only by)", variants("Only by working together can we succeed.", "Only by working together will we succeed."), "Only by working together can we succeed."),
    ],
    {"kind": "writing", "task": write("Aşağıdakilerden birini yazın (200–250 kelime): (a) Mezun olduğunuz okulun ya da kursunuzun mezuniyet töreni için bir konuşma metni. (b) Bir dergi için \"Hayatımı değiştiren an\" başlıklı kişisel bir deneme. Ölçülü olarak 3–4 farklı devrik yapı kullanın (Never have I, Not only ... but also, Only by / Only when, Little did I know, So ... that) ve en az iki başka vurgu aracı ekleyin (üçleme, tekrar, vurgulu do, kısa vurucu cümle).",
                                      "The moment that changed my life\n\nI was nineteen, sitting on a bench outside a hospital in Izmir, waiting for news about my father. Little did I know that the next three hours would change the way I saw everything.\n\nMy father had had a heart attack at work. The doctors were calm, kind and incredibly fast. Not only did they save his life, but they also took the time to explain everything to my mother and me, step by step, in a language we could understand.\n\nSitting on that bench, I watched them work. They rushed, they listened, they comforted. Never had I seen people do something so important with so much humility.\n\nAt the time, I was studying economics, and I didn't enjoy it. Only when I saw those doctors did I realise that I wanted my work to matter to someone.\n\nIt wasn't easy. I changed universities, lost two years and had to study harder than ever before. My friends did warn me that it was a crazy decision. Maybe it was.\n\nToday, I'm a nurse in the same hospital. Every time I see a frightened family sitting on that bench, I remember how I felt. And I go and sit with them.\n\nThat's all. Just sit with them.",
                                      ["3–4 doğru devrik yapı", "Ölçülü ve bağlama uygun kullanım", "Diğer vurgu araçları", "Etkileyici yapı ve kapanış", "C1 düzeyinde dil"])},
)

u.test([
    mc("Hangisi doğru?", ["Never I have felt so happy.", "Never have I felt so happy."], 1, "Never have I"),
    mc("Hangisi doğru?", ["Rarely she goes out.", "Rarely does she go out."], 1, "does + yalın"),
    mc("Hangisi doğru?", ["No sooner had he left when she arrived.", "No sooner had he left than she arrived."], 1, "No sooner ... than"),
    mc("Hangisi doğru?", ["Only when did I arrive I saw it.", "Only when I arrived did I see it."], 1, "Devrik ana cümlede"),
    mc("Devrik yapı için en uygun bağlam:", ["Arkadaşa kısa mesaj", "Resmî bir konuşma"], 1, "Resmî"),
    gap("Not only ___ she win the race, but she also broke the record.", ["did"], "Not only did"),
    gap("Hardly had we started ___ the lights went out.", ["when"], "Hardly ... when"),
    gap("Little ___ I know that he was lying.", ["did"], "Little did I know"),
    gap("Under no ___ should you open this door.", ["circumstances"], "Under no circumstances"),
    gap("So difficult ___ the exam that nobody finished it.", ["was"], "So + sıfat + was"),
    gap("Not ___ I got home did I realise I'd lost my phone.", ["until"], "Not until"),
    mc("\"She did warn me.\" vurgusu:", ["Beni uyarmadı.", "Beni gerçekten uyardı."], 1, "Vurgulu did"),
    listen("Never before had the village seen such a celebration. Not only did the whole village come, but people also travelled from nearby towns. So loud was the music that it could be heard across the valley.", "Kutlama hakkında ne söyleniyor?", ["Küçük ve sessizdi", "Köy daha önce hiç böyle bir kutlama görmemişti", "İptal edildi"], 1, "\"Never before had the village seen such a celebration.\""),
    typ("Devrik yapıyla yeniden yazın: \"I didn't realise the truth until much later.\" (Not until)", variants("Not until much later did I realise the truth.", "Not until much later did I realize the truth."), "Not until much later did I realise the truth."),
    write("Bir yerel derginin \"Unutamadığım bir yolculuk\" köşesi için kişisel bir yazı yazın (200–250 kelime). En az 4 farklı devrik yapı (Never have I / Rarely / Not only ... but also / No sooner ... than / Hardly ... when / Only when / Little did I know / So ... that) kullanın, ama doğal ve ölçülü olsun. En az bir vurgulu do / did ve bir üçleme ekleyin.",
          "The journey I will never forget\n\nIn the summer of 2019, my best friend and I decided to cycle from Istanbul to Izmir. We had no real training, very little money and a map that was ten years old. Little did we know what we were getting ourselves into.\n\nNo sooner had we left the city than it started to pour with rain. By the end of the first day, we were wet, sore and completely lost. Not only had we taken the wrong road, but my friend's bike also had a flat tyre.\n\nThe next few days were exhausting. We climbed hills, we slept in tents, we lived on bread and tomatoes. My mother did tell me it was a terrible idea, and there were moments when I agreed with her.\n\nBut then something changed. In every village, people stopped to talk to us. They gave us tea, fruit and directions. One family even invited us to stay the night. Rarely have I felt so welcome anywhere.\n\nSo beautiful was the coastline near Ayvalık that we stayed there for two extra days.\n\nWhen we finally arrived in Izmir, eleven days after leaving home, we were thinner, browner and much wiser. Only when I got home and looked at the photos did I realise how much that journey had taught me: about my country, about strangers, and about myself.",
          ["En az 4 doğru devrik yapı", "Doğal ve ölçülü kullanım", "Vurgulu do / did ve üçleme", "Hikâye akışı", "C1 dil düzeyi"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

"""C1 Ünite 8: Haber dili."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("C1", 8, "Haber dili", "The Language of News",
         "Haber ve resmî metinlerde kişisiz edilgen yapıları (It is said that ..., He is believed to have ...) anlayıp kullanabilir, There is thought to be ve edilgen mastar / -ing yapılarını uygulayabilir, gazete başlıklarının özel dilbilgisini çözebilir ve kaynakları doğru belirten nesnel bir haber metni yazabilirim.",
         ["It is said / believed / reported that ...", "Özne + is said / thought + to V1 / to have V3", "There is thought to be ...; edilgen mastar ve -ing", "gazete başlıkları dilbilgisi ve haber kelimeleri", "nesnel haber yazımı ve kaynak belirtme"],
         ["haberler ve medya", "suç ve adalet", "olaylar ve açıklamalar"],
         {"title": "Haber merkezi", "durationMinutes": 45,
          "goal": "Gruplar bir haber ajansında çalışıyor. Her gruba doğrulanmamış bilgiler içeren bir olay kartı verilir (bir hırsızlık, bir keşif, bir ünlünün açıklaması). Gruplar bilgileri kişisiz edilgen yapılarla (is believed to have, It is reported that) haber bültenine dönüştürür ve bir başlık yazar. Sınıf en nesnel ve en etkileyici bülteni seçer."})

u.vocab([
    ("allegedly", "iddiaya göre", "He allegedly stole the money.", "İddiaya göre parayı çaldı.", "allege (fiil), allegation (isim)"),
    ("reportedly", "bildirildiğine göre", "The singer has reportedly cancelled her tour.", "Bildirildiğine göre şarkıcı turnesini iptal etti.", None),
    ("suspect", "şüpheli; şüphelenmek", "A suspect has been arrested.", "Bir şüpheli tutuklandı.", None),
    ("investigation", "soruşturma", "Police have launched an investigation.", "Polis bir soruşturma başlattı.", None),
    ("probe", "soruşturma (başlık dili)", "Bank faces probe over missing funds", "Banka kayıp fonlar nedeniyle soruşturmayla karşı karşıya", None),
    ("spokesperson", "sözcü", "A spokesperson for the company declined to comment.", "Şirket sözcüsü yorum yapmayı reddetti.", None),
    ("decline to comment", "yorum yapmayı reddetmek", "The minister declined to comment.", "Bakan yorum yapmayı reddetti.", None),
    ("confirm", "doğrulamak", "Officials have confirmed the news.", "Yetkililer haberi doğruladı.", None),
    ("deny", "yalanlamak, inkâr etmek", "He denied all the allegations.", "Bütün iddiaları yalanladı.", None),
    ("source", "kaynak", "According to a reliable source, ...", "Güvenilir bir kaynağa göre ...", None),
    ("witness", "tanık", "Witnesses said they heard an explosion.", "Tanıklar bir patlama duyduklarını söyledi.", None),
    ("casualty", "kayıp, yaralı ya da ölü", "There were no casualties.", "Kayıp yoktu.", None),
    ("injured", "yaralı", "Three people were seriously injured.", "Üç kişi ağır yaralandı.", None),
    ("evacuate", "tahliye etmek", "Hundreds of residents were evacuated.", "Yüzlerce sakin tahliye edildi.", None),
    ("vow", "yemin etmek, söz vermek (başlık dili)", "Mayor vows to fix roads", "Belediye başkanı yolları onarma sözü verdi", None),
    ("slam", "sert eleştirmek (başlık dili)", "Critics slam new tax plan", "Eleştirmenler yeni vergi planını yerden yere vurdu", None),
    ("bid", "girişim, teklif (başlık dili)", "Club in bid to sign star player", "Kulüp yıldız oyuncuyu transfer girişiminde", None),
    ("row", "anlaşmazlık, kavga (başlık dili)", "Row over new airport grows", "Yeni havalimanı üzerindeki tartışma büyüyor", "/raʊ/"),
    ("toll", "kayıp sayısı", "The death toll has risen to twelve.", "Ölü sayısı on ikiye yükseldi.", None),
    ("unconfirmed", "doğrulanmamış", "There are unconfirmed reports of an explosion.", "Doğrulanmamış patlama haberleri var.", None),
    ("in custody", "gözaltında", "The man is being held in custody.", "Adam gözaltında tutuluyor.", None),
    ("on the run", "firari", "The suspect is still on the run.", "Şüpheli hâlâ firari.", None),
    ("rumour", "söylenti", "There are rumours that the CEO will resign.", "CEO'nun istifa edeceğine dair söylentiler var.", "AmE: rumor"),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Söylendiğine göre", "It is said / believed / reported that ... yapısıyla bilgiyi kişisiz ve mesafeli bir şekilde aktarabilirim.",
    {"kind": "text", "title": "Haber: Müzeden çalınan tablo", "body": "A valuable painting has been stolen from the City Art Museum.\n\nIt is believed that the thieves entered the building through a skylight on Sunday night. It is reported that the alarm system had been switched off for maintenance.\n\nThe painting, a 19th-century landscape, is thought to be worth around two million euros. It has been suggested that the theft was carried out by a professional gang.\n\nIt is understood that police are examining security camera footage from nearby streets. It is not yet known whether anyone working at the museum was involved.\n\nA museum spokesperson declined to comment.",
     "questions": [
        mc("How did the thieves probably enter?", ["Through the main door", "Through a skylight", "Through a window"], 1, "\"through a skylight\""),
        mc("Why didn't the alarm work?", ["It was broken by the thieves.", "It had been switched off for maintenance.", "There was no alarm."], 1, "\"the alarm system had been switched off for maintenance\""),
     ]},
    {"explanation": "Haberlerde ve resmî metinlerde bilginin **kaynağı belirsizse** ya da gazeteci **mesafeli** durmak istiyorsa kişisiz edilgen yapı kullanılır.\n\n**It + is / was + V3 (reporting verb) + that + cümle**\n\n| Etken (kim söylediği belli) | Kişisiz edilgen |\n|---|---|\n| People **say** that he is rich. | **It is said that** he is rich. |\n| Police **believe** that the thieves ... | **It is believed that** the thieves ... |\n| Experts **expect** that prices will rise. | **It is expected that** prices will rise. |\n| Someone **reported** that ... | **It was reported that** ... |\n\n**Sık kullanılan fiiller:**\n\n*say, believe, think, report, claim, allege, expect, understand, know, suggest, estimate, rumour, fear, hope, consider, agree*\n\n**Zaman uyumu:**\n\n- ***It is** said **that** he **lives** abroad.* (şimdi söyleniyor, şimdi yaşıyor)\n- ***It was** reported **that** the fire **had started** in the kitchen.* (geçmişte bildirildi)\n\n**Neden kullanılır?**\n\n1. Kaynak bilinmiyor ya da önemli değil.\n2. Bilgi **doğrulanmamış**; gazeteci sorumluluk almak istemiyor.\n3. Resmî ve nesnel bir üslup.\n\n**It is not yet known whether ...** = ... olup olmadığı henüz bilinmiyor.",
     "examples": [{"en": "It is said that the castle is haunted.", "tr": "Kalenin perili olduğu söyleniyor."},
                  {"en": "It is expected that the minister will resign.", "tr": "Bakanın istifa etmesi bekleniyor."},
                  {"en": "It was reported that two people had been injured.", "tr": "İki kişinin yaralandığı bildirildi."}],
     "turkishNote": "Türkçede \"... olduğu söyleniyor\", \"... sanılıyor\", \"... bildirildi\" yapıları çok yaygındır ve İngilizcedeki \"It is said / thought / reported that\" ile birebir örtüşür. Türkçe haber dilinde ayrıca \"-mış\" eki (\"Hırsızlar çatıdan girmiş\") de bu işi görür; İngilizcede bu eke karşılık gelen tek bir yapı yoktur, bu nedenle \"It is believed that the thieves entered...\" gibi açık yapılar kullanılır."},
    [
        mc("\"Hırsızların çatıdan girdiği sanılıyor.\"", ["It is believed that the thieves entered through the roof.", "It believes that the thieves entered through the roof."], 0, "It is believed that."),
        mc("Kişisiz edilgen yapı neden kullanılır?", ["Kaynağı vurgulamak için", "Kaynak belirsiz ya da bilgi doğrulanmamış olduğunda"], 1, "Mesafe."),
        mc("Hangisi doğru?", ["It is say that he's rich.", "It is said that he's rich."], 1, "V3."),
        mc("\"It is not yet known whether ...\"", ["... olduğu biliniyor.", "... olup olmadığı henüz bilinmiyor."], 1, "not yet known."),
        gap("It is ___ (expect) that the bridge will open next year.", ["expected"], "It is expected that."),
        gap("It ___ reported yesterday that the factory had closed. (geçmiş)", ["was"], "It was reported."),
        gap("It is ___ (understand) that police are questioning a man.", ["understood"], "It is understood that."),
        gap("It is not yet ___ whether anyone was injured.", ["known"], "not yet known."),
        listen("It is reported that a large fire broke out at a factory in the industrial zone early this morning. It is believed that no one was inside at the time. It is not yet known what caused the fire.", "Yangının nedeni hakkında ne biliniyor?", ["Elektrik arızası", "Henüz bilinmiyor", "Kasten çıkarıldı"], 1, "\"It is not yet known what caused the fire.\""),
        typ("Kişisiz edilgen yapıyla yeniden yazın: \"People say that the restaurant is the best in town.\"", variants("It is said that the restaurant is the best in town.", "It's said that the restaurant is the best in town."), "It is said that the restaurant is the best in town."),
    ],
    {"kind": "speaking", "task": speak("Bir radyo spikeri olarak şehrinizde olan hayalî bir olayı (bir hırsızlık, bir keşif, bir trafik kazası) kısa bir haber bülteniyle duyurun. En az 5 farklı It + passive + that yapısı kullanın: It is believed / reported / thought / expected / understood / claimed that ... ve It is not yet known whether ...",
                                       "Good morning. Here is the news. A rare Roman mosaic has been discovered during building work in the city centre. It is believed that the mosaic dates back to the second century. It is reported that construction workers found it while digging the foundations of a new hotel. It is thought that the site may contain other ancient objects. It is expected that archaeologists will begin excavations next week. However, it is not yet known whether the hotel project will be cancelled. It is understood that the city council will meet on Friday to discuss the issue.",
                                       ["It + passive + that çeşitliliği", "Zaman uyumu", "Haber üslubu"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "Olduğuna inanılıyor", "Özne + is said / thought / believed + to V1 / to be -ing / to have V3 yapılarıyla bilgiyi daha kısa ve doğal aktarabilirim.",
    {"kind": "text", "title": "Haber: Kayıp dağcı", "body": "A British climber who went missing on Mount Ararat three days ago is believed to be alive.\n\nThe 34-year-old, who is said to be an experienced mountaineer, is thought to have left his tent early on Monday morning. He is reported to have been climbing alone when the weather suddenly changed.\n\nRescue teams are understood to be searching an area just below the summit. A shepherd is said to have seen a man in a red jacket near the glacier on Tuesday.\n\nThe climber's family, who are reported to be travelling to Turkey, are expected to arrive in Doğubayazıt tonight.\n\nThe search is likely to continue throughout the night.",
     "questions": [
        mc("What is the climber said to be?", ["A beginner", "An experienced mountaineer", "A guide"], 1, "\"is said to be an experienced mountaineer\""),
        mc("What did the shepherd see?", ["The climber's tent", "A man in a red jacket near the glacier", "A helicopter"], 1, "\"a man in a red jacket near the glacier\""),
     ]},
    {"explanation": "**Özne + be + V3 (reporting verb) + to-mastar**\n\nBu yapı \"It is said that ...\" yapısından **daha kısa ve daha yaygındır**.\n\n| It ... that | Özne + to-mastar |\n|---|---|\n| It is said that he **is** rich. | He **is said to be** rich. |\n| It is thought that she **lives** abroad. | She **is thought to live** abroad. |\n\n**Mastarın zamanı çok önemli:**\n\n| Olay ne zaman? | Mastar | Örnek |\n|---|---|---|\n| Şimdi / genel | **to + V1** | He **is said to be** an expert. |\n| Şu an devam ediyor | **to be + -ing** | Rescue teams **are understood to be searching** ... |\n| Daha önce (geçmiş) | **to have + V3** | He **is thought to have left** on Monday. |\n| Geçmişte devam ediyordu | **to have been + -ing** | He **is reported to have been climbing** alone. |\n| Edilgen, geçmiş | **to have been + V3** | Two people **are believed to have been injured**. |\n| Gelecek | **is expected to** + V1 | They **are expected to arrive** tonight. |\n\n**Dikkat:** **say** ve **think** genellikle **etken** yapıda bu şekilde kullanılmaz:\n\n- ~~People say him to be rich.~~ ✗\n- ✓ *He **is said to be** rich.*\n\n**Geçmişte söylenmişse:** *He **was said to be** the richest man in the city.* (o dönemde söyleniyordu)",
     "examples": [{"en": "The president is expected to make a statement this afternoon.", "tr": "Cumhurbaşkanının bu öğleden sonra açıklama yapması bekleniyor."},
                  {"en": "The suspect is believed to have fled the country.", "tr": "Şüphelinin ülkeden kaçtığına inanılıyor."},
                  {"en": "The company is reported to be planning major job cuts.", "tr": "Şirketin büyük çaplı işten çıkarmalar planladığı bildiriliyor."}],
     "turkishNote": "Türkçede \"Şüphelinin ülkeden kaçtığına inanılıyor\" cümlesinde özne \"şüpheli\" değildir; ama İngilizcede \"The suspect is believed to have fled\" yapısında özne doğrudan \"the suspect\" olur. Bu yapı Türkçe konuşanlar için başlangıçta garip gelebilir. Asıl zorluk mastarın zamanını seçmektir: Olay inanmadan önce olduysa \"to have + V3\" kullanılır. \"He is believed to flee\" yanlıştır; kaçma eylemi geçmişte olduğu için \"to have fled\" gerekir."},
    [
        mc("\"Şüphelinin ülkeden kaçtığına inanılıyor.\"", ["The suspect is believed to flee the country.", "The suspect is believed to have fled the country."], 1, "Geçmiş → to have + V3."),
        mc("\"Şirketin yeni bir fabrika kurmayı planladığı bildiriliyor.\" (şu an)", ["The company is reported to be planning a new factory.", "The company is reported to have planned a new factory."], 0, "Şu an devam → to be + -ing."),
        mc("Hangisi doğru?", ["People say him to be a genius.", "He is said to be a genius."], 1, "Edilgen."),
        mc("\"They are expected to arrive at six.\" olay ne zaman?", ["Geçmiş", "Gelecek"], 1, "expected to → gelecek."),
        gap("The singer is said ___ be very shy in real life.", ["to"], "is said to + V1."),
        gap("The fire is thought to ___ started in the kitchen.", ["have"], "to have + V3."),
        gap("Police are understood to be ___ (question) a local man.", ["questioning"], "to be + -ing."),
        gap("Three people are reported to have ___ injured. (edilgen)", ["been"], "to have been + V3."),
        listen("The famous footballer is reported to be in talks with a club in Spain. He is said to have rejected two offers from England last month. The deal is expected to be worth more than fifty million euros.", "Futbolcu geçen ay ne yaptı?", ["İspanya'ya transfer oldu", "İngiltere'den gelen iki teklifi reddetti", "Emekli oldu"], 1, "\"is said to have rejected two offers from England\""),
        typ("Özne + passive + to-mastar ile yeniden yazın: \"It is believed that the thieves escaped in a blue car.\"", variants("The thieves are believed to have escaped in a blue car.", "The thieves are believed to have escaped in a blue van."), "The thieves are believed to have escaped in a blue car."),
    ],
    {"kind": "speaking", "task": speak("Ünlü bir kişi hakkında (gerçek ya da hayalî) bir dedikodu programı sunucusu gibi \"söylentileri\" aktarın. Özne + is said / thought / believed / reported / rumoured + to-mastar yapısını en az 6 kez kullanın; şimdi (to be), devam eden (to be -ing), geçmiş (to have V3) ve gelecek (is expected to) zamanlarından en az birer örnek verin.",
                                       "Welcome back to Celebrity News! Today's top story: the famous actor Kaan Demir is rumoured to be leaving his hit TV series. He is said to be unhappy with the new scripts. According to sources, he is thought to have argued with the director last month. He is also reported to be working on a new film in Hollywood. His co-star is believed to have known about his decision for weeks. The actor is expected to make an announcement at the end of the season. We'll keep you updated!",
                                       ["Özne + passive + to-mastar", "Mastar zamanı doğru", "Haber / sunucu üslubu"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "Olduğu düşünülen", "There is thought to be ... yapısını, edilgen mastar (to be done) ve edilgen -ing (being done) biçimlerini doğru kullanabilirim.",
    {"kind": "text", "title": "Haber: Yeni keşfedilen mağara", "body": "Scientists have discovered an enormous cave system beneath the mountains of eastern Anatolia.\n\nThere are thought to be at least 15 kilometres of tunnels, and there is believed to be an underground lake more than 200 metres deep. There are said to be rare species of fish living in complete darkness.\n\nThe cave is likely to be explored in more detail next summer. The team leader said she was delighted to have been given the chance to lead the expedition. \"Being chosen for this project is the greatest honour of my career,\" she said.\n\nLocal authorities are keen for the area to be protected. \"We don't want the cave to be damaged by tourists before it has been properly studied,\" a spokesperson said.",
     "questions": [
        mc("What is believed to be in the cave?", ["A river", "An underground lake more than 200 metres deep", "Ancient paintings"], 1, "\"there is believed to be an underground lake\""),
        mc("What are the local authorities worried about?", ["Tourists damaging the cave", "The cost of the expedition", "Earthquakes"], 0, "\"We don't want the cave to be damaged by tourists\""),
     ]},
    {"explanation": "**1. There + be + V3 + to be**\n\n\"Var olduğu düşünülüyor / söyleniyor\" demek için:\n\n| It ... that | There + passive |\n|---|---|\n| It is thought that there **are** 15 km of tunnels. | **There are thought to be** 15 km of tunnels. |\n| It is believed that there **is** a lake. | **There is believed to be** a lake. |\n| It is said that there **were** survivors. | **There are said to have been** survivors. |\n\n**2. Edilgen mastar: to be + V3 / to have been + V3**\n\n| Yapı | Örnek |\n|---|---|\n| **want / expect / hope + to be + V3** | I **want to be told** the truth. |\n| **need to be + V3** | The cave **needs to be protected**. |\n| **is likely to be + V3** | It **is likely to be explored** next summer. |\n| **sb + to be + V3** | We don't want **the cave to be damaged**. |\n| **to have been + V3** (geçmiş) | She was delighted **to have been given** the chance. |\n\n**3. Edilgen -ing: being + V3 / having been + V3**\n\n| Yapı | Örnek |\n|---|---|\n| **Being + V3** (özne) | **Being chosen** is a great honour. |\n| **hate / love / avoid / remember + being + V3** | I hate **being interrupted**. |\n| **without being + V3** | He left **without being seen**. |\n| **having been + V3** (geçmiş) | **Having been warned**, they stayed inside. |",
     "examples": [{"en": "There are thought to be more than 1,000 species in the forest.", "tr": "Ormanda 1.000'den fazla tür olduğu düşünülüyor."},
                  {"en": "Nobody likes being told what to do.", "tr": "Kimse ne yapacağının söylenmesinden hoşlanmaz."},
                  {"en": "The results are expected to be published next month.", "tr": "Sonuçların gelecek ay yayımlanması bekleniyor."}],
     "turkishNote": "Türkçede \"15 kilometre tünel olduğu düşünülüyor\" cümlesi İngilizcede \"There are thought to be 15 km of tunnels\" olur; \"there\" yapısının edilgen hale gelmesi Türkçe konuşanlar için alışılmadık olabilir. Edilgen -ing yapıları da Türkçede \"-ılmak\" (söz kesilmek, seçilmek) ile karşılanır: \"Sözümün kesilmesinden nefret ederim\" = \"I hate being interrupted\". \"I hate interrupting\" ise \"Söz kesmekten nefret ederim\" demektir; anlamı tamamen farklıdır."},
    [
        mc("\"Hayatta kalanlar olduğu düşünülüyor.\"", ["There are thought to be survivors.", "There think to be survivors."], 0, "There are thought to be."),
        mc("\"Sözümün kesilmesinden nefret ederim.\"", ["I hate interrupting.", "I hate being interrupted."], 1, "being + V3."),
        mc("Hangisi doğru?", ["I want to tell the truth. (Bana doğru söylensin.)", "I want to be told the truth."], 1, "Edilgen mastar."),
        mc("\"He left without being seen.\"", ["Kimseyi görmeden ayrıldı.", "Görülmeden ayrıldı."], 1, "Edilgen -ing."),
        gap("There ___ believed to be a hidden room in the castle.", ["is"], "There is believed to be."),
        gap("The report is expected to ___ published on Monday.", ["be"], "to be + V3."),
        gap("She was proud to have ___ chosen for the team.", ["been"], "to have been + V3."),
        gap("I don't like ___ (be) photographed.", ["being"], "being + V3."),
        listen("There are said to be more than 300 people still waiting for help after the floods. Many homes need to be rebuilt, and roads are unlikely to be reopened before next week. One resident said she was lucky to have been rescued so quickly.", "Yollar hakkında ne söyleniyor?", ["Bugün açılacak", "Gelecek haftadan önce açılması pek olası değil", "Hiç kapanmadı"], 1, "\"roads are unlikely to be reopened before next week\""),
        typ("There + passive ile yeniden yazın: \"It is thought that there are hundreds of birds on the island.\"", variants("There are thought to be hundreds of birds on the island.", "There are thought to be hundreds of birds on this island."), "There are thought to be hundreds of birds on the island."),
    ],
    {"kind": "speaking", "task": speak("(1) Yeni keşfedilmiş hayalî bir yer (bir ada, bir orman, bir şehir kalıntısı) hakkında There is / are thought / believed / said to be ... yapısıyla en az 3 cümle kurun. (2) Kendinizle ilgili sevdiğiniz ve sevmediğiniz 3'er şeyi edilgen -ing ile söyleyin (I love being ..., I hate being ...). (3) Edilgen mastarla 2 dilek söyleyin (I want to be ..., I'd like to be ...).",
                                       "One: Scientists have found a small island in the Pacific. There are thought to be several species of birds that live nowhere else. There is believed to be fresh water in the centre of the island, and there are said to be the remains of an old village. Two: I love being surprised, I love being invited to dinner, and I love being given flowers. I hate being interrupted, I hate being kept waiting, and I really hate being woken up early. Three: I'd like to be promoted next year, and I want to be told the truth, even when it's difficult.",
                                       ["There + passive", "Edilgen -ing", "Edilgen mastar", "Doğru anlam"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Başlıkları çözmek", "Gazete başlıklarının özel dilbilgisini (atlanan kelimeler, zaman kuralları) ve tipik başlık kelimelerini anlayabilirim.",
    {"kind": "text", "title": "Bugünün manşetleri", "body": "1. MAYOR VOWS TO FIX CITY ROADS BY SUMMER\n\n2. THREE HURT IN MOTORWAY CRASH\n\n3. PM TO VISIT JAPAN NEXT MONTH\n\n4. CRITICS SLAM NEW TAX PLAN\n\n5. STAR STRIKER IN BID TO JOIN SPANISH CLUB\n\n6. ROW OVER AIRPORT EXPANSION GROWS\n\n7. BANK BOSS QUITS AMID FRAUD PROBE\n\n8. TEENAGER SAVES DROWNING CHILD\n\n9. MISSING CLIMBER FOUND ALIVE",
     "questions": [
        mc("Headline 3 means:", ["The PM visited Japan.", "The PM will visit Japan.", "The PM is in Japan now."], 1, "to + V1 → gelecek."),
        mc("Headline 9 means:", ["Someone found the climber alive.", "The climber found something."], 0, "Edilgen, is atlanmış."),
     ]},
    {"explanation": "**Gazete başlıkları (headlines)** yer kazanmak için özel bir dilbilgisi kullanır.\n\n**1. Kelimeler atlanır:**\n\n- **Article** (a, the): *~~The~~ Mayor vows to fix ~~the~~ roads*\n- **be fiili**: *Missing climber ~~is~~ found alive*\n\n**2. Zaman kuralları:**\n\n| Başlık | Gerçek anlam | Kural |\n|---|---|---|\n| Teenager **saves** child | A teenager **has saved / saved** a child. | **Present simple → yakın geçmiş** |\n| PM **to visit** Japan | The PM **is going to / will** visit Japan. | **to + V1 → gelecek** |\n| Three **hurt** in crash | Three people **were / have been hurt**. | **V3 → edilgen** (be atlanmış) |\n| Row over airport **grows** | The row **is growing**. | Present simple → şimdi |\n\n**3. Kısa ve dramatik kelimeler (\"headlinese\"):**\n\n| Başlık kelimesi | Normal anlam |\n|---|---|\n| **vow** | promise |\n| **slam** | criticise strongly |\n| **bid** | attempt |\n| **row** | argument / disagreement |\n| **probe** | investigation |\n| **quit** | resign |\n| **axe** | cut / cancel (jobs, plans) |\n| **back** | support |\n| **clash** | fight / disagree |\n| **hit** | affect badly |\n| **boost** | increase, help |\n| **amid** | during, while (a problem) |\n\n**4. İsim dizileri:** *Bank boss fraud probe* = an investigation into fraud involving the boss of a bank",
     "examples": [{"en": "Government to axe 500 jobs = The government is going to cut 500 jobs.", "tr": "Hükümet 500 kişiyi işten çıkaracak."},
                  {"en": "Storm hits coast = A storm has hit the coast.", "tr": "Fırtına kıyıyı vurdu."},
                  {"en": "Minister backs new plan = The minister supports the new plan.", "tr": "Bakan yeni planı destekliyor."}],
     "turkishNote": "Türkçe gazete başlıkları da kısa ve dramatiktir (\"Bakan istifa etti\", \"Şehir sele teslim\"). İngilizce başlıkların en kafa karıştırıcı yanı zaman kurallarıdır: \"Teenager saves child\" şimdiki zaman gibi görünse de aslında geçmişte olmuş bir olayı anlatır. \"PM to visit Japan\" ise gelecek planıdır. Bir başka tuzak \"row\" kelimesidir: Başlıklarda \"kürek çekmek\" değil, \"tartışma, kavga\" anlamına gelir ve /raʊ/ diye okunur."},
    [
        mc("\"Teenager saves drowning child\" olay ne zaman?", ["Şimdi oluyor", "Geçmişte oldu (yakın geçmiş)"], 1, "Present simple → geçmiş."),
        mc("\"Minister to resign\" anlamı:", ["Bakan istifa etti.", "Bakan istifa edecek."], 1, "to + V1 → gelecek."),
        mc("\"Critics slam plan\" anlamı:", ["Eleştirmenler planı sert eleştirdi.", "Eleştirmenler planı kapattı."], 0, "slam."),
        mc("\"Row over new stadium\" row:", ["Kürek çekmek", "Tartışma"], 1, "row = argument."),
        gap("Başlık: \"Bank boss ___ amid scandal\" (istifa etti)", ["quits"], "quit = resign."),
        gap("Başlık: \"Police launch ___ into missing funds\" (soruşturma)", ["probe"], "probe."),
        gap("Başlık: \"Mayor ___ to build new hospital\" (söz verdi)", ["vows"], "vow."),
        gap("Başlık: \"Company to ___ 200 jobs\" (kesmek, iptal etmek)", ["axe", "cut"], "axe."),
        match([("probe", "investigation"), ("slam", "criticise strongly"), ("bid", "attempt"), ("quit", "resign"), ("back", "support")], "Başlık kelimelerini anlamlarıyla eşleştirin."),
        listen("And now, the headlines. Flooding hits eastern villages. Government to announce new housing plan on Friday. And in sport, national team coach quits after shock defeat.", "Milli takım teknik direktörü hakkında ne söyleniyor?", ["Yeni bir sözleşme imzaladı", "Şok yenilginin ardından istifa etti", "İstifa edecek"], 1, "\"coach quits after shock defeat\""),
    ],
    {"kind": "speaking", "task": speak("(1) Aşağıdaki başlıkları tam cümlelerle açıklayın: \"Storm hits coast\", \"PM to visit Brazil\", \"Five hurt in fire\", \"Club in bid to sign star\", \"Teachers slam exam changes\". (2) Ardından şehrinizde ya da okulunuzda geçen hafta olan 3 olay için kendi gazete başlıklarınızı oluşturun ve okuyun.",
                                       "One: 'Storm hits coast' means a storm has hit the coast. 'PM to visit Brazil' means the Prime Minister is going to visit Brazil. 'Five hurt in fire' means five people were hurt in a fire. 'Club in bid to sign star' means a club is trying to sign a star player. 'Teachers slam exam changes' means teachers have strongly criticised the changes to the exams. Two: My headlines: 'Local café wins national award', 'School to open new science lab', and 'Residents slam plans for car park'.",
                                       ["Başlık zaman kuralları", "Başlık kelimelerinin anlamı", "Kendi başlıklarını oluşturma"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Haber yazmak", "Ters piramit yapısı, kaynak belirtme ve kişisiz edilgen yapılarla nesnel bir haber metni yazabilirim.",
    {"kind": "text", "title": "Örnek haber", "body": "HUNDREDS EVACUATED AS WILDFIRE SPREADS\n\nMore than 800 residents were evacuated from villages near Muğla yesterday as a wildfire spread rapidly through nearby forests.\n\nThe fire, which is believed to have started in a field on Tuesday afternoon, has already destroyed an estimated 500 hectares of pine forest. Strong winds are thought to have helped it spread.\n\nAccording to the regional governor's office, 12 helicopters and more than 300 firefighters are currently working to control the flames. No casualties have been reported, although two firefighters are said to have been treated for smoke inhalation.\n\nThe cause of the fire has not yet been confirmed. However, officials have not ruled out the possibility that it was started deliberately. An investigation has been launched.\n\n\"We have never seen a fire spread so fast,\" said Hasan Yıldız, a farmer from one of the evacuated villages. \"We left with nothing.\"\n\nThe fire is expected to be brought under control by the weekend, provided the wind drops.",
     "questions": [
        mc("How many residents were evacuated?", ["About 300", "More than 800", "12"], 1, "\"More than 800 residents were evacuated\""),
        mc("What is said about the cause?", ["It was definitely an accident.", "It has not yet been confirmed.", "Lightning started it."], 1, "\"The cause of the fire has not yet been confirmed.\""),
     ]},
    {"explanation": "**Ters piramit (inverted pyramid) yapısı:**\n\n| Bölüm | İçerik | Örnek |\n|---|---|---|\n| **Başlık** | Kısa, dramatik (başlık dilbilgisi) | *Hundreds evacuated as wildfire spreads* |\n| **Giriş (lead)** | En önemli bilgi: **Ne? Kim? Nerede? Ne zaman?** | *More than 800 residents were evacuated ... yesterday ...* |\n| **Ayrıntılar** | **Nasıl? Neden?** + rakamlar | *The fire, which is believed to have started ...* |\n| **Kaynaklar** | Resmî açıklamalar | *According to the governor's office, ...* |\n| **Alıntı** | Tanık ya da uzman sözü | *\"We left with nothing,\" said ...* |\n| **Sonraki adım** | Ne olacak? | *The fire is expected to be brought under control ...* |\n\n**Kaynak belirtme dili:**\n\n| Yapı | Örnek |\n|---|---|\n| **According to** + kaynak | *According to police, ...* |\n| **X said / told reporters / confirmed** | *a spokesperson told reporters* |\n| **in a statement** | *In a statement, the company said ...* |\n| **declined to comment** | *The minister declined to comment.* |\n| **has not been confirmed** | *The cause **has not yet been confirmed**.* |\n| **have not ruled out** | *Officials **have not ruled out** ...* |\n\n**Nesnellik:**\n\n- Kişisel görüş yok: ~~This terrible fire ...~~\n- Doğrulanmamış bilgi için kişisiz edilgen: *is believed to / is thought to*\n- Duygu sadece **alıntılarda**: *\"We left with nothing,\" said ...*\n- **Rakamlar ve kesin bilgiler**: *an estimated 500 hectares*",
     "examples": [{"en": "According to police, the man was arrested at the scene.", "tr": "Polise göre adam olay yerinde tutuklandı."},
                  {"en": "Officials have not ruled out the possibility of sabotage.", "tr": "Yetkililer sabotaj ihtimalini göz ardı etmedi."},
                  {"en": "In a statement, the company apologised to its customers.", "tr": "Şirket yaptığı açıklamada müşterilerinden özür diledi."}],
     "turkishNote": "Türkçe haber metinleri bazen duygusal sıfatlar (\"korkunç yangın\", \"acı olay\") ve yazarın yorumlarıyla başlar. İngilizce haber yazımında (özellikle ajans haberlerinde) duygular alıntılara bırakılır ve gazeteci nesnel kalır. Ayrıca İngilizce haberlerde kaynak belirtmek çok önemlidir: Doğrulanmamış her bilgi \"is believed to\", \"according to\" ya da \"has not been confirmed\" ile işaretlenir."},
    [
        mc("Haberin girişinde (lead) ne olmalı?", ["Bir tanığın duyguları", "Ne, kim, nerede, ne zaman"], 1, "En önemli bilgiler."),
        mc("Nesnel bir haber cümlesi:", ["This terrible fire has destroyed our beautiful forests.", "The fire has destroyed an estimated 500 hectares of forest."], 1, "Nesnel."),
        mc("Doğrulanmamış bilgi:", ["The fire started in a field.", "The fire is believed to have started in a field."], 1, "Kişisiz edilgen."),
        mc("Duygular haberde nerede yer alır?", ["Alıntılarda", "Başlıkta ve girişte"], 0, "Alıntılar."),
        gap("___ to the police, two men were arrested. (göre)", ["According"], "According to."),
        gap("The cause has not yet been ___. (doğrulanmak)", ["confirmed"], "has not been confirmed."),
        gap("Officials have not ruled ___ the possibility of arson.", ["out"], "rule out."),
        gap("A company spokesperson ___ to comment. (reddetti)", ["declined", "refused"], "declined to comment."),
        listen("Police have arrested a 45-year-old man in connection with the bank robbery in the city centre last Friday. According to a police statement, the man was arrested at his home early this morning. Two other suspects are believed to be on the run. The stolen money has not yet been recovered.", "Diğer iki şüpheli hakkında ne biliniyor?", ["Tutuklandılar", "Firari oldukları düşünülüyor", "Teslim oldular"], 1, "\"Two other suspects are believed to be on the run.\""),
        typ("Nesnel hale getirin: \"The horrible storm destroyed loads of houses.\" (an estimated 50)", variants("The storm destroyed an estimated 50 houses.", "An estimated 50 houses were destroyed by the storm.", "The storm is believed to have destroyed an estimated 50 houses."), "The storm destroyed an estimated 50 houses."),
    ],
    {"kind": "writing", "task": write("Hayalî bir olay hakkında bir gazete haberi yazın (180–220 kelime): bir sel, bir keşif, ünlü bir hırsızlık ya da bir kurtarma operasyonu. Başlık dilbilgisiyle bir başlık yazın; ters piramit yapısını kullanın (lead, ayrıntılar, kaynaklar, alıntı, sonraki adım). En az 3 Özne + passive + to-mastar (is believed to have, is reported to be), en az 2 It is ... that ya da There is thought to be yapısı ve en az 2 kaynak belirtme ifadesi kullanın. Nesnel kalın; duyguyu yalnızca alıntıya bırakın.",
                                      "FISHERMEN RESCUED AFTER TWO DAYS AT SEA\n\nThree fishermen who had been missing off the Black Sea coast since Sunday were rescued yesterday morning, about 40 kilometres north of Sinop.\n\nThe men, aged between 28 and 56, are believed to have lost power after their boat's engine failed in rough weather on Sunday evening. They are reported to have survived on rainwater and a small supply of bread.\n\nAccording to the coast guard, the men were spotted by a passing cargo ship, whose crew raised the alarm. A rescue helicopter reached the boat within an hour. All three are said to be in good condition, although one is thought to have suffered a minor hand injury.\n\nIt is understood that the boat's radio had stopped working shortly after the engine failure. There are thought to have been several other boats in the area at the time, but none of them had noticed the men's signals.\n\n\"We had almost given up hope,\" said Ali Kara, the youngest of the three. \"When we saw the ship, we just cried.\"\n\nIn a statement, the coast guard reminded all fishermen to check the weather forecast carefully before going out to sea. An investigation into the engine failure is expected to be completed next week.",
                                      ["Başlık dilbilgisi", "Ters piramit yapısı", "Özne + passive + to-mastar", "It ... that / There is thought to be", "Kaynak belirtme ve nesnellik"])},
)

u.test([
    mc("\"Kalenin perili olduğu söyleniyor.\"", ["It says that the castle is haunted.", "It is said that the castle is haunted."], 1, "It is said that"),
    mc("\"Şüphelinin ülkeden kaçtığına inanılıyor.\"", ["The suspect is believed to flee the country.", "The suspect is believed to have fled the country."], 1, "to have + V3"),
    mc("\"Minister to resign\" başlığının anlamı:", ["Bakan istifa etti.", "Bakan istifa edecek."], 1, "to + V1 → gelecek"),
    mc("\"I hate being interrupted.\"", ["Söz kesmekten nefret ederim.", "Sözümün kesilmesinden nefret ederim."], 1, "Edilgen -ing"),
    mc("Nesnel haber cümlesi:", ["This shocking crime has upset everyone.", "Police are investigating the crime."], 1, "Nesnel"),
    gap("It is ___ (expect) that the new law will be passed next week.", ["expected"], "It is expected that"),
    gap("The company is reported ___ be planning job cuts.", ["to"], "to be + -ing"),
    gap("Two people are thought to have ___ injured.", ["been"], "to have been + V3"),
    gap("There ___ said to be a secret tunnel under the palace.", ["is"], "There is said to be"),
    gap("___ to a police statement, the man was arrested at home.", ["According"], "According to"),
    gap("A spokesperson ___ to comment.", ["declined", "refused"], "declined to comment"),
    mc("\"Critics slam new law\"", ["Eleştirmenler yeni yasayı sert eleştirdi.", "Eleştirmenler yeni yasayı kapattı."], 0, "slam"),
    listen("A rare painting is reported to have been found in the attic of a house in Bursa. The painting is thought to be more than 300 years old. It is not yet known how it got there. Experts are expected to examine it next week.", "Uzmanlar ne zaman tabloyu inceleyecek?", ["Bugün", "Gelecek hafta", "Çoktan incelediler"], 1, "\"Experts are expected to examine it next week.\""),
    typ("Özne + passive + to-mastar ile yeniden yazın: \"It is said that the actor is very generous.\"", variants("The actor is said to be very generous.", "The actor's said to be very generous."), "The actor is said to be very generous."),
    write("Okulunuzda, şirketinizde ya da mahallenizde olan hayalî bir olay hakkında bir yerel gazete haberi yazın (180–220 kelime). Başlık dilbilgisiyle bir başlık, ters piramit yapısı, en az 3 Özne + passive + to-mastar, en az 2 It is ... that / There is thought to be yapısı, en az 2 kaynak belirtme ifadesi ve bir alıntı kullanın. Nesnel kalın.",
          "LOCAL BAKERY WINS NATIONAL BREAD AWARD\n\nA small family bakery in Eskişehir has been named the best bakery in Turkey at this year's national bread competition, held in Ankara on Saturday.\n\nThe bakery, which is said to have been founded in 1962, beat more than 400 other businesses from across the country. Its sourdough loaf is believed to be made using a recipe that has not changed for three generations.\n\nAccording to the competition organisers, the judges were particularly impressed by the bread's flavour and texture. It is understood that the bakery uses only local flour, and there are thought to be just four people working there, all of them members of the same family.\n\nThe owner, Fatma Özkan, 64, is reported to have started working in the bakery at the age of twelve. \"I still can't believe it,\" she told reporters. \"My father would have been so proud.\"\n\nIn a statement, the mayor of Eskişehir congratulated the family and said the award would \"put the city on the map\".\n\nSince the news broke, queues are reported to have formed outside the bakery every morning. The family is expected to open a second shop later this year.",
          ["Başlık dilbilgisi", "Ters piramit", "Kişisiz edilgen yapılar", "Kaynak belirtme ve alıntı", "Nesnellik"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

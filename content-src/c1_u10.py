"""C1 Ünite 10: Doğal konuşma."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("C1", 10, "Doğal konuşma", "Natural Conversation",
         "Tekrardan kaçınmak için yerine koyma (one, so, not, do so) ve eksiltme (ellipsis) kullanabilir, konuşmada kısa ve doğal cevaplar verebilir, yankı soruları ve dinleyici tepkileriyle sohbeti sürdürebilir ve yazıda the former / the latter, such gibi araçlarla metni akıcı hale getirebilirim.",
         ["yerine koyma: one / ones, so / not", "yardımcı fiille eksiltme ve do so", "konuşmada durumsal eksiltme ve to ile biten cevaplar", "yankı soruları ve dinleyici tepkileri", "yazıda tekrardan kaçınma: the former / the latter, such, this"],
         ["günlük sohbet", "arkadaşlık", "yazılı iletişim"],
         {"title": "Kısa ama doğal", "durationMinutes": 45,
          "goal": "Öğrenciler ikili gruplarda \"uzun ve tekrarlı\" yazılmış bir diyaloğu (her cevap tam cümle) eksiltme ve yerine koyma ile doğal hale getirir, sonra canlandırır. İkinci bölümde öğretmen kısa haberler okur; öğrenciler yankı soruları ve dinleyici tepkileriyle (Did you? / Really? / No way!) sohbeti en az üç tur sürdürür."})

u.vocab([
    ("ellipsis", "eksiltme", "Ellipsis makes conversation sound natural.", "Eksiltme konuşmayı doğal kılar.", "Dilbilgisi terimi; ayrıca \"üç nokta\" (...) anlamına da gelir."),
    ("substitution", "yerine koyma", "\"One\" is often used for substitution.", "\"One\" sıklıkla yerine koyma için kullanılır.", None),
    ("I think so", "sanırım öyle", "\"Is she coming?\" \"I think so.\"", "\"Geliyor mu?\" \"Sanırım.\"", None),
    ("I hope not", "umarım hayır", "\"Will it rain?\" \"I hope not.\"", "\"Yağmur yağacak mı?\" \"Umarım yağmaz.\"", None),
    ("I'm afraid so", "maalesef evet", "\"Is the flight cancelled?\" \"I'm afraid so.\"", "\"Uçuş iptal mi?\" \"Maalesef evet.\"", None),
    ("I doubt it", "pek sanmıyorum", "\"Will he call back?\" \"I doubt it.\"", "\"Geri arar mı?\" \"Pek sanmıyorum.\"", None),
    ("I'd love to", "çok isterim", "\"Do you want to come?\" \"I'd love to.\"", "\"Gelmek ister misin?\" \"Çok isterim.\"", None),
    ("do so", "bunu yapmak (resmî)", "If you wish to leave, please do so quietly.", "Ayrılmak isterseniz lütfen sessizce ayrılın.", None),
    ("the former", "ilki, ilk bahsedilen", "Of the two options, the former is cheaper.", "İki seçenekten ilki daha ucuz.", None),
    ("the latter", "ikincisi, son bahsedilen", "Tea or coffee? I prefer the latter.", "Çay mı kahve mi? İkincisini tercih ederim.", None),
    ("such", "böyle, bu tür", "Such problems are common.", "Bu tür sorunlar yaygın.", None),
    ("echo question", "yankı sorusu", "\"I've quit my job.\" \"Have you?\"", "\"İşimi bıraktım.\" \"Öyle mi?\"", None),
    ("No way!", "Olamaz! / Yok artık!", "\"I won the lottery.\" \"No way!\"", "\"Piyangoyu kazandım.\" \"Yok artık!\"", None),
    ("Fair enough.", "Haklısın / Makul.", "\"I'm too tired to go out.\" \"Fair enough.\"", "\"Dışarı çıkamayacak kadar yorgunum.\" \"Anlıyorum, makul.\"", None),
    ("Fingers crossed.", "Umarım / Şans dile.", "\"I hope I get the job.\" \"Fingers crossed!\"", "\"Umarım işi alırım.\" \"İnşallah!\"", None),
    ("Sounds good.", "Kulağa iyi geliyor.", "\"Dinner at eight?\" \"Sounds good.\"", "\"Sekizde yemek?\" \"Olur, güzel.\"", None),
    ("Tell me about it!", "Bana mı anlatıyorsun! (katılma)", "\"This traffic is awful.\" \"Tell me about it!\"", "\"Bu trafik berbat.\" \"Hiç sorma!\"", None),
    ("Same here.", "Ben de.", "\"I'm starving.\" \"Same here.\"", "\"Açlıktan ölüyorum.\" \"Ben de.\"", None),
    ("I suppose so", "herhalde, öyle sanırım (isteksiz)", "\"Can you help?\" \"I suppose so.\"", "\"Yardım edebilir misin?\" \"Eh, ederim herhalde.\"", None),
    ("backchannel", "dinleyici tepkisi (mm, right, I see)", "Backchannels show that you are listening.", "Dinleyici tepkileri dinlediğinizi gösterir.", None),
    ("repetition", "tekrar", "Good writers avoid unnecessary repetition.", "İyi yazarlar gereksiz tekrardan kaçınır.", None),
    ("cohesion", "metin bağlılığı", "Pronouns and linkers improve cohesion.", "Zamirler ve bağlaçlar metin bağlılığını artırır.", None),
    ("mind you", "gerçi, ama şunu da söyleyeyim", "It's expensive. Mind you, it's very good.", "Pahalı. Gerçi çok iyi.", None),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "one / ones ve so / not", "İsimleri tekrar etmemek için one / ones, cümleleri tekrar etmemek için so ve not kullanabilirim.",
    {"kind": "dialogue", "title": "Telefon dükkânında", "lines": [
        {"speaker": "Assistant", "text": "Can I help you?"},
        {"speaker": "Defne", "text": "Yes, I'm looking for a new phone. My old one keeps switching off."},
        {"speaker": "Assistant", "text": "Do you want a big one or a small one?"},
        {"speaker": "Defne", "text": "A small one, ideally. What about the ones in the window?"},
        {"speaker": "Assistant", "text": "The black one is on sale this week."},
        {"speaker": "Defne", "text": "Does it have a good camera?"},
        {"speaker": "Assistant", "text": "I think so. It's had very good reviews."},
        {"speaker": "Defne", "text": "Is the price going to go up next week?"},
        {"speaker": "Assistant", "text": "I'm afraid so. The offer ends on Sunday."},
        {"speaker": "Defne", "text": "And will I need a new charger?"},
        {"speaker": "Assistant", "text": "I don't think so. Your old one should work."}],
     "questions": [
        mc("What is wrong with Defne's old phone?", ["It keeps switching off.", "The screen is broken.", "It's too big."], 0, "\"My old one keeps switching off.\""),
        mc("Will Defne need a new charger?", ["Yes, definitely.", "Probably not.", "The assistant doesn't know."], 1, "\"I don't think so.\""),
     ]},
    {"explanation": "**1. one / ones (isim yerine):** Sayılabilen bir ismi tekrar etmemek için.\n\n| Tekil | Çoğul |\n|---|---|\n| a big **one** | the **ones** in the window |\n| my old **one** | the red **ones** |\n| this **one** / that **one** | these (**ones**) / those (**ones**) |\n| **Which one?** | **Which ones?** |\n\n**Dikkat:**\n\n- Sayılamayan isimlerle **kullanılmaz**: *I like white wine more than red* (✗ *red one*).\n- Tek başına \"a\" ile: *I need **one**.* (✗ *I need a one.*); ama sıfat varsa: *I need **a new one**.*\n- İyelik sıfatlarından sonra genellikle kullanılmaz: *This is **mine**.* (✗ *my one* gayri resmî)\n\n**2. so / not (cümle yerine):** Düşünce ve tahmin fiilleriyle bir önceki cümleyi tekrar etmemek için.\n\n| Olumlu | Olumsuz |\n|---|---|\n| I think **so**. | I don't think **so**. (daha doğal) / I think **not**. (resmî) |\n| I hope **so**. | I hope **not**. (✗ *I don't hope so*) |\n| I'm afraid **so**. | I'm afraid **not**. |\n| I suppose **so**. | I suppose **not**. / I don't suppose **so**. |\n| I expect **so**. | I don't expect **so**. |\n| I guess **so**. | I guess **not**. |\n| Probably. / Probably **not**. | |\n\n**Not:** *hope* ve *afraid* ile olumsuz hep **not** ile yapılır: *I hope not, I'm afraid not.* *think, expect, believe* ile ise genelde **don't ... so**: *I don't think so.*\n\n**so** *know* ile kullanılmaz: \"Is he coming?\" \"*I don't know.*\" (✗ *I don't know so.*)",
     "examples": [{"en": "\"Is the shop open on Sundays?\" \"I don't think so.\"", "tr": "\"Dükkân pazar açık mı?\" \"Sanmıyorum.\""},
                  {"en": "\"Are we going to be late?\" \"I hope not.\"", "tr": "\"Geç mi kalacağız?\" \"Umarım kalmayız.\""},
                  {"en": "These shoes are too tight. Do you have bigger ones?", "tr": "Bu ayakkabılar çok dar. Daha büyükleri var mı?"}],
     "turkishNote": "Türkçede \"Sanırım\", \"Umarım\", \"Maalesef\" tek başına cevap olabilir. İngilizcede ise genellikle \"so\" ya da \"not\" eklenmesi gerekir: \"I think so\", \"I hope so\". Türk öğrencilerin en sık hatası \"I hope\" ya da \"I think\" diyip bırakmak ya da olumsuzu \"I don't hope so\" şeklinde kurmaktır. Doğrusu: \"I hope not.\" Ayrıca Türkçedeki \"büyüğü\", \"kırmızısı\" gibi yapılar İngilizcede \"the big one\", \"the red one\" olur; \"one\" atlanmaz."},
    [
        mc("\"Will it rain tomorrow?\" (Olumsuz umut)", ["I don't hope so.", "I hope not."], 1, "I hope not."),
        mc("\"Is the museum free?\" (Olumsuz düşünce, doğal)", ["I don't think so.", "I think not so."], 0, "I don't think so."),
        mc("Doğru olan:", ["I prefer red wine to white one.", "I prefer red wine to white."], 1, "Sayılamayan isimle one yok."),
        mc("Doğru olan:", ["I need a new one.", "I need a one."], 0, "Sıfat + one."),
        gap("\"Is the train delayed?\" \"I'm afraid ___. About 20 minutes.\"", ["so"], "I'm afraid so."),
        gap("\"Will they cancel the concert?\" \"I hope ___.\"", ["not"], "I hope not."),
        gap("These glasses are dirty. Can I have some clean ___?", ["ones"], "ones."),
        gap("\"Which jacket do you like?\" \"The blue ___.\"", ["one"], "one."),
        listen("Is there a bank near here? I think so. There's one next to the post office, I believe. Is it open on Saturdays? Hmm, I don't think so, but the one in the shopping centre is.", "Cumartesi açık olan banka nerede?", ["Postanenin yanında", "Alışveriş merkezinde", "Hiçbiri açık değil"], 1, "\"the one in the shopping centre is\""),
        match([("Will it be expensive?", "I'm afraid so."), ("Is she ill?", "I hope not."), ("Have we got enough time?", "I think so."), ("Can you lend me your car?", "I suppose so."), ("Will he apologise?", "I doubt it.")], "Her soruyu en uygun cevapla eşleştirin."),
    ],
    {"kind": "speaking", "task": speak("Bir arkadaşınız size hafta sonu planları hakkında sorular soruyor. Her soruya so / not ile kısa ve doğal cevap verin, sonra bir cümle ekleyin: (1) Is it going to rain at the weekend? (2) Will the shops be busy? (3) Are you going to see Murat? (4) Is the new café any good? (5) Do you need a new coat? (one / ones kullanın)",
                                       "One: I hope not! I'm planning to go hiking. Two: I'm afraid so. It's the start of the sales. Three: I think so. He said he'd call me. Four: I don't think so, actually. My sister went last week and said the coffee was terrible. Five: I suppose so. My old one is falling apart, so I need a warmer one for the winter.",
                                       ["so / not doğru", "hope not / don't think so", "one / ones", "Doğal ek cümle"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "Yardımcı fiille eksiltme ve do so", "Fiil öbeğini tekrar etmemek için yardımcı fiille eksiltme (I can't, but she can) ve do so / do that yapılarını kullanabilirim.",
    {"kind": "text", "title": "İki kardeş", "body": "My brother and I are very different. He can cook brilliantly; I can't. I've never been abroad, but he has, many times. He wanted to study medicine, and he did. I wanted to become a musician, but I didn't, in the end. People often ask if we get on well. We do, surprisingly. He thinks I should travel more, and maybe he's right. I've promised to do so next year. Mind you, I said that last year too.",
     "questions": [
        mc("Who can cook well?", ["The writer", "The writer's brother", "Both of them"], 1, "\"He can cook brilliantly; I can't.\""),
        mc("Did the writer become a musician?", ["Yes", "No"], 1, "\"I wanted to become a musician, but I didn't\""),
     ]},
    {"explanation": "**1. Yardımcı fiille eksiltme:** Bir önceki fiil öbeği anlaşıldığında, sadece yardımcı fiili söyleriz.\n\n| Tam cümle | Eksiltilmiş |\n|---|---|\n| He can cook; I can't cook. | He can cook; **I can't**. |\n| I haven't been abroad, but he has been abroad. | I haven't been abroad, but **he has**. |\n| He wanted to study medicine, and he studied medicine. | ..., and **he did**. |\n| Do we get on well? We get on well. | **We do.** |\n| She'll be there, and so will I. | ..., and **so will I**. |\n\n**Yardımcı fiil yoksa:** *do / does / did* kullanılır.\n\n**Vurgu:** Eksiltilmiş yardımcı fiil **vurgulu** söylenir: *I can't, but she **CAN**.*\n\n**2. Zincirleme yardımcı fiiller:**\n\n- *\"Have you finished?\" \"No, but I **will have** by six.\"*\n- *\"Could you have helped?\" \"I suppose I **could have**.\"*\n- *\"Is he being difficult?\" \"He **is**, a bit.\"*\n\n**3. do so / do that / do it:**\n\n| Yapı | Üslup | Örnek |\n|---|---|---|\n| **do so** | resmî | If you wish to cancel, please **do so** in writing. |\n| **do that** | nötr / samimi | \"Let's paint the kitchen.\" \"I'd rather not **do that** this week.\" |\n| **do it** | samimi, belirli bir eylem | \"Can you fix the tap?\" \"I'll **do it** tomorrow.\" |\n\n**4. too / either / so / neither (hatırlatma):**\n\n- *I'm tired.* → *So am I.* / *I am too.*\n- *I don't like it.* → *Neither do I.* / *I don't either.*",
     "examples": [{"en": "\"Have you read it?\" \"No, but I will.\"", "tr": "\"Okudun mu?\" \"Hayır ama okuyacağım.\""},
                  {"en": "I didn't want to go, but my sister did.", "tr": "Ben gitmek istemedim ama kız kardeşim istedi."},
                  {"en": "Passengers who wish to change seats may do so after take-off.", "tr": "Koltuk değiştirmek isteyen yolcular kalkıştan sonra değiştirebilir."}],
     "turkishNote": "Türkçede eksiltme genellikle fiilin kendisiyle yapılır: \"Ben yüzemem ama o yüzer.\" İngilizcede ise ana fiil düşer ve sadece yardımcı fiil kalır: \"I can't swim, but she can.\" Türk öğrenciler ya ana fiili tekrar eder (\"but she can swim\") ya da yardımcı fiili tamamen atlar (✗ \"but she\"). Ayrıca geniş zaman ve geçmiş zamanda \"do / did\" eklemeyi unutmak sık görülür: ✗ \"I wanted to go, but he not.\" ✓ \"..., but he didn't.\""},
    [
        mc("\"I can't swim, but my sister ___.\"", ["can", "can swim it"], 0, "Yardımcı fiil."),
        mc("\"He hasn't finished yet, but he ___ by tomorrow.\"", ["will have", "will have finish"], 0, "will have."),
        mc("Resmî duyuru:", ["If you want to leave early, please do so quietly.", "If you want to leave early, do it, OK?"], 0, "do so resmî."),
        mc("\"I wanted to go, but he ___.\"", ["didn't", "not"], 0, "did yardımcı fiili."),
        gap("\"Do you like spicy food?\" \"I ___, but my husband doesn't.\"", ["do"], "I do."),
        gap("I've never seen the film, but my friends ___.", ["have"], "have."),
        gap("She said she would call, and she ___.", ["did"], "did."),
        gap("\"Is it cold outside?\" \"It ___, a bit.\"", ["is"], "It is."),
        listen("I didn't expect to enjoy the course, but I did. Everyone said it would be hard, and it was, at times. My friend wanted to take it too, but in the end, she couldn't. She says she will next year.", "Konuşanın arkadaşı kursa katıldı mı?", ["Evet", "Hayır, katılamadı", "Henüz bilinmiyor"], 1, "\"in the end, she couldn't\""),
        typ("Eksiltin: \"I wasn't invited to the wedding, but my brother was invited to the wedding.\"", variants("I wasn't invited to the wedding, but my brother was.", "I wasn't invited to the wedding but my brother was."), "I wasn't invited to the wedding, but my brother was."),
    ],
    {"kind": "speaking", "task": speak("Kendinizi bir aile üyeniz ya da yakın bir arkadaşınızla karşılaştırın (1 dakika). En az 5 eksiltilmiş yardımcı fiil kullanın (He can, but I can't / I have, but she hasn't / I did / She will) ve bir kez do so ya da do that kullanın.",
                                       "My best friend Ece and I have known each other since primary school, but we're quite different. She can speak four languages; I can't, I only speak two. I've lived abroad, but she hasn't. She's always wanted to, though, and I think she will one day. I didn't enjoy school much, but she did; she loved every minute. People think we argue a lot, and we do, sometimes, but never seriously. She keeps telling me to learn a third language, and I've promised to do that next year.",
                                       ["Yardımcı fiil eksiltmesi", "do / did kullanımı", "do so / do that", "Doğal vurgu"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "Konuşmada eksiltme", "Günlük konuşmada cümle başındaki kelimeleri düşürme (Sounds good, Seen it) ve to ile biten cevapları (I'd love to, I don't want to) doğal şekilde anlayıp kullanabilirim.",
    {"kind": "dialogue", "title": "Cuma akşamı", "lines": [
        {"speaker": "Mert", "text": "Doing anything tonight?"},
        {"speaker": "Aylin", "text": "Not really. Why?"},
        {"speaker": "Mert", "text": "Fancy seeing a film?"},
        {"speaker": "Aylin", "text": "I'd love to. Which one?"},
        {"speaker": "Mert", "text": "The new sci-fi one. Seen it?"},
        {"speaker": "Aylin", "text": "No, but I've been meaning to."},
        {"speaker": "Mert", "text": "Great. Starts at nine. Want to grab something to eat first?"},
        {"speaker": "Aylin", "text": "Sounds good. Pizza?"},
        {"speaker": "Mert", "text": "Had pizza for lunch, actually. Sushi?"},
        {"speaker": "Aylin", "text": "Fine by me. See you at seven, then?"},
        {"speaker": "Mert", "text": "Perfect. Don't be late!"},
        {"speaker": "Aylin", "text": "I'll try not to!"}],
     "questions": [
        mc("What time does the film start?", ["At seven", "At nine", "At eight"], 1, "\"Starts at nine.\""),
        mc("Why doesn't Mert want pizza?", ["He doesn't like it.", "He had it for lunch.", "It's too expensive."], 1, "\"Had pizza for lunch, actually.\""),
     ]},
    {"explanation": "**1. Durumsal eksiltme (situational ellipsis):** Samimi konuşmada, bağlamdan anlaşılan **özne ve yardımcı fiil** cümle başından düşer.\n\n| Eksiltilmiş | Tam hali |\n|---|---|\n| **Doing** anything tonight? | *Are you* doing anything tonight? |\n| **Seen** it? | *Have you* seen it? |\n| **Want** to grab something? | *Do you* want to grab something? |\n| **Fancy** a coffee? | *Do you* fancy a coffee? |\n| **Sounds** good. | *That* sounds good. |\n| **Had** pizza for lunch. | *I* had pizza for lunch. |\n| **Starts** at nine. | *It* starts at nine. |\n| **Told** you! | *I* told you! |\n| **Nice** to meet you. | *It's* nice to meet you. |\n| **Anyone** sitting here? | *Is* anyone sitting here? |\n\n**2. to ile biten cevaplar (to-infinitive ellipsis):** Mastarın fiili tekrar edilmez, sadece **to** kalır.\n\n| Örnek | Anlam |\n|---|---|\n| \"Fancy a film?\" \"**I'd love to.**\" | çok isterim |\n| \"Why did you tell him?\" \"**I didn't mean to.**\" | istemeden oldu |\n| \"Don't be late.\" \"**I'll try not to.**\" | geç kalmamaya çalışacağım |\n| \"Seen it?\" \"No, but **I've been meaning to.**\" | uzun süredir niyetliyim |\n| \"Are you coming?\" \"**I'm supposed to**, but ...\" | gelmem gerekiyor ama |\n| \"Can I come?\" \"**If you want to.**\" | istersen |\n\n**Dikkat:** *to* düşürülmez! ✗ *I'd love.* ✓ *I'd love to.* Ancak *want / like* \"if\" ya da \"whatever\" ile kullanılınca **to** düşebilir: *Come if you **want**.*\n\n**Üslup:** Durumsal eksiltme **samimidir**; iş e-postası veya sunumlarda kullanmayın.",
     "examples": [{"en": "\"Ready?\" \"Almost. Give me two minutes.\"", "tr": "\"Hazır mısın?\" \"Neredeyse. İki dakika ver.\""},
                  {"en": "\"Why didn't you call?\" \"I wanted to, but my phone died.\"", "tr": "\"Neden aramadın?\" \"İstedim ama telefonumun şarjı bitti.\""},
                  {"en": "\"Can you help me move on Saturday?\" \"I'd be happy to.\"", "tr": "\"Cumartesi taşınmama yardım eder misin?\" \"Seve seve.\""}],
     "turkishNote": "Türkçe zaten özneyi düşüren bir dildir (\"Geliyorum\", \"Gördün mü?\"), bu yüzden İngilizce durumsal eksiltme Türk öğrencilere doğal gelir. Ama dikkat: İngilizcede bu sadece samimi konuşmada olur; yazıda ve resmî konuşmada özne her zaman gereklidir. Diğer sık hata ise \"I'd love\", \"I want\" deyip \"to\"yu atmaktır. Türkçedeki \"Çok isterim\" cevabının İngilizce karşılığı mutlaka \"I'd love to\" olmalıdır."},
    [
        mc("\"Fancy a coffee?\" (Kabul)", ["I'd love.", "I'd love to."], 1, "to düşmez."),
        mc("\"Seen the news?\" tam hali:", ["Have you seen the news?", "Did you see the news yesterday?"], 0, "Have you."),
        mc("\"Don't forget to call me.\"", ["I'll try not to.", "I'll try not."], 0, "try not to."),
        mc("Durumsal eksiltme nerede uygun DEĞİL?", ["Arkadaşa mesajda", "İş başvurusu e-postasında"], 1, "Samimi üslup."),
        gap("\"Why did you break it?\" \"I didn't mean ___!\"", ["to"], "didn't mean to."),
        gap("\"Have you called your mother?\" \"No, but I've been meaning ___.\"", ["to"], "been meaning to."),
        gap("\"Dinner at eight?\" \"___ good.\" (Kulağa iyi geliyor)", ["Sounds"], "Sounds good."),
        gap("\"Can I bring a friend?\" \"If you ___ to.\"", ["want"], "If you want to."),
        listen("Hi! Long time no see. Been busy? ... Yeah, me too. Listen, want to come to Can's party on Saturday? ... You'd love to? Great! Starts at eight. See you there!", "Parti ne zaman başlıyor?", ["Cuma sekizde", "Cumartesi sekizde", "Cumartesi dokuzda"], 1, "\"party on Saturday ... Starts at eight.\""),
        typ("Eksiltilmiş samimi soruyu tam hale getirin: \"Finished yet?\"", variants("Have you finished yet?", "Have you finished yet"), "Have you finished yet?"),
    ],
    {"kind": "speaking", "task": speak("Bir arkadaşınızı mesajla / telefonla bir etkinliğe davet edin ve planı yapın. Hem davet eden hem de davet edilen rolünü oynayın (8–10 replik). En az 4 durumsal eksiltme (Doing anything? / Fancy ...? / Sounds good. / Seen it?) ve en az 3 to ile biten cevap (I'd love to / I'll try not to / I've been meaning to / If you want to) kullanın.",
                                       "A: Hey! Free on Sunday? B: Think so. Why? A: Fancy going to the new exhibition at the art centre? B: I'd love to. I've been meaning to go for ages. Been already? A: No, not yet. Want to have breakfast first? B: Sounds good. Usual place? A: Perfect. Ten o'clock? B: Bit early, but fine. A: Don't be late this time! B: I'll try not to! Can I bring my cousin? A: If you want to. The more, the merrier.",
                                       ["Durumsal eksiltme", "to ile biten cevaplar", "Samimi ve doğal ton", "Akıcı sohbet"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Sohbeti sürdürmek", "Yankı soruları (Have you? / Did she?), dinleyici tepkileri ve kısa yanıt kalıplarıyla (Tell me about it!, Fair enough) ilgi gösterip sohbeti sürdürebilirim.",
    {"kind": "dialogue", "title": "Büyük haber", "lines": [
        {"speaker": "Selin", "text": "I've got some news. I've handed in my notice."},
        {"speaker": "Burak", "text": "Have you? Wow! When did that happen?"},
        {"speaker": "Selin", "text": "Yesterday. I'm going to start my own business."},
        {"speaker": "Burak", "text": "Are you really? That's brilliant! What kind of business?"},
        {"speaker": "Selin", "text": "A small bakery. I've always wanted to."},
        {"speaker": "Burak", "text": "I know you have. Mind you, it's a lot of work."},
        {"speaker": "Selin", "text": "Tell me about it! I haven't slept properly in weeks."},
        {"speaker": "Burak", "text": "I can imagine. So when are you opening?"},
        {"speaker": "Selin", "text": "In the spring, hopefully."},
        {"speaker": "Burak", "text": "Fingers crossed! Let me know if you need any help."}],
     "questions": [
        mc("What has Selin done?", ["Lost her job", "Handed in her notice", "Got a promotion"], 1, "\"I've handed in my notice.\""),
        mc("What does Burak warn her about?", ["It's expensive.", "It's a lot of work.", "It's risky."], 1, "\"Mind you, it's a lot of work.\""),
     ]},
    {"explanation": "**1. Yankı soruları (echo questions):** İlgi, şaşkınlık ya da merak göstermek için. Yapı: **yardımcı fiil + özne + ?** (Söylenen cümlenin zamanına uyar.)\n\n| Söylenen | Yankı sorusu |\n|---|---|\n| I've handed in my notice. | **Have you?** |\n| I'm going to start a business. | **Are you (really)?** |\n| She failed her test. | **Did she?** (Oh no!) |\n| I can't come tonight. | **Can't you?** Why not? |\n| My brother lives in Japan. | **Does he?** |\n| It wasn't my fault. | **Wasn't it?** |\n\n**Tonlama önemli!** Yükselen tonlama: ilgi / şaşkınlık. Düşen tonlama: \"Anladım\" (daha az ilgi).\n\n**2. Dinleyici tepkileri (backchannels):** Konuşanı dinlediğinizi göstermek için.\n\n| Tepki | Kullanım |\n|---|---|\n| **Mm. / Uh-huh. / Right. / I see.** | dinliyorum |\n| **Really? / Seriously? / No way!** | şaşkınlık |\n| **That's brilliant! / Good for you!** | sevinç |\n| **Oh no! / What a shame! / That's awful.** | üzüntü |\n| **I can imagine.** | empati |\n\n**3. Kısa yanıt kalıpları:**\n\n| Kalıp | Anlam |\n|---|---|\n| **Tell me about it!** | Hiç sorma! (tamamen katılıyorum) |\n| **Fair enough.** | Makul, anlıyorum. |\n| **Same here. / Me too.** | Ben de. |\n| **Fingers crossed!** | İnşallah! / Umarım! |\n| **Fine by me.** | Bana uyar. |\n| **Mind you, ...** | Gerçi ... (karşı nokta ekleme) |\n\nİyi bir dinleyici, **cevap + takip sorusu** verir: *\"Have you? Wow! When did that happen?\"*",
     "examples": [{"en": "\"I met a famous chef yesterday.\" \"Did you? Who?\"", "tr": "\"Dün ünlü bir şefle tanıştım.\" \"Öyle mi? Kim?\""},
                  {"en": "\"I can't stand this weather.\" \"Tell me about it!\"", "tr": "\"Bu havaya dayanamıyorum.\" \"Hiç sorma!\""},
                  {"en": "\"I'd rather stay in tonight.\" \"Fair enough.\"", "tr": "\"Bu akşam evde kalmayı tercih ederim.\" \"Anlıyorum, olur.\""}],
     "turkishNote": "Türkçede yankı sorusu genellikle tek bir kalıpla yapılır: \"Öyle mi?\" ya da \"Sahi mi?\". İngilizcede ise yankı sorusunun yardımcı fiili ve zamiri, karşıdakinin cümlesine uymalıdır: \"Have you?\", \"Did she?\", \"Is it?\". Türk öğrenciler genellikle her duruma \"Really?\" der. Bu yanlış değildir ama yankı soruları çok daha doğal ve ilgili görünür. Ayrıca \"Tell me about it!\" kelimesi kelimesine \"Bana bundan bahset\" değil, \"Hiç sorma, aynen öyle!\" anlamına gelir."},
    [
        mc("\"I've lost my keys again.\" Yankı sorusu:", ["Have you?", "Did you?"], 0, "Present perfect: Have you?"),
        mc("\"My sister lives in Canada.\" Yankı sorusu:", ["Is she?", "Does she?"], 1, "Present simple: Does she?"),
        mc("\"This traffic is terrible!\" (Tamamen katılıyorum)", ["Tell me about it!", "Tell me more about it."], 0, "Tell me about it!"),
        mc("\"I'm too tired to come out tonight.\" (Anlayış göster)", ["Fair enough.", "No way!"], 0, "Fair enough."),
        gap("\"I can't drive.\" \"___ you? I thought you could.\"", ["Can't"], "Can't you?"),
        gap("\"Kaan didn't come to the party.\" \"___ he? Why not?\"", ["Didn't"], "Didn't he?"),
        gap("\"I've got an interview tomorrow.\" \"Fingers ___!\"", ["crossed"], "Fingers crossed."),
        gap("It's an expensive hotel. ___ you, the views are amazing. (Gerçi)", ["Mind"], "Mind you."),
        listen("I've just been offered a job in Lisbon. ... I know, I can't believe it either! ... It starts in March. ... Well, I haven't decided yet. Mind you, the salary is really good.", "Konuşan işi kabul etti mi?", ["Evet, kabul etti", "Henüz karar vermedi", "Reddetti"], 1, "\"I haven't decided yet\""),
        match([("I've won a prize!", "Have you? Congratulations!"), ("I failed my driving test.", "Oh no! What happened?"), ("I hate Mondays.", "Tell me about it!"), ("Let's meet at six.", "Fine by me."), ("I'm starving.", "Same here.")], "Her cümleyi en uygun tepkiyle eşleştirin."),
    ],
    {"kind": "speaking", "task": speak("Bir arkadaşınız size şu üç haberi veriyor. Her birine yankı sorusu + uygun tepki + bir takip sorusuyla cevap verin: (1) \"I've decided to move to the countryside.\" (2) \"My laptop was stolen yesterday.\" (3) \"I'm going to run a marathon next month.\" Sonra kendi haberinizi verin ve arkadaşınızın nasıl tepki vereceğini de canlandırın.",
                                       "One: Have you? Wow, that's a big change! Where are you thinking of going? Two: Was it? Oh no, that's awful! Did you have everything backed up? Three: Are you really? Good for you! How long have you been training? My news: I've started learning the guitar. Friend: Have you? That's great! How's it going? Me: Slowly! My fingers really hurt. Friend: I can imagine. Mind you, it gets easier.",
                                       ["Doğru yankı soruları", "Uygun duygusal tepki", "Takip soruları", "Doğal tonlama"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Yazıda tekrardan kaçınmak", "Yazılı metinlerde the former / the latter, such, this / these, do so ve eksiltme kullanarak gereksiz tekrardan kaçınabilir ve metin bağlılığını artırabilirim.",
    {"kind": "text", "title": "Bir yorum yazısından", "body": "Draft:\n\"Many people choose between living in a city and living in the countryside. Living in a city offers more job opportunities. Living in the countryside offers a quieter lifestyle. Some people move to the countryside after retirement. People move to the countryside after retirement because they want peace and quiet. However, problems like poor transport and limited healthcare can make life in the countryside difficult.\"\n\nRevised:\n\"Many people choose between living in a city and living in the countryside. The former offers more job opportunities, whereas the latter offers a quieter lifestyle. Some people move to the countryside after retirement, usually because they want peace and quiet. However, such problems as poor transport and limited healthcare can make rural life difficult. These issues are often overlooked by those who decide to do so.\"",
     "questions": [
        mc("In the revised text, what does \"the former\" refer to?", ["Living in the countryside", "Living in a city"], 1, "İlk bahsedilen: a city."),
        mc("What problems of rural life are mentioned?", ["Noise and pollution", "Poor transport and limited healthcare", "High prices"], 1, "\"poor transport and limited healthcare\""),
     ]},
    {"explanation": "Yazıda gereksiz tekrar, metni **sıkıcı ve amatör** gösterir. İşte araçlar:\n\n**1. the former / the latter:** İki şeyden bahsettikten sonra.\n\n- *the former* = ilk bahsedilen\n- *the latter* = ikinci bahsedilen\n- *Cities offer jobs; the countryside offers peace. **The former** ..., whereas **the latter** ...*\n\n**Dikkat:** Sadece **iki** şey için kullanılır. Üç ya da daha fazla için: *the first / the last*.\n\n**2. such:** \"bu tür\" anlamında.\n\n- ***Such** problems are common.*\n- *problems **such as** poor transport* (örnek verme)\n- *in **such** cases* (bu gibi durumlarda)\n\n**3. this / these / that + isim (özetleyici isim):** Önceki fikri bir isimle özetlemek.\n\n- *Prices rose sharply. **This increase** ...*\n- *Poor transport and limited healthcare ... **These issues** ...*\n- *Some argue that ... **This view** ...*\n\n**4. do so (resmî):** Fiil öbeğini tekrar etmemek için.\n\n- *... those who decide **to do so*** (= to move to the countryside)\n\n**5. Yazıda eksiltme:** Bağlaçlardan sonra tekrarlanan özne / fiil düşürülür.\n\n- *Some move for work; **others, for family**.* (resmî yazıda virgülle eksiltme)\n- *She applied for the job and (she) **was offered** it.*\n\n**6. Eşanlamlılar ve genel isimler:**\n\n- *the countryside* → *rural areas, rural life*\n- *the city* → *urban areas, urban life*",
     "examples": [{"en": "Both trains and buses run to the airport; the former are faster, while the latter are cheaper.", "tr": "Havalimanına hem tren hem otobüs gidiyor; ilki daha hızlı, ikincisi daha ucuz."},
                  {"en": "Unemployment rose by 3%. This increase was mainly due to factory closures.", "tr": "İşsizlik %3 arttı. Bu artış büyük ölçüde fabrika kapanışlarından kaynaklandı."},
                  {"en": "In such cases, it is best to seek legal advice.", "tr": "Bu gibi durumlarda hukuki danışmanlık almak en iyisidir."}],
     "turkishNote": "Türkçede \"ilki / ikincisi\", \"bu tür\", \"söz konusu\" gibi ifadeler İngilizcedeki \"the former / the latter\", \"such\", \"the ... in question\" ile benzer işlev görür. Türk öğrencilerin İngilizce yazılarında sık görülen sorun, aynı isim öbeğini (örneğin \"living in the countryside\") art arda birçok kez tekrar etmektir. Bunun nedeni genellikle zamir kullanınca anlam karışacağı endişesidir. Özetleyici isimler (\"This trend\", \"These problems\") bu sorunu hem açık hem de profesyonel bir şekilde çözer."},
    [
        mc("\"I like tea and coffee, but I prefer ___.\" (kahve)", ["the latter", "the former"], 0, "İkinci bahsedilen: the latter."),
        mc("Üç seçenekten ilki için:", ["the former", "the first"], 1, "the former sadece iki şey için."),
        mc("Özetleyici isim: \"House prices doubled. ___ has made it hard for young people to buy.\"", ["This rise", "It rise"], 0, "This + isim."),
        mc("Resmî yazıda fiil tekrarından kaçınma:", ["Those who wish to apply should do so by Friday.", "Those who wish to apply should apply by Friday."], 0, "do so."),
        gap("Problems ___ as noise and pollution are common in big cities. (gibi)", ["such"], "such as."),
        gap("Laptops and tablets are both popular; the ___ are more powerful, while the latter are lighter.", ["former"], "the former."),
        gap("In ___ cases, students should contact their tutor. (bu gibi)", ["such"], "such cases."),
        gap("Many young people leave rural areas. ___ trend has been growing for decades. (Bu)", ["This"], "This trend."),
        listen("Students can choose between living in halls of residence and renting a private flat. The former is more sociable and usually includes bills, whereas the latter offers more independence. Most first-year students choose halls, while older students tend to rent.", "\"The former\" neyi ifade ediyor?", ["Özel kiralık daire", "Öğrenci yurdu (halls of residence)"], 1, "İlk bahsedilen."),
        typ("the latter ile yeniden yazın: \"You can pay by card or in cash. Paying in cash is quicker.\"", variants("You can pay by card or in cash. The latter is quicker.", "You can pay by card or in cash; the latter is quicker.", "You can pay by card or in cash, but the latter is quicker.", "You can pay by card or in cash, and the latter is quicker."), "You can pay by card or in cash. The latter is quicker."),
    ],
    {"kind": "writing", "task": write("Aşağıdaki tekrarlı paragrafı yeniden yazın. the former / the latter, such, this / these + özetleyici isim, do so ve eşanlamlılar kullanarak tekrarları giderin (90–120 kelime). Sonra aynı konuda kendi görüşünüzü ekleyen 2–3 cümle yazın.\n\n\"Many people work from home, and many people work in an office. Working from home saves time. Working in an office makes it easier to work with colleagues. Some companies allow employees to work from home two days a week. Companies allow employees to work from home because working from home makes employees happier. However, problems like loneliness and poor communication can happen when people work from home. Problems like loneliness and poor communication are serious.\"",
                                      "Revised paragraph:\n\nToday, some people work from home, while others work in an office. The former saves commuting time, whereas the latter makes it easier to collaborate with colleagues. Some companies now allow staff to work remotely two days a week, mainly because doing so tends to make employees happier. However, such problems as loneliness and poor communication can arise when people are away from the office. These issues are serious and should not be ignored.\n\nMy view:\n\nIn my opinion, a combination of the two is the best solution. Employees who wish to work from home should be allowed to do so, but regular team meetings in the office are essential to prevent such problems.",
                                      ["Tekrarların giderilmesi", "the former / the latter doğru", "such ve özetleyici isimler", "do so", "Akıcılık ve anlam bütünlüğü"])},
)

u.test([
    mc("\"Will it be cold tomorrow?\" (Olumsuz umut)", ["I don't hope so.", "I hope not."], 1, "I hope not"),
    mc("\"Is the shop open?\" (Olumsuz düşünce, doğal)", ["I don't think so.", "I think not so."], 0, "I don't think so"),
    mc("\"Fancy a walk?\" (Kabul)", ["I'd love.", "I'd love to."], 1, "to düşmez"),
    mc("\"My uncle lives in Berlin.\" Yankı sorusu:", ["Does he?", "Is he?"], 0, "Does he?"),
    mc("\"I prefer cats to dogs. The ___ are more independent.\" (kediler)", ["former", "latter"], 0, "the former"),
    gap("These shoes are too small. Have you got any bigger ___?", ["ones"], "ones"),
    gap("I can't speak Spanish, but my sister ___.", ["can"], "can"),
    gap("She said she would finish it, and she ___.", ["did"], "did"),
    gap("\"Why did you tell her?\" \"I didn't mean ___.\"", ["to"], "didn't mean to"),
    gap("\"I've passed my exam!\" \"___ you? Well done!\"", ["Have"], "Have you?"),
    gap("Passengers who wish to change seats may ___ so after take-off.", ["do"], "do so"),
    mc("\"This weather is awful.\" (Tamamen katılıyorum)", ["Tell me about it!", "Tell me more."], 0, "Tell me about it"),
    listen("Got any plans for the weekend? ... Not really. Fancy going to the beach? ... You'd love to? Great. Leaving at nine, then. Don't forget your sunscreen! ... You'll try not to? OK!", "Ne zaman yola çıkıyorlar?", ["Saat dokuzda", "Saat sekizde", "Öğleden sonra"], 0, "\"Leaving at nine\""),
    typ("Eksiltin: \"I haven't been to Japan, but my parents have been to Japan.\"", variants("I haven't been to Japan, but my parents have.", "I haven't been to Japan but my parents have."), "I haven't been to Japan, but my parents have."),
    write("İki yazı yazın. (A) Bir arkadaşınızla kısa bir mesajlaşma (8–10 mesaj): bir haber verin ya da bir plan yapın. Durumsal eksiltme, to ile biten cevaplar, yankı soruları ve en az iki kısa yanıt kalıbı (Fair enough / Tell me about it / Fingers crossed / Sounds good) kullanın. (B) \"Toplu taşıma mı, özel araç mı?\" konusunda kısa ve resmî bir paragraf (100–130 kelime): the former / the latter, such, özetleyici isimler ve do so kullanarak tekrardan kaçının.",
          "(A) Messages:\n\nZehra: Guess what? Got the job!\nOnur: Did you?! That's amazing! Which one, the design company?\nZehra: Yep. Start on Monday.\nOnur: Celebrate tonight? Dinner on me.\nZehra: I'd love to, but I can't. Seeing my parents.\nOnur: Fair enough. Tomorrow, then?\nZehra: Sounds good. Usual place?\nOnur: Perfect. Nervous about Monday?\nZehra: Tell me about it! Haven't slept properly all week.\nOnur: You'll be brilliant. Fingers crossed!\n\n(B) Paragraph:\n\nCity residents generally choose between public transport and private cars. The former is cheaper and more environmentally friendly, whereas the latter offers greater comfort and flexibility. In recent years, many cities have encouraged people to leave their cars at home, and an increasing number of commuters have chosen to do so. This shift has been driven largely by rising fuel prices and growing concern about air pollution. However, such problems as overcrowding and unreliable timetables still discourage many people from using buses and trains. Unless these issues are addressed, it is unlikely that the trend will continue.",
          ["(A) Eksiltme ve doğal tepkiler", "(A) Yankı soruları ve kalıplar", "(B) the former / the latter", "(B) such, özetleyici isim, do so", "Üslup farkının farkındalığı"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

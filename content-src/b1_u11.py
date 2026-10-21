"""B1 Ünite 11: Gizemler."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("B1", 11, "Gizemler", "Mysteries",
         "Elimdeki ipuçlarından yola çıkarak must, might, may, could ve can't ile şu anki durumlar hakkında çıkarım yapabilir, ne kadar emin olduğumu ifade edebilir ve gizem ve suç kelimeleriyle bir olayı tartışabilirim.",
         ["must (eminim ki)", "can't (olamaz)", "might / may / could (olabilir)", "must be + -ing (şu an yapıyor olmalı)", "emin olma dereceleri: definitely, probably, perhaps"],
         ["gizemler", "suç ve dedektiflik", "ipuçları ve kanıtlar"],
         {"title": "Dedektif masası", "durationMinutes": 45,
          "goal": "Gruplar bir \"gizem dosyası\" alır: Kayıp bir tablo, birkaç şüpheli ve ipuçları (bir fiş, bir ayak izi, bir mesaj). It must be..., It can't be..., He might be... kalıplarıyla şüphelileri tartışır, ne kadar emin olduklarını belirtir ve suçluyu kanıtlarıyla birlikte sınıfa açıklarlar. Doğru çözüme ulaşan grup kazanır."})

u.vocab([
    ("mystery", "gizem", "The disappearance is still a mystery.", "Kayboluş hâlâ bir gizem.", "mysterious (gizemli)"),
    ("detective", "dedektif", "The detective found an important clue.", "Dedektif önemli bir ipucu buldu.", None),
    ("clue", "ipucu", "There aren't any clues.", "Hiç ipucu yok.", None),
    ("evidence", "kanıt", "There's no evidence that he did it.", "Onun yaptığına dair kanıt yok.", "Sayılamaz: a piece of evidence"),
    ("suspect", "şüpheli; şüphelenmek", "The police have three suspects.", "Polisin üç şüphelisi var.", None),
    ("crime", "suç", "Crime is falling in the city.", "Şehirde suç oranı düşüyor.", "criminal (suçlu)"),
    ("burglar", "(eve giren) hırsız", "A burglar broke into the house.", "Bir hırsız eve girdi.", None),
    ("break into", "zorla girmek", "Someone broke into my car.", "Biri arabama zorla girdi.", "break → broke"),
    ("footprint", "ayak izi", "There are footprints in the garden.", "Bahçede ayak izleri var.", None),
    ("fingerprint", "parmak izi", "They found fingerprints on the glass.", "Bardakta parmak izi buldular.", None),
    ("witness", "tanık", "The witness saw a tall man.", "Tanık uzun boylu bir adam gördü.", None),
    ("alibi", "mazeret (suç anında başka yerde olduğu)", "He has an alibi. He was at work.", "Mazereti var, işteydi.", None),
    ("guilty", "suçlu", "I think he's guilty.", "Bence suçlu.", None),
    ("innocent", "masum", "She says she's innocent.", "Masum olduğunu söylüyor.", None),
    ("solve", "çözmek", "The detective solved the case.", "Dedektif davayı çözdü.", None),
    ("case", "dava, vaka", "It's a very strange case.", "Çok tuhaf bir vaka.", None),
    ("strange", "tuhaf", "There's a strange noise upstairs.", "Üst katta tuhaf bir ses var.", None),
    ("ghost", "hayalet", "Do you believe in ghosts?", "Hayaletlere inanır mısın?", None),
    ("explanation", "açıklama", "There must be a simple explanation.", "Basit bir açıklaması olmalı.", None),
    ("definitely", "kesinlikle", "It's definitely not the cat.", "Kesinlikle kedi değil.", None),
    ("probably", "muhtemelen", "She's probably at home.", "Muhtemelen evde.", None),
    ("perhaps", "belki", "Perhaps he forgot.", "Belki unuttu.", "maybe ile aynı"),
    ("disappear", "ortadan kaybolmak", "My keys have disappeared again!", "Anahtarlarım yine kayboldu!", None),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Olmalı ya da olamaz", "Kanıtlara dayanarak must ve can't ile emin olduğum çıkarımları yapabilirim.",
    {"kind": "dialogue", "title": "Kimin çantası?", "lines": [
        {"speaker": "Eda", "text": "Look, someone's left a bag on the bench."},
        {"speaker": "Can", "text": "Let's see. There's a football shirt and some boots inside. It must belong to a footballer."},
        {"speaker": "Eda", "text": "And there's a student card. The name is Mert Aksoy, and he's 15."},
        {"speaker": "Can", "text": "So he must be a student at the school across the road."},
        {"speaker": "Eda", "text": "He can't be far away. His phone is still in the bag!"},
        {"speaker": "Can", "text": "Ha! You must be a detective. Let's take it to the school office."}],
     "questions": [
        mc("Who does Can think the bag belongs to?", ["A teacher", "A footballer", "A detective"], 1, "\"It must belong to a footballer.\""),
        mc("How old is Mert?", ["15", "18", "We don't know."], 0, "\"he's 15\""),
     ]},
    {"explanation": "**Çıkarım (deduction)**, elimizdeki **kanıtlara** bakarak bir şeyin **doğru olup olmadığı** hakkında tahmin yürütmektir.\n\n| Modal | Anlam | Örnek |\n|---|---|---|\n| **must** + fiil | **Eminim ki doğru** (%95) | He **must be** a student. (Öğrenci olmalı.) |\n| **can't** + fiil | **Eminim ki doğru değil** (%95) | He **can't be** far away. (Uzakta olamaz.) |\n\n**Kanıt → Sonuç:**\n\n- She's wearing a uniform. → She **must be** a nurse.\n- He's only 15. → He **can't be** a teacher.\n- The lights are off. → They **must be** asleep.\n\n**Dikkat:**\n\n- must'ın olumsuzu çıkarımda **mustn't değil, can't**'tir. (~~He mustn't be at home.~~ → He **can't be** at home.)\n- mustn't = **yasak** anlamındadır (A2'de öğrendik).\n- Bu kullanımda must zorunluluk anlatmaz.",
     "examples": [{"en": "You've been travelling all day. You must be tired.", "tr": "Bütün gün yoldaydın. Yorgun olmalısın."},
                  {"en": "That can't be Ali. He's in London this week.", "tr": "O Ali olamaz. Bu hafta Londra'da."},
                  {"en": "This bag must cost a fortune!", "tr": "Bu çanta çok pahalı olmalı!"}],
     "turkishNote": "Türkçedeki \"-malı / -meli\" eki hem zorunluluk (gitmelisin) hem çıkarım (yorgun olmalısın) anlatır; İngilizcede de must ikisini de karşılar. Ama olumsuz çıkarımda \"olamaz\" için can't kullanılır: \"O olamaz\" → It can't be him. \"It mustn't be him\" yanlıştır."},
    [
        mc("She's wearing a white coat in a hospital. She ___ a doctor.", ["must be", "can't be"], 0, "Kanıt → must."),
        mc("He's only 10. He ___ a university student.", ["must be", "can't be"], 1, "İmkânsız → can't."),
        mc("\"O Ali olamaz.\"", ["It mustn't be Ali.", "It can't be Ali."], 1, "Olumsuz çıkarım → can't."),
        gap("You've been working for 12 hours. You ___ be exhausted.", ["must"], "must."),
        gap("That ___ be Selin's car. She doesn't have a car.", ["can't"], "can't."),
        gap("The house is dark. They ___ be at home. (olamaz)", ["can't"], "can't."),
        gap("This restaurant is always full. The food ___ be good.", ["must"], "must."),
        mc("\"mustn't\" hangi anlamdadır?", ["Olamaz (çıkarım)", "Yasak"], 1, "mustn't = yasak."),
        listen("Listen! There's someone in the kitchen. It can't be Mum, because she's at work. It must be my brother. He always comes home early on Fridays.", "Konuşan mutfaktakinin kim olduğunu düşünüyor?", ["Annesi", "Kardeşi", "Bir hırsız"], 1, "\"It must be my brother.\""),
        typ("İngilizce yazın: \"Bütün gün çalıştın. Yorgun olmalısın.\"", variants("You've worked all day. You must be tired.", "You've been working all day. You must be tired.", "You worked all day. You must be tired.", "You have worked all day. You must be tired.", "You have been working all day. You must be tired."), "You've been working all day. You must be tired."),
    ],
    {"kind": "speaking", "task": speak("JAI size 6 \"ipucu\" söyleyecek (\"Her eyes are red and she's holding a tissue.\" / \"He's carrying a guitar.\" ...). Her biri için must ya da can't ile bir çıkarım yapın ve nedenini söyleyin.",
                                       "She must be sad, or she must have a cold, because her eyes are red. He must be a musician. He's carrying a guitar. That can't be the right address. The house number is 25, not 52.",
                                       ["must / can't doğru seçimi", "mustn't kullanılmadı", "Kanıt + sonuç"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "Belki de...", "Emin olmadığım durumlar için might, may ve could ile olasılık bildirebilirim.",
    {"kind": "text", "title": "Tavan arasındaki ses", "body": "Every night at about midnight, the Aydın family hear a strange noise above their bedroom. It sounds like small footsteps.\n\nMr Aydın thinks it might be a mouse. \"It could be a bird too,\" he says. \"The roof is old, and there may be a hole somewhere.\"\n\nTheir daughter, Ela, has a different idea. \"It might be a ghost!\" she says. \"The house is a hundred years old.\"\n\nMrs Aydın doesn't agree. \"It can't be a ghost. Ghosts don't exist! And it can't be a bird, because birds sleep at night. It must be a cat from the neighbourhood. I've seen one on the roof.\"\n\nThe family have called an expert, who is coming on Friday to look.",
     "questions": [
        mc("What does Ela think the noise is?", ["A mouse", "A ghost", "A cat"], 1, "\"It might be a ghost!\""),
        mc("Why does Mrs Aydın think it can't be a bird?", ["Birds are too small.", "Birds sleep at night.", "There are no birds in the city."], 1, "\"birds sleep at night\""),
     ]},
    {"explanation": "**Emin değilsek** (yaklaşık %30–60):\n\n| Modal | Örnek |\n|---|---|\n| **might** + fiil | It **might be** a mouse. |\n| **may** + fiil | There **may be** a hole in the roof. |\n| **could** + fiil | It **could be** a bird. |\n\nÜçü de **\"olabilir, belki\"** anlamındadır. **may** biraz daha resmîdir.\n\n**Olumsuz:**\n\n- **might not** / **may not** = belki değildir\n  - He **might not** know the answer.\n- **couldn't** = olamaz (can't gibi), \"belki değil\" anlamında kullanılmaz!\n\n**Emin olma ölçeği:**\n\n```\n%100  It IS a cat.\n %95  It MUST be a cat.\n %50  It MIGHT / MAY / COULD be a cat.\n %50  It MIGHT NOT / MAY NOT be a cat.\n %95  It CAN'T be a cat.\n  %0  It ISN'T a cat.\n```",
     "examples": [{"en": "Take an umbrella. It might rain later.", "tr": "Şemsiye al. Sonra yağmur yağabilir."},
                  {"en": "She may not be at home. Call her mobile.", "tr": "Evde olmayabilir. Cep telefonundan ara."},
                  {"en": "That could be the answer!", "tr": "Cevap bu olabilir!"}],
     "turkishNote": "Türkçedeki \"olabilir\" ve \"olmayabilir\" ifadeleri might / may / could ve might not / may not ile karşılanır. \"couldn't\" ise \"olmayabilir\" değil, \"olamaz\" anlamına gelir. \"Evde olmayabilir\" → She might not be at home (~~She couldn't be at home~~)."},
    [
        mc("Emin değilsiniz: \"It ___ be a mouse.\"", ["must", "might", "can't"], 1, "Olasılık → might."),
        mc("\"Evde olmayabilir.\"", ["She couldn't be at home.", "She might not be at home."], 1, "might not."),
        mc("Hangisi \"olabilir\" anlamında değil?", ["might", "may", "could", "can't"], 3, "can't = olamaz."),
        gap("Take a coat. It ___ get cold tonight. (olabilir)", ["might", "may", "could"], "might / may / could."),
        gap("He ___ not know about the party. (belki bilmiyor)", ["might", "may"], "might not / may not."),
        gap("There ___ be a simple explanation. (resmî olasılık)", ["may", "might", "could"], "may."),
        mc("Doğru sıralama (en emin → en az emin):", ["must, might, can't", "must, might, is"], 0, "must (%95) → might (%50) → can't (%95 değil)."),
        order(["might", "It", "be", "a", "bird", "on", "the", "roof"], "It might be a bird on the roof.", "It + might + be.", "Çatıda bir kuş olabilir."),
        listen("I can't find my phone. It might be in the car. No, wait. It could be in my coat pocket. Let me check.", "Konuşan telefonunun nerede olabileceğini düşünüyor?", ["Sadece arabada", "Arabada ya da ceket cebinde", "İş yerinde"], 1, "\"It might be in the car... It could be in my coat pocket.\""),
        typ("İngilizce yazın: \"Sonra yağmur yağabilir.\"", variants("It might rain later.", "It may rain later.", "It could rain later.", "Later it might rain.", "It might rain later on.", "It may rain later on."), "It might rain later."),
    ],
    {"kind": "speaking", "task": speak("Aşağıdaki gizemli durumlar için en az 2 olası açıklama (might / may / could) ve 1 imkânsız açıklama (can't) önerin: 1) Komşunuzun evinde her gece saat 3'te ışık yanıyor. 2) Masanızın üstünde kimden geldiği belli olmayan bir çiçek var. 3) Arkadaşınız üç gündür mesajlarınıza cevap vermiyor.",
                                       "My neighbour might work at night. Or he could be a student who studies late. It can't be a party every night! The flowers might be from my colleague. It's my birthday next week. They may be a thank-you present. My friend might be on holiday. Her phone could be broken. She can't be angry with me. We had a great time last week.",
                                       ["might / may / could", "can't ile imkânsız açıklama", "Gerekçeler"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "Şu an ne yapıyor olabilir?", "Bir kişinin şu anda ne yaptığı hakkında must / might / can't + be + -ing ile çıkarım yapabilirim.",
    {"kind": "dialogue", "title": "Cevap vermeyen telefon", "lines": [
        {"speaker": "Seher", "text": "I've called Barış five times, and he isn't answering."},
        {"speaker": "Volkan", "text": "Don't worry. He might be driving. He never answers when he's in the car."},
        {"speaker": "Seher", "text": "He can't be driving. His car is at the mechanic's."},
        {"speaker": "Volkan", "text": "Then he must be sleeping. He was working until four last night."},
        {"speaker": "Seher", "text": "Hmm, or he might be watching the match. It's a big game today."},
        {"speaker": "Volkan", "text": "That's it! He must be watching it. The match started half an hour ago."}],
     "questions": [
        mc("Why can't Barış be driving?", ["He doesn't have a licence.", "His car is at the mechanic's.", "He's at work."], 1, "\"His car is at the mechanic's.\""),
        mc("What do they decide Barış must be doing?", ["Sleeping", "Watching the match", "Working"], 1, "\"He must be watching it.\""),
     ]},
    {"explanation": "Birinin **şu anda** ne yaptığı hakkında çıkarım yaparken **modal + be + -ing** kullanılır:\n\n| Yapı | Anlam | Örnek |\n|---|---|---|\n| **must be** + -ing | şu an yapıyor **olmalı** | He **must be sleeping**. |\n| **might / may / could be** + -ing | şu an yapıyor **olabilir** | He **might be driving**. |\n| **can't be** + -ing | şu an yapıyor **olamaz** | He **can't be driving**. |\n\n**Karşılaştırın:**\n\n- He **must be** tired. (Durum → be + sıfat)\n- He **must be sleeping**. (Şu anki eylem → be + -ing)\n- He **must sleep** a lot. (Genel alışkanlık → yalın fiil)\n\n**Sık kullanılan kalıplar:**\n\n- **You must be joking!** (Şaka yapıyor olmalısın!)\n- **They must be having fun.**\n- **She can't be working**; it's Sunday.",
     "examples": [{"en": "Listen to that noise! The neighbours must be having a party.", "tr": "Şu sese bak! Komşular parti veriyor olmalı."},
                  {"en": "She isn't at her desk. She might be having lunch.", "tr": "Masasında değil. Öğle yemeği yiyor olabilir."},
                  {"en": "You must be joking! That's impossible.", "tr": "Şaka yapıyor olmalısın! Bu imkânsız."}],
     "turkishNote": "Türkçedeki \"-iyor olmalı\" (uyuyor olmalı) ve \"-iyor olabilir\" (araba kullanıyor olabilir) yapıları İngilizcede tam olarak must be + -ing ve might be + -ing'e denk gelir. Bu yapı Türkçeyle çok benzer olduğu için kolayca kullanabilirsiniz."},
    [
        mc("Şu anki eylem: \"He isn't answering. He ___.\"", ["must sleep", "must be sleeping"], 1, "Şu an → must be + -ing."),
        mc("Genel alışkanlık: \"She's always so fit. She ___ a lot.\"", ["must exercise", "must be exercising"], 0, "Alışkanlık → yalın fiil."),
        mc("\"Şaka yapıyor olmalısın!\"", ["You must joke!", "You must be joking!"], 1, "Kalıp."),
        gap("Listen! Someone ___ be playing the piano upstairs. (olmalı)", ["must"], "must be + -ing."),
        gap("She ___ be working. It's Sunday and the office is closed. (olamaz)", ["can't"], "can't be + -ing."),
        gap("They aren't here yet. They might be ___ (wait) for the bus.", ["waiting"], "be + -ing."),
        gap("Look at the smoke! Someone must be ___ (cook) on a barbecue.", ["cooking"], "be + -ing."),
        order(["be", "They", "must", "having", "a", "great", "time"], "They must be having a great time.", "must + be + -ing.", "Harika vakit geçiriyor olmalılar."),
        listen("The lights are on and I can hear music, but nobody's answering the door. They might be in the garden, or they could be listening to music with headphones.", "Konuşan neden kapıyı açmadıklarını düşünüyor?", ["Evde değiller", "Bahçede ya da kulaklıkla müzik dinliyor olabilirler", "Uyuyorlar"], 1, "\"They might be in the garden, or they could be listening to music with headphones.\""),
        typ("İngilizce yazın: \"Masasında değil. Öğle yemeği yiyor olabilir.\"", variants("She isn't at her desk. She might be having lunch.", "He isn't at his desk. He might be having lunch.", "She's not at her desk. She might be having lunch.", "He's not at his desk. He might be having lunch.", "She isn't at her desk. She may be having lunch.", "He isn't at his desk. He may be having lunch.", "She isn't at her desk. She could be having lunch.", "He isn't at his desk. He could be having lunch.", "They aren't at their desk. They might be having lunch.", "They're not at their desk. They might be having lunch."), "She isn't at her desk. She might be having lunch."),
    ],
    {"kind": "speaking", "task": speak("Şu anda tanıdığınız 4 kişinin ne yaptığını tahmin edin (bir aile üyesi, bir arkadaş, bir iş arkadaşı, bir komşu). Her biri için must be / might be / can't be + -ing kullanın ve nedenini söyleyin.",
                                       "It's 10 o'clock on Saturday morning. My mum must be shopping at the market. She always goes on Saturdays. My brother can't be working; he doesn't work at weekends. He might be sleeping, or he could be playing football. My neighbour must be walking her dog, because I can't hear the dog.",
                                       ["modal + be + -ing doğru", "Kesinlik derecesi uygun", "Gerekçe"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Dedektif kelimeleri", "Suç ve dedektiflik kelimeleriyle bir olayı ve ipuçlarını anlatabilirim.",
    {"kind": "text", "title": "Müzedeki hırsızlık", "body": "Last night, a burglar broke into a small museum in Safranbolu and stole a valuable old clock.\n\nDetective Ayla Şen arrived early this morning. \"There are no fingerprints, so the thief must be an expert,\" she said. \"But there are footprints in the garden. They're quite small, so the suspect might be a woman, or a man with small feet.\"\n\nThe police are questioning three suspects: the night guard, a cleaner and a visitor who was in the museum yesterday afternoon. The night guard has an alibi. A witness saw him at a café at the time of the crime.\n\n\"The guard can't be guilty,\" says the detective. \"But someone knew the code for the alarm. That's an important clue.\"",
     "questions": [
        mc("Why does the detective think the thief must be an expert?", ["There are no fingerprints.", "The alarm didn't work.", "The clock was heavy."], 0, "\"There are no fingerprints, so the thief must be an expert\""),
        mc("Why can't the night guard be guilty?", ["He was asleep.", "He has an alibi.", "He's too old."], 1, "\"The night guard has an alibi.\""),
     ]},
    {"explanation": "**Suç ve dedektiflik kelimeleri:**\n\n| Kişiler | Eylemler | Kanıtlar |\n|---|---|---|\n| **detective** (dedektif) | **steal** (çalmak) | **clue** (ipucu) |\n| **suspect** (şüpheli) | **break into** (zorla girmek) | **evidence** (kanıt) |\n| **witness** (tanık) | **solve** (çözmek) | **fingerprint** (parmak izi) |\n| **burglar** (eve giren hırsız) | **question** (sorgulamak) | **footprint** (ayak izi) |\n| **thief** (hırsız) | **arrest** (tutuklamak) | **alibi** (mazeret) |\n\n**steal mi rob mu?**\n\n- **steal** + **eşya**: They **stole** a clock / my phone.\n- **rob** + **kişi / yer**: They **robbed** a bank / an old man.\n\n**Sıfatlar:** **guilty** (suçlu) ↔ **innocent** (masum)\n\n**Çıkarımla birleştirme:**\n\n- There are no fingerprints, **so** the thief **must** be an expert.\n- He has an alibi, **so** he **can't** be guilty.\n- The footprints are small, **so** the suspect **might** be a woman.",
     "examples": [{"en": "The police found an important clue at the scene.", "tr": "Polis olay yerinde önemli bir ipucu buldu."},
                  {"en": "Someone stole my bike from outside the library.", "tr": "Biri bisikletimi kütüphanenin önünden çaldı."},
                  {"en": "Two men robbed a jewellery shop yesterday.", "tr": "Dün iki adam bir kuyumcuyu soydu."}],
     "turkishNote": "Türkçede \"çalmak\" ve \"soymak\" ayrımı İngilizcedeki steal / rob ayrımına benzer: Eşya çalınır (steal a phone), kişi ya da yer soyulur (rob a bank). \"They stole the bank\" yanlıştır; \"They robbed the bank\" doğrudur."},
    [
        mc("They ___ a bank in the city centre.", ["stole", "robbed"], 1, "Yer → rob."),
        mc("Someone ___ my wallet.", ["stole", "robbed"], 0, "Eşya → steal."),
        mc("Suç anında başka yerde olduğunu gösteren şey:", ["clue", "alibi", "witness"], 1, "alibi."),
        mc("Masum:", ["guilty", "innocent"], 1, "innocent."),
        gap("A ___ broke into our house last night. (eve giren hırsız)", ["burglar", "thief"], "burglar."),
        gap("The police are questioning three ___. (şüpheli)", ["suspects"], "suspects."),
        gap("The detective found a ___ under the sofa. (ipucu)", ["clue"], "clue."),
        gap("He has an alibi, ___ he can't be guilty.", ["so"], "so + çıkarım."),
        match([("witness", "tanık"), ("evidence", "kanıt"), ("solve", "çözmek"), ("break into", "zorla girmek"), ("fingerprint", "parmak izi")], "Eşleştirin."),
        listen("The witness says she saw a man in a red jacket running from the shop. The suspect we arrested is wearing a blue jacket, so he might not be the thief.", "Polis neden tutuklanan kişinin hırsız olmayabileceğini düşünüyor?", ["Mazereti var", "Ceketi farklı renkte", "Tanık onu tanımadı"], 1, "Tanık kırmızı ceket gördü, şüpheli mavi ceket giyiyor."),
    ],
    {"kind": "speaking", "task": speak("Müzedeki hırsızlık vakasında üç şüpheliyi (gece bekçisi, temizlikçi, ziyaretçi) tartışın. Her biri için must / might / can't ile bir çıkarım yapın ve bir ipucu ya da kanıt gösterin. Sonunda kimin suçlu olabileceğine karar verin.",
                                       "The night guard can't be the thief, because a witness saw him at a café. The cleaner might be guilty. She knows the museum very well, and she could know the alarm code. The visitor was there yesterday afternoon, so he might be the thief too. But the footprints are small. I think the cleaner must be the burglar.",
                                       ["Suç kelimeleri doğru", "must / might / can't + kanıt", "Mantıklı sonuç"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Gizemi çöz", "Bir gizem hakkındaki teorileri tartışabilir, ne kadar emin olduğumu farklı ifadelerle belirtebilirim.",
    {"kind": "dialogue", "title": "Podcast: Çözülemeyen gizemler", "lines": [
        {"speaker": "Host 1", "text": "Today's mystery: every year, thousands of people visit a lake in the mountains because of strange lights above it at night."},
        {"speaker": "Host 2", "text": "Some people say they must be UFOs. Personally, I'm not convinced."},
        {"speaker": "Host 1", "text": "Me neither. They could be lights from a village on the other side."},
        {"speaker": "Host 2", "text": "That's possible, but there aren't any villages near the lake. I'm sure that's not it."},
        {"speaker": "Host 1", "text": "Then perhaps it's a natural gas. Scientists say that's probably the answer."},
        {"speaker": "Host 2", "text": "I think so too. It's definitely not ghosts, anyway!"}],
     "questions": [
        mc("Why can't the lights be from a village?", ["The village is too far.", "There aren't any villages near the lake.", "The villagers turn off their lights."], 1, "\"there aren't any villages near the lake\""),
        mc("What do scientists think is probably the answer?", ["UFOs", "A natural gas", "Ghosts"], 1, "\"perhaps it's a natural gas. Scientists say that's probably the answer.\""),
     ]},
    {"explanation": "Modallar dışında da **ne kadar emin olduğumuzu** gösterebiliriz:\n\n| Kesinlik | İfadeler |\n|---|---|\n| **Çok emin** | I'm sure / certain (that) ... / It's **definitely** ... / **There's no doubt** that ... |\n| **Oldukça emin** | It's **probably** ... / I **think** ... / It's **likely** that ... |\n| **Emin değil** | **Perhaps / Maybe** ... / It's **possible** that ... / I'm **not sure**. |\n| **Pek inanmıyor** | I **doubt** it. / I'm **not convinced**. / It's **unlikely** that ... |\n| **Kesinlikle hayır** | It's **definitely not** ... / There's **no way** ... |\n\n**Yer:** definitely / probably genellikle **be'den sonra**, diğer fiillerden **önce** gelir:\n\n- It's **probably** a gas. / He **probably** knows.\n\n**Fikir tartışmak:**\n\n- **Personally**, I think ... / **In my opinion**, ...\n- **That's possible, but** ... / **I'm not sure about that.**\n- **Me too. / Me neither. / I think so too.**",
     "examples": [{"en": "There's no doubt that someone was here.", "tr": "Birinin burada olduğundan hiç şüphe yok."},
                  {"en": "It's unlikely that he took the money.", "tr": "Parayı onun almış olması pek olası değil."},
                  {"en": "She's probably at the gym.", "tr": "Muhtemelen spor salonunda."}],
     "turkishNote": "\"Sanmıyorum\" için \"I don't think so\" ya da daha güçlü olarak \"I doubt it\" kullanılır. \"Me neither\" olumsuz bir cümleye katılırken (Ben de değil), \"Me too\" olumlu bir cümleye katılırken kullanılır."},
    [
        mc("Çok emin:", ["It's definitely a cat.", "It's possibly a cat."], 0, "definitely."),
        mc("\"Pek olası değil.\"", ["It's likely.", "It's unlikely."], 1, "unlikely."),
        mc("A: \"I'm not convinced.\" B: \"___\"", ["Me too.", "Me neither."], 1, "Olumsuz → Me neither."),
        mc("Doğru sıra:", ["He knows probably.", "He probably knows."], 1, "probably + fiil."),
        gap("There's no ___ that he's guilty. (şüphe)", ["doubt"], "There's no doubt."),
        gap("It's ___ a natural gas. (muhtemelen)", ["probably"], "probably."),
        gap("I'm not ___. (ikna olmadım)", ["convinced", "sure"], "convinced."),
        gap("That's ___, but I don't think it's true. (mümkün)", ["possible"], "possible."),
        listen("Some people say the old house is haunted. I doubt it. It's probably just the wind. But I'm not sure why the lights turn on at night.", "Konuşan evin perili olduğuna inanıyor mu?", ["Evet, kesinlikle", "Pek inanmıyor", "Henüz karar vermedi ama korkuyor"], 1, "\"I doubt it.\""),
        typ("İngilizce yazın: \"Muhtemelen spor salonunda.\"", variants("She's probably at the gym.", "He's probably at the gym.", "She is probably at the gym.", "He is probably at the gym.", "They're probably at the gym.", "They are probably at the gym."), "She's probably at the gym."),
    ],
    {"kind": "writing", "task": write("Bir forumda gerçek ya da hayali bir gizem hakkında yazın (130–160 kelime): Ne oldu, ipuçları neler, insanlar ne düşünüyor? Farklı teorileri must / might / could / can't ile tartışın, definitely / probably / I doubt it gibi ifadelerle ne kadar emin olduğunuzu belirtin ve kendi teorinizi açıklayın.",
                                      "The Mystery of the Moving Bench\n\nIn our park, there's an old wooden bench next to the lake. For the last month, people have noticed something strange: every morning, the bench is in a different place.\n\nSome children say it must be a ghost. I doubt it! Others think it might be teenagers who come to the park at night. That's possible, but the bench is very heavy, so it can't be just one person.\n\nThe park gardener has a different idea. He says the city workers could be moving it to clean the grass. But the city says they don't work at night, so that's unlikely.\n\nPersonally, I think the answer is probably simple. There's a café next to the park, and the owner is always complaining that the bench is too far from his door. I'm not sure, but I think he might be moving it every night!",
                                      ["must / might / could / can't doğru", "Kesinlik ifadeleri", "İpuçları ve teoriler", "Kendi görüşü", "Akıcı ve düzenli metin"])},
)

u.test([
    mc("She's wearing a uniform and carrying a stethoscope. She ___ a nurse.", ["must be", "can't be"], 0, "must"),
    mc("He's only five. He ___ drive.", ["must", "can't"], 1, "can't"),
    mc("\"O olamaz.\"", ["It mustn't be him.", "It can't be him."], 1, "can't"),
    mc("Emin değilsiniz: \"It ___ rain tomorrow.\"", ["must", "might"], 1, "might"),
    mc("\"Evde olmayabilir.\"", ["She couldn't be at home.", "She might not be at home."], 1, "might not"),
    gap("Listen! The baby ___ be crying. (olmalı)", ["must"], "must be + -ing"),
    gap("They can't be ___ (sleep). The music is so loud!", ["sleeping"], "be + -ing"),
    gap("Someone ___ my phone! (çaldı)", ["stole", "took"], "steal"),
    gap("Two men ___ a bank yesterday. (soydu)", ["robbed"], "rob"),
    gap("The police have three ___. (şüpheli)", ["suspects"], "suspect"),
    mc("Suç anında başka yerde olduğunun kanıtı:", ["alibi", "clue", "suspect"], 0, "alibi"),
    mc("A: \"I don't believe it.\" B: \"___\"", ["Me too.", "Me neither."], 1, "Me neither"),
    listen("The window is broken and there's mud on the floor, but nothing is missing. It can't be a burglar. It might be the wind, or it could be a bird... no, look! There's a football under the table.", "Sonunda camı neyin kırdığı anlaşılıyor?", ["Bir hırsız", "Rüzgâr", "Bir futbol topu"], 2, "\"There's a football under the table.\""),
    typ("İngilizce yazın: \"Şaka yapıyor olmalısın!\"", variants("You must be joking!", "You must be joking.", "You must be kidding!", "You must be kidding."), "You must be joking!"),
    write("Sabah evden çıkarken kapınızın önünde, içinde bir anahtar, bir tren bileti ve bir not (\"Thank you for everything. – K.\") olan bir kutu buldunuz. Bu gizemi açıklamaya çalışan bir paragraf yazın (120–150 kelime). must, might, could, can't, be + -ing yapıları ve definitely / probably / I doubt gibi kesinlik ifadeleri kullanın.",
          "This morning I found a small box outside my door. Inside, there was a key, a train ticket to Izmir and a note: \"Thank you for everything. – K.\" Who could it be from? It can't be from my brother, because his name is Murat. It might be from my old flatmate, Kader. She moved to Izmir last year, and she probably wants me to visit her. The key could be for her new flat! But I doubt it, because she always sends messages, not notes. It might be from my neighbour, Kemal Bey. I helped him a lot when he was ill. Perhaps he's moving to Izmir and he wants me to take care of his house. I'm not sure, but there's definitely a story here. Kemal Bey must be at home now, so I'm going to knock on his door and ask!",
          ["Modal çıkarımlar doğru", "Kesinlik ifadeleri", "Mantıklı gerekçeler", "be + -ing ya da çeşitli yapılar", "Akıcı paragraf"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

"""B2 Ünite 7: Geçmişe dair tahmin."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("B2", 7, "Geçmişe dair tahmin", "Looking Back",
         "Geçmişteki olaylar hakkında kanıtlara dayanarak ne kadar emin olduğumu (must have, can't have, might have) ifade edebilir, geçmişteki hataları eleştirebilir (should have) ve gereksiz yapılan işleri (needn't have) anlatabilirim.",
         ["must have / can't have + V3", "might / may / could have + V3", "should / shouldn't have + V3", "needn't have vs didn't need to", "kanıt ve çıkarım dili"],
         ["gizemler ve araştırma", "tarih ve arkeoloji", "yorum ve eleştiri"],
         {"title": "Dedektif masası", "durationMinutes": 45,
          "goal": "Gruplar kısa bir \"gizem dosyası\" alır (bir fotoğraf, birkaç ipucu). Kanıtları tartışıp must have / can't have / might have ile ne olduğuna dair bir teori kurar ve sınıfa sunar. Sonunda öğretmen gerçeği açıklar ve gruplar should have ile kendi akıl yürütme hatalarını değerlendirir."})

u.vocab([
    ("evidence", "kanıt", "There's no evidence that he was there.", "Orada olduğuna dair hiçbir kanıt yok.", "sayılamaz: a piece of evidence"),
    ("clue", "ipucu", "The detective found an important clue.", "Dedektif önemli bir ipucu buldu.", None),
    ("theory", "teori", "I have a theory about what happened.", "Ne olduğuna dair bir teorim var.", None),
    ("deduce", "sonuç çıkarmak", "From the footprints, she deduced that two people had been there.", "Ayak izlerinden orada iki kişinin bulunduğu sonucunu çıkardı.", None),
    ("conclusion", "sonuç, varılan yargı", "Don't jump to conclusions.", "Hemen sonuca atlama.", None),
    ("assume", "varsaymak", "I assumed you had already left.", "Çoktan gittiğini varsaydım.", None),
    ("suspect", "şüphelenmek; şüpheli", "Police suspect that the fire was started deliberately.", "Polis yangının kasten çıkarıldığından şüpheleniyor.", None),
    ("witness", "tanık", "A witness saw a man running away.", "Bir tanık kaçan bir adam gördü.", None),
    ("mystery", "gizem", "Her disappearance is still a mystery.", "Ortadan kaybolması hâlâ bir gizem.", None),
    ("solve", "çözmek", "The case was never solved.", "Dava hiç çözülmedi.", None),
    ("explanation", "açıklama", "There must be a logical explanation.", "Mantıklı bir açıklaması olmalı.", None),
    ("likely", "muhtemel", "It's likely that they got lost.", "Kaybolmuş olmaları muhtemel.", None),
    ("unlikely", "pek olası değil", "It's unlikely that he did it alone.", "Bunu tek başına yapmış olması pek olası değil.", None),
    ("ruins", "harabe, kalıntılar", "We explored the ruins of an ancient temple.", "Antik bir tapınağın kalıntılarını gezdik.", None),
    ("excavation", "kazı", "The excavation began in 1995.", "Kazı 1995'te başladı.", None),
    ("archaeologist", "arkeolog", "Archaeologists found pottery at the site.", "Arkeologlar alanda çanak çömlek buldu.", None),
    ("site", "alan, ören yeri", "Göbekli Tepe is an important archaeological site.", "Göbekli Tepe önemli bir arkeolojik alan.", None),
    ("date back to", "-e dayanmak (tarih)", "The tools date back to 10,000 BC.", "Aletler MÖ 10.000'e dayanıyor.", None),
    ("ritual", "ritüel, tören", "The stones may have been used for rituals.", "Taşlar ritüeller için kullanılmış olabilir.", None),
    ("carelessly", "dikkatsizce", "He carelessly left the door open.", "Kapıyı dikkatsizce açık bıraktı.", None),
    ("in hindsight", "geriye dönüp bakınca", "In hindsight, we should have left earlier.", "Geriye dönüp bakınca daha erken çıkmalıydık.", None),
    ("to blame", "suçlu, sorumlu", "Who is to blame for the mistake?", "Hatadan kim sorumlu?", None),
    ("overreact", "aşırı tepki vermek", "Maybe I overreacted a little.", "Belki biraz aşırı tepki verdim.", None),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Kesin olmalı, olamaz", "must have ve can't / couldn't have ile geçmiş hakkında güçlü çıkarımlar yapabilirim.",
    {"kind": "dialogue", "title": "Ofiste sabah", "lines": [
        {"speaker": "Nur", "text": "Look at this. The kitchen's a mess, and all the cake is gone."},
        {"speaker": "Kaan", "text": "Someone must have stayed late last night. The lights were still on when I arrived."},
        {"speaker": "Nur", "text": "It can't have been Melis. She was at the conference in Izmir all week."},
        {"speaker": "Kaan", "text": "And it couldn't have been the cleaners. They don't come on Thursdays."},
        {"speaker": "Nur", "text": "Wait, there's a pizza box with Burak's name on it."},
        {"speaker": "Kaan", "text": "Ha! He must have been working on the presentation. It's due today."}],
     "questions": [
        mc("Why does Kaan think someone stayed late?", ["The door was open.", "The lights were still on.", "He saw them."], 1, "\"The lights were still on when I arrived.\""),
        mc("Why can't it have been Melis?", ["She was ill.", "She was at a conference in Izmir.", "She doesn't like cake."], 1, "\"She was at the conference in Izmir all week.\""),
     ]},
    {"explanation": "Şimdiki zamanda **must** ve **can't** ile çıkarım yapmayı biliyorsunuz (*He must be tired.*). Geçmiş için **modal + have + V3** kullanılır.\n\n| Yapı | Anlam | Kesinlik |\n|---|---|---|\n| **must have** + V3 | Kesin öyle oldu (kanıta göre) | ~%95 evet |\n| **can't have** + V3 | Kesin öyle olmadı (imkânsız) | ~%95 hayır |\n| **couldn't have** + V3 | Kesin öyle olmadı | ~%95 hayır |\n\n**Örnekler:**\n\n- The lights were on. Someone **must have stayed** late.\n- She was in Izmir. It **can't have been** her.\n- He **couldn't have seen** us. It was too dark.\n\n**Çok önemli:**\n\n- **must have**'ın olumsuzu **mustn't have DEĞİLDİR**. Çıkarımda olumsuz **can't have / couldn't have**'dır.\n  - ~~She mustn't have known.~~ → She **can't have known**.\n- Telaffuz: konuşmada **must've** /ˈmʌstəv/, **can't've** /ˈkɑːntəv/ gibi kısaltılır.\n- Süreç bildiren olaylar için **must have been + -ing**: *He **must have been working** on the presentation.*",
     "examples": [{"en": "The ground is wet. It must have rained last night.", "tr": "Yer ıslak. Dün gece yağmur yağmış olmalı."},
                  {"en": "You can't have finished already! You only started ten minutes ago.", "tr": "Bitirmiş olamazsın! On dakika önce başladın."},
                  {"en": "She must have been waiting for hours.", "tr": "Saatlerdir bekliyor olmalı."}],
     "turkishNote": "Türkçede \"-mış olmalı\" (must have) ve \"-mış olamaz\" (can't have) yapıları birebir karşılık gelir: \"yağmış olmalı\" = must have rained. En sık hata olumsuzu \"mustn't have\" ile kurmaktır. Bir de \"-mış\" ekinin duyulan geçmiş (He's left, apparently) anlamıyla karışmamasına dikkat: çıkarımda modal + have gerekir."},
    [
        mc("\"Yerde ayak izleri var.\" → Someone ___ in here.", ["must have been", "can't have been"], 0, "Kanıt → must have."),
        mc("Doğru olumsuz çıkarım:", ["He mustn't have heard us.", "He can't have heard us."], 1, "can't have."),
        mc("\"It can't have been Ali.\" anlamı:", ["Ali olmuş olabilir.", "Ali olmuş olamaz."], 1, "İmkânsız."),
        mc("\"She must have been sleeping.\" vurgusu:", ["Tamamlanmış eylem", "Süren eylem"], 1, "have been + -ing."),
        gap("The car is gone. Dad must ___ taken it.", ["have"], "must have + V3."),
        gap("You can't have ___ (see) him yesterday. He's in Japan.", ["seen"], "V3."),
        gap("The window is broken. Someone must have ___ (throw) a stone.", ["thrown"], "throw-threw-thrown."),
        gap("She couldn't have ___ (know) about the party. It was a secret.", ["known"], "know-knew-known."),
        listen("Wow, your garden looks amazing! You must have spent all weekend working on it. And these tomatoes can't have come from the supermarket. They're far too tasty.", "Konuşan domatesler hakkında ne düşünüyor?", ["Süpermarketten alınmış", "Süpermarketten gelmiş olamaz", "Komşudan gelmiş"], 1, "\"can't have come from the supermarket\""),
        typ("İngilizcesi: \"Yolu kaybetmiş olmalılar.\" (they, lose their way)", variants("They must have lost their way.", "They must've lost their way."), "They must have lost their way."),
    ],
    {"kind": "speaking", "task": speak("Aşağıdaki durumlar için must have ve can't / couldn't have ile birer çıkarım yapın ve gerekçenizi söyleyin: (1) Komşunuzun evinin önünde bir taşınma kamyonu vardı. (2) Arkadaşınız sınavdan 100 aldı. (3) Telefonunuzda 12 cevapsız arama var. (4) Buzdolabındaki tatlı yok olmuş.",
                                       "There was a removal van outside my neighbour's house, so they must have moved out. My friend got 100 in the exam. She must have studied really hard. She can't have cheated because the teacher was watching all the time. I've got twelve missed calls from my mum. Something must have happened. The dessert has disappeared. It can't have been my dad because he's on a diet, so it must have been my brother!",
                                       ["must have + V3", "can't / couldn't have", "Gerekçe gösterme"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "Olmuş olabilir", "might / may / could have ile geçmiş hakkında olasılıkları tartışabilir ve farklı teoriler önerebilirim.",
    {"kind": "text", "title": "Göbekli Tepe'nin gizemi", "body": "Göbekli Tepe, near Şanlıurfa, is one of the most important archaeological sites in the world. Its huge stone pillars date back to around 9500 BC, which makes them about 6,000 years older than Stonehenge.\n\nBut who built it, and why? The people who lived there were hunter-gatherers. They didn't have metal tools or the wheel. So how did they move stones that weigh several tonnes?\n\nArchaeologists have several theories. The site may have been a religious centre, where people from different groups came together for rituals and feasts. Some experts think it might have been used for burials. Others suggest that it could have been a kind of meeting place for trade.\n\nOne thing is clear: building it must have required hundreds of people working together for years. And that may have changed the way humans lived, and even led to the beginning of farming.",
     "questions": [
        mc("How old are the pillars?", ["About 2,000 years old", "Around 9500 BC", "About 500 years old"], 1, "\"date back to around 9500 BC\""),
        mc("What is one theory about the site?", ["It was a royal palace.", "It may have been a religious centre.", "It was a market for metal tools."], 1, "\"The site may have been a religious centre\""),
     ]},
    {"explanation": "Geçmişteki **olasılıklar** için **might / may / could have + V3** kullanılır. Üçü de yaklaşık aynı anlama gelir: **\"-mış olabilir\"**.\n\n| Yapı | Anlam | Kesinlik |\n|---|---|---|\n| must have | kesin (çıkarım) | %95 |\n| **may have** | olabilir | %50 |\n| **might have** | olabilir (biraz daha az emin) | %40 |\n| **could have** | olabilir | %40 |\n| can't have | imkânsız | %5 |\n\n**Olumsuz:**\n\n- **may not have / might not have** = belki olmadı\n  - *He **might not have received** my email.* (Belki almadı.)\n- **couldn't have** ≠ might not have!\n  - *He **couldn't have received** it.* = Kesinlikle almadı (imkânsız).\n\n**B2 Ünite 3'teki could have ile farkı:** Orada **could have** \"yapabilirdin ama yapmadın\" (kaçırılmış fırsat) anlamındaydı. Burada **\"belki öyle oldu, bilmiyoruz\"** anlamında bir tahmin.\n\n- *You **could have called** me!* (Arayabilirdin, aramadın. → eleştiri)\n- *She **could have called** while I was out.* (Ben dışarıdayken aramış olabilir. → tahmin)",
     "examples": [{"en": "The site may have been a religious centre.", "tr": "Alan bir dini merkez olmuş olabilir."},
                  {"en": "I can't find my keys. I might have left them at work.", "tr": "Anahtarlarımı bulamıyorum. İşte bırakmış olabilirim."},
                  {"en": "She may not have heard the news yet.", "tr": "Haberi henüz duymamış olabilir."}],
     "turkishNote": "Türkçede \"-mış olabilir\" tek bir yapıyla karşılanır; İngilizcede may / might / could have aynı işi görür. Asıl zorluk olumsuzlarda: \"might not have\" (belki olmadı) ile \"couldn't have\" (kesinlikle olmadı) çok farklı kesinlik düzeyleridir. \"Almamış olabilir\" demek istiyorsanız \"couldn't have\" değil, \"might not have\" kullanın."},
    [
        mc("\"Toplantıyı unutmuş olabilir.\"", ["He must have forgotten the meeting.", "He might have forgotten the meeting."], 1, "Olasılık → might have."),
        mc("\"Belki e-postamı görmedi.\"", ["She couldn't have seen my email.", "She may not have seen my email."], 1, "Belki olmadı → may not have."),
        mc("\"You could have told me!\" burada:", ["Tahmin", "Eleştiri (söyleyebilirdin)"], 1, "Kaçırılmış fırsat."),
        mc("Hangisi en kesin?", ["might have", "may have", "must have"], 2, "must have."),
        gap("I'm not sure where Can is. He ___ have gone to the gym. (olabilir)", ["might", "may", "could"], "might / may / could."),
        gap("The stones may have ___ (use) for rituals.", ["been used"], "Edilgen: have been + V3."),
        gap("They might not ___ (hear) the doorbell.", ["have heard"], "might not have + V3."),
        gap("It ___ have been a meeting place. Nobody knows for sure. (olabilir)", ["may", "might", "could"], "Olasılık."),
        listen("Nobody knows why the ancient city was abandoned. There might have been a terrible drought, or an earthquake could have destroyed it. Some historians think disease may have killed most of the population.", "Hangisi teorilerden biri DEĞİL?", ["Kuraklık", "Deprem", "Savaş"], 2, "Savaştan söz edilmiyor."),
        typ("İngilizcesi: \"Otobüsü kaçırmış olabilir.\" (she, might)", variants("She might have missed the bus.", "She might've missed the bus."), "She might have missed the bus."),
    ],
    {"kind": "speaking", "task": speak("Tarihî bir gizem seçin (Truva, piramitler, Göbekli Tepe, kayıp bir uçak, vb.). Ne olduğuna dair en az 3 farklı teori önerin (may / might / could have) ve en mantıklısının hangisi olduğunu must have / can't have ile savunun.",
                                       "I'd like to talk about the pyramids in Egypt. People have wondered how they were built for thousands of years. Some people believe that the Egyptians might have used ramps to move the stones. Others think they could have used water to float the blocks. A few even say aliens may have helped, but that can't have happened! In my opinion, the workers must have used ramps, because archaeologists have found evidence of them.",
                                       ["may / might / could have", "must / can't have ile savunma", "Kanıta dayalı akıl yürütme"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "Yapmalıydın", "should have ve shouldn't have ile geçmişteki hataları eleştirebilir ve ders çıkarabilirim.",
    {"kind": "dialogue", "title": "Kaçırılan uçak", "lines": [
        {"speaker": "Selin", "text": "I can't believe we missed the flight."},
        {"speaker": "Arda", "text": "We should have left the house earlier. I told you the traffic would be terrible."},
        {"speaker": "Selin", "text": "Well, you shouldn't have spent forty minutes looking for your sunglasses!"},
        {"speaker": "Arda", "text": "Fair enough. And we should have checked in online. The queue was enormous."},
        {"speaker": "Selin", "text": "In hindsight, we shouldn't have booked such an early flight either."},
        {"speaker": "Arda", "text": "OK, lesson learned. Next time, we pack the night before."}],
     "questions": [
        mc("Why did Arda delay them?", ["He forgot his passport.", "He was looking for his sunglasses.", "He was on the phone."], 1, "\"looking for your sunglasses\""),
        mc("What lesson do they learn?", ["Take a taxi.", "Pack the night before.", "Never fly again."], 1, "\"Next time, we pack the night before.\""),
     ]},
    {"explanation": "**should have + V3** = \"-malıydı / -meliydin\" (yapılmadı ve bu bir hataydı)\n\n**shouldn't have + V3** = \"-mamalıydı / -mamalıydın\" (yapıldı ve bu bir hataydı)\n\n| Yapı | Gerçek | Anlam |\n|---|---|---|\n| We **should have left** earlier. | Erken çıkmadık. | Erken çıkmalıydık. |\n| You **shouldn't have spent** so long. | Çok zaman harcadın. | Harcamamalıydın. |\n| He **ought to have** told us. | Söylemedi. | Söylemeliydi. (daha resmî) |\n\n**Kullanım alanları:**\n\n1. **Eleştiri:** *You **should have asked** me first.*\n2. **Pişmanlık:** *I **shouldn't have said** that.*\n3. **Beklenti (şaşırma):** *The train **should have arrived** by now.* (Şimdiye kadar gelmiş olmalıydı; gelmedi.)\n\n**must have ile karıştırmayın:**\n\n- He **must have left**. (Gitmiş olmalı. → çıkarım)\n- He **should have left**. (Gitmeliydi. → eleştiri; gitmedi)\n\n**Kibar eleştiri:** *Maybe you **could have** asked first?* / *It **might have been** better to ...*",
     "examples": [{"en": "I should have studied harder for the exam.", "tr": "Sınava daha çok çalışmalıydım."},
                  {"en": "You shouldn't have left the door unlocked.", "tr": "Kapıyı kilitsiz bırakmamalıydın."},
                  {"en": "They should have arrived by now. I hope they're OK.", "tr": "Şimdiye kadar gelmiş olmaları gerekirdi. Umarım iyilerdir."}],
     "turkishNote": "Türkçede \"çıkmalıydık\" (should have left) ile \"çıkmış olmalıyız\" (must have left) yapıları benzer olduğu için karıştırılabilir. Kural: eleştiri ya da pişmanlıksa should have, kanıta dayalı çıkarımsa must have. Ayrıca \"Teşekkürler, zahmet etmeseydin!\" İngilizcede \"You shouldn't have!\" olarak söylenir: hediye alırken çok kullanılan nazik bir kalıptır."},
    [
        mc("\"Sana söylemeliydim.\"", ["I must have told you.", "I should have told you."], 1, "Pişmanlık → should have."),
        mc("\"Gitmiş olmalı, arabası yok.\"", ["He should have left.", "He must have left."], 1, "Çıkarım → must have."),
        mc("Hediye aldığınızda \"Zahmet etmeseydin!\":", ["You mustn't!", "You shouldn't have!"], 1, "Kalıp."),
        mc("\"The bus should have come by now.\" anlamı:", ["Otobüs geldi.", "Otobüsün gelmiş olması gerekirdi ama gelmedi."], 1, "Beklenti."),
        gap("You ___ have eaten so much. Now you feel sick. (yememeliydin)", ["shouldn't"], "shouldn't have."),
        gap("We should have ___ (book) a table. The restaurant is full.", ["booked"], "V3."),
        gap("I shouldn't have ___ (say) that. I'm sorry.", ["said"], "say-said-said."),
        gap("He ought ___ have told his boss earlier.", ["to"], "ought to have."),
        listen("I really regret selling my old car. It was cheap to run and never broke down. I should have kept it. And I definitely shouldn't have bought this new one. It's been to the garage three times already.", "Konuşan neden pişman?", ["Eski arabasını sattığı için", "Hiç araba almadığı için", "Ehliyet almadığı için"], 0, "\"I really regret selling my old car... I should have kept it.\""),
        typ("İngilizcesi: \"Kapıyı kilitlemeliydin.\" (you, lock the door)", variants("You should have locked the door.", "You should've locked the door."), "You should have locked the door."),
    ],
    {"kind": "speaking", "task": speak("Hayatınızda ya da bir arkadaşınızın hayatında yanlış giden bir durumu anlatın (kötü geçen bir tatil, bir iş görüşmesi, bir tartışma). should have ve shouldn't have ile en az 5 hata ve ders çıkarın. Bir kez de kibar eleştiri kalıbı (Maybe I could have ...) kullanın.",
                                       "Last year I had a job interview that went really badly. First of all, I should have researched the company, because they asked me questions I couldn't answer. I shouldn't have stayed up so late the night before. I was exhausted. I should have left home earlier, too, because I arrived ten minutes late. And I definitely shouldn't have talked so much about my salary. Maybe I could have asked more questions about the team. Lesson learned!",
                                       ["should have / shouldn't have", "must have ile karıştırmama", "Kibar eleştiri"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Gerek yokmuş", "needn't have ile didn't need to arasındaki farkı bilerek gereksiz yapılan işleri anlatabilirim.",
    {"kind": "dialogue", "title": "Piknik hazırlığı", "lines": [
        {"speaker": "Defne", "text": "I made three kinds of salad and two cakes for the picnic."},
        {"speaker": "Mert", "text": "Oh, you needn't have made so much! Everyone else brought food too."},
        {"speaker": "Defne", "text": "Really? I should have asked. What about you? Did you bring drinks?"},
        {"speaker": "Mert", "text": "No, I didn't need to. The park café gives free water to everyone."},
        {"speaker": "Defne", "text": "And I took a taxi because I thought it would rain. I needn't have worried. It's sunny!"},
        {"speaker": "Mert", "text": "Never mind. At least we won't go hungry."}],
     "questions": [
        mc("Did Defne make a lot of food?", ["Yes, but it wasn't necessary.", "No, she forgot.", "Yes, and it was necessary."], 0, "\"you needn't have made so much\""),
        mc("Did Mert bring drinks?", ["Yes", "No, it wasn't necessary"], 1, "\"I didn't need to.\""),
     ]},
    {"explanation": "İkisi de \"gerek yoktu\" anlamına gelir, ama farklı bir şey söyler:\n\n| Yapı | Eylem yapıldı mı? | Örnek |\n|---|---|---|\n| **needn't have** + V3 | **Evet, yapıldı** (ama gereksizdi) | You **needn't have made** so much. (Yaptın, ama gerek yokmuş.) |\n| **didn't need to** + V1 | Genellikle **hayır**, yapılmadı | I **didn't need to** bring drinks. (Getirmedim, çünkü gerek yoktu.) |\n\n**Daha fazla örnek:**\n\n- I **needn't have taken** an umbrella. It didn't rain. (Şemsiye aldım, boşunaymış.)\n- I **didn't need to take** an umbrella. The forecast said sun. (Almadım, gerek yoktu.)\n\n**Dikkat:** **didn't need to** bazen eylem yapılmış olsa da kullanılabilir (*I didn't need to wait, but I did.*), ama **needn't have** her zaman eylemin yapıldığını gösterir.\n\n**didn't have to** = didn't need to\n\n- *We **didn't have to** pay. It was free.*\n\n**Sık kullanılan kalıp:** *You **needn't have bothered**.* (Zahmet etmeseydin. / Boşuna uğraşmışsın.) *I **needn't have worried**.* (Boşuna endişelenmişim.)",
     "examples": [{"en": "I needn't have worried. The exam was easy.", "tr": "Boşuna endişelenmişim. Sınav kolaydı."},
                  {"en": "We didn't need to book. The restaurant was empty.", "tr": "Rezervasyon yapmamıza gerek yoktu. Restoran boştu."},
                  {"en": "You needn't have bought me a present!", "tr": "Bana hediye almana gerek yoktu!"}],
     "turkishNote": "Türkçede \"Boşuna endişelenmişim\" ve \"Endişelenmeme gerek yoktu\" farklı şeyler anlatır; İngilizce de bu farkı needn't have (yaptım, boşunaymış) ve didn't need to (gerek yoktu, yapmadım) ile yapar. \"Boşuna\" kelimesini düşünmek işe yarar: \"boşuna yaptım\" diyorsanız needn't have kullanın."},
    [
        mc("\"Şemsiye almışım, boşunaymış.\"", ["I didn't need to take an umbrella.", "I needn't have taken an umbrella."], 1, "Yapıldı ama gereksizdi."),
        mc("\"We didn't need to queue.\" Sıraya girdiler mi?", ["Muhtemelen hayır", "Evet"], 0, "didn't need to."),
        mc("\"You needn't have bothered.\" anlamı:", ["Zahmet etmeseydin.", "Zahmet etmeliydin."], 0, "Kalıp."),
        mc("Hangisi didn't need to ile aynı anlamda?", ["didn't have to", "mustn't"], 0, "didn't have to."),
        gap("I needn't ___ (cook). They'd already eaten.", ["have cooked"], "needn't have + V3."),
        gap("We didn't ___ to pay. Entry was free.", ["need", "have"], "didn't need / have to."),
        gap("You needn't have ___ (buy) so much bread.", ["bought"], "buy-bought-bought."),
        gap("I needn't have ___ (worry). Everything went well.", ["worried"], "V3."),
        listen("I got up at five to finish my report before the meeting. Then my manager called and said the meeting had been postponed until next week. I needn't have rushed at all.", "Konuşan erken kalkmakla ilgili ne düşünüyor?", ["Gerekliydi", "Boşunaymış", "Daha da erken kalkmalıydı"], 1, "\"I needn't have rushed at all.\""),
        typ("İngilizcesi: \"Bu kadar çok yemek yapmana gerek yoktu!\" (needn't have)", variants("You needn't have cooked so much!", "You needn't have made so much food!", "You needn't have cooked so much food!"), "You needn't have cooked so much!"),
    ],
    {"kind": "speaking", "task": speak("Boşuna yaptığınız 3 şeyi (needn't have) ve gerek olmadığı için yapmadığınız 3 şeyi (didn't need to / didn't have to) anlatın. Her biri için nedenini de söyleyin.",
                                       "Last week I needn't have studied all night for the quiz, because the teacher cancelled it. I needn't have taken a jacket to Antalya. It was thirty degrees. And I needn't have worried about my presentation. Everyone loved it. On the other hand, I didn't need to cook on Sunday, because my aunt invited us for lunch. I didn't have to pay for parking, because it was a holiday. And I didn't need to take the bus, because my friend gave me a lift.",
                                       ["needn't have + V3", "didn't need to / didn't have to", "Doğru anlam farkı"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Olayı yeniden kurmak", "Bütün geçmiş modal yapılarını birleştirerek bir olayı kanıtlara dayanarak analiz edebilir ve yorumlayan bir metin yazabilirim.",
    {"kind": "text", "title": "Okuyucu mektubu: Kayıp bisiklet", "body": "Last Tuesday, my bike disappeared from outside the library. I had locked it to the railings at 2 p.m., and when I came out at 5, only the lock was left, cut cleanly in half.\n\nThe thief must have used a strong cutting tool, because it was a thick steel lock. They can't have done it quickly, so someone must have seen something. However, the security guard told me the camera at the entrance hadn't been working for a week.\n\nIn hindsight, I made a few mistakes. I shouldn't have left the bike in the same place every day, and I should have registered it with the police. I might have got it back if I had done that.\n\nThe library should have repaired the camera much sooner. And the city needn't have spent so much money on new bike lanes if it can't protect the bikes that use them.",
     "questions": [
        mc("Why does the writer think the thief used a strong tool?", ["The bike was heavy.", "It was a thick steel lock.", "A witness saw it."], 1, "\"because it was a thick steel lock\""),
        mc("What does the writer criticise the library for?", ["Closing early", "Not repairing the camera sooner", "Not having bike racks"], 1, "\"should have repaired the camera much sooner\""),
     ]},
    {"explanation": "**Geçmiş modal yapıları: Bütün tablo**\n\n| İşlev | Yapı | Türkçe |\n|---|---|---|\n| Kesin çıkarım | **must have** + V3 | -mış olmalı |\n| İmkânsızlık | **can't / couldn't have** + V3 | -mış olamaz |\n| Olasılık | **may / might / could have** + V3 | -mış olabilir |\n| Olumsuz olasılık | **may not / might not have** + V3 | -mamış olabilir |\n| Eleştiri / pişmanlık | **should / ought to have** + V3 | -malıydı |\n| Olumsuz eleştiri | **shouldn't have** + V3 | -mamalıydı |\n| Gereksiz yapılmış | **needn't have** + V3 | gerek yokmuş (yapıldı) |\n| Kaçırılan fırsat | **could have** + V3 | -abilirdi (yapılmadı) |\n\n**Bir olayı analiz ederken yapı:**\n\n1. **Olgular:** past simple / past perfect (*I had locked it at 2 p.m.*)\n2. **Çıkarımlar:** must / can't / might have (*The thief must have used ...*)\n3. **Değerlendirme:** should / shouldn't have (*The library should have ...*)\n4. **Ders:** In hindsight, ... / Next time, ...\n\n**Kanıt dili:** *judging by* (-e bakılırsa), *the evidence suggests*, *it seems likely that*, *there's no way that*",
     "examples": [{"en": "Judging by the footprints, there must have been two people.", "tr": "Ayak izlerine bakılırsa, iki kişi olmalı."},
                  {"en": "The evidence suggests that the fire may have started in the kitchen.", "tr": "Kanıtlar yangının mutfakta başlamış olabileceğini gösteriyor."},
                  {"en": "In hindsight, they should have called the police immediately.", "tr": "Geriye dönüp bakınca, polisi hemen aramalıydılar."}],
     "turkishNote": "Türkçede \"-mış\" eki hem çıkarım hem duyulan geçmiş hem de bitmiş eylem için kullanılabilir; bu yüzden Türkçe konuşanlar İngilizcede kesinlik düzeyini belirtmeyi unutabilir. \"Hırsız güçlü bir alet kullanmış\" cümlesini İngilizceye çevirirken kendinize sorun: Bunu biliyor musunuz (used), kesin mi düşünüyorsunuz (must have used), yoksa sadece olası mı (might have used)?"},
    [
        mc("Kesin çıkarım:", ["He may have taken it.", "He must have taken it."], 1, "must have."),
        mc("Eleştiri:", ["You should have told me.", "You must have told me."], 0, "should have."),
        mc("İmkânsızlık:", ["She can't have done it.", "She shouldn't have done it."], 0, "can't have."),
        mc("Gereksiz yapılmış:", ["I didn't need to run.", "I needn't have run."], 1, "needn't have."),
        gap("___ by the mess, there must have been a party. (-e bakılırsa)", ["Judging"], "Judging by."),
        gap("The evidence ___ that the boat sank in a storm. (gösteriyor)", ["suggests"], "the evidence suggests."),
        gap("He ___ have stolen it. He was with me all evening. (imkânsız)", ["can't", "couldn't"], "can't / couldn't have."),
        gap("In ___, I shouldn't have trusted him. (geriye dönüp bakınca)", ["hindsight"], "in hindsight."),
        listen("When the police arrived, the window was open and the jewellery box was empty. The dog hadn't barked, so the thief must have been someone the dog knew. It can't have been the gardener, because he was on holiday. The owners should have installed an alarm years ago.", "Köpeğin havlamaması neyi gösteriyor?", ["Köpek uyuyordu", "Hırsız köpeğin tanıdığı biriydi", "Hırsız yoktu"], 1, "\"the thief must have been someone the dog knew\""),
        order(["Judging", "by", "the", "evidence", "the", "fire", "might", "have", "started", "in", "the", "kitchen"], "Judging by the evidence the fire might have started in the kitchen.", "Judging by + modal have + V3.", "Kanıtlara bakılırsa yangın mutfakta başlamış olabilir."),
    ],
    {"kind": "writing", "task": write("Bir gazetenin \"okuyucu mektupları\" bölümü için yaşadığınız (ya da hayal ettiğiniz) olumsuz bir olayı analiz eden bir mektup yazın (180–220 kelime): kaybolan bir kargo, iptal edilen bir konser, bozuk çıkan bir ürün, vb. Olguları anlatın; must have, can't have ve might have ile çıkarımlar yapın; should / shouldn't have ile sorumluları eleştirin ve needn't have ile bir gereksiz yapılan işi anlatın.",
                                      "Dear Editor,\n\nI am writing about the concert that was cancelled at the City Stadium last Saturday.\n\nThousands of us had travelled from other cities, and many had booked hotels. At 8 p.m., when the concert should have started, an announcement said it had been cancelled \"for technical reasons\".\n\nJudging by the storm the night before, the stage must have been damaged. The organisers can't have discovered this at the last minute, as workers had been on the stage all afternoon. They might have hoped to fix it in time, but they clearly couldn't.\n\nIn my opinion, the organisers should have informed us that morning. A simple text message would have saved thousands of people a lot of time and money. They also shouldn't have kept the gates open until 7:30, letting people in when they already knew there was a problem.\n\nPersonally, I needn't have taken two days off work and paid for a hotel. I am still waiting for a refund.\n\nI hope the organisers will learn from this and treat their audiences with more respect in the future.\n\nYours faithfully,\nZeynep Arslan",
                                      ["Olgular ve geçmiş zamanlar", "must / can't / might have ile çıkarım", "should / shouldn't have ile eleştiri", "needn't have", "Resmî mektup yapısı"])},
)

u.test([
    mc("\"The ground is wet.\" → It ___ rained.", ["must have", "should have"], 0, "Çıkarım"),
    mc("Doğru olumsuz çıkarım:", ["She mustn't have seen it.", "She can't have seen it."], 1, "can't have"),
    mc("\"Belki e-postamı almadı.\"", ["He couldn't have received my email.", "He might not have received my email."], 1, "might not have"),
    mc("\"Sana söylemeliydim.\"", ["I should have told you.", "I must have told you."], 0, "should have"),
    mc("\"Boşuna endişelenmişim.\"", ["I didn't need to worry.", "I needn't have worried."], 1, "needn't have"),
    gap("I can't find my phone. I ___ have left it on the bus. (olabilir)", ["might", "may", "could"], "Olasılık"),
    gap("You ___ have eaten all that chocolate. (yememeliydin)", ["shouldn't"], "shouldn't have"),
    gap("She must have ___ (forget) about our meeting.", ["forgotten"], "V3"),
    gap("We didn't ___ to book. The restaurant was empty.", ["need", "have"], "didn't need to"),
    gap("He couldn't have ___ (see) us. It was too dark.", ["seen"], "V3"),
    mc("\"You could have called me!\" burada:", ["Tahmin", "Eleştiri"], 1, "Kaçırılmış fırsat"),
    gap("In ___, we should have left earlier. (geriye dönüp bakınca)", ["hindsight"], "in hindsight"),
    listen("The flat was empty when we arrived. The table was set for two and the candles had burned down completely. They must have been waiting for someone who never came. Or they might have left in a hurry. We'll probably never know.", "Konuşan ne olduğundan ne kadar emin?", ["Tamamen emin", "Emin değil, birden fazla teori var", "Polis açıkladı"], 1, "must have / might have / never know"),
    typ("İngilizcesi: \"Kapıyı açık bırakmış olamaz.\" (he, leave the door open)", variants("He can't have left the door open.", "He couldn't have left the door open."), "He can't have left the door open."),
    write("Tarihte çözülememiş bir gizemi ya da hayatınızda açıklanamayan bir olayı anlatın (180–220 kelime). Olguları verin; must have, can't have, may / might / could have ile farklı teorileri tartışın; en mantıklı açıklamayı savunun ve should have ile birinin (ya da sizin) yapması gerekeni değerlendirin.",
          "One of the strangest things that ever happened to me took place during a summer holiday in Ayvalık when I was twelve.\n\nOne evening, my grandmother's gold bracelet disappeared from the kitchen table. She had taken it off to cook, and twenty minutes later it was gone. The windows were open, but the house was on the second floor, and nobody else had come in.\n\nWe discussed several theories. My cousin might have taken it as a joke, but he swore he hadn't. It could have fallen behind the cupboard, but we moved everything and found nothing. My uncle even suggested that the cat may have knocked it off the table, but the cat can't have carried it very far.\n\nThree days later, my grandfather found it on the roof, next to a seagull's nest. A seagull must have flown in through the window, attracted by the shiny gold, and carried it away. It sounds unbelievable, but there was no other explanation.\n\nIn hindsight, my grandmother shouldn't have left it near an open window. And we needn't have blamed my poor cousin. We still laugh about it every summer.",
          ["Olgular", "must / can't / may / might / could have", "En mantıklı açıklama", "should / needn't have", "Akıcı anlatım"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

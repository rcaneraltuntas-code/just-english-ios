"""A2 Ünite 9: Gelecek."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("A2", 9, "Gelecek", "The Future",
         "Gelecek hakkında tahminlerde bulunabilir, ne kadar emin olduğumu belirtebilir, anlık kararlar verip yardım teklif edebilir ve çevreyle ilgili basit görüşlerimi paylaşabilirim.",
         ["will / won't (tahmin)", "Will ...? ve I think / I don't think ... will", "might / might not (olasılık)", "will: anlık karar, teklif, söz", "will ve going to"],
         ["çevre ve doğa", "iklim ve hava", "geleceğin dünyası"],
         {"title": "2050 yılında dünya", "durationMinutes": 45,
          "goal": "Gruplar 2050 yılı için bir konu seçer (şehirler, iş hayatı, okul, çevre) ve will / won't / might ile 5 tahmin hazırlar. Sınıfa sunarlar; diğer öğrenciler I agree / I don't think so ile tepki verir ve her tahmin için 'kesinlik ölçeği'nde oylama yapılır."})

u.vocab([
    ("environment", "çevre", "We must protect the environment.", "Çevreyi korumalıyız.", None),
    ("planet", "gezegen", "Earth is our only planet.", "Dünya bizim tek gezegenimiz.", None),
    ("climate change", "iklim değişikliği", "Climate change is a big problem.", "İklim değişikliği büyük bir sorun.", None),
    ("pollution", "kirlilik", "Air pollution is bad in big cities.", "Büyük şehirlerde hava kirliliği kötü.", None),
    ("recycle", "geri dönüştürmek", "We recycle paper and plastic.", "Kağıt ve plastiği geri dönüştürüyoruz.", None),
    ("rubbish", "çöp", "Don't leave rubbish on the beach.", "Plajda çöp bırakma.", "Amerikan: garbage / trash."),
    ("plastic", "plastik", "There's too much plastic in the sea.", "Denizde çok fazla plastik var.", None),
    ("energy", "enerji", "Solar energy is clean.", "Güneş enerjisi temiz.", None),
    ("electric car", "elektrikli araba", "Most people will drive electric cars.", "Çoğu insan elektrikli araba kullanacak.", None),
    ("forest", "orman", "We need to save the forests.", "Ormanları kurtarmamız gerek.", None),
    ("drought", "kuraklık", "There was a drought last summer.", "Geçen yaz kuraklık vardı.", "Okunuşu: /draʊt/"),
    ("flood", "sel", "The flood destroyed many houses.", "Sel birçok evi yıktı.", "Okunuşu: /flʌd/"),
    ("temperature", "sıcaklık", "Temperatures will rise.", "Sıcaklıklar artacak.", None),
    ("rise", "yükselmek, artmak", "Sea levels are rising.", "Deniz seviyeleri yükseliyor.", "rise → rose → risen"),
    ("disappear", "yok olmak", "Some animals might disappear.", "Bazı hayvanlar yok olabilir.", None),
    ("robot", "robot", "Robots will do many jobs.", "Robotlar birçok işi yapacak.", None),
    ("will", "-ecek (tahmin, karar)", "I think it will rain tomorrow.", "Bence yarın yağmur yağacak.", "'ll kısaltması: I'll, she'll"),
    ("won't", "-meyecek", "Prices won't go down.", "Fiyatlar düşmeyecek.", "will not'ın kısaltması"),
    ("might", "-ebilir (belki)", "It might snow tonight.", "Bu gece kar yağabilir.", "might + yalın fiil"),
    ("probably", "muhtemelen", "She'll probably be late.", "Muhtemelen geç kalacak.", None),
    ("definitely", "kesinlikle", "I'll definitely call you.", "Seni kesinlikle arayacağım.", None),
    ("perhaps / maybe", "belki", "Maybe we'll live on Mars.", "Belki Mars'ta yaşayacağız.", "Cümle başında."),
    ("promise", "söz vermek", "I promise I won't tell anyone.", "Kimseye söylemeyeceğime söz veriyorum.", None),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Bence olacak", "will ile gelecek hakkında tahminlerde bulunabilirim.",
    {"kind": "text", "title": "Gelecekte şehirler", "body": "What will cities look like in 2050? Experts have some ideas.\n\nMore people will live in cities. Today about 55% of people live in cities, but in 2050 it will probably be about 70%.\n\nMost cars will be electric, and some will drive themselves. There will be more parks and gardens on buildings, because they help keep cities cool.\n\nPeople will probably work from home more often. And robots will deliver our shopping!",
     "questions": [
        mc("How many people will live in cities in 2050?", ["About 55%", "About 70%", "About 90%"], 1, "\"in 2050 it will probably be about 70%\""),
        mc("Why will there be gardens on buildings?", ["They're beautiful.", "They help keep cities cool.", "They're cheap."], 1, "\"they help keep cities cool\""),
     ]},
    {"explanation": "**will** + yalın fiil → gelecek hakkında **tahmin** (bir görüşe ya da bilgiye dayalı)\n\n| | |\n|---|---|\n| I / You / He / She / It / We / They **will** ('ll) | live |\n\n- People **will** live longer.\n- It**'ll** be hot tomorrow.\n- There **will be** more robots.\n\nwill her özneyle aynıdır: she will (~~she wills~~), will + yalın fiil (~~will to go~~ / ~~will goes~~).\n\n**Tahmini yumuşatmak:**\n\n- I **think** + will: I think it'll rain.\n- **probably / definitely**: will'den **sonra** gelir → It'll **probably** rain. / She'll **definitely** win.\n- **Maybe / Perhaps**: cümle başında → Maybe they'll come.",
     "examples": [{"en": "I think robots will do a lot of jobs.", "tr": "Bence robotlar birçok işi yapacak."},
                  {"en": "There will be more electric cars.", "tr": "Daha çok elektrikli araba olacak."},
                  {"en": "Prices will probably go up.", "tr": "Fiyatlar muhtemelen artacak."}],
     "turkishNote": "Türkçedeki \"-ecek\" eki hem going to (plan) hem will (tahmin, karar) karşılığıdır. İngilizcede bir görüşe dayalı tahmin için will (I think it will...), gördüğümüz bir kanıta dayalı tahmin için going to (Look at the clouds, it's going to rain) daha doğaldır. \"There will be\" = olacak (var olacak)."},
    [
        mc("Hangisi doğru?", ["She wills come.", "She will come.", "She will comes."], 1, "will + yalın fiil."),
        mc("Hangisi doğru?", ["It will to rain.", "It will rain.", "It wills rain."], 1, "will + yalın fiil (to yok)."),
        gap("I think people ___ live on the moon one day.", ["will", "'ll"], "Tahmin → will."),
        gap("There ___ be more robots in 2050.", ["will"], "There will be."),
        gap("It'll ___ rain tomorrow. (muhtemelen)", ["probably"], "will + probably."),
        mc("Hangisi doğru?", ["It probably will rains.", "It'll probably rain.", "Probably it will to rain."], 1, "will + probably + yalın fiil."),
        order(["think", "I", "cars", "will", "be", "electric"], "I think cars will be electric.", "I think + özne + will + fiil.", "Bence arabalar elektrikli olacak."),
        listen("In the future, I think we'll eat less meat and more vegetables. Maybe we'll even eat insects!", "Konuşana göre gelecekte ne olacak?", ["Daha çok et yiyeceğiz", "Daha az et, daha çok sebze yiyeceğiz", "Sadece böcek yiyeceğiz"], 1, "\"we'll eat less meat and more vegetables\""),
        typ("İngilizce yazın: \"Bence yarın hava sıcak olacak.\"", variants("I think it'll be hot tomorrow.", "I think it will be hot tomorrow.", "I think tomorrow will be hot.", "I think the weather will be hot tomorrow."), "I think + it'll be hot + tomorrow."),
        match([("I will", "I'll"), ("she will", "she'll"), ("they will", "they'll"), ("it will", "it'll")], "Kısaltmaları eşleştirin."),
    ],
    {"kind": "speaking", "task": speak("2050 yılında şehrinizin nasıl olacağını tahmin edin. En az 5 tahmin yapın; I think, probably ve There will be kullanın.",
                                       "I think Istanbul will be bigger. There will be more metro lines and fewer cars. People will probably work from home. Maybe there will be robots in restaurants. The summers will definitely be hotter.",
                                       ["will + yalın fiil", "There will be", "probably / definitely doğru yerde"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "Olmayacak mı?", "won't ve Will ...? ile olumsuz tahminler yapıp tahmin sorabilirim.",
    {"kind": "dialogue", "title": "Radyo programı", "lines": [
        {"speaker": "Host", "text": "Professor, will we solve climate change?"},
        {"speaker": "Professor", "text": "I think we will, but it won't be easy. We won't stop it in ten years."},
        {"speaker": "Host", "text": "Will summers get hotter in Turkey?"},
        {"speaker": "Professor", "text": "Yes, they will. And I don't think we'll have enough water in some cities."},
        {"speaker": "Host", "text": "Will young people change things?"},
        {"speaker": "Professor", "text": "Definitely. They care a lot more about the environment."}],
     "questions": [
        mc("Does the professor think it will be easy to solve climate change?", ["Yes", "No"], 1, "\"it won't be easy\""),
        mc("What problem does the professor mention for some cities?", ["Too much rain", "Not enough water", "Too many people"], 1, "\"I don't think we'll have enough water in some cities\""),
     ]},
    {"explanation": "**Olumsuz:** will not = **won't** + yalın fiil\n\n- It **won't** be easy.\n- Prices **won't** go down.\n\n**Soru:** Will + özne + yalın fiil?\n\n- **Will** it rain tomorrow? – Yes, it **will**. / No, it **won't**.\n- **What will** the world **be like**?\n- **When will** you **know**?\n\n**I don't think ... will** → \"Bence ... -meyecek\"\n\n- **I don't think** it **will** rain. (doğal)\n- I think it won't rain. (doğru ama daha az doğal)\n\n**Kısa cevaplar:** I hope so. (Umarım.) / I hope not. (Umarım olmaz.) / I don't think so. (Sanmıyorum.)",
     "examples": [{"en": "Will we have flying cars? – I don't think so.", "tr": "Uçan arabalarımız olacak mı? – Sanmıyorum."},
                  {"en": "Don't worry. It won't take long.", "tr": "Merak etme. Uzun sürmeyecek."},
                  {"en": "I don't think she'll come.", "tr": "Geleceğini sanmıyorum."}],
     "turkishNote": "won't'un okunuşu /wəʊnt/ olup want /wɒnt/ ile karışabilir: I won't go (gitmeyeceğim) ≠ I want to go (gitmek istiyorum). \"Sanmıyorum\" İngilizcede \"I don't think so\" ile söylenir; \"I think not\" eski ve resmidir."},
    [
        mc("Hangisi doğru?", ["It won't be easy.", "It willn't be easy.", "It won't is easy."], 0, "won't + yalın fiil."),
        mc("Hangisi daha doğal?", ["I think it won't rain.", "I don't think it will rain."], 1, "I don't think ... will."),
        mc("\"Will it be cold tomorrow?\" (Hayır.)", ["No, it won't.", "No, it isn't.", "No, it doesn't."], 0, "No, it won't."),
        gap("Don't worry. It ___ take long. (sürmeyecek)", ["won't", "will not"], "won't."),
        gap("___ people live on Mars one day?", ["Will"], "Will + özne + fiil?"),
        gap("What will the world ___ like in 2100?", ["be"], "What will ... be like?"),
        mc("\"Will it rain at the wedding?\" Olmasın istiyorsunuz:", ["I hope so.", "I hope not."], 1, "I hope not = Umarım olmaz."),
        order(["don't", "I", "think", "she'll", "come"], "I don't think she'll come.", "I don't think + özne + will + fiil.", "Geleceğini sanmıyorum."),
        listen("Will we have robot teachers in the future? – I don't think so. Students will always need real teachers.", "Konuşan robot öğretmenler hakkında ne düşünüyor?", ["Olacaklar", "Olmayacaklar, gerçek öğretmenler hep gerekli", "Emin değil"], 1, "\"I don't think so. Students will always need real teachers.\""),
        typ("İngilizce yazın: \"Uzun sürmeyecek.\"", variants("It won't take long.", "It will not take long."), "It won't + take long."),
    ],
    {"kind": "speaking", "task": speak("JAI'ye gelecek hakkında 4 tane Will...? sorusu sorun. Sonra JAI'nin sorularına I think / I don't think / I hope so / I hope not ile cevap verin.",
                                       "Will people live longer? Will we use cash in 2040? Will robots take our jobs? Will Turkey win the World Cup? ... I hope so! ... I don't think we'll use cash. ... I hope not!",
                                       ["Will + özne + fiil? doğru", "won't / I don't think ... will", "I hope so / not"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "Belki olur", "might ile olasılıkları ve ne kadar emin olduğumu ifade edebilirim.",
    {"kind": "dialogue", "title": "Hafta sonu planı", "lines": [
        {"speaker": "Zeynep", "text": "Are you coming to the beach on Saturday?"},
        {"speaker": "Bulut", "text": "I'm not sure. I might go to my parents' house."},
        {"speaker": "Zeynep", "text": "The weather forecast says it might rain on Saturday anyway."},
        {"speaker": "Bulut", "text": "Really? Then maybe we'll go on Sunday."},
        {"speaker": "Zeynep", "text": "Sunday is better. It definitely won't rain on Sunday. It'll be sunny."},
        {"speaker": "Bulut", "text": "OK, I'll probably come then. I might bring my cousin too."}],
     "questions": [
        mc("Is Bulut sure about Saturday?", ["Yes", "No"], 1, "\"I'm not sure. I might go to my parents' house.\""),
        mc("What will the weather be like on Sunday?", ["Rainy", "Sunny", "Windy"], 1, "\"It'll be sunny.\""),
     ]},
    {"explanation": "**might** + yalın fiil → olabilir, belki (emin değilim)\n\n- It **might** rain. (Yağmur yağabilir.)\n- I **might not** come. (Gelmeyebilirim.)\n\nmight her özneyle aynıdır ve -s, to almaz.\n\n**Kesinlik ölçeği:**\n\n| Kesinlik | İfade |\n|---|---|\n| 100% ✅ | It **will definitely** rain. |\n| 80% | It**'ll probably** rain. |\n| 50% | It **might** rain. / **Maybe** it'll rain. |\n| 20% | It **probably won't** rain. |\n| 0% ❌ | It **definitely won't** rain. |\n\n**Dikkat:** probably / definitely olumsuz cümlede won't'tan **önce** gelir: It **probably won't** rain.",
     "examples": [{"en": "Take an umbrella. It might rain.", "tr": "Şemsiye al. Yağmur yağabilir."},
                  {"en": "I might not finish the project today.", "tr": "Projeyi bugün bitiremeyebilirim."},
                  {"en": "He probably won't come. He's very busy.", "tr": "Muhtemelen gelmeyecek. Çok meşgul."}],
     "turkishNote": "Türkçedeki \"-ebilir\" eki hem yetenek (can) hem olasılık (might) anlamı taşır: \"Yüzebilirim\" = I can swim; \"Yağmur yağabilir\" = It might rain. Olasılık için can değil might kullanılır: \"It can rain tomorrow\" yanlış anlam verir."},
    [
        mc("Olasılık: \"Yarın kar yağabilir.\"", ["It can snow tomorrow.", "It might snow tomorrow."], 1, "Olasılık → might."),
        mc("Hangisi doğru?", ["She mights come.", "She might come.", "She might to come."], 1, "might + yalın fiil."),
        gap("I'm not sure. I ___ go to the party. (belki)", ["might"], "might."),
        gap("He might ___ come. He's ill. (gelmeyebilir)", ["not"], "might not."),
        gap("It probably ___ rain. The sky is blue. (yağmayacak)", ["won't", "will not"], "probably won't."),
        mc("En emin olan hangisi?", ["It might rain.", "It'll probably rain.", "It'll definitely rain."], 2, "definitely = %100."),
        mc("Hangisi doğru?", ["It won't probably rain.", "It probably won't rain."], 1, "probably won't."),
        order(["might", "We", "move", "to", "Izmir", "next", "year"], "We might move to Izmir next year.", "Özne + might + fiil + yer + zaman.", "Gelecek yıl İzmir'e taşınabiliriz."),
        listen("I might change my job next year. I'm not sure yet. But I'll definitely take a long holiday.", "Konuşan neden kesinlikle emin?", ["İş değiştirmekten", "Uzun bir tatil yapmaktan", "Taşınmaktan"], 1, "\"I'll definitely take a long holiday\""),
        typ("İngilizce yazın: \"Şemsiye al. Yağmur yağabilir.\"", variants("Take an umbrella. It might rain.", "Take an umbrella, it might rain.", "Take your umbrella. It might rain."), "Take an umbrella. + It might rain."),
    ],
    {"kind": "speaking", "task": speak("Gelecek yıl hayatınızda neler olacağını kesinlik ölçeğini kullanarak anlatın: 1 definitely, 1 probably, 2 might, 1 probably won't.",
                                       "Next year I'll definitely finish my English course. I'll probably get a new job. I might move to a new flat, and I might buy a car. I probably won't travel abroad because it's expensive.",
                                       ["definitely / probably doğru yerde", "might + yalın fiil", "probably won't doğru"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Ben yaparım!", "will ile anlık kararlar verebilir, yardım teklif edebilir ve söz verebilirim.",
    {"kind": "dialogue", "title": "Mutfakta", "lines": [
        {"speaker": "Mum", "text": "Oh no, we haven't got any bread."},
        {"speaker": "Kaan", "text": "I'll go to the shop. I'll be back in ten minutes."},
        {"speaker": "Mum", "text": "Thanks. Oh, and the phone is ringing!"},
        {"speaker": "Kaan", "text": "I'll answer it. ... Hello? ... Mum, it's Aunt Sevim."},
        {"speaker": "Mum", "text": "Tell her I'll call her back."},
        {"speaker": "Kaan", "text": "OK. And don't worry, I won't forget the bread. I promise!"}],
     "questions": [
        mc("What does Kaan decide to do first?", ["Call his aunt", "Go to the shop", "Make dinner"], 1, "\"I'll go to the shop.\""),
        mc("What does Kaan promise?", ["He won't forget the bread.", "He'll call his aunt.", "He'll cook dinner."], 0, "\"I won't forget the bread. I promise!\""),
     ]},
    {"explanation": "**will** tahmin dışında şunlar için de kullanılır:\n\n| Kullanım | Örnek |\n|---|---|\n| **Anlık karar** (konuşurken veriliyor) | The phone's ringing. – **I'll** answer it. |\n| **Teklif** | **I'll** carry your bag. / **Shall I** open the window? |\n| **Söz** | **I'll** call you tomorrow. / **I won't** tell anyone. |\n| **Rica** | **Will** you help me, please? |\n\n**going to ile karşılaştırın:**\n\n- **I'm going to** buy bread. (Önceden karar verdim, planım.)\n- We've got no bread? **I'll** buy some. (Şu an karar verdim.)\n\n**Shall I / Shall we** (öneri, teklif): **Shall I** help you? / **Shall we** go?",
     "examples": [{"en": "It's cold in here. – I'll close the window.", "tr": "Burası soğuk. – Pencereyi kapatayım."},
                  {"en": "Shall I carry that for you?", "tr": "Onu senin için taşıyayım mı?"},
                  {"en": "I promise I'll be careful.", "tr": "Dikkatli olacağıma söz veriyorum."}],
     "turkishNote": "Türkçedeki \"-eyim\" (kapatayım, açayım) eki çoğu zaman anlık kararı ya da teklifi gösterir ve İngilizcede \"I'll ...\" ile karşılanır. Restoranda sipariş verirken de will kullanılır: I'll have the fish, please (Ben balık alayım)."},
    [
        mc("Telefon çalıyor. Siz:", ["I'm going to answer it.", "I'll answer it."], 1, "Anlık karar → I'll."),
        mc("Bileti geçen hafta aldınız:", ["I'll fly to Ankara on Monday.", "I'm going to fly to Ankara on Monday."], 1, "Önceden plan → going to."),
        gap("This bag is heavy. – I'll ___ it for you. (carry)", ["carry"], "I'll + yalın fiil."),
        gap("___ I open the window? (açayım mı)", ["Shall"], "Shall I...?"),
        gap("I promise I ___ tell anyone. (söylemeyeceğim)", ["won't", "will not"], "Söz → won't."),
        mc("Restoranda sipariş:", ["I'll have the soup, please.", "I have the soup, please.", "I'm having soup yesterday."], 0, "Sipariş → I'll have."),
        order(["I'll", "call", "you", "back", "in", "five", "minutes"], "I'll call you back in five minutes.", "I'll + fiil + nesne + back + zaman.", "Beş dakika içinde seni geri arayacağım."),
        listen("I'm so tired and I haven't cooked anything. – Don't worry. I'll make dinner tonight. You sit down.", "Kim yemek yapacak?", ["Yorgun olan kişi", "İkinci konuşan", "Kimse"], 1, "\"I'll make dinner tonight.\""),
        typ("İngilizce yazın: \"Pencereyi kapatayım.\"", variants("I'll close the window.", "I will close the window.", "I'll shut the window."), "I'll + close the window."),
        match([("The phone's ringing.", "I'll get it."), ("I'm thirsty.", "I'll get you some water."), ("It's dark in here.", "I'll turn on the light."), ("I can't do this exercise.", "I'll help you.")], "Durumlarla anlık kararları eşleştirin."),
    ],
    {"kind": "speaking", "task": speak("JAI size sorunlar söyleyecek (\"I'm hungry\", \"My car broke down\", \"I can't find my keys\"). Her biri için will ile anlık bir teklif ya da karar söyleyin; en az birinde Shall I...? kullanın ve bir de söz verin.",
                                       "I'll make you a sandwich. ... I'll drive you to work. ... Shall I help you look for them? ... I promise I'll be on time tomorrow.",
                                       ["I'll + yalın fiil", "Shall I...? doğru", "Söz verme ifadesi"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Gezegenimiz", "Çevre sorunları hakkında tahminlerde bulunup ne yapabileceğimizi tartışabilirim.",
    {"kind": "text", "title": "Öğrenci kulübü posteri", "body": "SAVE OUR PLANET – What will happen if we don't act?\n\nScientists say temperatures will rise by 2°C or more. There will probably be more droughts in some countries and more floods in others. Some animals might disappear forever.\n\nBut it's not too late! Here's what we can do:\n• Use less plastic. Take your own bag to the shop.\n• Recycle paper, glass and plastic.\n• Walk, cycle or use public transport.\n• Switch off lights and devices when you don't use them.\n\nJoin our Green Club! We're going to clean the beach next Saturday. Will you help us?",
     "questions": [
        mc("What might happen to some animals?", ["They might disappear.", "They will live longer.", "They will move to cities."], 0, "\"Some animals might disappear forever.\""),
        mc("What is the Green Club going to do next Saturday?", ["Plant trees", "Clean the beach", "Recycle paper"], 1, "\"We're going to clean the beach next Saturday.\""),
     ]},
    {"explanation": "Bu ünitede gördüğümüz gelecek yapılarının hepsi bir arada:\n\n| Yapı | Kullanım | Örnek |\n|---|---|---|\n| will | görüşe dayalı tahmin | Temperatures **will** rise. |\n| might | olasılık | Some animals **might** disappear. |\n| will | anlık karar / teklif | I**'ll** join the club! |\n| going to | plan / niyet | We**'re going to** clean the beach. |\n| going to | kanıta dayalı tahmin | Look at the smoke. There**'s going to** be a fire. |\n| present continuous | ayarlanmış plan | We**'re meeting** at 9 on Saturday. |\n\n**Görüş bildirmek:**\n\n- I'm worried that ... (... diye endişeleniyorum)\n- I'm sure ... will ... (... -eceğinden eminim)\n- We need to ... / We should ...",
     "examples": [{"en": "I'm worried that there won't be enough water.", "tr": "Yeterli su olmayacağından endişeleniyorum."},
                  {"en": "I'm sure young people will make a difference.", "tr": "Gençlerin bir fark yaratacağından eminim."},
                  {"en": "We should use less plastic.", "tr": "Daha az plastik kullanmalıyız."}],
     "turkishNote": "Hangi gelecek yapısını seçeceğinizden emin değilseniz şunu sorun: Bu bir plan mı (going to / present continuous), bir tahmin mi (will / might), yoksa şu an verdiğim bir karar mı (will)? \"Make a difference\" = fark yaratmak (do a difference değil)."},
    [
        mc("Plan: \"Gelecek cumartesi plajı temizleyeceğiz.\"", ["We'll clean the beach next Saturday.", "We're going to clean the beach next Saturday."], 1, "Plan → going to."),
        mc("Olasılık: \"Bazı hayvanlar yok olabilir.\"", ["Some animals might disappear.", "Some animals are disappearing tomorrow."], 0, "Olasılık → might."),
        mc("Anlık karar: \"Kulübe katılıyorum!\"", ["I'll join the club!", "I'm joining the club since yesterday."], 0, "Anlık karar → will."),
        gap("I'm worried ___ there won't be enough water.", ["that"], "I'm worried that..."),
        gap("Temperatures ___ rise by 2 degrees. (tahmin)", ["will"], "Tahmin → will."),
        gap("We need to use ___ plastic. (daha az)", ["less"], "less + sayılamaz."),
        gap("Young people will make a ___. (fark)", ["difference"], "make a difference."),
        order(["sure", "I'm", "we", "will", "find", "a", "solution"], "I'm sure we will find a solution.", "I'm sure + özne + will + fiil.", "Bir çözüm bulacağımızdan eminim."),
        listen("I think the biggest problem will be water. Our city might have a drought this summer, so we're going to collect rainwater at home.", "Konuşan evde ne yapacak?", ["Su satın alacak", "Yağmur suyu toplayacak", "Taşınacak"], 1, "\"we're going to collect rainwater at home\""),
        typ("İngilizce yazın: \"Daha az plastik kullanmalıyız.\"", variants("We should use less plastic.", "We need to use less plastic.", "We must use less plastic."), "We should + use less plastic."),
    ],
    {"kind": "writing", "task": write("Okul ya da şehir dergisi için çevre hakkında kısa bir yazı yazın (80–100 kelime): 2 tahmin (will), 1 olasılık (might), 2 öneri (should / need to) ve sizin bir planınız (going to).",
                                      "Our city in 2050\nI think summers will be hotter and there will be less water. Some trees in our parks might die. But I'm sure we can change things. We should plant more trees and we need to use less water at home. We should also use public transport more. My friends and I are going to start a recycling project at our school next month. Will you join us?",
                                      ["will ile tahmin", "might ile olasılık", "should / need to ile öneri", "going to ile plan"])},
)

u.test([
    mc("Hangisi doğru?", ["It will rains.", "It will rain."], 1, "will + yalın fiil"),
    gap("There ___ be more electric cars in the future.", ["will"], "There will be"),
    mc("Hangisi doğru?", ["It'll probably rain.", "It probably'll rain."], 0, "will + probably"),
    gap("Don't worry. It ___ hurt. (acıtmayacak)", ["won't", "will not"], "won't"),
    mc("Hangisi daha doğal?", ["I think he won't come.", "I don't think he'll come."], 1, "I don't think ... will"),
    mc("\"Will it be sunny?\" (Umarım.)", ["I hope so.", "I hope not."], 0, "I hope so."),
    mc("Olasılık:", ["It can snow tonight.", "It might snow tonight."], 1, "might"),
    gap("I might ___ go. I'm very tired. (gitmeyebilirim)", ["not"], "might not"),
    mc("Hangisi doğru?", ["It won't probably rain.", "It probably won't rain."], 1, "probably won't"),
    mc("Kapı çalıyor:", ["I'll open it.", "I'm going to open it."], 0, "Anlık karar"),
    gap("___ I carry your bag? (taşıyayım mı)", ["Shall"], "Shall I...?"),
    mc("Uçak bileti alındı:", ["I'll visit Rome in May.", "I'm going to visit Rome in May."], 1, "Plan → going to"),
    listen("I think it'll be a difficult year, but I'm sure we'll be fine. We might have to work harder, but we'll definitely succeed.", "Konuşan neyden kesinlikle emin?", ["Zor bir yıl olacağından", "Başaracaklarından", "Daha çok çalışacaklarından"], 1, "\"we'll definitely succeed\""),
    typ("İngilizce yazın: \"Bunu kimseye söylemeyeceğim, söz veriyorum.\"", variants("I won't tell anyone, I promise.", "I won't tell anyone. I promise.", "I promise I won't tell anyone.", "I won't tell anybody, I promise.", "I promise I won't tell anybody."), "I won't tell anyone + I promise."),
    write("\"Hayatım 10 yıl sonra\" başlıklı kısa bir yazı yazın (80–100 kelime). will, won't, might, probably / definitely ve en az bir going to kullanın.",
          "My life in ten years\nIn ten years I'll be 38. I think I'll live in a small house near the sea. I'll definitely have a dog! I might have children, but I'm not sure yet. I probably won't work in an office; I'll work from home. I'll speak English very well because I'm going to study every day. Maybe I'll travel to Japan. I hope I'll be happy and healthy.",
          ["will / won't doğru", "might doğru", "probably / definitely yeri doğru", "going to doğru"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

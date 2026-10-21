"""C1 Ünite 7: Deyimler."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("C1", 7, "Deyimler", "Idioms",
         "İş, duygular ve günlük hayatla ilgili yaygın İngilizce deyimleri, sabit ikilileri (binomials) ve kalıplaşmış ifadeleri anlayıp doğal bir şekilde kullanabilir, Türkçe deyimlerle benzerlik ve farklılıklarını bilebilir ve deyimleri doğru üslupta, ölçülü kullanabilirim.",
         ["iş ve başarı deyimleri", "duygular ve ilişkiler deyimleri", "sabit ikililer (binomials): pros and cons, ups and downs", "vücut ve benzetme deyimleri; Türkçe karşılıklar", "deyimleri doğru üslupta ve ölçülü kullanmak"],
         ["iş hayatı", "duygular ve insanlar", "günlük konuşma"],
         {"title": "Deyim düellosu", "durationMinutes": 45,
          "goal": "Sınıf iki takıma ayrılır. Öğretmen bir durum okur (Your boss has just given you three new projects), takımlar en uygun İngilizce deyimi bulmaya çalışır (I've got a lot on my plate). Ardından her takım bir Türkçe deyimi seçip İngilizce karşılığını sorar (Etekleri zil çalıyor → over the moon). Son turda takımlar 5 deyim içeren kısa bir skeç hazırlar."})

u.vocab([
    ("hit the nail on the head", "tam üstüne basmak", "You've hit the nail on the head. That's exactly the problem.", "Tam üstüne bastın. Sorun tam olarak bu.", None),
    ("cut corners", "işi baştan savma yapmak, kestirmeden gitmek", "Don't cut corners on safety.", "Güvenlik konusunda işi baştan savma yapma.", None),
    ("go the extra mile", "fazladan çaba göstermek", "She always goes the extra mile for her customers.", "Müşterileri için hep fazladan çaba gösterir.", None),
    ("call it a day", "paydos etmek, bugünlük bırakmak", "It's late. Let's call it a day.", "Geç oldu. Bugünlük paydos edelim.", None),
    ("back to square one", "başa dönmek, sıfırdan başlamak", "The plan failed, so we're back to square one.", "Plan başarısız oldu, yani başa döndük.", None),
    ("get the ball rolling", "işi başlatmak", "Let's get the ball rolling with a quick introduction.", "Kısa bir tanıtımla işe başlayalım.", None),
    ("pull your weight", "üzerine düşeni yapmak", "Everyone in the team needs to pull their weight.", "Ekipteki herkes üzerine düşeni yapmalı.", None),
    ("over the moon", "çok mutlu, havalara uçmuş", "She was over the moon about the job offer.", "İş teklifi yüzünden havalara uçtu.", None),
    ("down in the dumps", "morali bozuk, keyifsiz", "He's been a bit down in the dumps lately.", "Son zamanlarda biraz keyifsiz.", None),
    ("on edge", "gergin, tetikte", "Everyone was on edge before the results.", "Sonuçlardan önce herkes gergindi.", None),
    ("get on sb's nerves", "birinin sinirini bozmak", "His constant complaining gets on my nerves.", "Sürekli şikâyet etmesi sinirimi bozuyor.", None),
    ("see eye to eye", "aynı fikirde olmak", "We don't always see eye to eye.", "Her zaman aynı fikirde değiliz.", None),
    ("give sb the cold shoulder", "birine soğuk davranmak, yüz vermemek", "She gave me the cold shoulder at the party.", "Partide bana yüz vermedi.", None),
    ("pros and cons", "artıları ve eksileri", "Let's weigh up the pros and cons.", "Artılarını ve eksilerini tartalım.", None),
    ("ups and downs", "iniş çıkışlar", "Every relationship has its ups and downs.", "Her ilişkinin iniş çıkışları vardır.", None),
    ("sick and tired", "bıkıp usanmış", "I'm sick and tired of waiting.", "Beklemekten bıktım usandım.", None),
    ("by and large", "genel olarak", "By and large, the trip was a success.", "Genel olarak gezi başarılıydı.", None),
    ("cost an arm and a leg", "çok pahalı olmak, ateş pahası", "That car must have cost an arm and a leg.", "O araba ateş pahasına olmalı.", None),
    ("keep an eye on", "göz kulak olmak", "Can you keep an eye on my bag?", "Çantama göz kulak olur musun?", None),
    ("get cold feet", "son anda cesaretini kaybetmek", "He got cold feet before the wedding.", "Düğünden önce son anda cesaretini kaybetti.", None),
    ("have a lot on your plate", "başı kalabalık olmak, işi çok olmak", "I can't help. I've got a lot on my plate.", "Yardım edemem, başım çok kalabalık.", None),
    ("break the ice", "buzları eritmek", "He told a joke to break the ice.", "Buzları eritmek için bir şaka yaptı.", None),
    ("once in a blue moon", "kırk yılda bir", "I only see him once in a blue moon.", "Onu kırk yılda bir görüyorum.", None),
    ("the last straw", "bardağı taşıran son damla", "His rude email was the last straw.", "Kaba e-postası bardağı taşıran son damla oldu.", None),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "İş hayatında deyimler", "İş ve başarıyla ilgili yaygın deyimleri bağlamdan anlayabilir ve toplantılarda doğal bir şekilde kullanabilirim.",
    {"kind": "dialogue", "title": "Proje toplantısı", "lines": [
        {"speaker": "Leader", "text": "Right, let's get the ball rolling. As you know, the client rejected our first design."},
        {"speaker": "Ozan", "text": "So we're back to square one?"},
        {"speaker": "Leader", "text": "Not quite. They liked the colours, but they said the website was too slow."},
        {"speaker": "Ece", "text": "That's because we cut corners on the testing. We were in such a hurry."},
        {"speaker": "Leader", "text": "You've hit the nail on the head, Ece. This time, we need to go the extra mile."},
        {"speaker": "Ozan", "text": "And everyone needs to pull their weight. Last time, half the work was done by two people."},
        {"speaker": "Leader", "text": "Agreed. OK, it's six o'clock. Let's call it a day and start fresh tomorrow."}],
     "questions": [
        mc("Why did the client reject the design?", ["The colours were wrong.", "The website was too slow.", "It was too expensive."], 1, "\"they said the website was too slow\""),
        mc("What does Ozan complain about?", ["The client", "Some people didn't do their share of the work.", "The deadline"], 1, "\"half the work was done by two people\""),
     ]},
    {"explanation": "**Deyim (idiom):** Anlamı kelimelerin tek tek anlamından **çıkarılamayan** sabit ifade.\n\n- *hit the nail on the head* ≠ çiviye vurmak → **tam üstüne basmak**\n\n**İş hayatında sık kullanılan deyimler:**\n\n| Deyim | Anlam | Türkçe yakın karşılık |\n|---|---|---|\n| **get the ball rolling** | bir işi başlatmak | işe koyulmak |\n| **back to square one** | başa dönmek | sil baştan |\n| **cut corners** | baştan savma yapmak | işi kılıfına uydurmak |\n| **go the extra mile** | fazladan çaba göstermek | elinden gelenin fazlasını yapmak |\n| **hit the nail on the head** | tam doğru tespiti yapmak | tam üstüne basmak |\n| **pull your weight** | üzerine düşeni yapmak | taşın altına elini koymak |\n| **call it a day** | paydos etmek | bugünlük bu kadar |\n| **think outside the box** | yaratıcı düşünmek | kalıpların dışında düşünmek |\n| **on the same page** | aynı şeyi anlamış olmak | aynı frekansta olmak |\n| **a win-win situation** | herkesin kazandığı durum | |\n| **learn the ropes** | işin inceliklerini öğrenmek | işi öğrenmek |\n\n**Deyimler genellikle sabittir:** Kelimeleri değiştirmeyin.\n\n- ~~hit the nail on its head~~ / ~~back to square two~~\n- Ama fiil çekimlenir: *She **hit** the nail on the head.* / *We're **calling** it a day.*\n\n**Zamir uyumu:** *pull **your / their / my** weight*",
     "examples": [{"en": "Let's get the ball rolling with a quick update from each team.", "tr": "Her ekipten kısa bir güncellemeyle işe başlayalım."},
                  {"en": "It's my first week, so I'm still learning the ropes.", "tr": "İlk haftam, o yüzden hâlâ işin inceliklerini öğreniyorum."},
                  {"en": "Before we start, let's make sure we're all on the same page.", "tr": "Başlamadan önce hepimizin aynı şeyi anladığından emin olalım."}],
     "turkishNote": "Türkçede de iş hayatında çok deyim kullanılır (\"taşın altına elini koymak\", \"sil baştan\"). İngilizce deyimlerin bir kısmının Türkçede yakın karşılığı vardır, ama birebir çeviri neredeyse hiç işe yaramaz: \"Taşın altına elini koy\" İngilizcede \"put your hand under the stone\" değil, \"pull your weight\" olur. Deyimleri tek tek kelime olarak değil, bağlamıyla birlikte bir bütün olarak öğrenin."},
    [
        mc("\"Let's call it a day.\" anlamı:", ["Bugünlük paydos edelim.", "Bir gün arayalım."], 0, "call it a day."),
        mc("\"We're back to square one.\"", ["İlk kareye geldik.", "Başa döndük."], 1, "back to square one."),
        mc("\"He always cuts corners.\"", ["Hep köşeleri keser.", "İşini hep baştan savma yapar."], 1, "cut corners."),
        mc("\"Taşın altına elini koymak\" İngilizcede:", ["put your hand under the stone", "pull your weight"], 1, "pull your weight."),
        gap("You've hit the ___ on the head. That's exactly the problem.", ["nail"], "hit the nail on the head."),
        gap("She always goes the extra ___ for her clients.", ["mile"], "go the extra mile."),
        gap("Let's get the ___ rolling. Who wants to start?", ["ball"], "get the ball rolling."),
        gap("Is everyone on the same ___? (aynı şeyi anlamak)", ["page"], "on the same page."),
        listen("I'm not happy with the new intern. He doesn't really pull his weight, and when he does finish something, he cuts corners. To be fair, it's only his second week, so he's still learning the ropes.", "Konuşan stajyer hakkında neyi kabul ediyor?", ["Çok çalışkan olduğunu", "Henüz işin inceliklerini öğrendiğini", "İşten ayrılacağını"], 1, "\"he's still learning the ropes\""),
        match([("get the ball rolling", "işi başlatmak"), ("call it a day", "paydos etmek"), ("cut corners", "baştan savma yapmak"), ("pull your weight", "üzerine düşeni yapmak"), ("learn the ropes", "işin inceliklerini öğrenmek")], "Eşleştirin."),
    ],
    {"kind": "speaking", "task": speak("Bir ekip liderisiniz ve haftalık toplantıyı yönetiyorsunuz (1 dakika). Toplantıyı başlatın, bir sorunu tespit edin, ekibi motive edin ve toplantıyı bitirin. En az 6 iş deyimi kullanın: get the ball rolling, back to square one, cut corners, hit the nail on the head, go the extra mile, pull your weight, on the same page, think outside the box, call it a day.",
                                       "OK, everyone, let's get the ball rolling. First, the bad news: the client didn't like our proposal, so we're back to square one. Murat, you said last week that we'd cut corners on the research, and I think you hit the nail on the head. This time, we really need to think outside the box and go the extra mile. And I know it's been a busy month, but I need everyone to pull their weight. Let's make sure we're all on the same page before Friday. Right, I think we can call it a day. Thanks, everyone.",
                                       ["En az 6 iş deyimi", "Doğru bağlam", "Doğal toplantı akışı"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "Duygular ve insanlar", "Duyguları ve insan ilişkilerini anlatan deyimleri doğru bağlamda kullanabilirim.",
    {"kind": "text", "title": "Bir günlükten", "body": "What a week!\n\nOn Monday, I was really down in the dumps. My best friend Tuğçe had been giving me the cold shoulder for days, and I had no idea why.\n\nOn Wednesday, I was on edge all day, waiting for the exam results. And my brother kept playing the drums, which really got on my nerves.\n\nBut on Thursday, everything changed. I got the results: I'd passed with a high mark! I was over the moon. Then Tuğçe called. It turned out she thought I'd forgotten her birthday, but I'd actually planned a surprise party. We laughed about it for ages.\n\nWe don't always see eye to eye, but she's still my best friend. And my brother? He's still driving me up the wall with those drums.",
     "questions": [
        mc("Why was Tuğçe giving the writer the cold shoulder?", ["They had an argument.", "She thought the writer had forgotten her birthday.", "She was busy."], 1, "\"she thought I'd forgotten her birthday\""),
        mc("How did the writer feel about the exam results?", ["Disappointed", "Very happy", "Nervous"], 1, "\"I was over the moon.\""),
     ]},
    {"explanation": "**Duygular:**\n\n| Deyim | Anlam | Türkçe yakın karşılık |\n|---|---|---|\n| **over the moon** | çok mutlu | havalara uçmak, etekleri zil çalmak |\n| **on cloud nine** | çok mutlu | dünyalar onun olmak |\n| **down in the dumps** | keyifsiz, morali bozuk | morali sıfır |\n| **on edge** | gergin | diken üstünde |\n| **at the end of your tether** | sabrının sonuna gelmiş | sabrı taşmak |\n| **scared stiff** | ödü kopmuş | ödü patlamak |\n| **in two minds** | kararsız | iki arada bir derede |\n\n**İnsanlar ve ilişkiler:**\n\n| Deyim | Anlam | Türkçe yakın karşılık |\n|---|---|---|\n| **get on sb's nerves** | sinirini bozmak | sinirine dokunmak |\n| **drive sb up the wall** | çıldırtmak | çileden çıkarmak |\n| **see eye to eye** | aynı fikirde olmak | aynı fikri paylaşmak |\n| **give sb the cold shoulder** | soğuk davranmak | yüz vermemek |\n| **bite sb's head off** | birine aniden çıkışmak | birine patlamak |\n| **a pain in the neck** | baş belası | başının belası |\n| **get on like a house on fire** | çok iyi anlaşmak | çok iyi kaynaşmak |\n| **be in sb's good / bad books** | birinin gözünde iyi / kötü durumda olmak | gözüne girmek / gözünden düşmek |\n\n**Dikkat:** *see eye to eye* genellikle **olumsuz** kullanılır: *We **don't** always see eye to eye.*",
     "examples": [{"en": "She was over the moon when she heard the news.", "tr": "Haberi duyunca havalara uçtu."},
                  {"en": "I'm in two minds about whether to accept the offer.", "tr": "Teklifi kabul edip etmeme konusunda kararsızım."},
                  {"en": "We met at a conference and got on like a house on fire.", "tr": "Bir konferansta tanıştık ve çok iyi kaynaştık."}],
     "turkishNote": "Türkçe ve İngilizce deyimler bazen aynı imgeleri kullanır, bazen de tamamen farklıdır. \"Diken üstünde olmak\" İngilizcede \"on edge\" (kenarda) olur; \"Etekleri zil çalıyor\" ise \"over the moon\" (ayın üstünde). \"Get on like a house on fire\" kulağa olumsuz gelebilir ama aslında \"çok iyi anlaşmak\" demektir. Bu tür sürprizler deyimleri ezberlemek yerine bağlamda öğrenmenin önemini gösteriyor."},
    [
        mc("\"over the moon\" anlamı:", ["Çok mutlu", "Çok üzgün"], 0, "over the moon."),
        mc("\"They get on like a house on fire.\"", ["Sürekli kavga ediyorlar.", "Çok iyi anlaşıyorlar."], 1, "Olumlu."),
        mc("\"Diken üstündeydim.\"", ["I was on edge.", "I was on the moon."], 0, "on edge."),
        mc("\"I'm in two minds.\"", ["İki fikrim var, ikisi de kesin.", "Kararsızım."], 1, "in two minds."),
        gap("His loud music really gets ___ my nerves.", ["on"], "get on sb's nerves."),
        gap("We don't always see ___ to eye, but we respect each other.", ["eye"], "see eye to eye."),
        gap("She's been a bit down in the ___ since she lost her job.", ["dumps"], "down in the dumps."),
        gap("He gave me the cold ___ all evening.", ["shoulder"], "give sb the cold shoulder."),
        listen("I asked my manager a simple question, and she bit my head off! I think she's at the end of her tether with this project. Honestly, the client is a real pain in the neck. They change their minds every day.", "Müdür neden konuşana çıkıştı?", ["Konuşan hata yaptı", "Proje yüzünden sabrının sonuna gelmiş", "Hastaydı"], 1, "\"she's at the end of her tether with this project\""),
        typ("İngilizce deyimle söyleyin: \"İş teklifini alınca havalara uçtu.\" (she, over the moon)", variants("She was over the moon when she got the job offer.", "She was over the moon about the job offer.", "When she got the job offer, she was over the moon."), "She was over the moon when she got the job offer."),
    ],
    {"kind": "speaking", "task": speak("Son bir ayda yaşadığınız duygusal iniş çıkışları bir arkadaşınıza anlatıyormuş gibi anlatın. En az 6 duygu ve ilişki deyimi kullanın: over the moon, down in the dumps, on edge, in two minds, get on sb's nerves, drive sb up the wall, see eye to eye, get on like a house on fire, a pain in the neck.",
                                       "It's been a crazy month. At the beginning, I was really down in the dumps because I didn't get the promotion I wanted. Then my new flatmate moved in. At first, she drove me up the wall. She leaves her dishes everywhere, which really gets on my nerves! But we actually get on like a house on fire now. Last week, I was on edge because I had a job interview, and yesterday they offered me the position. I was over the moon! The only problem is that I'm in two minds about accepting it, because it's in another city.",
                                       ["En az 6 deyim", "Doğru bağlam", "Akıcı ve samimi anlatım"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "İkili kalıplar", "Sabit ikilileri (binomials) doğru sırayla ve bağlamda kullanabilirim.",
    {"kind": "dialogue", "title": "Taşınma kararı", "lines": [
        {"speaker": "Burak", "text": "So, have you decided whether to move to the countryside?"},
        {"speaker": "Melike", "text": "Not yet. We've been weighing up the pros and cons for weeks."},
        {"speaker": "Burak", "text": "What's the main reason for going?"},
        {"speaker": "Melike", "text": "First and foremost, peace and quiet. I'm sick and tired of the traffic and the noise."},
        {"speaker": "Burak", "text": "And the downside?"},
        {"speaker": "Melike", "text": "Well, there aren't many jobs. But by and large, I think it would be good for the kids."},
        {"speaker": "Burak", "text": "Every big change has its ups and downs. But sooner or later, you have to take the leap."},
        {"speaker": "Melike", "text": "True. And we can always come back to the city now and then."}],
     "questions": [
        mc("What is Melike's main reason for moving?", ["Jobs", "Peace and quiet", "Cheaper houses"], 1, "\"First and foremost, peace and quiet.\""),
        mc("What is the downside?", ["There aren't many jobs.", "It's too noisy.", "The kids don't want to go."], 0, "\"there aren't many jobs\""),
     ]},
    {"explanation": "**Binomials (sabit ikililer):** \"and\" ya da \"or\" ile bağlanan, **sırası sabit** iki kelime.\n\n- ✓ *pros **and** cons* / ✗ ~~cons and pros~~\n- ✓ *ups **and** downs* / ✗ ~~downs and ups~~\n\n| Binomial | Anlam | Türkçe |\n|---|---|---|\n| **pros and cons** | artıları ve eksileri | artıları eksileri |\n| **ups and downs** | iniş çıkışlar | iniş çıkışlar |\n| **sick and tired** (of) | bıkıp usanmış | bıkıp usanmak |\n| **peace and quiet** | huzur ve sessizlik | huzur |\n| **by and large** | genel olarak | genel olarak |\n| **first and foremost** | her şeyden önce | her şeyden önce |\n| **now and then / every now and again** | ara sıra | arada bir |\n| **sooner or later** | er ya da geç | er geç |\n| **give and take** | karşılıklı fedakârlık | al gülüm ver gülüm |\n| **safe and sound** | sağ salim | sağ salim |\n| **odds and ends** | ufak tefek şeyler | ıvır zıvır |\n| **trial and error** | deneme yanılma | deneme yanılma |\n| **neat and tidy** | derli toplu | derli toplu |\n| **back and forth** | ileri geri | gidip gelmek |\n| **more or less** | aşağı yukarı | aşağı yukarı |\n| **black and white** | siyah beyaz / net | net |\n| **loud and clear** | yüksek sesle ve net | gayet net |\n\n**Not:** Türkçede de çok sayıda ikili kalıp vardır (\"ıvır zıvır\", \"eğri büğrü\"). İngilizcede bunlar çoğunlukla **anlamlı iki kelime**den oluşur ve **sıra değiştirilemez**.",
     "examples": [{"en": "We learned to cook by trial and error.", "tr": "Yemek yapmayı deneme yanılmayla öğrendik."},
                  {"en": "They arrived home safe and sound.", "tr": "Eve sağ salim vardılar."},
                  {"en": "A good marriage is all about give and take.", "tr": "İyi bir evlilik karşılıklı fedakârlıkla ilgilidir."}],
     "turkishNote": "Türkçede ikilemeler çok yaygındır: \"ıvır zıvır\", \"çoluk çocuk\", \"er geç\". İngilizce binomials bunlara benzer, ama sıraları kesinlikle sabittir: \"sooner or later\" doğru, \"later or sooner\" yanlıştır. Bazı ikililer Türkçeyle birebir örtüşür (iniş çıkışlar = ups and downs, deneme yanılma = trial and error), bu da öğrenmeyi kolaylaştırır."},
    [
        mc("Doğru sıra:", ["cons and pros", "pros and cons"], 1, "pros and cons."),
        mc("Doğru sıra:", ["later or sooner", "sooner or later"], 1, "sooner or later."),
        mc("\"They got home safe and sound.\"", ["Güvenli bir sesle geldiler.", "Eve sağ salim vardılar."], 1, "safe and sound."),
        mc("\"I'm sick and tired of it.\"", ["Hastayım ve yorgunum.", "Bıktım usandım."], 1, "sick and tired."),
        gap("Every job has its ups and ___.", ["downs"], "ups and downs."),
        gap("By and ___, the holiday was a success. (genel olarak)", ["large"], "by and large."),
        gap("I just want some peace and ___.", ["quiet"], "peace and quiet."),
        gap("We learned it by trial and ___.", ["error"], "trial and error."),
        listen("Living with a partner isn't always easy. There's a lot of give and take, and of course there are ups and downs. But by and large, we're very happy. First and foremost, we respect each other.", "Konuşan ilişkisi hakkında genel olarak ne düşünüyor?", ["Mutsuz", "Genel olarak çok mutlu", "Ayrılmak istiyor"], 1, "\"by and large, we're very happy\""),
        match([("odds and", "ends"), ("back and", "forth"), ("now and", "then"), ("first and", "foremost"), ("loud and", "clear")], "İkilileri tamamlayın."),
    ],
    {"kind": "speaking", "task": speak("Hayatınızdaki büyük bir kararı (taşınmak, iş değiştirmek, yurt dışında okumak) anlatın ve artılarını eksilerini tartışın. En az 7 binomial kullanın: pros and cons, first and foremost, peace and quiet, sick and tired, by and large, ups and downs, sooner or later, give and take, trial and error, now and then.",
                                       "Last year I had to decide whether to study abroad. I spent weeks weighing up the pros and cons. First and foremost, I wanted to improve my English. I was also sick and tired of living with my parents! On the other hand, I knew I would miss my family and friends. In the end, I went to Dublin. Of course, there were ups and downs. I learned to cook by trial and error, and I felt lonely now and then. But by and large, it was the best decision of my life. Sooner or later, everyone needs to leave their comfort zone.",
                                       ["En az 7 binomial", "Doğru sıra", "Doğal bağlam"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Vücut ve benzetmeler", "Vücut parçalarıyla ve benzetmelerle kurulan deyimleri anlayabilir, Türkçe deyimlerle benzerliklerini ve tuzaklarını bilebilirim.",
    {"kind": "text", "title": "Bir köşe yazısı: \"Deyimler tercümede kaybolunca\"", "body": "When I first moved to London, idioms drove me crazy. My colleagues kept saying things that made absolutely no sense.\n\nOn my first day, my manager said, \"Can you keep an eye on the new intern?\" I wondered which eye. When I mentioned that my rent cost an arm and a leg, my flatmate laughed and agreed, but I was confused: in Turkish, we say it costs \"fire price\".\n\nThen a friend told me that she had got cold feet before her wedding. I thought she had a circulation problem!\n\nThe funniest moment came when I told a colleague that I had \"a lot on my head\", translating directly from Turkish. She looked worried and asked if I had a headache. The correct expression, I later learned, was \"a lot on my plate\".\n\nNowadays, I use idioms like a native. Well, almost. Once in a blue moon, I still make a mistake.",
     "questions": [
        mc("What did the writer think \"cold feet\" meant at first?", ["Being nervous", "A circulation problem", "Being cold"], 1, "\"I thought she had a circulation problem!\""),
        mc("What is the correct English expression for \"başım kalabalık\"?", ["a lot on my head", "a lot on my plate"], 1, "\"The correct expression... was 'a lot on my plate'.\""),
     ]},
    {"explanation": "**Vücut parçalarıyla deyimler:**\n\n| Deyim | Anlam | Türkçe |\n|---|---|---|\n| **cost an arm and a leg** | çok pahalı | ateş pahası, dudak uçuklatan |\n| **keep an eye on** | göz kulak olmak | göz kulak olmak ✓ |\n| **get cold feet** | son anda korkmak | ayakları geri geri gitmek |\n| **have a lot on your plate** | işi çok olmak | başı kalabalık olmak |\n| **pull sb's leg** | biriyle dalga geçmek, şaka yapmak | birini işletmek |\n| **be all ears** | dikkatle dinlemek | kulak kesilmek ✓ |\n| **by heart** | ezbere | ezbere ✓ |\n| **have a change of heart** | fikrini değiştirmek | fikir değiştirmek |\n| **see eye to eye** | aynı fikirde olmak | |\n| **head over heels (in love)** | sırılsıklam âşık | |\n\n**Benzetmeler (as ... as):**\n\n| Benzetme | Anlam | Türkçe |\n|---|---|---|\n| **as clear as mud** (ironik) | hiç anlaşılır değil | |\n| **as good as gold** (çocuk) | çok uslu | kuzu gibi |\n| **as fit as a fiddle** | turp gibi | turp gibi |\n| **as cool as a cucumber** | soğukkanlı | |\n| **as quiet as a mouse** | çok sessiz | |\n\n**Zaman deyimleri:** *once in a blue moon* (kırk yılda bir), *in the nick of time* (son anda), *at the drop of a hat* (hiç düşünmeden)\n\n**Tuzaklar (yanlış çeviri):**\n\n| Türkçe | ✗ Birebir | ✓ İngilizce |\n|---|---|---|\n| Başım kalabalık | a lot on my head | a lot on my plate |\n| Ateş pahası | fire price | cost an arm and a leg |\n| Kırk yılda bir | once in forty years | once in a blue moon |\n| Bardağı taşıran son damla | the last drop | the last straw |",
     "examples": [{"en": "Are you pulling my leg?", "tr": "Benimle dalga mı geçiyorsun? / Şaka mı yapıyorsun?"},
                  {"en": "He was as cool as a cucumber during the interview.", "tr": "Mülakat boyunca çok soğukkanlıydı."},
                  {"en": "We reached the station in the nick of time.", "tr": "İstasyona son anda yetiştik."}],
     "turkishNote": "Bazı İngilizce deyimler Türkçeyle tamamen örtüşür (keep an eye on = göz kulak olmak, be all ears = kulak kesilmek, by heart = ezbere). Bu deyimler kolayca öğrenilir. Ama çoğu deyimde imgeler farklıdır ve birebir çeviri karşıdakini şaşırtır: \"once in forty years\" ya da \"fire price\" bir İngiliz için anlamsızdır. Bir Türkçe deyimi İngilizceye çevirmeden önce mutlaka karşılığını kontrol edin."},
    [
        mc("\"Başım çok kalabalık.\"", ["I have a lot on my head.", "I have a lot on my plate."], 1, "a lot on my plate."),
        mc("\"Kırk yılda bir\"", ["once in forty years", "once in a blue moon"], 1, "once in a blue moon."),
        mc("\"Are you pulling my leg?\"", ["Bacağımı mı çekiyorsun?", "Şaka mı yapıyorsun?"], 1, "pull sb's leg."),
        mc("\"as clear as mud\" anlamı:", ["Çok net", "Hiç anlaşılır değil (ironik)"], 1, "İronik."),
        gap("Can you keep an ___ on my bag for a minute?", ["eye"], "keep an eye on."),
        gap("That holiday cost an ___ and a leg.", ["arm"], "cost an arm and a leg."),
        gap("He got cold ___ and didn't apply.", ["feet"], "get cold feet."),
        gap("His rude comment was the last ___. (son damla)", ["straw"], "the last straw."),
        listen("My grandfather is ninety, but he's as fit as a fiddle. He walks five kilometres every day and knows hundreds of poems by heart. Once in a blue moon, he even goes dancing!", "Büyükbaba hakkında ne söyleniyor?", ["Çok hasta", "Turp gibi sağlıklı", "Hiç yürümüyor"], 1, "\"he's as fit as a fiddle\""),
        typ("İngilizce deyimle söyleyin: \"Bu telefon ateş pahası.\" (cost an arm and a leg)", variants("This phone costs an arm and a leg.", "This phone cost an arm and a leg."), "This phone costs an arm and a leg."),
    ],
    {"kind": "speaking", "task": speak("5 Türkçe deyim seçin (başı kalabalık, ateş pahası, göz kulak olmak, kırk yılda bir, bardağı taşıran son damla, kulak kesilmek, turp gibi, vb.). Her birinin İngilizce karşılığını söyleyin, birebir çevirinin neden yanlış olacağını açıklayın ve her biriyle bir örnek cümle kurun.",
                                       "First, 'başım kalabalık'. In English, you can't say 'a lot on my head'. You say 'I've got a lot on my plate'. For example: I can't come tonight, I've got a lot on my plate. Second, 'ateş pahası' is 'cost an arm and a leg'. My new laptop cost an arm and a leg. Third, 'kırk yılda bir' is 'once in a blue moon'. I only eat fast food once in a blue moon. Fourth, 'bardağı taşıran son damla' is 'the last straw', not 'the last drop'. And finally, 'turp gibi' is 'as fit as a fiddle'. My grandmother is as fit as a fiddle.",
                                       ["Doğru İngilizce karşılıklar", "Birebir çeviri tuzağını açıklama", "Örnek cümleler"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Ölçülü ve doğal", "Deyimleri doğru üslupta ve ölçülü kullanarak samimi bir e-posta ya da hikâye yazabilir, resmî metinlerde deyimlerden kaçınabilirim.",
    {"kind": "text", "title": "İki e-posta", "body": "Email to a friend:\n\"Hi Zeynep,\nSorry I haven't been in touch. I've had so much on my plate lately! Work has been driving me up the wall: my boss keeps changing his mind, so we're always back to square one. But guess what? I finally got the job in Izmir! I'm over the moon. I start in March, so sooner or later you'll have to come and visit. By the way, how's the new flat? I hope your neighbours aren't getting on your nerves any more. Let's catch up properly soon.\nLove,\nCeren\"\n\nEmail to a manager:\n\"Dear Mr Kaplan,\nThank you for your message. I am writing to confirm that I have accepted the position in Izmir and will start on 3 March. I would like to thank you for your support over the past three years. I would be happy to help with the handover of my current projects.\nKind regards,\nCeren Aydın\"",
     "questions": [
        mc("Which email uses idioms?", ["The email to the friend", "The email to the manager", "Both"], 0, "Samimi."),
        mc("When does Ceren start her new job?", ["In January", "In March", "Next week"], 1, "\"I start in March\" / \"on 3 March\""),
     ]},
    {"explanation": "**Deyimler ne zaman uygun?**\n\n| Uygun ✓ | Dikkatli olun ⚠ | Kaçının ✗ |\n|---|---|---|\n| Arkadaşla sohbet | İş toplantısı (bazı iş deyimleri uygun) | Akademik makale |\n| Samimi e-posta / mesaj | Sunum (ölçülü) | Resmî mektup |\n| Hikâye, blog | Gazete köşe yazısı | Rapor |\n| Film, dizi | Sınav essay'i (çok az) | Hukuki metin |\n\n**Altın kurallar:**\n\n1. **Ölçülü olun:** Bir paragrafta 2–3 deyim yeterli. Fazlası **yapay ve komik** durur.\n   - ~~I was over the moon, on cloud nine, and as happy as a clam!~~\n2. **Doğru biçimi kullanın:** Deyimin kelimelerini değiştirmeyin, ama fiili çekimleyin.\n3. **Eskimiş deyimlerden kaçının:** *It's raining cats and dogs* ders kitaplarında sık geçer ama günlük dilde nadiren kullanılır.\n4. **Kendinizden emin değilseniz kullanmayın.** Yanlış kullanılan bir deyim, hiç kullanmamaktan daha kötü bir izlenim bırakır.\n5. **Dinleyicinizi düşünün:** İngilizceyi ikinci dil olarak konuşanlar (uluslararası iş ortamı) deyimleri anlamayabilir.\n\n**Deyimleri resmîleştirmek:**\n\n| Deyim (samimi) | Resmî |\n|---|---|\n| I've got a lot on my plate. | I have a very heavy workload. |\n| It cost an arm and a leg. | It was extremely expensive. |\n| We're back to square one. | We need to start the process again. |\n| I'm over the moon. | I am delighted. |\n| He gets on my nerves. | I find his behaviour frustrating. |",
     "examples": [{"en": "I've got a lot on my plate. → I have a very heavy workload.", "tr": "Başım kalabalık. → İş yüküm çok ağır."},
                  {"en": "I'm over the moon. → I am delighted.", "tr": "Havalara uçuyorum. → Çok memnunum."},
                  {"en": "We're back to square one. → We need to start the process again.", "tr": "Başa döndük. → Süreci yeniden başlatmamız gerekiyor."}],
     "turkishNote": "Türkçede de \"etekleri zil çalıyor\" gibi bir deyimi resmî bir yazışmada kullanmak tuhaf olur. İngilizcede bu ayrım daha da belirgindir. Türk öğrenciler deyimleri yeni öğrendiklerinde onları her yerde kullanma eğiliminde olabilir; bu, özellikle sınav essay'lerinde ve iş e-postalarında olumsuz bir izlenim yaratır. Deyimleri konuşmada ve samimi yazıda kullanın; resmî metinlerde düz ve net bir dil tercih edin."},
    [
        mc("Deyimler için en uygun:", ["Akademik makale", "Arkadaşa e-posta"], 1, "Samimi."),
        mc("\"I'm over the moon.\" resmî hali:", ["I am delighted.", "I am on the moon."], 0, "delighted."),
        mc("Bir paragrafta kaç deyim ideal?", ["2–3", "10 veya daha fazla"], 0, "Ölçülü."),
        mc("Resmî bir e-postada:", ["The project cost an arm and a leg.", "The project was extremely expensive."], 1, "Resmî."),
        gap("Resmî: \"I've got a lot on my plate.\" → \"I have a very heavy ___.\"", ["workload"], "heavy workload."),
        gap("Resmî: \"We're back to square one.\" → \"We need to start the process ___.\"", ["again"], "start again."),
        gap("I've had so much on my ___ lately!", ["plate"], "a lot on my plate."),
        gap("Sooner or ___, you'll have to visit me.", ["later"], "sooner or later."),
        listen("Hi, it's me! Just a quick message. I know you've got a lot on your plate, but I'm over the moon: we're having a baby! I'll call you at the weekend so we can catch up properly. Fingers crossed everything goes well!", "Mesajın tonu nasıl?", ["Resmî", "Samimi ve mutlu", "Üzgün"], 1, "Deyimler ve samimi ton."),
        typ("Resmîleştirin: \"His attitude really gets on my nerves.\"", variants("I find his attitude very frustrating.", "I find his attitude frustrating.", "His attitude is very frustrating.", "I find his attitude extremely frustrating."), "I find his attitude very frustrating."),
    ],
    {"kind": "writing", "task": write("Uzun süredir görüşmediğiniz bir arkadaşınıza samimi bir e-posta yazın (150–180 kelime). Son aylarda hayatınızda olanları anlatın (iş, okul, ilişkiler, taşınma, vb.). Bu ünitedeki deyimlerden ve binomial'lardan en az 6'sını doğal ve ölçülü bir şekilde kullanın (her paragrafta 2–3'ü geçmesin). Ardından aynı haberin bir cümlesini resmî bir e-postaya uygun şekilde yeniden yazın.",
                                      "Hi Mert,\n\nI'm so sorry I haven't been in touch for ages. I've had a lot on my plate since the summer, and the months have flown by.\n\nAs you know, I started a new job in September. The first few weeks were tough because I was still learning the ropes, and my manager was a bit of a pain in the neck. But by and large, things are going really well now. In fact, last week I was told that I'm going to lead a new project. I was over the moon!\n\nOn the personal side, there have been a few ups and downs. Ela and I moved into a new flat in Kadıköy. It's lovely, but it cost an arm and a leg to furnish. Still, we finally have some peace and quiet after living next to that noisy bar.\n\nWhat about you? Are you still thinking about moving to Berlin? Let me know when you're free so we can catch up properly. Sooner or later, you have to come and see the flat!\n\nTake care,\nDeniz\n\nFormal version: \"I am delighted to inform you that I have been asked to lead a new project.\"",
                                      ["En az 6 deyim / binomial", "Ölçülü ve doğal kullanım", "Samimi e-posta üslubu", "Resmî yeniden yazım", "Doğru biçim"])},
)

u.test([
    mc("\"Let's call it a day.\"", ["Bugünlük paydos edelim.", "Bir gün arayalım."], 0, "call it a day"),
    mc("\"Başım çok kalabalık.\"", ["I have a lot on my head.", "I have a lot on my plate."], 1, "a lot on my plate"),
    mc("\"They get on like a house on fire.\"", ["Sürekli kavga ediyorlar.", "Çok iyi anlaşıyorlar."], 1, "Olumlu"),
    mc("Doğru sıra:", ["downs and ups", "ups and downs"], 1, "ups and downs"),
    mc("Resmî bir raporda:", ["The project cost an arm and a leg.", "The project was extremely expensive."], 1, "Resmî"),
    gap("You've hit the ___ on the head.", ["nail"], "hit the nail on the head"),
    gap("Everyone needs to pull their ___.", ["weight"], "pull your weight"),
    gap("I only see my cousins once in a blue ___.", ["moon"], "once in a blue moon"),
    gap("I'm sick and ___ of this weather.", ["tired"], "sick and tired"),
    gap("Can you keep an ___ on the children?", ["eye"], "keep an eye on"),
    gap("He got cold ___ and cancelled the trip.", ["feet"], "get cold feet"),
    mc("\"Bardağı taşıran son damla\"", ["the last drop", "the last straw"], 1, "the last straw"),
    listen("The plan didn't work, so we're back to square one. Honestly, I'm at the end of my tether. But my manager was as cool as a cucumber. She just said, \"Let's get the ball rolling again tomorrow.\"", "Müdür nasıl tepki verdi?", ["Çok sinirlendi", "Çok soğukkanlıydı", "Ağladı"], 1, "\"as cool as a cucumber\""),
    typ("İngilizce deyimle söyleyin: \"Sonuçları duyunca havalara uçtum.\" (over the moon)", variants("I was over the moon when I heard the results.", "When I heard the results, I was over the moon.", "I was over the moon when I got the results."), "I was over the moon when I heard the results."),
    write("Bir blog için \"İngilizce öğrenirken yaptığım en komik hatalar\" başlıklı kısa bir yazı yazın (170–210 kelime). En az 2 Türkçe deyimi birebir çevirip yaşadığınız (gerçek ya da hayali) yanlış anlamaları anlatın ve doğru İngilizce karşılıklarını verin. Yazıda bu üniteden en az 6 deyim ve binomial'ı doğal ve ölçülü kullanın.",
          "My funniest mistakes in English\n\nLearning English has had its ups and downs, but by and large, it's been a lot of fun, especially when I've made mistakes.\n\nMy most embarrassing moment happened during my first week at an office in Manchester. My manager asked me to take on another project, and I said, \"Sorry, I have a lot on my head.\" She looked really worried and asked if I needed to see a doctor! Later, a colleague explained that the correct expression was \"a lot on my plate\".\n\nAnother time, I was telling a friend about a new phone. I wanted to say it was very expensive, so I translated the Turkish idiom and said it was \"fire price\". He just stared at me. Of course, I should have said it \"cost an arm and a leg\".\n\nI've learned most idioms by trial and error, and I still make mistakes once in a blue moon. But honestly, I don't mind. When people laugh, it breaks the ice, and I usually remember the correct expression forever.\n\nMy advice? Don't get cold feet. Use idioms, make mistakes and learn from them. Sooner or later, they'll feel natural.",
          ["En az 6 deyim / binomial", "Türkçe deyim tuzakları", "Doğal ve ölçülü kullanım", "Blog üslubu", "Akıcı anlatım"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

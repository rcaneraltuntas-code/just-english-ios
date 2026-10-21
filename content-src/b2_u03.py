"""B2 Ünite 3: Pişmanlıklar."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("B2", 3, "Pişmanlıklar", "Regrets",
         "Geçmişteki kararları ve olayları third conditional ile değerlendirebilir, şimdiki ve geçmişteki pişmanlıklarımı wish ve if only ile ifade edebilir, başkalarının davranışlarından duyduğum rahatsızlığı wish + would ile dile getirebilirim.",
         ["third conditional (if + past perfect, would have + V3)", "could have / might have ile third conditional", "wish / if only + past simple (şimdi)", "wish / if only + past perfect (geçmiş)", "wish + would (şikâyet) ve wish + could"],
         ["kararlar", "pişmanlık ve hayal kırıklığı", "dönüm noktaları"],
         {"title": "Keşke...", "durationMinutes": 45,
          "goal": "Öğrenciler hayatlarındaki bir dönüm noktasını (bir okul seçimi, bir taşınma, bir tesadüf) anlatır ve partneri If you hadn't..., would you have...? sorularıyla \"alternatif hayatı\" keşfeder. İkinci bölümde gruplar I wish... / If only... cümleleriyle küçük ve büyük pişmanlıklarını paylaşır ve birbirlerine tavsiye verir. Son olarak sınıf \"pişmanlık mı, ders mi?\" sorusunu tartışır."})

u.vocab([
    ("regret", "pişmanlık; pişman olmak", "I don't regret leaving.", "Ayrıldığıma pişman değilim.", "regret + -ing"),
    ("decision", "karar", "It was the best decision of my life.", "Hayatımın en iyi kararıydı.", "make a decision"),
    ("turning point", "dönüm noktası", "Moving abroad was a turning point.", "Yurt dışına taşınmak bir dönüm noktasıydı.", None),
    ("opportunity", "fırsat", "I missed a great opportunity.", "Harika bir fırsatı kaçırdım.", None),
    ("miss out on", "kaçırmak (fırsat)", "Don't miss out on this chance.", "Bu şansı kaçırma.", None),
    ("in hindsight", "geriye dönüp bakınca, şimdi düşününce", "In hindsight, I should have stayed.", "Şimdi düşünüyorum da kalmalıydım.", None),
    ("by chance", "tesadüfen", "We met by chance at a concert.", "Bir konserde tesadüfen tanıştık.", None),
    ("take a risk", "risk almak", "Sometimes you have to take a risk.", "Bazen risk alman gerekir.", None),
    ("play it safe", "riske girmemek", "I played it safe and stayed in my job.", "Riske girmedim ve işimde kaldım.", None),
    ("follow your heart", "kalbinin sesini dinlemek", "She followed her heart and became an artist.", "Kalbinin sesini dinleyip sanatçı oldu.", None),
    ("make a mistake", "hata yapmak", "Everyone makes mistakes.", "Herkes hata yapar.", "do a mistake ✗"),
    ("learn from", "-den ders çıkarmak", "You learn from your mistakes.", "Hatalarından ders çıkarırsın.", None),
    ("disappointed", "hayal kırıklığına uğramış", "I was disappointed with the result.", "Sonuçtan hayal kırıklığına uğradım.", None),
    ("relieved", "rahatlamış", "I'm relieved I didn't take that job.", "O işi almadığım için rahatladım.", None),
    ("ashamed", "utanmış", "I'm ashamed of what I said.", "Söylediklerimden utanıyorum.", None),
    ("if only", "keşke", "If only I had more time!", "Keşke daha fazla vaktim olsaydı!", None),
    ("wish", "keşke ... olsa / dilemek", "I wish I lived by the sea.", "Keşke deniz kenarında yaşasam.", None),
    ("would have", "-ardı / -mış olurdu", "I would have called you.", "Seni arardım.", "would've"),
    ("could have", "-ebilirdi", "We could have won.", "Kazanabilirdik.", "could've"),
    ("should have", "-meliydi", "I should have listened to you.", "Seni dinlemeliydim.", "should've"),
    ("it's too late", "artık çok geç", "It's too late to change now.", "Artık değiştirmek için çok geç.", None),
    ("look back on", "geriye dönüp bakmak", "I look back on those years with joy.", "O yıllara sevinçle bakıyorum.", None),
    ("second chance", "ikinci şans", "Everyone deserves a second chance.", "Herkes ikinci bir şansı hak eder.", None),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Olsaydı, olurdu", "Geçmişte olmayan bir durumu ve onun hayali sonucunu third conditional ile anlatabilirim.",
    {"kind": "text", "title": "Bir tesadüfün hikâyesi", "body": "Twelve years ago, Nazlı missed her train to Ankara by thirty seconds.\n\n\"I was furious,\" she remembers. \"I had an important exam the next morning. I had to wait two hours for the next train.\"\n\nWhile she was waiting, she started talking to a young man who was reading her favourite novel. His name was Tarık.\n\n\"If I hadn't missed that train, I would never have met him,\" Nazlı says. \"And if we hadn't started talking about that book, we wouldn't have discovered how much we had in common.\"\n\nToday, they are married with two children, and they run a small bookshop together. \"If the train had been on time,\" Tarık laughs, \"I'd probably have spent that evening reading alone!\"",
     "questions": [
        mc("Why was Nazlı furious at first?", ["She lost her ticket.", "She missed her train.", "She failed her exam."], 1, "\"Nazlı missed her train\""),
        mc("What were they talking about?", ["The weather", "A novel", "The exam"], 1, "\"talking about that book\""),
     ]},
    {"explanation": "**Third conditional**, geçmişte **gerçekleşmemiş** bir durumu ve onun **hayali sonucunu** anlatır. Geçmiş değiştirilemez, bu yüzden tamamen hayalidir.\n\n| If + **past perfect** | , **would have** + V3 |\n|---|---|\n| If I **hadn't missed** the train, | I **would never have met** him. |\n| If you **had studied** harder, | you **would have passed**. |\n| If it **had rained**, | we **wouldn't have gone** to the beach. |\n\n**Gerçekte ne oldu?**\n\n- If I **hadn't missed** the train ... → Gerçekte treni **kaçırdım**.\n- ... I **would never have met** him. → Gerçekte onunla **tanıştım**.\n\n**Kısaltmalar (konuşmada):**\n\n- If I**'d** known, I**'d have** told you. (**'d** = had / would)\n- would have → **would've** /ˈwʊdəv/\n\n**Soru:** What **would** you **have done** if you **had lost** your job?\n\n**Dikkat:** if kısmında would kullanılmaz: ~~If I would have known~~",
     "examples": [{"en": "If I'd known you were coming, I'd have made a cake.", "tr": "Geleceğini bilseydim pasta yapardım."},
                  {"en": "We wouldn't have got lost if we'd taken a map.", "tr": "Harita alsaydık kaybolmazdık."},
                  {"en": "What would you have done if you hadn't gone to university?", "tr": "Üniversiteye gitmeseydin ne yapardın?"}],
     "turkishNote": "Türkçede \"bilseydim ... yapardım\" yapısı hem second hem third conditional anlamına gelebilir; bağlamdan anlarız. İngilizcede geçmiş için mutlaka past perfect + would have + V3 kullanılır. \"If I knew, I would tell you\" (şu an bilmiyorum) ile \"If I had known, I would have told you\" (o zaman bilmiyordum) farklıdır. Ayrıca \"I'd\" kısaltmasının iki anlamı vardır: if kısmında had, sonuç kısmında would."},
    [
        mc("Geçmiş: \"Bilseydim sana söylerdim.\" (o zaman bilmiyordum)", ["If I knew, I'd tell you.", "If I had known, I would have told you."], 1, "Geçmiş → third conditional."),
        mc("Hangisi doğru?", ["If I would have studied, I would have passed.", "If I had studied, I would have passed."], 1, "if + past perfect."),
        mc("\"If I'd seen him, I'd have said hello.\" İlk 'd ne?", ["would", "had"], 1, "if kısmında 'd = had."),
        gap("If we ___ (leave) earlier, we would have caught the train.", ["had left", "'d left"], "if + past perfect."),
        gap("She ___ (not / get) the job if she hadn't spoken English.", ["wouldn't have got", "would not have got", "wouldn't have gotten", "would not have gotten"], "wouldn't have + V3."),
        gap("What would you have done if you ___ (lose) your passport?", ["had lost", "'d lost"], "past perfect."),
        gap("If it hadn't rained, we would ___ (go) to the beach.", ["have gone"], "would have + V3."),
        order(["hadn't", "If", "I", "missed", "the", "train", "I", "wouldn't", "have", "met", "him"], "If I hadn't missed the train I wouldn't have met him.", "If + past perfect, would have + V3.", "Treni kaçırmasaydım onunla tanışmazdım."),
        listen("If I hadn't broken my leg when I was sixteen, I would have become a professional footballer. But in hospital I read a book about medicine, and now I'm a doctor.", "Konuşan neden profesyonel futbolcu olmadı?", ["Ailesi istemedi", "On altı yaşında bacağını kırdı", "Yetenekli değildi"], 1, "\"If I hadn't broken my leg when I was sixteen\""),
        typ("İngilizce yazın: \"Geleceğini bilseydim pasta yapardım.\"", variants("If I'd known you were coming, I'd have made a cake.", "If I had known you were coming, I would have made a cake.", "If I had known you were coming, I'd have made a cake.", "If I'd known you were coming, I would have made a cake.", "I'd have made a cake if I'd known you were coming.", "I would have made a cake if I had known you were coming.", "If I'd known that you were coming, I'd have made a cake.", "If I had known that you were coming, I would have made a cake."), "If I'd known you were coming, I'd have made a cake."),
    ],
    {"kind": "speaking", "task": speak("Hayatınızdaki bir dönüm noktasını anlatın (bir okul ya da iş seçimi, bir taşınma, bir tesadüf). Sonra \"alternatif hayatınızı\" en az 4 third conditional cümlesiyle hayal edin: Eğer o olmasaydı ne olurdu?",
                                       "In 2015, I chose to study engineering instead of music. If I had studied music, I would have moved to Istanbul. I wouldn't have met my wife, because we met at the engineering faculty. If I hadn't become an engineer, I wouldn't have got my job in Germany. But maybe I would have become a famous pianist!",
                                       ["if + past perfect", "would have + V3", "Mantıklı zincir", "Kısaltmalar doğru"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "Olabilirdi, yapabilirdik", "Third conditional'da could have ve might have kullanarak geçmişteki olasılıkları ve kaçırılan fırsatları anlatabilirim.",
    {"kind": "dialogue", "title": "Kaybedilen maç", "lines": [
        {"speaker": "Coach", "text": "That was so close. If we'd scored that penalty, we might have won the cup."},
        {"speaker": "Player", "text": "I know. It's my fault. If I hadn't been so nervous, I could have scored easily."},
        {"speaker": "Coach", "text": "Don't blame yourself. If the referee hadn't given them that free kick, we wouldn't have needed the penalty."},
        {"speaker": "Player", "text": "True. And if Burak hadn't been injured, we could have played a different system."},
        {"speaker": "Coach", "text": "Exactly. We can't change the past. Let's learn from it."},
        {"speaker": "Player", "text": "You're right. Next year we'll be ready."}],
     "questions": [
        mc("What might have happened if they had scored the penalty?", ["They might have lost.", "They might have won the cup.", "The match would have finished earlier."], 1, "\"we might have won the cup\""),
        mc("Why couldn't they play a different system?", ["The coach didn't want to.", "Burak was injured.", "It was raining."], 1, "\"if Burak hadn't been injured\""),
     ]},
    {"explanation": "Third conditional'ın sonuç kısmında would have yerine **could have** ya da **might have** kullanılabilir:\n\n| Modal | Anlam | Örnek |\n|---|---|---|\n| **would have** + V3 | kesin hayali sonuç | If we'd scored, we **would have won**. |\n| **might have** + V3 | olası sonuç (belki) | If we'd scored, we **might have won**. |\n| **could have** + V3 | yetenek / olanak | If I'd been calm, I **could have scored**. |\n\n**Olumsuz:**\n\n- **wouldn't have** = olmazdı\n- **might not have** = olmayabilirdi\n- **couldn't have** = olamazdı / yapamazdım\n\n**Tek başına could have / might have:** Koşul cümlesi olmadan da kaçırılan fırsatları ya da tehlikeleri anlatır:\n\n- You **could have** told me! (Bana söyleyebilirdin! → Söylemedin, kızgınım.)\n- Be careful! You **might have** hurt yourself. (Kendine zarar verebilirdin.)\n\n**if'siz third conditional (konuşmada):**\n\n- **Without** your help, I **wouldn't have** finished. (= If you hadn't helped me ...)\n- **But for** the rain, we'd have gone. (resmî)",
     "examples": [{"en": "If I'd left five minutes earlier, I might have caught the bus.", "tr": "Beş dakika erken çıksaydım otobüsü yakalayabilirdim belki."},
                  {"en": "You could have called me! I was worried.", "tr": "Beni arayabilirdin! Endişelendim."},
                  {"en": "Without your advice, I would have made a terrible mistake.", "tr": "Tavsiyen olmasaydı korkunç bir hata yapardım."}],
     "turkishNote": "\"-ebilirdi\" (yapabilirdim, kazanabilirdik) Türkçede hem olanak hem olasılık anlatır. İngilizcede olanak için could have, belirsiz olasılık için might have tercih edilir. \"You could have told me!\" cümlesi Türkçedeki sitemli \"Söyleyebilirdin ama!\" tonunu taşır."},
    [
        mc("Belki: \"If we'd left earlier, we ___ the flight.\"", ["would have caught", "might have caught"], 1, "Belirsiz → might have."),
        mc("Yetenek / olanak: \"If I'd had a car, I ___ you a lift.\"", ["could have given", "might give"], 0, "Olanak → could have."),
        mc("Sitem: \"Bana söyleyebilirdin!\"", ["You can tell me!", "You could have told me!"], 1, "could have + V3."),
        gap("If she'd trained harder, she ___ (might / win) the race.", ["might have won"], "might have + V3."),
        gap("If I'd had more money, I ___ (could / buy) that house.", ["could have bought"], "could have + V3."),
        gap("___ your help, I wouldn't have passed. (yardımın olmasaydı)", ["Without"], "Without."),
        gap("Be careful! You ___ have fallen! (düşebilirdin)", ["might", "could"], "might / could have."),
        gap("If they hadn't been late, they ___ (not / miss) the start.", ["wouldn't have missed", "would not have missed"], "wouldn't have + V3."),
        listen("I didn't apply for the job in Barcelona because I thought I wasn't good enough. If I'd applied, I might have got it. I could have moved to Spain!", "Konuşan neden başvurmadı?", ["İspanyolca bilmiyordu", "Yeterince iyi olmadığını düşündü", "Ailesi istemedi"], 1, "\"I thought I wasn't good enough\""),
        typ("İngilizce yazın: \"Tavsiyen olmasaydı korkunç bir hata yapardım.\"", variants("Without your advice, I would have made a terrible mistake.", "Without your advice, I'd have made a terrible mistake.", "If it hadn't been for your advice, I would have made a terrible mistake.", "I would have made a terrible mistake without your advice.", "Without your advice I would have made a terrible mistake.", "If you hadn't advised me, I would have made a terrible mistake."), "Without your advice, I would have made a terrible mistake."),
    ],
    {"kind": "speaking", "task": speak("Kaçırdığınız bir fırsatı ya da kıl payı atlattığınız bir tehlikeyi anlatın. would have, might have ve could have'i en az birer kez kullanın ve bir \"without\" cümlesi ekleyin.",
                                       "Two years ago, I was offered a place on a photography course in Florence, but I said no because it was expensive. If I'd gone, I might have become a professional photographer. I could have learned Italian too. On the other hand, if I'd spent all my savings, I wouldn't have been able to buy my car. And without that car, I wouldn't have got my current job.",
                                       ["would / might / could have doğru", "Without + isim", "Anlam farkı bilinçli"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "Keşke şimdi...", "wish ve if only ile şimdiki durumlardan duyduğum pişmanlığı ve özlemi ifade edebilirim.",
    {"kind": "text", "title": "Sosyal medyada bir paylaşım", "body": "Monday morning thoughts...\n\nI wish I didn't have to go to work today. I wish I lived by the sea and could swim every morning instead of sitting in traffic for an hour.\n\nIf only I had more free time! I wish I knew how to play the guitar, and I wish I could speak Italian.\n\nBut then I look at my daughter, who's still asleep, and I think: I wish she weren't growing up so fast.\n\nOK, enough dreaming. Coffee time! #mondaymood",
     "questions": [
        mc("Where does the writer wish they lived?", ["In the city", "By the sea", "In Italy"], 1, "\"I wish I lived by the sea\""),
        mc("What does the writer wish about their daughter?", ["That she was older", "That she weren't growing up so fast", "That she could speak Italian"], 1, "\"I wish she weren't growing up so fast\""),
     ]},
    {"explanation": "**wish / if only + past simple** → **şu anki** bir durumun farklı olmasını isteriz (\"keşke ... olsa\").\n\n| Gerçek (şimdi) | Dilek |\n|---|---|\n| I **have** to go to work. | I wish I **didn't have** to go to work. |\n| I **don't live** by the sea. | I wish I **lived** by the sea. |\n| I **can't** speak Italian. | I wish I **could** speak Italian. |\n| She **is** growing up so fast. | I wish she **weren't** growing up so fast. |\n\nZaman **bir adım geriye** gider: present → past, can → could, is -ing → was/were -ing.\n\n**be fiili:** Resmî dilde tüm kişilerde **were**: I wish I **were** taller. (Günlük dilde **was** da kullanılır.)\n\n**if only** = wish'in daha **güçlü, duygusal** hali:\n\n- **If only** I had more time! (Keşke daha fazla vaktim olsaydı!)\n\n**Dikkat:** Gelecekte gerçekçi olarak olmasını istediğimiz şeyler için **hope** kullanılır:\n\n- I **hope** it **stops** raining. (Olabilir.) ≠ I **wish** it **wasn't** raining. (Şu an yağıyor.)",
     "examples": [{"en": "I wish I had a bigger flat.", "tr": "Keşke daha büyük bir dairem olsa."},
                  {"en": "If only I could sing!", "tr": "Keşke şarkı söyleyebilsem!"},
                  {"en": "I wish it weren't so cold today.", "tr": "Keşke bugün bu kadar soğuk olmasa."}],
     "turkishNote": "Türkçedeki \"keşke\" kelimesinden sonra genellikle \"-sa / -saydı\" eki gelir. İngilizcede şimdiki durumlar için wish + past simple kullanılır; fiil geçmiş zamanda olsa da anlam şimdiyi anlatır. \"I wish I have more money\" yanlıştır; doğrusu \"I wish I had more money\"."},
    [
        mc("\"Keşke daha fazla param olsa.\"", ["I wish I have more money.", "I wish I had more money."], 1, "wish + past simple."),
        mc("\"Keşke yüzebilsem.\"", ["I wish I can swim.", "I wish I could swim."], 1, "can → could."),
        mc("Gerçekçi gelecek isteği:", ["I wish you pass your exam.", "I hope you pass your exam."], 1, "Gerçekçi → hope."),
        mc("Resmî: \"I wish I ___ taller.\"", ["am", "were"], 1, "were."),
        gap("I wish I ___ (live) closer to my parents.", ["lived"], "wish + past."),
        gap("I wish I ___ (not / have) so much work.", ["didn't have", "did not have"], "Olumsuz."),
        gap("If ___ I knew the answer! (keşke)", ["only"], "If only."),
        gap("I wish it ___ (not / rain) right now.", ["wasn't raining", "weren't raining"], "is raining → was/were raining."),
        listen("I wish I could take a holiday, but we're so busy at work. If only I didn't have this huge project!", "Konuşan neden tatile çıkamıyor?", ["Parası yok", "İşte büyük bir proje var", "Hasta"], 1, "\"If only I didn't have this huge project!\""),
        typ("İngilizce yazın: \"Keşke İtalyanca konuşabilsem.\"", variants("I wish I could speak Italian.", "If only I could speak Italian.", "I wish I spoke Italian.", "If only I spoke Italian."), "I wish I could speak Italian."),
    ],
    {"kind": "speaking", "task": speak("Hayatınızda şu an farklı olmasını istediğiniz 6 şeyi wish ve if only ile söyleyin (ev, iş, yetenekler, hava, alışkanlıklar). En az birinde could, birinde were, birinde olumsuz yapı kullanın. Sonra gerçekçi bir umudunuzu hope ile ekleyin.",
                                       "I wish I had a garden. I wish I could play the piano. I wish my job weren't so stressful. I wish I didn't spend so much time on my phone. If only I lived nearer the city centre! I wish it were summer already. But I hope I'll find a better flat next year.",
                                       ["wish + past simple", "could / were / olumsuz", "wish ve hope farkı"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Keşke yapmasaydım", "wish / if only + past perfect ile geçmişteki pişmanlıkları, wish + would ile başkalarının davranışlarına duyduğum rahatsızlığı ifade edebilirim.",
    {"kind": "dialogue", "title": "Kötü bir tatil", "lines": [
        {"speaker": "Mehmet", "text": "I wish I'd never booked that hotel. It was a disaster."},
        {"speaker": "Selin", "text": "What happened?"},
        {"speaker": "Mehmet", "text": "The room was tiny and dirty. If only I'd read the reviews first! And the people next door had parties every night."},
        {"speaker": "Selin", "text": "Oh no. Did you complain?"},
        {"speaker": "Mehmet", "text": "Every day! But nothing changed. And my brother kept playing loud music in our room. I wish he would listen to me sometimes."},
        {"speaker": "Selin", "text": "Next time, you should check everything before you book."}],
     "questions": [
        mc("What does Mehmet wish he had done?", ["Booked a bigger room", "Read the reviews first", "Stayed at home"], 1, "\"If only I'd read the reviews first!\""),
        mc("What does Mehmet complain about his brother?", ["He doesn't listen to him.", "He's always late.", "He spends too much money."], 0, "\"I wish he would listen to me sometimes.\""),
     ]},
    {"explanation": "**1. wish / if only + past perfect** → **geçmişteki** bir pişmanlık (\"keşke ... yapsaydım / yapmasaydım\")\n\n| Gerçek (geçmiş) | Pişmanlık |\n|---|---|\n| I **booked** that hotel. | I wish I **hadn't booked** that hotel. |\n| I **didn't read** the reviews. | If only I **had read** the reviews! |\n| I **said** something stupid. | I wish I **hadn't said** that. |\n\n**should have** ile benzer anlam:\n\n- I wish I **had studied** more. ≈ I **should have studied** more.\n\n**2. wish + would** → başkasının (ya da bir durumun) **sürekli davranışından şikâyet** ve değişmesini istemek\n\n- I wish my brother **would** listen to me. (Hiç dinlemiyor, sinir oluyorum.)\n- I wish it **would** stop raining! (Durmuyor!)\n- I wish you **wouldn't** leave your clothes on the floor.\n\n**Dikkat:** Kendimiz için wish + would kullanılmaz: ~~I wish I would~~ → I wish I **could** ...\n\n**Özet:**\n\n| Yapı | Zaman | Anlam |\n|---|---|---|\n| wish + past simple | şimdi | Keşke ... olsa |\n| wish + past perfect | geçmiş | Keşke ... olsaydı |\n| wish + would | başkasının davranışı | Keşke ... yapsa (şikâyet) |\n| wish + could | yetenek | Keşke ... yapabilsem |",
     "examples": [{"en": "I wish I hadn't eaten so much.", "tr": "Keşke bu kadar çok yemeseydim."},
                  {"en": "If only we had left earlier!", "tr": "Keşke daha erken çıksaydık!"},
                  {"en": "I wish you wouldn't interrupt me all the time.", "tr": "Keşke sürekli sözümü kesmesen."}],
     "turkishNote": "Türkçede \"Keşke o oteli ayırtmasaydım\" ve \"Keşke beni dinlese\" cümleleri aynı \"keşke\" ile kurulur. İngilizcede ilki wish + past perfect (geçmiş pişmanlık), ikincisi wish + would (başkasından şikâyet) ile ifade edilir. wish + would genellikle bir sitem tonu taşır."},
    [
        mc("Geçmiş pişmanlık: \"Keşke o kadar çok yemeseydim.\"", ["I wish I didn't eat so much.", "I wish I hadn't eaten so much."], 1, "Geçmiş → past perfect."),
        mc("Şikâyet: \"Keşke sürekli sözümü kesmese.\"", ["I wish he wouldn't interrupt me all the time.", "I wish he hadn't interrupt me."], 0, "Başkasının davranışı → would."),
        mc("Hangisi yanlış?", ["I wish I would be taller.", "I wish I were taller."], 0, "Kendimiz için wish + would olmaz."),
        mc("\"I wish I had studied more.\" ≈", ["I should have studied more.", "I should study more."], 0, "Geçmiş pişmanlık."),
        gap("I wish I ___ (not / say) that to her.", ["hadn't said", "had not said"], "wish + past perfect."),
        gap("If only I ___ (listen) to your advice!", ["had listened", "'d listened"], "if only + past perfect."),
        gap("I wish the neighbours ___ stop making so much noise. (şikâyet)", ["would"], "wish + would."),
        gap("I wish you ___ leave your dirty dishes in the sink! (olumsuz şikâyet)", ["wouldn't", "would not"], "wish + wouldn't."),
        listen("I wish I'd learned to drive when I was younger. Now I'm forty and I have to ask my husband to take me everywhere. And I wish he wouldn't complain about it every time!", "Konuşanın kocası hakkında şikâyeti ne?", ["Hiç yardım etmiyor", "Her seferinde şikâyet ediyor", "Çok hızlı sürüyor"], 1, "\"I wish he wouldn't complain about it every time!\""),
        typ("İngilizce yazın: \"Keşke daha erken çıksaydık!\"", variants("If only we had left earlier!", "If only we'd left earlier!", "I wish we had left earlier!", "I wish we'd left earlier!", "If only we had left earlier.", "I wish we had left earlier."), "If only we had left earlier!"),
    ],
    {"kind": "speaking", "task": speak("Önce geçmişteki 3 pişmanlığınızı wish / if only + past perfect ile söyleyin ve her birinin sonucunu third conditional ile açıklayın. Sonra çevrenizdeki insanların ya da durumların sizi rahatsız eden 3 davranışını wish + would ile söyleyin.",
                                       "I wish I'd studied abroad. If I had, my English would have improved faster. If only I hadn't sold my old guitar! I wish I'd spent more time with my grandmother. ... I wish my colleague would stop talking on the phone so loudly. I wish it would stop raining. I wish people wouldn't drop rubbish in the park.",
                                       ["wish + past perfect", "Third conditional ile sonuç", "wish + would (şikâyet)"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Pişmanlık mı, ders mi?", "Geçmiş kararları dengeli bir şekilde değerlendirebilir, pişmanlıkları ve çıkarılan dersleri bir yazıda bir araya getirebilirim.",
    {"kind": "text", "title": "Röportaj: \"Pişman değilim\"", "body": "At 45, Gökhan Demir left his job as a bank manager to become a farmer. We asked him about the decision.\n\n\"People ask me if I regret it. Honestly? Sometimes. In the first year, I made every mistake possible. If I'd done a course in agriculture first, I wouldn't have lost so much money. I wish I'd been more patient.\n\nBut in hindsight, I'm glad I took the risk. If I had played it safe, I would have spent the rest of my life wondering 'what if?'\n\nMy advice? Don't spend your life wishing things were different. Learn from your mistakes, and don't be afraid of second chances. The only real regret is the chance you never took.\"",
     "questions": [
        mc("What does Gökhan wish he had done?", ["Stayed at the bank", "Been more patient", "Moved to the city"], 1, "\"I wish I'd been more patient.\""),
        mc("What would have happened if he had played it safe?", ["He would have become rich.", "He would have spent his life wondering 'what if?'", "He would have become a farmer anyway."], 1, "\"I would have spent the rest of my life wondering 'what if?'\""),
     ]},
    {"explanation": "**Geçmiş kararları değerlendirmek için kalıplar:**\n\n| Duygu | Kalıp |\n|---|---|\n| **Pişmanlık** | I **regret** + -ing / I **wish I'd** ... / I **should have** ... |\n| **Memnuniyet** | I'm **glad** I + past simple / I **don't regret** + -ing / It was **the best decision** ... |\n| **Rahatlama** | I'm **relieved** I didn't ... / **Thank goodness** I ... |\n| **Ders** | I've **learned** that ... / **In hindsight**, ... / **Looking back**, ... |\n| **Kabullenme** | **It's too late now.** / **There's no point in** + -ing / **What's done is done.** |\n\n**regret + -ing:**\n\n- I **regret leaving** school early. (Okulu erken bıraktığım için pişmanım.)\n- I **don't regret taking** the risk.\n\n**Dengeli bir değerlendirme yazısı:**\n\n1. **Kararı tanıtın**: Ne oldu, ne zaman?\n2. **Olumsuz tarafı**: wish / third conditional\n3. **Olumlu tarafı**: I'm glad ... / If I hadn't ..., I wouldn't have ...\n4. **Ders ve sonuç**: In hindsight / I've learned that ...",
     "examples": [{"en": "I regret not travelling more when I was young.", "tr": "Gençken daha fazla seyahat etmediğim için pişmanım."},
                  {"en": "I'm glad I didn't accept that offer.", "tr": "O teklifi kabul etmediğime sevindim."},
                  {"en": "There's no point in worrying about it now.", "tr": "Şimdi bunun için endişelenmenin anlamı yok."}],
     "turkishNote": "\"Pişmanım\" için \"I'm regret\" demek yaygın bir hatadır; regret bir fiildir: I regret it. \"... yapmadığım için pişmanım\" ise \"I regret not doing ...\" olur. \"There's no point in\" kalıbından sonra -ing gelir: There's no point in crying."},
    [
        mc("Hangisi doğru?", ["I'm regret leaving.", "I regret leaving."], 1, "regret bir fiil."),
        mc("\"Daha fazla seyahat etmediğim için pişmanım.\"", ["I regret not travelling more.", "I regret to not travel more."], 0, "regret not + -ing."),
        mc("Memnuniyet:", ["I'm glad I took the job.", "I wish I took the job."], 0, "I'm glad + past simple."),
        gap("There's no point ___ worrying about it now.", ["in"], "There's no point in."),
        gap("In ___, it was the right decision. (geriye dönüp bakınca)", ["hindsight"], "In hindsight."),
        gap("I don't regret ___ (take) the risk.", ["taking"], "regret + -ing."),
        gap("I'm ___ I didn't buy that car. It broke down a month later. (rahatladım)", ["relieved", "glad"], "relieved."),
        gap("If I'd ___ (play) it safe, I would never have started my own business.", ["played"], "past perfect."),
        listen("I regret not learning my grandmother's language. When she was alive, I was too busy. If I'd spent more time with her, I could have learned so much. It's too late now, but I'm teaching my children instead.", "Konuşan şimdi ne yapıyor?", ["Büyükannesinin dilini öğreniyor", "Çocuklarına bu dili öğretiyor", "Büyükannesini ziyaret ediyor"], 1, "\"I'm teaching my children instead\""),
        typ("İngilizce yazın: \"O teklifi kabul etmediğime sevindim.\"", variants("I'm glad I didn't accept that offer.", "I am glad I didn't accept that offer.", "I'm glad that I didn't accept that offer.", "I'm glad I did not accept that offer.", "I'm glad I didn't accept the offer.", "I'm happy I didn't accept that offer."), "I'm glad I didn't accept that offer."),
    ],
    {"kind": "writing", "task": write("Hayatınızda verdiğiniz önemli bir kararı (ya da vermediğiniz bir kararı) değerlendiren bir blog yazısı yazın (180–220 kelime). Kararı tanıtın; olumsuz tarafını wish / if only ve third conditional ile, olumlu tarafını I'm glad / I don't regret ile anlatın; sonunda in hindsight / I've learned that ile bir ders çıkarın.",
                                      "The Year I Said No\n\nFive years ago, I was offered a job in London. The salary was double what I was earning in Izmir, and it was a big international company. After a week of thinking, I said no.\n\nAt first, I regretted it terribly. I wish I had been braver. If I had accepted, my English would have improved much faster, and I might have climbed the career ladder more quickly. Every time I saw my friends' photos from abroad, I thought: that could have been me.\n\nBut in hindsight, I'm glad I stayed. Six months later, my father became seriously ill. If I had been in London, I couldn't have looked after him, and I would never have forgiven myself. I also wouldn't have met my wife, who joined my company that year.\n\nI don't regret my decision any more. I've learned that there's no point in comparing your life with an imaginary one. Every choice has a cost, and the \"perfect\" path doesn't exist. What matters is that you make your decisions honestly, and then make the best of them.",
                                      ["Third conditional", "wish / if only + past perfect", "I'm glad / I don't regret / regret + -ing", "Dengeli değerlendirme", "Düzenli ve akıcı yazı"])},
)

u.test([
    mc("Hangisi doğru?", ["If I would have known, I would have told you.", "If I had known, I would have told you."], 1, "Third conditional"),
    mc("If we had left earlier, we ___ the train.", ["would catch", "would have caught"], 1, "would have + V3"),
    mc("Belki: \"If she'd asked, he ___ yes.\"", ["might have said", "will say"], 0, "might have"),
    mc("\"Keşke daha fazla param olsa.\" (şimdi)", ["I wish I had more money.", "I wish I had had more money."], 0, "wish + past simple"),
    mc("\"Keşke ona söylemeseydim.\" (geçmiş)", ["I wish I didn't tell her.", "I wish I hadn't told her."], 1, "wish + past perfect"),
    mc("Şikâyet: \"I wish my neighbour ___ his dog bark all night.\"", ["wouldn't let", "doesn't let"], 0, "wish + would"),
    mc("Gerçekçi istek:", ["I wish you feel better soon.", "I hope you feel better soon."], 1, "hope"),
    gap("If I ___ (not / miss) the bus, I wouldn't have met her.", ["hadn't missed", "had not missed"], "if + past perfect"),
    gap("I wish I ___ (can) speak Japanese.", ["could"], "wish + could"),
    gap("If ___ I had listened to you!", ["only"], "If only"),
    gap("You ___ have told me! I was so worried. (söyleyebilirdin)", ["could"], "could have"),
    gap("I don't regret ___ (move) to Izmir.", ["moving"], "regret + -ing"),
    listen("If I hadn't taken that wrong turn, we would have arrived on time. But then we wouldn't have found that amazing little restaurant in the mountains!", "Yanlış yola sapmanın olumlu sonucu ne oldu?", ["Daha erken vardılar", "Dağda harika bir restoran buldular", "Eski bir arkadaşla karşılaştılar"], 1, "\"we wouldn't have found that amazing little restaurant\""),
    typ("İngilizce yazın: \"Keşke daha sabırlı olsaydım.\" (geçmiş)", variants("I wish I had been more patient.", "I wish I'd been more patient.", "If only I had been more patient.", "If only I'd been more patient."), "I wish I had been more patient."),
    write("\"Hayatımı değiştiren bir an\" başlıklı bir yazı yazın (160–200 kelime). O anı kısaca anlatın; o an olmasaydı neler farklı olurdu (third conditional: would / might / could have); bugün o anla ilgili neler hissettiğinizi wish, if only, I'm glad ve regret ile ifade edin.",
          "The moment that changed my life was a phone call from my aunt when I was nineteen. She asked if I wanted to help in her small hotel in Kaş for the summer. I almost said no, because I'd planned to work in my father's shop in Ankara.\n\nIf I hadn't said yes, I would never have discovered how much I love the sea and meeting people from all over the world. I wouldn't have learned English so quickly, and I might never have studied tourism. I certainly wouldn't have met my best friend, Lena, who was staying at the hotel with her family.\n\nOf course, there are things I wish I'd done differently. I wish I had spent more time with my father during those years, because he needed help in the shop. If only I had understood that then!\n\nBut overall, I'm glad I took the chance. I don't regret leaving Ankara at all. Today, I run my own guesthouse, and every summer I think about that phone call and smile.",
          ["Third conditional (would / might / could have)", "wish / if only", "I'm glad / regret + -ing", "Duygusal derinlik", "Düzenli ve akıcı yazı"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

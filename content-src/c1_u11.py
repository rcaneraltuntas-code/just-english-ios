"""C1 Ünite 11: Kelime türetme."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("C1", 11, "Kelime türetme", "Word Formation",
         "Önek ve sonekleri tanıyarak bilmediğim kelimelerin anlamını tahmin edebilir, bir kelimenin isim, fiil, sıfat ve zarf hallerini doğru türetebilir, olumsuz önekleri doğru seçebilir ve sınav tipi kelime türetme sorularını çözebilirim.",
         ["isim yapan sonekler: -tion, -ment, -ness, -ity, -ance, -ship, -hood", "sıfat yapan sonekler: -able, -ful, -less, -ous, -ive, -al", "olumsuz önekler: un-, in-, im-, il-, ir-, dis-, mis-, non-", "anlam önekleri ve fiil yapma: over-, under-, re-, co-, -ise, -en, en-", "kelime aileleri ve sınav stratejisi"],
         ["dil öğrenme stratejileri", "iş dünyası", "sınavlar"],
         {"title": "Kelime fabrikası", "durationMinutes": 45,
          "goal": "Gruplara kök kelimeler (act, rely, child, able, deep, power) dağıtılır. Her grup bir kelime ağacı kurar: isim, fiil, sıfat, zarf ve olumsuz halleri. Sonra gruplar birbirlerine sınav tipi kelime türetme soruları hazırlayıp yarışır. Son bölümde her öğrenci ağacındaki en az beş kelimeyi kullanarak kısa bir konuşma yapar."})

u.vocab([
    ("prefix", "önek", "\"Un-\" is a common negative prefix.", "\"Un-\" yaygın bir olumsuzluk önekidir.", None),
    ("suffix", "sonek", "\"-ness\" is a suffix that forms nouns.", "\"-ness\" isim yapan bir sonektir.", None),
    ("root / stem", "kök", "The root of \"unhappiness\" is \"happy\".", "\"Unhappiness\" kelimesinin kökü \"happy\"dir.", None),
    ("word family", "kelime ailesi", "\"Decide, decision, decisive\" belong to the same word family.", "\"Decide, decision, decisive\" aynı kelime ailesine aittir.", None),
    ("reliable", "güvenilir", "She's a very reliable colleague.", "O çok güvenilir bir iş arkadaşı.", None),
    ("reliability", "güvenilirlik", "The reliability of the data is uncertain.", "Verilerin güvenilirliği belirsiz.", None),
    ("childhood", "çocukluk", "I had a happy childhood.", "Mutlu bir çocukluğum oldu.", None),
    ("leadership", "liderlik", "The team needs strong leadership.", "Ekibin güçlü bir liderliğe ihtiyacı var.", None),
    ("awareness", "farkındalık", "The campaign raised awareness of the problem.", "Kampanya soruna dair farkındalığı artırdı.", None),
    ("effectiveness", "etkililik", "We measured the effectiveness of the new method.", "Yeni yöntemin etkililiğini ölçtük.", None),
    ("irrelevant", "alakasız", "That question is irrelevant.", "O soru alakasız.", None),
    ("illegal", "yasa dışı", "Parking here is illegal.", "Buraya park etmek yasa dışı.", None),
    ("impatient", "sabırsız", "Don't be so impatient!", "Bu kadar sabırsız olma!", None),
    ("misunderstand", "yanlış anlamak", "I think you misunderstood me.", "Sanırım beni yanlış anladın.", None),
    ("disagree", "katılmamak", "I completely disagree.", "Hiç katılmıyorum.", None),
    ("non-profit", "kâr amacı gütmeyen", "She works for a non-profit organisation.", "Kâr amacı gütmeyen bir kuruluşta çalışıyor.", None),
    ("overestimate", "olduğundan fazla tahmin etmek", "We overestimated how many people would come.", "Kaç kişinin geleceğini fazla tahmin ettik.", None),
    ("underpaid", "düşük ücretli", "Many nurses feel underpaid.", "Birçok hemşire düşük ücret aldığını düşünüyor.", None),
    ("rewrite", "yeniden yazmak", "I had to rewrite the whole report.", "Bütün raporu yeniden yazmak zorunda kaldım.", None),
    ("strengthen", "güçlendirmek", "Exercise strengthens your muscles.", "Egzersiz kaslarınızı güçlendirir.", None),
    ("modernise", "modernleştirmek", "The government plans to modernise the railways.", "Hükümet demiryollarını modernleştirmeyi planlıyor.", None),
    ("enable", "mümkün kılmak", "The app enables users to learn offline.", "Uygulama kullanıcıların çevrimdışı öğrenmesini mümkün kılar.", None),
    ("outnumber", "sayıca üstün olmak", "Women outnumber men in this profession.", "Bu meslekte kadınlar erkeklerden sayıca fazla.", None),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "İsim yapan sonekler", "Fiil ve sıfatlardan isim türeten sonekleri (-tion, -ment, -ness, -ity, -ance / -ence, -ship, -hood) tanıyıp doğru kullanabilirim.",
    {"kind": "text", "title": "Kelime avcısı", "body": "When Leyla started learning English, she wrote every new word on a separate card. After a while, she noticed a pattern. Many long words were simply short words with an ending added: \"happy\" became \"happiness\", \"develop\" became \"development\", \"able\" became \"ability\". This discovery changed her whole approach. Instead of learning one word at a time, she started learning whole families of words. Her vocabulary grew much faster, and her confidence in reading improved enormously. Today, she teaches this method to her own students. \"Recognition comes first,\" she says. \"Once you can see the parts of a word, you can often guess its meaning.\"",
     "questions": [
        mc("What did Leyla notice?", ["Most English words are short.", "Many long words are short words with endings.", "Cards are not useful."], 1, "\"Many long words were simply short words with an ending added\""),
        mc("What is Leyla's job today?", ["She is a student.", "She is a teacher.", "She is a writer."], 1, "\"she teaches this method to her own students\""),
     ]},
    {"explanation": "**Fiilden isim yapan sonekler:**\n\n| Sonek | Örnekler |\n|---|---|\n| **-tion / -sion / -ation** | decide → deci**sion**, inform → inform**ation**, recognise → recogni**tion** |\n| **-ment** | develop → develop**ment**, agree → agree**ment**, achieve → achieve**ment** |\n| **-ance / -ence** | perform → perform**ance**, depend → depend**ence**, exist → exist**ence** |\n| **-al** | arrive → arriv**al**, refuse → refus**al**, approve → approv**al** |\n| **-er / -or / -ant / -ee** (kişi) | teach**er**, edit**or**, assist**ant**, employ**ee** |\n\n**Sıfattan isim yapan sonekler:**\n\n| Sonek | Örnekler |\n|---|---|\n| **-ness** | happy → happi**ness**, aware → aware**ness**, kind → kind**ness** |\n| **-ity** | able → abil**ity**, possible → possibil**ity**, reliable → reliabil**ity** |\n| **-ance / -ence** | important → import**ance**, confident → confid**ence**, patient → pati**ence** |\n| **-th** | strong → streng**th**, deep → dep**th**, wide → wid**th**, long → leng**th** |\n\n**İsimden soyut isim yapan sonekler:**\n\n| Sonek | Örnekler |\n|---|---|\n| **-ship** | friend → friend**ship**, leader → leader**ship**, member → member**ship** |\n| **-hood** | child → child**hood**, neighbour → neighbour**hood**, parent → parent**hood** |\n| **-ism** | real → real**ism**, tour → tour**ism** |\n\n**Yazım değişikliklerine dikkat:**\n\n- *-y → -i*: happy → happ**i**ness\n- Sessiz *-e* düşer: arrive → arriv**al**, (ama: agree → agree**ment**)\n- *-able → -ability*: reliable → reli**ability**\n- Kökte ses değişimi: strong → str**e**ngth, long → l**e**ngth, deep → d**e**pth",
     "examples": [{"en": "The development of the new app took two years.", "tr": "Yeni uygulamanın geliştirilmesi iki yıl sürdü."},
                  {"en": "Her kindness and patience made her a great teacher.", "tr": "Nezaketi ve sabrı onu harika bir öğretmen yaptı."},
                  {"en": "Membership of the club is free for students.", "tr": "Kulüp üyeliği öğrenciler için ücretsiz."}],
     "turkishNote": "Türkçede de isim yapma ekleri çok güçlüdür: \"mutlu → mutluluk\", \"arkadaş → arkadaşlık\", \"çocuk → çocukluk\". Hatta bazı eşleşmeler neredeyse birebirdir: -ness / -lik (happiness / mutluluk), -ship / -lik (friendship / arkadaşlık), -hood / -luk (childhood / çocukluk). Ancak İngilizcede hangi sonekin geleceği tahmin edilemeyebilir (\"important → importance\" ama \"happy → happiness\"), bu yüzden kelimeleri aileleriyle birlikte öğrenmek en iyi yöntemdir."},
    [
        mc("\"decide\" isim hali:", ["decidement", "decision"], 1, "decision."),
        mc("\"strong\" isim hali:", ["strongness", "strength"], 1, "strength."),
        mc("\"friend\" soyut isim:", ["friendship", "friendhood"], 0, "friendship."),
        mc("\"confident\" isim hali:", ["confidence", "confidentness"], 0, "confidence."),
        gap("I had a very happy ___. (CHILD)", ["childhood"], "-hood."),
        gap("Thank you for your ___. (KIND)", ["kindness"], "-ness."),
        gap("The ___ of the project took three years. (DEVELOP)", ["development"], "-ment."),
        gap("We were surprised by the ___ of the river. It was over five metres deep. (DEEP)", ["depth"], "deep → depth."),
        listen("The success of any team depends on good leadership. A leader needs the ability to listen, the confidence to make difficult decisions, and the patience to support people through hard times.", "Konuşmaya göre bir liderde hangi üç özellik olmalı?", ["Dinleme yeteneği, özgüven, sabır", "Zekâ, para, güç", "Hız, disiplin, sertlik"], 0, "ability to listen, confidence, patience."),
        match([("happy", "happiness"), ("able", "ability"), ("arrive", "arrival"), ("member", "membership"), ("perform", "performance")], "Her kökü isim haliyle eşleştirin."),
    ],
    {"kind": "speaking", "task": speak("Hayatınızdaki önemli bir kişiyi (öğretmen, arkadaş, aile üyesi) anlatın (1 dakika). Bu kişinin özelliklerini anlatırken en az 6 türetilmiş isim kullanın (kindness, patience, honesty, confidence, ability, friendship, childhood, leadership, strength ...).",
                                       "The person who has influenced me most is my grandmother. During my childhood, I spent every summer at her house in the village. What I remember most is her kindness. She always had time for everyone. She also had incredible patience; she taught me to cook, sew and play backgammon, and she never got angry, even when I made a mess. Her honesty was also important to me. She always told me the truth, even when it was difficult to hear. I think her greatest strength was her ability to make people feel welcome. Our friendship is still very special to me.",
                                       ["Türetilmiş isimler", "Doğru sonekler", "Akıcı anlatım", "Telaffuz"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "Sıfat yapan sonekler", "İsim ve fiillerden sıfat türeten sonekleri (-able / -ible, -ful, -less, -ous, -ive, -al, -ic, -y) tanıyıp doğru kullanabilirim.",
    {"kind": "text", "title": "Bir ürün incelemesi", "body": "I've been using this wireless speaker for three months, and overall I'm very impressed. It's lightweight, portable and surprisingly powerful for its size. The battery is reliable, too: it lasts about twelve hours. The design is attractive and modern, and the controls are simple and intuitive. My only complaint is that the instructions were rather useless. They were confusing and full of technical terms. However, the customer service team was helpful and responsive. At this price, it's a sensible choice for anyone who wants good sound without spending a fortune. Highly recommended!",
     "questions": [
        mc("How long does the battery last?", ["About six hours", "About twelve hours", "Three months"], 1, "\"it lasts about twelve hours\""),
        mc("What was the writer's only complaint?", ["The price", "The sound", "The instructions"], 2, "\"the instructions were rather useless\""),
     ]},
    {"explanation": "**Sıfat yapan sonekler:**\n\n| Sonek | Anlam | Örnekler |\n|---|---|---|\n| **-able / -ible** | yapılabilir | rely → reli**able**, port → port**able**, sense → sens**ible**, access → access**ible** |\n| **-ful** | ile dolu | help → help**ful**, power → power**ful**, success → success**ful** |\n| **-less** | -sız | use → use**less**, home → home**less**, care → care**less** |\n| **-ous** | özelliğinde | danger → danger**ous**, fame → fam**ous**, ambition → ambiti**ous** |\n| **-ive** | eğilimli | attract → attract**ive**, create → creat**ive**, respond → respons**ive** |\n| **-al** | ile ilgili | nature → natur**al**, culture → cultur**al**, tradition → tradition**al** |\n| **-ic / -ical** | ile ilgili | economy → econom**ic**, history → histor**ic(al)**, energy → energet**ic** |\n| **-y** | ile dolu (genelde samimi) | rain → rain**y**, noise → nois**y**, health → health**y** |\n| **-ish** | -imsi, yaklaşık | child → child**ish**, red → redd**ish** |\n\n**Önemli ikililer:**\n\n| -ful | -less |\n|---|---|\n| use**ful** (yararlı) | use**less** (işe yaramaz) |\n| care**ful** (dikkatli) | care**less** (dikkatsiz) |\n| hope**ful** (umutlu) | hope**less** (umutsuz) |\n| harm**ful** (zararlı) | harm**less** (zararsız) |\n| pain**ful** (acı veren) | pain**less** (acısız) |\n\n**Dikkat:** Her *-ful* kelimesinin *-less* karşılığı yoktur: *beautiful* → ✗ *beautiless*. \n\n**Anlam farkı olan ikililer:**\n\n- *economic* (ekonomiyle ilgili: *economic growth*) / *economical* (tasarruflu: *an economical car*)\n- *historic* (tarihi önemi olan: *a historic day*) / *historical* (tarihle ilgili: *historical documents*)\n- *sensible* (mantıklı) / *sensitive* (hassas)",
     "examples": [{"en": "This is a historic moment for our country.", "tr": "Bu ülkemiz için tarihi bir an."},
                  {"en": "Small cars are more economical to run.", "tr": "Küçük arabaların kullanımı daha ekonomik."},
                  {"en": "Don't be careless with your passport.", "tr": "Pasaportuna karşı dikkatsiz olma."}],
     "turkishNote": "Türkçedeki -lı / -sız ekleri, İngilizcedeki -ful / -less ile çok benzerdir: \"umutlu / umutsuz\" = \"hopeful / hopeless\", \"zararlı / zararsız\" = \"harmful / harmless\". Ancak Türk öğrenciler sık sık \"sensible\" ile \"sensitive\" kelimelerini karıştırır. \"Sensible\" mantıklı demektir, \"hassas\" değil! Hassas için \"sensitive\" kullanılır. Ayrıca \"economic\" ve \"economical\" farkı da Türkçede tek kelimeyle (\"ekonomik\") ifade edildiği için karışıklığa yol açar."},
    [
        mc("\"mantıklı\":", ["sensible", "sensitive"], 0, "sensible = mantıklı."),
        mc("\"an ___ car\" (tasarruflu)", ["economic", "economical"], 1, "economical."),
        mc("\"care\" + -less:", ["dikkatli", "dikkatsiz"], 1, "careless."),
        mc("\"a ___ day\" (tarihi önemi olan)", ["historic", "historical"], 0, "historic."),
        gap("Thanks, that was very ___ advice. (HELP)", ["helpful"], "-ful."),
        gap("Smoking is ___ to your health. (HARM)", ["harmful"], "-ful."),
        gap("She's a very ___ designer. She always has new ideas. (CREATE)", ["creative"], "-ive."),
        gap("Climbing without ropes is extremely ___. (DANGER)", ["dangerous"], "-ous."),
        listen("I wouldn't recommend this laptop. It's attractive and fairly powerful, but the battery is completely unreliable, and the keyboard is so noisy that it's almost useless in a quiet office.", "Konuşanın dizüstü bilgisayarla ilgili şikâyeti nedir?", ["Çirkin ve yavaş olması", "Pilin güvenilmez ve klavyenin gürültülü olması", "Çok pahalı olması"], 1, "unreliable battery, noisy keyboard."),
        match([("use", "useful / useless"), ("fame", "famous"), ("nature", "natural"), ("rely", "reliable"), ("noise", "noisy")], "Her kökü sıfat haliyle eşleştirin."),
    ],
    {"kind": "speaking", "task": speak("Son zamanlarda kullandığınız bir ürünü (telefon, uygulama, kulaklık, araba ...) bir arkadaşınıza sözlü olarak tavsiye edin ya da eleştirin (1 dakika). En az 7 türetilmiş sıfat kullanın (reliable, useful, useless, attractive, powerful, economical, careless, sensible, portable ...).",
                                       "I recently bought a new pair of wireless headphones, and I'd definitely recommend them. They're lightweight and portable, so they're easy to carry around. The sound quality is powerful and clear, and the noise cancelling is really effective on the metro. The battery is reliable, too; it lasts around thirty hours. They're also quite attractive, with a simple, modern design. The app is a bit useless, to be honest, but you don't really need it. At that price, I think they're a sensible choice, especially for students.",
                                       ["Türetilmiş sıfatlar", "Doğru sonekler", "Tavsiye / eleştiri dili", "Akıcılık"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "Olumsuz önekler", "Olumsuz önekleri (un-, in-, im-, il-, ir-, dis-, mis-, non-) doğru seçebilir ve anlamlarını ayırt edebilirim.",
    {"kind": "dialogue", "title": "Toplantı sonrası", "lines": [
        {"speaker": "Ece", "text": "That meeting was a complete disaster."},
        {"speaker": "Kerem", "text": "I know. I think the manager misunderstood the whole proposal."},
        {"speaker": "Ece", "text": "And he was so impatient. He kept interrupting."},
        {"speaker": "Kerem", "text": "Half of his questions were irrelevant, too."},
        {"speaker": "Ece", "text": "Exactly. And that comment about the budget being unrealistic? It's completely inaccurate."},
        {"speaker": "Kerem", "text": "I disagree with him on almost everything. But it's impossible to change his mind."},
        {"speaker": "Ece", "text": "Well, we can't give up. Let's rewrite the proposal and present it again next week."}],
     "questions": [
        mc("What do Ece and Kerem think of the manager?", ["He was helpful.", "He misunderstood the proposal and was impatient.", "He agreed with them."], 1, "\"misunderstood\", \"impatient\""),
        mc("What do they decide to do?", ["Give up", "Rewrite and present the proposal again", "Complain to the director"], 1, "\"Let's rewrite the proposal and present it again next week.\""),
     ]},
    {"explanation": "**Olumsuz önekler:**\n\n| Önek | Kullanım | Örnekler |\n|---|---|---|\n| **un-** | en yaygın; sıfat, fiil, zarf | **un**happy, **un**realistic, **un**fair, **un**lock, **un**fortunately |\n| **in-** | çoğunlukla Latin kökenli sıfatlar | **in**accurate, **in**complete, **in**dependent, **in**formal |\n| **im-** | **p, m, b** ile başlayan kelimeler | **im**possible, **im**patient, **im**mature, **im**balance |\n| **il-** | **l** ile başlayan kelimeler | **il**legal, **il**logical, **il**literate |\n| **ir-** | **r** ile başlayan kelimeler | **ir**relevant, **ir**responsible, **ir**regular |\n| **dis-** | fiil, sıfat, isim | **dis**agree, **dis**honest, **dis**like, **dis**advantage |\n| **mis-** | yanlış / kötü | **mis**understand, **mis**lead, **mis**spell, **mis**use |\n| **non-** | -olmayan (genellikle tireyle) | **non**-smoker, **non**-profit, **non**-fiction |\n\n**Kurallar:**\n\n- **im-, il-, ir-** ses kurallarına göre seçilir (p/m/b → im, l → il, r → ir).\n- **un-** ve **in-** için kesin kural yoktur; kelimeyle birlikte öğrenin. *(un**able** ama in**ability**!)*\n- **dis-** fiillerde **tersini yapmak** anlamı verir: *appear → **dis**appear*, *connect → **dis**connect*.\n- **un-** fiillerde de **geri almak** anlamı verir: *lock → **un**lock*, *pack → **un**pack*, *do → **un**do*.\n- **mis-** \"olumsuz\" değil, **\"yanlış\"** demektir: *misunderstand* = yanlış anlamak (anlamamak değil).\n\n**Dikkat: in- her zaman olumsuz değildir!**\n\n- *inflammable* = yanıcı (= *flammable*)\n- *invaluable* = paha biçilmez, çok değerli (değersiz değil!)",
     "examples": [{"en": "It's illegal to drive without insurance.", "tr": "Sigortasız araç kullanmak yasa dışı."},
                  {"en": "Your help has been invaluable.", "tr": "Yardımınız paha biçilmezdi."},
                  {"en": "I'm sorry, I think I misread the instructions.", "tr": "Özür dilerim, sanırım talimatları yanlış okudum."}],
     "turkishNote": "Türkçede olumsuzluk genellikle sonekle yapılır: \"mutsuz\", \"imkânsız\", \"sorumsuz\". İngilizcede ise öneklerle yapılır ve doğru öneki seçmek zordur. Türk öğrencilerin sık hataları: ✗ \"unpossible\" (✓ impossible), ✗ \"unlegal\" (✓ illegal), ✗ \"inresponsible\" (✓ irresponsible). Ses kuralını (p/m/b → im, l → il, r → ir) öğrenmek bu hataların çoğunu önler. Ayrıca \"invaluable\" kelimesinin \"değersiz\" değil \"paha biçilmez\" anlamına geldiğini unutmayın."},
    [
        mc("\"possible\" olumsuzu:", ["unpossible", "impossible"], 1, "p → im."),
        mc("\"legal\" olumsuzu:", ["illegal", "unlegal"], 0, "l → il."),
        mc("\"responsible\" olumsuzu:", ["irresponsible", "inresponsible"], 0, "r → ir."),
        mc("\"Your advice was invaluable.\" anlamı:", ["Tavsiyen değersizdi.", "Tavsiyen paha biçilmezdi."], 1, "invaluable = çok değerli."),
        gap("I'm sorry, I think I ___understood the question. (yanlış)", ["mis"], "mis-."),
        gap("Telling lies is ___honest. (olumsuz)", ["dis"], "dishonest."),
        gap("His answer was completely ___relevant to the topic.", ["ir"], "irrelevant."),
        gap("This book is ___-fiction; everything in it really happened.", ["non"], "non-fiction."),
        listen("I'm afraid your application is incomplete. Several sections were left blank, and some of the information appears to be inaccurate. Unfortunately, it's impossible for us to process it in its current form.", "Başvurunun sorunları nelerdir?", ["Geç gönderilmiş ve pahalı", "Eksik ve bazı bilgiler yanlış", "Çok uzun"], 1, "incomplete, inaccurate."),
        match([("patient", "impatient"), ("logical", "illogical"), ("regular", "irregular"), ("agree", "disagree"), ("lead", "mislead")], "Her kelimeyi olumsuz / zıt haliyle eşleştirin."),
    ],
    {"kind": "speaking", "task": speak("Yaşadığınız kötü bir deneyimi (bir kurum, bir toplantı, bir tatil, bir alışveriş) anlatın (1 dakika). En az 7 olumsuz önekli kelime kullanın (unhelpful, impatient, irresponsible, illegal, inaccurate, dishonest, misunderstand, impossible, unfair, unreliable ...).",
                                       "Last year, I had a terrible experience with a moving company. First of all, they were completely unreliable. They arrived three hours late and didn't even apologise. The workers were impatient and quite careless, and they broke two of my chairs. When I complained, the manager was very unhelpful. He said it was impossible to prove that his team had broken them, which I thought was really unfair. Then the final bill was inaccurate; they charged me for five hours instead of three. I think they were simply dishonest. Maybe I misunderstood the contract, but I'll never use them again.",
                                       ["Olumsuz önekler doğru", "Çeşitlilik", "Akıcı anlatım", "Doğru telaffuz"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Anlam önekleri ve fiil yapma", "Anlam katan önekleri (over-, under-, re-, pre-, co-, out-, inter-) ve fiil yapan ekleri (-ise / -ize, -en, en-) kullanarak kelime dağarcığımı genişletebilirim.",
    {"kind": "text", "title": "Bir şirketin yeniden yapılanması", "body": "Last year, our company went through a major reorganisation. The management admitted that they had overestimated demand and underestimated costs. Several departments were restructured, and two smaller offices were merged. To strengthen the team, the company hired a new co-director who had previously worked abroad. She modernised the IT system, which enabled staff to work more efficiently. She also introduced international training programmes. At first, many employees felt overworked and underpaid, but after six months, most people agreed that the changes had been worth it. This year, the company has outperformed most of its competitors.",
     "questions": [
        mc("What mistake did the management admit?", ["They spent too little on IT.", "They overestimated demand and underestimated costs.", "They hired too many people."], 1, "\"overestimated demand and underestimated costs\""),
        mc("What did the new co-director do?", ["She closed the company.", "She modernised the IT system.", "She cut salaries."], 1, "\"She modernised the IT system\""),
     ]},
    {"explanation": "**1. Anlam önekleri:**\n\n| Önek | Anlam | Örnekler |\n|---|---|---|\n| **over-** | fazla, aşırı | **over**work, **over**estimate, **over**sleep, **over**crowded |\n| **under-** | az, yetersiz | **under**paid, **under**estimate, **under**cooked |\n| **re-** | yeniden | **re**write, **re**organise, **re**build, **re**cycle |\n| **pre-** | önce | **pre**view, **pre**pay, **pre**-war |\n| **post-** | sonra | **post**graduate, **post**-war |\n| **co-** | birlikte | **co**-worker, **co**-author, **co**operate |\n| **inter-** | arası | **inter**national, **inter**view, **inter**act |\n| **out-** | -den daha fazla / aşmak | **out**grow, **out**number, **out**live, **out**perform |\n| **multi-** | çok | **multi**national, **multi**cultural |\n| **self-** | kendi | **self**-confident, **self**-employed |\n\n**2. Fiil yapan ekler:**\n\n| Ek | Kök | Örnekler |\n|---|---|---|\n| **-ise / -ize** | sıfat / isim | modern → modern**ise**, real → real**ise**, critic → critic**ise**, summary → summar**ise** |\n| **-en** | sıfat | strong → strength**en**, wide → wid**en**, short → short**en**, deep → deep**en** |\n| **en-** | sıfat / isim | able → **en**able, courage → **en**courage, large → **en**large, danger → **en**danger |\n| **-ify** | sıfat / isim | simple → simpl**ify**, class → class**ify**, pure → pur**ify** |\n\n**Not:** İngiliz İngilizcesinde **-ise** ve **-ize** ikisi de kabul edilir (*organise / organize*); Amerikan İngilizcesi **-ize** kullanır. Bir metinde birini seçip tutarlı olun.\n\n**Kelime kombinasyonları:** Bir kelimede birden fazla ek olabilir:\n\n- *un + believe + able* → **unbelievable**\n- *re + organise + ation* → **reorganisation**\n- *en + courage + ment* → **encouragement**",
     "examples": [{"en": "Let's simplify the instructions so that everyone can understand them.", "tr": "Talimatları herkesin anlayabileceği şekilde basitleştirelim."},
                  {"en": "My teacher's encouragement gave me confidence.", "tr": "Öğretmenimin cesaretlendirmesi bana özgüven verdi."},
                  {"en": "Don't underestimate how long the journey will take.", "tr": "Yolculuğun ne kadar süreceğini hafife alma."}],
     "turkishNote": "Türkçede \"yeniden\", \"aşırı\", \"ortak\" gibi anlamlar genellikle ayrı kelimelerle ifade edilir: \"yeniden yazmak\", \"aşırı çalışmak\", \"ortak yazar\". İngilizcede ise bu anlamlar önekle tek kelimeye sığar: \"rewrite\", \"overwork\", \"co-author\". Ayrıca \"-laştırmak\" eki (modernleştirmek, basitleştirmek) İngilizcedeki \"-ise / -ify\" eklerine çok benzer: \"modernise\", \"simplify\". Bu benzerlikleri fark etmek, yeni kelimeleri tahmin etmenize yardımcı olur."},
    [
        mc("\"underestimate\" anlamı:", ["Hafife almak", "Abartmak"], 0, "under- = az."),
        mc("\"wide\" fiil hali:", ["widen", "enwide"], 0, "-en."),
        mc("\"courage\" fiil hali:", ["couragise", "encourage"], 1, "en-."),
        mc("\"outlive\" anlamı:", ["Dışarıda yaşamak", "-den daha uzun yaşamak"], 1, "out- = aşmak."),
        gap("I ___slept and missed the bus. (fazla uyumak)", ["over"], "oversleep."),
        gap("The essay is too long. Can you ___ it? (SHORT)", ["shorten"], "-en."),
        gap("We need to ___ the instructions. They're too complicated. (SIMPLE)", ["simplify"], "-ify."),
        gap("She is ___-employed; she runs her own business.", ["self"], "self-employed."),
        listen("The city council has announced plans to widen the main road and modernise the bus station. The project is expected to cost more than originally estimated, but the council says it will strengthen the local economy.", "Belediye ne yapmayı planlıyor?", ["Yolu genişletip otobüs terminalini modernleştirmek", "Yeni bir havalimanı yapmak", "Yolu kapatmak"], 0, "widen, modernise."),
        typ("Tek kelimeyle söyleyin: \"to write something again\"", variants("rewrite", "re-write"), "rewrite"),
    ],
    {"kind": "speaking", "task": speak("Okulunuzda, işyerinizde ya da şehrinizde yapılması gereken değişiklikleri önerin (1 dakika). En az 6 önekli ya da fiil yapan ekli kelime kullanın (overcrowded, underfunded, rebuild, reorganise, modernise, widen, strengthen, encourage, simplify, co-operate ...).",
                                       "I think my city needs some important changes. First, the public transport system is overcrowded, especially during rush hour, so the council should add more buses and widen some of the main roads. Second, many schools are underfunded and need to be modernised; some of them haven't been renovated for decades. Third, I'd like the council to simplify the process for opening a small business, because at the moment it's far too complicated. Finally, they should encourage people to recycle more by providing better facilities. If local businesses and the council co-operate, I'm sure these changes would strengthen the community.",
                                       ["Önekli kelimeler", "Fiil yapan ekler", "Öneri dili", "Akıcılık"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Kelime aileleri ve sınav stratejisi", "Bir kelimenin tüm ailesini (isim, fiil, sıfat, zarf, olumsuz) türetebilir, cümledeki boşluğun hangi kelime türünü gerektirdiğini analiz edebilir ve sınav tipi soruları çözebilirim.",
    {"kind": "text", "title": "Bir sınav metninden", "body": "Many students find word formation tasks extremely (1) CHALLENGE. However, with the right (2) PREPARE, they can become much more (3) MANAGE. The first step is to read the whole sentence (4) CARE and decide which part of speech is needed. Is it a noun, a verb, an adjective or an adverb? Then, think about whether the meaning is positive or negative. Many students lose marks (5) NECESSARY because they forget to add a prefix or a plural ending.\n\nAnswers: (1) challenging, (2) preparation, (3) manageable, (4) carefully, (5) unnecessarily",
     "questions": [
        mc("What is the first step in a word formation task?", ["Look up the word in a dictionary.", "Read the sentence and decide which part of speech is needed.", "Write the word in capitals."], 1, "\"decide which part of speech is needed\""),
        mc("Why do students often lose marks?", ["They write too slowly.", "They forget prefixes or plural endings.", "They don't know the root word."], 1, "\"they forget to add a prefix or a plural ending\""),
     ]},
    {"explanation": "**Kelime ailesi örnekleri:**\n\n| Fiil | İsim | Sıfat | Zarf | Olumsuz |\n|---|---|---|---|---|\n| decide | decision | decisive | decisively | indecisive |\n| succeed | success | successful | successfully | unsuccessful |\n| rely | reliability | reliable | reliably | unreliable |\n| care | care | careful / careless | carefully | careless |\n| strengthen | strength | strong | strongly | — |\n| manage | management / manager | manageable | — | unmanageable |\n| believe | belief | believable | believably | unbelievable |\n| — | necessity | necessary | necessarily | unnecessary / unnecessarily |\n\n**Sınav stratejisi (4 adım):**\n\n**1. Kelime türünü belirleyin:** Boşluktan önce ve sonra ne var?\n\n| Boşluktan önce | Gereken |\n|---|---|\n| *a / the / his / their* (+ sıfat) | **isim** |\n| *very / extremely / more / be / seem* | **sıfat** |\n| fiil + ___ / cümle sonu | **zarf** |\n| *to* / modal | **fiil** |\n\n**2. Anlam olumlu mu, olumsuz mu?** Bağlam *However, but, sadly* gibi işaretler içeriyor mu?\n\n**3. Tekil mi, çoğul mu?** (*many ___* → çoğul isim)\n\n**4. Yazımı kontrol edin!** (*happi**ness**, begin**n**ing, necessar**ily***)\n\n**Sık yapılan hatalar:**\n\n- Olumsuz öneki unutmak\n- İsmin çoğul halini unutmak: *many **possibilities***\n- Zarf yerine sıfat: ✗ *He drove careful.* ✓ *carefully*\n- İki değişiklik gereken kelimeler: *NECESSARY → **un**necessar**ily***",
     "examples": [{"en": "She answered the question confidently.", "tr": "Soruyu kendinden emin bir şekilde cevapladı."},
                  {"en": "The results were completely unbelievable.", "tr": "Sonuçlar tamamen inanılmazdı."},
                  {"en": "There are many possibilities.", "tr": "Birçok olasılık var."}],
     "turkishNote": "Türkçede bir kelimenin türü genellikle ekten kolayca anlaşılır ve zarflar çoğu zaman sıfatla aynı biçimdedir (\"iyi bir öğrenci\" / \"iyi çalıştı\"). Bu yüzden Türk öğrenciler İngilizcede sıfat yerine zarf kullanmayı (\"careful\" / \"carefully\") sık sık unutur. Ayrıca sınav sorularında öğrenciler genellikle sadece bir değişiklik yapar; oysa birçok soru hem önek hem sonek gerektirir (NECESSARY → unnecessarily). Cevap yazmadan önce her zaman \"Olumsuz mu? Çoğul mu? Zarf mı?\" diye kontrol edin."},
    [
        mc("\"He drove ___.\" (CARE)", ["careful", "carefully"], 1, "Fiilden sonra zarf."),
        mc("\"There are many ___ .\" (POSSIBLE)", ["possibility", "possibilities"], 1, "many + çoğul."),
        mc("\"Sadly, the plan was ___.\" (SUCCEED)", ["successful", "unsuccessful"], 1, "Sadly → olumsuz."),
        mc("\"a ___ leader\" (DECIDE)", ["decisive", "decision"], 0, "a + sıfat + isim."),
        gap("You don't need to bring anything. It's completely ___. (NECESSARY)", ["unnecessary"], "Olumsuz."),
        gap("She ___ passed all her exams. (SUCCEED)", ["successfully"], "Zarf."),
        gap("Good time ___ is essential for students. (MANAGE)", ["management"], "İsim."),
        gap("The story was so strange that it was almost ___. (BELIEVE)", ["unbelievable"], "un- + -able."),
        listen("When you see a gap, first ask yourself what kind of word you need. If there's an article before the gap, you probably need a noun. If there's a verb before it, you might need an adverb. And always check whether the sentence needs a negative.", "Boşluktan önce bir artikel (a / the) varsa ne gerekir?", ["Fiil", "Zarf", "Muhtemelen isim"], 2, "\"If there's an article before the gap, you probably need a noun.\""),
        typ("Doğru biçimi yazın: \"The weather is ___ at this time of year.\" (PREDICT, olumsuz)", variants("unpredictable"), "unpredictable"),
    ],
    {"kind": "writing", "task": write("\"How to learn vocabulary effectively\" başlıklı kısa bir blog yazısı ya da öneri metni yazın (140–170 kelime). Metinde en az 12 türetilmiş kelime kullanın (önek ve sonekli); bunların en az 3'ü olumsuz önekli, en az 2'si fiil yapan ekli (-ise, -en, en-, -ify) ve en az 3'ü zarf olsun. Türetilmiş kelimelerin altını çizin ya da büyük harfle yazın.",
                                      "How to learn vocabulary EFFECTIVELY\n\nMany learners find vocabulary learning FRUSTRATING. They write long lists of words, try to memorise them and then forget them a week later. This approach is not only TIRING but also largely INEFFECTIVE.\n\nA more SUCCESSFUL method is to learn words in families. When you learn \"decide\", also learn \"DECISION\", \"DECISIVE\" and \"INDECISIVE\". This will STRENGTHEN your memory, because each word helps you remember the others.\n\nSecondly, pay attention to prefixes and suffixes. Once you RECOGNISE common endings like \"-ness\" or \"-able\", you can often guess the meaning of UNFAMILIAR words without a dictionary.\n\nThirdly, review words REGULARLY. Spaced repetition apps make this much easier and will ENABLE you to remember words for months, not days.\n\nFinally, don't be IMPATIENT. Vocabulary grows SLOWLY, but if you study CONSISTENTLY, the results will be REMARKABLE. It's UNREALISTIC to expect to learn everything at once, so be kind to yourself and enjoy the process.",
                                      ["En az 12 türetilmiş kelime", "Olumsuz önekler", "Fiil yapan ekler ve zarflar", "Doğru yazım", "Anlam bütünlüğü ve akıcılık"])},
)

u.test([
    mc("\"strong\" isim hali:", ["strongness", "strength"], 1, "strength"),
    mc("\"possible\" olumsuzu:", ["unpossible", "impossible"], 1, "im-"),
    mc("\"mantıklı\":", ["sensible", "sensitive"], 0, "sensible"),
    mc("\"Your help has been invaluable.\"", ["Yardımın değersizdi.", "Yardımın paha biçilmezdi."], 1, "invaluable"),
    mc("\"She answered ___.\" (CONFIDENT)", ["confident", "confidently"], 1, "Zarf"),
    gap("I had a happy ___ in a small village. (CHILD)", ["childhood"], "-hood"),
    gap("Parking here is ___. (LEGAL, olumsuz)", ["illegal"], "il-"),
    gap("His comments were completely ___. (RELEVANT, olumsuz)", ["irrelevant"], "ir-"),
    gap("Smoking is ___ to your health. (HARM)", ["harmful"], "-ful"),
    gap("We need to ___ the road. It's too narrow. (WIDE)", ["widen"], "-en"),
    gap("Sorry, I ___understood your question. (yanlış)", ["mis"], "mis-"),
    gap("You don't need to call. It's ___. (NECESSARY, olumsuz)", ["unnecessary"], "un-"),
    listen("Our new manager has really changed the department. She has simplified many of the procedures, encouraged more teamwork and strengthened our relationship with customers. Honestly, her leadership has been invaluable.", "Yeni müdür ne yaptı?", ["Prosedürleri basitleştirdi ve ekip çalışmasını teşvik etti", "Departmanı kapattı", "Herkesin maaşını düşürdü"], 0, "simplified, encouraged, strengthened."),
    typ("Doğru biçimi yazın: \"Many people ___ how long it takes to learn a language.\" (ESTIMATE, \"hafife almak\")", variants("underestimate"), "underestimate"),
    write("\"The qualities of a good leader\" konusunda kısa bir paragraf ya da konuşma metni yazın (130–160 kelime). En az 12 türetilmiş kelime kullanın: isim yapan sonekler (-ness, -ity, -ship, -ence), sıfat yapan sonekler (-ful, -able, -ive), en az 3 olumsuz önek ve en az 2 zarf.",
          "What makes a good leader? In my opinion, the most important quality is HONESTY. A leader who is DISHONEST will quickly lose the trust of the team. Secondly, good LEADERSHIP requires PATIENCE. Leaders who are IMPATIENT or IRRESPONSIBLE tend to make CARELESS mistakes.\n\nA SUCCESSFUL leader is also DECISIVE. Being INDECISIVE can be just as harmful as making the wrong choice, because the team needs clear DIRECTION. At the same time, a good leader should be SUPPORTIVE and listen CAREFULLY to other people's ideas.\n\nFinally, I believe RELIABILITY is essential. Team members need to know that their leader will act CONSISTENTLY and keep promises. In short, the best leaders combine CONFIDENCE with KINDNESS, and they ENCOURAGE the people around them to grow.",
          ["En az 12 türetilmiş kelime", "İsim ve sıfat sonekleri", "Olumsuz önekler", "Zarflar", "Doğru yazım ve akıcılık"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

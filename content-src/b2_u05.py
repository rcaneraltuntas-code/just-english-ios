"""B2 Ünite 5: Medya."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("B2", 5, "Medya", "The Media",
         "Haber ve röportajlarda sorulan soruları, verilen emir ve rica cümlelerini dolaylı anlatımla aktarabilir, advise, warn, deny, accuse gibi aktarma fiillerini doğru kalıplarıyla kullanabilir ve bir röportajı haber diliyle özetleyebilirim.",
         ["dolaylı sorular (asked if / whether, wh-)", "dolaylı emir ve rica (told / asked sb (not) to)", "aktarma fiilleri + to / + sb + to", "aktarma fiilleri + -ing / that / edat + -ing", "haber dilinde aktarma"],
         ["medya ve gazetecilik", "röportaj", "haber ve sosyal medya"],
         {"title": "Basın toplantısı", "durationMinutes": 45,
          "goal": "Bir öğrenci ünlü bir kişiyi (sporcu, oyuncu, belediye başkanı) canlandırır, diğerleri gazeteci olarak soru sorar. Ardından her \"gazeteci\" röportajı aktarma fiilleriyle haberleştirir (The journalist asked whether..., She denied..., He promised to...). Gruplar haberlerini okur ve kimin en doğru ve en ilgi çekici aktarımı yaptığını tartışır."})

u.vocab([
    ("journalist", "gazeteci", "The journalist asked a difficult question.", "Gazeteci zor bir soru sordu.", None),
    ("press conference", "basın toplantısı", "The minister held a press conference.", "Bakan bir basın toplantısı düzenledi.", None),
    ("interview", "röportaj; röportaj yapmak", "She gave an interview to a newspaper.", "Bir gazeteye röportaj verdi.", None),
    ("headline", "manşet", "It made the headlines all over the world.", "Bütün dünyada manşet oldu.", None),
    ("source", "kaynak", "According to a reliable source, ...", "Güvenilir bir kaynağa göre ...", None),
    ("reliable", "güvenilir", "Is this website reliable?", "Bu site güvenilir mi?", None),
    ("fake news", "sahte haber", "Fake news spreads quickly online.", "Sahte haberler internette hızla yayılır.", None),
    ("go viral", "viral olmak", "The video went viral overnight.", "Video bir gecede viral oldu.", None),
    ("coverage", "haber kapsamı", "The election got a lot of coverage.", "Seçim çok fazla haber kapsamı aldı.", None),
    ("biased", "taraflı", "This newspaper is very biased.", "Bu gazete çok taraflı.", "bias (önyargı)"),
    ("editor", "editör", "The editor rejected the article.", "Editör yazıyı reddetti.", None),
    ("broadcast", "yayınlamak; yayın", "The match was broadcast live.", "Maç canlı yayınlandı.", "broadcast → broadcast"),
    ("advise", "tavsiye etmek", "She advised me to wait.", "Beklememi tavsiye etti.", "advise sb to"),
    ("warn", "uyarmak", "He warned us not to go.", "Gitmememiz için bizi uyardı.", "warn sb (not) to"),
    ("remind", "hatırlatmak", "Remind me to call her.", "Onu aramamı bana hatırlat.", "remind sb to"),
    ("persuade", "ikna etmek", "I persuaded him to come.", "Onu gelmeye ikna ettim.", None),
    ("deny", "inkâr etmek, reddetmek", "He denied taking the money.", "Parayı aldığını inkâr etti.", "deny + -ing"),
    ("accuse (of)", "suçlamak", "They accused him of lying.", "Onu yalan söylemekle suçladılar.", "accuse sb of + -ing"),
    ("insist (on)", "ısrar etmek", "She insisted on paying.", "Ödemekte ısrar etti.", None),
    ("threaten", "tehdit etmek", "He threatened to resign.", "İstifa etmekle tehdit etti.", "threaten + to"),
    ("apologise (for)", "özür dilemek", "The company apologised for the delay.", "Şirket gecikme için özür diledi.", None),
    ("suggest", "önermek", "He suggested meeting at six.", "Altıda buluşmayı önerdi.", "suggest + -ing / that"),
    ("whether", "-ıp -madığını", "She asked whether I was ready.", "Hazır olup olmadığımı sordu.", "= if"),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Ne sordu?", "Evet-hayır sorularını ve soru kelimeli soruları dolaylı anlatımla doğru sözcük sırasıyla aktarabilirim.",
    {"kind": "text", "title": "Bir röportajın perde arkası", "body": "Last week, our reporter interviewed the young chef Arda Yalın, whose restaurant has just won a major award.\n\nFirst, she asked him how he had felt when he heard the news. He said he had been completely shocked.\n\nShe then asked whether he had always wanted to be a chef. He laughed and said that, as a child, he had wanted to be a footballer.\n\nShe also asked him what his favourite dish was and where he found his inspiration. Arda explained that his grandmother's cooking was his biggest influence.\n\nFinally, she asked if he was planning to open a second restaurant. He refused to answer, but he smiled.",
     "questions": [
        mc("What did Arda want to be as a child?", ["A chef", "A footballer", "A journalist"], 1, "\"as a child, he had wanted to be a footballer\""),
        mc("What is Arda's biggest influence?", ["His mother", "His grandmother's cooking", "Famous chefs"], 1, "\"his grandmother's cooking was his biggest influence\""),
     ]},
    {"explanation": "B1'de ifadeleri aktarmayı öğrendiniz. **Soruları** aktarırken iki önemli değişiklik olur:\n\n**1. Soru sırası düz cümle sırasına döner** (yardımcı fiil ve do/does/did kalkar)\n\n**2. Soru işareti kullanılmaz.**\n\n**Evet-hayır soruları → ask + if / whether**\n\n| Doğrudan | Dolaylı |\n|---|---|\n| \"**Are you** happy?\" | She asked **if he was** happy. |\n| \"**Have you** always wanted to cook?\" | She asked **whether he had** always wanted to cook. |\n| \"**Do you** like fish?\" | She asked **if he liked** fish. |\n\n**Soru kelimeli sorular → ask + soru kelimesi + özne + fiil**\n\n| Doğrudan | Dolaylı |\n|---|---|\n| \"**What is** your favourite dish?\" | She asked **what his favourite dish was**. |\n| \"**Where do you** find inspiration?\" | She asked **where he found** inspiration. |\n| \"**How did you** feel?\" | She asked **how he had felt**. |\n\n**Zaman kaydırma** ve **zamir değişiklikleri** ifadelerdeki gibidir.\n\n**Dikkat:** ~~She asked where did he find~~ / ~~She asked what was his favourite dish~~ (soru sırası korunmaz)\n\n**Diğer fiiller:** **wanted to know** / **wondered** + if / wh-",
     "examples": [{"en": "He asked me where I lived.", "tr": "Bana nerede yaşadığımı sordu."},
                  {"en": "The interviewer asked whether I had any experience.", "tr": "Mülakatçı deneyimim olup olmadığını sordu."},
                  {"en": "I wondered what time the shop closed.", "tr": "Dükkânın saat kaçta kapandığını merak ettim."}],
     "turkishNote": "Türkçede dolaylı soru yapısı (\"nerede yaşadığımı sordu\") düz cümle gibidir; İngilizcede de öyledir: He asked where I lived. Türkçe konuşanların sık hatası, soru sırasını korumaktır: \"He asked where do I live\" yanlıştır. Evet-hayır sorularında \"-ıp -madığını\" yapısı if / whether ile karşılanır."},
    [
        mc("\"Where do you live?\" → He asked me ___.", ["where do I live", "where I lived", "where did I live"], 1, "Düz sıra + zaman kaydırma."),
        mc("\"Are you ready?\" → She asked ___ I was ready.", ["if", "that", "what"], 0, "Evet-hayır → if / whether."),
        mc("Hangisi doğru?", ["She asked what was his name.", "She asked what his name was."], 1, "Düz sıra: özne + fiil."),
        mc("Dolaylı soruda soru işareti:", ["Kullanılır", "Kullanılmaz"], 1, "Dolaylı soru düz cümledir."),
        gap("\"Have you finished?\" → He asked whether I ___ finished.", ["had"], "present perfect → past perfect."),
        gap("\"What time does the film start?\" → She asked what time the film ___.", ["started"], "does start → started."),
        gap("\"Can you help me?\" → He asked if I ___ help him.", ["could"], "can → could."),
        gap("\"Why did you leave?\" → They asked me why I ___ left.", ["had"], "did leave → had left."),
        listen("The customs officer asked me where I had come from and how long I was planning to stay. Then he asked if I had anything to declare.", "Gümrük memuru ne sordu?", ["Nerede çalıştığını", "Nereden geldiğini ve ne kadar kalacağını", "Kaç yaşında olduğunu"], 1, "\"where I had come from and how long I was planning to stay\""),
        typ("Aktarın: Selin: \"Where did you buy your shoes?\" (Selin asked me ...)", variants("Selin asked me where I had bought my shoes.", "Selin asked me where I bought my shoes.", "Selin asked me where I'd bought my shoes."), "Selin asked me where I had bought my shoes."),
    ],
    {"kind": "speaking", "task": speak("Son katıldığınız bir iş görüşmesinde, sınavda ya da resmî bir görüşmede (vize, banka, doktor) size sorulan 6 soruyu dolaylı anlatımla aktarın. En az 2 evet-hayır sorusu (if / whether) ve 3 soru kelimeli soru olsun.",
                                       "At my last job interview, they asked me why I wanted to leave my current job. Then they asked whether I had ever managed a team. They wanted to know what my biggest weakness was and how I dealt with stress. They also asked if I could start in two weeks, and finally they asked where I saw myself in five years.",
                                       ["Düz sözcük sırası", "if / whether", "Zaman kaydırma"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "Yapmamı istedi", "Emir ve rica cümlelerini told / asked + kişi + (not) to ile aktarabilirim.",
    {"kind": "dialogue", "title": "Haber merkezinde ilk gün", "lines": [
        {"speaker": "Ece", "text": "How was your first day at the TV station?"},
        {"speaker": "Kaan", "text": "Intense! The editor told me to check every fact twice before I wrote anything."},
        {"speaker": "Ece", "text": "Sounds sensible. What else?"},
        {"speaker": "Kaan", "text": "She asked me not to post anything about the stories on social media. And she warned me not to trust anonymous sources."},
        {"speaker": "Ece", "text": "Did you get to go out on a story?"},
        {"speaker": "Kaan", "text": "Yes! A senior reporter asked me to come with her to a press conference. She told me to stay quiet and just take notes."}],
     "questions": [
        mc("What did the editor tell Kaan to do?", ["Write quickly", "Check every fact twice", "Post on social media"], 1, "\"The editor told me to check every fact twice\""),
        mc("What did the senior reporter ask Kaan to do?", ["Ask questions", "Come with her to a press conference", "Write the story"], 1, "\"asked me to come with her to a press conference\""),
     ]},
    {"explanation": "**Emir ve rica cümleleri** aktarılırken **to + yalın fiil** kullanılır. Zaman kaydırma gerekmez.\n\n| Doğrudan | Dolaylı |\n|---|---|\n| \"**Check** every fact.\" | She **told me to check** every fact. |\n| \"**Don't post** anything.\" | She **told me not to post** anything. |\n| \"**Could you come** with me?\" | She **asked me to come** with her. |\n| \"**Please don't be** late.\" | He **asked us not to be** late. |\n\n**Yapı:** fiil + **kişi** + **(not) to** + yalın fiil\n\n| Fiil | Ton |\n|---|---|\n| **tell** sb to | emir |\n| **ask** sb to | rica |\n| **order** sb to | resmî / askerî emir |\n| **beg** sb to | yalvarma |\n| **warn** sb (not) to | uyarı |\n| **remind** sb to | hatırlatma |\n| **advise** sb to | tavsiye |\n| **encourage** sb to | cesaretlendirme |\n\n**Dikkat:** \"say\" bu yapıyla kullanılmaz: ~~She said me to check~~ → She **told me to** check.",
     "examples": [{"en": "The doctor told me to rest for a week.", "tr": "Doktor bir hafta dinlenmemi söyledi."},
                  {"en": "My mum reminded me to take my keys.", "tr": "Annem anahtarlarımı almamı hatırlattı."},
                  {"en": "The police warned people not to leave their homes.", "tr": "Polis insanları evlerinden çıkmamaları için uyardı."}],
     "turkishNote": "Türkçede \"gitmememi söyledi\" yapısında olumsuzluk fiile eklenir. İngilizcede not, to'dan önce gelir: He told me not to go (~~He didn't tell me to go~~ farklı bir anlama gelir: Bana gitmemi söylemedi). \"say\" fiili bu yapıda kullanılamaz; tell, ask, warn gibi fiiller tercih edilmelidir."},
    [
        mc("\"Sit down.\" → He told me ___ down.", ["sit", "to sit", "sitting"], 1, "told + kişi + to."),
        mc("\"Don't be late.\" → She told us ___ late.", ["to not be", "not to be", "don't be"], 1, "not to + fiil."),
        mc("Hangisi doğru?", ["She said me to wait.", "She told me to wait."], 1, "tell + kişi + to."),
        mc("\"He told me not to go.\" ≠", ["He didn't tell me to go.", "He told me that I shouldn't go."], 0, "Anlam farklı."),
        gap("\"Please help me.\" → She asked me ___ help her.", ["to"], "asked + kişi + to."),
        gap("\"Don't touch the wire!\" → He warned us ___ to touch the wire.", ["not"], "warn sb not to."),
        gap("\"Remember to call your dad.\" → My mum ___ me to call my dad.", ["reminded"], "remind sb to."),
        gap("\"You should see a lawyer.\" → She ___ me to see a lawyer.", ["advised"], "advise sb to."),
        listen("Before the exam, the teacher told us to switch off our phones and not to talk. She also reminded us to write our names on every page.", "Öğretmen neyi hatırlattı?", ["Telefonları kapatmayı", "Her sayfaya isim yazmayı", "Erken gelmeyi"], 1, "\"reminded us to write our names on every page\""),
        typ("Aktarın: Doctor: \"Don't eat too much salt.\" (The doctor told me ...)", variants("The doctor told me not to eat too much salt.", "The doctor told me not to eat so much salt."), "The doctor told me not to eat too much salt."),
    ],
    {"kind": "speaking", "task": speak("Hayatınızda aldığınız en önemli 5 tavsiye, uyarı ya da talimatı aktarın (anne-babanız, bir öğretmen, bir doktor, bir patron). told / asked / advised / warned / reminded / encouraged + kişi + (not) to yapılarını kullanın.",
                                       "My father always told me to save some money every month. My English teacher encouraged me to read books in English. When I started driving, my mother warned me not to use my phone in the car. My first boss advised me to ask questions when I didn't understand something. And my doctor told me to drink more water.",
                                       ["fiil + kişi + (not) to", "Çeşitli aktarma fiilleri", "say kullanılmadı"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "Söz verdi, reddetti", "Aktarma fiillerini doğru kalıplarıyla (fiil + to, fiil + kişi + to) kullanarak söylenenlerin niyetini aktarabilirim.",
    {"kind": "text", "title": "Belediye meclisinde gergin toplantı", "body": "Yesterday's city council meeting was one of the most heated in years.\n\nThe mayor promised to build three new parks before the end of her term. However, opposition councillors refused to support the plan, saying it was too expensive.\n\nOne councillor even threatened to take the issue to court. The mayor's team offered to publish the full budget online, and the opposition finally agreed to discuss the plan again next month.\n\nLocal residents who attended the meeting urged the council to make a decision quickly. One resident, a teacher, persuaded several councillors to visit her school, where there is no playground at all.",
     "questions": [
        mc("What did the mayor promise?", ["To lower taxes", "To build three new parks", "To publish a book"], 1, "\"The mayor promised to build three new parks\""),
        mc("What did the opposition agree to do?", ["Support the plan immediately", "Discuss the plan again next month", "Go to court"], 1, "\"the opposition finally agreed to discuss the plan again next month\""),
     ]},
    {"explanation": "**said** yerine **aktarma fiilleri** kullanmak, konuşanın **niyetini** de aktarır. Her fiilin kendi **kalıbı** vardır.\n\n**1. Fiil + to + yalın fiil**\n\n| Fiil | Doğrudan | Dolaylı |\n|---|---|---|\n| **promise** | \"I'll build three parks.\" | She **promised to build** three parks. |\n| **refuse** | \"No, I won't support it.\" | They **refused to support** it. |\n| **offer** | \"Shall I publish the budget?\" | They **offered to publish** the budget. |\n| **agree** | \"OK, we'll discuss it.\" | They **agreed to discuss** it. |\n| **threaten** | \"I'll go to court!\" | He **threatened to go** to court. |\n\n**2. Fiil + kişi + to + yalın fiil**\n\n| Fiil | Doğrudan | Dolaylı |\n|---|---|---|\n| **urge** | \"Please decide quickly!\" | They **urged the council to decide**. |\n| **persuade** | (ikna etti) | She **persuaded them to visit**. |\n| **invite** | \"Would you like to come?\" | He **invited me to come**. |\n| **encourage** | \"Go on, try it!\" | She **encouraged me to try**. |\n\n**Olumsuz:** not to → He **promised not to tell** anyone.",
     "examples": [{"en": "He offered to carry my bags.", "tr": "Çantalarımı taşımayı teklif etti."},
                  {"en": "She refused to answer the question.", "tr": "Soruyu cevaplamayı reddetti."},
                  {"en": "My friends persuaded me to apply for the job.", "tr": "Arkadaşlarım beni işe başvurmaya ikna etti."}],
     "turkishNote": "Türkçede \"taşımayı teklif etti\", \"cevaplamayı reddetti\" gibi yapılar \"-mayı / -meyi\" ile kurulur. İngilizcede bu fiiller to + yalın fiil alır: offered to carry, refused to answer. \"He refused answering\" ya da \"He offered me carrying\" yanlıştır."},
    [
        mc("\"I'll help you.\" → He ___ to help me.", ["promised", "denied", "accused"], 0, "promise + to."),
        mc("\"No, I won't sign it.\" → She ___ to sign it.", ["agreed", "refused", "offered"], 1, "refuse + to."),
        mc("\"Shall I drive you home?\" → He ___ to drive me home.", ["offered", "threatened", "refused"], 0, "offer + to."),
        mc("Hangisi doğru?", ["He refused answering.", "He refused to answer."], 1, "refuse + to."),
        gap("\"If you don't pay, I'll call the police!\" → He ___ to call the police.", ["threatened"], "threaten + to."),
        gap("\"Go on, apply for it!\" → My sister ___ me to apply.", ["encouraged", "urged", "persuaded"], "encourage sb to."),
        gap("\"Would you like to come to dinner?\" → She ___ me to come to dinner.", ["invited"], "invite sb to."),
        gap("\"I won't tell anyone, I promise.\" → He promised ___ to tell anyone.", ["not"], "promise not to."),
        listen("The company's CEO refused to comment on the rumours, but she promised to give more information at next week's press conference.", "CEO ne vaat etti?", ["Söylentileri yalanlamayı", "Gelecek haftaki basın toplantısında daha fazla bilgi vermeyi", "İstifa etmeyi"], 1, "\"she promised to give more information at next week's press conference\""),
        typ("Aktarın (offer): Ali: \"Shall I carry your bags?\"", variants("Ali offered to carry my bags.", "Ali offered to carry my bag.", "He offered to carry my bags.", "Ali offered to carry the bags.", "Ali offered to carry your bags.", "Ali offered to carry her bags.", "Ali offered to carry his bags."), "Ali offered to carry my bags."),
    ],
    {"kind": "speaking", "task": speak("Bir aile toplantısını, iş toplantısını ya da arkadaşlarla bir tartışmayı (gerçek ya da hayali) aktarın. promise, refuse, offer, agree, threaten (+ to) ve persuade, encourage, urge, invite (+ kişi + to) fiillerinden en az 6 tanesini kullanın.",
                                       "Last week we had a family meeting about our summer holiday. My dad offered to pay for the hotel. My sister refused to go camping again, and my brother threatened to stay at home. In the end, my mum persuaded everyone to try a new place. My grandparents invited us to stay with them for a week, and we all agreed to go to Ayvalık.",
                                       ["Fiil + to doğru", "Fiil + kişi + to doğru", "Niyet aktarımı"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "İnkâr etti, suçladı", "-ing, that ve edat + -ing alan aktarma fiilleriyle (deny, admit, suggest, accuse of, apologise for) karmaşık ifadeleri aktarabilirim.",
    {"kind": "dialogue", "title": "Skandal haberi", "lines": [
        {"speaker": "Presenter", "text": "Breaking news: the football club's president has been accused of hiding financial information."},
        {"speaker": "Reporter", "text": "That's right. At this morning's press conference, he denied doing anything illegal."},
        {"speaker": "Presenter", "text": "Did he admit making any mistakes?"},
        {"speaker": "Reporter", "text": "He admitted that the club's accounts had not been checked properly, and he apologised for not being more careful."},
        {"speaker": "Presenter", "text": "And what happens next?"},
        {"speaker": "Reporter", "text": "Fans are insisting on a full investigation, and one lawyer has suggested that the president should step down until it's finished."}],
     "questions": [
        mc("What did the president deny?", ["Making mistakes", "Doing anything illegal", "Being the president"], 1, "\"he denied doing anything illegal\""),
        mc("What did one lawyer suggest?", ["That the fans should leave", "That the president should step down", "That the club should be sold"], 1, "\"suggested that the president should step down\""),
     ]},
    {"explanation": "**3. Fiil + -ing**\n\n| Fiil | Doğrudan | Dolaylı |\n|---|---|---|\n| **deny** | \"I didn't do it.\" | He **denied doing** it. |\n| **admit** | \"Yes, I made a mistake.\" | He **admitted making** a mistake. |\n| **suggest** | \"Let's meet at six.\" | She **suggested meeting** at six. |\n| **recommend** | \"You should try the fish.\" | He **recommended trying** the fish. |\n\n**4. Fiil + (kişi) + edat + -ing**\n\n| Fiil | Örnek |\n|---|---|\n| **accuse** sb **of** | They **accused him of hiding** information. |\n| **apologise for** | He **apologised for being** late. |\n| **insist on** | She **insisted on paying**. |\n| **blame** sb **for** | They **blamed me for losing** the keys. |\n| **thank** sb **for** | She **thanked us for coming**. |\n| **congratulate** sb **on** | We **congratulated her on winning**. |\n\n**5. Fiil + that + cümle** (birçok fiil bu kalıbı da alır)\n\n- He **admitted that** the accounts had not been checked.\n- She **suggested that** he **should** step down. (suggest + -ing **veya** that + should)\n\n**Dikkat:** ~~suggest someone to do~~ yanlıştır: She suggested **that I** (should) **go** / She suggested **going**.",
     "examples": [{"en": "The minister denied knowing about the plan.", "tr": "Bakan plandan haberi olduğunu inkâr etti."},
                  {"en": "She accused me of reading her messages.", "tr": "Beni mesajlarını okumakla suçladı."},
                  {"en": "He suggested that we should take a break.", "tr": "Mola vermemizi önerdi."}],
     "turkishNote": "\"Bana gitmemi önerdi\" cümlesini \"He suggested me to go\" diye çevirmek Türkçe konuşanların çok sık yaptığı bir hatadır. suggest kişi + to almaz: He suggested going / He suggested that I (should) go. Aynı şekilde \"accuse\" fiili \"of\" ile kullanılır: accused him of lying (~~accused him for lying~~)."},
    [
        mc("\"I didn't take the money!\" → He denied ___ the money.", ["to take", "taking"], 1, "deny + -ing."),
        mc("Hangisi doğru?", ["She suggested me to go.", "She suggested that I should go."], 1, "suggest + that / -ing."),
        mc("They accused him ___ lying.", ["for", "of", "with"], 1, "accuse of."),
        mc("\"I'm sorry I'm late.\" → He apologised ___ late.", ["to be", "for being"], 1, "apologise for + -ing."),
        gap("\"Yes, I broke the window.\" → She admitted ___ (break) the window.", ["breaking"], "admit + -ing."),
        gap("\"No, I'll pay!\" → He insisted ___ paying.", ["on"], "insist on."),
        gap("\"Let's go to the cinema.\" → She suggested ___ (go) to the cinema.", ["going"], "suggest + -ing."),
        gap("\"You lost the tickets!\" → They blamed me ___ losing the tickets.", ["for"], "blame sb for."),
        match([("deny", "+ -ing"), ("accuse", "+ sb + of + -ing"), ("insist", "+ on + -ing"), ("promise", "+ to"), ("advise", "+ sb + to")], "Fiilleri kalıplarıyla eşleştirin."),
        listen("The actor apologised for missing the premiere, but he denied having any problems with the director. He also thanked the fans for their support.", "Oyuncu neyi inkâr etti?", ["Galayı kaçırdığını", "Yönetmenle sorunu olduğunu", "Hayranlarına teşekkür ettiğini"], 1, "\"he denied having any problems with the director\""),
    ],
    {"kind": "speaking", "task": speak("Gerçek ya da hayali bir \"skandal\" haberini muhabir gibi sunun (bir ünlü, bir şirket, bir spor kulübü). accuse of, deny, admit, apologise for, insist on ve suggest fiillerini doğru kalıplarıyla kullanın.",
                                       "Good evening. A famous singer has been accused of copying another artist's song. At a press conference today, she denied stealing the melody. However, she admitted that she had listened to the song before. She apologised for causing confusion and insisted on meeting the other artist. Her lawyer suggested that both artists should share the credit.",
                                       ["Edat + -ing kalıpları", "deny / admit / suggest + -ing", "Haber üslubu"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Röportajdan habere", "Bir röportajı aktarma fiilleri ve dolaylı anlatımla, haber üslubunda tarafsız ve doğru bir şekilde özetleyebilirim.",
    {"kind": "dialogue", "title": "Röportaj: Genç bir girişimci", "lines": [
        {"speaker": "Reporter", "text": "Your recycling app has 2 million users. Did you ever expect this?"},
        {"speaker": "Melis", "text": "Honestly, no. I started it as a university project. I never thought it would get this big."},
        {"speaker": "Reporter", "text": "Some people say your app collects too much personal data. Is that true?"},
        {"speaker": "Melis", "text": "Absolutely not. We don't sell any data. But I'll publish a full privacy report next month."},
        {"speaker": "Reporter", "text": "What advice would you give to young entrepreneurs?"},
        {"speaker": "Melis", "text": "Don't wait for the perfect idea. Start small, and listen to your users."}],
     "questions": [
        mc("How did Melis start the app?", ["With a big investment", "As a university project", "With a famous partner"], 1, "\"I started it as a university project\""),
        mc("What will Melis publish next month?", ["A new app", "A full privacy report", "A book"], 1, "\"I'll publish a full privacy report next month\""),
     ]},
    {"explanation": "**Bir röportajı haberleştirirken:**\n\n1. **Soruları** dolaylı anlatımla aktarın: *She was asked whether she had expected ...*\n2. **Cevapları** niyeti gösteren fiillerle aktarın: *She **admitted** that ... / She **denied** ...*\n3. **Tavsiye ve emirleri** to ile aktarın: *She **advised** young people **not to wait** ...*\n4. Gerekirse kısa **doğrudan alıntılar** ekleyin: *\"Start small,\" she said.*\n\n**Gazetecilik dilinde sık kullanılan fiiller:**\n\n| Fiil | Kullanım |\n|---|---|\n| **claim** (that) | iddia etmek (kanıt olmayabilir) |\n| **state** (that) | resmî olarak belirtmek |\n| **reveal** (that) | ortaya çıkarmak, açıklamak |\n| **confirm** (that) | doğrulamak |\n| **point out** (that) | dikkat çekmek |\n| **add** (that) | eklemek |\n\n**Passive aktarma** (haber dili):\n\n- She **was asked** whether ... (Ona ... sorulduğunda)\n- Melis, **who was interviewed** last week, ...\n\n**Tarafsızlık:** Gazeteci kendi fikrini değil, kaynağın söylediklerini aktarır. **claim** kelimesi, iddianın doğrulanmadığını ima eder.",
     "examples": [{"en": "The company claimed that the product was completely safe.", "tr": "Şirket ürünün tamamen güvenli olduğunu iddia etti."},
                  {"en": "She revealed that she had been offered a job in Hollywood.", "tr": "Hollywood'dan iş teklifi aldığını açıkladı."},
                  {"en": "When asked about her plans, she refused to give details.", "tr": "Planları sorulduğunda ayrıntı vermeyi reddetti."}],
     "turkishNote": "Türk basınında \"... dedi\", \"... ifade etti\", \"... kaydetti\" gibi fiiller sık kullanılır. İngilizce haber dilinde de benzer çeşitlilik vardır: said, stated, claimed, revealed, added. \"claim\" kelimesi Türkçedeki \"iddia etti\" gibi tarafsız ama temkinli bir ton taşır; söylenen şeyin doğru olduğunu garanti etmez."},
    [
        mc("Doğrulanmamış bir iddia:", ["She claimed that ...", "She confirmed that ..."], 0, "claim → iddia."),
        mc("Gizli bir bilgiyi açıklamak:", ["reveal", "deny"], 0, "reveal."),
        mc("\"Did you ever expect this?\" → She was asked ___.", ["whether she had ever expected it", "did she ever expect it"], 0, "whether + düz sıra."),
        gap("\"Don't wait for the perfect idea.\" → She advised young entrepreneurs ___ to wait.", ["not"], "advise sb not to."),
        gap("\"We don't sell any data.\" → She ___ selling any data.", ["denied"], "deny + -ing."),
        gap("\"I'll publish a report.\" → She promised ___ publish a report.", ["to"], "promise to."),
        gap("When ___ about her plans, she smiled. (sorulduğunda)", ["asked"], "When asked."),
        gap("She ___ out that most of her users were under 25. (dikkat çekti)", ["pointed"], "point out."),
        listen("The minister confirmed that the new law would come into force in January. However, he refused to say how much it would cost, and he denied that taxes would rise.", "Bakan neyi doğruladı?", ["Vergilerin artacağını", "Yeni yasanın ocakta yürürlüğe gireceğini", "Maliyeti"], 1, "\"The minister confirmed that the new law would come into force in January.\""),
        typ("Aktarın (claim): Company: \"Our product is the best on the market.\"", variants("The company claimed that its product was the best on the market.", "The company claimed its product was the best on the market.", "The company claimed that their product was the best on the market.", "The company claimed their product was the best on the market."), "The company claimed that its product was the best on the market."),
    ],
    {"kind": "writing", "task": write("Yukarıdaki Melis röportajını bir gazete haberi olarak yazın (160–200 kelime). Bir manşetle başlayın. Soruları dolaylı anlatımla, cevapları en az 6 farklı aktarma fiiliyle (admit, deny, promise, advise, reveal, claim, point out...) aktarın ve en az bir kısa doğrudan alıntı ekleyin.",
                                      "YOUNG FOUNDER DENIES DATA CLAIMS\n\nMelis Aydın, the 26-year-old founder of the recycling app GreenStep, has denied selling her users' personal data.\n\nIn an interview with our newspaper, Ms Aydın was asked whether she had ever expected her app to become so successful. She admitted that she had never imagined it would reach 2 million users. She revealed that the app had started as a simple university project.\n\nWhen asked about recent criticism that the app collects too much information, Ms Aydın was firm. She insisted that the company did not sell any data, and she promised to publish a full privacy report next month. She pointed out that the app had been checked by independent experts last year.\n\nFinally, she was asked what advice she would give to young people who want to start a business. She advised them not to wait for the perfect idea. \"Start small, and listen to your users,\" she said.\n\nThe privacy report will be published in early June.",
                                      ["Manşet ve haber yapısı", "Dolaylı sorular doğru", "En az 6 aktarma fiili doğru kalıplarla", "Doğrudan alıntı", "Tarafsız haber üslubu"])},
)

u.test([
    mc("\"Where do you work?\" → He asked me where ___.", ["do I work", "I worked"], 1, "Düz sıra"),
    mc("\"Are you tired?\" → She asked ___ I was tired.", ["that", "whether"], 1, "whether"),
    mc("Hangisi doğru?", ["She said me to wait.", "She told me to wait."], 1, "tell + kişi + to"),
    mc("\"Don't touch it.\" → He told me ___ it.", ["not to touch", "to not touching"], 0, "not to"),
    mc("Hangisi doğru?", ["She suggested me to go.", "She suggested going."], 1, "suggest + -ing"),
    mc("They accused her ___ stealing.", ["for", "of"], 1, "accuse of"),
    gap("\"I didn't do it!\" → He denied ___ (do) it.", ["doing"], "deny + -ing"),
    gap("\"Shall I help?\" → She offered ___ help.", ["to"], "offer to"),
    gap("\"No, I won't come.\" → He ___ to come.", ["refused"], "refuse to"),
    gap("\"I'm sorry I forgot.\" → She apologised ___ forgetting.", ["for"], "apologise for"),
    gap("\"Remember to lock the door.\" → He ___ me to lock the door.", ["reminded"], "remind sb to"),
    gap("\"What time does it start?\" → I asked what time it ___.", ["started"], "Zaman kaydırma"),
    listen("The journalist asked the mayor whether she would run for election again. The mayor refused to answer directly, but she admitted that she was thinking about it.", "Belediye başkanı ne itiraf etti?", ["Tekrar aday olacağını", "Bunu düşündüğünü", "İstifa edeceğini"], 1, "\"she admitted that she was thinking about it\""),
    typ("Aktarın (warn): \"Don't swim here. It's dangerous.\" (The lifeguard warned us ...)", variants("The lifeguard warned us not to swim there.", "The lifeguard warned us not to swim there because it was dangerous.", "The lifeguard warned us not to swim there as it was dangerous.", "The lifeguard warned us not to swim here."), "The lifeguard warned us not to swim there."),
    write("Bir şirketin ürünüyle ilgili yaşanan bir sorunu (geri çağırma, müşteri şikâyeti, gecikme) anlatan kısa bir haber yazın (160–200 kelime). Hayali bir basın toplantısında sorulan soruları ve verilen cevapları dolaylı anlatımla aktarın; en az 6 farklı aktarma fiili (claim, deny, admit, apologise for, promise, urge, confirm...) kullanın.",
          "PHONE MAKER RECALLS 50,000 DEVICES\n\nTechnology company NovaTel has confirmed that it is recalling 50,000 smartphones after several reports of batteries overheating.\n\nAt a press conference yesterday, the company's director, Murat Kaya, was asked how many customers had been affected. He revealed that around 30 cases had been reported, but he insisted that nobody had been seriously hurt.\n\nWhen journalists asked whether the company had known about the problem for months, Mr Kaya denied hiding any information. However, he admitted that the first tests had not been carried out carefully enough, and he apologised for causing customers so much worry.\n\nMr Kaya promised to replace every faulty phone free of charge within two weeks. He also urged customers to stop using the phone immediately and to contact the company's customer service.\n\nSome consumer groups claimed that the company had acted too slowly. One expert pointed out that similar problems had been reported in other countries last year.\n\nThe company's share price fell by 8% after the announcement.",
          ["Dolaylı sorular", "Çeşitli aktarma fiilleri doğru kalıplarla", "Zaman kaydırma", "Haber üslubu", "Düzenli metin"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

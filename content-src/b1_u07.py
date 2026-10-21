"""B1 Ünite 7: Aktarma."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("B1", 7, "Aktarma", "Reported Speech",
         "Başkalarının söylediklerini dolaylı anlatımla aktarabilir, say ve tell'i doğru kullanabilir, zaman, zamir ve zaman ifadelerini değiştirebilir ve explain, promise, complain gibi fiillerle konuşmaları özetleyebilirim.",
         ["say ve tell", "dolaylı anlatım: present → past", "zaman kaydırma: perfect, past, will, can", "zamir ve zaman ifadesi değişiklikleri", "aktarma fiilleri + that"],
         ["iletişim fiilleri", "mesajlar ve dedikodu", "iş yeri iletişimi"],
         {"title": "Kim ne dedi?", "durationMinutes": 45,
          "goal": "Öğrenciler \"kulaktan kulağa\" oyununun gelişmiş bir halini oynar: Her öğrenci kısa bir cümle duyar ve bir sonrakine He said that... / She told me that... ile aktarır. Sonra çiftler halinde birbirlerini hafta sonları hakkında röportaj yapar ve partnerlerinin söylediklerini aktarma fiilleriyle (explained, complained, admitted) sınıfa anlatır."})

u.vocab([
    ("say", "söylemek, demek", "She said that she was tired.", "Yorgun olduğunu söyledi.", "say → said; say (to sb)"),
    ("tell", "söylemek, anlatmak (birine)", "He told me that he was busy.", "Bana meşgul olduğunu söyledi.", "tell → told; tell + kişi"),
    ("explain", "açıklamak", "She explained that the shop was closed.", "Dükkânın kapalı olduğunu açıkladı.", None),
    ("promise", "söz vermek", "He promised that he would call.", "Arayacağına söz verdi.", None),
    ("complain", "şikâyet etmek", "They complained that the room was cold.", "Odanın soğuk olduğundan şikâyet ettiler.", "complaint (şikâyet)"),
    ("admit", "itiraf etmek, kabul etmek", "He admitted that he had made a mistake.", "Hata yaptığını kabul etti.", None),
    ("agree", "katılmak, kabul etmek", "She agreed that it was a good idea.", "Bunun iyi bir fikir olduğunu kabul etti.", None),
    ("reply", "cevap vermek", "He replied that he didn't know.", "Bilmediğini cevap verdi.", None),
    ("mention", "bahsetmek", "She mentioned that she was moving.", "Taşınacağından bahsetti.", None),
    ("announce", "duyurmak", "The manager announced that the office would close.", "Müdür ofisin kapanacağını duyurdu.", None),
    ("whisper", "fısıldamak", "He whispered that he loved her.", "Onu sevdiğini fısıldadı.", None),
    ("shout", "bağırmak", "Someone shouted that there was a fire.", "Biri yangın olduğunu bağırdı.", None),
    ("gossip", "dedikodu; dedikodu yapmak", "I don't like gossip.", "Dedikoduyu sevmem.", None),
    ("rumour", "söylenti", "There's a rumour that she's leaving.", "Gideceğine dair bir söylenti var.", None),
    ("message", "mesaj", "Can I take a message?", "Mesaj bırakmak ister misiniz?", None),
    ("pass on", "iletmek", "I'll pass on your message.", "Mesajını iletirim.", None),
    ("keep a secret", "sır saklamak", "Can you keep a secret?", "Sır saklayabilir misin?", None),
    ("tell the truth", "doğruyu söylemek", "Please tell me the truth.", "Lütfen bana doğruyu söyle.", None),
    ("the day before", "bir önceki gün", "She said she had seen him the day before.", "Onu bir önceki gün gördüğünü söyledi.", "yesterday → the day before"),
    ("the next day", "ertesi gün", "He said he would come the next day.", "Ertesi gün geleceğini söyledi.", "tomorrow → the next day"),
    ("that day", "o gün", "She said she was busy that day.", "O gün meşgul olduğunu söyledi.", "today → that day"),
    ("according to", "-e göre", "According to Ali, the meeting is at ten.", "Ali'ye göre toplantı saat onda.", None),
    ("misunderstand", "yanlış anlamak", "I think you misunderstood me.", "Sanırım beni yanlış anladın.", "misunderstanding"),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Ne dedi?", "say ve tell'i doğru kullanarak başkasının söylediklerini aktarabilirim.",
    {"kind": "dialogue", "title": "Ofiste", "lines": [
        {"speaker": "Burak", "text": "Did you talk to Seda this morning?"},
        {"speaker": "Gül", "text": "Yes. She said she was really tired."},
        {"speaker": "Burak", "text": "Why? What's wrong?"},
        {"speaker": "Gül", "text": "She told me that her neighbours had a party until three in the morning."},
        {"speaker": "Burak", "text": "Poor Seda. Is she coming to the meeting?"},
        {"speaker": "Gül", "text": "She said she wanted to go home early, so I don't think so."}],
     "questions": [
        mc("Why was Seda tired?", ["She worked late.", "Her neighbours had a party.", "She was ill."], 1, "\"her neighbours had a party until three in the morning\""),
        mc("What did Seda want to do?", ["Go home early", "Go to the party", "Go to the meeting"], 0, "\"She said she wanted to go home early\""),
     ]},
    {"explanation": "**Dolaylı anlatım (reported speech)**, birinin söylediğini **onun kelimeleriyle değil**, kendi cümlemizle aktarmaktır.\n\n| Doğrudan | Dolaylı |\n|---|---|\n| Seda: \"I **am** tired.\" | Seda said (that) she **was** tired. |\n| Seda: \"I **want** to go home.\" | She told me (that) she **wanted** to go home. |\n\nAktarma fiili geçmişte olduğu için (said, told) **zaman bir adım geriye** gider: present simple → **past simple**, present continuous → **past continuous**.\n\n- \"I'm working.\" → He said he **was working**.\n\n**say mi tell mi?**\n\n| say | tell |\n|---|---|\n| say (that) ... | tell **+ kişi** (that) ... |\n| She **said** she was tired. | She **told me** she was tired. |\n| She said **to me** ... (az kullanılır) | ~~She told that...~~ |\n\n**that** günlük konuşmada genellikle atlanır.",
     "examples": [{"en": "He said he was hungry.", "tr": "Aç olduğunu söyledi."},
                  {"en": "She told us she lived in Ankara.", "tr": "Bize Ankara'da yaşadığını söyledi."},
                  {"en": "They said they were waiting for a taxi.", "tr": "Taksi beklediklerini söylediler."}],
     "turkishNote": "Türkçede \"Yorgun olduğunu söyledi\" derken zaman değişmez gibi görünür, ama İngilizcede said'den sonra zaman geriye kayar: \"She said she is tired\" yerine \"She said she was tired\". Ayrıca \"söylemek\" fiilinin iki karşılığı vardır: kişi varsa tell (told me), kişi yoksa say (said)."},
    [
        mc("She ___ me she was busy.", ["said", "told"], 1, "Kişi var → told."),
        mc("He ___ he was hungry.", ["said", "told"], 0, "Kişi yok → said."),
        mc("Hangisi yanlış?", ["She told that she was tired.", "She said that she was tired.", "She told me that she was tired."], 0, "tell + kişi zorunlu."),
        mc("\"I live in Izmir.\" → He said he ___ in Izmir.", ["lives", "lived", "is living"], 1, "Present → past."),
        gap("\"I'm cooking.\" → She said she ___ cooking.", ["was"], "am → was."),
        gap("\"We like it.\" → They said they ___ it.", ["liked"], "like → liked."),
        gap("He ___ us that he worked in a bank.", ["told"], "told + us."),
        order(["told", "She", "me", "she", "was", "tired"], "She told me she was tired.", "Özne + told + kişi + cümle.", "Bana yorgun olduğunu söyledi."),
        listen("I saw Murat yesterday. He said he was looking for a new job because he didn't like his manager.", "Murat neden yeni iş arıyor?", ["Maaşı düşük", "Müdürünü sevmiyor", "Şehir değiştiriyor"], 1, "\"he didn't like his manager\""),
        typ("Aktarın: Ayşe: \"I'm very happy.\"", variants("Ayşe said she was very happy.", "Ayşe said that she was very happy.", "She said she was very happy.", "She said that she was very happy."), "Ayşe said (that) she was very happy."),
    ],
    {"kind": "speaking", "task": speak("JAI size 5 kısa cümle söyleyecek (I'm hungry. I live near the sea. I'm learning Japanese...). Her birini önce said, sonra told me ile aktarın.",
                                       "You said you were hungry. You told me you lived near the sea. You said you were learning Japanese. You told me you didn't like cold weather.",
                                       ["said / told doğru", "Zaman kaydırma", "Zamir değişikliği (I → you/he/she)"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "Zaman geri gider", "Present perfect, past simple, will ve can içeren cümleleri doğru zaman kaydırmasıyla aktarabilirim.",
    {"kind": "text", "title": "Müşteri temsilcisinin notları", "body": "Call 1 – Mr Kaya\nMr Kaya said he had ordered a sofa three weeks ago, but it hadn't arrived. He told me he had called twice already. I explained that the delivery company would bring it on Friday.\n\nCall 2 – Ms Er\nMs Er said she couldn't log in to her account. She said she had tried five times. I told her I would send her a new password by email.\n\nCall 3 – Mr Tan\nMr Tan said he was very happy with his new washing machine. He said it was quieter than his old one and he would recommend us to his friends.",
     "questions": [
        mc("What was Mr Kaya's problem?", ["His sofa was broken.", "His sofa hadn't arrived.", "He wanted a refund."], 1, "\"he had ordered a sofa three weeks ago, but it hadn't arrived\""),
        mc("What did the customer service agent promise Ms Er?", ["A refund", "A new password by email", "A phone call"], 1, "\"I would send her a new password by email\""),
     ]},
    {"explanation": "**Zaman kaydırma tablosu:**\n\n| Doğrudan | Dolaylı |\n|---|---|\n| present simple: \"I **work**.\" | past simple: he said he **worked** |\n| present continuous: \"I'**m working**.\" | past continuous: he said he **was working** |\n| present perfect: \"I'**ve ordered** it.\" | past perfect: he said he **had ordered** it |\n| past simple: \"I **ordered** it.\" | past perfect: he said he **had ordered** it |\n| **will**: \"I'**ll** call.\" | **would**: she said she **would** call |\n| **can**: \"I **can't** log in.\" | **could**: she said she **couldn't** log in |\n| **am/is/are going to**: \"I'm going to stay.\" | **was/were going to**: he said he **was going to** stay |\n\n**Not:** Günlük konuşmada past simple bazen değişmeden kalabilir: He said he **ordered** it last week. ✓\n\n**Hâlâ doğru olan bilgiler** değişmeyebilir: She said she **lives** in Bursa. (Hâlâ orada yaşıyor.)",
     "examples": [{"en": "\"I've lost my keys.\" → She said she had lost her keys.", "tr": "Anahtarlarını kaybettiğini söyledi."},
                  {"en": "\"I'll help you.\" → He said he would help me.", "tr": "Bana yardım edeceğini söyledi."},
                  {"en": "\"I can swim.\" → She said she could swim.", "tr": "Yüzebildiğini söyledi."}],
     "turkishNote": "Türkçede \"Arayacağını söyledi\" (gelecek) ve \"Aradığını söyledi\" (geçmiş) diyerek zamanı ekle belirtiriz. İngilizcede will → would, past → past perfect kaydırması yapılır. \"He said he will call\" çok yaygın bir hatadır; doğrusu \"He said he would call\"."},
    [
        mc("\"I'll call you.\" → She said she ___ call me.", ["will", "would"], 1, "will → would."),
        mc("\"I can't come.\" → He said he ___ come.", ["can't", "couldn't"], 1, "can → could."),
        mc("\"I've finished.\" → She said she ___ finished.", ["has", "had"], 1, "present perfect → past perfect."),
        mc("\"I lost my phone.\" → He said he ___ his phone.", ["had lost", "has lost"], 0, "past → past perfect."),
        gap("\"I'm going to leave.\" → She said she ___ going to leave.", ["was"], "am going to → was going to."),
        gap("\"We'll be late.\" → They said they ___ be late.", ["would", "'d"], "will → would."),
        gap("\"I've never been to Rome.\" → He said he had never ___ to Rome.", ["been"], "had + V3."),
        gap("\"I can speak French.\" → She said she ___ speak French.", ["could"], "can → could."),
        listen("My brother called this morning. He said he had passed his driving test and he would drive us to the beach at the weekend!", "Kardeşi ne yapmış?", ["Ehliyet sınavını geçmiş", "Araba almış", "Plaja gitmiş"], 0, "\"he had passed his driving test\""),
        typ("Aktarın: Can: \"I'll pay you back tomorrow.\" (He said...)", variants("He said he would pay me back the next day.", "He said that he would pay me back the next day.", "He said he would pay me back the following day.", "He said he'd pay me back the next day.", "He said he would pay me back tomorrow.", "He said that he would pay me back the following day."), "He said he would pay me back the next day."),
    ],
    {"kind": "speaking", "task": speak("Son bir haftada biriyle yaptığınız telefon görüşmesini ya da mesajlaşmayı aktarın. Karşınızdakinin söylediği en az 5 şeyi will → would, can → could, present perfect → past perfect kaydırmalarıyla anlatın.",
                                       "My friend Elif called me on Sunday. She said she had found a new flat. She told me it was near the sea and she would move next month. She said she couldn't carry everything alone, so I said I would help her. She said she had already bought a new sofa!",
                                       ["Zaman kaydırma doğru", "said / told", "Akıcı aktarım"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "Burada, bugün, yarın", "Aktarırken zamirleri, zaman ve yer ifadelerini doğru şekilde değiştirebilirim.",
    {"kind": "dialogue", "title": "Kaçırılan mesaj", "lines": [
        {"speaker": "Tuna", "text": "Did Asya call? I was out all day yesterday."},
        {"speaker": "Mom", "text": "Yes, she called around five. She said she was at the station."},
        {"speaker": "Tuna", "text": "The station? Why?"},
        {"speaker": "Mom", "text": "She said she was leaving for Izmir that evening and she would be back the next week."},
        {"speaker": "Tuna", "text": "Oh no! Did she say anything else?"},
        {"speaker": "Mom", "text": "She told me she had left your book on the table there, at the café."}],
     "questions": [
        mc("Where was Asya when she called?", ["At home", "At the station", "At the café"], 1, "\"She said she was at the station.\""),
        mc("When will Asya be back?", ["The next day", "The next week", "That evening"], 1, "\"she would be back the next week\""),
     ]},
    {"explanation": "Aktarırken **kişi, yer ve zaman** değişebilir, çünkü konuşan ve zaman farklıdır.\n\n**Zamirler:**\n\n- Asya: \"**I** left **your** book.\" → She said **she** had left **my** book.\n\n**Zaman ve yer ifadeleri** (farklı bir zamanda / yerde aktarıyorsak):\n\n| Doğrudan | Dolaylı |\n|---|---|\n| today | **that day** |\n| tonight | **that night** |\n| tomorrow | **the next day** / the following day |\n| yesterday | **the day before** / the previous day |\n| next week | **the next week** / the following week |\n| last week | **the week before** |\n| now | **then** / at that time |\n| here | **there** |\n| this | **that** |\n| ago | **before** |\n\n**Aynı gün ve aynı yerde** aktarıyorsak değişmeyebilir:\n\n- (Bugün) Ali said he would come **tomorrow**. ✓",
     "examples": [{"en": "\"I saw him yesterday.\" → She said she had seen him the day before.", "tr": "Onu bir önceki gün gördüğünü söyledi."},
                  {"en": "\"I'm leaving tonight.\" → He said he was leaving that night.", "tr": "O gece gideceğini söyledi."},
                  {"en": "\"I'll meet you here.\" → She said she would meet me there.", "tr": "Benimle orada buluşacağını söyledi."}],
     "turkishNote": "Türkçede de \"yarın gelirim\" dediğini bir hafta sonra anlatırken \"ertesi gün geleceğini söyledi\" deriz; mantık aynıdır. Kendinize sorun: Konuşmayı aktardığım an ve yer, konuşmanın yapıldığı an ve yerle aynı mı? Değilse ifadeleri değiştirin."},
    [
        mc("\"tomorrow\" (bir hafta sonra aktarırken)", ["tomorrow", "the next day", "the day before"], 1, "tomorrow → the next day."),
        mc("\"yesterday\"", ["the day before", "the next day", "that day"], 0, "yesterday → the day before."),
        mc("\"here\"", ["there", "here", "that"], 0, "here → there."),
        mc("\"two weeks ago\"", ["two weeks before", "two weeks later", "two weeks ago"], 0, "ago → before."),
        gap("\"I'm busy today.\" → She said she was busy ___ day.", ["that"], "today → that day."),
        gap("\"I'll call you tonight.\" → He said he would call me that ___.", ["night", "evening"], "tonight → that night."),
        gap("\"I love your dress.\" → She said she loved ___ dress. (benim)", ["my"], "your → my."),
        gap("\"I saw her last week.\" → He said he had seen her the week ___.", ["before"], "last week → the week before."),
        listen("When I spoke to Kemal on Monday, he said he would finish the report the next day. But it's Friday now and I still haven't got it!", "Kemal raporu ne zaman bitireceğini söylemişti?", ["Pazartesi", "Salı (ertesi gün)", "Cuma"], 1, "Pazartesi konuştular, \"the next day\" = salı."),
        typ("Aktarın (bir hafta sonra): Deniz: \"I'll see you tomorrow.\"", variants("Deniz said she would see me the next day.", "Deniz said he would see me the next day.", "Deniz said they would see me the next day.", "Deniz said she would see me the following day.", "Deniz said he would see me the following day.", "Deniz said that she would see me the next day.", "Deniz said that he would see me the next day."), "Deniz said ... would see me the next day."),
    ],
    {"kind": "speaking", "task": speak("Geçen hafta biriyle yaptığınız bir konuşmayı aktarın. today, tomorrow, yesterday, here, this gibi ifadeleri dolaylı anlatıma uygun şekilde değiştirin (that day, the next day...). En az 5 cümle.",
                                       "Last Tuesday my boss called me into her office. She said she had read my report the day before. She told me she was very happy with it. She said there would be a meeting the next day and she wanted me to present it there. She also said I could leave early that day!",
                                       ["Zaman / yer ifadeleri değişti", "Zamirler doğru", "Zaman kaydırma"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Söz verdi, şikâyet etti", "explain, promise, complain, admit gibi aktarma fiilleriyle söylenenleri daha net aktarabilirim.",
    {"kind": "text", "title": "Apartman toplantısından notlar", "body": "Last night's building meeting was a long one.\n\nMrs Avcı complained that the lift had been out of order for two weeks. The building manager apologised and explained that the repair company was very busy. He promised that the lift would work again by Monday.\n\nMr Öz mentioned that some people were leaving rubbish bags in the corridor. Nobody admitted that they had done it, but everyone agreed that it was a problem.\n\nFinally, the manager announced that the building would get a new security camera next month. Everyone replied that it was a great idea.",
     "questions": [
        mc("What did Mrs Avcı complain about?", ["The rubbish", "The lift", "The camera"], 1, "\"the lift had been out of order\""),
        mc("What did the manager promise?", ["A new lift", "The lift would work again by Monday", "A new camera this week"], 1, "\"He promised that the lift would work again by Monday.\""),
     ]},
    {"explanation": "**said** yerine daha **anlamlı aktarma fiilleri** kullanmak anlatımı zenginleştirir. Hepsi **(that) + cümle** ile kullanılabilir.\n\n| Fiil | Anlam | Örnek |\n|---|---|---|\n| **explain** | açıklamak | He **explained that** the company was busy. |\n| **promise** | söz vermek | He **promised that** it would work by Monday. |\n| **complain** | şikâyet etmek | She **complained that** the lift was broken. |\n| **admit** | kabul / itiraf etmek | He **admitted that** he had forgotten. |\n| **agree** | katılmak | Everyone **agreed that** it was a problem. |\n| **mention** | bahsetmek | She **mentioned that** she was moving. |\n| **announce** | duyurmak | The manager **announced that** ... |\n| **reply** | cevap vermek | He **replied that** he didn't know. |\n\n**Dikkat:** explain **+ kişi** olmaz, **to + kişi** gerekir:\n\n- He explained **to me** that ... (~~He explained me~~)",
     "examples": [{"en": "She admitted that she had broken the glass.", "tr": "Bardağı kırdığını itiraf etti."},
                  {"en": "My son promised that he would tidy his room.", "tr": "Oğlum odasını toplayacağına söz verdi."},
                  {"en": "The teacher explained to us that the exam was easy.", "tr": "Öğretmen bize sınavın kolay olduğunu açıkladı."}],
     "turkishNote": "Türkçede \"Bana açıkladı\" dediğimiz için \"He explained me\" demek çok yaygın bir hatadır. explain fiilinden sonra kişi gelecekse to kullanılır: He explained to me. Aynı kural say için de geçerlidir: He said to me."},
    [
        mc("Hangisi doğru?", ["He explained me the problem.", "He explained the problem to me."], 1, "explain + to + kişi."),
        mc("\"I'll help you, I promise!\" → He ___ that he would help me.", ["complained", "promised", "admitted"], 1, "promise."),
        mc("\"OK, it was me. I ate the cake.\" → She ___ that she had eaten the cake.", ["admitted", "announced", "replied"], 0, "admit."),
        mc("\"The food is cold!\" → He ___ that the food was cold.", ["agreed", "complained", "promised"], 1, "complain."),
        gap("Everyone ___ that it was a good idea. (katıldı)", ["agreed"], "agree."),
        gap("She ___ that she was moving to Spain. (bahsetti)", ["mentioned"], "mention."),
        gap("The pilot ___ that we would land in ten minutes. (duyurdu)", ["announced"], "announce."),
        gap("He explained ___ us that the road was closed.", ["to"], "explain to."),
        listen("At the hotel reception, a guest complained that there was no hot water. The manager apologised and explained that a pipe was broken. He promised that it would work again by the evening.", "Müdür neye söz verdi?", ["Odayı değiştirmeye", "Suyun akşama kadar geleceğine", "Para iadesine"], 1, "\"He promised that it would work again by the evening.\""),
        typ("Aktarın: Elif: \"I'm sorry. I forgot your birthday.\" (admit)", variants("Elif admitted that she had forgotten my birthday.", "Elif admitted she had forgotten my birthday.", "She admitted that she had forgotten my birthday.", "She admitted she had forgotten my birthday.", "Elif admitted that she'd forgotten my birthday."), "Elif admitted (that) she had forgotten my birthday."),
    ],
    {"kind": "speaking", "task": speak("İş yerinizde, okulunuzda ya da apartmanınızda yapılan bir toplantıyı (gerçek ya da hayali) anlatın. Kimin ne söylediğini en az 5 farklı aktarma fiiliyle aktarın: complain, explain, promise, admit, agree, announce.",
                                       "At our team meeting last week, Ahmet complained that the office was too cold. The manager explained that the heating system was old. She promised that someone would fix it next month. Then Zehra admitted that she hadn't finished her part of the project. In the end, everyone agreed that we needed more time.",
                                       ["En az 5 aktarma fiili", "that + kaydırılmış zaman", "explain to doğru"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Mesajını ileteyim", "Telefon mesajlarını ve konuşmaları başkasına doğru ve özet bir şekilde aktarabilirim.",
    {"kind": "dialogue", "title": "Resepsiyonda", "lines": [
        {"speaker": "Receptionist", "text": "Good morning, Ms Uslu. You had two calls while you were out."},
        {"speaker": "Ms Uslu", "text": "Oh, thank you. Who called?"},
        {"speaker": "Receptionist", "text": "First, Mr Polat. He said he was going to be late for your meeting this afternoon. He explained that his flight was late."},
        {"speaker": "Ms Uslu", "text": "I see. And the other one?"},
        {"speaker": "Receptionist", "text": "Your daughter. She told me she had forgotten her keys and she would come here after school to get yours."},
        {"speaker": "Ms Uslu", "text": "Typical! Thanks for passing on the messages."}],
     "questions": [
        mc("Why will Mr Polat be late?", ["He's ill.", "His flight was delayed.", "He forgot the meeting."], 1, "\"He explained that his flight was late.\""),
        mc("What had Ms Uslu's daughter forgotten?", ["Her phone", "Her keys", "Her school bag"], 1, "\"she had forgotten her keys\""),
     ]},
    {"explanation": "**Mesaj almak:**\n\n- **Can I take a message?** (Mesaj bırakmak ister misiniz?)\n- **I'll pass on the message.** / I'll tell her you called.\n- **Could you tell him (that)** I called?\n\n**Mesajı aktarmak:**\n\n| Kalıp | Örnek |\n|---|---|\n| X called. **He said (that)** ... | Mr Polat called. He said he was going to be late. |\n| **She asked me to tell you (that)** ... | She asked me to tell you that she'd be here at four. |\n| **According to** X, ... | According to Ali, the meeting is cancelled. |\n| **Apparently**, ... | Apparently, the flight was delayed. |\n\n**Özetlemek:** Her kelimeyi aktarmak gerekmez. **Önemli bilgiyi** seçin:\n\n- \"Hi, it's Polat. Look, I'm really sorry, but my flight's late, and, you know, I won't be there until four.\"\n- → **He said** his flight was late **and** he **wouldn't** be there until four.",
     "examples": [{"en": "Your mum called. She said she would call back later.", "tr": "Annen aradı. Sonra tekrar arayacağını söyledi."},
                  {"en": "According to the weather forecast, it's going to snow.", "tr": "Hava durumuna göre kar yağacak."},
                  {"en": "He asked me to tell you that he's sorry.", "tr": "Senden özür dilediğini söylememi istedi."}],
     "turkishNote": "\"... söylememi istedi\" yapısı İngilizcede \"asked me to tell you\" ile kurulur. \"According to\" kalıbından sonra kişinin ya da kaynağın adı gelir; \"according to me\" denmez, kendi fikriniz için \"in my opinion\" kullanılır."},
    [
        mc("Telefonda: \"Mesaj bırakmak ister misiniz?\"", ["Can I take a message?", "Can I give a message?", "Do you want to say me?"], 0, "Can I take a message?"),
        mc("Kendi fikriniz için:", ["According to me, ...", "In my opinion, ..."], 1, "according to me denmez."),
        mc("\"... söylememi istedi\"", ["She wanted me say you...", "She asked me to tell you..."], 1, "asked me to tell you."),
        gap("I'll pass ___ the message.", ["on"], "pass on."),
        gap("___ to Ali, the meeting is at ten. (-e göre)", ["According"], "According to."),
        gap("Your dad called. He said he ___ (will) be late.", ["would", "'d"], "will → would."),
        gap("Could you ___ her that I called?", ["tell"], "tell + kişi."),
        order(["asked", "She", "me", "to", "tell", "you", "she", "was", "sorry"], "She asked me to tell you she was sorry.", "asked me to tell you + cümle.", "Senden özür dilediğini söylememi istedi."),
        listen("Hi, it's Leyla. Can you tell Okan that I can't come to dinner tonight? My son's ill. I'll call him tomorrow.", "Okan'a ne iletilmeli?", ["Leyla akşam yemeğine gelemeyecek", "Leyla geç kalacak", "Leyla'nın oğlu yemeğe gelecek"], 0, "\"I can't come to dinner tonight\""),
        typ("Mesajı aktarın: \"Hi, it's Mert. I'm stuck in traffic. I'll be there in twenty minutes.\" (Mert called. He said...)", variants("Mert called. He said he was stuck in traffic and he would be there in twenty minutes.", "Mert called. He said he was stuck in traffic and would be there in twenty minutes.", "Mert called. He said that he was stuck in traffic and he would be there in twenty minutes.", "Mert called. He said he was stuck in traffic and he'd be there in twenty minutes.", "Mert called. He said he was in traffic and he would be there in twenty minutes."), "Mert called. He said he was stuck in traffic and he would be there in twenty minutes."),
    ],
    {"kind": "writing", "task": write("Bir iş arkadaşınız bugün ofiste yoktu. Ona, gün içinde aldığınız 3 telefon mesajını ve toplantıda konuşulanları aktaran bir e-posta yazın (100–130 kelime). say, tell, explain, promise ve complain kullanın; zamanları ve zaman ifadelerini doğru kaydırın.",
                                      "Hi Ece,\n\nHere are your messages from today.\n\nFirst, Mr Demir called at ten. He said he had received your report and he was very happy with it. He promised that he would send the contract the next day.\n\nThen a customer, Ms Arslan, called. She complained that her order hadn't arrived. I told her you would call her back.\n\nYour sister called too. She said she couldn't pick you up after work.\n\nIn the meeting, the manager explained that the office would close early on Friday. She also announced that there would be a team lunch next week. Everyone agreed that it was a great idea!\n\nSee you tomorrow,\nKaan",
                                      ["Aktarma fiilleri çeşitli", "Zaman kaydırma doğru", "Zaman ifadeleri değişti", "Özet ve net mesajlar", "E-posta düzeni"])},
)

u.test([
    mc("She ___ me she was tired.", ["said", "told"], 1, "tell + kişi"),
    mc("He ___ he was hungry.", ["told", "said"], 1, "say"),
    mc("\"I'm busy.\" → She said she ___ busy.", ["is", "was"], 1, "am → was"),
    mc("\"I'll help.\" → He said he ___ help.", ["will", "would"], 1, "will → would"),
    mc("\"I can't swim.\" → She said she ___ swim.", ["can't", "couldn't"], 1, "can → could"),
    gap("\"I've lost my bag.\" → He said he ___ lost his bag.", ["had"], "past perfect"),
    gap("\"I saw it yesterday.\" → She said she had seen it the day ___.", ["before"], "yesterday → the day before"),
    gap("\"I'll come tomorrow.\" → He said he would come the ___ day.", ["next", "following"], "tomorrow → the next day"),
    mc("Hangisi doğru?", ["She explained me the rules.", "She explained the rules to me."], 1, "explain to"),
    mc("\"Yes, it was me. I broke it.\" → He ___ that he had broken it.", ["promised", "admitted"], 1, "admit"),
    gap("They ___ that the room was too small. (şikâyet ettiler)", ["complained"], "complain"),
    mc("\"I love your new car.\" → She said she loved ___ new car. (benim)", ["your", "my", "her"], 1, "your → my"),
    listen("My landlord called this morning. He said he was going to increase the rent next year, but he promised that he would repair the kitchen first.", "Ev sahibi neye söz verdi?", ["Kirayı artırmamaya", "Önce mutfağı tamir etmeye", "Yeni mobilya almaya"], 1, "\"he promised that he would repair the kitchen first\""),
    typ("Aktarın: Selim: \"I'm moving to Berlin next month.\" (He told me...)", variants("He told me he was moving to Berlin the next month.", "He told me that he was moving to Berlin the next month.", "He told me he was moving to Berlin the following month.", "He told me that he was moving to Berlin the following month.", "He told me he was moving to Berlin next month.", "He told me that he was moving to Berlin next month."), "He told me he was moving to Berlin the next month."),
    write("Son zamanlarda biriyle yaptığınız ilginç bir konuşmayı bir arkadaşınıza anlatan bir mesaj yazın (100–130 kelime). En az 6 dolaylı anlatım cümlesi, say / tell ve en az 3 farklı aktarma fiili (explain, promise, admit, complain, mention...) kullanın.",
          "You won't believe my conversation with Burcu yesterday! She told me she had quit her job. She explained that she had been unhappy there for a long time and she wanted to start her own business. She said she was going to open a small bakery near the university. She admitted that she was a bit scared, but she said she had saved enough money for a year. She mentioned that her brother would help her with the shop. I told her it was a brave decision. She promised that I would get the first cake for free! She said the bakery would open in March. I can't wait!",
          ["Zaman kaydırma doğru", "say / tell doğru", "Çeşitli aktarma fiilleri", "Zaman ifadeleri ve zamirler", "Akıcı anlatım"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

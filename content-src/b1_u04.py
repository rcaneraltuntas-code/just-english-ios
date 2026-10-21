"""B1 Ünite 4: Hayaller."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("B1", 4, "Hayaller", "Dreams and Dilemmas",
         "Hayali ya da gerçek dışı durumları second conditional ile anlatabilir, tavsiye verebilir, ikilemler hakkında ne yapacağımı tartışabilir ve gerçekçi ile hayali durumları ayırt edebilirim.",
         ["second conditional (if + past, would)", "If I were you, I'd ...", "first ve second conditional farkı", "would / could / might", "What would you do if ...?"],
         ["hayaller ve hedefler", "ikilemler", "ahlaki seçimler"],
         {"title": "Ya olsaydı?", "durationMinutes": 45,
          "goal": "Öğrenciler \"ikilem kartları\" çeker (sokakta para dolu bir cüzdan bulsan, en iyi arkadaşın kopya çekse...). What would you do if...? sorusuna second conditional ile cevap verip gerekçelerini tartışırlar. Ardından herkes tek bir hayalini If I could..., I'd... kalıbıyla anlatır ve sınıf en ilginç hayali oylar."})

u.vocab([
    ("dream", "hayal, rüya; hayal etmek", "My dream is to open a small hotel.", "Hayalim küçük bir otel açmak.", "dream of / about + -ing"),
    ("dilemma", "ikilem", "I'm in a real dilemma.", "Gerçekten bir ikilemdeyim.", None),
    ("win the lottery", "piyango kazanmak", "What would you do if you won the lottery?", "Piyango kazansan ne yapardın?", None),
    ("millionaire", "milyoner", "If I were a millionaire, I'd travel the world.", "Milyoner olsaydım dünyayı gezerdim.", None),
    ("give away", "dağıtmak, bağışlamak", "I'd give away half of the money.", "Paranın yarısını bağışlardım.", None),
    ("charity", "hayır kurumu", "She gives money to charity every month.", "Her ay hayır kurumuna para veriyor.", None),
    ("ambition", "hırs, büyük hedef", "Her ambition is to become a pilot.", "Büyük hedefi pilot olmak.", "ambitious (hırslı)"),
    ("achieve", "başarmak, ulaşmak", "You can achieve your goals.", "Hedeflerine ulaşabilirsin.", None),
    ("goal", "hedef", "My goal is to speak English fluently.", "Hedefim akıcı İngilizce konuşmak.", None),
    ("imagine", "hayal etmek, düşünmek", "Imagine you could fly.", "Uçabildiğini hayal et.", None),
    ("tell the truth", "doğruyu söylemek", "I'd always tell the truth.", "Her zaman doğruyu söylerdim.", None),
    ("tell a lie", "yalan söylemek", "Would you tell a lie to protect a friend?", "Bir arkadaşı korumak için yalan söyler miydin?", None),
    ("honest", "dürüst", "It's important to be honest.", "Dürüst olmak önemli.", "dishonest (dürüst olmayan)"),
    ("find", "bulmak", "If I found a wallet, I'd take it to the police.", "Bir cüzdan bulsam polise götürürdüm.", "find → found"),
    ("keep", "elinde tutmak, saklamak", "Would you keep the money?", "Parayı kendine saklar mıydın?", "keep → kept"),
    ("report", "bildirmek, şikâyet etmek", "I would report it to my manager.", "Müdürüme bildirirdim.", None),
    ("pretend", "-mış gibi yapmak", "I'd pretend I didn't see anything.", "Hiçbir şey görmemiş gibi yapardım.", None),
    ("risk", "risk; riske atmak", "I wouldn't risk my job.", "İşimi riske atmazdım.", None),
    ("chance", "şans, fırsat", "If I had the chance, I'd live abroad.", "Fırsatım olsa yurt dışında yaşardım.", None),
    ("famous", "ünlü", "If you were famous, what would you do?", "Ünlü olsan ne yapardın?", None),
    ("invisible", "görünmez", "If I were invisible for a day, I'd...", "Bir günlüğüne görünmez olsam...", None),
    ("in your shoes", "senin yerinde", "If I were in your shoes, I'd say no.", "Senin yerinde olsam hayır derdim.", None),
    ("I'd rather", "tercih ederim", "I'd rather stay at home.", "Evde kalmayı tercih ederim.", "I'd rather + yalın fiil"),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Piyango kazansan?", "Gerçek olmayan ya da çok düşük ihtimalli durumları second conditional ile anlatabilirim.",
    {"kind": "dialogue", "title": "Kahve molası", "lines": [
        {"speaker": "Cem", "text": "Did you buy a lottery ticket this week?"},
        {"speaker": "Aslı", "text": "No, I never do. But if I won the lottery, I'd quit my job immediately!"},
        {"speaker": "Cem", "text": "Really? I wouldn't. I'd get bored at home."},
        {"speaker": "Aslı", "text": "I wouldn't stay at home. I'd travel around South America for a year."},
        {"speaker": "Cem", "text": "And what would you do after that?"},
        {"speaker": "Aslı", "text": "I'd buy a house by the sea and I'd give some money to charity."}],
     "questions": [
        mc("Does Aslı buy lottery tickets?", ["Yes, every week.", "No, never."], 1, "\"No, I never do.\""),
        mc("Why wouldn't Cem quit his job?", ["He loves his boss.", "He'd get bored at home.", "He needs the money."], 1, "\"I'd get bored at home.\""),
     ]},
    {"explanation": "**Second conditional**, şu an **gerçek olmayan** ya da gelecekte **pek olası olmayan** hayali durumları anlatır.\n\n| If + **past simple** | , **would** ('d) + fiil |\n|---|---|\n| If I **won** the lottery, | I**'d quit** my job. |\n| If I **had** more time, | I**'d learn** the piano. |\n| If she **lived** near the sea, | she**'d swim** every day. |\n\nGeçmiş zaman kullanılır ama **anlam geçmiş değildir**: hayali bir şimdiki ya da gelecek durum.\n\n**Olumsuz:** would not → **wouldn't**\n\n- If I didn't have a car, I **wouldn't** go to work so easily.\n\n**Soru:** **What would** you **do if** you **won** a million?\n\n**Kısa cevap:** Would you ...? – Yes, I **would**. / No, I **wouldn't**.\n\nif'li kısımda **would kullanılmaz**: ~~If I would win~~",
     "examples": [{"en": "If I had a lot of money, I'd buy a farm.", "tr": "Çok param olsa bir çiftlik alırdım."},
                  {"en": "If we didn't live in the city, we'd have a big garden.", "tr": "Şehirde yaşamasaydık büyük bir bahçemiz olurdu."},
                  {"en": "What would you do if you lost your job?", "tr": "İşini kaybetsen ne yapardın?"}],
     "turkishNote": "Türkçede \"kazansam / kazansaydım ... yapardım\" yapısı second conditional'a denk gelir. \"-sa\" kısmı past simple, \"-ardım\" kısmı would + fiil olur. Türkçe konuşanlar bazen her iki tarafa da would koyar (\"If I would have money, I would buy\"); if kısmına would gelmez."},
    [
        mc("Hangisi doğru?", ["If I would win, I'd buy a house.", "If I won, I'd buy a house."], 1, "if + past simple."),
        mc("If I ___ more time, I'd learn to paint.", ["have", "had", "would have"], 1, "Hayali → had."),
        mc("If she lived in Paris, she ___ French.", ["will speak", "would speak", "speaks"], 1, "would + fiil."),
        gap("If I ___ (know) the answer, I'd tell you.", ["knew"], "know → knew."),
        gap("We'd go out more if we ___ (not have) kids.", ["didn't have", "did not have"], "Olumsuz past."),
        gap("What ___ you do if you found a lot of money?", ["would"], "What would you do...?"),
        gap("I ___ (not quit) my job if I won the lottery.", ["wouldn't quit", "would not quit"], "wouldn't + fiil."),
        order(["you", "would", "What", "do", "if", "you", "won", "the", "lottery", "?"], "What would you do if you won the lottery?", "What would you do if + past?", "Piyango kazansan ne yapardın?"),
        listen("If I had more money, I'd move to a bigger flat. But I don't, so I'm staying here for now.", "Konuşan neden daha büyük bir daireye taşınmıyor?", ["Yeterli parası yok", "Mevcut dairesini seviyor", "İşi yakın"], 0, "\"If I had more money... But I don't\""),
        typ("İngilizce yazın: \"Çok param olsa dünyayı gezerdim.\"", variants("If I had a lot of money, I'd travel the world.", "If I had a lot of money, I would travel the world.", "If I had lots of money, I'd travel the world.", "If I had a lot of money, I'd travel around the world.", "I'd travel the world if I had a lot of money.", "If I had a lot of money I'd travel the world.", "If I had lots of money, I would travel around the world."), "If I had a lot of money, I'd travel the world."),
    ],
    {"kind": "speaking", "task": speak("JAI size 5 hayali soru soracak (piyango kazansan, bir günlüğüne görünmez olsan, bir yıl tatil yapabilsen...). Her birine second conditional ile en az iki cümle cevap verin.",
                                       "If I won the lottery, I'd buy my parents a house. I wouldn't quit my job, but I'd work less. If I were invisible for a day, I'd go into the parliament and listen to the meetings!",
                                       ["if + past simple", "would / wouldn't + fiil", "if kısmında would yok"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "Senin yerinde olsam", "If I were you ile tavsiye verebilir, were kullanımını öğrenebilirim.",
    {"kind": "text", "title": "Okur mektubu: Ne yapmalıyım?", "body": "Dear Ask Ayla,\n\nA company in another city has offered me a great job. The salary is much better, but my girlfriend doesn't want to move. She has a good job here, and all her family is here too. I really don't know what to do. What would you do?\n\nEmre, 29\n\n\nDear Emre,\n\nThat's a hard situation. If I were you, I'd talk to her honestly before you make any decision. If the new job were only for a year or two, maybe she would agree. You could also ask the company about working from home some days. If I were in your shoes, I wouldn't say yes to the job until you've found a plan together.\n\nAyla",
     "questions": [
        mc("What is Emre's problem?", ["He lost his job.", "He has a job offer in another city.", "His girlfriend wants to move."], 1, "\"A company in another city has offered me a great job.\""),
        mc("What is Ayla's first piece of advice?", ["Take the job immediately", "Talk to his girlfriend honestly", "Find a new girlfriend"], 1, "\"I'd talk to her honestly\""),
     ]},
    {"explanation": "Second conditional'da **be** fiili için tüm kişilerde **were** kullanılabilir. Özellikle **If I were you** kalıbı sabittir.\n\n| Kalıp | Örnek |\n|---|---|\n| If I **were** you, I'd ... | If I were you, I'd take the job. |\n| If I **were** in your shoes, I'd ... | If I were in your shoes, I'd say no. |\n| If he **were** taller, ... | If he were taller, he'd play basketball. |\n\nGünlük dilde **If I / he / she was** de sık duyulur, ama **If I were you** kalıbı hep were ile kullanılır.\n\n**Tavsiye vermenin diğer yolları:**\n\n- **You could** ask your boss. (Seçenek önerme)\n- **Why don't you** talk to her?\n- **I wouldn't** do that **if I were you**.\n\n**Tavsiye istemek:**\n\n- **What would you do** (if you were me)?\n- **What should I do?**",
     "examples": [{"en": "If I were you, I'd see a doctor.", "tr": "Senin yerinde olsam doktora görünürdüm."},
                  {"en": "I wouldn't buy that car if I were you.", "tr": "Senin yerinde olsam o arabayı almazdım."},
                  {"en": "If it were cheaper, I'd buy it.", "tr": "Daha ucuz olsa alırdım."}],
     "turkishNote": "\"Senin yerinde olsam\" ifadesinin en doğal karşılığı \"If I were you\"dur. \"If I was you\" günlük konuşmada duyulsa da sınavlarda ve yazıda were tercih edilir. \"In your place\" çok resmî ve az kullanılır."},
    [
        mc("\"Senin yerinde olsam...\"", ["If I am you...", "If I were you...", "If I would be you..."], 1, "If I were you."),
        mc("If I were you, I ___ that job.", ["'ll take", "'d take", "took"], 1, "would + fiil."),
        mc("Hangisi doğru?", ["If it was cheaper, I'll buy it.", "If it were cheaper, I'd buy it."], 1, "were / would."),
        gap("If I ___ you, I'd call him. (be)", ["were"], "If I were you."),
        gap("I ___ (not) do that if I were you.", ["wouldn't", "would not"], "wouldn't."),
        gap("___ would you do if you were me?", ["What"], "What would you do...?"),
        gap("You ___ ask your manager for help. (seçenek önerme)", ["could"], "You could..."),
        mc("Tavsiye istemek:", ["What would you do?", "What will you do?"], 0, "Hayali → would."),
        listen("I've had a terrible toothache for three days. – Three days? If I were you, I'd go to the dentist today.", "Arkadaşının tavsiyesi ne?", ["Bugün dişçiye gitmesi", "İlaç alması", "Beklemesi"], 0, "\"I'd go to the dentist today\""),
        typ("İngilizce yazın: \"Senin yerinde olsam o arabayı almazdım.\"", variants("If I were you, I wouldn't buy that car.", "I wouldn't buy that car if I were you.", "If I were you, I would not buy that car.", "If I was you, I wouldn't buy that car.", "If I were you I wouldn't buy that car.", "I would not buy that car if I were you."), "If I were you, I wouldn't buy that car."),
    ],
    {"kind": "speaking", "task": speak("JAI size 4 sorununu anlatacak (uyuyamıyor, ev arkadaşı çok gürültülü, İngilizcesi ilerlemiyor, patronu ona fazla iş veriyor). Her biri için If I were you... ve You could... ile tavsiye verin.",
                                       "If I were you, I wouldn't drink coffee after 4 pm. You could also try reading before bed. If I were in your shoes, I'd talk to your flatmate calmly. And I wouldn't stay quiet if I were you. I'd tell my boss.",
                                       ["If I were you + would", "You could / Why don't you", "Nazik ve mantıklı tavsiyeler"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "Gerçek mi, hayal mi?", "First ve second conditional arasında ihtimale göre doğru seçimi yapabilirim.",
    {"kind": "dialogue", "title": "İki öğrenci", "lines": [
        {"speaker": "Bora", "text": "If I pass my exams, I'll go to Italy in the summer."},
        {"speaker": "Ece", "text": "That's a great plan! I'm sure you'll pass."},
        {"speaker": "Bora", "text": "What about you? Any plans?"},
        {"speaker": "Ece", "text": "Well, if I had enough money, I'd go to Japan. But I don't, so I'll probably work in my uncle's shop."},
        {"speaker": "Bora", "text": "If you work all summer, you'll save some money for next year."},
        {"speaker": "Ece", "text": "Exactly. And if I save enough, I'll go to Japan next summer!"}],
     "questions": [
        mc("Which plan is realistic?", ["Bora going to Italy", "Ece going to Japan this summer"], 0, "Bora: \"If I pass... I'll go\" (gerçekçi). Ece: \"if I had enough money\" (hayali)."),
        mc("What will Ece probably do this summer?", ["Go to Japan", "Work in her uncle's shop", "Study Italian"], 1, "\"I'll probably work in my uncle's shop\""),
     ]},
    {"explanation": "| First conditional | Second conditional |\n|---|---|\n| **Gerçekçi**, olabilir | **Hayali**, pek olası değil ya da gerçek dışı |\n| If + present, **will** | If + past, **would** |\n| If I **pass**, I**'ll go** to Italy. | If I **had** a million, I**'d go** to Japan. |\n| If it **rains**, we**'ll stay** in. | If I **were** a bird, I**'d fly**. |\n\n**Aynı durum, farklı ihtimal:**\n\n- If I **get** the job, I**'ll buy** a car. (İş görüşmem iyi geçti, büyük ihtimalle alırım.)\n- If I **got** the job, I**'d buy** a car. (Pek ihtimal vermiyorum.)\n\n**Kendinize sorun:** Bu olabilir mi? **Evet** → first. **Pek değil / imkânsız** → second.",
     "examples": [{"en": "If I see Deniz tomorrow, I'll give her the book.", "tr": "Yarın Deniz'i görürsem kitabı veririm."},
                  {"en": "If I lived in Norway, I'd see the northern lights.", "tr": "Norveç'te yaşasaydım kuzey ışıklarını görürdüm."},
                  {"en": "If you asked her, she'd probably say yes.", "tr": "Ona sorsan muhtemelen evet derdi."}],
     "turkishNote": "Türkçede \"kazanırsam\" (first) ile \"kazansam\" (second) arasındaki fark İngilizcede de vardır. \"-ırsam ... -ırım\" → first conditional; \"-sam ... -ırdım\" → second conditional. Bu eşleştirme çoğu durumda doğru seçimi yapmanıza yardım eder."},
    [
        mc("Gerçekçi: Yarın arkadaşınla buluşacaksın.", ["If I see him, I'll tell him.", "If I saw him, I'd tell him."], 0, "Olası → first."),
        mc("Hayali: Bir kuş olmak.", ["If I'm a bird, I'll fly.", "If I were a bird, I'd fly."], 1, "İmkânsız → second."),
        mc("\"Kazansam, alırdım.\"", ["If I win, I'll buy it.", "If I won, I'd buy it."], 1, "-sam / -ırdım → second."),
        mc("\"Kazanırsam, alırım.\"", ["If I win, I'll buy it.", "If I won, I'd buy it."], 0, "-ırsam / -ırım → first."),
        gap("If it ___ (rain) tomorrow, we'll stay at home.", ["rains"], "Olası → present."),
        gap("If I ___ (speak) Chinese, I'd work in Beijing.", ["spoke"], "Hayali → past."),
        gap("If you study hard, you ___ pass. (olası)", ["'ll", "will"], "First → will."),
        gap("If I were taller, I ___ play basketball. (hayali)", ["'d", "would"], "Second → would."),
        listen("If I finish work early today, I'll come to your party. But if I lived closer, I'd come to all your parties!", "Konuşan bugün partiye gelecek mi?", ["Kesin gelecek", "İşi erken biterse gelecek", "Hiç gelmeyecek"], 1, "\"If I finish work early today, I'll come\""),
        typ("İngilizce yazın: \"Norveç'te yaşasaydım kuzey ışıklarını görürdüm.\"", variants("If I lived in Norway, I'd see the northern lights.", "If I lived in Norway, I would see the northern lights.", "I'd see the northern lights if I lived in Norway.", "If I lived in Norway I'd see the northern lights.", "If I lived in Norway, I could see the northern lights."), "If I lived in Norway, I'd see the northern lights."),
    ],
    {"kind": "speaking", "task": speak("Bu yıl için 3 gerçekçi planınızı first conditional ile, 3 hayalinizi second conditional ile anlatın. Hangisinin hangisi olduğunu açıkça belli edin.",
                                       "If I save enough money, I'll go to Greece in August. If I pass my driving test, I'll buy a small car. If my team wins the league, I'll celebrate all night! But if I were rich, I'd have a house in every country. If I could speak ten languages, I'd work at the UN. And if I had wings, I'd fly to work!",
                                       ["First conditional doğru", "Second conditional doğru", "İhtimale göre doğru seçim"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Sen ne yapardın?", "Ahlaki ikilemleri tartışabilir, would / could / might ile seçeneklerimi anlatabilirim.",
    {"kind": "text", "title": "Anket: Sen ne yapardın?", "body": "We asked 500 people three difficult questions. Here are the results.\n\n1. If you found a wallet with 5,000 lira in the street, what would you do?\n72% said they would take it to the police. 18% said they might keep some of the money. 10% said they would keep it all.\n\n2. If your best friend cheated in an exam, would you tell the teacher?\nOnly 15% said yes. Most people said they would talk to their friend first.\n\n3. If you could read people's minds, would you do it?\n61% said no. As one person said: \"If I knew what everyone thought about me, I'd never leave the house!\"",
     "questions": [
        mc("What would most people do with the wallet?", ["Keep it", "Take it to the police", "Give it to charity"], 1, "\"72% said they would take it to the police.\""),
        mc("Would most people like to read minds?", ["Yes", "No"], 1, "\"61% said no.\""),
     ]},
    {"explanation": "Second conditional'ın sonuç kısmında would dışında başka modallar da kullanılabilir:\n\n| Modal | Anlam | Örnek |\n|---|---|---|\n| **would** | kesin hayali sonuç | I**'d** take it to the police. |\n| **might** | belki | I **might** keep some of the money. |\n| **could** | yapabilirdim (olanak) | If I had a car, I **could** drive you home. |\n\n**if kısmında could:** = was/were able to\n\n- **If I could** read minds, I'd know the truth. (Okuyabilseydim)\n\n**Fikir sormak ve tartışmak:**\n\n- **Would you** tell the teacher? – **It depends.** / I'm not sure.\n- **I'd probably** ... / **I don't think I'd** ...\n- **I'd rather** + fiil: I'd rather talk to my friend first. (… tercih ederdim)",
     "examples": [{"en": "If I saw someone stealing, I might call the police.", "tr": "Birinin çaldığını görsem polisi arayabilirdim."},
                  {"en": "If I could live anywhere, I'd live in Lisbon.", "tr": "İstediğim yerde yaşayabilsem Lizbon'da yaşardım."},
                  {"en": "I don't think I'd tell anyone.", "tr": "Kimseye söyleyeceğimi sanmıyorum."}],
     "turkishNote": "\"Söylemezdim sanırım\" için \"I think I wouldn't tell\" yerine \"I don't think I'd tell\" demek çok daha doğaldır. İngilizcede olumsuzluk genellikle think'e eklenir: I don't think I'd do that."},
    [
        mc("Belki: \"I ___ keep the money.\"", ["would", "might", "will"], 1, "Belki → might."),
        mc("If I had a car, I ___ drive you to the airport. (olanak)", ["could", "can", "will"], 0, "could."),
        mc("Daha doğal olan:", ["I think I wouldn't tell her.", "I don't think I'd tell her."], 1, "I don't think I'd..."),
        gap("If I ___ (could) fly, I'd go to Australia.", ["could"], "If I could..."),
        gap("Would you tell the teacher? – It ___. (duruma bağlı)", ["depends"], "It depends."),
        gap("I'd ___ talk to my friend first. (tercih ederdim)", ["rather"], "I'd rather."),
        gap("If you found a wallet, what ___ you do?", ["would"], "what would you do?"),
        match([("I'd", "yapardım"), ("I might", "belki yapardım"), ("I could", "yapabilirdim"), ("I wouldn't", "yapmazdım"), ("I'd rather", "tercih ederdim")], "Eşleştirin."),
        listen("If a shop assistant gave me too much change, I'd tell them. I wouldn't feel good if I kept it.", "Fazla para üstü alsa ne yapar?", ["Saklar", "Görevliye söyler", "Hayır kurumuna verir"], 1, "\"I'd tell them\""),
        typ("İngilizce yazın: \"İstediğim yerde yaşayabilsem Lizbon'da yaşardım.\"", variants("If I could live anywhere, I'd live in Lisbon.", "If I could live anywhere, I would live in Lisbon.", "I'd live in Lisbon if I could live anywhere.", "If I could live anywhere I'd live in Lisbon."), "If I could live anywhere, I'd live in Lisbon."),
    ],
    {"kind": "speaking", "task": speak("Anketteki üç soruya kendi cevabınızı verin ve gerekçenizi söyleyin. would, might, could, I'd rather ve It depends kalıplarını kullanın. JAI size zor bir ek soru soracak.",
                                       "If I found a wallet with 5,000 lira, I'd take it to the police. I wouldn't feel good if I kept it. If my best friend cheated, I don't think I'd tell the teacher. I'd rather talk to my friend first. If I could read minds, I might do it for one day, but not forever.",
                                       ["would / might / could", "Gerekçe sunma", "Doğal ifadeler (It depends, I'd rather)"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Hayalimdeki hayat", "Hayallerimi ve hedeflerimi anlatabilir, gerçekçi adımlarla hayali durumları bir arada kullanabilirim.",
    {"kind": "dialogue", "title": "Kariyer koçuyla", "lines": [
        {"speaker": "Coach", "text": "So, imagine anything was possible. What would your dream life look like?"},
        {"speaker": "Yasin", "text": "I'd live by the sea and I'd run my own restaurant."},
        {"speaker": "Coach", "text": "Lovely. What's stopping you?"},
        {"speaker": "Yasin", "text": "Money, mainly. And I don't have enough experience. If I had more experience, I'd feel more confident."},
        {"speaker": "Coach", "text": "OK. So what could you do this year to get closer to your goal?"},
        {"speaker": "Yasin", "text": "If I take a cooking course and work part-time in a kitchen, I'll learn a lot. That's a realistic first step."}],
     "questions": [
        mc("What is Yasin's dream?", ["To be a teacher", "To run his own restaurant by the sea", "To travel the world"], 1, "\"I'd live by the sea and I'd run my own restaurant.\""),
        mc("What is his realistic first step?", ["Buying a restaurant", "Taking a cooking course and working part-time in a kitchen", "Moving to the sea"], 1, "\"If I take a cooking course and work part-time in a kitchen\""),
     ]},
    {"explanation": "**Hayalleri anlatmak:**\n\n- **My dream is to** + fiil: My dream is to run a restaurant.\n- **I've always dreamed of** + -ing: I've always dreamed of living abroad.\n- **I'd love to** + fiil: I'd love to learn to sail.\n- **Imagine** + hayali durum: Imagine you had no job. What would you do?\n\n**Hayal (second) → gerçekçi adım (first):**\n\n| Hayal | Adım |\n|---|---|\n| If I **had** more experience, I**'d feel** more confident. | If I **take** a course, I**'ll learn** a lot. |\n| If I **spoke** perfect English, I**'d work** abroad. | If I **practise** every day, I**'ll improve**. |\n\n**Engelleri anlatmak:**\n\n- **What's stopping me is** ...\n- **The problem is that** ...\n- **I'm not ready yet**, but ...",
     "examples": [{"en": "I've always dreamed of having a house with a garden.", "tr": "Hep bahçeli bir evim olsun istedim."},
                  {"en": "I'd love to write a novel one day.", "tr": "Bir gün bir roman yazmayı çok isterim."},
                  {"en": "What's stopping me is fear.", "tr": "Beni durduran şey korku."}],
     "turkishNote": "\"I'd love to\" (çok isterim) ile \"I love to\" (yapmayı severim) farklıdır. \"I'd love to go to Japan\" bir isteği, \"I love going to the cinema\" ise bir alışkanlığı anlatır. \"dream of\" kalıbında of'tan sonra fiil -ing alır."},
    [
        mc("\"Japonya'ya gitmeyi çok isterim.\"", ["I love to go to Japan.", "I'd love to go to Japan."], 1, "İstek → I'd love to."),
        mc("I've always dreamed ___ living abroad.", ["to", "of", "for"], 1, "dream of + -ing."),
        mc("My dream is ___ my own business.", ["start", "to start", "starting of"], 1, "My dream is to..."),
        gap("I've always dreamed of ___ (have) a big family.", ["having"], "of + -ing."),
        gap("___ you had no job. What would you do? (hayal et)", ["Imagine"], "Imagine..."),
        gap("What's ___ me is money. (durduran)", ["stopping"], "What's stopping me..."),
        mc("Gerçekçi adım:", ["If I practise every day, I'll improve.", "If I practised every day, I'd improve."], 0, "Gerçekçi plan → first."),
        order(["I'd", "to", "love", "write", "a", "novel", "one", "day"], "I'd love to write a novel one day.", "I'd love to + fiil.", "Bir gün bir roman yazmayı çok isterim."),
        listen("I've always dreamed of being a vet. If I were younger, I'd go back to university. But I'll volunteer at an animal shelter next month. It's a start!", "Konuşan gelecek ay ne yapacak?", ["Üniversiteye dönecek", "Bir hayvan barınağında gönüllü çalışacak", "Veteriner olacak"], 1, "\"I'll volunteer at an animal shelter next month\""),
        typ("İngilizce yazın: \"Hep bahçeli bir evim olsun istedim.\" (dream of)", variants("I've always dreamed of having a house with a garden.", "I have always dreamed of having a house with a garden.", "I've always dreamt of having a house with a garden.", "I've always dreamed of having a house with a garden"), "I've always dreamed of + having..."),
    ],
    {"kind": "writing", "task": write("\"Hayalimdeki hayat\" başlıklı bir paragraf yazın (120–150 kelime). Hayalinizi second conditional ile anlatın, sizi durduran engelleri söyleyin ve bu yıl atabileceğiniz gerçekçi adımları first conditional ile yazın. dream of, I'd love to ve If I were... kullanın.",
                                      "I've always dreamed of living in a small village in Italy. If I lived there, I'd wake up early, walk to the market and buy fresh bread. I'd love to grow my own vegetables, and I'd paint in the afternoons. If I were braver, I'd move tomorrow! What's stopping me is my job and, of course, money. I also don't speak Italian. But I can start now. If I take an Italian course this year, I'll be able to talk to people when I visit. If I save a little every month, I'll go to Italy for a long holiday next summer. Maybe one day my dream will come true.",
                                      ["Second conditional ile hayal", "First conditional ile gerçekçi adımlar", "dream of / I'd love to", "Engelleri anlatma", "Düzenli paragraf"])},
)

u.test([
    mc("Hangisi doğru?", ["If I would have money, I'd travel.", "If I had money, I'd travel."], 1, "if + past"),
    mc("If I ___ you, I'd say sorry.", ["am", "were", "will be"], 1, "If I were you"),
    mc("If she knew the answer, she ___ tell us.", ["will", "would", "does"], 1, "would"),
    mc("Gerçekçi: \"If it ___ tomorrow, we'll cancel the match.\"", ["rains", "rained"], 0, "First"),
    mc("Hayali: \"If I ___ invisible, I'd visit the museum at night.\"", ["am", "were"], 1, "Second"),
    gap("What would you do if you ___ (lose) your phone?", ["lost"], "past"),
    gap("I ___ (not) tell anyone if I were you.", ["wouldn't", "would not"], "wouldn't"),
    gap("If I had a car, I ___ drive you home. (olanak)", ["could"], "could"),
    mc("Daha doğal:", ["I think I wouldn't go.", "I don't think I'd go."], 1, "I don't think I'd..."),
    mc("I've always dreamed ___ being a pilot.", ["of", "to"], 0, "dream of"),
    gap("I'd ___ to visit Peru one day. (çok isterim)", ["love", "like"], "I'd love to"),
    mc("\"Gidersem görürüm.\"", ["If I go, I'll see it.", "If I went, I'd see it."], 0, "-ırsam → first"),
    listen("If I could change one thing about my city, I'd add more parks. If the mayor listens to us, maybe they'll build one next year.", "Konuşan şehrinde neyi değiştirmek isterdi?", ["Daha fazla park", "Daha az trafik", "Daha çok müze"], 0, "\"I'd add more parks\""),
    typ("İngilizce yazın: \"Senin yerinde olsam doktora giderdim.\"", variants("If I were you, I'd go to the doctor.", "If I were you, I would go to the doctor.", "If I were you, I'd see a doctor.", "I'd go to the doctor if I were you.", "If I was you, I'd go to the doctor.", "If I were you I'd go to the doctor.", "If I were you, I would see a doctor."), "If I were you, I'd go to the doctor."),
    write("\"Bir yıllığına istediğin her şeyi yapabilseydin ne yapardın?\" sorusuna cevap verin (120–150 kelime). Second conditional (would, could, might), If I were..., I'd love to ve en az bir gerçekçi plan (first conditional) kullanın.",
          "If I could do anything for a year, I'd travel around the world. First, I'd go to South America. I'd love to see Machu Picchu and the Amazon. Then I might spend a few months in Asia. If I had enough time, I'd learn to cook Thai food in Bangkok. I'd also volunteer for a charity, because I'd like to help people too. If I were braver, I'd try skydiving! Of course, I can't do this now because I have a job. But if I save money for the next three years, I'll take a long trip in 2030. I don't think I'd stay away for a whole year, but six months would be amazing.",
          ["Second conditional (would / could / might)", "If I were...", "First conditional ile gerçekçi plan", "Hayal kelimeleri", "Akıcı paragraf"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

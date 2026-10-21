"""B1 Ünite 3: Kararlar."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("B1", 3, "Kararlar", "Decisions",
         "Gerçekçi gelecek durumların sonuçlarını first conditional ile anlatabilir, para ve alışveriş kararları hakkında konuşabilir, when / unless / as soon as ile koşul ve zaman bildirebilirim.",
         ["first conditional (if + present, will)", "if / when farkı", "unless", "as soon as / until / before / after (gelecek)", "koşul cümlelerinde may / might / could / imperative"],
         ["para", "alışveriş", "bütçe ve tasarruf"],
         {"title": "Ne yapacaksın?", "durationMinutes": 45,
          "goal": "Öğrenciler küçük gruplarda bir aylık sınırlı bir bütçeyle karar vermeleri gereken senaryolar alır (yeni telefon mu, tatil mi, birikim mi). If..., I'll... / Unless..., ... / As soon as... kalıplarıyla seçeneklerin sonuçlarını tartışır ve grup olarak ortak bir karar verip gerekçesiyle sunarlar."})

u.vocab([
    ("afford", "(parası) yetmek, karşılayabilmek", "I can't afford a new car.", "Yeni bir arabaya param yetmez.", "can / can't afford"),
    ("save (money)", "biriktirmek", "I'm saving for a holiday.", "Tatil için para biriktiriyorum.", "save up for"),
    ("waste (money)", "(para) israf etmek", "Don't waste your money on that.", "Paranı ona harcama.", None),
    ("spend ... on", "... -e harcamak", "How much do you spend on food?", "Yemeğe ne kadar harcıyorsun?", "spend → spent"),
    ("budget", "bütçe", "We need to stick to our budget.", "Bütçemize sadık kalmalıyız.", None),
    ("borrow", "ödünç almak", "Can I borrow ten pounds?", "On sterlin ödünç alabilir miyim?", "Sen benden → borrow"),
    ("lend", "ödünç vermek", "I'll lend you some money.", "Sana biraz para ödünç veririm.", "lend → lent; Ben sana → lend"),
    ("owe", "borçlu olmak", "You owe me twenty euros.", "Bana yirmi avro borçlusun.", None),
    ("pay back", "(borcu) geri ödemek", "I'll pay you back tomorrow.", "Yarın sana geri öderim.", None),
    ("bargain", "kelepir, kapış kapış", "This jacket was a real bargain.", "Bu ceket tam bir kelepirdi.", None),
    ("discount", "indirim", "Students get a 10% discount.", "Öğrenciler %10 indirim alır.", None),
    ("on sale", "indirimde", "These shoes are on sale.", "Bu ayakkabılar indirimde.", None),
    ("refund", "para iadesi", "Can I get a refund?", "Paramı geri alabilir miyim?", None),
    ("receipt", "fiş, makbuz", "Keep the receipt in case you need to return it.", "İade etmen gerekirse diye fişi sakla.", "p okunmaz: /rɪˈsiːt/"),
    ("return", "iade etmek", "I want to return this shirt.", "Bu gömleği iade etmek istiyorum.", None),
    ("in debt", "borç içinde", "He's been in debt for years.", "Yıllardır borç içinde.", None),
    ("cash", "nakit", "Do you take cash?", "Nakit alıyor musunuz?", None),
    ("by card", "kartla", "Can I pay by card?", "Kartla ödeyebilir miyim?", None),
    ("worth it", "değer, buna değer", "It's expensive, but it's worth it.", "Pahalı ama buna değer.", None),
    ("unless", "-medikçe, -mezse", "I won't buy it unless it's on sale.", "İndirimde olmadıkça almam.", "= if ... not"),
    ("as soon as", "-ir -mez, -dığı anda", "I'll call you as soon as I arrive.", "Varır varmaz seni ararım.", None),
    ("make up your mind", "karar vermek", "I can't make up my mind.", "Karar veremiyorum.", None),
    ("on the one hand ... on the other hand", "bir yandan ... öte yandan", "On the one hand it's cheap; on the other hand it's slow.", "Bir yandan ucuz, öte yandan yavaş.", None),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Eğer olursa...", "Gerçekçi bir gelecek durumu ve sonucunu first conditional ile anlatabilirim.",
    {"kind": "dialogue", "title": "Telefon dükkânında", "lines": [
        {"speaker": "Selin", "text": "I love this phone, but it's so expensive."},
        {"speaker": "Kaan", "text": "If you buy it today, you'll get a free case."},
        {"speaker": "Selin", "text": "Hmm. But if I spend that much, I won't have money for my holiday."},
        {"speaker": "Kaan", "text": "What about the older model? It's on sale."},
        {"speaker": "Selin", "text": "If it has a good camera, I'll think about it."},
        {"speaker": "Kaan", "text": "It does. And if you don't like it, you can return it in fourteen days."}],
     "questions": [
        mc("What will Selin get if she buys the phone today?", ["A discount", "A free case", "A free holiday"], 1, "\"you'll get a free case\""),
        mc("What is Selin worried about?", ["She won't have money for her holiday.", "The phone is too old.", "The shop closes soon."], 0, "\"I won't have money for my holiday\""),
     ]},
    {"explanation": "**First conditional**, gelecekte **gerçekleşmesi mümkün** bir durumu ve onun **olası sonucunu** anlatır.\n\n| If + **present simple** | , **will** + fiil |\n|---|---|\n| If it **rains**, | I**'ll stay** at home. |\n| If you **buy** it today, | you**'ll get** a free case. |\n| If I **don't save**, | I **won't have** enough money. |\n\n**Sıra değişebilir.** Sonuç başta gelirse virgül kullanılmaz:\n\n- I**'ll stay** at home **if** it **rains**.\n\n**Soru:** What **will** you **do if** they **don't give** you a refund?\n\n**Önemli:** if'li kısımda **will kullanılmaz**:\n\n- **If** it **rains** tomorrow... (~~If it will rain~~)",
     "examples": [{"en": "If we leave now, we'll catch the bus.", "tr": "Şimdi çıkarsak otobüsü yakalarız."},
                  {"en": "You'll feel better if you get some sleep.", "tr": "Biraz uyursan daha iyi hissedersin."},
                  {"en": "What will you do if you don't get the job?", "tr": "İşi alamazsan ne yapacaksın?"}],
     "turkishNote": "Türkçede \"Yarın yağmur yağarsa\" derken -ar/-er eki geleceği de kapsar; bu yüzden Türkçe konuşanlar sık sık \"If it will rain tomorrow\" der. İngilizcede if'ten sonra gelecek anlamı için de present simple kullanılır: If it rains tomorrow, I'll stay at home."},
    [
        mc("Hangisi doğru?", ["If it will rain, I'll stay home.", "If it rains, I'll stay home."], 1, "if + present simple."),
        mc("If you ___ hard, you'll pass the exam.", ["study", "will study", "studied"], 0, "if + present."),
        mc("If she misses the bus, she ___ late.", ["is", "will be", "would be"], 1, "Sonuç → will."),
        gap("If I ___ (not save) money, I won't go on holiday.", ["don't save", "do not save"], "Olumsuz present."),
        gap("We ___ (miss) the train if we don't hurry.", ["'ll miss", "will miss"], "will + fiil."),
        gap("What ___ you do if they say no?", ["will"], "What will you do if...?"),
        mc("Virgül doğru olan:", ["I'll call you, if I'm late.", "If I'm late, I'll call you."], 1, "if başta → virgül."),
        order(["you", "If", "buy", "two", "you'll", "get", "one", "free"], "If you buy two, you'll get one free.", "If + present, will + fiil.", "İki tane alırsan bir tane bedava alırsın."),
        listen("If the weather's nice on Saturday, we'll have a picnic. But if it rains, we'll go to the cinema instead.", "Yağmur yağarsa ne yapacaklar?", ["Piknik", "Sinemaya gidecekler", "Evde kalacaklar"], 1, "\"if it rains, we'll go to the cinema instead\""),
        typ("İngilizce yazın: \"Şimdi çıkarsak otobüsü yakalarız.\"", variants("If we leave now, we'll catch the bus.", "If we leave now, we will catch the bus.", "We'll catch the bus if we leave now.", "If we go now, we'll catch the bus.", "If we leave now we'll catch the bus."), "If we leave now, we'll catch the bus."),
    ],
    {"kind": "speaking", "task": speak("JAI size \"What will you do if...?\" diye 5 soru soracak (yarın tatil olursa, bir zam alırsan, telefonun bozulursa...). Her birine first conditional ile cevap verin ve bir sonuç daha ekleyin.",
                                       "If tomorrow is a holiday, I'll sleep late and I'll meet my friends for breakfast. If I get a pay rise, I'll save half of it. If my phone breaks, I won't buy a new one immediately. I'll repair it first.",
                                       ["if + present simple", "will / won't doğru", "if kısmında will yok"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "Para konuşmaları", "Para ödünç alma, borç, tasarruf ve bütçe hakkında konuşabilirim.",
    {"kind": "text", "title": "Öğrenci bütçesi: 5 altın kural", "body": "1. Make a budget. If you know how much you spend on food, transport and fun every month, you'll find it easier to save.\n\n2. Don't borrow money from friends unless it's an emergency. If you borrow, pay it back quickly.\n\n3. Cook at home. If you eat out every day, you'll waste hundreds every month.\n\n4. Always ask about student discounts. Many cinemas, museums and shops offer them.\n\n5. Before you buy something expensive, wait 48 hours. If you still want it after two days, it's probably worth it.",
     "questions": [
        mc("According to the text, when is it OK to borrow from friends?", ["Every month", "Only in an emergency", "Never"], 1, "\"unless it's an emergency\""),
        mc("What should you do before buying something expensive?", ["Ask a friend", "Wait 48 hours", "Pay by card"], 1, "\"wait 48 hours\""),
     ]},
    {"explanation": "**borrow mu lend mi?**\n\n| Fiil | Anlam | Örnek |\n|---|---|---|\n| **borrow** (from) | ödünç **almak** | Can I **borrow** your pen? / I borrowed money **from** my sister. |\n| **lend** (to) | ödünç **vermek** | Can you **lend** me your pen? / She lent money **to** me. |\n| **owe** | borçlu olmak | I **owe** you 20 lira. |\n| **pay back** | geri ödemek | I'll **pay** you **back** on Friday. |\n\n**spend / waste / save:**\n\n- **spend** money **on** something: I spend a lot **on** clothes.\n- **waste** money **on** something: Don't waste money **on** junk food.\n- **save** (up) **for** something: I'm saving **for** a new laptop.\n\n**afford:**\n\n- I **can't afford** a new car. / I **can't afford to** go on holiday.\n\n**First conditional + imperative:** Tavsiyede sonuç kısmında emir kipi kullanılabilir.\n\n- **If** you borrow money, **pay** it back quickly.",
     "examples": [{"en": "Could you lend me your car this weekend?", "tr": "Bu hafta sonu arabanı bana ödünç verebilir misin?"},
                  {"en": "How much do I owe you?", "tr": "Sana ne kadar borçluyum?"},
                  {"en": "If you need money, ask me first.", "tr": "Paraya ihtiyacın olursa önce bana sor."}],
     "turkishNote": "Türkçede \"ödünç almak\" ve \"ödünç vermek\" tek bir kelimeyle (ödünç) kurulduğu için borrow ve lend sık karıştırılır. \"Can you borrow me...\" yanlıştır; doğrusu \"Can you lend me...?\" ya da \"Can I borrow...?\" olur."},
    [
        mc("Arkadaşınızdan kalem istiyorsunuz:", ["Can you borrow me your pen?", "Can I borrow your pen?"], 1, "Ben alıyorum → borrow."),
        mc("Kardeşim bana para verdi, geri vereceğim:", ["My brother lent me some money.", "My brother borrowed me some money."], 0, "O veriyor → lend."),
        mc("I spend too much money ___ coffee.", ["for", "on", "in"], 1, "spend on."),
        mc("I'm saving ___ a new bike.", ["for", "on", "to"], 0, "save for."),
        gap("I can't ___ a holiday this year. (parası yetmek)", ["afford"], "can't afford."),
        gap("You ___ me fifty lira. (borçlusun)", ["owe"], "owe."),
        gap("I'll pay you ___ next week.", ["back"], "pay back."),
        gap("If you need help, ___ me. (call → emir)", ["call", "ask", "tell", "phone"], "if + imperative."),
        listen("Can you lend me twenty euros? I left my wallet at home. – Sure. – Thanks, I'll pay you back as soon as we get home.", "Konuşan neden para istiyor?", ["Cüzdanını evde unuttu", "Kartı çalışmıyor", "Bütçesi bitti"], 0, "\"I left my wallet at home\""),
        typ("İngilizce yazın: \"Bana biraz para ödünç verebilir misin?\"", variants("Can you lend me some money?", "Could you lend me some money?", "Can you lend me a bit of money?", "Could you lend me a little money?"), "Can you lend me some money?"),
    ],
    {"kind": "speaking", "task": speak("Para alışkanlıklarınızı anlatın: neye çok harcıyorsunuz, ne için biriktiriyorsunuz, neye paranız yetmiyor? Sonra bir arkadaşa para tavsiyesi verin: If you..., ... (en az 3 tavsiye, birinde emir kipi).",
                                       "I spend too much on coffee and taxis. I'm saving for a trip to Japan, but I can't afford it yet. My advice: if you want to save, make a budget. If you eat at home, you'll save a lot. And if you borrow money, pay it back quickly.",
                                       ["borrow / lend doğru", "spend on / save for", "Conditional + imperative"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "Olmadıkça", "unless ile koşul bildirebilir, if ve when arasındaki farkı ayırt edebilirim.",
    {"kind": "dialogue", "title": "Hafta sonu planı", "lines": [
        {"speaker": "Arda", "text": "Shall we go to the outlet centre on Saturday?"},
        {"speaker": "Melis", "text": "Only if they have good discounts. I won't buy anything unless it's at least 30% off."},
        {"speaker": "Arda", "text": "Fair enough. When we get there, let's have lunch first."},
        {"speaker": "Melis", "text": "Good idea. And unless we leave early, the car park will be full."},
        {"speaker": "Arda", "text": "OK, I'll pick you up at nine. If I'm late, I'll text you."},
        {"speaker": "Melis", "text": "Don't be late this time!"}],
     "questions": [
        mc("When will Melis buy something?", ["Only if it's at least 30% off", "Only if Arda pays", "Only after lunch"], 0, "\"unless it's at least 30% off\""),
        mc("What will happen unless they leave early?", ["The shops will close.", "The car park will be full.", "They will miss lunch."], 1, "\"unless we leave early, the car park will be full\""),
     ]},
    {"explanation": "**unless = if ... not** (-medikçe, -mezse)\n\n| unless | if ... not |\n|---|---|\n| I won't go **unless** you come. | I won't go **if** you **don't** come. |\n| **Unless** we leave now, we'll be late. | **If** we **don't** leave now, we'll be late. |\n\nunless'tan sonra fiil **olumlu** kalır (anlam zaten olumsuz):\n\n- **Unless** it **rains**... (~~Unless it doesn't rain~~)\n\n**if mi when mi?**\n\n| if | when |\n|---|---|\n| **Belki** olur, belki olmaz. | **Kesin** olacak, zamanı belli. |\n| **If** I see Ali, I'll tell him. (Görebilirim, görmeyebilirim.) | **When** I see Ali, I'll tell him. (Görüşeceğiz.) |\n| **If** I get the job, I'll celebrate. | **When** I get home, I'll call you. |\n\nİkisinden sonra da **present simple** kullanılır.",
     "examples": [{"en": "You won't get a refund unless you have the receipt.", "tr": "Fişin olmadıkça para iadesi alamazsın."},
                  {"en": "When I get paid, I'll pay you back.", "tr": "Maaşımı alınca sana geri öderim."},
                  {"en": "If I have time, I'll help you.", "tr": "Vaktim olursa sana yardım ederim."}],
     "turkishNote": "Türkçede \"-ince\" (when) ve \"-se\" (if) farklı eklerdir; bu farkı İngilizcede de koruyun. \"When I will get home\" yanlıştır, doğrusu \"When I get home\". unless cümlesine ayrıca \"not\" eklemeyin; çift olumsuz olur."},
    [
        mc("\"unless\" = ?", ["if", "if ... not", "when"], 1, "unless = if not."),
        mc("Hangisi doğru?", ["Unless it doesn't rain, we'll go.", "Unless it rains, we'll go."], 1, "unless + olumlu fiil."),
        mc("Kesin olacak bir durum: \"___ I get home, I'll call you.\"", ["If", "When"], 1, "Kesin → when."),
        mc("Belirsiz bir durum: \"___ I win the competition, I'll buy a car.\"", ["If", "When"], 0, "Belki → if."),
        gap("I won't come ___ you invite me. (davet etmedikçe)", ["unless"], "unless."),
        gap("You can't return it unless you ___ the receipt.", ["have"], "unless + present."),
        gap("When I ___ (finish) work, I'll meet you.", ["finish"], "when + present."),
        typ("unless ile yeniden yazın: \"If you don't hurry, you'll miss the train.\"", variants("Unless you hurry, you'll miss the train.", "Unless you hurry, you will miss the train.", "You'll miss the train unless you hurry.", "You will miss the train unless you hurry."), "Unless you hurry, you'll miss the train."),
        listen("I never buy clothes online unless I know the brand. When I order something, I always check the return policy first.", "Konuşan ne zaman internetten kıyafet alır?", ["Markayı tanıyorsa", "İndirim varsa", "Hiç almaz"], 0, "\"unless I know the brand\""),
        order(["get", "When", "I", "paid", "I'll", "pay", "you", "back"], "When I get paid, I'll pay you back.", "When + present, will.", "Maaşımı alınca sana geri öderim."),
    ],
    {"kind": "speaking", "task": speak("Alışveriş kurallarınızı anlatın: Neyi asla almazsınız... unless...? Sonra bugün ve bu hafta kesin yapacağınız 2 şeyi when ile, belki olacak 2 şeyi if ile söyleyin.",
                                       "I never buy shoes unless I try them on. I don't buy expensive things unless I really need them. When I get home tonight, I'll cook dinner. When I see my mum on Sunday, I'll give her the present. If I have time, I'll go to the gym. If my friend calls, we'll go out.",
                                       ["unless + olumlu fiil", "if / when doğru seçimi", "when / if sonrası present"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Olur olmaz", "as soon as, until, before, after ile gelecekteki olayların sırasını anlatabilirim.",
    {"kind": "text", "title": "İade süreci", "body": "How to return an item to OnlineShop:\n\nAs soon as you receive your order, check that everything is OK.\n\nIf you want to return something, keep it in its original box until you send it back.\n\nBefore you post it, print the return label from your account.\n\nAfter we receive the item, we'll check it. As soon as we've checked it, we'll send you an email.\n\nYou won't get your refund until we confirm the return. Most refunds take 5 to 7 days.",
     "questions": [
        mc("What should you do before you post the item?", ["Call the shop", "Print the return label", "Open the box"], 1, "\"Before you post it, print the return label\""),
        mc("When will you get your refund?", ["As soon as you post it", "After they confirm the return", "Before they receive it"], 1, "\"You won't get your refund until we confirm the return.\""),
     ]},
    {"explanation": "Geleceği anlatırken şu bağlaçlardan sonra da **present simple** kullanılır (will değil):\n\n| Bağlaç | Anlam | Örnek |\n|---|---|---|\n| **as soon as** | -ir -mez | I'll call you **as soon as** I **arrive**. |\n| **until** | -e kadar | I'll wait here **until** you **come** back. |\n| **before** | -meden önce | **Before** you **leave**, turn off the lights. |\n| **after** | -dikten sonra | **After** I **finish** work, I'll go shopping. |\n| **when** | -ince | **When** she **calls**, I'll tell her. |\n\n**Bitmiş olmayı vurgulamak için present perfect** de kullanılabilir:\n\n- I'll call you **as soon as** I**'ve finished**. (Bitirir bitirmez)\n\n**not ... until:** -meden ... -me / -e kadar ... yok\n\n- I **won't** decide **until** I**'ve seen** all the options. (Bütün seçenekleri görmeden karar vermeyeceğim.)",
     "examples": [{"en": "As soon as the shop opens, I'll go in.", "tr": "Dükkân açılır açılmaz içeri gireceğim."},
                  {"en": "Don't pay until you've checked the price.", "tr": "Fiyatı kontrol etmeden ödeme yapma."},
                  {"en": "We'll have dinner after the film finishes.", "tr": "Film bittikten sonra akşam yemeği yiyeceğiz."}],
     "turkishNote": "Türkçede \"varır varmaz\", \"gelene kadar\" gibi eklerde gelecek anlamı vardır, ama İngilizcede bu bağlaçlardan sonra will kullanılmaz. \"I'll call you as soon as I will arrive\" yanlış, \"as soon as I arrive\" doğru."},
    [
        mc("Hangisi doğru?", ["I'll call you as soon as I will arrive.", "I'll call you as soon as I arrive."], 1, "as soon as + present."),
        mc("I'll wait here ___ you come back. (gelene kadar)", ["until", "before", "as soon as"], 0, "until."),
        mc("___ you leave, close the window. (çıkmadan önce)", ["After", "Before", "Until"], 1, "before."),
        gap("As soon as I ___ (get) my salary, I'll buy a new coat.", ["get"], "as soon as + present."),
        gap("We won't start ___ everyone is here. (gelene kadar)", ["until"], "not ... until."),
        gap("___ I finish this course, I'll look for a job. (bitirdikten sonra)", ["After", "When"], "after / when."),
        gap("I'll call you as soon as I've ___ (finish).", ["finished"], "as soon as + present perfect."),
        listen("Don't buy the tickets until I've checked my calendar. As soon as I know my dates, I'll send you a message.", "Konuşan ne zaman mesaj atacak?", ["Biletleri alınca", "Tarihlerini öğrenir öğrenmez", "Yarın sabah"], 1, "\"As soon as I know my dates\""),
        order(["the", "film", "finishes", "We'll", "eat", "after"], "We'll eat after the film finishes.", "will + after + present.", "Film bittikten sonra yemek yiyeceğiz."),
        typ("İngilizce yazın: \"Varır varmaz seni ararım.\"", variants("I'll call you as soon as I arrive.", "I will call you as soon as I arrive.", "As soon as I arrive, I'll call you.", "I'll phone you as soon as I arrive.", "As soon as I arrive, I will call you.", "I'll call you as soon as I get there.", "As soon as I get there, I'll call you."), "I'll call you + as soon as I arrive."),
    ],
    {"kind": "speaking", "task": speak("Yarınki gününüzü sırasıyla anlatın. as soon as, before, after, until ve when'i en az birer kez kullanın.",
                                       "As soon as I wake up, I'll have a coffee. Before I leave the house, I'll check my emails. I'll stay at the office until I finish the report. After I finish work, I'll meet Elif. When I get home, I'll watch a film.",
                                       ["Bağlaçlardan sonra present", "Ana cümlede will", "Olay sırası mantıklı"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Karar ver!", "Bir alışveriş kararının artılarını ve eksilerini tartışıp gerekçeli bir karar verebilirim.",
    {"kind": "dialogue", "title": "Araba mı, bisiklet mi?", "lines": [
        {"speaker": "Okan", "text": "I can't make up my mind. Should I buy a second-hand car or an electric bike?"},
        {"speaker": "Duru", "text": "Well, on the one hand, a car is more comfortable in winter."},
        {"speaker": "Okan", "text": "True. On the other hand, if I buy a car, I'll have to pay for petrol, insurance and parking."},
        {"speaker": "Duru", "text": "And the bike is much cheaper. If you use it every day, you'll get fit too."},
        {"speaker": "Okan", "text": "But what will I do when it rains?"},
        {"speaker": "Duru", "text": "You might take the bus on rainy days. Honestly, I think the bike is worth it."}],
     "questions": [
        mc("What's one advantage of the car?", ["It's cheaper.", "It's more comfortable in winter.", "You'll get fit."], 1, "\"a car is more comfortable in winter\""),
        mc("What does Duru recommend?", ["The car", "The bike", "The bus every day"], 1, "\"I think the bike is worth it.\""),
     ]},
    {"explanation": "**Seçenekleri tartmak:**\n\n- **On the one hand**, ... **On the other hand**, ...\n- The **advantage / disadvantage** of ... is that ...\n- **The main problem is** ...\n- It's expensive, **but it's worth it**.\n\n**Sonuçları first conditional ile düşünmek** (ana cümlede will dışında modal da olur):\n\n| Yapı | Anlam | Örnek |\n|---|---|---|\n| If ..., **will** | kesin sonuç | If I buy a car, I**'ll** have to pay for parking. |\n| If ..., **might / may** | olası sonuç | If you wait, prices **might** go down. |\n| If ..., **can** | olanak | If you don't like it, you **can** return it. |\n| If ..., **should** | tavsiye | If you need it, you **should** buy it. |\n\n**Karar vermek:**\n\n- I **can't make up my mind**. / I'**ve decided to** ...\n- I think I'**ll** go for the bike. (Anlık karar → will)\n- **In the end**, ...",
     "examples": [{"en": "If you wait until January, the prices might go down.", "tr": "Ocak'a kadar beklersen fiyatlar düşebilir."},
                  {"en": "The main disadvantage is the price.", "tr": "Asıl dezavantajı fiyatı."},
                  {"en": "OK, I'll go for the cheaper one.", "tr": "Tamam, ucuz olanı seçiyorum."}],
     "turkishNote": "\"Karar veremiyorum\" için \"I can't give a decision\" demeyin; doğal karşılığı \"I can't make up my mind\" ya da \"I can't decide\"dır. Anlık kararlar için will kullanılır: \"OK, I'll take it!\" (Tamam, alıyorum!)"},
    [
        mc("\"Karar veremiyorum.\"", ["I can't give a decision.", "I can't make up my mind.", "I don't make my mind."], 1, "make up my mind."),
        mc("Olası sonuç: \"If you wait, prices ___ go down.\"", ["will", "might", "must"], 1, "Belki → might."),
        mc("Dükkânda anlık karar:", ["OK, I take it!", "OK, I'll take it!", "OK, I'm going to taking it!"], 1, "Anlık karar → will."),
        gap("On the one hand it's fast. On the ___ hand, it's expensive.", ["other"], "On the other hand."),
        gap("It's expensive, but it's ___ it. (buna değer)", ["worth"], "worth it."),
        gap("If you don't like it, you ___ return it. (olanak)", ["can"], "can."),
        gap("The main ___ is that it's heavy. (dezavantaj)", ["disadvantage", "problem"], "disadvantage."),
        match([("On the one hand", "Bir yandan"), ("worth it", "değer"), ("make up your mind", "karar vermek"), ("go for", "seçmek"), ("in the end", "sonunda")], "Eşleştirin."),
        listen("I've decided. On the one hand, the flat in the centre is small. On the other hand, if I live there, I'll walk to work and save money on transport. So I'll go for it.", "Konuşan hangi daireyi seçti?", ["Merkezdeki küçük daire", "Dışarıdaki büyük daire", "Henüz karar vermedi"], 0, "\"So I'll go for it.\""),
        typ("İngilizce yazın: \"Ocak'a kadar beklersen fiyatlar düşebilir.\"", variants("If you wait until January, prices might go down.", "If you wait until January, the prices might go down.", "If you wait until January, prices may go down.", "If you wait until January, the prices may go down.", "Prices might go down if you wait until January.", "If you wait until January prices might go down."), "If you wait until January, prices might go down."),
    ],
    {"kind": "writing", "task": write("Önünüzdeki bir kararı anlatan bir forum gönderisi yazın (100–130 kelime): örneğin yeni telefon mu tamir mi, kiralık mı satılık mı, tatil mi birikim mi. Artıları ve eksileri on the one hand / on the other hand ile yazın, first conditional (will, might, can) ve unless kullanın, sonunda kararınızı verin.",
                                      "I can't make up my mind about my holiday this summer. On the one hand, I've always wanted to visit Italy. If I go, I'll see Rome and Florence, and I'll practise my Italian. On the other hand, it's very expensive in August. If I spend that much, I won't be able to save for my new laptop. My friend says prices might go down if I travel in September, but I can't take time off then unless my boss agrees. So in the end, I've decided to stay in Turkey this summer and save my money. I'll go to Italy next spring when it's cheaper!",
                                      ["Artı / eksi tartışma kalıpları", "First conditional (will, might, can)", "unless doğru", "Net bir karar", "Düzenli paragraf"])},
)

u.test([
    mc("Hangisi doğru?", ["If it will snow, the school will close.", "If it snows, the school will close."], 1, "if + present"),
    mc("If you ___ now, you'll be on time.", ["leave", "will leave"], 0, "if + present"),
    mc("Ödünç vermesini istiyorsunuz:", ["Can you borrow me your bike?", "Can you lend me your bike?"], 1, "lend"),
    mc("I spend a lot ___ books.", ["on", "for"], 0, "spend on"),
    mc("\"unless\" = ?", ["if not", "when", "as soon as"], 0, "unless"),
    mc("Hangisi doğru?", ["Unless you don't hurry, you'll be late.", "Unless you hurry, you'll be late."], 1, "unless + olumlu"),
    mc("Kesin: \"___ I get home, I'll text you.\"", ["If", "When"], 1, "when"),
    gap("I'll wait ___ you finish. (bitirene kadar)", ["until"], "until"),
    gap("As soon as I ___ (arrive), I'll call you.", ["arrive", "get there"], "as soon as + present"),
    gap("I can't ___ a new car. (parası yetmek)", ["afford"], "afford"),
    gap("You won't get a refund unless you have the ___. (fiş)", ["receipt"], "receipt"),
    mc("Olası sonuç: \"If we don't book now, there ___ be any tickets left.\"", ["mightn't", "might not", "can"], 1, "might not"),
    listen("I won't buy a new laptop until mine breaks. When it stops working, I'll look for a good discount.", "Konuşan ne zaman yeni laptop alacak?", ["Hemen", "Eskisi bozulunca", "İndirim gelince, bozulmasa bile"], 1, "\"until mine breaks\""),
    typ("İngilizce yazın: \"Fişin olmadıkça para iadesi alamazsın.\"", variants("You won't get a refund unless you have the receipt.", "You can't get a refund unless you have the receipt.", "Unless you have the receipt, you won't get a refund.", "Unless you have the receipt, you can't get a refund.", "You will not get a refund unless you have the receipt.", "You cannot get a refund unless you have the receipt."), "... unless you have the receipt."),
    write("Bir arkadaşınız ilk maaşını aldı ve ne yapacağını bilmiyor. Ona bir mesaj yazın (100–130 kelime): first conditional, unless, as soon as / before / when ve para kelimeleri (save, spend on, budget, afford, worth it) kullanarak tavsiyeler verin.",
          "Congratulations on your first salary! Here's my advice. Before you spend anything, make a budget. If you know where your money goes, you'll save more easily. Try to save 20% as soon as you get paid. If you wait until the end of the month, there won't be anything left! Don't buy expensive clothes unless they're on sale, and don't borrow money unless it's an emergency. If you want a new phone, wait a few months. Prices might go down. But if you really want a good holiday, save for it. It's always worth it. When you get your next salary, you'll see the difference!",
          ["First conditional", "unless doğru", "Zaman bağlaçlarından sonra present", "Para kelimeleri", "Tavsiye tonu"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

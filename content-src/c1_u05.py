"""C1 Ünite 5: Olasılık."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("C1", 5, "Olasılık", "Probability",
         "Geleceğe, şimdiye ve geçmişe dair olasılıkları ince derecelerle (bound to, may well, likely to, the chances are, I doubt whether) ifade edebilir, tahminlerimi gerekçelendirebilir ve geleceğe dair dengeli bir öngörü yazısı yazabilirim.",
         ["may well / might well / could well", "be bound to / be sure to / be certain to", "be (un)likely to / It is likely that / The chances are", "geçmişe dair olasılık: is bound to have, may well have", "kesinlik ve şüphe ifadeleri"],
         ["gelecek tahminleri", "teknoloji ve toplum", "risk ve şans"],
         {"title": "Kâhinler meclisi", "durationMinutes": 45,
          "goal": "Gruplar 2050 yılı için bir alan seçer (eğitim, ulaşım, sağlık, iş). Her grup 5 tahmin hazırlar ve her birinin olasılığını farklı yapılarla belirtir (bound to, may well, highly unlikely to). Sınıf her tahmin için kendi olasılık oyunu verir ve gruplar tahminlerini savunur."})

u.vocab([
    ("bound to", "kesinlikle ... olacak", "Prices are bound to rise.", "Fiyatlar kesinlikle artacak.", None),
    ("may well", "pekâlâ ... olabilir", "It may well rain later.", "Sonra pekâlâ yağmur yağabilir.", None),
    ("likely", "muhtemel", "She's likely to win.", "Kazanması muhtemel.", "likelihood (isim)"),
    ("unlikely", "pek olası değil", "It's unlikely that he'll come.", "Gelmesi pek olası değil.", None),
    ("the chances are", "büyük ihtimalle", "The chances are that it'll be late.", "Büyük ihtimalle geç kalacak.", None),
    ("in all likelihood", "büyük olasılıkla", "In all likelihood, the plan will be approved.", "Büyük olasılıkla plan onaylanacak.", "resmî"),
    ("odds", "olasılık, ihtimal", "The odds are against us.", "İhtimaller aleyhimize.", None),
    ("a long shot", "zayıf ihtimal", "It's a long shot, but it's worth trying.", "Zayıf bir ihtimal ama denemeye değer.", None),
    ("a foregone conclusion", "önceden belli sonuç", "The result was a foregone conclusion.", "Sonuç önceden belliydi.", None),
    ("doubt", "şüphe etmek; şüphe", "I doubt whether she'll agree.", "Kabul edeceğinden şüpheliyim.", None),
    ("inevitable", "kaçınılmaz", "Change is inevitable.", "Değişim kaçınılmaz.", None),
    ("conceivable", "akla yatkın, mümkün", "It's conceivable that we'll live on Mars.", "Mars'ta yaşamamız akla yatkın.", None),
    ("predict", "öngörmek, tahmin etmek", "Experts predict a slow recovery.", "Uzmanlar yavaş bir toparlanma öngörüyor.", "prediction"),
    ("forecast", "tahmin; tahmin etmek", "The weather forecast is good.", "Hava tahmini iyi.", None),
    ("speculate", "spekülasyon yapmak, tahmin yürütmek", "It's too early to speculate.", "Tahmin yürütmek için çok erken.", None),
    ("trend", "eğilim", "This trend is likely to continue.", "Bu eğilimin devam etmesi muhtemel.", None),
    ("outcome", "sonuç", "The outcome is still uncertain.", "Sonuç hâlâ belirsiz.", None),
    ("uncertain", "belirsiz", "The future is uncertain.", "Gelecek belirsiz.", None),
    ("probability", "olasılık", "There is a high probability of rain.", "Yüksek yağmur olasılığı var.", None),
    ("in the foreseeable future", "öngörülebilir gelecekte", "Prices won't fall in the foreseeable future.", "Öngörülebilir gelecekte fiyatlar düşmeyecek.", None),
    ("by no means certain", "hiç de kesin değil", "Victory is by no means certain.", "Zafer hiç de kesin değil.", None),
    ("against all odds", "her şeye rağmen", "Against all odds, they survived.", "Her şeye rağmen hayatta kaldılar.", None),
    ("chances are slim", "ihtimal çok düşük", "The chances of finding him are slim.", "Onu bulma ihtimali çok düşük.", None),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Pekâlâ olabilir", "may well / might well / could well ve bound to / sure to yapılarıyla gelecek hakkında farklı derecelerde tahmin yapabilirim.",
    {"kind": "dialogue", "title": "Maç öncesi", "lines": [
        {"speaker": "Kemal", "text": "So, who do you think will win tonight?"},
        {"speaker": "Seda", "text": "Well, the away team is bound to be tired. They played on Saturday too."},
        {"speaker": "Kemal", "text": "True, but they've got a much better squad. They may well win anyway."},
        {"speaker": "Seda", "text": "Maybe. But our goalkeeper is back from injury, and that could well make the difference."},
        {"speaker": "Kemal", "text": "And the stadium's sure to be full. The crowd will help."},
        {"speaker": "Seda", "text": "Exactly. I think it might well be a draw."}],
     "questions": [
        mc("Why does Seda think the away team will be tired?", ["They travelled a long way.", "They played on Saturday too.", "They're old."], 1, "\"They played on Saturday too.\""),
        mc("What does Seda predict?", ["A home win", "An away win", "A draw"], 2, "\"I think it might well be a draw.\""),
     ]},
    {"explanation": "**Olasılık ölçeği (gelecek):**\n\n| Kesinlik | Yapı | Örnek |\n|---|---|---|\n| ~%100 | **be bound to** + V1 | They're **bound to** be tired. |\n| ~%100 | **be sure / certain to** + V1 | The stadium's **sure to** be full. |\n| ~%90 | **will definitely / certainly** | It'll **definitely** rain. |\n| ~%70 | **may well / might well / could well** + V1 | They **may well** win. |\n| ~%70 | **will probably** / **probably won't** | He'll **probably** be late. |\n| ~%50 | **may / might / could** + V1 | It **might** snow. |\n| ~%30 | **might not / may not** | She **might not** come. |\n| ~%5 | **definitely won't / certainly won't** | It **definitely won't** happen. |\n\n**may well / might well / could well:** **well** eklemek olasılığı **artırır**.\n\n- *It **might** rain.* (Belki.) → *It **might well** rain.* (Gayet muhtemel.)\n\n**be bound to:** Konuşanın **mantıklı kanıta dayalı kesin tahmini**:\n\n- *You've worked so hard. You're **bound to** pass.*\n- *If you leave it there, someone **is bound to** steal it.*\n\n**Zarfların yeri:**\n\n- Olumlu cümlede **will'den sonra**: *It **will probably** rain.*\n- Olumsuz cümlede **won't'tan önce**: *It **probably won't** rain.* (~~It won't probably~~)",
     "examples": [{"en": "If you don't book now, the tickets are bound to sell out.", "tr": "Şimdi ayırtmazsan biletler kesinlikle tükenecek."},
                  {"en": "The new policy may well cause problems.", "tr": "Yeni politika pekâlâ sorunlara yol açabilir."},
                  {"en": "He probably won't get the job.", "tr": "Muhtemelen işi alamayacak."}],
     "turkishNote": "Türkçede olasılık \"kesin\", \"büyük ihtimalle\", \"belki\", \"pek sanmam\" gibi kelimelerle ince ince ayarlanır; İngilizce de çok zengindir. \"may well\" Türkçedeki \"pekâlâ\" kelimesine çok yakındır (\"Pekâlâ kazanabilirler\"). Türkçe konuşanların en sık hatası zarfın yeridir: \"It won't probably\" yanlıştır; olumsuz cümlede \"probably\" won't'tan önce gelir."},
    [
        mc("En kesin tahmin:", ["She may win.", "She's bound to win."], 1, "bound to."),
        mc("\"might well\" anlamı:", ["Belki, düşük ihtimal", "Gayet muhtemel"], 1, "well güçlendirir."),
        mc("Hangisi doğru?", ["It won't probably rain.", "It probably won't rain."], 1, "Olumsuzda probably önce."),
        mc("Hangisi doğru?", ["He's bound to being late.", "He's bound to be late."], 1, "bound to + V1."),
        gap("You've studied so much. You're ___ to pass. (kesinlikle)", ["bound", "sure", "certain"], "bound to."),
        gap("The meeting ___ well go on until late. (pekâlâ)", ["may", "might", "could"], "may well."),
        gap("It will ___ be cold tomorrow. (muhtemelen)", ["probably"], "will probably."),
        gap("The stadium is ___ to be full. (kesin)", ["sure", "bound", "certain"], "sure to."),
        listen("With the new airport opening next year, tourism in the region is bound to grow. Hotels may well double their prices, and some local people might well decide to rent out their homes to visitors. It probably won't be good news for everyone, though.", "Konuşan bölgede turizm hakkında ne kadar emin?", ["Emin değil", "Kesinlikle büyüyeceğini düşünüyor", "Azalacağını düşünüyor"], 1, "\"tourism in the region is bound to grow\""),
        typ("İngilizcesi: \"Kesinlikle geç kalacak.\" (he, bound to)", variants("He's bound to be late.", "He is bound to be late."), "He's bound to be late."),
    ],
    {"kind": "speaking", "task": speak("Önümüzdeki yıl hayatınızda, şehrinizde ya da ülkenizde olacaklar hakkında 6 tahmin yapın. Her biri için farklı bir kesinlik düzeyi seçin: bound to, sure to, will definitely, may well, might, probably won't, definitely won't. Tahminlerinizi kısaca gerekçelendirin.",
                                       "Next year, prices are bound to go up again, because they always do. My brother is sure to finish university in June. He's already passed most of his exams. I may well change jobs, because I've been offered a position in another company. The new metro line might open in my city, but it probably won't be ready before the end of the year. And I definitely won't stop drinking coffee!",
                                       ["Kesinlik ölçeği çeşitliliği", "bound to / may well doğru yapı", "Zarf yeri", "Gerekçe"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "Muhtemel ve pek olası değil", "be likely to, It is likely that, The chances are ve in all likelihood gibi yapılarla olasılığı resmî ve dengeli bir dille ifade edebilirim.",
    {"kind": "text", "title": "Bir rapor: İşin geleceği", "body": "Over the next twenty years, artificial intelligence is likely to change the nature of work dramatically.\n\nIt is highly likely that many routine office tasks, such as data entry and scheduling, will be fully automated. Jobs in areas like customer service are also likely to be affected. However, it is unlikely that machines will replace jobs that require creativity, empathy or complex decision-making, at least in the foreseeable future.\n\nThe chances are that most workers will need to retrain at least once during their careers. In all likelihood, lifelong learning will become the norm rather than the exception.\n\nThere is also a strong possibility that working hours will become more flexible. Some experts even believe that a four-day week is likely to become common by 2040, although this is by no means certain.",
     "questions": [
        mc("Which jobs are unlikely to be replaced?", ["Data entry", "Jobs requiring creativity and empathy", "Scheduling"], 1, "\"jobs that require creativity, empathy or complex decision-making\""),
        mc("What will most workers probably need to do?", ["Retire early", "Retrain at least once", "Work longer hours"], 1, "\"most workers will need to retrain at least once\""),
     ]},
    {"explanation": "**be likely / unlikely to + V1** (özne kişi ya da şey)\n\n- *AI **is likely to** change work.*\n- *He **is unlikely to** agree.*\n- *Prices **are highly likely to** rise.* (çok muhtemel)\n\n**It is likely / unlikely that + cümle**\n\n- ***It is likely that** many tasks **will** be automated.*\n- ***It is highly unlikely that** she **will** resign.*\n\n**Dikkat:** **likely** bir **sıfattır**, zarf değil!\n\n- ~~He will likely come.~~ (AmE'de kullanılır, ama İngiliz akademik yazısında genellikle tercih edilmez)\n- ✓ *He **is likely to** come.* / ✓ *He will **probably** come.*\n\n**Diğer yapılar:**\n\n| Yapı | Örnek |\n|---|---|\n| **The chances are (that)** | **The chances are** most workers will retrain. |\n| **There's a good / strong chance that** | **There's a good chance that** it'll rain. |\n| **There's a strong possibility that** | **There's a strong possibility that** hours will change. |\n| **In all likelihood,** (resmî) | **In all likelihood,** the plan will fail. |\n| **The likelihood of** + isim / -ing | **The likelihood of** success is low. |\n| **The chances of** + -ing **are slim** | **The chances of** finding him **are slim**. |\n\n**Derecelendirme:** *highly / very / quite likely* — *highly / extremely unlikely*",
     "examples": [{"en": "The new law is likely to be approved next month.", "tr": "Yeni yasanın gelecek ay onaylanması muhtemel."},
                  {"en": "It is highly unlikely that prices will fall.", "tr": "Fiyatların düşmesi son derece düşük bir ihtimal."},
                  {"en": "The chances of winning the lottery are extremely slim.", "tr": "Piyangoyu kazanma ihtimali son derece düşük."}],
     "turkishNote": "Türkçede \"-mesi muhtemel\" yapısı (\"onaylanması muhtemel\") İngilizcede iki şekilde kurulabilir: \"It is likely to be approved\" ya da \"It is likely that it will be approved\". Türkçe konuşanların sık hatası, \"likely\"yi \"probably\" gibi zarf olarak kullanmaktır: \"It will likely happen\" Amerikan İngilizcesinde duyulur ama sınavlarda ve İngiliz akademik dilinde \"It is likely to happen\" daha güvenli bir tercihtir."},
    [
        mc("Hangisi doğru?", ["She is likely to be promoted.", "She is likely be promoted."], 0, "likely to + V1."),
        mc("Hangisi doğru?", ["It's likely that he will come.", "It's likely that he come."], 0, "that + tam cümle."),
        mc("\"The chances of finding it are slim.\"", ["Bulma ihtimali yüksek.", "Bulma ihtimali çok düşük."], 1, "slim = düşük."),
        mc("Resmî rapor dili:", ["In all likelihood, sales will increase.", "Sales gonna go up, I reckon."], 0, "Resmî."),
        gap("The project is ___ to be finished on time. (muhtemel değil)", ["unlikely"], "unlikely to."),
        gap("The ___ are that we'll have to wait. (büyük ihtimalle)", ["chances"], "The chances are."),
        gap("It is highly ___ that the company will close. (pek olası değil)", ["unlikely"], "highly unlikely."),
        gap("There's a strong ___ that the meeting will be postponed. (olasılık)", ["possibility", "chance"], "strong possibility."),
        listen("According to the latest forecast, there's a strong chance of heavy rain this weekend. Flooding is likely in low-lying areas, although it's unlikely to be as bad as last year. In all likelihood, the coastal road will be closed on Saturday.", "Sahil yolu hakkında ne söyleniyor?", ["Kesinlikle açık olacak", "Büyük olasılıkla cumartesi kapalı olacak", "Sel nedeniyle yıkıldı"], 1, "\"In all likelihood, the coastal road will be closed on Saturday.\""),
        typ("\"likely to\" ile yeniden yazın: \"It's probable that prices will rise.\" (Prices ...)", variants("Prices are likely to rise.", "Prices are very likely to rise.", "Prices are highly likely to rise."), "Prices are likely to rise."),
    ],
    {"kind": "speaking", "task": speak("Önümüzdeki 20 yılda eğitimde, ulaşımda ya da sağlıkta olacak değişiklikleri bir uzman gibi değerlendirin. be likely / unlikely to, It is highly likely that, The chances are, There's a strong possibility that, In all likelihood ve The chances of ... are slim yapılarından en az 5'ini kullanın.",
                                       "In education, I think online learning is likely to become even more common. It's highly likely that most universities will offer degrees that can be completed entirely online. The chances are that teachers will use AI tools to give students personal feedback. There's a strong possibility that exams will change too, because it's becoming harder to stop students from using technology. However, it's unlikely that schools will disappear completely. In all likelihood, children will still need a place to meet and learn together. The chances of replacing teachers entirely are, in my view, very slim.",
                                       ["likely / unlikely to", "It is likely that", "The chances are / of", "Resmî ve dengeli ton"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "Olmuş olmalı, olmuş olabilir", "Şimdiki ve geçmiş zaman hakkında ileri düzey olasılık yapılarını (must be -ing, is bound to have, may well have, is likely to have) kullanabilirim.",
    {"kind": "dialogue", "title": "Kayıp kargo", "lines": [
        {"speaker": "Aylin", "text": "The package still hasn't arrived. It was supposed to come yesterday."},
        {"speaker": "Tarık", "text": "The delivery driver must be having a busy week. It's nearly the holidays."},
        {"speaker": "Aylin", "text": "But the tracking says it was delivered at 3 p.m."},
        {"speaker": "Tarık", "text": "Then it's bound to have been left with a neighbour. They always do that."},
        {"speaker": "Aylin", "text": "Or someone may well have taken it from the doorstep."},
        {"speaker": "Tarık", "text": "That's unlikely. It's a quiet street. It's more likely to have been delivered to the wrong flat."},
        {"speaker": "Aylin", "text": "You're right. I'll check with Mrs Yazıcı on the second floor."}],
     "questions": [
        mc("What does the tracking say?", ["It's still at the warehouse.", "It was delivered at 3 p.m.", "It's been cancelled."], 1, "\"it was delivered at 3 p.m.\""),
        mc("What does Tarık think is most likely?", ["Someone stole it.", "It was delivered to the wrong flat or a neighbour.", "It was never sent."], 1, "\"more likely to have been delivered to the wrong flat\""),
     ]},
    {"explanation": "B2'de **must have / might have / can't have** yapılarını öğrendiniz. C1'de olasılık yapılarını **şimdiki** ve **geçmiş** zamanla birleştiriyoruz.\n\n**Şimdi devam eden durum hakkında:**\n\n| Yapı | Örnek |\n|---|---|\n| **must be + -ing** | He **must be having** a busy week. |\n| **can't be + -ing** | She **can't be working**. It's Sunday. |\n| **may / might be + -ing** | They **might be sleeping**. |\n| **is bound to be + -ing** | He**'s bound to be waiting** for us. |\n\n**Geçmiş hakkında:**\n\n| Yapı | Kesinlik | Örnek |\n|---|---|---|\n| **is bound to have** + V3 | çok yüksek | It**'s bound to have been** left with a neighbour. |\n| **must have** + V3 | çok yüksek | It **must have been** delivered. |\n| **is likely to have** + V3 | yüksek | It**'s likely to have been** delivered to the wrong flat. |\n| **may well / might well have** + V3 | gayet muhtemel | Someone **may well have** taken it. |\n| **may / might / could have** + V3 | orta | It **might have** got lost. |\n| **is unlikely to have** + V3 | düşük | He**'s unlikely to have** forgotten. |\n| **can't / couldn't have** + V3 | imkânsız | It **can't have** been stolen. |\n\n**Edilgen:** *It **is likely to have been** delivered.* / *It **may well have been** stolen.*",
     "examples": [{"en": "She must be feeling nervous about the interview.", "tr": "Mülakat için gergin hissediyor olmalı."},
                  {"en": "The email is bound to have gone to your spam folder.", "tr": "E-posta kesinlikle spam klasörüne düşmüştür."},
                  {"en": "He may well have missed the train.", "tr": "Pekâlâ treni kaçırmış olabilir."}],
     "turkishNote": "Türkçede \"düşmüştür\" (The email has probably gone) ve \"düşmüş olmalı\" (must have gone) gibi yapılar kesinliği ayarlar. İngilizcede \"is bound to have\" ve \"is likely to have\" bu derecelendirmeyi çok daha ince yapar. Türkçe konuşanlar geçmiş için \"is likely that it was\" demeye eğilimlidir; bu da doğrudur, ama \"is likely to have been\" daha kısa ve daha akademiktir."},
    [
        mc("Şu an devam eden tahmin:", ["He must work late.", "He must be working late."], 1, "must be + -ing."),
        mc("\"Kesinlikle komşuya bırakılmıştır.\"", ["It's bound to be left with a neighbour.", "It's bound to have been left with a neighbour."], 1, "Geçmiş + edilgen."),
        mc("\"He's unlikely to have forgotten.\"", ["Unutmuş olması pek olası değil.", "Unutacak gibi görünmüyor."], 0, "Geçmiş."),
        mc("En düşük ihtimal:", ["It may well have been stolen.", "It can't have been stolen."], 1, "can't have."),
        gap("She isn't answering. She ___ be driving. (olabilir)", ["might", "may", "could", "must"], "might be + -ing."),
        gap("The parcel is likely to have ___ delivered to the wrong address.", ["been"], "have been + V3."),
        gap("He's bound ___ have heard the news by now.", ["to"], "bound to have."),
        gap("They may ___ have left already. (pekâlâ)", ["well"], "may well have."),
        listen("The lights are off and the car's gone. They must be visiting her parents. Or they may well have gone away for the weekend. Anyway, they're unlikely to have forgotten our dinner tonight. Let's call them.", "Konuşan akşam yemeği hakkında ne düşünüyor?", ["Unuttular", "Unutmuş olmaları pek olası değil", "İptal ettiler"], 1, "\"they're unlikely to have forgotten our dinner tonight\""),
        typ("İngilizcesi: \"Pekâlâ yanlış otobüse binmiş olabilir.\" (she, may well)", variants("She may well have taken the wrong bus.", "She may well have got on the wrong bus.", "She may well have caught the wrong bus."), "She may well have taken the wrong bus."),
    ],
    {"kind": "speaking", "task": speak("Şu durumları yorumlayın, her biri için en az 2 farklı olasılık yapısı kullanın (şimdi için must / might be + -ing; geçmiş için bound to have, may well have, likely / unlikely to have, can't have): (1) Bir arkadaşınız 3 gündür mesajlarınıza cevap vermiyor. (2) Ofise geldiğinizde masanızda bir çiçek buketi var. (3) Komşunuzun evinden yüksek sesle müzik geliyor.",
                                       "One: My friend hasn't replied for three days. She must be having a really busy week. Or she may well have lost her phone again. She's unlikely to have forgotten about me! Two: There's a bouquet on my desk. It's bound to have been my colleague Ece. She knows it's my birthday. It can't have been my boss. He never remembers anything. Three: My neighbours are playing loud music. They must be having a party. Their son is likely to have finished his exams today.",
                                       ["Şimdiki devam eden olasılık", "Geçmiş olasılık yapıları", "Kesinlik çeşitliliği", "Edilgen"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Emin misin?", "Kesinlik ve şüphe bildiren deyimsel ifadeleri (I doubt whether, I wouldn't be surprised if, it's a long shot, a foregone conclusion) doğal bir şekilde kullanabilirim.",
    {"kind": "text", "title": "Seçim gecesi yorumları", "body": "Commentator 1: \"With half the votes counted, it's looking like a foregone conclusion. There's no doubt that the governing party will win the most seats.\"\n\nCommentator 2: \"I wouldn't be so sure. I doubt whether they'll have a majority. The big cities haven't been counted yet.\"\n\nCommentator 1: \"True, but I'd be very surprised if the opposition won more than 40%.\"\n\nCommentator 2: \"I wouldn't be surprised if we saw a coalition. It's a long shot, but the smaller parties could well hold the balance of power.\"\n\nCommentator 1: \"The odds are against it. But anything can happen in politics. Against all odds, a new party won 15% of the vote four years ago.\"",
     "questions": [
        mc("What does Commentator 2 doubt?", ["That the governing party will win any seats", "That the governing party will have a majority", "That the votes will be counted"], 1, "\"I doubt whether they'll have a majority.\""),
        mc("What surprising thing happened four years ago?", ["A coalition was formed.", "A new party won 15% of the vote.", "Nobody voted."], 1, "\"a new party won 15% of the vote four years ago\""),
     ]},
    {"explanation": "**Kesinlik:**\n\n| İfade | Anlam |\n|---|---|\n| **There's no doubt that** ... | Hiç şüphe yok ki ... |\n| **It's a foregone conclusion.** | Sonuç önceden belli. |\n| **It's a dead cert.** (samimi) | Kesin. |\n| **I'm (absolutely) convinced that** ... | ... olduğuna kesinlikle inanıyorum. |\n| **Without a shadow of a doubt** | Hiç şüphesiz |\n\n**Olasılık / şüphe:**\n\n| İfade | Anlam |\n|---|---|\n| **I wouldn't be surprised if** + past | ... olsa şaşırmam (= muhtemel) |\n| **I'd be (very) surprised if** + past | ... olsa çok şaşırırım (= pek olası değil) |\n| **I doubt (whether / if / that)** ... | ... olacağından şüpheliyim |\n| **I have my doubts about** ... | ... konusunda şüphelerim var |\n| **It's a long shot.** | Zayıf ihtimal. |\n| **The odds are against it / in our favour.** | İhtimaller aleyhimize / lehimize. |\n| **Against all odds,** ... | Her şeye rağmen, imkânsız gibi görünse de ... |\n| **It's touch and go.** | Belirsiz, ucu ucuna. |\n| **It's anyone's guess.** | Kimse bilemez. |\n| **I wouldn't bet on it.** | Pek sanmam. |\n\n**Dikkat:**\n\n- *I wouldn't be surprised if* **muhtemel** demek (olumsuz görünse de!)\n- *I doubt whether he'll come.* = He probably won't come.\n- **I doubt** + olumsuz kullanılmaz: ~~I doubt he won't come~~",
     "examples": [{"en": "I wouldn't be surprised if it snowed tonight.", "tr": "Bu gece kar yağsa şaşırmam."},
                  {"en": "I doubt whether we'll finish on time.", "tr": "Zamanında bitireceğimizden şüpheliyim."},
                  {"en": "Who will win? It's anyone's guess.", "tr": "Kim kazanacak? Kimse bilemez."}],
     "turkishNote": "\"I wouldn't be surprised if...\" ifadesi Türkçedeki \"... olsa şaşırmam\" ile birebir aynıdır; olumsuz yapıya rağmen \"muhtemel\" anlamına gelir. \"I doubt\" ise Türkçedeki \"Pek sanmam\" ya da \"Şüpheliyim\" ile örtüşür, yani olumsuz bir tahmindir. \"It's anyone's guess\" (Kimse bilemez / Allah bilir) çok doğal ve sık kullanılan bir kalıptır."},
    [
        mc("\"I wouldn't be surprised if she resigned.\" konuşan ne düşünüyor?", ["İstifa etmesi muhtemel.", "İstifa etmesi imkânsız."], 0, "Muhtemel."),
        mc("\"I doubt whether he'll come.\" konuşan ne düşünüyor?", ["Muhtemelen gelecek.", "Muhtemelen gelmeyecek."], 1, "Şüphe."),
        mc("\"It's a foregone conclusion.\"", ["Sonuç belirsiz.", "Sonuç önceden belli."], 1, "foregone conclusion."),
        mc("\"It's anyone's guess.\"", ["Herkes biliyor.", "Kimse bilemez."], 1, "anyone's guess."),
        gap("I ___ be surprised if it rained. It's very cloudy. (şaşırmam)", ["wouldn't"], "I wouldn't be surprised if."),
        gap("It's a long ___, but let's try. (zayıf ihtimal)", ["shot"], "a long shot."),
        gap("Against all ___, the small team won the cup.", ["odds"], "Against all odds."),
        gap("There's no ___ that she's the best candidate.", ["doubt"], "There's no doubt that."),
        listen("Will the new bridge be finished by summer? Honestly, it's touch and go. The builders say yes, but I have my doubts. I'd be surprised if it opened before September, and I wouldn't bet on that either.", "Konuşan köprünün yazın açılması hakkında ne düşünüyor?", ["Kesinlikle açılacak", "Şüpheli, pek olası değil", "Çoktan açıldı"], 1, "\"I have my doubts... I'd be surprised if it opened before September\""),
        typ("İngilizcesi: \"Geç kalsa şaşırmam.\" (he)", variants("I wouldn't be surprised if he was late.", "I wouldn't be surprised if he were late.", "I wouldn't be surprised if he arrived late."), "I wouldn't be surprised if he was late."),
    ],
    {"kind": "speaking", "task": speak("Bir spor yorumcusu, bir ekonomi uzmanı ya da bir dizi eleştirmeni olarak bir sonuç hakkında tahminde bulunun (bir maç, bir seçim, bir dizinin finali, döviz kuru). En az 6 farklı kesinlik / şüphe ifadesi kullanın: There's no doubt that, I wouldn't be surprised if, I doubt whether, It's a long shot, The odds are, It's anyone's guess, I wouldn't bet on it.",
                                       "So, the big question: how will the series end? There's no doubt that the main character will survive. The writers would never kill her. I wouldn't be surprised if her brother turned out to be the villain. There have been so many clues. I doubt whether the couple will get back together, though. It's a long shot, but some fans think the whole story was a dream. The odds are against that, I think. As for who gets the throne, it's anyone's guess. Some say the youngest sister, but I wouldn't bet on it.",
                                       ["Kesinlik ve şüphe ifadeleri", "I wouldn't be surprised if doğru anlam", "Doğal ve canlı anlatım"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Geleceği öngörmek", "Farklı kesinlik düzeylerini dengeli kullanarak geleceğe dair gerekçeli ve inandırıcı bir öngörü makalesi yazabilirim.",
    {"kind": "text", "title": "Makale: 2050'de şehirler", "body": "What will our cities look like in 2050? Nobody can say for certain, but current trends give us some clues.\n\nFirstly, cities are bound to become larger. According to the United Nations, around two-thirds of the world's population is expected to live in urban areas by 2050. This means that housing is likely to remain one of the biggest challenges.\n\nTransport may well change beyond recognition. Electric and self-driving vehicles are likely to become common, and there is a strong possibility that many city centres will ban private cars altogether. Some cities in Europe have already started.\n\nClimate change, however, is the great unknown. Coastal cities could well face serious flooding, and in all likelihood, many will need to invest heavily in sea defences. Rising temperatures are also likely to make green spaces and trees more important than ever.\n\nWill we all be living in \"smart\" cities controlled by AI? I doubt it. Technology will undoubtedly play a role, but I would be surprised if it solved problems such as inequality on its own.\n\nIn short, the cities of 2050 are likely to be greener, more crowded and more connected. Whether they will also be fairer is anyone's guess.",
     "questions": [
        mc("What proportion of people are expected to live in cities by 2050?", ["About half", "About two-thirds", "Almost everyone"], 1, "\"around two-thirds of the world's population\""),
        mc("What does the writer doubt?", ["That cities will grow", "That we'll all live in AI-controlled smart cities", "That climate change will matter"], 1, "\"Will we all be living in 'smart' cities controlled by AI? I doubt it.\""),
     ]},
    {"explanation": "**İyi bir öngörü makalesinin özellikleri:**\n\n| Özellik | Örnek |\n|---|---|\n| **Belirsizliği kabul etmek** | *Nobody can say for certain, but ...* |\n| **Kanıta dayanmak** | *According to ..., current trends suggest ...* |\n| **Kesinliği derecelendirmek** | En emin olduğundan en az emin olduğuna sıralayın: *bound to → likely to → may well → I doubt* |\n| **Bağlam ve neden** | *This means that ... / because ...* |\n| **Kendi sesini eklemek** | *I would be surprised if ... / I doubt it.* |\n| **Dengeli kapanış** | *In short, ... Whether ... is anyone's guess.* |\n\n**Kaçınılması gerekenler:**\n\n- Her şeyi **kesin** sunmak: ~~Cities will be completely green.~~ → *Cities are likely to be greener.*\n- Aynı yapıyı **tekrarlamak**: ~~will probably ... will probably ... will probably~~\n- **Kanıtsız** iddialar: Kaynak belirtin ya da \"current trends\" gibi gerekçe verin.\n\n**Edilgen öngörü yapıları (resmî):**\n\n- *... **is expected to** reach 10 million.*\n- *... **is predicted / forecast to** grow by 5%.*\n- ***It is estimated that** ...*\n\n(Bu yapıları C1 Ünite 8'de daha ayrıntılı göreceksiniz.)",
     "examples": [{"en": "Nobody can say for certain, but current trends give us some clues.", "tr": "Kimse kesin bir şey söyleyemez ama mevcut eğilimler bize bazı ipuçları veriyor."},
                  {"en": "The population is expected to reach 10 million by 2040.", "tr": "Nüfusun 2040'a kadar 10 milyona ulaşması bekleniyor."},
                  {"en": "Whether this will make us happier is anyone's guess.", "tr": "Bunun bizi daha mutlu edip etmeyeceğini kimse bilemez."}],
     "turkishNote": "Türkçe makalelerde gelecek tahminleri bazen çok kesin bir dille yapılır (\"2050'de şehirler tamamen akıllı olacak\"). İngilizce yazı kültüründe ise okuyucu, yazarın ne kadar emin olduğunu bilmek ister; aşırı kesin ifadeler güvenilirliği azaltır. Farklı olasılık yapılarını kullanmak hem dil düzeyinizi gösterir hem de yazınızı daha inandırıcı yapar."},
    [
        mc("Öngörü makalesine en iyi giriş:", ["In 2050, cities will be perfect.", "Nobody can say for certain, but current trends give us some clues."], 1, "Belirsizliği kabul."),
        mc("En dengeli ifade:", ["Cities will be completely green.", "Cities are likely to be greener."], 1, "Derecelendirilmiş."),
        mc("Resmî edilgen öngörü:", ["The population is expected to double.", "The population gonna double."], 0, "is expected to."),
        mc("İyi bir kapanış:", ["Whether they will also be fairer is anyone's guess.", "That's it."], 0, "Dengeli kapanış."),
        gap("The population is ___ to reach 20 million by 2050. (bekleniyor)", ["expected", "predicted", "forecast", "projected"], "is expected to."),
        gap("Nobody can say for ___, but ... (kesin)", ["certain", "sure"], "for certain."),
        gap("Coastal cities ___ well face serious flooding. (pekâlâ)", ["could", "may", "might"], "could well."),
        gap("I would be ___ if technology solved inequality on its own.", ["surprised"], "I would be surprised if."),
        listen("By 2040, it's highly likely that most cars sold in Europe will be electric. Self-driving buses may well be common in big cities. But I'd be surprised if people stopped owning cars completely. The chances of that happening in the next twenty years are, I think, quite slim.", "Konuşan insanların araba sahibi olmayı bırakması hakkında ne düşünüyor?", ["Kesinlikle olacak", "Önümüzdeki 20 yılda pek olası değil", "Çoktan oldu"], 1, "\"I'd be surprised if people stopped owning cars completely\""),
        typ("Daha dengeli yazın (likely to): \"In 2050, everyone will work from home.\"", variants("In 2050, more people are likely to work from home.", "By 2050, more people are likely to work from home.", "In 2050, many people are likely to work from home.", "By 2050, many people are likely to be working from home."), "In 2050, more people are likely to work from home."),
    ],
    {"kind": "writing", "task": write("Bir dergi için \"Eğitim 2050\" ya da \"Sağlık 2050\" başlıklı bir öngörü makalesi yazın (230–280 kelime). Belirsizliği kabul eden bir girişle başlayın; en az 3 öngörüyü farklı kesinlik düzeyleriyle sunun ve gerekçelendirin. En az 7 farklı olasılık yapısı kullanın (bound to, likely to, may well, It is highly unlikely that, The chances are, I doubt whether, I wouldn't be surprised if, is expected to, in all likelihood). Kendi sesinizi ekleyin ve dengeli bir kapanış yapın.",
                                      "Education in 2050\n\nPredicting the future of education is risky. Twenty years ago, few people imagined that millions of students would one day attend classes through their laptops. Nevertheless, current trends suggest a few likely changes.\n\nFirstly, technology is bound to play an even bigger role. Artificial intelligence is likely to become a personal tutor for every student, adapting lessons to their level and giving instant feedback. The chances are that homework, as we know it today, will look very different, since it is becoming harder to know whether students have done it themselves.\n\nSecondly, the idea of finishing education at twenty-two may well disappear. As jobs change faster, most adults are expected to return to learning several times during their careers. In all likelihood, short online courses will become as important as university degrees.\n\nHowever, some things are unlikely to change. It is highly unlikely that schools will disappear, because children need more than information. They need friends, teachers who care about them and a place to learn how to live with others. I doubt whether any machine will be able to replace that.\n\nThere are also risks. If access to technology remains unequal, the gap between rich and poor students could well grow. I wouldn't be surprised if this became one of the most important political debates of the next decade.\n\nIn short, the classroom of 2050 is likely to be more flexible, more personal and more digital. Whether it will also be more human depends on the choices we make today.",
                                      ["Belirsizliği kabul eden giriş", "En az 7 olasılık yapısı", "Gerekçeli öngörüler", "Kendi sesi", "Dengeli kapanış"])},
)

u.test([
    mc("En kesin tahmin:", ["It may rain.", "It's bound to rain."], 1, "bound to"),
    mc("Hangisi doğru?", ["It won't probably happen.", "It probably won't happen."], 1, "probably won't"),
    mc("\"I wouldn't be surprised if he quit.\"", ["İstifa etmesi muhtemel.", "İstifa etmesi imkânsız."], 0, "Muhtemel"),
    mc("Şu an devam eden tahmin:", ["She must sleep.", "She must be sleeping."], 1, "must be + -ing"),
    mc("\"I doubt whether she'll agree.\"", ["Muhtemelen kabul edecek.", "Muhtemelen kabul etmeyecek."], 1, "Şüphe"),
    gap("The project is ___ to be finished on time. (pek olası değil)", ["unlikely"], "unlikely to"),
    gap("The ___ are that we'll have to start again. (büyük ihtimalle)", ["chances"], "The chances are"),
    gap("They may ___ have left already. (pekâlâ)", ["well"], "may well have"),
    gap("The package is likely to have ___ stolen.", ["been"], "have been + V3"),
    gap("It's a long ___, but it might work. (zayıf ihtimal)", ["shot"], "long shot"),
    gap("The population is ___ to double by 2060. (bekleniyor)", ["expected", "predicted", "forecast", "projected"], "is expected to"),
    mc("\"It's anyone's guess.\"", ["Kimse bilemez.", "Herkes biliyor."], 0, "anyone's guess"),
    listen("I'm sure the train is bound to be delayed again. It always is on Fridays. But I'd be surprised if it was cancelled. We may well get there late, though, so let's call the restaurant.", "Konuşan trenin iptal edilmesi hakkında ne düşünüyor?", ["Kesinlikle iptal edilecek", "Pek olası değil", "Çoktan iptal edildi"], 1, "\"I'd be surprised if it was cancelled\""),
    typ("İngilizcesi: \"E-posta kesinlikle spam klasörüne gitmiştir.\" (the email, bound to)", variants("The email is bound to have gone to the spam folder.", "The email's bound to have gone to the spam folder.", "The email is bound to have gone into the spam folder."), "The email is bound to have gone to the spam folder."),
    write("\"Çalışma hayatı 2040\" konulu bir blog yazısı yazın (220–260 kelime). Belirsizliği kabul eden bir girişle başlayın; uzaktan çalışma, yapay zekâ ve çalışma saatleri konularında öngörülerde bulunun. En az 7 farklı olasılık yapısı kullanın ve her öngörüyü gerekçelendirin. Bir yerde geçmişe dair bir olasılık yapısı (may well have, is likely to have) kullanın ve dengeli bir kapanış yapın.",
          "Work in 2040: what's coming?\n\nIf anyone had told us in 2015 that millions of people would soon be working from their kitchens, few of us would have believed them. The pandemic may well have changed the world of work more in two years than the previous twenty. So what comes next? Nobody can say for certain, but here are my predictions.\n\nFirstly, remote and hybrid work are bound to remain common. Most companies have already invested in the technology, and many employees are unlikely to accept a return to five days in the office. The chances are that offices will become places for meetings and teamwork, rather than for everyday tasks.\n\nSecondly, artificial intelligence is likely to change almost every job. Routine tasks such as writing reports or analysing data may well be done mostly by machines. However, it is highly unlikely that AI will replace people completely. Instead, workers will in all likelihood need to learn how to work alongside it.\n\nFinally, I wouldn't be surprised if the four-day week became normal in many countries. Several trials have shown that productivity doesn't fall when people work fewer hours. That said, I doubt whether every industry will be able to adopt it.\n\nOf course, these changes won't benefit everyone equally. Workers without digital skills could well be left behind.\n\nIn short, the job market of 2040 is likely to be more flexible and more digital. Whether it will also be fairer is, for now, anyone's guess.",
          ["Belirsizliği kabul eden giriş", "En az 7 olasılık yapısı", "Geçmişe dair olasılık", "Gerekçeli öngörüler", "Dengeli kapanış"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

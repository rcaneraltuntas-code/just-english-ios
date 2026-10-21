"""C1 Ünite 3: Yollar."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("C1", 3, "Yollar", "Paths Not Taken",
         "Geçmişteki bir koşulun bugünkü sonucunu ve bugünkü bir durumun geçmişteki etkisini karma koşul cümleleriyle (mixed conditionals) anlatabilir, if yerine unless, provided that, but for gibi alternatifler kullanabilir ve resmî devrik koşul yapılarını (Had I known, Should you need) uygulayabilirim.",
         ["karma koşul: geçmiş koşul → bugünkü sonuç", "karma koşul: bugünkü durum → geçmişteki sonuç", "if alternatifleri: unless, provided that, as long as, otherwise, but for", "devrik koşul: Had I ..., Were I to ..., Should you ...", "hayat seçimleri üzerine düşünme yazısı"],
         ["hayat seçimleri ve dönüm noktaları", "kariyer ve kararlar", "alternatif tarih"],
         {"title": "Kayan kapılar", "durationMinutes": 45,
          "goal": "Öğrenciler hayatlarındaki bir dönüm noktasını seçer (bir okul, bir şehir, bir arkadaşlık) ve \"başka bir yol\" seçseler bugün hayatlarının nasıl olacağını karma koşul cümleleriyle anlatır. Ardından sınıf hep birlikte \"alternatif tarih\" senaryosu kurar (If the internet had never been invented, ...) ve zinciri devam ettirir."})

u.vocab([
    ("turning point", "dönüm noktası", "Moving to Ankara was a turning point.", "Ankara'ya taşınmak bir dönüm noktasıydı.", None),
    ("crossroads", "yol ayrımı", "I'm at a crossroads in my career.", "Kariyerimde bir yol ayrımındayım.", None),
    ("take a chance", "şansını denemek", "She took a chance and applied.", "Şansını deneyip başvurdu.", None),
    ("make a leap", "büyük bir adım atmak", "He made the leap and started his own business.", "Büyük adımı atıp kendi işini kurdu.", None),
    ("in retrospect", "geriye dönüp bakınca", "In retrospect, it was the right decision.", "Geriye dönüp bakınca doğru karardı.", None),
    ("hindsight", "sonradan görme, geç gelen akıl", "Hindsight is a wonderful thing.", "Sonradan akıl etmek kolay.", None),
    ("fate", "kader", "Was it fate or chance?", "Kader miydi, tesadüf mü?", None),
    ("coincidence", "tesadüf", "What a coincidence!", "Ne tesadüf!", None),
    ("consequence", "sonuç (çoğunlukla olumsuz)", "Every decision has consequences.", "Her kararın sonuçları vardır.", None),
    ("alternative", "alternatif", "There was no real alternative.", "Gerçek bir alternatif yoktu.", None),
    ("provided (that)", "-mek şartıyla", "You can go, provided that you're back by ten.", "Saat ona kadar dönmen şartıyla gidebilirsin.", None),
    ("as long as", "... sürece", "I'll help you as long as you try.", "Denediğin sürece sana yardım ederim.", None),
    ("unless", "-medikçe, -mezse", "I won't go unless you come with me.", "Sen benimle gelmezsen gitmem.", None),
    ("otherwise", "aksi takdirde", "Hurry up, otherwise we'll miss the train.", "Acele et, yoksa treni kaçıracağız.", None),
    ("but for", "... olmasaydı", "But for your help, I would have failed.", "Senin yardımın olmasaydı başarısız olurdum.", "resmî"),
    ("on condition that", "... koşuluyla", "He agreed on condition that he could work from home.", "Evden çalışabilmesi koşuluyla kabul etti.", None),
    ("suppose / supposing", "farz et ki", "Suppose you won the lottery, what would you do?", "Farz et ki piyangoyu kazandın, ne yapardın?", None),
    ("regret", "pişman olmak; pişmanlık", "I have no regrets.", "Hiç pişmanlığım yok.", None),
    ("settle for", "(daha azına) razı olmak", "Don't settle for less than you deserve.", "Hak ettiğinden daha azına razı olma.", None),
    ("pursue", "peşinden gitmek, sürdürmek", "She decided to pursue a career in music.", "Müzik kariyerinin peşinden gitmeye karar verdi.", None),
    ("drift", "sürüklenmek", "I drifted into teaching by accident.", "Öğretmenliğe tesadüfen sürüklendim.", None),
    ("path", "yol", "Everyone has to find their own path.", "Herkes kendi yolunu bulmalı.", None),
    ("what if", "ya ... olsaydı / olursa", "What if I had said yes?", "Ya evet deseydim?", None),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "O zaman şimdi ...", "Geçmişteki bir koşulun bugünkü sonucunu karma koşul cümlesiyle (If + past perfect, would + V1) anlatabilirim.",
    {"kind": "text", "title": "Bir blogdan: Kayan kapılar", "body": "Twelve years ago, I was offered a place to study law in Istanbul. At the last minute, I turned it down and went to a small university in Eskişehir to study music.\n\nPeople often ask me if I regret it. Honestly? Sometimes I wonder.\n\nIf I had studied law, I would probably be earning much more money now. I might be living in a big flat in the city, and my parents would definitely be prouder.\n\nBut if I hadn't gone to Eskişehir, I wouldn't have met my wife, who was in the same orchestra. And if I hadn't met her, we wouldn't have our two wonderful children.\n\nSo, no. I don't regret it. If I had taken the other path, I wouldn't be the person I am today.",
     "questions": [
        mc("What did the writer study?", ["Law", "Music", "Medicine"], 1, "\"went to a small university in Eskişehir to study music\""),
        mc("Does the writer regret the decision?", ["Yes, completely", "No", "The writer hasn't decided"], 1, "\"So, no. I don't regret it.\""),
     ]},
    {"explanation": "B2'de **third conditional**'ı öğrendiniz: geçmiş koşul → geçmiş sonuç.\n\n*If I had studied law, I **would have become** a lawyer.*\n\n**Mixed conditional (karma koşul) tip 1:** Geçmiş koşul → **bugünkü** sonuç\n\n| Koşul (geçmiş, gerçek dışı) | Sonuç (şimdi, gerçek dışı) |\n|---|---|\n| **If + past perfect** | **would / might / could + V1** |\n| If I **had studied** law, | I **would be** a lawyer **now**. |\n| If I **hadn't met** her, | we **wouldn't have** children. |\n| If she **had taken** the job, | she **would be living** in London. |\n\n**Karşılaştırın:**\n\n| Tip | Örnek | Sonuç ne zaman? |\n|---|---|---|\n| Third | If I had studied law, I **would have earned** more **last year**. | Geçmiş |\n| Mixed | If I had studied law, I **would earn** more **now**. | Şimdi |\n\n**İpucu:** Sonuç kısmında **now, today, still, at the moment** gibi zaman ifadeleri çoğu zaman karma koşula işarettir.\n\n**Sürekli hali:** *I **would be living** / **would be earning*** → şu an devam eden hayalî durum.",
     "examples": [{"en": "If I had saved more money, I wouldn't be in debt now.", "tr": "Daha fazla para biriktirmiş olsaydım şimdi borçlu olmazdım."},
                  {"en": "If they hadn't missed the flight, they would be in Rome today.", "tr": "Uçağı kaçırmasalardı bugün Roma'da olurlardı."},
                  {"en": "If she had accepted the offer, she would be living abroad.", "tr": "Teklifi kabul etseydi şimdi yurt dışında yaşıyor olurdu."}],
     "turkishNote": "Türkçede \"Hukuk okusaydım şimdi avukat olurdum\" cümlesi çok doğal bir yapıdır ve iki farklı zamanı rahatça birleştirir. İngilizcede bunun için \"If I had studied law, I would be a lawyer now\" demek gerekir. Türkçe konuşanların en sık hatası, iki kısmı da third conditional yapmaktır (\"I would have been a lawyer now\"); \"now\" kelimesi varsa sonuç kısmı \"would + V1\" olmalıdır."},
    [
        mc("\"Kahvaltı etseydim şimdi aç olmazdım.\"", ["If I had had breakfast, I wouldn't have been hungry now.", "If I had had breakfast, I wouldn't be hungry now."], 1, "Şimdi → would + V1."),
        mc("\"If I had learned to drive, I would have a car now.\" sonuç ne zaman?", ["Geçmiş", "Şimdi"], 1, "Mixed."),
        mc("Hangisi third conditional?", ["If she had left earlier, she would have caught the train.", "If she had left earlier, she would be here now."], 0, "Geçmiş → geçmiş."),
        mc("\"If I had moved to Spain, I would be speaking Spanish now.\" anlamı:", ["İspanya'ya taşındım.", "İspanya'ya taşınmadım, şimdi İspanyolca konuşmuyorum."], 1, "Gerçek dışı."),
        gap("If I ___ (take) that job, I would be living in Ankara now.", ["had taken"], "If + past perfect."),
        gap("If he hadn't broken his leg, he ___ (be) a professional footballer today.", ["would be"], "would + V1."),
        gap("If we had bought that house, we ___ (not / have) so much money now.", ["wouldn't have", "would not have"], "would + V1."),
        gap("If you had listened to me, you ___ (not / be) in this mess now.", ["wouldn't be", "would not be"], "would + V1."),
        listen("I almost didn't go to that party ten years ago. I was tired and wanted to stay at home. If I hadn't gone, I wouldn't have met Pelin, and I definitely wouldn't be living in Bodrum now with our dog and our little café.", "Konuşan partiye gitmeseydi ne olurdu?", ["Bodrum'a tatile giderdi", "Pelin'le tanışmaz ve şimdi Bodrum'da yaşamazdı", "Kafe açardı"], 1, "\"I wouldn't have met Pelin... wouldn't be living in Bodrum now\""),
        typ("Karma koşulla birleştirin: \"I didn't study for the exam. I'm worried now.\"", variants("If I had studied for the exam, I wouldn't be worried now.", "If I had studied for the exam, I would not be worried now.", "If I had studied for the exam I wouldn't be worried now."), "If I had studied for the exam, I wouldn't be worried now."),
    ],
    {"kind": "speaking", "task": speak("Hayatınızdaki 3 önemli kararı ya da olayı düşünün (bir okul, bir şehir, bir iş, bir kişi). Her biri için \"Başka türlü olsaydı bugün hayatım nasıl olurdu?\" sorusunu karma koşul cümleleriyle cevaplayın. En az birinde sürekli hali (would be living / working) kullanın.",
                                       "If I hadn't chosen to study engineering, I would probably be a teacher now, like my mother. If my family hadn't moved to Izmir when I was ten, I wouldn't speak with this accent, and I wouldn't have my best friend, who I met at school there. And if I had accepted that job offer in Germany three years ago, I would be living in Munich now and I might be speaking German quite well. But I'm happy with the path I took.",
                                       ["If + past perfect, would + V1", "Sürekli hali", "Third conditional ile karıştırmama"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "Öyle biri olmasaydım", "Bugünkü bir durumun ya da kişilik özelliğinin geçmişteki etkisini karma koşulla (If + past simple, would have + V3) anlatabilirim.",
    {"kind": "dialogue", "title": "Kaçırılan fırsat", "lines": [
        {"speaker": "Nil", "text": "Did you speak to the director at the conference?"},
        {"speaker": "Arda", "text": "No. I saw her, but I didn't say anything."},
        {"speaker": "Nil", "text": "Why not? It was the perfect chance!"},
        {"speaker": "Arda", "text": "I know. If I weren't so shy, I would have introduced myself."},
        {"speaker": "Nil", "text": "And if your English were better, you'd have asked her about the job."},
        {"speaker": "Arda", "text": "Exactly. If I didn't get so nervous in front of important people, I'd probably have a better job by now."},
        {"speaker": "Nil", "text": "Well, you can still email her. It's not too late."}],
     "questions": [
        mc("Why didn't Arda speak to the director?", ["She was busy.", "He's shy.", "He didn't see her."], 1, "\"If I weren't so shy, I would have introduced myself.\""),
        mc("What does Nil suggest?", ["Forget about it.", "Email the director.", "Go to another conference."], 1, "\"you can still email her\""),
     ]},
    {"explanation": "**Mixed conditional (karma koşul) tip 2:** **Bugünkü / genel** durum → **geçmişteki** sonuç\n\n| Koşul (şimdi / genel, gerçek dışı) | Sonuç (geçmiş, gerçek dışı) |\n|---|---|\n| **If + past simple** | **would / might / could + have + V3** |\n| If I **weren't** so shy, | I **would have introduced** myself. |\n| If my English **were** better, | I **would have asked** her. |\n| If he **didn't live** so far away, | he **would have come** to the party. |\n\nBu yapı genellikle **kalıcı bir özellik** (kişilik, yetenek, durum) yüzünden geçmişte bir şeyin olmadığını anlatır.\n\n**Gerçek durum:**\n\n- *I'm shy* (her zaman) → *I didn't introduce myself* (geçmişte)\n- → ***If I weren't** so shy, I **would have introduced** myself.*\n\n**Karşılaştırın:**\n\n| Tip | Örnek |\n|---|---|\n| Second | If I **weren't** shy, I **would talk** to people. (genel → genel) |\n| Mixed 2 | If I **weren't** shy, I **would have talked** to her **yesterday**. (genel → geçmiş) |\n\n**Not:** Resmî dilde **If I / he / she were** tercih edilir; günlük dilde **was** de duyulur.",
     "examples": [{"en": "If I weren't afraid of flying, I would have visited you in Canada.", "tr": "Uçmaktan korkmasaydım seni Kanada'da ziyaret ederdim."},
                  {"en": "If she spoke French, she would have got the job in Paris.", "tr": "Fransızca konuşsaydı Paris'teki işi alırdı."},
                  {"en": "If he were more organised, he wouldn't have missed the deadline.", "tr": "Daha düzenli biri olsaydı son tarihi kaçırmazdı."}],
     "turkishNote": "Türkçede \"Bu kadar utangaç olmasaydım kendimi tanıtırdım\" cümlesindeki \"olmasaydım\" hem geçmişi hem genel durumu kapsar. İngilizcede ise kişilik özelliği (şimdi de utangaçsınız) past simple ile (If I weren't), geçmişteki sonuç ise would have + V3 ile (I would have introduced) verilir. İlk kısmı \"If I hadn't been so shy\" yapmak da mümkündür, ama bu o anki geçici bir durumu anlatır; kalıcı özellik için past simple daha doğaldır."},
    [
        mc("Kalıcı özellik → geçmiş sonuç:", ["If I weren't so lazy, I would have finished the project.", "If I weren't so lazy, I would finish the project."], 0, "would have + V3."),
        mc("\"If she lived nearer, she would have come.\" gerçek durum:", ["Yakında yaşıyor ve geldi.", "Uzakta yaşıyor ve gelmedi."], 1, "Gerçek dışı."),
        mc("Resmî dilde:", ["If I was you, ...", "If I were you, ..."], 1, "were."),
        mc("\"Yüzme bilseydim o gün denize girerdim.\"", ["If I could swim, I would have gone into the sea that day.", "If I could swim, I would go into the sea that day."], 0, "Mixed 2."),
        gap("If I ___ (be) taller, I would have joined the basketball team.", ["were", "was"], "If + past simple."),
        gap("If he didn't talk so much, he ___ (hear) what she said.", ["would have heard"], "would have + V3."),
        gap("If I ___ (not / have) a fear of heights, I would have climbed the tower.", ["didn't have"], "If + past simple."),
        gap("If she were more patient, she ___ (not / shout) at the children yesterday.", ["wouldn't have shouted", "would not have shouted"], "would have + V3."),
        listen("My brother is terrible with money. If he weren't so careless, he would have bought a house years ago. Instead, he spent everything on cars and holidays. And if he didn't trust everyone so easily, he wouldn't have lost his savings in that strange business deal.", "Kardeşin parasını neden kaybettiğini düşünüyor?", ["Kötü şans", "Herkese kolayca güvendiği için", "Yanlış bankayı seçtiği için"], 1, "\"if he didn't trust everyone so easily, he wouldn't have lost his savings\""),
        typ("Karma koşulla birleştirin: \"I don't speak German. I didn't understand the film.\"", variants("If I spoke German, I would have understood the film.", "If I could speak German, I would have understood the film.", "If I spoke German I would have understood the film."), "If I spoke German, I would have understood the film."),
    ],
    {"kind": "speaking", "task": speak("Kendinizin ya da tanıdığınız birinin 3 kalıcı özelliğini düşünün (utangaçlık, sabırsızlık, bir dili bilmemek, korkular, vb.). Bu özellikler yüzünden geçmişte olan ya da olmayan şeyleri karma koşul cümleleriyle (If + past simple, would have + V3) anlatın. Ardından bir cümleyle iki karma koşul tipini birleştirin.",
                                       "I'm quite impatient. If I were more patient, I wouldn't have argued with my manager last week. I'm also afraid of the sea. If I weren't afraid of the sea, I would have tried diving when we went to Kaş. And my best friend doesn't speak English. If she spoke English, she would have come to London with me. Finally, if I hadn't grown up in a big family, I wouldn't be so good at sharing, and I wouldn't have survived living with four flatmates!",
                                       ["If + past simple, would have + V3", "Kalıcı özellik / geçmiş sonuç mantığı", "İki tipi karşılaştırma"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "If yerine", "unless, provided that, as long as, on condition that, otherwise, suppose ve but for gibi if alternatiflerini doğru anlamla kullanabilirim.",
    {"kind": "text", "title": "Bir burs ilanından", "body": "THE YOUNG RESEARCHERS SCHOLARSHIP\n\nWe offer full funding for a one-year research project abroad, provided that applicants meet the following conditions.\n\nApplicants must be under 30. Applications will not be accepted unless they include two letters of recommendation.\n\nYou may choose any university, as long as it has an agreement with our foundation.\n\nThe scholarship is awarded on condition that the student returns to Turkey and works here for at least two years. Otherwise, the full amount must be paid back.\n\nSuppose you are accepted but cannot travel for health reasons: in this case, the start date may be postponed for up to six months.\n\nBut for the generous support of our donors, this programme would not exist. We thank them all.",
     "questions": [
        mc("What must applications include?", ["A passport photo", "Two letters of recommendation", "A research budget"], 1, "\"unless they include two letters of recommendation\""),
        mc("What happens if the student doesn't work in Turkey for two years?", ["Nothing", "They must pay the money back.", "They lose their degree."], 1, "\"Otherwise, the full amount must be paid back.\""),
     ]},
    {"explanation": "| Bağlaç | Anlam | Örnek |\n|---|---|---|\n| **unless** | if ... not (-mezse) | I won't go **unless** you come. (= if you don't come) |\n| **provided / providing (that)** | -mek şartıyla (resmî) | You can borrow it **provided that** you return it. |\n| **as long as / so long as** | ... sürece | **As long as** you're happy, I'm happy. |\n| **on condition that** | ... koşuluyla (çok resmî) | He was released **on condition that** he left the country. |\n| **suppose / supposing** | farz et ki | **Supposing** you lost your job, what would you do? |\n| **otherwise** | aksi takdirde | Leave now. **Otherwise**, you'll be late. |\n| **but for** + isim | ... olmasaydı (resmî) | **But for** your help, I would have failed. |\n| **without** + isim | ... olmadan / olmasaydı | **Without** the internet, life would be very different. |\n| **in case** | ihtimaline karşı (≠ if) | Take an umbrella **in case** it rains. |\n\n**Dikkat:**\n\n- **unless** zaten olumsuzdur: ~~Unless you don't come~~ ✗ → **Unless you come** ✓\n- Zaman kuralı **if** ile aynıdır: ~~provided that you will return~~ → **provided that you return**\n- **in case** ≠ **if**: *I'll take an umbrella **if** it rains.* (Yağarsa alırım.) / *I'll take an umbrella **in case** it rains.* (Yağma ihtimaline karşı şimdi alırım.)",
     "examples": [{"en": "You can't enter unless you have a ticket.", "tr": "Biletin yoksa giremezsin."},
                  {"en": "I'll lend you my car as long as you drive carefully.", "tr": "Dikkatli sürdüğün sürece arabamı sana ödünç veririm."},
                  {"en": "But for the doctor's quick action, he would have died.", "tr": "Doktorun hızlı müdahalesi olmasaydı ölürdü."}],
     "turkishNote": "Türkçede \"-mezse\" ve \"-medikçe\" ekleri İngilizcede \"unless\" ile karşılanır, ama unless zaten olumsuz anlam taşıdığı için ardından olumsuz fiil gelmez: \"Unless you don't hurry\" yanlıştır. Bir diğer yaygın karışıklık \"in case\" ile \"if\" arasındadır: \"in case\" Türkçedeki \"... ihtimaline karşı\" anlamındadır ve önlem bildirir."},
    [
        mc("Hangisi doğru?", ["Unless you don't study, you'll fail.", "Unless you study, you'll fail."], 1, "unless zaten olumsuz."),
        mc("\"Take a jacket in case it gets cold.\" anlamı:", ["Soğuk olursa ceket al.", "Soğuk olma ihtimaline karşı ceket al."], 1, "in case = önlem."),
        mc("Hangisi doğru?", ["Provided that you will pay, you can stay.", "Provided that you pay, you can stay."], 1, "Zaman kuralı."),
        mc("\"But for the rain, we would have won.\" anlamı:", ["Yağmur sayesinde kazandık.", "Yağmur olmasaydı kazanırdık."], 1, "but for."),
        gap("I won't sign the contract ___ they change this clause. (-mezlerse)", ["unless"], "unless."),
        gap("You can stay out late as ___ as you call me.", ["long"], "as long as."),
        gap("Hurry up. ___, we'll miss the start of the film. (Aksi takdirde)", ["Otherwise"], "Otherwise."),
        gap("___ you won a million dollars, what would you do? (Farz et ki)", ["Suppose", "Supposing", "Imagine"], "Suppose."),
        listen("Yes, you can use my flat while I'm away, provided that you water the plants and feed the cat. And please don't have any parties, unless you want the neighbours to call me. Oh, and take my spare key in case you lose yours.", "Konuşan neden yedek anahtarı veriyor?", ["Kedi için", "Diğer anahtarı kaybetme ihtimaline karşı", "Komşu için"], 1, "\"in case you lose yours\""),
        typ("Unless ile yeniden yazın: \"If you don't leave now, you'll miss the bus.\"", variants("Unless you leave now, you'll miss the bus.", "Unless you leave now, you will miss the bus.", "You'll miss the bus unless you leave now."), "Unless you leave now, you'll miss the bus."),
    ],
    {"kind": "speaking", "task": speak("Bir arkadaşınız sizden bir şey ödünç istiyor (arabanız, eviniz, köpeğinize bakmak). Koşullarınızı en az 5 farklı bağlaçla belirtin: provided that, as long as, unless, on condition that, otherwise, in case. Ardından but for ya da without ile hayatınızda size yardım eden biri hakkında bir cümle kurun.",
                                       "Sure, you can borrow my car for the weekend, provided that you fill up the tank before you bring it back. You can drive it to the coast as long as you don't go on the motorway at night. Don't let anyone else drive it unless you've asked me first. I'll lend it to you on condition that you wash it! Keep the insurance papers in the glove box in case the police stop you. And please be careful, otherwise my dad will kill me. By the way, but for my uncle, I would never have learned to drive.",
                                       ["Çeşitli koşul bağlaçları", "unless doğru", "in case anlamı", "but for / without"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Bilseydim", "Had I known, Were I to ve Should you need gibi devrik koşul yapılarını resmî bağlamlarda kullanabilirim.",
    {"kind": "text", "title": "Resmî yazışmalar", "body": "Email 1\n\"Dear Ms Erdem,\nThank you for your application. Should you require any further information about the position, please do not hesitate to contact me.\"\n\nEmail 2\n\"Dear Mr Taylan,\nHad we been informed of the delay earlier, we would have been able to make alternative arrangements. We would therefore ask you to keep us updated in future.\"\n\nSpeech\n\"Were the government to introduce this tax, thousands of small businesses would close. Were it not for their hard work, our local economy would collapse.\"\n\nNote\n\"Had it not been for your support this year, I would never have finished my thesis. Thank you.\"",
     "questions": [
        mc("What does the writer of Email 2 complain about?", ["They were informed about the delay too late.", "The product was broken.", "The price was too high."], 0, "\"Had we been informed of the delay earlier...\""),
        mc("What does the speaker say about the tax?", ["It would help businesses.", "Thousands of small businesses would close.", "It's already been introduced."], 1, "\"thousands of small businesses would close\""),
     ]},
    {"explanation": "Resmî İngilizcede **if** düşürülerek yardımcı fiil başa alınabilir. Anlam değişmez, ama üslup **daha resmî ve edebi** olur.\n\n| Normal | Devrik | Tip |\n|---|---|---|\n| **If** you **should** need help, ... | **Should** you need help, ... | 1st (olası) |\n| **If** I **were to** lose my job, ... | **Were** I **to** lose my job, ... | 2nd (hayalî gelecek) |\n| **If** I **were** you, ... | **Were** I you, ... (çok resmî, nadir) | 2nd |\n| **If** I **had known**, ... | **Had** I **known**, ... | 3rd / mixed |\n| **If** it **weren't for** ... | **Were it not for** ... | 2nd (... olmasaydı) |\n| **If** it **hadn't been for** ... | **Had it not been for** ... | 3rd (... olmasaydı) |\n\n**Should** + özne + V1 → \"... olursa / gerekirse\" (resmî mektup, e-posta, talimat):\n\n- ***Should you have** any questions, please contact us.*\n\n**Were** + özne + **to** + V1 → \"... olsa / olacak olsa\" (olası ama pek beklenmeyen gelecek):\n\n- ***Were the company to close**, 500 people would lose their jobs.*\n\n**Olumsuz:** **not** öznenin **sonuna** gelir, kısaltılmaz:\n\n- ***Had I not seen** it, I wouldn't have believed it.* (~~Hadn't I seen~~ ✗)\n\n**Not:** Bu yapılar resmî yazı ve konuşmada etkilidir; günlük sohbette **if** kullanın.",
     "examples": [{"en": "Should you need any assistance, please call reception.", "tr": "Herhangi bir yardıma ihtiyacınız olursa lütfen resepsiyonu arayın."},
                  {"en": "Had I known about the traffic, I would have taken the metro.", "tr": "Trafiği bilseydim metroya binerdim."},
                  {"en": "Were it not for tourism, the island would be empty.", "tr": "Turizm olmasaydı ada boş olurdu."}],
     "turkishNote": "Türkçede resmî yazışmada \"... olması halinde\", \"... olmasaydı\" gibi yapılar kullanılır; İngilizcede bunların karşılığı \"Should you require...\" ve \"Had it not been for...\" gibi devrik yapılardır. Türkçe konuşanların en sık hatası olumsuz hali kısaltmaktır: \"Hadn't I known\" yanlıştır, \"Had I not known\" doğrudur. Bu yapıları iş e-postalarınızda ölçülü kullanmak çok profesyonel bir izlenim bırakır."},
    [
        mc("Hangisi doğru?", ["Had I known, I would have called.", "Had I knew, I would have called."], 0, "Had + V3."),
        mc("Hangisi doğru?", ["Hadn't she helped, I'd have failed.", "Had she not helped, I'd have failed."], 1, "Had + özne + not."),
        mc("\"Should you need help, call me.\" anlamı:", ["Yardıma ihtiyacın olmalı.", "Yardıma ihtiyacın olursa beni ara."], 1, "Should = if."),
        mc("En uygun bağlam:", ["Arkadaşa mesaj: Should you want pizza, tell me.", "Otel e-postası: Should you require anything, please contact reception."], 1, "Resmî."),
        gap("___ you have any questions, please do not hesitate to contact us.", ["Should"], "Should + özne + V1."),
        gap("___ I known about the problem, I would have helped. (Bilseydim)", ["Had"], "Had I known."),
        gap("Were the company ___ close, many people would lose their jobs.", ["to"], "Were ... to."),
        gap("Had it not ___ for her advice, I would have made a terrible mistake.", ["been"], "Had it not been for."),
        listen("Good evening. Had we not acted quickly last year, the factory would have closed. Were we to lose this new contract, we would face the same danger again. Should anyone have any doubts, my door is always open.", "Konuşan ne zaman \"kapım açık\" diyor?", ["Herkes kapıyı açarsa", "Şüphesi olan olursa", "Fabrika kapanırsa"], 1, "\"Should anyone have any doubts, my door is always open.\""),
        typ("Devrik koşulla yeniden yazın: \"If I had seen the sign, I would have stopped.\"", variants("Had I seen the sign, I would have stopped.", "Had I seen the sign I would have stopped."), "Had I seen the sign, I would have stopped."),
    ],
    {"kind": "speaking", "task": speak("Bir şirket müdürü olarak çalışanlarınıza yılsonu konuşması yapın (1 dakika). Geçen yılı Had we not ... / Had it not been for ..., gelecekteki riskleri Were we to ..., ve son olarak bir davet Should anyone ... yapılarıyla anlatın. En az 4 devrik koşul kullanın.",
                                       "Good evening, everyone. This has been a difficult year. Had we not worked together so closely, we would never have survived the crisis in the spring. Had it not been for our sales team, we would have lost our biggest client. Looking ahead, were we to expand into new markets next year, we would need to hire at least twenty new people. And were it not for your hard work, none of this would be possible. Should anyone have ideas for next year, please come and talk to me. Thank you.",
                                       ["Had / Were / Should devrik", "Olumsuz devrik doğru (Had we not)", "Resmî ton", "Mantıklı zaman"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Seçilmeyen yol", "Karma koşullar, if alternatifleri ve devrik koşullarla hayattaki seçimler üzerine düşündüren bir kişisel deneme yazabilirim.",
    {"kind": "text", "title": "Kişisel deneme: İki şehir", "body": "When I was twenty-two, I had two job offers on the table: one in a large bank in Istanbul, the other in a small non-profit organisation in Diyarbakır.\n\nEveryone told me to take the bank job. It paid three times as much, and it was in the city where I had grown up. Had I listened to them, I would probably be a senior manager by now. I would be living close to my parents, and I wouldn't have spent the first two years of my career sleeping in a rented room with no heating.\n\nBut I chose Diyarbakır, and I have never regretted it.\n\nIf I hadn't gone, I wouldn't speak Kurdish, which I now use every day in my work. I wouldn't have learned that the best teachers are often not in classrooms. And I certainly wouldn't be the person I am today: more patient, more curious and far less afraid of the unknown.\n\nOf course, I sometimes wonder. Were I to go back in time, would I make the same choice? Probably, provided that I could take a good winter coat with me.\n\nThe truth is, we can never know where the other path would have led. What we can do is make sure that, whichever road we take, we walk it with our eyes open.",
     "questions": [
        mc("Why did people advise the writer to take the bank job?", ["It was more interesting.", "It paid more and was in their home city.", "It was in Diyarbakır."], 1, "\"It paid three times as much, and it was in the city where I had grown up.\""),
        mc("How does the writer feel about the decision?", ["They regret it.", "They have never regretted it.", "They're not sure."], 1, "\"I have never regretted it.\""),
     ]},
    {"explanation": "**Düşündüren kişisel denemenin (reflective essay) özellikleri:**\n\n| Özellik | Teknik | Örnek |\n|---|---|---|\n| **Somut bir an** | Kesin bir zaman ve seçim | *When I was twenty-two, I had two job offers ...* |\n| **Alternatif yol** | Karma ve third conditional | *Had I listened to them, I would be a manager by now.* |\n| **Seçilen yolun sonuçları** | Karma koşul, olumsuz | *If I hadn't gone, I wouldn't speak Kurdish.* |\n| **Dürüstlük ve ironi** | Mizahla dengelenen duygu | *... provided that I could take a good winter coat.* |\n| **Evrensel ders** | Kişiselden genele geçiş | *What we can do is make sure that ...* |\n\n**Koşul yapılarını çeşitlendirmek:**\n\n- Karma tip 1: *If I hadn't gone, I **wouldn't speak** ...*\n- Karma tip 2: *If I **were** braver, I **would have** ...*\n- Third: *If I had stayed, I **would have missed** ...*\n- Devrik: ***Had I** listened ... / **Were I to** go back ...*\n- Alternatifler: *provided that, unless, but for, otherwise*\n- **would have led** gibi **belirsiz geçmiş**: *We can never know where the other path **would have led**.*\n\n**Dikkat:** Aynı yapıyı sürekli tekrarlamak (If ... would ... If ... would ...) metni monotonlaştırır. Yapıları karıştırın ve aralara **kısa, sade cümleler** ekleyin: *But I chose Diyarbakır.*",
     "examples": [{"en": "Had I listened to them, I would be a manager by now.", "tr": "Onları dinleseydim şimdiye müdür olmuştum."},
                  {"en": "If I hadn't moved, I wouldn't have the friends I have today.", "tr": "Taşınmasaydım bugünkü arkadaşlarım olmazdı."},
                  {"en": "We can never know where the other path would have led.", "tr": "Öteki yolun nereye çıkacağını asla bilemeyiz."}],
     "turkishNote": "Türkçe kişisel denemelerde \"keşke\" ve \"-saydım\" yapıları sık tekrarlanır. İngilizcede aynı düşünceyi farklı yapılarla (karma koşul, devrik koşul, wish, provided that) ifade etmek metne derinlik ve akıcılık katar. Ayrıca İngilizce reflective writing'de duygusal anlatım genellikle hafif bir mizah ya da ironiyle dengelenir; bu, metni daha samimi ve okunabilir yapar."},
    [
        mc("İyi bir reflective essay girişi:", ["Life is full of choices.", "When I was twenty-two, I had two job offers on the table."], 1, "Somut an."),
        mc("Yapı çeşitliliği için en iyisi:", ["Her cümlede If ... would", "Karma, devrik ve alternatif yapıları karıştırmak"], 1, "Çeşitlilik."),
        mc("\"Had I stayed, I would be living in Istanbul now.\" tipi:", ["Third conditional", "Devrik karma koşul"], 1, "Had + V3 → would + V1 now."),
        mc("İyi bir kapanış:", ["The end.", "What we can do is make sure that we walk our path with our eyes open."], 1, "Evrensel ders."),
        gap("Had I ___ (choose) the other job, I would be richer now.", ["chosen"], "Had + V3."),
        gap("If I hadn't moved abroad, I ___ (not / speak) three languages now.", ["wouldn't speak", "would not speak"], "Karma."),
        gap("We can never know where the other road ___ have led.", ["would"], "would have led."),
        gap("I'd make the same choice again, ___ that I could take a warmer coat. (şartıyla)", ["provided", "providing"], "provided that."),
        listen("I often think about the scholarship I turned down. Had I accepted it, I would be living in Canada now. But if I had gone, I wouldn't have been here when my father got ill, and I would never have forgiven myself. So I think I made the right choice.", "Konuşan bursu neden reddettiği için mutlu?", ["Kanada'yı sevmediği için", "Babası hastalandığında yanında olabildiği için", "Para yeterli değildi"], 1, "\"I wouldn't have been here when my father got ill\""),
        typ("Devrik karma koşulla yazın: \"I didn't learn Spanish as a child, so I don't speak it now.\" (Had I)", variants("Had I learned Spanish as a child, I would speak it now.", "Had I learnt Spanish as a child, I would speak it now.", "Had I learned Spanish as a child, I would be able to speak it now."), "Had I learned Spanish as a child, I would speak it now."),
    ],
    {"kind": "writing", "task": write("\"The road not taken\" (Seçilmeyen yol) başlıklı kişisel bir deneme yazın (250–300 kelime). Hayatınızdaki gerçek ya da hayalî bir yol ayrımını anlatın. Somut bir anla başlayın; seçmediğiniz yolun sizi bugün nereye götürebileceğini ve seçtiğiniz yolun size kattıklarını anlatın. En az 2 karma koşul (iki farklı tip), 2 devrik koşul (Had I ..., Were I to ...) ve 2 if alternatifi (unless, provided that, but for, otherwise) kullanın. Evrensel bir düşünceyle bitirin.",
                                      "The road not taken\n\nIt was a rainy afternoon in June, and I was standing outside the music conservatory in Ankara with an acceptance letter in my hand. My father, who had driven me there, was waiting in the car. He wanted me to study engineering.\n\nI walked back to the car and handed him the letter. Then I told him I wasn't going.\n\nNearly fifteen years later, I'm a civil engineer. Had I gone to the conservatory, I would probably be a violin teacher now, or perhaps playing in an orchestra somewhere in Europe. I wouldn't be designing bridges, and I certainly wouldn't spend my weekends on muddy construction sites.\n\nAnd yet, if I weren't such a practical person, I would have chosen music without a second thought. Part of me has always wanted to be braver.\n\nBut the road I took has given me things I could never have imagined. But for my job, I would never have travelled to the mountains of eastern Turkey, where I helped build a bridge that now connects two villages. If I hadn't become an engineer, I wouldn't know the joy of seeing a child walk safely to school across something I designed.\n\nI still play the violin every evening. Were I to start again, would I choose differently? I don't think so, provided that I could still keep music in my life. Otherwise, something important would be missing.\n\nPerhaps the point is not to find the \"right\" road, but to bring the best parts of the other one with you.",
                                      ["Somut başlangıç", "İki tip karma koşul", "Devrik koşullar", "if alternatifleri", "Evrensel ve güçlü kapanış"])},
)

u.test([
    mc("\"Daha erken kalksaydım şimdi yorgun olmazdım.\" (Ama değil: geç kalktım, yorgunum)", ["If I had got up earlier, I wouldn't have been tired now.", "If I had got up earlier, I wouldn't be tired now."], 1, "Mixed 1"),
    mc("\"If I weren't so shy, I would have spoken to her.\" gerçek:", ["Utangaç değilim, konuştum.", "Utangacım, konuşmadım."], 1, "Mixed 2"),
    mc("Hangisi doğru?", ["Unless you don't hurry, you'll be late.", "Unless you hurry, you'll be late."], 1, "unless"),
    mc("Hangisi doğru?", ["Hadn't I seen it, I wouldn't have believed it.", "Had I not seen it, I wouldn't have believed it."], 1, "Had I not"),
    mc("\"Take an umbrella in case it rains.\"", ["Yağmur yağarsa şemsiye al.", "Yağmur ihtimaline karşı şemsiye al."], 1, "in case"),
    gap("If she ___ (accept) the job, she would be living in Berlin now.", ["had accepted"], "If + past perfect"),
    gap("If I spoke Italian, I ___ (understand) what they said yesterday.", ["would have understood"], "would have + V3"),
    gap("You can borrow it as ___ as you give it back tomorrow.", ["long"], "as long as"),
    gap("___ you need any help, please contact reception. (resmî)", ["Should"], "Should you"),
    gap("___ it not been for your help, I would have failed.", ["Had"], "Had it not been for"),
    gap("Were the government ___ raise taxes, prices would rise.", ["to"], "Were ... to"),
    mc("\"But for the map, we would have got lost.\"", ["Harita sayesinde kaybolduk.", "Harita olmasaydı kaybolurduk."], 1, "but for"),
    listen("If I hadn't failed my driving test three times, I wouldn't have started cycling to work. And if I didn't cycle every day, I wouldn't be as fit as I am now. So, in a strange way, failing was the best thing that happened to me.", "Konuşan başarısız olmayı neden iyi buluyor?", ["Ehliyet almadı ve mutlu", "Bisiklete başladı ve şimdi formda", "Para biriktirdi"], 1, "\"I wouldn't have started cycling... I wouldn't be as fit\""),
    typ("Devrik koşulla yeniden yazın: \"If I had known you were coming, I would have cooked.\"", variants("Had I known you were coming, I would have cooked.", "Had I known that you were coming, I would have cooked."), "Had I known you were coming, I would have cooked."),
    write("\"Alternatif tarih\": Tarihte ya da teknolojide bir olay farklı gelişseydi bugün dünya nasıl olurdu? (İnternet hiç icat edilmeseydi, matbaa olmasaydı, insanlar Ay'a gitmeseydi, vb.) Bir makale yazın (230–280 kelime). Karma koşulları (iki tip), third conditional'ı, en az 2 devrik koşulu ve en az 2 if alternatifini (without, but for, unless, provided that) kullanın. Bir giriş, iki gelişme paragrafı ve bir sonuç yazın.",
          "A world without the internet\n\nIt is difficult to imagine life without the internet. Yet only forty years ago, very few people had heard of it. So what would the world look like today had it never been invented?\n\nFirstly, the way we communicate would be completely different. If the internet hadn't been created, we would still be writing letters and making expensive international phone calls. Families living in different countries would see each other far less often, and many friendships would have faded with time. Without social media, news would travel more slowly, and governments would find it easier to control what people know.\n\nSecondly, the global economy would look very different. Had online shopping never existed, millions of small businesses would never have found customers abroad. Many of today's biggest companies wouldn't exist, and many people who now work from home would be commuting every day. On the other hand, if we weren't so dependent on technology, we might have developed a healthier balance between work and rest. Perhaps fewer of us would have suffered from stress caused by constantly checking our phones.\n\nOf course, some things would be better. But for the internet, we would probably read more books and spend more time talking face to face. Were we to lose it tomorrow, however, I doubt that most people would feel relieved.\n\nIn conclusion, the internet has changed almost every part of our lives. Unless something dramatic happens, it will continue to shape the future, provided that we learn to use it wisely.",
          ["Karma koşullar (iki tip)", "Third conditional ve devrik koşul", "if alternatifleri", "Mantıklı yapı", "C1 dil düzeyi"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

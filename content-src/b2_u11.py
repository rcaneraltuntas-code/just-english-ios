"""B2 Ünite 11: Para."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("B2", 11, "Para", "Money",
         "Parayla ilgili doğal kelime eşlemelerini (collocations) kullanabilir, -ing ve -ed sıfatlarını doğru seçebilir, ekonomik eğilimleri ve grafikleri betimleyebilir ve kişisel finans hakkında tavsiye veren bir yazı yazabilirim.",
         ["para fiilleri ve collocations", "-ing ve -ed sıfatları", "ekonomi collocations: sıfat + isim", "eğilimleri betimleme: rise sharply, a slight fall", "tavsiye ve kişisel finans yazısı"],
         ["kişisel finans", "ekonomi", "alışveriş ve tüketim"],
         {"title": "Bütçe meclisi", "durationMinutes": 45,
          "goal": "Gruplar hayali bir öğrenci evinin aylık bütçesini alır: gelir, kira, faturalar, yemek. Para birdenbire %20 azalır. Gruplar neyi keseceklerini collocation'larla tartışır (cut back on, save up for, can't afford). Sonra grafiği sınıfa betimler ve en yaratıcı tasarruf planını oylarlar."})

u.vocab([
    ("earn", "kazanmak (çalışarak)", "She earns a good salary.", "İyi bir maaş kazanıyor.", None),
    ("afford", "(parası) yetmek", "We can't afford a new car.", "Yeni bir arabaya paramız yetmez.", None),
    ("borrow", "ödünç almak", "Can I borrow some money?", "Biraz borç alabilir miyim?", None),
    ("lend", "ödünç vermek", "I lent him 500 lira.", "Ona 500 lira borç verdim.", None),
    ("owe", "borçlu olmak", "How much do I owe you?", "Sana ne kadar borcum var?", None),
    ("debt", "borç", "They're trying to get out of debt.", "Borçtan kurtulmaya çalışıyorlar.", "b sessiz"),
    ("loan", "kredi, borç", "He took out a loan to buy a flat.", "Daire almak için kredi çekti.", None),
    ("pay off", "(borcu) ödeyip bitirmek", "It took them ten years to pay off the loan.", "Krediyi ödeyip bitirmeleri on yıl sürdü.", None),
    ("save up (for)", "(bir şey için) para biriktirmek", "I'm saving up for a holiday.", "Tatil için para biriktiriyorum.", None),
    ("cut back (on)", "(harcamayı) azaltmak", "We need to cut back on eating out.", "Dışarıda yemeyi azaltmamız gerek.", None),
    ("budget", "bütçe", "We're on a tight budget this month.", "Bu ay bütçemiz kısıtlı.", None),
    ("income", "gelir", "Rent takes up half of my income.", "Kira gelirimin yarısını götürüyor.", None),
    ("expenses", "giderler, masraflar", "Our monthly expenses have gone up.", "Aylık giderlerimiz arttı.", None),
    ("bill", "fatura", "I paid the electricity bill.", "Elektrik faturasını ödedim.", None),
    ("interest rate", "faiz oranı", "Interest rates have risen again.", "Faiz oranları yine yükseldi.", None),
    ("inflation", "enflasyon", "High inflation makes everything more expensive.", "Yüksek enflasyon her şeyi pahalılaştırır.", None),
    ("cost of living", "hayat pahalılığı, geçim maliyeti", "The cost of living has risen sharply.", "Geçim maliyeti keskin bir şekilde arttı.", None),
    ("worth", "değerinde, değer", "Is it worth the money?", "Parasına değer mi?", None),
    ("bargain", "kelepir", "These shoes were a real bargain.", "Bu ayakkabılar tam bir kelepirdi.", None),
    ("rip-off", "kazık (aşırı pahalı)", "Twenty euros for a coffee? What a rip-off!", "Bir kahveye yirmi avro mu? Ne kazık!", "samimi"),
    ("invest (in)", "yatırım yapmak", "She invested her savings in gold.", "Birikimlerini altına yatırdı.", None),
    ("savings", "birikim", "I spent all my savings on the trip.", "Bütün birikimimi geziye harcadım.", None),
    ("sharply", "keskin bir şekilde", "Prices rose sharply last year.", "Fiyatlar geçen yıl keskin bir şekilde yükseldi.", None),
    ("steadily", "istikrarlı bir şekilde", "Sales have grown steadily.", "Satışlar istikrarlı bir şekilde arttı.", None),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Kazanmak, harcamak, biriktirmek", "Parayla ilgili fiilleri ve kelime eşlemelerini doğal bir şekilde kullanabilirim.",
    {"kind": "dialogue", "title": "Ay sonu", "lines": [
        {"speaker": "Barış", "text": "Can you lend me 200 lira until Friday? I'm completely broke."},
        {"speaker": "Gamze", "text": "Again? You already owe me 300 from last month."},
        {"speaker": "Barış", "text": "I know, I know. I'll pay you back, I promise. The rent went up, and I had to pay the electricity bill."},
        {"speaker": "Gamze", "text": "You earn a decent salary. Where does it all go?"},
        {"speaker": "Barış", "text": "Honestly? Takeaways, mostly. And I bought a new phone."},
        {"speaker": "Gamze", "text": "You need to make a budget and cut back on takeaways. Otherwise, you'll never save any money."}],
     "questions": [
        mc("How much does Barış already owe Gamze?", ["200 lira", "300 lira", "500 lira"], 1, "\"You already owe me 300\""),
        mc("What does Gamze suggest?", ["Getting a second job", "Making a budget and cutting back on takeaways", "Borrowing from the bank"], 1, "\"make a budget and cut back on takeaways\""),
     ]},
    {"explanation": "**Sık karıştırılan para fiilleri:**\n\n| Fiil | Anlam | Örnek |\n|---|---|---|\n| **borrow** (from) | ödünç **almak** | I **borrowed** 100 lira **from** my sister. |\n| **lend** (to) | ödünç **vermek** | My sister **lent** me 100 lira. |\n| **owe** | borçlu olmak | I **owe** her 100 lira. |\n| **pay back** | borcu geri ödemek | I'll **pay** you **back** on Friday. |\n| **earn** | (çalışarak) kazanmak | She **earns** 40,000 a month. |\n| **win** | (yarışma/şans) kazanmak | He **won** the lottery. |\n| **afford** | parası yetmek | I **can't afford** it. |\n\n**Doğal kelime eşlemeleri (collocations):**\n\n| Fiil | + isim |\n|---|---|\n| **make** | money, a profit, a loss, a living |\n| **save** | money, time / **save up for** a car |\n| **spend** | money **on** sth, time |\n| **waste** | money **on** sth, time |\n| **take out** | a loan, a mortgage (konut kredisi) |\n| **pay off** | a loan, a debt |\n| **get into / get out of** | debt |\n| **live on** | a low income, 20,000 a month |\n\n**Dikkat:** ~~earn money from the lottery~~ → **win** money. / ~~make a budget~~ ve **set a budget** ikisi de kullanılır.",
     "examples": [{"en": "I owe my brother 1,000 lira.", "tr": "Kardeşime 1.000 lira borcum var."},
                  {"en": "They took out a loan to start a business.", "tr": "İş kurmak için kredi çektiler."},
                  {"en": "It's hard to live on a student budget.", "tr": "Öğrenci bütçesiyle geçinmek zor."}],
     "turkishNote": "Türkçede \"borç almak\" ve \"borç vermek\" aynı \"borç\" kelimesiyle kurulur; İngilizcede ise iki farklı fiil vardır: borrow (almak) ve lend (vermek). \"Can you borrow me some money?\" yanlıştır; doğrusu \"Can you lend me some money?\" ya da \"Can I borrow some money?\". Ayrıca \"kazanmak\" İngilizcede earn (çalışarak), win (yarışma) ve make (para kazanmak, kâr etmek) olarak ayrılır."},
    [
        mc("\"Bana biraz para ödünç verebilir misin?\"", ["Can you borrow me some money?", "Can you lend me some money?"], 1, "lend = vermek."),
        mc("Piyangodan para kazanmak:", ["earn money", "win money"], 1, "Şans → win."),
        mc("\"Parası yetmez.\"", ["He can't afford it.", "He can't earn it."], 0, "afford."),
        mc("Doğal kelime eşlemesi:", ["take out a loan", "make a loan"], 0, "take out a loan."),
        gap("I borrowed some money ___ my parents.", ["from"], "borrow from."),
        gap("How much do I ___ you? (borçlu olmak)", ["owe"], "owe."),
        gap("She spends too much money ___ clothes.", ["on"], "spend on."),
        gap("I'm saving ___ for a new laptop.", ["up"], "save up for."),
        listen("When I started university, I took out a student loan. I lived on a very tight budget for four years. Now I've got a good job, and last month I finally paid it off. It feels amazing to be out of debt.", "Konuşan geçen ay ne yaptı?", ["Yeni bir kredi çekti", "Öğrenci kredisini ödeyip bitirdi", "Yeni bir iş buldu"], 1, "\"last month I finally paid it off\""),
        typ("İngilizcesi: \"Kardeşime 500 lira borcum var.\" (my brother)", variants("I owe my brother 500 lira.", "I owe 500 lira to my brother."), "I owe my brother 500 lira."),
    ],
    {"kind": "speaking", "task": speak("Parayla ilişkinizi anlatın: Harçlığınızı / maaşınızı genellikle neye harcıyorsunuz? Hiç birinden borç aldınız mı ya da birine borç verdiniz mi? Şu an ne için para biriktiriyorsunuz? Neye paranız yetmiyor? En az 8 para fiili ya da collocation kullanın.",
                                       "I'm not very good with money, to be honest. I spend most of my salary on rent and food, and I waste quite a lot on online shopping. Last year, I borrowed money from my brother to go on holiday, and it took me three months to pay him back. I've also lent money to friends, but some of them never paid me back! Right now, I'm saving up for a car, but I can't afford a new one, so I'll probably buy a second-hand one. I'd really like to stop living from month to month.",
                                       ["borrow / lend / owe doğru", "Collocations", "Kişisel deneyim"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "Endişe verici mi, endişeli mi?", "-ing ve -ed sıfatlarını (worrying / worried, shocking / shocked) doğru ve çeşitli kullanabilirim.",
    {"kind": "text", "title": "Bir ekonomi blogundan", "body": "This month's figures are worrying. Food prices have risen again, and many families are worried about how they will pay their bills this winter.\n\nWhat's surprising is that, at the same time, sales of luxury goods have increased. Economists aren't surprised, though. They say it's a sign that the gap between rich and poor is getting wider, which is alarming.\n\nThere is some encouraging news, however. Unemployment has fallen slightly, and young people who are interested in technology are finding jobs more easily.\n\nIt's frustrating for many people to work hard and still struggle to save money. But experts say that small changes in our spending habits can make an amazing difference over time.",
     "questions": [
        mc("What is the encouraging news?", ["Food prices have fallen.", "Unemployment has fallen slightly.", "Luxury goods are cheaper."], 1, "\"Unemployment has fallen slightly\""),
        mc("Why aren't economists surprised by luxury sales?", ["It's normal in winter.", "It shows the gap between rich and poor is growing.", "Luxury goods are cheaper now."], 1, "\"a sign that the gap between rich and poor is getting wider\""),
     ]},
    {"explanation": "Bu iki sıfat türünü A2'den beri biliyorsunuz (*bored / boring*). B2'de daha geniş bir kelime yelpazesi ve daha ince kullanımlar öğreniyoruz.\n\n| -ing (sebep: şey/durum **nasıl**) | -ed (sonuç: kişi **ne hissediyor**) |\n|---|---|\n| The news is **worrying**. | People are **worried**. |\n| The price was **shocking**. | I was **shocked**. |\n| The result was **disappointing**. | We were **disappointed**. |\n| It's **frustrating**. | I feel **frustrated**. |\n| The rise is **alarming**. | Experts are **alarmed**. |\n| The figures are **encouraging**. | We feel **encouraged**. |\n| The offer was **tempting**. | I was **tempted** to buy it. |\n| It's **overwhelming**. | I felt **overwhelmed**. |\n\n**Önemli:** Bir **kişi** de -ing sıfatıyla anlatılabilir: o zaman o kişinin **başkalarında yarattığı etki** anlatılır.\n\n- *He's **boring**.* (Sıkıcı biri; başkalarını sıkar.)\n- *He's **bored**.* (Canı sıkılıyor.)\n- *My boss is very **demanding**.* (Çok şey bekleyen, zorlayıcı biri.)\n\n**Edatlar:** worried **about**, disappointed **with/by/in**, shocked **by/at**, interested **in**, tempted **to** + fiil",
     "examples": [{"en": "The rise in rents is alarming.", "tr": "Kiralardaki artış alarm verici."},
                  {"en": "I was tempted to buy it, but it was too expensive.", "tr": "Almaya can attı ama çok pahalıydı."},
                  {"en": "Dealing with debt can be overwhelming.", "tr": "Borçla uğraşmak bunaltıcı olabilir."}],
     "turkishNote": "Türkçede \"endişe verici\" ve \"endişeli\", \"sıkıcı\" ve \"sıkılmış\" farklı ekler alır; İngilizcede bu ayrım -ing ve -ed ile yapılır. Türkçe konuşanların B2'de bile sık yaptığı hata \"I'm boring\" (Ben sıkıcıyım) demektir, oysa kastedilen \"I'm bored\" (Canım sıkılıyor). Kural basit: -ed bir duygu, -ing o duyguya neden olan şey."},
    [
        mc("\"Canım sıkılıyor.\"", ["I'm boring.", "I'm bored."], 1, "Duygu → -ed."),
        mc("\"Sonuçlar hayal kırıklığı yarattı.\"", ["The results were disappointed.", "The results were disappointing."], 1, "Sebep → -ing."),
        mc("\"She's very demanding.\" anlamı:", ["Çok şey talep eden, zorlayıcı biri", "Çok yorgun"], 0, "-ing → etkisi."),
        mc("\"Almaya can attı.\"", ["I was tempting to buy it.", "I was tempted to buy it."], 1, "tempted to."),
        gap("Many families are ___ (worry) about rising prices.", ["worried"], "Duygu."),
        gap("The rise in unemployment is ___ (alarm).", ["alarming"], "Sebep."),
        gap("It's really ___ (frustrate) when the website crashes.", ["frustrating"], "Sebep."),
        gap("I was ___ (shock) by the price of a coffee at the airport.", ["shocked"], "Duygu."),
        listen("I was really excited about my new job, but my first salary was disappointing. After paying rent and bills, there was hardly anything left. It's frustrating, but my manager says I'll get a pay rise in six months, which is encouraging.", "Konuşan ilk maaşı hakkında ne hissediyor?", ["Heyecanlı", "Hayal kırıklığına uğramış", "Şaşırmamış"], 1, "\"my first salary was disappointing\""),
        typ("İngilizcesi: \"Rakamlar cesaret verici.\" (the figures)", variants("The figures are encouraging.", "The figures are very encouraging."), "The figures are encouraging."),
    ],
    {"kind": "speaking", "task": speak("Ekonomi ya da kendi finansal durumunuzla ilgili son zamanlarda sizi etkileyen 5 şeyi anlatın. Her biri için hem -ing hem -ed sıfatı kullanın: worrying / worried, shocking / shocked, frustrating / frustrated, encouraging / encouraged, tempting / tempted, overwhelming / overwhelmed.",
                                       "The rise in rents in my city is shocking. I was shocked when my landlord asked for 30% more. It's also frustrating that my salary hasn't gone up, so I feel frustrated every time I pay the bills. Online sales are really tempting, and I'm often tempted to buy things I don't need. On the other hand, my savings plan is going well, which is encouraging. Planning everything can be overwhelming, but I feel less worried now that I have a budget.",
                                       ["-ing / -ed doğru seçim", "Edatlar", "Kelime çeşitliliği"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "Ekonominin dili", "Ekonomi haberlerinde sık geçen sıfat + isim ve isim + isim collocation'larını anlayabilir ve kullanabilirim.",
    {"kind": "text", "title": "Haber özeti: Ekonomide bu hafta", "body": "The central bank announced on Thursday that it would keep interest rates unchanged for the third month in a row.\n\nInflation remains high, and the rising cost of living continues to put pressure on households. Many families are spending a larger share of their income on basic needs such as food and housing.\n\nMeanwhile, the job market is showing signs of improvement. The unemployment rate fell slightly, and several companies have announced plans to create new jobs in the technology sector.\n\nExperts warn, however, that economic growth is likely to remain slow next year. Small businesses, in particular, are struggling with high energy costs and fierce competition from online shops.",
     "questions": [
        mc("What did the central bank do?", ["Raised interest rates", "Kept interest rates unchanged", "Cut interest rates"], 1, "\"keep interest rates unchanged\""),
        mc("What are small businesses struggling with?", ["Low taxes", "High energy costs and competition from online shops", "Too many customers"], 1, "\"high energy costs and fierce competition\""),
     ]},
    {"explanation": "Ekonomi dilinde bazı kelimeler **belli kelimelerle** birlikte kullanılır. Bunları **kalıp olarak** öğrenin.\n\n**Sıfat + isim:**\n\n| Doğal | Doğal değil |\n|---|---|\n| **high / low** inflation | ~~big~~ inflation |\n| **high / low** prices | ~~expensive~~ prices |\n| **fierce / strong** competition | ~~hard~~ competition |\n| **steady / slow / rapid** growth | ~~fast~~ growth (kullanılır ama az) |\n| a **tight** budget | ~~narrow~~ budget |\n| a **low / high** income | ~~small~~ income |\n| a **heavy** debt / **heavily** in debt | ~~big~~ debt |\n\n**İsim + isim:**\n\n- **interest** rate, **unemployment** rate, **exchange** rate (döviz kuru)\n- **job** market, **housing** market, **stock** market\n- **cost** of living, **standard** of living\n- **energy** costs, **living** costs\n\n**Fiil + isim:**\n\n- **create** jobs, **cut** taxes / costs, **raise** prices / taxes / interest rates\n- **put pressure on** sb, **struggle with** costs\n\n**Dikkat:** ***prices*** **high / low** olur, **expensive / cheap** olmaz. *Products* expensive olur.\n\n- ~~The prices are expensive.~~ → **Prices are high.** / **Things are expensive.**",
     "examples": [{"en": "Inflation has remained high this year.", "tr": "Enflasyon bu yıl yüksek kaldı."},
                  {"en": "Small shops face fierce competition from online retailers.", "tr": "Küçük dükkânlar çevrimiçi satıcılardan gelen sert rekabetle karşı karşıya."},
                  {"en": "The government plans to create 100,000 new jobs.", "tr": "Hükümet 100.000 yeni iş yaratmayı planlıyor."}],
     "turkishNote": "Türkçede \"fiyatlar pahalı\" demek doğal gelir; İngilizcede ise \"prices are expensive\" yanlış bir eşleşmedir: prices are high, things are expensive. Benzer şekilde \"büyük enflasyon\" değil \"high inflation\", \"sıkı bütçe\" değil \"tight budget\" deyin. Collocation'lar sözlükte tek tek bulunmaz; okuyarak ve not alarak öğrenilir."},
    [
        mc("Hangisi doğal?", ["The prices are very expensive.", "Prices are very high."], 1, "Prices → high."),
        mc("Hangisi doğal?", ["big inflation", "high inflation"], 1, "high inflation."),
        mc("Hangisi doğal?", ["hard competition", "fierce competition"], 1, "fierce competition."),
        mc("\"exchange rate\" anlamı:", ["Döviz kuru", "Faiz oranı"], 0, "exchange rate."),
        gap("We're on a ___ budget this month. (kısıtlı)", ["tight"], "tight budget."),
        gap("The new factory will ___ 2,000 jobs. (yaratmak)", ["create"], "create jobs."),
        gap("The ___ of living has risen sharply.", ["cost"], "cost of living."),
        gap("The bank decided to ___ interest rates. (yükseltmek)", ["raise"], "raise interest rates."),
        match([("interest", "rate"), ("job", "market"), ("cost of", "living"), ("fierce", "competition"), ("tight", "budget")], "Kelime eşlemelerini tamamlayın."),
        listen("The housing market has been difficult for young people. House prices are very high, and interest rates have made loans much more expensive. As a result, many people in their thirties are still living with their parents or renting.", "Gençler için ev almak neden zor?", ["Ev yok", "Ev fiyatları yüksek ve krediler pahalı", "Bankalar kredi vermiyor"], 1, "\"House prices are very high, and interest rates have made loans much more expensive\""),
    ],
    {"kind": "speaking", "task": speak("Bir haber spikeri gibi ülkenizin ya da şehrinizin ekonomisi hakkında kısa bir haber özeti sunun (1 dakika). En az 8 collocation kullanın: high inflation, interest rates, cost of living, job market, create jobs, fierce competition, tight budget, rising prices, unemployment rate, vb. Belirli rakamlar vermeniz gerekmiyor.",
                                       "Good evening. Here is this week's economic news. The rising cost of living remains the biggest concern for most families, as inflation stays high. Many households are on a tight budget, and they're cutting back on non-essential spending. The central bank has decided to keep interest rates unchanged. In better news, the job market is improving, and the unemployment rate has fallen slightly. A new technology park is expected to create thousands of jobs. However, small shops continue to face fierce competition from online retailers.",
                                       ["Ekonomi collocation'ları", "Haber üslubu", "Akıcılık"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Grafiği anlatmak", "Fiyatlardaki ve rakamlardaki değişimleri fiil + zarf ve sıfat + isim yapılarıyla doğru betimleyebilirim.",
    {"kind": "text", "title": "Bir kafenin yıllık raporu", "body": "The chart shows the monthly income of a small café in Eskişehir last year.\n\nIn January, income was quite low, at around 80,000 lira. It rose steadily in the spring and reached 120,000 in May.\n\nIn June, there was a sharp rise, as students finished their exams and tourists began to arrive. Income peaked at 180,000 lira in August.\n\nIn September, income fell dramatically when the summer season ended, but it then remained stable at about 110,000 for the rest of the autumn.\n\nIn December, there was a slight increase because of the holidays. Overall, the café's income almost doubled between January and August.",
     "questions": [
        mc("When did income peak?", ["In May", "In August", "In December"], 1, "\"peaked at 180,000 lira in August\""),
        mc("What happened in the autumn?", ["Income rose sharply.", "Income remained stable.", "The café closed."], 1, "\"remained stable at about 110,000\""),
     ]},
    {"explanation": "**Değişimi anlatmanın iki yolu:**\n\n| Fiil + zarf | Sıfat + isim |\n|---|---|\n| Prices **rose sharply**. | There was **a sharp rise** in prices. |\n| Sales **fell slightly**. | There was **a slight fall** in sales. |\n| Income **increased steadily**. | There was **a steady increase** in income. |\n| Costs **dropped dramatically**. | There was **a dramatic drop** in costs. |\n\n**Fiiller:**\n\n| Yukarı ↗ | Aşağı ↘ | Sabit → | Zirve / dip |\n|---|---|---|---|\n| rise, increase, go up, grow | fall, decrease, go down, drop, decline | remain stable, stay the same, level off | peak (at), reach a peak, hit a low |\n| double (iki katına çıkmak) | halve (yarıya inmek) | | |\n\n**Zarflar / sıfatlar (hıza ve miktara göre):**\n\n- **Büyük:** sharply / sharp, dramatically / dramatic, significantly / significant\n- **Orta:** steadily / steady, gradually / gradual\n- **Küçük:** slightly / slight\n\n**Edatlar çok önemli:**\n\n- rose **from** 80,000 **to** 120,000\n- rose **by** 40,000 (fark)\n- peaked **at** 180,000\n- a rise **in** prices / a rise **of** 20%",
     "examples": [{"en": "The price of bread rose by 15% last year.", "tr": "Ekmeğin fiyatı geçen yıl %15 arttı."},
                  {"en": "There was a sharp fall in sales in January.", "tr": "Ocak ayında satışlarda keskin bir düşüş oldu."},
                  {"en": "Unemployment peaked at 12% and then fell gradually.", "tr": "İşsizlik %12 ile zirveye ulaştı, sonra yavaş yavaş düştü."}],
     "turkishNote": "Türkçede \"%15 arttı\" derken edat kullanılmaz; İngilizcede \"rose by 15%\" (fark) ile \"rose to 15%\" (ulaşılan değer) çok farklı anlamlara gelir. \"Enflasyon %5 arttı\" cümlesinin İngilizcesi bağlama göre \"rose by 5%\" ya da \"rose to 5%\" olur. Grafik betimlerken by, to, from ve at'e çok dikkat edin."},
    [
        mc("\"Satışlar %10'dan %15'e yükseldi.\"", ["Sales rose by 10% to 15%.", "Sales rose from 10% to 15%."], 1, "from ... to."),
        mc("\"Fiyatlar %20 arttı.\" (fark)", ["Prices rose by 20%.", "Prices rose at 20%."], 0, "by = fark."),
        mc("\"rose sharply\" ile aynı anlamda:", ["There was a sharp rise.", "There was a sharply rise."], 0, "Sıfat + isim."),
        mc("İki katına çıkmak:", ["halve", "double"], 1, "double."),
        gap("Sales peaked ___ 2 million in July.", ["at"], "peak at."),
        gap("There was a slight ___ in prices. (düşüş)", ["fall", "decrease", "drop", "decline"], "a slight fall."),
        gap("Income increased ___ (steady) throughout the year.", ["steadily"], "Zarf."),
        gap("After the summer, the number of visitors remained ___. (sabit)", ["stable"], "remain stable."),
        listen("As you can see, our online sales grew steadily from January to March. Then, in April, there was a dramatic increase, mainly because of our new advertising campaign. Sales peaked in May and fell slightly in June.", "Nisan'daki büyük artışın sebebi ne?", ["Tatil", "Yeni reklam kampanyası", "Fiyat indirimi"], 1, "\"because of our new advertising campaign\""),
        order(["There", "was", "a", "sharp", "rise", "in", "the", "price", "of", "petrol"], "There was a sharp rise in the price of petrol.", "a + sıfat + isim + in.", "Benzin fiyatında keskin bir artış oldu."),
    ],
    {"kind": "speaking", "task": speak("Son bir yılda sizin için önemli bir şeyin değişimini bir grafik anlatır gibi betimleyin: kiranız, bir ürünün fiyatı, aylık harcamalarınız, telefonunuzda geçirdiğiniz süre, vb. En az 3 fiil + zarf, 2 sıfat + isim yapısı kullanın ve from / to / by / at edatlarını doğru kullanın.",
                                       "I'd like to describe how my monthly spending on food changed last year. In January, I was spending about 6,000 lira a month. It rose steadily in the spring and reached 8,000 in May. In the summer, there was a sharp increase because I ate out a lot on holiday, and it peaked at 11,000 in August. In September, it fell dramatically when I started cooking at home again. It then remained stable at around 7,500. Overall, my spending rose by about 25% over the year.",
                                       ["Fiil + zarf", "Sıfat + isim", "from / to / by / at", "Mantıklı sıra"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Para tavsiyesi", "Ünitedeki kelime ve yapıları kullanarak gençlere kişisel finans tavsiyesi veren ikna edici bir blog yazısı yazabilirim.",
    {"kind": "text", "title": "Blog: İlk maaşınla yapman gereken 5 şey", "body": "Congratulations on your first job! It's an exciting moment, and it's tempting to spend your first salary on something special. But a few smart decisions now can save you a lot of stress later.\n\n1. Make a budget. Write down your monthly income and expenses. You might be shocked by how much you spend on coffee and takeaways.\n\n2. Pay yourself first. As soon as you get paid, put at least 10% into a savings account. If you wait until the end of the month, there will be nothing left.\n\n3. Build an emergency fund. Try to save enough to cover three months of living costs. It will make unexpected bills much less frightening.\n\n4. Avoid debt if you can. Credit cards are convenient, but the interest rates are often very high. Never borrow money to buy things you don't really need.\n\n5. Treat yourself, but wisely. You've earned it! Just make sure it's worth the money.\n\nManaging money isn't always exciting, but feeling in control of your finances is one of the most satisfying feelings in the world.",
     "questions": [
        mc("What does \"pay yourself first\" mean?", ["Buy yourself a present.", "Put money into savings as soon as you get paid.", "Ask for a pay rise."], 1, "\"put at least 10% into a savings account\""),
        mc("How much should an emergency fund cover?", ["One month", "Three months of living costs", "A year"], 1, "\"three months of living costs\""),
     ]},
    {"explanation": "**Tavsiye veren blog yazısının özellikleri:**\n\n| Özellik | Örnek |\n|---|---|\n| **Okuyucuya doğrudan hitap** | *Congratulations on your first job!* / *You might be shocked ...* |\n| **Numaralı başlıklar** | *1. Make a budget.* (emir kipiyle kısa başlıklar) |\n| **Gerekçe** | *If you wait ..., there will be nothing left.* (koşul cümlesi) |\n| **Çeşitli tavsiye kalıpları** | *Try to ... / Make sure ... / Avoid + -ing / Never ... / It's a good idea to ... / You should ...* |\n| **Duyguya hitap** (-ing / -ed sıfatlar) | *exciting, tempting, frightening, satisfying* |\n| **Güçlü kapanış** | Bir özet ya da motive edici bir cümle |\n\n**Tavsiye kalıpları:**\n\n- ***Make sure** you read the small print.* (Mutlaka ... )\n- ***Avoid** taking out loans for holidays.* (avoid + **-ing**)\n- ***It's worth** comparing prices.* (worth + **-ing**)\n- ***The key is to** start early.*\n- ***If I were you, I'd** ...*\n\n**Üslup:** Blog yazısı **yarı samimi**dir: kısaltmalar (*you'll, don't*) ve doğrudan hitap kullanılır, ama dil düzgün ve açıktır.",
     "examples": [{"en": "Make sure you compare prices before you buy.", "tr": "Almadan önce mutlaka fiyatları karşılaştır."},
                  {"en": "Avoid using your credit card for everyday shopping.", "tr": "Günlük alışverişlerde kredi kartı kullanmaktan kaçın."},
                  {"en": "It's worth setting up an automatic savings plan.", "tr": "Otomatik bir birikim planı kurmaya değer."}],
     "turkishNote": "Türkçe blog yazılarında tavsiyeler genellikle \"-malısınız\" ile verilir ve tekrar edilir. İngilizcede \"You should\" yerine çeşitli kalıplar kullanmak (Make sure, Avoid, It's worth, Try to) yazıyı çok daha canlı yapar. \"avoid\" ve \"worth\" kelimelerinden sonra -ing geldiğini unutmayın: \"Avoid to spend\" yanlıştır, \"Avoid spending\" doğrudur."},
    [
        mc("Hangisi doğru?", ["Avoid to borrow money.", "Avoid borrowing money."], 1, "avoid + -ing."),
        mc("Hangisi doğru?", ["It's worth to compare prices.", "It's worth comparing prices."], 1, "worth + -ing."),
        mc("Blog yazısı için en uygun başlık:", ["Financial Management Strategies for Recently Employed Individuals", "5 Things to Do with Your First Salary"], 1, "Yarı samimi, doğrudan."),
        mc("\"Make sure you save 10%.\" anlamı:", ["%10 biriktirdiğinden emin ol.", "%10 biriktirmeyi unut."], 0, "Make sure."),
        gap("It's ___ (tempt) to spend your first salary on something special.", ["tempting"], "Sebep → -ing."),
        gap("Try ___ save at least 10% of your income.", ["to"], "try to."),
        gap("Feeling in control of your money is very ___ (satisfy).", ["satisfying"], "-ing."),
        gap("If I ___ you, I'd open a savings account.", ["were"], "If I were you."),
        listen("My best piece of advice? Don't buy things just because they're on sale. A bargain isn't a bargain if you don't need it. And make sure you check your bank account every week. It's boring, but it'll stop you from getting any shocking surprises.", "Konuşan neden her hafta banka hesabını kontrol etmeyi öneriyor?", ["Faiz kazanmak için", "Şok edici sürprizlerden kaçınmak için", "İndirimleri görmek için"], 1, "\"it'll stop you from getting any shocking surprises\""),
        typ("İngilizcesi: \"İhtiyacın olmayan şeyleri almaktan kaçın.\" (avoid)", variants("Avoid buying things you don't need.", "Avoid buying things that you don't need."), "Avoid buying things you don't need."),
    ],
    {"kind": "writing", "task": write("Üniversite öğrencilerine yönelik bir blog için \"Öğrenci bütçesiyle nasıl geçinilir?\" konulu bir yazı yazın (180–220 kelime). İlgi çekici bir girişle başlayın, numaralı en az 4 tavsiye verin ve her birini gerekçelendirin. En az 6 para collocation'ı (live on, cut back on, save up for, a tight budget, can't afford, waste money on), en az 3 -ing / -ed sıfat ve çeşitli tavsiye kalıpları (Make sure, Avoid + -ing, It's worth + -ing) kullanın.",
                                      "Living on a student budget: 5 tips that actually work\n\nLet's be honest: being a student is exciting, but living on a tight budget can be really stressful. Here are five tips that helped me survive my first year without getting into debt.\n\n1. Track every lira. For one month, write down everything you spend. Most students are shocked to see how much they waste on snacks and coffee.\n\n2. Cook in groups. Takeaways are tempting after a long day, but they're expensive. Cooking with your flatmates is cheaper, healthier and more fun.\n\n3. Use your student card. It's worth asking for a student discount everywhere: cinemas, museums, public transport and even some cafés.\n\n4. Avoid buying new textbooks. Second-hand books or library copies are just as good, and you can sell them again at the end of the year.\n\n5. Save up for the things you really want. If you can't afford something now, put a small amount aside each week. Make sure you never borrow money for things you don't need.\n\nCutting back on spending isn't always fun, but the feeling of reaching the end of the month with money in your account is incredibly satisfying. Trust me, it's worth it!",
                                      ["İlgi çekici giriş ve yapı", "Para collocation'ları", "-ing / -ed sıfatlar", "Çeşitli tavsiye kalıpları", "Yarı samimi üslup"])},
)

u.test([
    mc("\"Bana biraz para ödünç verir misin?\"", ["Can you borrow me some money?", "Can you lend me some money?"], 1, "lend"),
    mc("\"Canım sıkılıyor.\"", ["I'm boring.", "I'm bored."], 1, "-ed"),
    mc("Hangisi doğal?", ["The prices are very expensive.", "Prices are very high."], 1, "prices → high"),
    mc("\"Fiyatlar %10 arttı.\" (fark)", ["Prices rose by 10%.", "Prices rose at 10%."], 0, "by"),
    mc("Hangisi doğru?", ["Avoid to spend too much.", "Avoid spending too much."], 1, "avoid + -ing"),
    gap("How much do I ___ you? (borçlu olmak)", ["owe"], "owe"),
    gap("We need to cut ___ on eating out.", ["back"], "cut back on"),
    gap("They took ___ a loan to buy a house.", ["out"], "take out a loan"),
    gap("The rise in unemployment is ___ (alarm).", ["alarming"], "-ing"),
    gap("Sales peaked ___ 500,000 in December.", ["at"], "peak at"),
    gap("There was a ___ (sharp) rise in prices. (sıfat)", ["sharp"], "a sharp rise"),
    mc("Hangisi doğal?", ["big inflation", "high inflation"], 1, "high inflation"),
    listen("When I was a student, I lived on a very tight budget. I couldn't afford to eat out, so I learned to cook. Looking back, it was a great lesson. Now I earn a good salary, but I still cook at home most nights, and I save about a quarter of my income.", "Konuşan şu an gelirinin ne kadarını biriktiriyor?", ["Yarısını", "Dörtte birini", "Hiç"], 1, "\"I save about a quarter of my income\""),
    typ("İngilizcesi: \"Yeni bir arabaya param yetmez.\"", variants("I can't afford a new car.", "I can't afford to buy a new car.", "I cannot afford a new car."), "I can't afford a new car."),
    write("\"Okullarda finansal okuryazarlık dersi zorunlu olmalı mı?\" sorusuna bir blog yazısıyla cevap verin (180–220 kelime). Görüşünüzü belirtin, en az 3 gerekçe verin, bir karşı görüşe değinin ve güçlü bir kapanış yapın. Para collocation'ları, -ing / -ed sıfatlar, en az bir eğilim betimlemesi (rose sharply / a steady increase) ve tavsiye kalıpları kullanın.",
          "Should every school teach money?\n\nMost of us leave school knowing how to solve equations, but very few of us know how to make a budget, how interest rates work or what happens when you can't pay off a credit card. In my opinion, financial education should be compulsory in every secondary school.\n\nFirst, young people are getting into debt earlier than ever. Among my own friends, the number of people with credit card debt has risen sharply since we started university. Many of them simply don't understand how quickly interest can grow.\n\nSecond, the cost of living has increased steadily, and good money habits are now more important than ever. Learning to save, to compare prices and to avoid wasting money on things you don't need is a skill for life.\n\nFinally, money is a common source of stress. Studies suggest that people who feel in control of their finances are less worried and more satisfied with their lives.\n\nSome people argue that parents, not schools, should teach children about money. That's a fair point, but not every parent has the knowledge or the time to do it.\n\nIt's worth remembering that almost every adult decision involves money. Surely it's time our schools prepared students for that.",
          ["Açık görüş ve gerekçeler", "Karşı görüş", "Para collocation'ları ve eğilim dili", "-ing / -ed sıfatlar", "Güçlü kapanış"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

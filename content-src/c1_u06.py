"""C1 Ünite 6: Temkinli dil."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("C1", 6, "Temkinli dil", "Hedging",
         "Akademik ve profesyonel metinlerde iddialarımı temkinli bir dille (seem to, tend to, arguably, to some extent, It could be argued that) yumuşatabilir, kesinlik bildiren ifadelerle (clearly, undoubtedly) dengeleyebilir, konuşmada diplomatik belirsizlik ifadeleri kullanabilir ve aşırı kesin ya da aşırı temkinli dilden kaçınabilirim.",
         ["temkinli fiiller: seem, appear, tend to, suggest", "modal, zarf ve sıfatlarla temkin: arguably, relatively, to some extent", "miktar ve sıklıkla temkin; kişisiz yapılar", "konuşmada temkin: I'd say, as far as I know, sort of", "temkin ve kesinlik dengesi (hedging vs boosting)"],
         ["akademik tartışma", "bilim ve medya", "diplomatik iletişim"],
         {"title": "Kesin mi, değil mi?", "durationMinutes": 45,
          "goal": "Öğrencilere aşırı kesin cümleler içeren kısa \"sahte haber\" başlıkları verilir (Coffee cures cancer!, Young people never read). Gruplar her başlığı kanıta uygun, temkinli bir bilimsel cümleye çevirir. Sonra tersini yapar: aşırı temkinli bir paragrafı netleştirir. Sınıf \"altın orta\" yolu tartışır."})

u.vocab([
    ("hedge", "temkinli konuşmak, ihtiyatlı olmak", "Academics often hedge their claims.", "Akademisyenler iddialarını sık sık temkinli ifade eder.", None),
    ("tend to", "-me eğiliminde olmak", "Older people tend to vote more.", "Yaşlılar daha çok oy verme eğiliminde.", None),
    ("appear", "görünmek", "The results appear to support the theory.", "Sonuçlar teoriyi destekliyor gibi görünüyor.", None),
    ("suggest", "göstermek, işaret etmek", "The data suggest a link.", "Veriler bir bağlantıya işaret ediyor.", None),
    ("arguably", "tartışmaya açık olsa da, belki de", "She is arguably the best player in the world.", "Tartışmaya açık olsa da dünyanın en iyi oyuncusu olabilir.", None),
    ("relatively", "nispeten", "The test is relatively easy.", "Test nispeten kolay.", None),
    ("to some extent", "bir dereceye kadar", "I agree with you to some extent.", "Sana bir dereceye kadar katılıyorum.", None),
    ("largely", "büyük ölçüde", "The project was largely successful.", "Proje büyük ölçüde başarılıydı.", None),
    ("apparently", "görünüşe göre", "Apparently, the meeting has been cancelled.", "Görünüşe göre toplantı iptal edilmiş.", None),
    ("presumably", "muhtemelen, tahminen", "Presumably, he forgot.", "Muhtemelen unuttu.", None),
    ("potentially", "potansiyel olarak", "This is a potentially serious problem.", "Bu potansiyel olarak ciddi bir sorun.", None),
    ("in most cases", "çoğu durumda", "In most cases, the treatment works.", "Çoğu durumda tedavi işe yarar.", None),
    ("generally speaking", "genel olarak", "Generally speaking, prices are lower in the north.", "Genel olarak kuzeyde fiyatlar daha düşük.", None),
    ("it is widely believed", "yaygın olarak inanılıyor", "It is widely believed that exercise improves mood.", "Egzersizin ruh halini iyileştirdiğine yaygın olarak inanılıyor.", None),
    ("tentative", "geçici, kesin olmayan", "These are only tentative conclusions.", "Bunlar sadece kesin olmayan sonuçlar.", None),
    ("claim", "iddia; iddia etmek", "There is no evidence for this claim.", "Bu iddia için hiçbir kanıt yok.", None),
    ("overgeneralise", "aşırı genelleme yapmak", "Be careful not to overgeneralise.", "Aşırı genelleme yapmamaya dikkat et.", None),
    ("undoubtedly", "şüphesiz", "This is undoubtedly a major achievement.", "Bu şüphesiz büyük bir başarı.", None),
    ("clearly", "açıkça", "Clearly, more needs to be done.", "Açıkça, daha fazlasının yapılması gerekiyor.", None),
    ("as far as I know", "bildiğim kadarıyla", "As far as I know, the shop is still open.", "Bildiğim kadarıyla dükkân hâlâ açık.", None),
    ("I'd say", "diyebilirim ki, bence", "I'd say it's about two kilometres.", "Yaklaşık iki kilometre diyebilirim.", None),
    ("more or less", "aşağı yukarı", "We've more or less finished.", "Aşağı yukarı bitirdik.", None),
    ("somewhat", "biraz, bir miktar", "The results were somewhat disappointing.", "Sonuçlar biraz hayal kırıklığı yarattı.", None),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Görünüyor ki", "seem, appear, tend to ve suggest gibi fiillerle iddialarımı kanıta uygun bir şekilde yumuşatabilirim.",
    {"kind": "text", "title": "İki gazete, aynı araştırma", "body": "Newspaper A:\n\"SCIENTISTS PROVE: CHOCOLATE MAKES YOU SMARTER!\nA new study shows that people who eat chocolate are more intelligent. Eating chocolate every day improves your memory.\"\n\nNewspaper B:\n\"Chocolate and memory: a possible link?\nA new study suggests that there may be a connection between eating dark chocolate and memory. Participants who ate small amounts of dark chocolate every day appeared to perform slightly better on memory tests. However, the researchers stress that the sample was small and that the effect seems to be modest. People who eat chocolate also tend to have other habits, such as drinking less alcohol, which could explain the results.\"",
     "questions": [
        mc("Which newspaper reports the study more accurately?", ["Newspaper A", "Newspaper B"], 1, "Temkinli ve dengeli."),
        mc("What could also explain the results?", ["The chocolate brand", "Other habits, such as drinking less alcohol", "The weather"], 1, "\"People who eat chocolate also tend to have other habits\""),
     ]},
    {"explanation": "**Hedging** (temkinli dil), bir iddiayı **kanıtın gücüne uygun** şekilde ifade etmektir. Akademik, bilimsel ve profesyonel İngilizcenin vazgeçilmez bir parçasıdır.\n\n**Temkinli fiiller:**\n\n| Fiil | Örnek |\n|---|---|\n| **seem / appear** + to V1 | Participants **appeared to perform** better. |\n| **It seems / appears that** ... | **It seems that** the effect is small. |\n| **tend to** + V1 | Chocolate lovers **tend to** drink less. |\n| **suggest / indicate** (that) | The study **suggests that** there **may** be a link. |\n| **be thought / believed to** | It **is thought to** reduce stress. |\n\n**Kesin → temkinli:**\n\n| Kesin (riskli) | Temkinli |\n|---|---|\n| This **proves** that ... | This **suggests / indicates** that ... |\n| Chocolate **improves** memory. | Chocolate **may improve** / **appears to improve** memory. |\n| Young people **are** lazy. | Young people **tend to** ... / **Some** young people ... |\n| The drug **works**. | The drug **seems to be effective** in most cases. |\n\n**Geçmiş için:** *They **seem to have** misunderstood.* / *The fire **appears to have started** in the kitchen.*\n\n**Neden önemli?** Bilimde bir çalışma nadiren bir şeyi \"kanıtlar\". Temkinli dil, **dürüstlük ve güvenilirlik** göstergesidir.",
     "examples": [{"en": "The results seem to indicate a positive trend.", "tr": "Sonuçlar olumlu bir eğilime işaret ediyor gibi görünüyor."},
                  {"en": "Women tend to live longer than men.", "tr": "Kadınlar erkeklerden daha uzun yaşama eğilimindedir."},
                  {"en": "The fire appears to have started in the kitchen.", "tr": "Yangın mutfakta başlamış gibi görünüyor."}],
     "turkishNote": "Türk medyasında \"Bilim insanları kanıtladı!\" gibi başlıklar sık görülür, ama İngilizce akademik dilde \"prove\" fiili çok nadiren kullanılır. Türkçede \"-dığı görülüyor\", \"-ma eğiliminde\", \"-dığına işaret ediyor\" gibi yapılar temkinli dilin karşılığıdır. Türk öğrencilerin akademik yazılarında en sık görülen sorun, kanıtın desteklemediği kesin ifadeler kullanmaktır (\"This shows that all students...\")."},
    [
        mc("En temkinli ve doğru:", ["This study proves that coffee causes cancer.", "This study suggests that there may be a link between coffee and cancer."], 1, "suggest + may."),
        mc("\"tend to\" anlamı:", ["Her zaman", "Genellikle, -me eğiliminde"], 1, "Eğilim."),
        mc("Geçmiş için temkinli:", ["He seems to forget.", "He seems to have forgotten."], 1, "seem to have + V3."),
        mc("\"Young people are lazy.\" temkinli hali:", ["All young people are lazy.", "Some young people tend to be less active."], 1, "Genelleme yok."),
        gap("The results ___ to support our hypothesis. (görünüyor)", ["seem", "appear"], "seem / appear to."),
        gap("People who exercise ___ to sleep better. (eğiliminde)", ["tend"], "tend to."),
        gap("The data ___ that the policy has been successful. (işaret ediyor)", ["suggest", "suggests", "indicate", "indicates"], "suggest."),
        gap("It ___ that the meeting has been postponed. (görünüşe göre)", ["seems", "appears"], "It seems that."),
        listen("The new drug appears to reduce symptoms in many patients. However, it seems to work less well in older people, and some participants tended to experience mild headaches. Further research will be needed before it can be recommended.", "İlaç kimlerde daha az etkili görünüyor?", ["Gençlerde", "Yaşlılarda", "Çocuklarda"], 1, "\"it seems to work less well in older people\""),
        typ("Temkinli hale getirin (appear to): \"The plan has failed.\"", variants("The plan appears to have failed.", "It appears that the plan has failed."), "The plan appears to have failed."),
    ],
    {"kind": "speaking", "task": speak("Aşağıdaki kesin iddiaları temkinli bir bilim insanı gibi yeniden ifade edin ve her birine bir gerekçe ya da sınırlılık ekleyin: (1) Video games make children violent. (2) Breakfast is the most important meal. (3) Social media causes depression. (4) Rich people are happier.",
                                       "One: Some studies suggest that certain violent video games may be linked to aggressive behaviour in the short term, but the effect seems to be small, and other factors tend to be more important. Two: Breakfast appears to help some people concentrate, but it doesn't seem to matter as much as the overall quality of your diet. Three: Heavy social media use seems to be associated with lower mood in teenagers, although it's not clear which causes which. Four: Higher income tends to increase happiness up to a point, but the effect appears to become smaller after basic needs are met.",
                                       ["Temkinli fiiller", "Geçmiş için seem to have", "Gerekçe ve sınırlılık"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "Bir dereceye kadar", "Modal'lar, zarflar ve sınırlayıcı ifadelerle (arguably, relatively, to some extent, largely) iddialarımın gücünü ince ayarlayabilirim.",
    {"kind": "text", "title": "Bir tarih makalesinden", "body": "The Industrial Revolution was arguably the most important turning point in modern history. It transformed, to a large extent, the way people lived and worked.\n\nIt is often claimed that the revolution made everyone richer. This is only partly true. In the long term, living standards rose considerably. In the short term, however, conditions for many workers were relatively poor, and in some cases they may even have worsened.\n\nThe revolution was largely driven by new technology, particularly the steam engine. Nevertheless, it could be argued that social and political factors were, to some extent, equally important. Britain's stable government and access to coal were presumably also significant.\n\nIn general, historians agree that the changes were profound. Whether they were mainly positive is, perhaps, more open to debate.",
     "questions": [
        mc("What happened to living standards in the long term?", ["They fell.", "They rose considerably.", "They didn't change."], 1, "\"In the long term, living standards rose considerably.\""),
        mc("What were also important factors, according to the writer?", ["Only technology", "Social and political factors", "Weather"], 1, "\"social and political factors were, to some extent, equally important\""),
     ]},
    {"explanation": "**1. Modal'lar:** may, might, could, would → olasılık\n\n- *This **could** be a problem.* / *This **would** seem to suggest ...* (çok temkinli)\n\n**2. Zarflar:**\n\n| Zarf | Anlam | Örnek |\n|---|---|---|\n| **arguably** | tartışmaya açık ama savunulabilir | **arguably** the most important ... |\n| **probably / possibly / perhaps** | muhtemelen / belki | This is **perhaps** the main reason. |\n| **presumably** | makul bir varsayımla | They **presumably** knew. |\n| **apparently** | görünüşe göre (duyduğuma göre) | **Apparently**, she's left. |\n| **relatively / fairly / somewhat** | nispeten / oldukça / biraz | **relatively** poor |\n| **largely / mainly / mostly** | büyük ölçüde | **largely** driven by technology |\n| **partly** | kısmen | only **partly** true |\n| **generally / usually** | genellikle | **Generally**, ... |\n\n**3. Sınırlayıcı ifadeler:**\n\n| İfade | Örnek |\n|---|---|\n| **to some / a certain extent** | I agree **to some extent**. |\n| **to a large extent** | It changed, **to a large extent**, ... |\n| **in some cases / in most cases** | **In some cases**, it worsened. |\n| **in general / on the whole** | **On the whole**, it was positive. |\n| **up to a point** | That's true **up to a point**. |\n\n**4. Sıfatlar:** *possible, probable, likely, potential* → *a **possible** explanation*, *a **potential** risk*",
     "examples": [{"en": "This is arguably the best film of the decade.", "tr": "Bu, tartışmaya açık olsa da on yılın en iyi filmi olabilir."},
                  {"en": "I agree with you up to a point.", "tr": "Sana bir noktaya kadar katılıyorum."},
                  {"en": "The project was largely successful, although some problems remain.", "tr": "Proje büyük ölçüde başarılıydı, ancak bazı sorunlar devam ediyor."}],
     "turkishNote": "Türkçede \"bir dereceye kadar\", \"büyük ölçüde\", \"nispeten\" gibi ifadeler İngilizcedeki \"to some extent\", \"largely\", \"relatively\" ile birebir örtüşür. \"Arguably\" ise Türkçeye doğrudan çevrilmesi zor bir kelimedir: \"Tartışmaya açık olsa da ... denebilir\" anlamına gelir ve hem iddia hem de temkin içerir. Akademik İngilizcede çok değerli bir kelimedir."},
    [
        mc("\"arguably the best\" anlamı:", ["Kesinlikle en iyi", "Tartışmaya açık ama savunulabilir şekilde en iyi"], 1, "arguably."),
        mc("\"This is only partly true.\"", ["Tamamen doğru", "Kısmen doğru"], 1, "partly."),
        mc("En temkinli:", ["This proves ...", "This would seem to suggest ..."], 1, "would seem to suggest."),
        mc("\"I agree up to a point.\"", ["Tamamen katılıyorum.", "Bir noktaya kadar katılıyorum."], 1, "up to a point."),
        gap("I agree with you to some ___.", ["extent"], "to some extent."),
        gap("The changes were ___ driven by technology. (büyük ölçüde)", ["largely", "mainly", "mostly"], "largely."),
        gap("The test was ___ easy. (nispeten)", ["relatively", "fairly"], "relatively."),
        gap("On the ___, the results were positive. (genel olarak)", ["whole"], "On the whole."),
        listen("Is social media good or bad for democracy? I'd argue that it's partly both. On the whole, it has given ordinary people a voice. However, in some cases, it has also helped false information to spread very quickly. So, to some extent, it depends on how we use it.", "Konuşanın görüşü ne?", ["Tamamen kötü", "Kısmen ikisi de; kullanıma bağlı", "Tamamen iyi"], 1, "\"it's partly both... it depends on how we use it\""),
        typ("Daha temkinli yazın (arguably): \"Istanbul is the most beautiful city in the world.\"", variants("Istanbul is arguably the most beautiful city in the world.", "Arguably, Istanbul is the most beautiful city in the world."), "Istanbul is arguably the most beautiful city in the world."),
    ],
    {"kind": "speaking", "task": speak("Aşağıdaki görüşlere \"Evet\" ya da \"Hayır\" demek yerine nüanslı bir cevap verin. arguably, largely, partly, relatively, to some extent, up to a point, in most cases, on the whole gibi ifadelerden en az 6'sını kullanın: (1) Technology has made life better. (2) University is necessary for a good career. (3) Learning English is easy for Turkish speakers.",
                                       "One: On the whole, I think technology has made life better, but only up to a point. Medical technology, for example, has largely improved our health. However, in some cases, it has also made people more isolated. Two: University is arguably still important for many careers, such as medicine and law. But to some extent, skills and experience are becoming more important than degrees. Three: Learning English is relatively easy at the beginning for Turkish speakers, but some areas, like articles and pronunciation, tend to be quite difficult.",
                                       ["Zarflar ve sınırlayıcı ifadeler", "Nüanslı görüş", "Dengeli argüman"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "Bazıları, çoğu durumda", "Miktar, sıklık ve kişisiz yapılarla aşırı genellemeden kaçınabilir ve iddiaları başkalarına mesafeli bir şekilde aktarabilirim.",
    {"kind": "text", "title": "Öğrenci essay'i: önce ve sonra", "body": "First draft:\n\"Students today don't read books. They are always on their phones. Teachers think this is a disaster. Technology has destroyed reading.\"\n\nRevised draft:\n\"Many students today appear to read fewer books than previous generations. A number of surveys suggest that young people spend a considerable amount of time on their phones, and in some cases this may reduce the time available for reading. It is widely believed among teachers that this is a cause for concern. However, it could be argued that technology has changed, rather than destroyed, the way young people read, since many of them read extensively online.\"",
     "questions": [
        mc("What does the revised draft say about technology?", ["It has destroyed reading.", "It may have changed the way young people read.", "It has no effect."], 1, "\"technology has changed, rather than destroyed, the way young people read\""),
        mc("Which draft is more appropriate for an academic essay?", ["First draft", "Revised draft"], 1, "Temkinli ve dengeli."),
     ]},
    {"explanation": "**1. Miktar ifadeleriyle genellemeden kaçınmak:**\n\n| Aşırı genelleme | Temkinli |\n|---|---|\n| **Students** don't read. | **Many / Some / A number of** students ... |\n| **Everyone** knows that ... | **It is widely known / believed that** ... |\n| **All** experts agree. | **Most** experts agree. / **There is broad agreement that** ... |\n| **People** hate taxes. | **A majority of** people ... |\n\n**2. Sıklık ifadeleri:**\n\n- *always → **often, frequently, usually, in most cases***\n- *never → **rarely, seldom, in few cases***\n\n**3. Kişisiz yapılar (iddiayı başkalarına aktarmak):**\n\n| Yapı | Örnek |\n|---|---|\n| **It is widely believed / thought that** ... | **It is widely believed that** ... |\n| **It could / might be argued that** ... | **It could be argued that** technology has changed reading. |\n| **It has been suggested / claimed that** ... | **It has been suggested that** ... |\n| **There is some evidence that** ... | **There is some evidence that** ... |\n| **According to some researchers,** ... | |\n\n**4. Sınırlı iddia:**\n\n- *This **may** reduce the time **available**.*\n- *... **in some cases** ...*\n- *... **at least in the short term** ...*\n- *... **under certain conditions** ...*\n\n**Not:** Kişisiz edilgen yapıları (It is said that, X is thought to) C1 Ünite 8'de ayrıntılı göreceğiz.",
     "examples": [{"en": "A number of studies have found a link between sleep and memory.", "tr": "Bir dizi çalışma uyku ve hafıza arasında bir bağlantı buldu."},
                  {"en": "It could be argued that the policy has been partly successful.", "tr": "Politikanın kısmen başarılı olduğu savunulabilir."},
                  {"en": "In most cases, the symptoms disappear within a week.", "tr": "Çoğu durumda belirtiler bir hafta içinde kaybolur."}],
     "turkishNote": "Türkçe öğrenci essay'lerinde \"Herkes bilir ki...\", \"Günümüz gençleri hiç kitap okumuyor\" gibi genellemeler sık görülür ve Türkçede bunlar daha kabul edilebilir olabilir. İngilizce akademik yazıda ise bu tür ifadeler hemen \"overgeneralisation\" olarak işaretlenir. \"Many\", \"some\", \"a number of\" ve \"It could be argued that\" gibi küçük eklemeler yazınızın güvenilirliğini büyük ölçüde artırır."},
    [
        mc("Aşırı genelleme hangisi?", ["Many teenagers use social media every day.", "All teenagers are addicted to social media."], 1, "All → genelleme."),
        mc("Kişisiz ve temkinli:", ["I think everyone believes this.", "It is widely believed that ..."], 1, "It is widely believed."),
        mc("\"never\" yerine temkinli:", ["rarely", "always"], 0, "rarely."),
        mc("En temkinli:", ["Technology destroyed reading.", "It could be argued that technology has changed the way people read."], 1, "It could be argued."),
        gap("A ___ of studies suggest a link. (bir dizi)", ["number"], "A number of."),
        gap("It ___ be argued that the law is unfair. (savunulabilir)", ["could", "might", "can"], "It could be argued."),
        gap("In ___ cases, the treatment is effective. (çoğu)", ["most", "many"], "In most cases."),
        gap("There is ___ evidence that the diet works. (bazı)", ["some"], "There is some evidence."),
        listen("It has been suggested that working from home makes people less productive. However, a number of recent studies indicate that, in many cases, the opposite may be true. Productivity seems to depend largely on the type of job and the individual worker.", "Son çalışmalar ne gösteriyor?", ["Evden çalışan herkes daha az verimli", "Birçok durumda tersi doğru olabilir", "Verimlilik ölçülemez"], 1, "\"in many cases, the opposite may be true\""),
        typ("Temkinli hale getirin: \"Everyone knows that sugar is bad for you.\" (It is widely believed)", variants("It is widely believed that sugar is bad for you.", "It is widely believed that sugar is bad for your health.", "It is widely believed that too much sugar is bad for you."), "It is widely believed that sugar is bad for you."),
    ],
    {"kind": "speaking", "task": speak("Aşağıdaki aşırı genellemeleri temkinli bir akademik dile çevirin ve her birine bir karşı görüş ya da sınırlılık ekleyin. Miktar ifadeleri, sıklık zarfları ve kişisiz yapılar kullanın: (1) Turkish people are very hospitable. (2) Old people don't understand technology. (3) Online learning is useless. (4) Everybody in big cities is stressed.",
                                       "One: It is widely believed that Turkish people are very hospitable, and many visitors report being invited into people's homes. However, hospitality can vary from region to region. Two: Some older people tend to find new technology difficult, but a number of studies suggest that many of them use smartphones and the internet regularly. Three: It has been claimed that online learning is less effective, but in many cases, it seems to work well for motivated adult learners. Four: A large number of people in big cities report high levels of stress, although it could be argued that this is partly due to long working hours rather than the city itself.",
                                       ["Miktar ifadeleri", "Kişisiz yapılar", "Sıklık zarfları", "Karşı görüş"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Konuşurken temkin", "Konuşmada diplomatik belirsizlik ifadelerini (I'd say, as far as I know, I might be wrong, but) ve yuvarlama ifadelerini doğal bir şekilde kullanabilirim.",
    {"kind": "dialogue", "title": "Toplantıda", "lines": [
        {"speaker": "Manager", "text": "So, how many customers have we lost this year?"},
        {"speaker": "Emre", "text": "I'd say around 200, more or less. I don't have the exact figure with me."},
        {"speaker": "Manager", "text": "And why are they leaving?"},
        {"speaker": "Emre", "text": "As far as I know, it's mainly the price. I might be wrong, but I think our competitors are about 10% cheaper."},
        {"speaker": "Hande", "text": "To be fair, it's not just the price. Our app is sort of difficult to use, if I'm honest."},
        {"speaker": "Manager", "text": "Hmm. Is that a common complaint?"},
        {"speaker": "Hande", "text": "Correct me if I'm wrong, Emre, but I think it came up quite a lot in the last survey."},
        {"speaker": "Emre", "text": "Yes, that's more or less right."}],
     "questions": [
        mc("How many customers have they lost, according to Emre?", ["Exactly 200", "Around 200", "2,000"], 1, "\"I'd say around 200, more or less.\""),
        mc("What does Hande think is another problem?", ["The staff", "The app is difficult to use", "The location"], 1, "\"Our app is sort of difficult to use\""),
     ]},
    {"explanation": "Konuşmada temkinli dil **kibar, diplomatik ve dürüst** görünmenizi sağlar.\n\n**Emin olmadığınızı belirtmek:**\n\n| İfade | Kullanım |\n|---|---|\n| **I'd say** ... | Tahmini görüş: *I'd say about 200.* |\n| **As far as I know,** ... | Bilgim sınırlı: *As far as I know, it's closed.* |\n| **I might be wrong, but** ... | Görüşü yumuşatma |\n| **Correct me if I'm wrong, but** ... | Kibar itiraz / hatırlatma |\n| **I'm not entirely sure, but** ... | Kısmi bilgi |\n| **If I remember rightly,** ... | Hafızaya dayalı |\n| **I'm under the impression that** ... | İzlenim |\n\n**Yuvarlama ve belirsizlik (rakamlar ve tanımlar):**\n\n| İfade | Örnek |\n|---|---|\n| **around / about / roughly / approximately** | **roughly** 200 |\n| **more or less** | That's **more or less** right. |\n| **or so** | 200 **or so** |\n| **-ish** (samimi) | at six**-ish** / It's blue**-ish**. |\n| **sort of / kind of** (samimi) | It's **sort of** difficult. |\n| **a bit / a little** | It's **a bit** expensive. |\n\n**Diplomatik görüş:**\n\n- ***To be fair,** ...* (adil olmak gerekirse)\n- ***If I'm honest,** ...* / ***To be honest,** ...*\n- ***I see your point, but** ...*\n\n**Dikkat:** *sort of, kind of, -ish* samimidir; resmî yazıda kullanmayın. Fazla kullanmak da **kararsız** bir izlenim verebilir.",
     "examples": [{"en": "As far as I know, the meeting is still on.", "tr": "Bildiğim kadarıyla toplantı hâlâ geçerli."},
                  {"en": "Correct me if I'm wrong, but didn't we agree on Friday?", "tr": "Yanılıyorsam düzelt ama cumada anlaşmamış mıydık?"},
                  {"en": "We'll be there at seven-ish.", "tr": "Yedi gibi orada oluruz."}],
     "turkishNote": "Türkçede \"Bildiğim kadarıyla\", \"Yanılıyor olabilirim ama\", \"Yedi gibi\" ifadeleri günlük konuşmanın doğal bir parçasıdır ve İngilizcede birebir karşılıkları vardır. Türkçe konuşanların İngilizce iş toplantılarında sık yaptığı hata, tahmini rakamları kesin gibi söylemektir (\"We lost 200 customers\"). \"I'd say around 200\" demek hem daha dürüst hem daha profesyoneldir."},
    [
        mc("Tahmini bir rakam vermek:", ["We lost exactly 200 customers.", "I'd say we lost around 200 customers."], 1, "I'd say + around."),
        mc("\"Correct me if I'm wrong, but ...\" işlevi:", ["Kaba itiraz", "Kibar itiraz / hatırlatma"], 1, "Diplomatik."),
        mc("\"seven-ish\" anlamı:", ["Tam yedide", "Yedi gibi"], 1, "-ish."),
        mc("Resmî rapor için uygun değil:", ["approximately 200", "200-ish"], 1, "-ish samimi."),
        gap("As far as I ___, the shop closes at nine.", ["know"], "As far as I know."),
        gap("I ___ be wrong, but I think the deadline is today.", ["might", "may", "could"], "I might be wrong."),
        gap("There were 50 people ___ so at the meeting. (civarında)", ["or"], "or so."),
        gap("To be ___, he did try his best. (adil olmak gerekirse)", ["fair"], "To be fair."),
        listen("How far is the beach? Hmm, I'd say about two kilometres, more or less. If I remember rightly, there's a little café on the way. But I'm not entirely sure it's open in winter.", "Konuşan kafe hakkında ne kadar emin?", ["Tamamen emin", "Tam emin değil", "Kafe yok"], 1, "\"I'm not entirely sure it's open in winter\""),
        typ("Temkinli söyleyin (As far as I know): \"The museum is closed on Mondays.\"", variants("As far as I know, the museum is closed on Mondays.", "As far as I know the museum is closed on Mondays."), "As far as I know, the museum is closed on Mondays."),
    ],
    {"kind": "speaking", "task": speak("Bir iş toplantısında yöneticiniz size sorular soruyor ve kesin bilgilere sahip değilsiniz. Şu sorulara temkinli ve diplomatik cevaplar verin: (1) How many people came to the event? (2) Why did the project go over budget? (3) When will the new website be ready? (4) Do the customers like the new design? I'd say, as far as I know, I might be wrong but, roughly, more or less, to be fair, correct me if I'm wrong kalıplarını kullanın.",
                                       "One: I'd say about 150 people came, more or less. I'll check the exact number with the registration team. Two: As far as I know, it was mainly because the supplier raised their prices in March. To be fair, we also added two extra features that weren't in the original plan. Three: I might be wrong, but I think the developers said roughly three weeks. Four: If I remember rightly, the feedback was mostly positive. Correct me if I'm wrong, Selin, but I think about 70% said they preferred the new design.",
                                       ["Konuşmada temkin ifadeleri", "Yuvarlama ifadeleri", "Diplomatik ton", "Profesyonellik"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Altın orta", "Temkinli ve kesin ifadeleri (hedging ve boosting) dengeli kullanarak ikna edici ve güvenilir bir akademik paragraf yazabilirim.",
    {"kind": "text", "title": "Üç versiyon: aynı paragraf", "body": "Version 1 (too certain):\n\"Homework is useless. It doesn't help students learn, and it makes all children stressed. Schools must stop giving homework immediately.\"\n\nVersion 2 (too hedged):\n\"It could perhaps possibly be suggested that homework might, in some cases, potentially have a somewhat limited effect on some aspects of learning for some students, although this may not necessarily always be the case.\"\n\nVersion 3 (balanced):\n\"The value of homework is clearly a matter of debate. Research suggests that, for younger children, homework appears to have relatively little effect on achievement. For older students, however, there is strong evidence that moderate amounts of homework can improve results. It is undoubtedly true that excessive homework may cause stress. Schools should therefore consider limiting, rather than abolishing, homework.\"",
     "questions": [
        mc("What is the problem with Version 2?", ["It's too certain.", "It's so hedged that it says almost nothing.", "It has grammar mistakes."], 1, "Aşırı temkin."),
        mc("What does Version 3 recommend?", ["Abolishing homework", "Limiting homework", "Giving more homework"], 1, "\"limiting, rather than abolishing, homework\""),
     ]},
    {"explanation": "**Hedging** (temkin) ve **boosting** (kesinlik) arasında **denge** kurmak, C1 seviyesinin en önemli becerilerinden biridir.\n\n| Aşırı kesin ✗ | Aşırı temkinli ✗ | Dengeli ✓ |\n|---|---|---|\n| Kanıtsız, mutlak | Hiçbir şey söylemiyor | Kanıta uygun |\n| *Homework is useless.* | *It could perhaps possibly be suggested ...* | *Research suggests that homework appears to have little effect ...* |\n\n**Boosters (güçlendiriciler):** Güçlü kanıt olduğunda kullanın.\n\n| Booster | Örnek |\n|---|---|\n| **clearly / evidently** | **Clearly**, this is a serious issue. |\n| **undoubtedly / without doubt** | It is **undoubtedly** true that ... |\n| **there is strong / clear evidence that** | **There is strong evidence that** smoking causes cancer. |\n| **it is clear / evident that** | **It is clear that** more research is needed. |\n| **certainly / definitely** | This is **certainly** a factor. |\n| **demonstrate / show** | The data **demonstrate** a clear trend. |\n\n**Altın kurallar:**\n\n1. **Kanıt güçlüyse** → boost: *There is **strong evidence** that ...*\n2. **Kanıt zayıf ya da tartışmalıysa** → hedge: *It **may** ... / **appears to** ...*\n3. **Bir cümlede birden fazla hedge kullanmayın:** ~~It **might possibly perhaps** be~~ → *It **may** be*\n4. **Kendi önerinizi** net belirtin: *Schools **should therefore** ...*\n\n**Not:** İyi bir akademik metin \"her şeyden şüphe eden\" değil, **neyin ne kadar kesin olduğunu bilen** bir metindir.",
     "examples": [{"en": "There is strong evidence that regular exercise reduces the risk of heart disease.", "tr": "Düzenli egzersizin kalp hastalığı riskini azalttığına dair güçlü kanıtlar var."},
                  {"en": "However, its effect on mental health appears to vary considerably.", "tr": "Ancak ruh sağlığı üzerindeki etkisi önemli ölçüde değişkenlik gösteriyor gibi görünüyor."},
                  {"en": "Clearly, further research is needed.", "tr": "Açıkça, daha fazla araştırmaya ihtiyaç var."}],
     "turkishNote": "Temkinli dili yeni öğrenen öğrenciler bazen her cümleyi \"may\", \"perhaps\", \"possibly\" ile doldurur; bu da metni zayıf ve kararsız gösterir. İngilizce akademik yazıda amaç, kanıtın gücüne göre doğru dozu bulmaktır. Türkçe akademik yazıda da benzer bir denge vardır: \"Kesinlikle kanıtlanmıştır\" ile \"belki de olabilir\" arasında, kanıta uygun bir ifade seçin."},
    [
        mc("Aşırı temkinli hangisi?", ["It could perhaps possibly be suggested that it might ...", "Research suggests that it may ..."], 0, "Fazla hedge."),
        mc("Güçlü kanıt varsa:", ["There is strong evidence that smoking causes cancer.", "It might be that smoking could possibly cause cancer."], 0, "Boost."),
        mc("Booster hangisi?", ["arguably", "undoubtedly"], 1, "undoubtedly."),
        mc("Dengeli bir paragrafta öneri:", ["Schools should therefore consider limiting homework.", "Schools could maybe possibly think about it."], 0, "Net öneri."),
        gap("There is ___ evidence that vaccines save lives. (güçlü)", ["strong", "clear", "overwhelming"], "strong evidence."),
        gap("___, more needs to be done. (Açıkça)", ["Clearly", "Evidently"], "Clearly."),
        gap("It is ___ true that stress affects health. (şüphesiz)", ["undoubtedly", "certainly"], "undoubtedly."),
        gap("Schools should ___ consider limiting homework. (bu nedenle)", ["therefore"], "should therefore."),
        listen("There is clear evidence that air pollution damages the lungs. However, its effects on children's learning appear to be less well understood. Some studies suggest a link, but the findings are not yet consistent. What is certain is that cities need to take action.", "Konuşan neyden emin?", ["Kirliliğin öğrenmeyi etkilediğinden", "Şehirlerin harekete geçmesi gerektiğinden", "Hiçbir şeyden"], 1, "\"What is certain is that cities need to take action.\""),
        typ("Aşırı temkini düzeltin: \"It might possibly perhaps be true.\"", variants("It may be true.", "It might be true.", "It could be true.", "It is possibly true.", "It is perhaps true."), "It may be true."),
    ],
    {"kind": "writing", "task": write("Aşağıdaki konulardan birinde dengeli bir akademik paragraf yazın (150–180 kelime): (a) The effects of social media on teenagers, (b) Should university education be free? (c) The impact of tourism on local communities. Bir topic sentence ile başlayın; güçlü kanıt olan noktalar için en az 2 booster, tartışmalı noktalar için en az 4 farklı temkin aracı (fiil, zarf, miktar ifadesi, kişisiz yapı) kullanın ve net bir sonuç / öneri cümlesiyle bitirin. Aşırı temkinden kaçının.",
                                      "The impact of tourism on local communities is clearly complex. On the one hand, there is strong evidence that tourism creates jobs and brings money into regions that might otherwise struggle economically. In many coastal towns in Turkey, for example, a large proportion of local families depend on the summer season for most of their income. On the other hand, tourism appears to have a number of negative effects. Rising property prices tend to push local residents out of popular areas, and in some cases traditional businesses have been replaced by souvenir shops. It could also be argued that mass tourism may gradually weaken local culture, although this is arguably more difficult to measure. What is undoubtedly true is that the benefits are not shared equally. Local governments should therefore develop policies that ensure that a fair share of tourism income stays within the community.",
                                      ["Topic sentence", "En az 2 booster", "En az 4 farklı hedge", "Aşırı temkinden kaçınma", "Net sonuç / öneri"])},
)

u.test([
    mc("En temkinli ve doğru:", ["This study proves that tea prevents cancer.", "This study suggests that tea may reduce the risk of some cancers."], 1, "suggest + may"),
    mc("\"tend to\" anlamı:", ["Her zaman", "-me eğiliminde"], 1, "tend to"),
    mc("Aşırı genelleme:", ["Many students find maths difficult.", "All students hate maths."], 1, "All"),
    mc("Aşırı temkinli:", ["It may be true.", "It could perhaps possibly be true."], 1, "Fazla hedge"),
    mc("Booster:", ["arguably", "undoubtedly"], 1, "undoubtedly"),
    gap("The results ___ to support the theory. (görünüyor)", ["seem", "appear"], "seem / appear to"),
    gap("I agree with you to some ___.", ["extent"], "to some extent"),
    gap("It ___ be argued that the plan is too expensive. (savunulabilir)", ["could", "might", "can"], "It could be argued"),
    gap("As far as I ___, the shop is still open.", ["know"], "As far as I know"),
    gap("A ___ of studies have found similar results. (bir dizi)", ["number"], "A number of"),
    gap("There is ___ evidence that smoking damages health. (güçlü)", ["strong", "clear", "overwhelming"], "strong evidence"),
    mc("\"arguably the greatest writer\"", ["Kesinlikle en büyük yazar", "Tartışmaya açık ama savunulabilir şekilde en büyük yazar"], 1, "arguably"),
    listen("The fire appears to have started in the kitchen, although investigators haven't confirmed this yet. As far as we know, nobody was injured. It's thought that the restaurant may have been closed at the time.", "Yangının nerede başladığı hakkında ne biliniyor?", ["Kesin olarak mutfakta", "Mutfakta başlamış gibi görünüyor ama doğrulanmadı", "Hiçbir şey bilinmiyor"], 1, "\"appears to have started in the kitchen, although investigators haven't confirmed this yet\""),
    typ("Temkinli hale getirin (appear to have): \"The thief entered through the window.\"", variants("The thief appears to have entered through the window.", "It appears that the thief entered through the window."), "The thief appears to have entered through the window."),
    write("\"Is artificial intelligence a threat to jobs?\" sorusuna dengeli bir akademik paragrafla cevap verin (160–200 kelime). Topic sentence ile başlayın; güçlü kanıta dayalı noktalar için boosters (clearly, there is strong evidence, undoubtedly), tartışmalı noktalar için çeşitli hedging araçları (seem, tend to, may, arguably, to some extent, in some cases, It could be argued that) kullanın. Net bir sonuçla bitirin ve aşırı kesin ya da aşırı temkinli ifadelerden kaçının.",
          "Whether artificial intelligence represents a threat to jobs is clearly one of the most important economic questions of our time. There is strong evidence that AI is already changing the nature of many occupations, particularly those involving routine tasks such as data entry and basic customer service. In these areas, a considerable number of jobs may well disappear over the next two decades. However, the overall impact appears to be more complex than many headlines suggest. Historically, new technologies have tended to create new types of work, even as they destroyed others, and it could be argued that AI will follow a similar pattern. In some cases, it seems to make workers more productive rather than replacing them. Nevertheless, it is undoubtedly true that the benefits and costs will not be shared equally. Workers with fewer qualifications are arguably the most at risk, at least in the short term. Governments should therefore invest significantly in retraining programmes to ensure that no group is left behind.",
          ["Topic sentence", "Boosters", "Çeşitli hedging araçları", "Denge", "Net sonuç"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

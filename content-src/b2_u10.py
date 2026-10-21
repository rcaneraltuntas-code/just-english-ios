"""B2 Ünite 10: Bilim."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("B2", 10, "Bilim", "Science",
         "Genel ve özel anlamda article'ları (a / the / sıfır article) doğru kullanabilir, miktar bildiren ileri yapılarla (a few / few, plenty of, the majority of, neither of) bilimsel ve sağlıkla ilgili bilgileri doğru aktarabilir ve araştırma bulgularını özetleyen popüler bilim metni yazabilirim.",
         ["genelleme yaparken article: sıfır article ve the + tekil isim", "the kullanımı: özel isimler, kurumlar, coğrafya", "few / a few, little / a little, plenty of, a great deal of", "each / every, both / either / neither, most / most of", "araştırma bulgularını aktarma"],
         ["bilim ve keşifler", "sağlık ve tıp", "araştırma ve veri"],
         {"title": "Bilim kafe", "durationMinutes": 45,
          "goal": "Her öğrenci kısa bir bilimsel bulgu ya da keşif seçer (yeni bir araştırma, ünlü bir buluş, sağlıkla ilgili bir efsane). 2 dakikada sınıfa \"bilim kafe\" tarzında anlatır, doğru article ve miktar ifadeleri kullanır. Dinleyenler sorular sorar ve sınıf \"doğru mu, efsane mi?\" oylaması yapar."})

u.vocab([
    ("research", "araştırma", "Research shows that sleep improves memory.", "Araştırmalar uykunun hafızayı geliştirdiğini gösteriyor.", "sayılamaz"),
    ("study", "çalışma, araştırma", "A recent study found a link between diet and mood.", "Yakın tarihli bir çalışma beslenme ve ruh hali arasında bir bağlantı buldu.", None),
    ("findings", "bulgular", "The findings were published in a scientific journal.", "Bulgular bilimsel bir dergide yayımlandı.", None),
    ("discovery", "keşif", "The discovery of penicillin changed medicine.", "Penisilinin keşfi tıbbı değiştirdi.", None),
    ("experiment", "deney", "They carried out an experiment on mice.", "Fareler üzerinde bir deney yaptılar.", None),
    ("evidence", "kanıt", "There is little evidence that the diet works.", "Diyetin işe yaradığına dair çok az kanıt var.", None),
    ("cure", "tedavi, çare; iyileştirmek", "There is still no cure for the common cold.", "Soğuk algınlığının hâlâ bir tedavisi yok.", None),
    ("treatment", "tedavi", "The new treatment is very effective.", "Yeni tedavi çok etkili.", None),
    ("disease", "hastalık", "Heart disease is a major health problem.", "Kalp hastalığı büyük bir sağlık sorunu.", None),
    ("symptom", "belirti", "Fever is a common symptom of flu.", "Ateş gribin yaygın bir belirtisidir.", None),
    ("vaccine", "aşı", "Vaccines have saved millions of lives.", "Aşılar milyonlarca hayat kurtardı.", None),
    ("immune system", "bağışıklık sistemi", "Exercise strengthens the immune system.", "Egzersiz bağışıklık sistemini güçlendirir.", None),
    ("species", "tür", "Thousands of species are in danger.", "Binlerce tür tehlike altında.", "tekil = çoğul"),
    ("cell", "hücre", "The human body contains trillions of cells.", "İnsan vücudu trilyonlarca hücre içerir.", None),
    ("gene", "gen", "Some diseases are caused by a single gene.", "Bazı hastalıklar tek bir genden kaynaklanır.", None),
    ("the majority of", "çoğunluğu", "The majority of participants were women.", "Katılımcıların çoğunluğu kadındı.", None),
    ("a great deal of", "çok miktarda (sayılamaz)", "The project requires a great deal of money.", "Proje çok miktarda para gerektiriyor.", None),
    ("plenty of", "bol bol, yeterince", "Drink plenty of water.", "Bol su için.", None),
    ("hardly any", "neredeyse hiç", "There's hardly any sugar in this.", "Bunda neredeyse hiç şeker yok.", None),
    ("participant", "katılımcı", "The study had 2,000 participants.", "Çalışmanın 2.000 katılımcısı vardı.", None),
    ("significant", "anlamlı, önemli", "There was a significant improvement.", "Önemli bir iyileşme vardı.", None),
    ("breakthrough", "çığır açan buluş", "It was a major scientific breakthrough.", "Büyük bir bilimsel atılımdı.", None),
    ("side effect", "yan etki", "The drug has few side effects.", "İlacın az yan etkisi var.", None),
    ("prevent", "önlemek", "Washing your hands helps to prevent infection.", "Ellerinizi yıkamak enfeksiyonu önlemeye yardımcı olur.", None),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Genel olarak konuşmak", "Genelleme yaparken sıfır article, a / an ve the + tekil isim arasındaki farkı kullanabilirim.",
    {"kind": "text", "title": "Arılar neden önemli?", "body": "Bees are among the most important animals on the planet. Without them, we would lose many of the fruits and vegetables we eat every day.\n\nThe honeybee, in particular, is a remarkable insect. A single bee visits up to several thousand flowers a day, and a colony can contain tens of thousands of bees.\n\nBut bees are in danger. Pesticides, disease and the loss of wild flowers have all played a part. Scientists say that protecting bees is not just about honey. It is about food security for the whole world.\n\nThe good news is that everyone can help. Planting flowers on a balcony or in a garden gives bees food and shelter.",
     "questions": [
        mc("Why are bees important?", ["They make honey.", "Without them we would lose many fruits and vegetables.", "They eat pests."], 1, "\"we would lose many of the fruits and vegetables\""),
        mc("How can everyone help?", ["By buying honey", "By planting flowers", "By building hives"], 1, "\"Planting flowers on a balcony or in a garden\""),
     ]},
    {"explanation": "Bir şey hakkında **genel olarak** (o türün hepsi hakkında) konuşmanın üç yolu var:\n\n| Yapı | Örnek | Kullanım |\n|---|---|---|\n| **Sıfır article + çoğul** | **Bees** are important. | En yaygın, günlük dil |\n| **Sıfır article + sayılamaz** | **Water** boils at 100°C. / **Research** shows ... | Sayılamaz isimler |\n| **the + tekil** | **The honeybee** is a remarkable insect. | Daha resmî, bilimsel: tür, buluş, müzik aleti |\n| **a / an + tekil** | **A** bee visits many flowers. | \"Herhangi bir\" örnek üzerinden |\n\n**the + tekil isim** özellikle şunlar için kullanılır:\n\n- **Hayvan / bitki türleri:** *The tiger is in danger.*\n- **Buluşlar:** ***The telephone** was invented in the 19th century.*\n- **Müzik aletleri:** *She plays **the** violin.*\n- **Vücut organları (genel):** ***The heart** pumps blood.*\n\n**En sık hata: genellemede \"the\" kullanmak**\n\n- ~~**The** bees are important.~~ → **Bees** are important. (Genel)\n- ~~**The** science is interesting.~~ → **Science** is interesting.\n- ~~I love **the** music.~~ → I love **music**. (Genel)\n- Ama: I love **the music** in this film. (Belirli)",
     "examples": [{"en": "Vaccines save millions of lives every year.", "tr": "Aşılar her yıl milyonlarca hayat kurtarıyor."},
                  {"en": "The human brain weighs about 1.4 kilos.", "tr": "İnsan beyni yaklaşık 1,4 kilo ağırlığındadır."},
                  {"en": "The microscope was invented around 1600.", "tr": "Mikroskop 1600 civarında icat edildi."}],
     "turkishNote": "Türkçede article olmadığı için \"Arılar önemlidir\" ve \"Bu arılar önemli\" arasındaki fark bağlamla anlaşılır. İngilizcede genel konuşurken çoğul ve sayılamaz isimlerin önüne \"the\" konmaz. Türkçe konuşanların en sık hatası \"The people are...\", \"The life is...\" gibi genellemelerdir. Doğrusu \"People are...\", \"Life is...\"."},
    [
        mc("Genel olarak: \"___ are disappearing from cities.\"", ["The bees", "Bees"], 1, "Genelleme → sıfır article."),
        mc("Hangisi doğru?", ["The life is short.", "Life is short."], 1, "Sayılamaz, genel."),
        mc("Bilimsel üslupta tür:", ["The dolphin is an intelligent animal.", "Dolphin is an intelligent animal."], 0, "the + tekil."),
        mc("Hangisi doğru?", ["She plays piano and the guitar.", "She plays the piano and the guitar."], 1, "Müzik aletleri → the."),
        mc("Genel bir bilgi:", ["The research shows that exercise improves mood.", "Research shows that exercise improves mood."], 1, "Sayılamaz, genel → sıfır article."),
        gap("___ telephone was invented by Alexander Graham Bell.", ["The"], "Buluş → the."),
        mc("Hangisi doğru?", ["I don't like coffee, but the coffee in this café is excellent.", "I don't like the coffee, but coffee in this café is excellent."], 0, "Genel → sıfır; belirli → the."),
        gap("___ heart pumps about 7,000 litres of blood a day.", ["The"], "Organ (genel) → the."),
        listen("Sharks have been on Earth for more than 400 million years. The great white shark can detect tiny amounts of blood in the water. But sharks are in danger, mostly because of overfishing.", "Köpekbalıklarını en çok ne tehdit ediyor?", ["İklim değişikliği", "Aşırı avlanma", "Plastik"], 1, "\"mostly because of overfishing\""),
        typ("İngilizcesi: \"Kediler bağımsız hayvanlardır.\"", variants("Cats are independent animals.", "The cat is an independent animal."), "Cats are independent animals."),
    ],
    {"kind": "speaking", "task": speak("Sevdiğiniz bir hayvanı, bir buluşu ve bir bilim dalını genel olarak tanıtın. Her biri için en az 2 cümle kurun. Sıfır article + çoğul, the + tekil (tür / buluş) ve sayılamaz isimleri doğru kullanın.",
                                       "Elephants are my favourite animals. The African elephant is the largest land animal in the world, and elephants can remember other elephants for many years. The bicycle is one of the best inventions ever. It was invented in the 19th century, and bicycles are still the cheapest and healthiest way to travel in a city. I find biology fascinating. Biology explains how life works, from cells to whole ecosystems.",
                                       ["Sıfır article ile genelleme", "the + tekil (tür, buluş)", "Sayılamaz isimler"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "The ne zaman gelir?", "Özel isimler, kurumlar ve coğrafi adlarla the kullanımının kurallarını uygulayabilirim.",
    {"kind": "text", "title": "Bir bilim insanının hayatı", "body": "Aziz Sancar was born in 1946 in Savur, a small town in Mardin. He studied medicine at Istanbul University and worked as a doctor for a short time before moving to the United States.\n\nHe did his PhD at the University of Texas and later became a professor at the University of North Carolina, where he still works today.\n\nIn 2015, he won the Nobel Prize in Chemistry, together with Tomas Lindahl from Sweden and Paul Modrich from the USA, for their work on how cells repair damaged DNA. His research helps scientists understand diseases such as cancer.\n\nAfter the prize, he gave his Nobel medal to Anıtkabir in Ankara as a gift to the Turkish people.",
     "questions": [
        mc("Where did Aziz Sancar study medicine?", ["In Texas", "At Istanbul University", "In North Carolina"], 1, "\"He studied medicine at Istanbul University\""),
        mc("What was his Nobel Prize for?", ["A new vaccine", "How cells repair damaged DNA", "Discovering penicillin"], 1, "\"how cells repair damaged DNA\""),
     ]},
    {"explanation": "**Coğrafi adlar:**\n\n| the KULLANILIR | the KULLANILMAZ |\n|---|---|\n| Okyanus, deniz, nehir: **the** Pacific, **the** Black Sea, **the** Nile | Göl: Lake Van |\n| Dağ sıraları: **the** Alps, **the** Taurus Mountains | Tek dağ: Mount Ararat (Ağrı Dağı) |\n| Çoğul ülkeler, \"States/Kingdom/Republic\": **the** USA, **the** UK, **the** Netherlands, **the** Philippines | Çoğu ülke, şehir, kıta: Turkey, Ankara, Asia |\n| Çöller: **the** Sahara | |\n\n**Kurumlar ve yerler:**\n\n| Yapı | Örnek |\n|---|---|\n| **University of / of** yapısı → the | **the** University of Texas, **the** Museum of Modern Art |\n| İsimle başlayan → the yok | Istanbul University, Harvard University |\n\n**Kurum işlevi için the yok:**\n\n| the YOK (amacına uygun) | the VAR (bina olarak) |\n|---|---|\n| She's **in hospital**. (hasta) | I visited her at **the hospital**. |\n| He went **to prison**. (mahkûm) | His mum went to **the prison** to see him. |\n| I'm **at school / university**. (öğrenci) | The meeting is at **the school**. |\n\n**Hastalıklar:** Çoğunlukla article yok: *cancer, diabetes, flu* (ama *a cold, a headache*)\n\n**Benzersiz şeyler:** **the** sun, **the** moon, **the** Earth (ama *on Earth*), **the** internet",
     "examples": [{"en": "The Nile is the longest river in Africa.", "tr": "Nil, Afrika'nın en uzun nehridir."},
                  {"en": "My grandmother is in hospital with pneumonia.", "tr": "Büyükannem zatürreyle hastanede yatıyor."},
                  {"en": "She did her PhD at the University of Oxford.", "tr": "Doktorasını Oxford Üniversitesi'nde yaptı."}],
     "turkishNote": "Türkçede \"hastanede\" hem \"hasta olarak yatıyor\" hem de \"hastane binasında\" anlamına gelebilir. İngilizcede bu fark article ile yapılır: \"in hospital\" (hasta), \"at the hospital\" (ziyaretçi, çalışan). Ülke adlarında da dikkat: \"the Turkey\" yanlıştır; ama \"the United States\" ve \"the Netherlands\" doğrudur."},
    [
        mc("Hangisi doğru?", ["the Mount Everest", "Mount Everest"], 1, "Tek dağ → the yok."),
        mc("Hangisi doğru?", ["the Black Sea", "Black Sea"], 0, "Deniz → the."),
        mc("\"Annem hasta, hastanede yatıyor.\"", ["My mum is in hospital.", "My mum is in the hospital building."], 0, "Kurum işlevi → the yok."),
        mc("Hangisi doğru?", ["She lives in the Netherlands.", "She lives in Netherlands."], 0, "Çoğul ülke → the."),
        gap("Lake Van is in eastern Turkey. ___ Euphrates also starts in Turkey.", ["The"], "Nehir → the."),
        gap("He studied at ___ University of Cambridge.", ["the"], "University of → the."),
        mc("Hangisi doğru?", ["My aunt has the diabetes.", "My aunt has diabetes."], 1, "Hastalık → genellikle article yok."),
        mc("Hangisi doğru?", ["Is there life anywhere else, or only on Earth?", "Is there life anywhere else, or only on the Earth?"], 0, "on Earth kalıbında the kullanılmaz."),
        listen("After finishing school, I went to university in Ankara. Then I did a master's at the University of Edinburgh. Now I'm a researcher at the hospital where my father was a doctor.", "Konuşan şu anda nerede çalışıyor?", ["Edinburgh'da", "Babasının doktor olduğu hastanede", "Bir okulda"], 1, "\"at the hospital where my father was a doctor\""),
        match([("the Alps", "dağ sırası"), ("Mount Ararat", "tek dağ"), ("the Pacific", "okyanus"), ("Lake Van", "göl"), ("the Sahara", "çöl")], "Eşleştirin: Neden the var ya da yok?"),
    ],
    {"kind": "speaking", "task": speak("Türkiye'den ya da dünyadan bir bilim insanının, bir sporcunun ya da bir sanatçının hayatını anlatın. Doğduğu yer, okuduğu kurumlar (the University of ... / ... University), gittiği ülkeler (the USA, Germany), coğrafi yerler (the Mediterranean, Lake ..., Mount ...) gibi en az 6 özel isim kullanın ve article'lara dikkat edin.",
                                       "Cahit Arf was one of Turkey's greatest mathematicians. He was born in Thessaloniki in 1910, and his family later moved to Izmir. He studied in France and then did his PhD at the University of Göttingen in Germany. Later, he taught at Istanbul University and spent time at the Institute for Advanced Study in the USA. One of his discoveries is named after him: the Arf invariant. His picture was even on the 10 lira note.",
                                       ["Coğrafi adlarda the", "Kurum adlarında the", "Ülke adları"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "Az, biraz, bol", "few / a few, little / a little, plenty of, a great deal of ve hardly any ile miktarı doğru ve vurgulu ifade edebilirim.",
    {"kind": "dialogue", "title": "Doktor kontrolü", "lines": [
        {"speaker": "Doctor", "text": "Your blood tests look good, but your vitamin D is a little low."},
        {"speaker": "Ayhan", "text": "Really? I eat plenty of healthy food."},
        {"speaker": "Doctor", "text": "Food isn't the main source. Few people get enough vitamin D from food alone. Do you spend much time outside?"},
        {"speaker": "Ayhan", "text": "Hardly any. I work in an office, and I drive to work."},
        {"speaker": "Doctor", "text": "That's the problem. Try to spend a little time in the sun every day, even just fifteen minutes. I'll also give you a few supplements."},
        {"speaker": "Ayhan", "text": "Do they have any side effects?"},
        {"speaker": "Doctor", "text": "Very few, as long as you take the right dose."}],
     "questions": [
        mc("What is low in Ayhan's blood?", ["Iron", "Vitamin D", "Sugar"], 1, "\"your vitamin D is a little low\""),
        mc("How much time does Ayhan spend outside?", ["A lot", "Hardly any", "A few hours a day"], 1, "\"Hardly any.\""),
     ]},
    {"explanation": "**a few / few** (sayılabilir) ve **a little / little** (sayılamaz)\n\n| Yapı | Anlam | Ton |\n|---|---|---|\n| **a few** people | birkaç kişi | olumlu: **yeterli** |\n| **few** people | çok az kişi | olumsuz: **yetersiz** |\n| **a little** time | biraz zaman | olumlu: **yeterli** |\n| **little** time | çok az zaman | olumsuz: **yetersiz** |\n\n- *I have **a few** friends here.* (Birkaç arkadaşım var, yalnız değilim.)\n- *I have **few** friends here.* (Çok az arkadaşım var, yalnızım.)\n- ***Little** is known about this disease.* (Hakkında çok az şey biliniyor.)\n\n**Bol miktar:**\n\n| Yapı | İsim türü | Örnek |\n|---|---|---|\n| **plenty of** | ikisi de | plenty of **water** / plenty of **ideas** |\n| **a lot of / lots of** | ikisi de | a lot of **research** |\n| **a great deal of** | sayılamaz (resmî) | a great deal of **evidence** |\n| **a large number of** | sayılabilir (resmî) | a large number of **patients** |\n| **a large amount of** | sayılamaz (resmî) | a large amount of **data** |\n\n**Çok az / hiç:**\n\n- **hardly any** = neredeyse hiç: *There's **hardly any** sugar left.*\n- **very few / very little** = çok az\n- **no / none** = hiç",
     "examples": [{"en": "Few people know that the brain has no pain receptors.", "tr": "Beynin ağrı reseptörü olmadığını çok az kişi bilir."},
                  {"en": "There is a great deal of evidence that smoking causes cancer.", "tr": "Sigaranın kansere neden olduğuna dair çok fazla kanıt var."},
                  {"en": "I had a little time, so I read the article.", "tr": "Biraz vaktim vardı, o yüzden makaleyi okudum."}],
     "turkishNote": "Türkçede \"birkaç\" ile \"çok az\" arasındaki fark kelime seçimiyle yapılır; İngilizcede bu fark sadece \"a\" ile belirlenir: a few (birkaç, yeterli) / few (çok az, yetersiz). Bu küçük kelime cümlenin tonunu tamamen değiştirir. \"a great deal of\" sadece sayılamaz isimlerle kullanılır: \"a great deal of people\" yanlıştır; \"a large number of people\" doğrudur."},
    [
        mc("\"Partiye çok az kişi geldi, hayal kırıklığıydı.\"", ["A few people came.", "Few people came."], 1, "Olumsuz → few."),
        mc("\"Biraz zamanım var, yardım edebilirim.\"", ["I have little time.", "I have a little time."], 1, "Olumlu → a little."),
        mc("Hangisi doğru?", ["a great deal of patients", "a large number of patients"], 1, "Sayılabilir → a large number of."),
        mc("\"There's hardly any milk.\"", ["Çok süt var.", "Neredeyse hiç süt yok."], 1, "hardly any."),
        gap("Drink ___ of water when it's hot. (bol)", ["plenty"], "plenty of."),
        gap("Very ___ is known about this species. (çok az)", ["little"], "Sayılamaz, olumsuz."),
        gap("The study produced a large ___ of data. (miktar)", ["amount"], "a large amount of."),
        gap("I've got a ___ questions about the treatment. (birkaç)", ["few"], "a few."),
        listen("Scientists have spent a great deal of time studying this disease, but few treatments have been successful so far. However, a few recent studies have shown some promising results, so there is a little hope.", "Konuşan durum hakkında ne söylüyor?", ["Hiç umut yok", "Biraz umut var", "Hastalık tamamen tedavi edildi"], 1, "\"there is a little hope\""),
        typ("İngilizcesi: \"Bu hastalık hakkında çok az şey biliniyor.\"", variants("Little is known about this disease.", "Very little is known about this disease."), "Little is known about this disease."),
    ],
    {"kind": "speaking", "task": speak("Kendi sağlık alışkanlıklarınızı anlatın: Ne kadar su içiyorsunuz, ne kadar uyuyorsunuz, ne kadar spor yapıyorsunuz, ne kadar şeker / kahve tüketiyorsunuz? a few / few, a little / little, plenty of, hardly any ve a lot of yapılarını doğru tonla kullanın.",
                                       "To be honest, my habits aren't perfect. I drink plenty of tea, but I drink very little water, maybe two glasses a day. I get hardly any exercise during the week because I work long hours, but I go for a long walk at the weekend. I eat a lot of bread and quite a few sweets, which isn't great. I usually sleep only six hours, so I have little energy in the afternoons. I've made a few changes this month, though. I've started taking a little time every evening to stretch.",
                                       ["a few / few, a little / little", "plenty of, hardly any", "Ton farkını doğru kullanma"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Her biri, ikisi de, hiçbiri", "each / every, both / either / neither, all / none ve most / most of yapılarını doğru kullanabilirim.",
    {"kind": "text", "title": "Bir ilaç denemesi", "body": "In a recent study, 400 patients with high blood pressure were divided into two groups. Each group received a different treatment for six months.\n\nThe first group took a new drug, and the second group took a placebo (a pill with no medicine in it). Every participant also followed the same diet and exercise plan.\n\nBy the end of the study, most of the patients in the first group had lower blood pressure. Interestingly, some of the patients in the second group also improved, probably because of the diet and exercise.\n\nBoth groups reported a few minor side effects, but neither group had any serious problems. None of the participants left the study early.\n\nThe researchers say that both the drug and lifestyle changes are important, and that either one alone may not be enough for most people.",
     "questions": [
        mc("What did the second group take?", ["A new drug", "A placebo", "Vitamins"], 1, "\"the second group took a placebo\""),
        mc("Did any participants leave early?", ["Yes, a few", "No, none of them", "Most of them"], 1, "\"None of the participants left the study early.\""),
     ]},
    {"explanation": "**each / every**\n\n| | Anlam | Örnek |\n|---|---|---|\n| **each** | her biri (ayrı ayrı, 2 ve üstü) | **Each** group received a different treatment. |\n| **every** | her (hepsi bir arada, 3 ve üstü) | **Every** participant followed the diet. |\n\nİkisi de **tekil isim + tekil fiil** alır: *Every patient **was** ...*\n\n**İki şey için: both / either / neither**\n\n| Yapı | Anlam | Örnek |\n|---|---|---|\n| **both** (of) | ikisi de | **Both** groups improved. / **Both of** them ... |\n| **either** (of) | ikisinden biri | You can take **either** pill. |\n| **neither** (of) | ikisi de değil | **Neither** group had problems. |\n| **both ... and** | hem ... hem | **both** the drug **and** exercise |\n| **either ... or** | ya ... ya | **either** today **or** tomorrow |\n| **neither ... nor** | ne ... ne | **neither** sugar **nor** salt |\n\n**most / most of**\n\n| Yapı | Örnek |\n|---|---|\n| **most** + isim (genel) | **Most people** like chocolate. |\n| **most of the / my / these** + isim (belirli) | **Most of the patients** in the study improved. |\n| ~~most of people~~ ✗ | |\n\n**all / none:** *All (of) the participants ... / **None of** the participants ...*",
     "examples": [{"en": "Each patient was given a different dose.", "tr": "Her hastaya farklı bir doz verildi."},
                  {"en": "Neither treatment had serious side effects.", "tr": "İki tedavinin de ciddi yan etkisi yoktu."},
                  {"en": "Most of the students in my class want to study medicine.", "tr": "Sınıfımdaki öğrencilerin çoğu tıp okumak istiyor."}],
     "turkishNote": "Türkçede \"insanların çoğu\" dediğimiz için \"most of people\" demek doğal gelir, ama bu yanlıştır. Genel konuşurken \"most people\", belirli bir grup için \"most of the people\" kullanılır. Ayrıca \"Her iki grup da\" demek için \"both groups\", \"İki grup da ... değildi\" demek için \"neither group\" kullanılır; \"both groups didn't\" pek doğal değildir."},
    [
        mc("Hangisi doğru?", ["Most of people like music.", "Most people like music."], 1, "Genel → most."),
        mc("Hangisi doğru?", ["Every patients were tested.", "Every patient was tested."], 1, "every + tekil."),
        mc("\"İki ilaç da işe yaramadı.\"", ["Neither drug worked.", "Both drugs didn't work."], 0, "neither."),
        mc("\"Ya bugün ya yarın gelebilirsin.\"", ["You can come neither today nor tomorrow.", "You can come either today or tomorrow."], 1, "either ... or."),
        gap("___ of the participants left the study. (hiçbiri)", ["None"], "None of."),
        gap("___ the drug and exercise helped. (hem ... hem de)", ["Both"], "both ... and."),
        gap("Most ___ the patients in the study were over 50.", ["of"], "most of the."),
        gap("___ child in the class received a book. (her)", ["Every", "Each"], "every / each + tekil."),
        listen("We tested two new vaccines. Both of them were safe, but neither was effective enough against the new variant. Each vaccine was given to 500 volunteers, and most of the volunteers reported only mild side effects.", "Aşılar hakkında hangisi doğru?", ["İkisi de etkili", "İkisi de güvenli ama yeterince etkili değil", "Biri tehlikeli"], 1, "\"Both of them were safe, but neither was effective enough\""),
        order(["Neither", "the", "doctor", "nor", "the", "nurse", "noticed", "the", "mistake"], "Neither the doctor nor the nurse noticed the mistake.", "neither ... nor.", "Ne doktor ne de hemşire hatayı fark etti."),
    ],
    {"kind": "speaking", "task": speak("Ailenizi ya da arkadaş grubunuzu sağlık ve yaşam alışkanlıkları açısından karşılaştırın. each / every, both / neither / either, most / most of, all / none of yapılarından en az 6'sını kullanın.",
                                       "There are four people in my family, and each of us has different habits. Both of my parents get up early, but neither of them does any sport. My brother and I both go to the gym, but neither of us eats very healthily. Most of our meals are home-cooked, though, which is good. None of us smokes, and all of us love walking by the sea at the weekend. Every Sunday, we have a big breakfast together.",
                                       ["each / every + tekil", "both / either / neither", "most / most of", "all / none of"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Bulguları aktarmak", "Bir araştırmanın bulgularını doğru article ve miktar ifadeleriyle özetleyen popüler bilim metni yazabilirim.",
    {"kind": "text", "title": "Popüler bilim: Uyku ve ekranlar", "body": "Do you check your phone in bed? You're not alone, and it may be affecting your sleep.\n\nA recent study of 2,000 university students found that the majority of participants used a screen in the hour before bed. Nearly a third said they used their phones for more than an hour after turning off the lights.\n\nThe researchers found a significant link between screen use and sleep quality. Students who used screens late at night slept, on average, 45 minutes less than those who didn't. They were also twice as likely to feel tired during the day.\n\nHowever, only a small minority of participants believed that their phones affected their sleep.\n\nThe good news is that small changes can make a big difference. When a group of students stopped using screens an hour before bed for two weeks, most of them reported sleeping better.\n\nThe researchers point out that the study had some limitations. All of the participants were students, so the findings may not apply to everyone.",
     "questions": [
        mc("How much less did late screen users sleep on average?", ["15 minutes", "45 minutes", "2 hours"], 1, "\"45 minutes less\""),
        mc("What is one limitation of the study?", ["It was too short.", "All the participants were students.", "It had too few participants."], 1, "\"All of the participants were students\""),
     ]},
    {"explanation": "**Araştırma bulgularını aktarma dili:**\n\n| İşlev | Kalıplar |\n|---|---|\n| **Çalışmayı tanıtma** | *A recent study of 2,000 adults found that ...* / *Researchers at ... have discovered that ...* |\n| **Oranlar** | *the majority of* (çoğunluğu), *a minority of* (azınlığı), *nearly half*, *a third of*, *one in five*, *over 60%* |\n| **Karşılaştırma** | *twice as likely to* (iki kat daha fazla olası), *significantly more / less* |\n| **İlişki** | *a link between X and Y* / *X is associated with Y* |\n| **Dikkatli yorum** | *suggests that* / *may be linked to* / *it appears that* |\n| **Sınırlılık** | *The study had some limitations.* / *The findings may not apply to ...* / *More research is needed.* |\n\n**Oran ve fiil uyumu:**\n\n- *The majority of **participants were** ...* (çoğul isim → çoğul fiil)\n- *A third of **the money was** ...* (sayılamaz → tekil fiil)\n- *One in five **people has / have** ...* (ikisi de kabul edilir)\n\n**Bağlantı ≠ neden:** *Screen use **is linked to** poor sleep.* (Bağlantılı, ama sebep olduğu kanıtlanmadı.) Popüler bilim yazarken bu farka dikkat edin.",
     "examples": [{"en": "The majority of participants reported feeling better.", "tr": "Katılımcıların çoğunluğu daha iyi hissettiğini bildirdi."},
                  {"en": "Smokers are twice as likely to develop heart disease.", "tr": "Sigara içenlerin kalp hastalığına yakalanma olasılığı iki kat daha fazla."},
                  {"en": "The findings suggest that more research is needed.", "tr": "Bulgular daha fazla araştırmaya ihtiyaç olduğunu gösteriyor."}],
     "turkishNote": "Türk basınında \"Bilim insanları kanıtladı: Kahve kanseri önlüyor!\" gibi başlıklar sık görülür. İyi bir İngilizce popüler bilim yazısı ise daha temkinlidir: \"proves\" yerine \"suggests\", \"causes\" yerine \"is linked to\" kullanır. Bu temkinli dili C1'de daha ayrıntılı göreceksiniz (hedging). Oranlarda da Türkçedeki \"üçte biri\" İngilizcede \"a third of\" olur; \"one third of\" da kullanılabilir."},
    [
        mc("Katılımcıların çoğunluğu:", ["The majority of participants", "The majority participants"], 0, "the majority of."),
        mc("Bağlantı (sebep değil):", ["Screen use causes poor sleep.", "Screen use is linked to poor sleep."], 1, "Temkinli."),
        mc("\"İki kat daha olası\":", ["twice as likely to", "two times likely"], 0, "twice as likely to."),
        mc("Doğru fiil: \"The majority of the students ___ happy.\"", ["was", "were"], 1, "Çoğul isim → were."),
        gap("Nearly a ___ of the participants were over 60. (üçte biri)", ["third"], "a third of."),
        gap("The study found a significant ___ between diet and mood. (bağlantı)", ["link"], "a link between."),
        gap("More research is ___. (gerekli)", ["needed"], "More research is needed."),
        gap("The findings may not ___ to older adults. (geçerli olmak)", ["apply"], "apply to."),
        listen("According to a new survey, one in four adults in the city doesn't eat breakfast. Interestingly, people who skip breakfast are significantly more likely to snack in the afternoon. However, the researchers say the study doesn't prove that skipping breakfast causes snacking.", "Araştırmacılar ne konusunda dikkatli?", ["Katılımcı sayısı", "Kahvaltı atlamanın atıştırmaya neden olduğunu kanıtlamadıkları", "Anket tarihi"], 1, "\"the study doesn't prove that skipping breakfast causes snacking\""),
        typ("İngilizcesi: \"Katılımcıların çoğunluğu kadındı.\"", variants("The majority of participants were women.", "The majority of the participants were women.", "Most of the participants were women.", "Most participants were women."), "The majority of participants were women."),
    ],
    {"kind": "writing", "task": write("Bir popüler bilim dergisi için hayali bir araştırmanın bulgularını aktaran kısa bir makale yazın (180–220 kelime). Konu seçenekleri: kahve ve hafıza, yürüyüş ve mutluluk, müzik ve çalışma verimi. Okuyucunun ilgisini çeken bir giriş, oranlar (the majority of, a third of, one in five), karşılaştırma (twice as likely), temkinli yorum (suggests, is linked to) ve bir sınırlılık cümlesi kullanın. Article ve miktar ifadelerine dikkat edin.",
                                      "Need a mood boost? Try going for a walk.\n\nA new study of 1,500 office workers suggests that a short daily walk may have a significant effect on happiness. The participants were divided into two groups. Each person in the first group walked for 20 minutes every day for eight weeks, while the second group continued their normal routine.\n\nBy the end of the study, the majority of walkers said they felt happier and less stressed. Nearly a third reported sleeping better, and one in five said they had more energy at work. In contrast, very few people in the second group noticed any change.\n\nThe researchers also found that walkers were twice as likely to describe their mood as \"good\" or \"very good\". Interestingly, the benefits were greatest for people who walked outdoors, especially in parks or near water.\n\nHowever, the study had some limitations. All of the participants worked in offices in large cities, so the findings may not apply to everyone. The researchers also point out that walking is linked to better mood, but it may not be the only reason for it.\n\nStill, the message is simple: a little exercise goes a long way.",
                                      ["İlgi çekici giriş", "Oranlar ve miktar ifadeleri", "Karşılaştırma ve temkinli yorum", "Sınırlılık", "Article doğruluğu"])},
)

u.test([
    mc("Genel olarak: \"___ is important for good health.\"", ["The sleep", "Sleep"], 1, "Sayılamaz, genel"),
    mc("Hangisi doğru?", ["the Mount Everest", "Mount Everest"], 1, "Tek dağ"),
    mc("\"Büyükbabam hastanede yatıyor.\" (hasta olarak)", ["My grandfather is in hospital.", "My grandfather is in the hospital building."], 0, "Kurum işlevi"),
    mc("\"Çok az kişi bunu biliyor.\" (olumsuz ton)", ["A few people know this.", "Few people know this."], 1, "few"),
    mc("Hangisi doğru?", ["Most of people", "Most people"], 1, "Genel → most"),
    gap("___ telephone was invented in 1876.", ["The"], "Buluş → the"),
    gap("She lives in ___ Netherlands.", ["the"], "Çoğul ülke"),
    gap("I have a ___ time now. I can help you. (biraz)", ["little"], "a little"),
    gap("There's a great ___ of evidence that exercise helps. (çok miktarda)", ["deal"], "a great deal of"),
    gap("___ of the two treatments worked. (ikisi de değil)", ["Neither"], "Neither of"),
    gap("___ participant was given a questionnaire. (her)", ["Every", "Each"], "every / each + tekil"),
    mc("Temkinli bilimsel dil:", ["Coffee prevents cancer.", "Coffee may be linked to a lower risk of some cancers."], 1, "Temkinli"),
    listen("The study involved 3,000 children. The majority of them spent more than three hours a day on screens. Those children were twice as likely to have problems sleeping. However, the researchers say more research is needed.", "Ekranda uzun süre geçiren çocuklar hakkında ne bulundu?", ["Daha iyi uyuyorlar", "Uyku sorunu yaşama olasılıkları iki kat fazla", "Daha mutlular"], 1, "\"twice as likely to have problems sleeping\""),
    typ("İngilizcesi: \"Katılımcıların hiçbiri çalışmayı bırakmadı.\" (none of, leave the study)", variants("None of the participants left the study.", "None of the participants left the study early."), "None of the participants left the study."),
    write("Bir okul gazetesi için önemli bir bilimsel keşfi ya da tıbbi gelişmeyi anlatan bir makale yazın (180–220 kelime): penisilinin keşfi, aşılar, DNA, uzay araştırmaları, vb. Genelleme article'larını, özel isimlerde the kullanımını, miktar ifadelerini (a few, little, plenty of, the majority of) ve both / neither / most of yapılarını doğru kullanın.",
          "Few discoveries have saved as many lives as penicillin, and it all happened by accident.\n\nIn 1928, Alexander Fleming, a Scottish scientist working at St Mary's Hospital in London, returned from a holiday and noticed something strange. A mould had grown on one of his dishes of bacteria, and the bacteria around it had died. Fleming realised that the mould was producing a substance that could kill bacteria. He called it penicillin.\n\nAt first, however, little attention was paid to his discovery. It was very difficult to produce penicillin in large amounts, and few scientists believed it would be useful. It wasn't until the 1940s that a team at the University of Oxford found a way to produce it on a larger scale.\n\nDuring the Second World War, penicillin saved a large number of soldiers' lives. Since then, antibiotics have become one of the most important tools in medicine. Most of the infections that once killed people can now be treated in a few days.\n\nBut there is a problem. Bacteria are becoming resistant to antibiotics, and neither doctors nor patients always use them carefully. Scientists warn that if we don't act, the majority of today's antibiotics may stop working.\n\nFleming himself warned about this in 1945. Perhaps it's time we listened.",
          ["Genelleme ve özel isimlerde article", "Miktar ifadeleri", "both / neither / most of", "Bilgi doğruluğu ve akış", "İlgi çekici giriş ve kapanış"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

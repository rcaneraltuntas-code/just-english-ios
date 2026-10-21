"""B2 Ünite 6: Seyahat yazıları."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("B2", 6, "Seyahat yazıları", "Travel Writing",
         "Bir yeri tanıtırken virgüllü (non-defining) ilgi cümleleriyle ek bilgi verebilir, which ile bütün bir cümleye yorum ekleyebilir, edatlı ve miktar bildiren ilgi yapılarını kullanabilir ve coğrafya ile kültür kelimeleriyle zengin bir gezi yazısı yazabilirim.",
         ["defining ve non-defining relative clauses", "cümleye yorum ekleyen which", "edat + which / whom", "some of which / most of whom", "betimleyici gezi yazısı dili"],
         ["coğrafya ve manzara", "kültür ve gelenekler", "seyahat deneyimleri"],
         {"title": "Gizli cennetler", "durationMinutes": 45,
          "goal": "Her öğrenci gittiği ya da gitmek istediği bir yeri, virgüllü ilgi cümleleriyle zenginleştirilmiş 2 dakikalık bir sunumla tanıtır (Mardin, which overlooks the Mesopotamian plain, ...). Dinleyenler sorular sorar. Sınıf sonunda bir \"seyahat rehberi\" için en ilgi çekici üç yeri seçer ve her biri için birlikte bir paragraf yazar."})

u.vocab([
    ("landscape", "manzara, peyzaj", "The landscape changes completely in winter.", "Manzara kışın tamamen değişiyor.", None),
    ("coastline", "kıyı şeridi", "Turkey has a very long coastline.", "Türkiye'nin çok uzun bir kıyı şeridi var.", None),
    ("valley", "vadi", "The village lies in a green valley.", "Köy yeşil bir vadide yer alıyor.", None),
    ("plain", "ova", "The city overlooks a vast plain.", "Şehir geniş bir ovaya bakıyor.", None),
    ("peak", "zirve", "The peak is covered in snow all year.", "Zirve bütün yıl karla kaplı.", None),
    ("overlook", "-e bakmak, tepeden görmek", "Our room overlooked the harbour.", "Odamız limana bakıyordu.", None),
    ("stunning", "nefes kesici", "The views were stunning.", "Manzara nefes kesiciydi.", None),
    ("breathtaking", "nefes kesen", "It was a breathtaking sunset.", "Nefes kesen bir gün batımıydı.", None),
    ("picturesque", "pitoresk, resim gibi", "It's a picturesque fishing village.", "Resim gibi bir balıkçı köyü.", None),
    ("remote", "ücra, uzak", "We stayed in a remote mountain hut.", "Ücra bir dağ kulübesinde kaldık.", None),
    ("off the beaten track", "turistik rotaların dışında", "I prefer places off the beaten track.", "Turistik rotaların dışındaki yerleri tercih ederim.", None),
    ("bustling", "hareketli, kaynayan", "We walked through the bustling market.", "Hareketli pazarda yürüdük.", None),
    ("ancient", "antik, çok eski", "The ancient city is 2,000 years old.", "Antik kent 2.000 yıllık.", None),
    ("heritage", "miras", "It's a UNESCO World Heritage Site.", "UNESCO Dünya Mirası Alanı.", None),
    ("custom", "gelenek, âdet", "It's a local custom to take off your shoes.", "Ayakkabı çıkarmak yerel bir âdet.", "customs = gümrük"),
    ("cuisine", "mutfak (yemek kültürü)", "The local cuisine is famous for its spices.", "Yerel mutfak baharatlarıyla ünlü.", None),
    ("hospitality", "misafirperverlik", "We were amazed by their hospitality.", "Misafirperverliklerine hayran kaldık.", None),
    ("local", "yerel; yerli halk", "Ask the locals for recommendations.", "Önerileri yerlilere sor.", None),
    ("souvenir", "hatıra eşyası", "I bought a carpet as a souvenir.", "Hatıra olarak bir halı aldım.", None),
    ("tourist trap", "turist tuzağı", "That restaurant is a tourist trap.", "O restoran bir turist tuzağı.", None),
    ("unspoilt", "bozulmamış, el değmemiş", "The beaches are still unspoilt.", "Plajlar hâlâ el değmemiş.", None),
    ("stroll", "gezinmek, yürüyüş", "We strolled along the seafront.", "Sahil boyunca yürüdük.", None),
    ("whom", "kime, kimi (resmî)", "The guide, whom we met in Kars, spoke six languages.", "Kars'ta tanıştığımız rehber altı dil konuşuyordu.", "who'nun nesne hali"),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Virgüllü ilgi cümleleri", "Defining ve non-defining ilgi cümlelerini ayırt edebilir ve virgülle ek bilgi verebilirim.",
    {"kind": "text", "title": "Mardin'e bir hafta sonu", "body": "Mardin, which sits on a hill above the Mesopotamian plain, is one of the most beautiful cities in Turkey.\n\nThe old town, where honey-coloured stone houses climb up the hillside, looks like something from another century. Our guide, Şeyma, who has lived here all her life, took us through narrow streets full of small workshops.\n\nThe hotel that we stayed in was a 200-year-old mansion. From our room, which had a tiny balcony, we could see the plain stretching all the way to Syria.\n\nIn the evening, we tried a local dish called kaburga dolması, which was absolutely delicious.",
     "questions": [
        mc("Where does Mardin sit?", ["By the sea", "On a hill above a plain", "In a forest"], 1, "\"which sits on a hill above the Mesopotamian plain\""),
        mc("Who is Şeyma?", ["The hotel owner", "The guide", "A chef"], 1, "\"Our guide, Şeyma, who has lived here all her life\""),
     ]},
    {"explanation": "B1'de **defining** (tanımlayıcı) ilgi cümlelerini öğrendiniz. **Non-defining** (tanımlayıcı olmayan) ilgi cümleleri, zaten belli olan bir kişi ya da şey hakkında **ek bilgi** verir.\n\n| Defining | Non-defining |\n|---|---|\n| **Hangisi** olduğunu söyler | **Ek bilgi** verir; çıkarılsa da anlam bozulmaz |\n| **Virgül yok** | **Virgül var** (yazıda), konuşmada duraklama |\n| who, which, **that** | who, which (**that olmaz**) |\n| Zamir atlanabilir (nesne ise) | Zamir **asla atlanmaz** |\n| The hotel **that we stayed in** was old. | Our hotel, **which was 200 years old**, ... |\n\n**Karşılaştırın:**\n\n- My brother **who lives in Paris** is a chef. (Birden fazla erkek kardeşim var; Paris'teki aşçı.)\n- My brother, **who lives in Paris**, is a chef. (Tek erkek kardeşim var; ek bilgi: Paris'te yaşıyor.)\n\n**Özel isimler** (Mardin, Şeyma, my mother) zaten belirli olduğu için genellikle **non-defining** alır:\n\n- **Mardin, which** sits on a hill, ...\n- **Şeyma, who** has lived here all her life, ...\n\n**whose** ve **where** de non-defining olarak kullanılabilir: The old town, **where** ..., / Ali, **whose** father ..., ...",
     "examples": [{"en": "Istanbul, which is divided by the Bosphorus, is on two continents.", "tr": "Boğaz'la ikiye ayrılan İstanbul iki kıtada yer alır."},
                  {"en": "My grandmother, who is 90, still swims every day.", "tr": "90 yaşındaki büyükannem hâlâ her gün yüzüyor."},
                  {"en": "We visited Ephesus, where we saw the Library of Celsus.", "tr": "Efes'i ziyaret ettik, orada Celsus Kütüphanesi'ni gördük."}],
     "turkishNote": "Türkçede \"90 yaşındaki büyükannem\" gibi ek bilgiler ismin önüne gelir ve virgül kullanılmaz. İngilizcede bu tür ek bilgiler non-defining relative clause ile ismin arkasına, virgüller arasında verilir. En sık hata, non-defining cümlelerde \"that\" kullanmaktır: \"Mardin, that is in the south-east\" yanlıştır; \"Mardin, which is in the south-east\" doğrudur."},
    [
        mc("Hangisi doğru?", ["Ankara, that is the capital, is in central Turkey.", "Ankara, which is the capital, is in central Turkey."], 1, "Non-defining → that olmaz."),
        mc("\"My sister, who lives in Bursa, is a nurse.\" Konuşanın kaç kız kardeşi var?", ["Bir", "Birden fazla"], 0, "Virgül → ek bilgi → tek kız kardeş."),
        mc("\"My sister who lives in Bursa is a nurse.\" Konuşanın kaç kız kardeşi var?", ["Bir", "Muhtemelen birden fazla"], 1, "Virgülsüz → tanımlayıcı."),
        mc("Non-defining cümlede ilgi zamiri atlanabilir mi?", ["Evet", "Hayır"], 1, "Asla atlanmaz."),
        gap("Our guide, ___ spoke five languages, was fantastic.", ["who"], "Kişi → who."),
        gap("Cappadocia, ___ is famous for its balloons, is in central Anatolia.", ["which"], "Yer (özne) → which."),
        gap("We stayed in Kaş, ___ we went diving every day.", ["where"], "Yer + özne + fiil → where."),
        gap("The chef, ___ restaurant had just opened, cooked for us.", ["whose"], "Sahiplik → whose."),
        listen("We spent three days in Lisbon, which is built on seven hills. Our host, who was a retired teacher, showed us the best places to eat.", "Ev sahibinin mesleği neydi?", ["Rehber", "Emekli öğretmen", "Aşçı"], 1, "\"Our host, who was a retired teacher\""),
        typ("Birleştirin (virgüllü): \"My grandmother is 90. She still swims every day.\"", variants("My grandmother, who is 90, still swims every day.", "My grandmother, who is ninety, still swims every day."), "My grandmother, who is 90, still swims every day."),
    ],
    {"kind": "speaking", "task": speak("Ailenizden 3 kişiyi ve şehrinizden 3 yeri non-defining relative clause ile tanıtın. Her cümlede ek bilgiyi virgüller arasında verin (konuşurken kısa duraklama yapın). who, which, where ve whose'u en az birer kez kullanın.",
                                       "My father, who is a retired engineer, loves gardening. My aunt, whose children live abroad, visits us every Sunday. My best friend, who I've known since primary school, is getting married next month. Konya, which is in central Anatolia, is famous for Mevlana. The Mevlana Museum, which attracts millions of visitors, is beautiful. Our old neighbourhood, where I grew up, has changed a lot.",
                                       ["Non-defining doğru (that yok)", "who / which / where / whose", "Duraklama ve ek bilgi"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "Ki bu da...", "which ile bütün bir cümleye yorum ekleyebilir ve anlatımımı daha akıcı hale getirebilirim.",
    {"kind": "dialogue", "title": "Tatil dönüşü", "lines": [
        {"speaker": "Ozan", "text": "How was Georgia?"},
        {"speaker": "Bahar", "text": "Wonderful! It didn't rain once, which was lucky because we were hiking every day."},
        {"speaker": "Ozan", "text": "Did you go to Tbilisi?"},
        {"speaker": "Bahar", "text": "Yes, but our flight was delayed by five hours, which meant we missed our first night in the hotel."},
        {"speaker": "Ozan", "text": "Oh no!"},
        {"speaker": "Bahar", "text": "It was fine. The locals were incredibly friendly and kept inviting us for dinner, which made the trip really special."}],
     "questions": [
        mc("Why was it lucky that it didn't rain?", ["They were swimming.", "They were hiking every day.", "They didn't have umbrellas."], 1, "\"which was lucky because we were hiking every day\""),
        mc("What made the trip special?", ["The hotel", "The locals inviting them for dinner", "The weather"], 1, "\"The locals... kept inviting us for dinner, which made the trip really special.\""),
     ]},
    {"explanation": "**which** bütün bir **cümleye** (sadece bir isme değil) **yorum** ekleyebilir. Önünde **her zaman virgül** olur.\n\n| Cümle | Yorum (which = bu durum) |\n|---|---|\n| It didn't rain once, | **which** was lucky. |\n| Our flight was delayed, | **which** meant we missed the first night. |\n| They kept inviting us for dinner, | **which** made the trip special. |\n\nBu yapıda **which = and this / and that**:\n\n- It didn't rain, **which** was lucky. = It didn't rain, **and this** was lucky.\n\n**Dikkat:**\n\n- Bu kullanımda **what** ya da **that** kullanılmaz: ~~It didn't rain, what was lucky.~~\n- **which** ile başlayan yeni bir cümle yazıda kullanılmaz: ~~It didn't rain. Which was lucky.~~ (Konuşmada duyulabilir.)\n\n**Sık kullanılan yorumlar:**\n\n- ..., **which was a relief / a shame / a surprise**.\n- ..., **which meant (that)** ...\n- ..., **which is why** ...\n- ..., **which made me** + sıfat / fiil",
     "examples": [{"en": "The museum was closed, which was a real shame.", "tr": "Müze kapalıydı, bu gerçekten yazık oldu."},
                  {"en": "He spoke perfect Turkish, which surprised everyone.", "tr": "Mükemmel Türkçe konuşuyordu, bu herkesi şaşırttı."},
                  {"en": "The hotel was full, which is why we stayed in a guesthouse.", "tr": "Otel doluydu, bu yüzden bir pansiyonda kaldık."}],
     "turkishNote": "Türkçede \"... ki bu da ...\" ya da \"... bu da ... oldu\" yapıları, İngilizcedeki cümleye yorum ekleyen which'e denk gelir. Türkçe konuşanlar bu durumda sık sık \"what\" kullanır: \"It rained, what was terrible\" yanlıştır; doğrusu \"It rained, which was terrible\"."},
    [
        mc("Hangisi doğru?", ["It rained all week, what was terrible.", "It rained all week, which was terrible."], 1, "Cümleye yorum → which."),
        mc("\"which\" burada neye bağlı? \"We missed the bus, which made us late.\"", ["the bus", "Otobüsü kaçırmamız (bütün cümle)"], 1, "Bütün cümleye yorum."),
        mc("Doğru noktalama:", ["The shop was closed which was annoying.", "The shop was closed, which was annoying."], 1, "Virgül gerekli."),
        gap("Our guide got lost, ___ was quite funny.", ["which"], "Cümleye yorum → which."),
        gap("The flight was cancelled, which ___ we had to stay another night. (anlamına geldi)", ["meant"], "which meant."),
        gap("It was a holiday, which is ___ all the shops were closed. (bu yüzden)", ["why"], "which is why."),
        gap("They gave us free breakfast, which was a nice ___. (sürpriz)", ["surprise"], "which was a nice surprise."),
        order(["missed", "We", "the", "ferry", "which", "meant", "we", "had", "to", "wait", "three", "hours"], "We missed the ferry which meant we had to wait three hours.", "Cümle + which meant + cümle.", "Feribotu kaçırdık, bu da üç saat beklememiz gerektiği anlamına geliyordu."),
        listen("The hotel upgraded us to a suite with a sea view, which was amazing. But the restaurant closed at eight, which meant we had to eat in town every night.", "Restoranın erken kapanması ne anlama geliyordu?", ["Akşam yemeği yiyemediler", "Her akşam şehirde yemek zorunda kaldılar", "Oda servisi kullandılar"], 1, "\"which meant we had to eat in town every night\""),
        typ("Birleştirin (which ile): \"The museum was closed. That was a real shame.\"", variants("The museum was closed, which was a real shame.", "The museum was closed, which was a shame."), "The museum was closed, which was a real shame."),
    ],
    {"kind": "speaking", "task": speak("Son seyahatinizi anlatın ve en az 5 olayı which ile yorumlayın: which was lucky / a shame / a relief / a surprise, which meant ..., which is why ..., which made me ...",
                                       "Last summer I went to Antalya with my family. We arrived at midnight, which meant we were all exhausted. The hotel gave us a bigger room, which was a nice surprise. It was 40 degrees every day, which is why we spent most of the time in the sea. My brother lost his phone on the beach, which was a disaster. But a stranger found it, which restored my faith in people!",
                                       ["Cümleye yorum ekleyen which", "Virgül / duraklama", "Çeşitli yorum kalıpları"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "Edatlı ve miktarlı ilgi cümleleri", "Edat + which / whom ve some of which / most of whom gibi yapılarla daha resmî ve ayrıntılı tanımlar yapabilirim.",
    {"kind": "text", "title": "Rehber kitaptan: Van Gölü", "body": "Lake Van, which is the largest lake in Turkey, lies in the far east of the country at an altitude of about 1,650 metres.\n\nThe lake, the water of which is extremely salty and alkaline, has very few fish species. The best known is the inci kefali, which swims from the lake up into the rivers each spring to lay its eggs.\n\nThe region has many historical sites, most of which date back to the Urartian period. On Akdamar Island, to which boats run regularly in summer, you can visit a beautiful tenth-century Armenian church.\n\nThe local people, many of whom speak several languages, are known for their warm hospitality. Don't leave without trying a Van breakfast, for which the city is famous.",
     "questions": [
        mc("What is special about Lake Van's water?", ["It's very cold.", "It's extremely salty and alkaline.", "It's fresh drinking water."], 1, "\"extremely salty and alkaline\""),
        mc("What is the city of Van famous for?", ["Its fish market", "Its breakfast", "Its carpets"], 1, "\"a Van breakfast, for which the city is famous\""),
     ]},
    {"explanation": "**1. Edat + which / whom** (daha resmî)\n\nGünlük dilde edat cümlenin **sonunda** kalır; resmî yazıda **which / whom'dan önce** gelir.\n\n| Günlük | Resmî |\n|---|---|\n| The island **(which) boats run to** ... | The island, **to which** boats run, ... |\n| The city **(that) it's famous for** ... | ... **for which** the city is famous |\n| The man **(who) I spoke to** ... | The man **to whom** I spoke ... |\n\n**Dikkat:** Edattan sonra **who** ve **that** kullanılmaz: ~~to who~~ / ~~to that~~ → **to whom** / **to which**\n\n**2. Miktar + of which / of whom**\n\n| Yapı | Örnek |\n|---|---|\n| **some of which** | There are many sites, **some of which** are 3,000 years old. |\n| **most of whom** | The locals, **most of whom** speak Kurdish and Turkish, ... |\n| **all of which** | We visited five museums, **all of which** were free. |\n| **none of whom** | I met ten people, **none of whom** spoke English. |\n| **both of which** | It has two beaches, **both of which** are unspoilt. |\n| **the water of which** / **whose water** | The lake, **whose water** is salty, ... |\n\nİnsanlar için **whom**, şeyler için **which** kullanılır.",
     "examples": [{"en": "The village, to which there is only one road, is very peaceful.", "tr": "Tek bir yolla ulaşılan köy çok huzurlu."},
                  {"en": "We met many travellers, most of whom were from Europe.", "tr": "Pek çok gezginle tanıştık, çoğu Avrupalıydı."},
                  {"en": "The region has three national parks, all of which are worth visiting.", "tr": "Bölgede üç milli park var ve hepsi görülmeye değer."}],
     "turkishNote": "\"... hepsi görülmeye değer\", \"... çoğu Avrupalıydı\" gibi Türkçe yapılar İngilizcede \"all of which\", \"most of whom\" ile kurulur. Türkçe konuşanlar genellikle bunu iki ayrı cümle olarak söyler (\"...three parks. All of them are...\"). Bu da doğrudur, ama of which / of whom yapısı yazıda daha akıcı ve ileri bir seviye gösterir. \"most of them\" ile \"most of whom\" karıştırılmamalıdır: virgülden sonra tek cümlede \"whom\" gerekir."},
    [
        mc("Resmî: \"The man ___ I spoke was very helpful.\"", ["to who", "to whom", "to that"], 1, "Edat + whom."),
        mc("Hangisi doğru?", ["I met ten tourists, most of them were German.", "I met ten tourists, most of whom were German."], 1, "Tek cümle → most of whom."),
        mc("Şeyler için:", ["some of whom", "some of which"], 1, "Şey → which."),
        gap("We visited three castles, all of ___ were built in the 12th century.", ["which"], "all of which."),
        gap("The students, most of ___ were from Asia, loved the tour.", ["whom"], "most of whom."),
        gap("The hotel, ___ which we had paid a lot, was disappointing. (için)", ["for"], "for which."),
        gap("The house in ___ the poet was born is now a museum.", ["which"], "in which."),
        gap("It has two beaches, ___ of which are unspoilt. (ikisi de)", ["both"], "both of which."),
        listen("Our group had twelve people, none of whom had been to Iran before. The guide, to whom we owe a lot, showed us places that tourists rarely see.", "Gruptakilerden kaç kişi daha önce İran'a gitmişti?", ["Hiçbiri", "Yarısı", "Hepsi"], 0, "\"none of whom had been to Iran before\""),
        typ("Birleştirin: \"The region has five lakes. Most of them are very deep.\" (most of which)", variants("The region has five lakes, most of which are very deep."), "The region has five lakes, most of which are very deep."),
    ],
    {"kind": "speaking", "task": speak("Bir şehri ya da bölgeyi rehber kitap üslubuyla tanıtın. En az 2 edat + which / whom (to which, for which, in which) ve en az 3 miktar + of which / of whom (some of which, most of whom, all of which, none of which) kullanın.",
                                       "Kars, which is in north-eastern Turkey, is famous for its cheese and honey, for which people travel from all over the country. The city has many Russian-style buildings, most of which were built in the 19th century. Nearby is Ani, to which tourists come to see the ancient ruins. The region has several lakes, some of which freeze completely in winter. The locals, most of whom are farmers, are very welcoming.",
                                       ["Edat + which / whom", "Miktar + of which / whom", "Resmî rehber üslubu"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Manzarayı anlatmak", "Coğrafya, manzara ve kültür kelimeleriyle bir yeri canlı ve özgün bir şekilde betimleyebilirim.",
    {"kind": "dialogue", "title": "Gezi vlogu çekimi", "lines": [
        {"speaker": "Vlogger", "text": "Good morning from Pamukkale! Behind me you can see the famous white terraces, which look like snow but are actually made of limestone."},
        {"speaker": "Vlogger", "text": "The view from up here is breathtaking. You can see the whole valley stretching out below us."},
        {"speaker": "Friend", "text": "And it's still early, so it's not crowded yet. By noon this place will be bustling with tourists."},
        {"speaker": "Vlogger", "text": "Right. Tip number one: come at sunrise. Tip number two: you have to take your shoes off on the terraces to protect them."},
        {"speaker": "Friend", "text": "And don't miss Hierapolis, the ancient city right next to it."},
        {"speaker": "Vlogger", "text": "Absolutely. It's one of the most stunning places I've ever been to."}],
     "questions": [
        mc("What are the white terraces made of?", ["Snow", "Limestone", "Salt"], 1, "\"actually made of limestone\""),
        mc("Why should you take your shoes off?", ["Because it's hot", "To protect the terraces", "Because it's a custom in mosques"], 1, "\"to protect them\""),
     ]},
    {"explanation": "**Bir yeri betimlerken kullanılan dil:**\n\n| Konum | Örnek |\n|---|---|\n| **lie / be situated / be located** | The village **lies** in a green valley. |\n| **overlook** | The castle **overlooks** the sea. |\n| **stretch** | The beach **stretches** for 10 km. |\n| **surround** | It's **surrounded by** mountains. |\n| **be home to** | The park **is home to** rare birds. |\n\n**Güçlü betimleme sıfatları:**\n\n| Doğa | Şehir / kültür |\n|---|---|\n| breathtaking, stunning | bustling, lively, vibrant |\n| unspoilt, remote | picturesque, charming |\n| rugged (engebeli), lush (yemyeşil) | ancient, historic |\n\n**\"Klişe\"den kaçının:** \"beautiful\" ve \"nice\" yerine daha özgün kelimeler seçin.\n\n- ~~The beach was nice.~~ → The beach **stretched for miles**, and the sand was **as white as flour**.\n\n**Duyuları kullanın:** Ne gördünüz, ne duydunuz, ne kokladınız, ne tattınız?\n\n- The air **smelled of** jasmine. / You can **hear** the call to prayer echoing across the valley.\n\n**Tavsiye dili:** **Don't miss** ... / **It's well worth** + -ing / **Avoid** ... / **The best time to visit is** ...",
     "examples": [{"en": "The village lies at the foot of a rugged mountain.", "tr": "Köy engebeli bir dağın eteğinde yer alıyor."},
                  {"en": "The town is surrounded by lush green forests.", "tr": "Kasaba yemyeşil ormanlarla çevrili."},
                  {"en": "It's well worth getting up early to see the sunrise.", "tr": "Gün doğumunu görmek için erken kalkmaya kesinlikle değer."}],
     "turkishNote": "Türkçe gezi yazılarında \"muhteşem\", \"harika\" gibi sıfatlar sık tekrarlanır. İngilizce gezi yazısında okuyucu somut ayrıntı ve özgün betimleme bekler: \"It was amazing\" yerine ne gördüğünüzü, duyduğunuzu ve hissettiğinizi anlatın. \"customs\" kelimesine de dikkat: tekil \"custom\" gelenek, çoğul \"customs\" çoğunlukla gümrük anlamındadır."},
    [
        mc("\"Köy bir vadide yer alıyor.\"", ["The village lies in a valley.", "The village lays in a valley."], 0, "lie (yer almak)."),
        mc("Kalabalık ve hareketli bir pazar:", ["a remote market", "a bustling market"], 1, "bustling."),
        mc("Hiç bozulmamış plaj:", ["unspoilt", "spoilt"], 0, "unspoilt."),
        mc("\"customs\" havalimanında:", ["gelenekler", "gümrük"], 1, "customs = gümrük."),
        gap("The hotel ___ the harbour. (bakıyor)", ["overlooks"], "overlook."),
        gap("The town is surrounded ___ olive groves.", ["by"], "surrounded by."),
        gap("The national park is ___ to more than 200 species of birds.", ["home"], "be home to."),
        gap("It's well worth ___ (visit) the old bazaar.", ["visiting"], "worth + -ing."),
        match([("breathtaking", "nefes kesici"), ("remote", "ücra"), ("lush", "yemyeşil"), ("rugged", "engebeli"), ("picturesque", "resim gibi")], "Eşleştirin."),
        listen("The best time to visit Cappadocia is spring or autumn. In summer it gets very hot, and in winter the roads can be icy. But if you go in January, you might see the fairy chimneys covered in snow, which is stunning.", "Kapadokya'yı ziyaret için en iyi zaman ne?", ["Yaz", "İlkbahar ya da sonbahar", "Sadece kış"], 1, "\"The best time to visit Cappadocia is spring or autumn.\""),
    ],
    {"kind": "speaking", "task": speak("Bir vlogger gibi en sevdiğiniz doğal ya da tarihi bir yeri \"canlı\" olarak tanıtın. Konum fiillerini (lie, overlook, stretch, surround), en az 4 güçlü sıfatı ve duyularla ilgili ayrıntıları kullanın. Sonunda izleyicilere 2 tavsiye verin.",
                                       "Hi everyone, I'm in Uzungöl, which lies in a lush green valley in the mountains above Trabzon. The lake is surrounded by pine forests, and the air smells of wood and rain. Behind me, wooden houses climb up the rugged hillside. It's breathtaking in the early morning, when the mist covers the water. My tips: avoid weekends in August, when it's crowded, and don't miss the local trout!",
                                       ["Konum fiilleri", "Güçlü betimleme sıfatları", "Duyusal ayrıntılar", "Tavsiye dili"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Gezi yazısı", "İlgi cümleleri, betimleyici dil ve kişisel deneyimlerle zenginleştirilmiş, yayınlanabilir kalitede bir gezi yazısı yazabilirim.",
    {"kind": "text", "title": "Örnek gezi yazısı: Kaçkarlar'da bir yayla", "body": "At 2,000 metres, the clouds sit below you.\n\nThat was my first thought as I stepped out of the minibus in Pokut, a tiny highland village in the Kaçkar Mountains, which I had dreamed of visiting for years.\n\nThe village, which is only open from June to September, consists of about thirty wooden houses, most of which belong to families from the valleys below. There are no shops and almost no phone signal, which, I quickly realised, was exactly the point.\n\nOur host, Fadime Teyze, whose family has spent every summer here for four generations, welcomed us with fresh bread, butter and a cheese called minci. In the evening, we sat on her wooden balcony and watched the sun sink into a sea of clouds.\n\nIf you go, bring warm clothes, even in August. And leave your laptop at home. You won't need it.",
     "questions": [
        mc("When is the village open?", ["All year", "From June to September", "Only in winter"], 1, "\"only open from June to September\""),
        mc("What does the writer suggest leaving at home?", ["Warm clothes", "Your laptop", "Your camera"], 1, "\"leave your laptop at home\""),
     ]},
    {"explanation": "**İyi bir gezi yazısının özellikleri:**\n\n| Bölüm | İpucu | Örnek |\n|---|---|---|\n| **Çarpıcı giriş** | Bir görüntü, bir an ya da bir cümleyle başlayın. | *At 2,000 metres, the clouds sit below you.* |\n| **Konum ve bağlam** | Yeri kısa ve somut tanıtın. | *Pokut, a tiny highland village in the Kaçkar Mountains, ...* |\n| **Ayrıntılı betimleme** | Non-defining clauses ile ek bilgi ekleyin. | *The village, which is only open in summer, ...* |\n| **İnsanlar ve kültür** | Yerel bir kişi, yemek ya da gelenek. | *Our host, whose family has ...* |\n| **Kişisel yorum** | which ile duygu / yorum ekleyin. | *..., which was exactly the point.* |\n| **Pratik tavsiye ve kapanış** | Kısa ve akılda kalıcı. | *Leave your laptop at home. You won't need it.* |\n\n**Üslup ipuçları:**\n\n- **Cümle uzunluğunu değiştirin**: uzun betimleyici cümlelerin arkasından kısa vurucu cümleler.\n- **Apposition** (açıklayıcı isim grubu) kullanın: *Pokut, **a tiny highland village**, ...* (which is'siz kısa non-defining)\n- **Şimdiki zaman** yerin genel özelliklerini, **geçmiş zaman** sizin deneyiminizi anlatır.\n- Klişelerden kaçının: *hidden gem, paradise on earth* gibi ifadeleri az kullanın.",
     "examples": [{"en": "Göreme, a small town in the heart of Cappadocia, is surrounded by fairy chimneys.", "tr": "Kapadokya'nın kalbindeki küçük bir kasaba olan Göreme peri bacalarıyla çevrili."},
                  {"en": "There was no Wi-Fi, which, to my surprise, I didn't miss at all.", "tr": "Wi-Fi yoktu ve şaşırtıcı bir şekilde hiç aramadım."},
                  {"en": "Bring comfortable shoes. You'll be walking a lot.", "tr": "Rahat ayakkabı getirin. Çok yürüyeceksiniz."}],
     "turkishNote": "Türkçe gezi yazılarında bilgi ve kişisel deneyim genellikle ayrı paragraflarda verilir. İngilizce gezi yazısında (travel writing) ikisi iç içedir: Yazar okuyucuyu kendi gözünden geziye çıkarır. Non-defining relative clauses ve apposition, bilgiyi cümlenin akışını bozmadan eklemenin en etkili yoludur."},
    [
        mc("Etkili bir gezi yazısı girişi:", ["Today I will tell you about my holiday.", "The first thing you notice in Mardin is the silence."], 1, "Çarpıcı bir görüntü ya da an."),
        mc("Apposition örneği:", ["Pokut, a tiny village in the mountains, is ...", "Pokut is a tiny village. It is in the mountains."], 0, "İsim + açıklayıcı isim grubu."),
        mc("Yerin genel özelliği için genellikle hangi zaman?", ["Present simple", "Past simple"], 0, "Genel bilgi → present."),
        mc("Kaçınılması gereken klişe:", ["paradise on earth", "the village lies in a valley"], 0, "Klişe."),
        gap("Our host, ___ family had lived there for generations, made us breakfast.", ["whose"], "whose."),
        gap("The village has thirty houses, most of ___ are made of wood.", ["which"], "most of which."),
        gap("There was no signal, ___ was actually a relief.", ["which"], "Cümleye yorum."),
        gap("Göreme, a small town ___ the heart of Cappadocia, is very popular.", ["in"], "in the heart of."),
        listen("I arrived in Fes, one of the oldest cities in Morocco, late at night. The medina, which has more than 9,000 narrow streets, felt like a maze. I got lost twice, which turned out to be the best way to discover it.", "Konuşan kaybolmanın nasıl olduğunu söylüyor?", ["Korkutucuydu", "Şehri keşfetmenin en iyi yoluydu", "Zaman kaybıydı"], 1, "\"which turned out to be the best way to discover it\""),
        typ("Apposition ile birleştirin: \"Ayvalık is a charming town on the Aegean coast. It is famous for its olive oil.\"", variants("Ayvalık, a charming town on the Aegean coast, is famous for its olive oil.", "Ayvalık, a charming town on the Aegean coast, is famous for olive oil."), "Ayvalık, a charming town on the Aegean coast, is famous for its olive oil."),
    ],
    {"kind": "writing", "task": write("Bir seyahat dergisi için gittiğiniz (ya da çok iyi bildiğiniz) bir yer hakkında gezi yazısı yazın (200–250 kelime). Çarpıcı bir girişle başlayın; en az 4 non-defining relative clause, bir cümleye yorum ekleyen which, bir miktar + of which / whom ve bir apposition kullanın. Yerel insanlar ve kültürden söz edin ve pratik bir tavsiyeyle bitirin.",
                                      "The ferry horn sounds twice, and suddenly the noise of Istanbul disappears behind you.\n\nBüyükada, the largest of the Princes' Islands, is only ninety minutes from the city centre, but it feels like another century. There are no private cars on the island, which means the only sounds are seagulls, bicycle bells and the quiet hum of electric buggies.\n\nI spent a long weekend in a small guesthouse near the harbour. The owner, Rebeka Hanım, whose grandparents built the house in 1910, served breakfast in a garden full of roses and fig trees. She told me stories about the island's past, much of which I had never heard before.\n\nThe island is famous for its grand wooden mansions, many of which were built by wealthy families in the late nineteenth century. Some are beautifully restored; others are slowly falling apart, which gives the streets a strange, romantic sadness.\n\nThe best way to explore is on foot or by bicycle. Climb up to the Aya Yorgi Monastery, which sits on the island's highest hill, and you'll be rewarded with a breathtaking view of the Sea of Marmara.\n\nA final tip: avoid summer weekends, when the ferries are packed. Go on a weekday in May or October, and you might feel as if you have the whole island to yourself.",
                                      ["Çarpıcı giriş", "Non-defining clauses (en az 4)", "which ile yorum, of which / whom, apposition", "Betimleyici dil ve kültür", "Pratik tavsiye ve güçlü kapanış"])},
)

u.test([
    mc("Hangisi doğru?", ["Paris, that is the capital of France, is beautiful.", "Paris, which is the capital of France, is beautiful."], 1, "that olmaz"),
    mc("\"My brother, who is a doctor, lives in Ankara.\" Kaç erkek kardeş?", ["Bir", "Birden fazla"], 0, "Virgül → ek bilgi"),
    mc("Hangisi doğru?", ["It rained all day, what ruined our plans.", "It rained all day, which ruined our plans."], 1, "which"),
    mc("Resmî: \"The person ___ I spoke was very kind.\"", ["to who", "to whom"], 1, "to whom"),
    mc("Hangisi doğru?", ["We met many locals, most of them spoke English.", "We met many locals, most of whom spoke English."], 1, "most of whom"),
    gap("Our guide, ___ name was Aras, knew everything about the city.", ["whose"], "whose"),
    gap("We went to Kaş, ___ we went diving.", ["where"], "where"),
    gap("The flight was delayed, which ___ we missed the tour. (anlamına geliyordu)", ["meant"], "which meant"),
    gap("The region has four lakes, all of ___ are worth visiting.", ["which"], "all of which"),
    gap("The village is surrounded ___ mountains.", ["by"], "surrounded by"),
    mc("Kalabalık ve hareketli:", ["remote", "bustling"], 1, "bustling"),
    gap("The castle ___ the town. (tepeden bakıyor)", ["overlooks"], "overlook"),
    listen("We stayed in Şirince, a small village near Selçuk, which is famous for its fruit wines. Our host, whose house was more than 150 years old, cooked for us every evening, which made us feel like part of the family.", "Ev sahibinin her akşam yemek yapması onlara ne hissettirdi?", ["Turist gibi", "Ailenin bir parçası gibi", "Yabancı gibi"], 1, "\"which made us feel like part of the family\""),
    typ("Birleştirin (virgüllü): \"Antalya is on the Mediterranean coast. It attracts millions of tourists every year.\"", variants("Antalya, which is on the Mediterranean coast, attracts millions of tourists every year.", "Antalya, which attracts millions of tourists every year, is on the Mediterranean coast."), "Antalya, which is on the Mediterranean coast, attracts millions of tourists every year."),
    write("Türkiye'de turistlerin pek bilmediği bir yeri tanıtan bir gezi yazısı yazın (200–250 kelime). Non-defining relative clauses, cümleye yorum ekleyen which, miktar + of which / whom, apposition, konum fiilleri ve güçlü betimleme sıfatları kullanın. Kişisel bir deneyim ve pratik bir tavsiye ekleyin.",
          "Most people who visit the Black Sea go straight to Trabzon or Uzungöl. Very few take the narrow road east to Şavşat, a small town in the province of Artvin, which is a shame, because it's one of the most breathtaking corners of Turkey.\n\nŞavşat lies in a lush valley surrounded by dense forests of pine and spruce. Just above the town is Karagöl, a dark mountain lake which reflects the trees so perfectly that it looks like a mirror. In autumn, when the leaves turn orange and red, the landscape is truly stunning.\n\nI stayed in a wooden guesthouse run by a family, most of whom had never left the region. The grandmother, who was in her eighties, made fresh corn bread every morning and told me stories about the winters, some of which lasted six months.\n\nThe local cuisine is simple but delicious. Try the honey, much of which comes from tiny hives hidden in the forest, and the famous Şavşat cheese.\n\nThere's not much nightlife, and the phone signal is weak, which, after a busy year in Istanbul, was exactly what I needed.\n\nIf you go, rent a car, because public transport is limited. The best time to visit is late September or early October, when the forests are at their most colourful and the summer crowds have gone.",
          ["Non-defining clauses", "which ile yorum ve of which / whom", "Apposition ve konum fiilleri", "Güçlü betimleme ve kültür", "Kişisel deneyim ve tavsiye"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

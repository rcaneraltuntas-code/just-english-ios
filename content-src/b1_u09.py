"""B1 Ünite 9: Çocukluk."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("B1", 9, "Çocukluk", "Childhood",
         "Geçmişteki alışkanlıkları ve durumları used to ve would ile anlatabilir, geçmiş ile bugün arasındaki farkları any more / no longer / still ile karşılaştırabilir ve çocukluk anılarımı canlı bir şekilde paylaşabilirim.",
         ["used to (olumlu)", "didn't use to / Did you use to ...?", "would (geçmişteki tekrarlanan eylemler)", "used to, would ve past simple farkı", "any more / no longer / still"],
         ["çocukluk ve anılar", "oyunlar ve oyuncaklar", "aile ve yetiştirilme"],
         {"title": "Biz çocukken...", "durationMinutes": 45,
          "goal": "Öğrenciler çocukluk fotoğraflarını (ya da bir çocukluk eşyasını) getirir. Küçük gruplarda birbirlerine Did you use to...? soruları sorar, cevaplarında used to ve would kullanırlar. Sonra grup, \"Bizim çocukluğumuz ve bugünün çocukları\" karşılaştırmasını any more / no longer / still ile sınıfa sunar."})

u.vocab([
    ("childhood", "çocukluk", "I had a happy childhood.", "Mutlu bir çocukluğum oldu.", None),
    ("memory", "anı; hafıza", "My earliest memory is of my grandmother's garden.", "En eski anım büyükannemin bahçesi.", None),
    ("grow up", "büyümek", "I grew up in a small town.", "Küçük bir kasabada büyüdüm.", "grow → grew → grown"),
    ("bring up", "yetiştirmek, büyütmek", "My grandparents brought me up.", "Beni büyükannemle büyükbabam büyüttü.", "bring → brought"),
    ("toy", "oyuncak", "My favourite toy was a red car.", "En sevdiğim oyuncak kırmızı bir arabaydı.", None),
    ("hide and seek", "saklambaç", "We used to play hide and seek in the garden.", "Bahçede saklambaç oynardık.", None),
    ("marbles", "misket", "The boys would play marbles for hours.", "Oğlanlar saatlerce misket oynardı.", None),
    ("skipping rope", "atlama ipi", "She used to be the best at skipping rope.", "İp atlamada en iyisi oydu.", None),
    ("cartoon", "çizgi film", "I used to watch cartoons every Saturday morning.", "Her cumartesi sabahı çizgi film izlerdim.", None),
    ("pocket money", "harçlık", "How much pocket money did you get?", "Ne kadar harçlık alırdın?", None),
    ("naughty", "yaramaz", "I was a very naughty child.", "Çok yaramaz bir çocuktum.", None),
    ("strict", "katı, sıkı", "My father was quite strict.", "Babam oldukça katıydı.", None),
    ("spoil", "şımartmak", "My grandmother used to spoil us.", "Büyükannem bizi şımartırdı.", "spoilt (şımarık)"),
    ("tease", "takılmak, alay etmek", "My brother used to tease me all the time.", "Abim bana sürekli takılırdı.", None),
    ("punish", "cezalandırmak", "Were you ever punished at school?", "Okulda hiç ceza aldın mı?", "punishment (ceza)"),
    ("primary school", "ilkokul", "I walked to primary school every day.", "Her gün ilkokula yürürdüm.", None),
    ("used to", "-ardı, -erdi (eskiden)", "I used to live in Sivas.", "Eskiden Sivas'ta yaşardım.", "used to + yalın fiil"),
    ("would", "-ardı (tekrarlanan eylem)", "Every summer we would go to the village.", "Her yaz köye giderdik.", None),
    ("any more", "artık (olumsuz)", "I don't play football any more.", "Artık futbol oynamıyorum.", "Cümle sonunda; anymore de yazılır."),
    ("no longer", "artık ... değil", "The shop no longer exists.", "Dükkân artık yok.", "Daha resmî."),
    ("still", "hâlâ", "I still remember her name.", "Adını hâlâ hatırlıyorum.", None),
    ("nostalgic", "nostaljik", "Old songs make me feel nostalgic.", "Eski şarkılar beni nostaljik yapıyor.", None),
    ("in those days", "o zamanlar", "In those days, there was no internet.", "O zamanlar internet yoktu.", None),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Eskiden...", "Geçmişte düzenli yaptığım ama artık yapmadığım şeyleri ve eski durumları used to ile anlatabilirim.",
    {"kind": "dialogue", "title": "Eski fotoğraflar", "lines": [
        {"speaker": "Ceren", "text": "Is this you? You look so different!"},
        {"speaker": "Okan", "text": "Yes, that's me at eight. I used to have really long hair."},
        {"speaker": "Ceren", "text": "And glasses! I didn't know you wore glasses."},
        {"speaker": "Okan", "text": "I used to, but I had laser surgery a few years ago."},
        {"speaker": "Ceren", "text": "Where's this? It looks like a village."},
        {"speaker": "Okan", "text": "It's my grandparents' house near Amasya. We used to spend every summer there."}],
     "questions": [
        mc("What did Okan use to have?", ["Short hair", "Long hair", "A beard"], 1, "\"I used to have really long hair.\""),
        mc("Where did Okan use to spend his summers?", ["At the beach", "At his grandparents' house near Amasya", "In Istanbul"], 1, "\"We used to spend every summer there.\""),
     ]},
    {"explanation": "**used to + yalın fiil**, geçmişte **düzenli olarak yapılan** ya da **süren** ama **artık devam etmeyen** şeyleri anlatır.\n\n| Tür | Örnek |\n|---|---|\n| Alışkanlık | I **used to play** football every day. (Artık oynamıyorum.) |\n| Durum | I **used to have** long hair. (Artık uzun değil.) |\n| Durum | We **used to live** in Amasya. |\n\n**Yapı:** Tüm kişilerde aynı → I / you / he / she / we / they **used to** + fiil\n\n**Dikkat:**\n\n- used to'dan sonra **yalın fiil**: I used to **play** (~~played~~ / ~~playing~~)\n- used to **sadece geçmiş** içindir. Şimdiki alışkanlık için present simple: I **usually** play tennis. (~~I use to play~~)\n- Tek seferlik olaylar için kullanılmaz: ~~I used to go to Paris in 2015.~~ → I **went** to Paris in 2015.\n\n**Telaffuz:** used to → /ˈjuːstə/ (\"yustı\")",
     "examples": [{"en": "My mother used to make bread every Friday.", "tr": "Annem her cuma ekmek yapardı."},
                  {"en": "There used to be a cinema on this street.", "tr": "Eskiden bu sokakta bir sinema vardı."},
                  {"en": "I used to be very shy.", "tr": "Eskiden çok utangaçtım."}],
     "turkishNote": "Türkçede \"eskiden giderdik\", \"eskiden utangaçtım\" derken geniş zamanın hikâyesi (-ardı) ya da \"eskiden\" kelimesi kullanılır. İngilizcede bunun en doğal karşılığı used to'dur. \"There used to be\" (eskiden ... vardı) kalıbı da çok kullanışlıdır: There used to be a park here."},
    [
        mc("Hangisi doğru?", ["I used to played football.", "I used to play football."], 1, "used to + yalın fiil."),
        mc("Tek seferlik olay:", ["I used to visit Rome in 2018.", "I visited Rome in 2018."], 1, "Tek olay → past simple."),
        mc("Şimdiki alışkanlık:", ["I use to drink tea every morning.", "I usually drink tea every morning."], 1, "used to sadece geçmiş."),
        gap("We ___ to live in Sivas, but now we live in Ankara.", ["used"], "used to."),
        gap("She used to ___ (be) very shy.", ["be"], "used to + be."),
        gap("There ___ to be a bakery here. (eskiden vardı)", ["used"], "There used to be."),
        gap("My dad used to ___ (work) in a factory.", ["work"], "Yalın fiil."),
        order(["used", "I", "to", "have", "long", "hair"], "I used to have long hair.", "Özne + used to + fiil.", "Eskiden uzun saçlarım vardı."),
        listen("When I was a child, I used to walk to school with my best friend. It took about half an hour, and we used to buy simit on the way.", "Yolda ne alırlardı?", ["Simit", "Dondurma", "Şeker"], 0, "\"we used to buy simit on the way\""),
        typ("İngilizce yazın: \"Eskiden bu sokakta bir sinema vardı.\"", variants("There used to be a cinema on this street.", "There used to be a cinema in this street.", "There used to be a cinema on this road."), "There used to be a cinema on this street."),
    ],
    {"kind": "speaking", "task": speak("Çocukluğunuzdan 6 şeyi used to ile anlatın: görünüşünüz, yaşadığınız yer, sevdiğiniz yemek, oyunlar, hobiler ve bir de There used to be... cümlesi.",
                                       "I used to have very curly hair. We used to live in a small flat in Mersin. I used to love my mother's stuffed peppers. I used to play football in the street with my cousins. I used to collect stickers. There used to be a big park near our house, but now there's a shopping centre.",
                                       ["used to + yalın fiil", "Alışkanlık ve durum", "There used to be"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "Yapmazdın mı?", "used to'nun olumsuz ve soru hallerini kullanarak geçmiş hakkında sorular sorabilirim.",
    {"kind": "dialogue", "title": "Kuşaklar arası söyleşi", "lines": [
        {"speaker": "Student", "text": "Grandpa, did you use to have a TV when you were a child?"},
        {"speaker": "Grandpa", "text": "No, we didn't use to have one. There was only one TV in the whole village, at the coffee house."},
        {"speaker": "Student", "text": "Really? What did you use to do in the evenings?"},
        {"speaker": "Grandpa", "text": "We used to listen to the radio, and my grandmother used to tell us stories."},
        {"speaker": "Student", "text": "Did you use to get pocket money?"},
        {"speaker": "Grandpa", "text": "Pocket money? No! We didn't use to need money. We made our own toys from wood."}],
     "questions": [
        mc("Where was the only TV in the village?", ["At school", "At the coffee house", "At Grandpa's house"], 1, "\"at the coffee house\""),
        mc("What did they use to do in the evenings?", ["Watch TV", "Listen to the radio and stories", "Play computer games"], 1, "\"We used to listen to the radio, and my grandmother used to tell us stories.\""),
     ]},
    {"explanation": "**Olumsuz ve soru** hallerinde **did** kullanılır ve **use to** (d olmadan) yazılır:\n\n| | Yapı | Örnek |\n|---|---|---|\n| Olumlu | used to + fiil | I **used to** play outside. |\n| Olumsuz | **didn't use to** + fiil | We **didn't use to** have a TV. |\n| Soru | **Did** + özne + **use to** + fiil? | **Did** you **use to** get pocket money? |\n| Soru kelimeli | Wh- + did + özne + use to? | **What did** you **use to** do? |\n| Kısa cevap | | Yes, I **did**. / No, I **didn't**. |\n\n**Neden \"use\"?** Çünkü did varsa fiil yalın olur (did + go, did + use).\n\n**Olumsuz için alternatif:** **never used to** → I **never used to** eat vegetables.\n\n**Günlük konuşmada** \"Did you use to...?\" yerine çoğu zaman sadece past simple de kullanılır: **Did you have** a TV when you were a child?",
     "examples": [{"en": "I didn't use to like fish, but now I love it.", "tr": "Eskiden balık sevmezdim ama şimdi bayılıyorum."},
                  {"en": "Did you use to walk to school?", "tr": "Okula yürüyerek mi giderdin?"},
                  {"en": "Where did you use to go on holiday?", "tr": "Tatile nereye giderdiniz?"}],
     "turkishNote": "\"didn't used to\" ve \"Did you used to\" yazımları çok yaygın hatalardır. did varsa \"use\" yazılır (d'siz). Telaffuzda fark duyulmaz ama yazıda önemlidir."},
    [
        mc("Hangisi doğru?", ["Did you used to play outside?", "Did you use to play outside?"], 1, "did + use to."),
        mc("Hangisi doğru?", ["I didn't use to like coffee.", "I didn't used to like coffee."], 0, "didn't use to."),
        mc("Did you use to have a bike? – Yes, I ___.", ["used", "did", "use"], 1, "Kısa cevap → did."),
        gap("We ___ use to have a car. (olumsuz)", ["didn't", "did not"], "didn't use to."),
        gap("What did you ___ to do at weekends?", ["use"], "use to."),
        gap("___ your parents use to be strict?", ["Did"], "Did + özne + use to."),
        gap("I ___ used to eat vegetables. (hiç)", ["never"], "never used to."),
        order(["you", "Did", "use", "to", "get", "pocket", "money", "?"], "Did you use to get pocket money?", "Did + özne + use to + fiil?", "Harçlık alır mıydın?"),
        listen("I didn't use to like reading when I was young. My sister used to read all the time, but I preferred playing outside.", "Konuşan çocukken ne yapmayı tercih ederdi?", ["Kitap okumayı", "Dışarıda oynamayı", "Televizyon izlemeyi"], 1, "\"I preferred playing outside\""),
        typ("İngilizce yazın: \"Eskiden balık sevmezdim.\"", variants("I didn't use to like fish.", "I did not use to like fish.", "I never used to like fish."), "I didn't use to like fish."),
    ],
    {"kind": "speaking", "task": speak("JAI ile röportaj yapın: Ona çocukluğu hakkında 6 soru sorun (Did you use to...? / What did you use to...? / Where did you use to...?). Sonra JAI size aynı soruları soracak; olumlu ve olumsuz cevaplar verin.",
                                       "Did you use to have a pet? What did you use to do after school? Where did you use to go on holiday? ... No, I didn't use to have a pet, but my neighbour had a dog. I used to do my homework and then play outside. We didn't use to go abroad. We used to go to Ayvalık.",
                                       ["Did ... use to? soruları", "didn't use to", "Kısa cevaplar"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "Her yaz giderdik", "would ile geçmişte tekrarlanan eylemleri anlatabilir, would ile used to'nun farkını bilirim.",
    {"kind": "text", "title": "Köydeki yazlar", "body": "When I was a child, I used to spend every summer at my grandparents' farm near Bolu.\n\nEvery morning, my grandfather would wake me up at six. We would walk to the field together, and he would tell me the names of all the plants and birds. My grandmother would make fresh bread, and the whole house would smell wonderful.\n\nIn the afternoons, my cousins and I would play hide and seek in the barn. We would come home covered in dust, and my grandmother would pretend to be angry.\n\nI used to be a very shy child, but on the farm I was free and happy. The farm isn't there any more, but I still remember every corner of it.",
     "questions": [
        mc("What time would the writer's grandfather wake them up?", ["At five", "At six", "At seven"], 1, "\"my grandfather would wake me up at six\""),
        mc("Is the farm still there?", ["Yes, it is.", "No, it isn't."], 1, "\"The farm isn't there any more\""),
     ]},
    {"explanation": "**would + yalın fiil** de geçmişte **tekrarlanan eylemleri** anlatır. Özellikle anı ve hikâyelerde çok kullanılır.\n\n- Every morning, my grandfather **would wake** me up at six.\n- We **would play** hide and seek for hours.\n\n**used to mu would mu?**\n\n| | used to | would |\n|---|---|---|\n| Tekrarlanan **eylem** | ✓ We used to play outside. | ✓ We would play outside. |\n| **Durum** (be, have, live, like, know) | ✓ I used to be shy. | ✗ ~~I would be shy.~~ |\n| | ✓ We used to live in Bolu. | ✗ ~~We would live in Bolu.~~ |\n\n**Anlatımda:** Hikâyeye genellikle **used to** ile başlanır, sonra **would** ile devam edilir (tekrar etmemek için):\n\n- I **used to** spend summers at the farm. Every morning, my grandfather **would** wake me up...\n\n**Dikkat:** Bu \"would\" conditional değildir; anlamı \"-ardı / -erdi\"dir.",
     "examples": [{"en": "On Sundays, my father would cook breakfast for everyone.", "tr": "Pazar günleri babam herkese kahvaltı hazırlardı."},
                  {"en": "I used to have a dog called Karabaş.", "tr": "Karabaş adında bir köpeğim vardı."},
                  {"en": "We would sit on the balcony and watch the stars.", "tr": "Balkonda oturur, yıldızları izlerdik."}],
     "turkishNote": "Türkçedeki \"-ardı / -erdi\" eki hem eylemler hem durumlar için kullanılır (\"giderdik\", \"utangaçtım\"). İngilizcede ise would sadece eylemler için kullanılabilir. Durum fiilleri için (be, have, live, love, know) mutlaka used to kullanın."},
    [
        mc("Durum: \"I ___ shy when I was young.\"", ["would be", "used to be"], 1, "Durum → used to."),
        mc("Eylem: \"Every summer we ___ to the sea.\"", ["would go", "would went"], 0, "would + yalın fiil."),
        mc("Hangisi yanlış?", ["We would live in a small flat.", "We used to live in a small flat."], 0, "live → durum → would olmaz."),
        mc("Hangisi yanlış?", ["My dad would read me stories.", "My dad used to read me stories.", "My dad would to read me stories."], 2, "would + yalın fiil (to yok)."),
        gap("On Fridays, my mum ___ make pizza. (tekrarlanan eylem; would)", ["would"], "would + fiil."),
        gap("I used to ___ (have) a cat called Tekir.", ["have"], "Durum → used to have."),
        gap("We would ___ (play) in the street until dark.", ["play"], "would + yalın fiil."),
        mc("would mümkün mü? \"I ___ love chocolate as a child.\"", ["would", "used to"], 1, "love → durum."),
        listen("Every winter, when it snowed, my brother and I would build a snowman in the garden. My mum would make hot chocolate for us afterwards.", "Annesi onlara ne yapardı?", ["Sıcak çikolata", "Çay", "Çorba"], 0, "\"My mum would make hot chocolate\""),
        typ("İngilizce yazın (would kullanın): \"Pazar günleri babam kahvaltı hazırlardı.\"", variants("On Sundays, my father would make breakfast.", "On Sundays, my father would cook breakfast.", "On Sundays, my dad would make breakfast.", "On Sundays, my dad would cook breakfast.", "On Sundays my father would make breakfast.", "On Sundays my dad would make breakfast.", "My father would make breakfast on Sundays.", "My dad would make breakfast on Sundays.", "On Sundays, my father would prepare breakfast.", "On Sundays, my dad would prepare breakfast."), "On Sundays, my father would make breakfast."),
    ],
    {"kind": "speaking", "task": speak("Çocukluğunuzdan tekrarlanan bir \"ritüeli\" anlatın (bayramlar, yaz tatilleri, okul sabahları, pazar günleri). used to ile başlayın, sonra en az 4 cümleyi would ile devam ettirin. Bir durum cümlesi için mutlaka used to kullanın.",
                                       "During Bayram, we used to go to my grandmother's house in Kütahya. Early in the morning, my father would put on his best suit. We would kiss our grandparents' hands, and they would give us some money. My aunt would make baklava, and we would eat until we felt sick! I used to love those days.",
                                       ["used to ile başlangıç", "would ile tekrarlanan eylemler", "Durumlar için used to"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Artık değil", "Geçmiş ile bugünü any more, no longer ve still ile karşılaştırabilirim.",
    {"kind": "text", "title": "O zaman ve şimdi: Çocuk olmak", "body": "In those days, children used to play outside until it got dark. Today, many children no longer play in the street. They spend more time at home, on tablets and phones.\n\nChildren used to make their own toys. Now most toys come from shops, and many of them need batteries.\n\nIn the past, families used to eat dinner together every evening. In many homes, this doesn't happen any more, because parents work late.\n\nBut some things haven't changed. Children still love stories, they still laugh at silly jokes, and they still want their parents' attention.",
     "questions": [
        mc("What do many children no longer do?", ["Watch cartoons", "Play in the street", "Go to school"], 1, "\"many children no longer play in the street\""),
        mc("What do children still love?", ["Stories", "Making toys", "Playing until dark"], 0, "\"Children still love stories\""),
     ]},
    {"explanation": "**Değişimi anlatmak:**\n\n| İfade | Yeri | Örnek |\n|---|---|---|\n| **not ... any more** | cümle sonu | I **don't** play football **any more**. |\n| **no longer** | fiilden önce (be'den sonra) | I **no longer** play football. / The shop **is no longer** open. |\n| **still** | fiilden önce (be'den sonra) | I **still** play football. / She **is still** my best friend. |\n\n**no longer** daha resmîdir ve fiil **olumlu** kalır:\n\n- I **no longer live** there. (~~I don't no longer live~~)\n\n**any more** ile fiil **olumsuz** olur:\n\n- I **don't live** there **any more**.\n\n**Karşılaştırma kalıbı:**\n\n- I **used to** ..., but **now** I ...\n- I **used to** ..., but I **don't** ... **any more**.\n- I **didn't use to** ..., but **now** I ...\n- I **still** ...",
     "examples": [{"en": "I used to eat meat, but I don't any more.", "tr": "Eskiden et yerdim ama artık yemiyorum."},
                  {"en": "We no longer live in Istanbul.", "tr": "Artık İstanbul'da yaşamıyoruz."},
                  {"en": "My grandmother is 90, but she still cooks every day.", "tr": "Büyükannem 90 yaşında ama hâlâ her gün yemek yapıyor."}],
     "turkishNote": "Türkçedeki \"artık\" kelimesi iki anlama gelir: \"artık yapmıyorum\" (not any more / no longer) ve \"artık yapıyorum\" (now). \"I now drive to work\" (artık işe arabayla gidiyorum) gibi olumlu durumlarda any more kullanılmaz; now kullanılır."},
    [
        mc("Hangisi doğru?", ["I don't no longer smoke.", "I no longer smoke.", "I no longer don't smoke."], 1, "no longer + olumlu fiil."),
        mc("Hangisi doğru?", ["I don't play the piano any more.", "I play the piano any more."], 0, "any more + olumsuz."),
        mc("\"Hâlâ\":", ["any more", "still", "no longer"], 1, "still."),
        mc("\"Artık işe arabayla gidiyorum.\" (olumlu)", ["I drive to work any more.", "I now drive to work."], 1, "Olumlu değişim → now."),
        gap("She ___ lives with her parents. (hâlâ)", ["still"], "still."),
        gap("We don't go there ___ more.", ["any"], "any more."),
        gap("The shop is no ___ open.", ["longer"], "no longer."),
        gap("I used to be scared of dogs, but I'm not ___ more.", ["any"], "not any more."),
        listen("I used to watch a lot of TV, but I don't any more. I still watch the news every evening, though.", "Konuşan hâlâ ne izliyor?", ["Dizileri", "Haberleri", "Hiçbir şey"], 1, "\"I still watch the news every evening\""),
        typ("İngilizce yazın: \"Artık İstanbul'da yaşamıyoruz.\"", variants("We don't live in Istanbul any more.", "We don't live in Istanbul anymore.", "We no longer live in Istanbul.", "We do not live in Istanbul any more.", "We do not live in Istanbul anymore."), "We don't live in Istanbul any more."),
    ],
    {"kind": "speaking", "task": speak("Siz çocukken ve şimdi: Kendinizdeki ve dünyadaki değişimleri karşılaştırın. used to, didn't use to, any more, no longer ve still'i en az birer kez kullanın (en az 6 cümle).",
                                       "I used to be scared of the dark, but I'm not any more. I didn't use to like vegetables, but now I eat salad every day. I no longer collect football cards. I still love cartoons! In the past, people used to write letters. Now nobody writes letters any more. But children still play hide and seek.",
                                       ["any more / no longer / still doğru", "used to ile karşılaştırma", "Olumlu-olumsuz yapı doğru"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Bir çocukluk anısı", "Bir çocukluk anısını used to, would ve geçmiş zamanları bir arada kullanarak anlatabilirim.",
    {"kind": "dialogue", "title": "Radyo programı: Unutamadığım öğretmen", "lines": [
        {"speaker": "Host", "text": "Our next caller is Nurcan from Malatya. Nurcan, who's the teacher you'll never forget?"},
        {"speaker": "Nurcan", "text": "My primary school teacher, Mr Erdem. He was quite strict, but we all loved him."},
        {"speaker": "Host", "text": "What was special about him?"},
        {"speaker": "Nurcan", "text": "Every Friday, he would bring a new book and read it to us. We would sit on the floor and listen without making a sound."},
        {"speaker": "Host", "text": "That's lovely. Are you still in touch?"},
        {"speaker": "Nurcan", "text": "Yes! Last year I found him on social media. He no longer teaches, but he still reads every day. And I became a teacher because of him."}],
     "questions": [
        mc("What would Mr Erdem do every Friday?", ["Give a test", "Read a new book to the class", "Take them outside"], 1, "\"he would bring a new book and read it to us\""),
        mc("What happened because of Mr Erdem?", ["Nurcan became a writer.", "Nurcan became a teacher.", "Nurcan moved to Malatya."], 1, "\"I became a teacher because of him\""),
     ]},
    {"explanation": "**Bir anıyı anlatırken zamanları birleştirin:**\n\n| Zaman | Görevi | Örnek |\n|---|---|---|\n| **used to** | genel arka plan, durumlar | He **used to be** quite strict. |\n| **would** | tekrarlanan sahneler | Every Friday, he **would read** to us. |\n| **past simple** | tek bir olay | One day, he **brought** a puppy to class! |\n| **past continuous** | o anda süren | We **were sitting** on the floor when ... |\n| **still / no longer** | bugüne bağlantı | He **no longer** teaches, but he **still** reads. |\n\n**Anı anlatmak için kalıplar:**\n\n- **One of my earliest memories is** ...\n- **I'll never forget** the day when ...\n- **I remember** + -ing: I remember **sitting** on the floor.\n- **Looking back**, ... (Geriye dönüp bakınca)\n- **It makes me smile when I think about** it.",
     "examples": [{"en": "One of my earliest memories is my third birthday.", "tr": "En eski anılarımdan biri üçüncü doğum günüm."},
                  {"en": "I remember walking to school in the snow.", "tr": "Karda okula yürüdüğümü hatırlıyorum."},
                  {"en": "Looking back, I had a very happy childhood.", "tr": "Geriye dönüp bakınca çok mutlu bir çocukluğum olmuş."}],
     "turkishNote": "\"... yaptığımı hatırlıyorum\" yapısı İngilizcede \"I remember + -ing\" ile kurulur: I remember playing in the garden. \"I remember that I played\" de doğrudur ama daha az doğaldır."},
    [
        mc("Tek bir olay: \"One day, my dad ___ home a puppy.\"", ["would bring", "brought", "used to bring"], 1, "Tek olay → past simple."),
        mc("Tekrarlanan sahne: \"Every evening, we ___ on the balcony.\"", ["would sit", "sat once"], 0, "Tekrar → would."),
        mc("\"Bahçede oynadığımı hatırlıyorum.\"", ["I remember to play in the garden.", "I remember playing in the garden."], 1, "remember + -ing (anı)."),
        gap("One of my earliest ___ is my first day at school. (anı)", ["memories"], "One of my earliest memories."),
        gap("I'll never ___ the day I met her.", ["forget"], "I'll never forget."),
        gap("___ back, I was very lucky. (geriye dönüp bakınca)", ["Looking"], "Looking back."),
        gap("He no longer teaches, but he ___ reads every day.", ["still"], "still."),
        gap("My teacher used to ___ (be) very strict.", ["be"], "used to be."),
        listen("I'll never forget my eighth birthday. My parents didn't use to have much money, but that year they bought me a bike. I would ride it every day after school.", "Konuşanın sekizinci doğum gününde ne oldu?", ["Bir köpek aldı", "Bisiklet hediye edildi", "Partiye gitti"], 1, "\"that year they bought me a bike\""),
        typ("İngilizce yazın: \"Karda okula yürüdüğümü hatırlıyorum.\"", variants("I remember walking to school in the snow.", "I remember walking to school in snow.", "I remember that I walked to school in the snow."), "I remember walking to school in the snow."),
    ],
    {"kind": "writing", "task": write("\"Unutamadığım bir çocukluk anısı\" başlıklı bir yazı yazın (130–160 kelime). used to ile arka planı kurun, would ile tekrarlanan sahneleri anlatın, past simple / past continuous ile özel bir olayı aktarın ve still / no longer ile bugüne bağlayın.",
                                      "One of my earliest memories is of my grandfather's small shop in Tokat. He used to sell newspapers, sweets and toys, and I used to think it was the most exciting place in the world.\n\nEvery day after school, I would run to the shop. My grandfather would give me a piece of lokum, and I would sit behind the counter and watch the customers.\n\nI'll never forget one winter afternoon. It was snowing heavily and the shop was empty. My grandfather was reading his newspaper when he suddenly looked up and said, \"Let's build the biggest snowman in Tokat!\" We closed the shop and played in the snow for two hours.\n\nThe shop no longer exists, and my grandfather died ten years ago. But I still remember the smell of the newspapers, and it still makes me smile when I think about that day.",
                                      ["used to / would doğru", "Past simple / continuous ile özel olay", "still / no longer", "Anı kalıpları", "Duygusal ve düzenli anlatım"])},
)

u.test([
    mc("Hangisi doğru?", ["I used to living in Rize.", "I used to live in Rize."], 1, "used to + yalın fiil"),
    mc("Hangisi doğru?", ["Did you used to play outside?", "Did you use to play outside?"], 1, "did + use to"),
    mc("Durum: \"I ___ shy when I was a child.\"", ["would be", "used to be"], 1, "Durum → used to"),
    mc("Tek olay: \"I ___ to London in 2019.\"", ["used to go", "went"], 1, "past simple"),
    mc("Hangisi doğru?", ["I don't no longer eat meat.", "I no longer eat meat."], 1, "no longer + olumlu"),
    gap("We didn't ___ to have a car.", ["use"], "didn't use to"),
    gap("There ___ to be a cinema here.", ["used"], "There used to be"),
    gap("Every summer we ___ go to the village. (tekrarlanan eylem)", ["would", "used to"], "would / used to"),
    gap("I don't play the guitar ___ more.", ["any"], "any more"),
    gap("She's 85, but she ___ drives. (hâlâ)", ["still"], "still"),
    mc("\"I would have a dog.\" (eskiden köpeğim vardı)", ["Doğru", "Yanlış, used to have olmalı"], 1, "have → durum"),
    mc("\"Karda oynadığımı hatırlıyorum.\"", ["I remember playing in the snow.", "I remember to play in the snow."], 0, "remember + -ing"),
    listen("My mum used to be a nurse. She would work at night, so in the mornings my dad would take us to school. She no longer works, but she still helps our neighbours when they're ill.", "Annesi gece çalıştığı için sabahları onları okula kim götürürdü?", ["Annesi", "Babası", "Komşuları"], 1, "\"my dad would take us to school\""),
    typ("İngilizce yazın: \"Eskiden çok utangaçtım.\"", variants("I used to be very shy.", "I used to be really shy.", "I used to be so shy."), "I used to be very shy."),
    write("Siz çocukken ve bugün: Hayatınızın nasıl değiştiğini anlatan bir paragraf yazın (130–160 kelime). used to, didn't use to, would, any more, no longer ve still'in hepsini kullanın.",
          "When I was a child, I used to live in a small town near Samsun. I didn't use to have many toys, but I had lots of friends. Every afternoon, we would play football in the street until our mothers called us for dinner. At weekends, my father would take us fishing. I used to be very naughty, and my teachers used to complain about me! Today, my life is very different. I no longer live in a small town; I live in a big city, and I don't play football in the street any more. I didn't use to like reading, but now I read every evening. Some things haven't changed, though. I still love fishing, and I still talk to my childhood friends every week.",
          ["used to / didn't use to / would", "any more / no longer / still", "Geçmiş-bugün karşılaştırması", "Doğru zaman kullanımı", "Akıcı paragraf"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

"""B2 Ünite 8: İlişkiler."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("B2", 8, "İlişkiler", "Relationships",
         "İlişkileri anlatırken en sık kullanılan phrasal verb'leri doğru yapıda (ayrılabilen, ayrılamayan, üç parçalı) kullanabilir, zamirin yerini doğru seçebilir ve phrasal verb ile resmî karşılığı arasında üslup tercihi yapabilirim.",
         ["phrasal verb nedir: nesnesiz ve nesneli", "ayrılabilen phrasal verbs ve zamir yeri", "ayrılamayan ve üç parçalı phrasal verbs", "çok anlamlı phrasal verbs", "phrasal verb ve resmî karşılıkları"],
         ["arkadaşlık ve aile", "romantik ilişkiler", "anlaşmazlık ve barışma"],
         {"title": "İlişki danışmanı", "durationMinutes": 45,
          "goal": "Öğrenciler kısa \"dertleşme\" kartları alır (I've fallen out with my best friend, my flatmate never tidies up...). İkili rol oyununda biri derdini anlatır, diğeri phrasal verb'lerle tavsiye verir. Sonra sınıf en iyi tavsiyeleri seçer ve aynı tavsiyeyi resmî bir dille (tolerate, reconcile) yeniden ifade eder."})

u.vocab([
    ("get on (well) with", "iyi anlaşmak", "I get on really well with my sister.", "Kız kardeşimle çok iyi anlaşırım.", None),
    ("fall out (with)", "küsmek, bozuşmak", "They fell out over money.", "Para yüzünden bozuştular.", None),
    ("make up", "barışmak", "We argued, but we made up the next day.", "Tartıştık ama ertesi gün barıştık.", "make up a story = uydurmak"),
    ("break up (with)", "ayrılmak (ilişki)", "She broke up with her boyfriend last month.", "Geçen ay erkek arkadaşından ayrıldı.", None),
    ("ask sb out", "çıkma teklif etmek", "He finally asked her out.", "Sonunda ona çıkma teklif etti.", None),
    ("go out (with)", "çıkmak (sevgili olarak)", "They've been going out for two years.", "İki yıldır çıkıyorlar.", None),
    ("split up", "ayrılmak", "My parents split up when I was ten.", "Ben on yaşındayken annemle babam ayrıldı.", None),
    ("let sb down", "hayal kırıklığına uğratmak", "I trusted you. Please don't let me down.", "Sana güvendim. Lütfen beni hayal kırıklığına uğratma.", None),
    ("look after", "bakmak, ilgilenmek", "She looks after her grandmother.", "Büyükannesine bakıyor.", None),
    ("take after", "(aileden birine) çekmek", "He takes after his father.", "Babasına çekmiş.", None),
    ("bring up", "yetiştirmek; (konuyu) açmak", "She was brought up by her aunt.", "Teyzesi tarafından yetiştirildi.", None),
    ("grow apart", "zamanla uzaklaşmak", "We were close at school, but we grew apart.", "Okulda yakındık ama zamanla uzaklaştık.", None),
    ("look up to", "örnek almak, saygı duymak", "I've always looked up to my grandfather.", "Dedemi hep örnek aldım.", None),
    ("put up with", "katlanmak, tahammül etmek", "I can't put up with his moods any more.", "Onun huysuzluklarına artık katlanamıyorum.", None),
    ("get over", "atlatmak", "It took her months to get over the break-up.", "Ayrılığı atlatması aylarını aldı.", None),
    ("run into", "rastlamak", "I ran into an old friend at the airport.", "Havaalanında eski bir arkadaşa rastladım.", None),
    ("catch up (with)", "hasret gidermek, son durumu konuşmak", "Let's meet for coffee and catch up.", "Bir kahve içip hasret giderelim.", None),
    ("count on", "güvenmek, bel bağlamak", "You can always count on me.", "Bana her zaman güvenebilirsin.", None),
    ("stand by", "yanında olmak, desteklemek", "Her friends stood by her.", "Arkadaşları onun yanında durdu.", None),
    ("turn down", "reddetmek", "She turned down his invitation.", "Davetini reddetti.", None),
    ("settle down", "düzen kurmak, yerleşmek", "They want to settle down and have kids.", "Düzen kurup çocuk sahibi olmak istiyorlar.", None),
    ("tell sb off", "azarlamak", "My mum told me off for coming home late.", "Annem geç geldiğim için beni azarladı.", None),
    ("open up (to)", "açılmak, içini dökmek", "It took him a long time to open up to me.", "Bana açılması uzun zaman aldı.", None),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "İyi anlaşmak, bozuşmak", "İlişkileri anlatan temel phrasal verb'leri nesnesiz ve nesneli kullanabilirim.",
    {"kind": "dialogue", "title": "Kafede iki arkadaş", "lines": [
        {"speaker": "Duygu", "text": "So, how are things with Emre?"},
        {"speaker": "Ece", "text": "Not great. We fell out last week."},
        {"speaker": "Duygu", "text": "Oh no. What happened? You two always got on so well."},
        {"speaker": "Ece", "text": "He forgot my birthday, and then he didn't even apologise. We haven't spoken since."},
        {"speaker": "Duygu", "text": "You've been going out for three years. You can't break up over a birthday!"},
        {"speaker": "Ece", "text": "I know. I just want him to call me so we can make up."}],
     "questions": [
        mc("Why did Ece and Emre fall out?", ["He forgot her birthday.", "He lied to her.", "She forgot his birthday."], 0, "\"He forgot my birthday\""),
        mc("What does Ece want?", ["To break up", "To make up", "To move abroad"], 1, "\"so we can make up\""),
     ]},
    {"explanation": "**Phrasal verb** = fiil + edat/zarf (particle). Anlamı çoğu zaman parçalardan tahmin edilemez.\n\n- **get on** = iyi anlaşmak (≠ get + on)\n- **make up** = barışmak (≠ make + up)\n\n**1. Nesnesiz (intransitive) phrasal verbs:** Arkalarından nesne gelmez.\n\n| Phrasal verb | Örnek |\n|---|---|\n| **fall out** | We **fell out**. |\n| **make up** | We **made up** the next day. |\n| **break up / split up** | They **broke up** last year. |\n| **grow apart** | We slowly **grew apart**. |\n| **settle down** | They want to **settle down**. |\n\n**2. Nesne eklemek için genellikle bir edat daha gelir:**\n\n| Nesnesiz | Nesneli |\n|---|---|\n| We fell out. | I fell out **with** Can. |\n| They broke up. | She broke up **with** him. |\n| We get on well. | I get on well **with** my boss. |\n| We made up. | I made up **with** my brother. |\n\n**İlişki hikâyesi sırası:** ask sb out → go out with → (fall out → make up) → settle down / **break up**",
     "examples": [{"en": "I don't get on with my flatmate.", "tr": "Ev arkadaşımla anlaşamıyorum."},
                  {"en": "They split up after ten years together.", "tr": "On yıl birlikte olduktan sonra ayrıldılar."},
                  {"en": "We were best friends, but we grew apart after university.", "tr": "En iyi arkadaştık ama üniversiteden sonra zamanla uzaklaştık."}],
     "turkishNote": "Türkçede \"anlaşmak\", \"küsmek\", \"barışmak\" tek kelimedir; İngilizcede bunlar phrasal verb'lerle karşılanır. En sık hata, nesne eklerken \"with\" edatını unutmaktır: \"I don't get on my boss\" yanlıştır; doğrusu \"I don't get on with my boss\". \"Biriyle çıkmak\" da \"go out with\" olur; \"go out\" tek başına \"dışarı çıkmak\" demektir."},
    [
        mc("\"Patronumla iyi anlaşırım.\"", ["I get on well my boss.", "I get on well with my boss."], 1, "with gerekli."),
        mc("\"Barıştık.\"", ["We made up.", "We broke up."], 0, "make up = barışmak."),
        mc("\"They're going out.\" ilişki bağlamında:", ["Dışarı çıkıyorlar / sevgililer", "Ayrılıyorlar"], 0, "go out (with) = çıkmak."),
        mc("Nesnesiz phrasal verb:", ["fall out", "look after"], 0, "fall out."),
        gap("She broke up ___ her boyfriend.", ["with"], "break up with."),
        gap("We fell ___ over something stupid. (bozuştuk)", ["out"], "fall out."),
        gap("After school, the two friends slowly grew ___.", ["apart"], "grow apart."),
        gap("They want to settle ___ and buy a house.", ["down"], "settle down."),
        listen("My best friend and I fell out at university because we both liked the same boy. We didn't speak for two years. Then we ran into each other at a wedding, and we made up in five minutes. Now we laugh about it.", "Nasıl barıştılar?", ["Telefonda", "Bir düğünde karşılaşınca", "Ortak bir arkadaş sayesinde"], 1, "\"we ran into each other at a wedding, and we made up\""),
        typ("İngilizcesi: \"Kardeşimle iyi anlaşmıyorum.\" (my brother)", variants("I don't get on with my brother.", "I don't get on well with my brother.", "I don't get along with my brother."), "I don't get on with my brother."),
    ],
    {"kind": "speaking", "task": speak("Hayatınızdaki 3 ilişkiyi anlatın (bir arkadaş, bir aile üyesi, bir iş arkadaşı). Her biri için get on with, fall out (with), make up (with), grow apart gibi phrasal verb'leri kullanın. Bir ilişkinin zaman içinde nasıl değiştiğini de anlatın.",
                                       "I get on really well with my cousin Ayşe. We're the same age, and we talk every day. When we were teenagers, we fell out about a party, but we made up after a week. I had a close friend at primary school called Mert, but we grew apart when his family moved to Izmir. At work, I don't really get on with one of my colleagues because he never listens, but we're polite to each other.",
                                       ["Nesnesiz ve nesneli kullanım", "with edatı", "İlişkideki değişimi anlatma"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "Onu davet etti, onu reddetti", "Ayrılabilen phrasal verb'lerde nesneyi doğru yere, özellikle zamiri ortaya koyabilirim.",
    {"kind": "text", "title": "Sosyal medya itirafı", "body": "I've had a crush on Deniz from my yoga class for months. Last week, I finally decided to ask her out.\n\nI wrote a long message, read it twenty times, and then deleted it. I was scared she would turn me down. My flatmate told me off for being such a coward and said, \"Just call her up!\"\n\nSo I called her up. My hands were shaking. And guess what? She said yes!\n\nWe're meeting on Saturday. I really hope I don't let her down. Please don't tell me what to wear. I've already tried on everything I own.",
     "questions": [
        mc("Why did the writer delete the message?", ["Deniz has a partner.", "The writer was scared Deniz would say no.", "The writer made a spelling mistake."], 1, "\"I was scared she would turn me down.\""),
        mc("What did the flatmate say?", ["\"Just call her up!\"", "\"Send a message.\"", "\"Forget her.\""], 0, "\"Just call her up!\""),
     ]},
    {"explanation": "Bazı nesneli phrasal verb'ler **ayrılabilir** (separable): nesne particle'dan **önce ya da sonra** gelebilir.\n\n| Nesne isimse: İKİ YER DE OLUR | Nesne zamirse: SADECE ORTADA |\n|---|---|\n| He asked **Deniz** out. ✓ | He asked **her** out. ✓ |\n| He asked out **Deniz**. ✓ | ~~He asked out her.~~ ✗ |\n| She turned **the offer** down. ✓ | She turned **it** down. ✓ |\n| She turned down **the offer**. ✓ | ~~She turned down it.~~ ✗ |\n\n**Altın kural:** **it, him, her, them, me, you, us** her zaman **fiil ile particle'ın arasına** girer.\n\n**Sık kullanılan ayrılabilen phrasal verbs:**\n\n| Phrasal verb | Anlam | Zamirle |\n|---|---|---|\n| **ask sb out** | çıkma teklif etmek | ask **her** out |\n| **turn sth/sb down** | reddetmek | turn **it** down |\n| **let sb down** | hayal kırıklığına uğratmak | let **them** down |\n| **tell sb off** | azarlamak | tell **him** off |\n| **call sb up** | telefonla aramak | call **me** up |\n| **bring sb up** | yetiştirmek | bring **them** up |\n| **cheer sb up** | neşelendirmek | cheer **her** up |\n\n**Uzun nesneler** genellikle sona gider: *She turned down **the job offer from the bank in London**.*",
     "examples": [{"en": "I called him up, but he didn't answer.", "tr": "Onu aradım ama açmadı."},
                  {"en": "They offered her a job, but she turned it down.", "tr": "Ona bir iş teklif ettiler ama reddetti."},
                  {"en": "Don't worry, I won't let you down.", "tr": "Merak etme, seni hayal kırıklığına uğratmayacağım."}],
     "turkishNote": "Türkçede nesne fiilden önce gelir (\"onu reddetti\"), ama phrasal verb'lerde bölünme fikri yoktur. Türkçe konuşanların en sık yaptığı hata \"turn down it\", \"ask out her\" gibi yapılardır. Ezber cümle: \"Turn it down, pick it up, let me down\". Zamir her zaman ortada!"},
    [
        mc("Hangisi doğru?", ["She turned down it.", "She turned it down."], 1, "Zamir ortada."),
        mc("Hangisi doğru?", ["He asked out her.", "He asked her out."], 1, "Zamir ortada."),
        mc("İkisi de doğru mu? \"She turned the offer down.\" / \"She turned down the offer.\"", ["Evet", "Hayır"], 0, "İsim → iki yer de olur."),
        mc("\"Don't let me down.\" anlamı:", ["Beni yere indirme.", "Beni hayal kırıklığına uğratma."], 1, "let down."),
        gap("Your sister looks sad. Let's cheer ___ up.", ["her"], "Zamir ortada."),
        gap("They offered me the job, but I turned ___ down.", ["it"], "turn it down."),
        gap("My teacher told me ___ for being late. (azarladı)", ["off"], "tell sb off."),
        gap("He was brought ___ by his grandparents.", ["up"], "bring up (edilgen)."),
        listen("My best friend promised to help me move house on Saturday. I waited all morning, but he didn't come. I called him up three times, and he didn't answer. He really let me down.", "Arkadaşı ne yaptı?", ["Erken geldi", "Gelmedi ve telefonu açmadı", "Başka birini gönderdi"], 1, "\"he didn't come... he didn't answer\""),
        order(["She", "asked", "me", "out", "but", "I", "turned", "her", "down"], "She asked me out but I turned her down.", "Zamirler fiil ile particle arasında.", "Bana çıkma teklif etti ama onu reddettim."),
    ],
    {"kind": "speaking", "task": speak("Birinin size ya da sizin birine bir teklif yaptığınız bir durumu anlatın (bir iş, bir davet, bir randevu). En az 5 ayrılabilen phrasal verb kullanın ve zamirleri doğru yere koyun: ask (her/him) out, turn (it) down, call (them) up, let (me) down, cheer (him) up, tell (me) off.",
                                       "Two years ago, a company in Ankara offered me a great job, but I turned it down because I didn't want to leave my family. My manager was disappointed, and I felt I had let him down. My best friend called me up every day to cheer me up. Then, a year later, the company called me up again with a better offer, and this time I didn't turn it down!",
                                       ["Ayrılabilen phrasal verbs", "Zamir yeri (ortada)", "Akıcı anlatım"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "Örnek almak, katlanmak", "Ayrılamayan ve üç parçalı phrasal verb'leri doğru yapıda kullanabilirim.",
    {"kind": "text", "title": "Bir röportajdan: \"Dedem benim kahramanım\"", "body": "\"I've always looked up to my grandfather. He was a fisherman in Sinop, and he looked after his six younger brothers and sisters after his father died. He was only fifteen.\n\nPeople say I take after him. We're both stubborn, and we both love the sea.\n\nWhen I was a teenager, I went through a difficult time. My parents had split up, and I was angry with everyone. My grandfather never told me off. He just took me fishing every weekend and listened. Slowly, I opened up to him. He helped me get over it.\n\nHe died last year, at 92. I still can't believe he's gone, but I know I can always count on the lessons he taught me.\"",
     "questions": [
        mc("Who did the grandfather look after?", ["His children", "His younger brothers and sisters", "His neighbours"], 1, "\"he looked after his six younger brothers and sisters\""),
        mc("How did the grandfather help?", ["He gave advice.", "He took the speaker fishing and listened.", "He sent the speaker to a doctor."], 1, "\"He just took me fishing every weekend and listened.\""),
     ]},
    {"explanation": "**Ayrılamayan (inseparable) phrasal verbs:** Nesne (isim ya da zamir) **her zaman sonra** gelir.\n\n| Phrasal verb | Anlam | Örnek |\n|---|---|---|\n| **look after** | bakmak | She looks after **him**. (~~looks him after~~) |\n| **take after** | çekmek | I take after **my mum**. |\n| **get over** | atlatmak | He got over **it**. |\n| **run into** | rastlamak | I ran into **her** yesterday. |\n| **count on** | güvenmek | You can count on **me**. |\n| **go through** | (zor bir dönem) yaşamak | She's going through **a hard time**. |\n| **stand by** | yanında olmak | They stood by **him**. |\n\n**Üç parçalı (three-part) phrasal verbs:** Her zaman ayrılamaz.\n\n| Phrasal verb | Anlam | Örnek |\n|---|---|---|\n| **look up to** | örnek almak | I look up to **her**. |\n| **put up with** | katlanmak | I can't put up with **it**. |\n| **get on with** | iyi anlaşmak | I get on with **them**. |\n| **catch up with** | yetişmek; hasret gidermek | Let's catch up with **Ali**. |\n| **fall out with** | bozuşmak | She fell out with **him**. |\n| **look down on** | küçük görmek | Don't look down on **people**. |\n\n**Nasıl ayırt edilir?** Sözlükler genellikle **look after sb** (ayrılamaz) ve **turn sth down** (ayrılabilir) biçiminde gösterir: **sb/sth'nin yeri** ipucudur.",
     "examples": [{"en": "Who looks after your kids when you're at work?", "tr": "Sen işteyken çocuklarına kim bakıyor?"},
                  {"en": "I can't put up with this noise any longer.", "tr": "Bu gürültüye artık katlanamıyorum."},
                  {"en": "It took me a year to get over it.", "tr": "Onu atlatmam bir yılımı aldı."}],
     "turkishNote": "Türkçede \"babasına çekmek\", \"birine katlanmak\", \"bir şeyi atlatmak\" gibi fiiller tek parçadır ve doğru hal ekiyle kullanılır. İngilizce karşılıklarında bu hal eki işlevini particle görür; bu yüzden particle hiç atlanmamalıdır: \"I can't put up him\" yanlıştır; \"I can't put up with him\" doğrudur. Ayrıca \"take after\" sadece aileden birine benzemek için kullanılır."},
    [
        mc("Hangisi doğru?", ["She looks her grandmother after.", "She looks after her grandmother."], 1, "Ayrılamaz."),
        mc("Hangisi doğru?", ["I got it over.", "I got over it."], 1, "Ayrılamaz."),
        mc("\"Annesine çekmiş.\"", ["She takes after her mother.", "She looks after her mother."], 0, "take after."),
        mc("Üç parçalı:", ["put up with", "turn down"], 0, "put up with."),
        gap("I can't put up ___ his jokes any more.", ["with"], "put up with."),
        gap("I've always looked ___ to my older sister.", ["up"], "look up to."),
        gap("You can always count ___ me.", ["on"], "count on."),
        gap("She's going ___ a difficult time at the moment.", ["through"], "go through."),
        listen("I ran into my old teacher at the supermarket yesterday. She remembered me after twenty years! We caught up for half an hour. She was the one who made me want to become a teacher. I've always looked up to her.", "Konuşan öğretmenine karşı ne hissediyor?", ["Ona katlanamıyor", "Onu örnek alıyor", "Onu hatırlamıyor"], 1, "\"I've always looked up to her.\""),
        typ("İngilizcesi: \"Ayrılığı atlatması aylarını aldı.\" (it took her months)", variants("It took her months to get over the break-up.", "It took her months to get over the breakup."), "It took her months to get over the break-up."),
    ],
    {"kind": "speaking", "task": speak("Hayatınızda örnek aldığınız (look up to) birini anlatın. Kim olduğunu, kime çektiğinizi (take after), zor bir dönemi nasıl atlattığınızı (go through, get over), kime güvenebildiğinizi (count on, stand by) ve neye katlanamadığınızı (put up with) anlatın.",
                                       "I've always looked up to my mother. She's a nurse, and she looked after me and my two brothers on her own after my father passed away. Everyone says I take after her, because I'm very patient. When I was at university, I went through a really hard time, and she stood by me. I can always count on her. The only thing she can't put up with is people who are rude to waiters!",
                                       ["Ayrılamayan phrasal verbs", "Üç parçalı phrasal verbs", "Doğru particle kullanımı"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Bir fiil, birçok anlam", "Çok anlamlı phrasal verb'lerin anlamını bağlamdan çıkarabilir ve doğru kullanabilirim.",
    {"kind": "dialogue", "title": "Yeni hobiler", "lines": [
        {"speaker": "Cem", "text": "I've taken up salsa dancing!"},
        {"speaker": "Hale", "text": "Really? How's it working out?"},
        {"speaker": "Cem", "text": "Great. I'm picking it up quite quickly. And I've met loads of new people."},
        {"speaker": "Hale", "text": "That's great. Didn't your ex go to salsa classes too?"},
        {"speaker": "Cem", "text": "Please don't bring that up. She turned up at my class last week!"},
        {"speaker": "Hale", "text": "No way! What did you do?"},
        {"speaker": "Cem", "text": "Nothing. We just said hello. I've got over it. Honestly."}],
     "questions": [
        mc("What has Cem started?", ["Yoga", "Salsa dancing", "Cooking classes"], 1, "\"I've taken up salsa dancing!\""),
        mc("What happened last week?", ["Cem's ex came to his class.", "Cem won a competition.", "The class was cancelled."], 0, "\"She turned up at my class last week!\""),
     ]},
    {"explanation": "Birçok phrasal verb'ün **birden fazla anlamı** vardır. Anlamı **bağlam** belirler.\n\n| Phrasal verb | Anlam 1 | Anlam 2 | Anlam 3 |\n|---|---|---|---|\n| **pick up** | (yerden) almak | (birini arabayla) almak | (dil/beceri) kolayca öğrenmek |\n| **take up** | (hobi) başlamak | (yer/zaman) kaplamak | |\n| **bring up** | (çocuk) yetiştirmek | (konu) açmak | |\n| **work out** | spor yapmak | (bir sorunu) çözmek | iyi sonuçlanmak |\n| **turn up** | (beklenmedik) gelmek, ortaya çıkmak | (ses) açmak | |\n| **make up** | barışmak | (hikâye) uydurmak | (bir bütünü) oluşturmak |\n| **go off** | (alarm) çalmak | (yiyecek) bozulmak | (birinden) soğumak |\n\n**Örnekler:**\n\n- I **picked up** some Spanish in Mexico. (öğrendim)\n- Can you **pick me up** at eight? (arabayla almak)\n- I **worked out** the answer. (çözdüm) / I **work out** at the gym. (spor yapıyorum)\n- Things didn't **work out** between us. (yürümedi)\n- He **made up** an excuse. (uydurdu)\n\n**Strateji:** Bilmediğiniz bir phrasal verb'le karşılaşınca önce cümlenin konusuna bakın: ilişki, iş, spor, yemek?",
     "examples": [{"en": "I picked up a bit of Italian on holiday.", "tr": "Tatilde biraz İtalyanca kaptım."},
                  {"en": "I'm sorry it didn't work out between you two.", "tr": "İkinizin arasının yürümemesine üzüldüm."},
                  {"en": "He always makes up excuses for being late.", "tr": "Geç kalmak için hep bahaneler uydurur."}],
     "turkishNote": "Türkçede de \"almak\" fiilinin pek çok anlamı vardır (ders almak, haber almak, birini arabayla almak). İngilizcedeki pick up da benzer şekilde çalışır. Bilmediğiniz bir phrasal verb'ü kelime kelime çevirmeye çalışmak yerine bağlama bakın: \"Things didn't work out\" ifadesinin sporla bir ilgisi yoktur!"},
    [
        mc("\"I picked up some Japanese in Tokyo.\" anlamı:", ["Japonca kitap aldım.", "Biraz Japonca öğrendim."], 1, "Beceri kapmak."),
        mc("\"Things didn't work out between us.\"", ["Spor yapmadık.", "İlişkimiz yürümedi."], 1, "work out = iyi sonuçlanmak."),
        mc("\"Don't bring it up.\"", ["Onu yetiştirme.", "O konuyu açma."], 1, "Konu açmak."),
        mc("\"The milk has gone off.\"", ["Süt bozulmuş.", "Süt bitmiş."], 0, "go off = bozulmak."),
        gap("I've taken ___ yoga to reduce stress.", ["up"], "take up (hobi)."),
        gap("He didn't turn ___ to the meeting. (gelmedi)", ["up"], "turn up."),
        gap("Can you pick me ___ from the station?", ["up"], "pick up."),
        gap("She made ___ a story about losing her keys. (uydurdu)", ["up"], "make up."),
        match([("take up", "(hobiye) başlamak"), ("turn up", "çıkagelmek"), ("work out", "çözmek / yürümek"), ("go off", "bozulmak / çalmak"), ("pick up", "kapmak, öğrenmek")], "Eşleştirin."),
        listen("My alarm didn't go off this morning, so I overslept. I tried to make up an excuse for my boss, but he just laughed and said, \"Don't worry, it happens.\" I'm going to buy a new alarm clock.", "Konuşan neden geç kaldı?", ["Alarm çalmadı", "Otobüs gelmedi", "Hastaydı"], 0, "\"My alarm didn't go off\""),
    ],
    {"kind": "speaking", "task": speak("Şu phrasal verb'lerin her birini iki farklı anlamda birer cümlede kullanın: pick up, work out, make up, bring up, turn up. Sonra bunlardan üçünü kullanarak kısa bir hikâye anlatın.",
                                       "Pick up: I picked up some Greek in Crete. My dad picks me up from work on Fridays. Work out: I work out three times a week. We finally worked out the problem. Make up: We had a fight but we made up. He made up a story. Bring up: My aunt brought me up. Please don't bring up politics at dinner. Turn up: Can you turn up the music? He turned up two hours late. Story: Last summer, I took up surfing. My friend picked me up every morning, and after a week, I picked it up quite well.",
                                       ["Çok anlamlı phrasal verbs", "Bağlama uygun anlam", "Doğru yapı"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Dert ortağı", "Phrasal verb ile resmî karşılıkları arasında üslup seçimi yapabilir ve bir tavsiye köşesine samimi ama dengeli bir cevap yazabilirim.",
    {"kind": "text", "title": "Tavsiye köşesi", "body": "Dear Ayla,\n\nMy best friend and I have known each other since primary school, but recently we've been growing apart. She's started going out with a new group of people and she hardly ever calls me. Last month she didn't turn up to my birthday dinner. I feel she has let me down, but I don't want to lose her. What should I do?\n\nBerna, 24\n\n—\n\nDear Berna,\n\nI'm sorry you're going through this. It's painful when a close friendship starts to change.\n\nFirst, try not to jump to conclusions. Your friend might be dealing with something you don't know about. Call her up and suggest meeting for coffee, just the two of you, so you can catch up properly.\n\nWhen you meet, be honest. Tell her that you felt hurt when she didn't come to your birthday, but don't tell her off. Ask her how she's feeling.\n\nFriendships change as we get older. That doesn't always mean they end. But if she doesn't make an effort, it may be time to let go and invest in people you can really count on.\n\nAyla",
     "questions": [
        mc("What did Berna's friend do last month?", ["She moved away.", "She didn't come to Berna's birthday dinner.", "She borrowed money."], 1, "\"she didn't turn up to my birthday dinner\""),
        mc("What is Ayla's first piece of advice?", ["End the friendship.", "Don't jump to conclusions.", "Make new friends."], 1, "\"try not to jump to conclusions\""),
     ]},
    {"explanation": "**Phrasal verb mi, tek kelimelik fiil mi?**\n\nPhrasal verb'ler **günlük, samimi** dildir. Resmî yazıda (iş e-postası, rapor, makale) genellikle **Latin kökenli tek kelimelik** fiiller tercih edilir.\n\n| Phrasal verb (samimi) | Tek kelime (resmî) |\n|---|---|\n| put up with | **tolerate** |\n| turn down | **reject / decline** |\n| look after | **care for / take care of** |\n| find out | **discover** |\n| bring up (a topic) | **raise / mention** |\n| make up (with sb) | **reconcile** |\n| split up / break up | **separate** |\n| go through (a difficult time) | **experience** |\n| look up to | **admire** |\n| put off | **postpone** |\n\n**Örnek:**\n\n- Samimi: *I can't **put up with** my neighbour's noise.*\n- Resmî: *Residents should not have to **tolerate** excessive noise.*\n\n**Tavsiye köşesi cevabı nasıl yazılır?**\n\n1. **Empati:** *I'm sorry you're going through this.*\n2. **Durumu farklı açıdan görme:** *Your friend might be ...*\n3. **Somut adımlar:** *Call her up and ... / When you meet, ...*\n4. **Dengeli bir kapanış:** *If ..., it may be time to ...*",
     "examples": [{"en": "I'm sorry you're going through this.", "tr": "Bunu yaşadığın için üzgünüm."},
                  {"en": "The company rejected the proposal. (= turned it down)", "tr": "Şirket teklifi reddetti."},
                  {"en": "We had to postpone the meeting. (= put it off)", "tr": "Toplantıyı ertelemek zorunda kaldık."}],
     "turkishNote": "Türkçede resmî ve samimi dil arasındaki fark genellikle hitap ve fiil ekleriyle yapılır (\"yaparsınız\" / \"yaparsın\"). İngilizcede ise kelime seçimi önemlidir: Bir iş e-postasında \"We turned down your offer\" yerine \"We have decided to decline your offer\" yazmak çok daha profesyonel durur. Konuşmada ise tek kelimelik fiiller fazla resmî ve soğuk gelebilir."},
    [
        mc("Resmî bir e-postada:", ["We can't put up with these delays.", "We cannot tolerate these delays."], 1, "Resmî → tolerate."),
        mc("\"turn down\" resmî karşılığı:", ["decline", "discover"], 0, "decline / reject."),
        mc("\"find out\" resmî karşılığı:", ["discover", "admire"], 0, "discover."),
        mc("Arkadaşa mesajda en doğal:", ["I admire my grandfather greatly.", "I really look up to my grandad."], 1, "Samimi → phrasal verb."),
        gap("The meeting has been ___ until Friday. (put off = ertelendi, resmî)", ["postponed"], "postpone."),
        gap("I'd like to ___ an important issue. (bring up, resmî)", ["raise", "mention"], "raise / mention."),
        gap("I'm sorry you're going ___ this.", ["through"], "go through."),
        gap("Try not to jump ___ conclusions.", ["to"], "jump to conclusions."),
        listen("Thanks for your letter. I understand that you can't put up with your flatmate's mess any more. My advice is to bring it up calmly, maybe over dinner. Don't tell him off in front of others. And if things don't work out, it might be time to find a new flat.", "Tavsiyeye göre konu nasıl açılmalı?", ["Başkalarının önünde", "Sakin bir şekilde, belki akşam yemeğinde", "Mesajla"], 1, "\"bring it up calmly, maybe over dinner\""),
        typ("Resmîleştirin: \"The manager turned down my request.\"", variants("The manager rejected my request.", "The manager declined my request."), "The manager rejected my request."),
    ],
    {"kind": "writing", "task": write("Bir dergi tavsiye köşesine gelen aşağıdaki mektuba cevap yazın (150–200 kelime): \"I've been living with my flatmate for two years. We used to get on really well, but now he never tidies up, he brings friends home late at night, and he forgets to pay his share of the bills. I don't want to fall out with him, but I can't put up with it any more. Can.\" Empatiyle başlayın, en az 6 phrasal verb kullanın, somut adımlar önerin ve dengeli bir kapanış yapın.",
                                      "Dear Can,\n\nI'm sorry you're going through this. Sharing a flat with someone you used to get on with can be really hard when things start to change.\n\nFirst of all, don't let things build up any longer. The longer you put up with it, the angrier you'll become. Choose a calm moment and bring the problems up honestly, but don't tell him off. Start by asking if everything is OK with him. He might be going through a difficult time that you don't know about.\n\nThen be specific. Suggest a simple cleaning rota and agree on some house rules about guests on weeknights. For the bills, you could set up a shared account so neither of you has to remember.\n\nIf he makes an effort, great. You can stay friends and flatmates. But if he keeps letting you down, it might be time to look for a new place. A good friendship is worth more than a cheap flat.\n\nGood luck,\nAyla",
                                      ["Empatiyle giriş", "En az 6 phrasal verb ve doğru yapı", "Somut tavsiyeler", "Dengeli kapanış", "Samimi ama düzgün üslup"])},
)

u.test([
    mc("Hangisi doğru?", ["She turned down it.", "She turned it down."], 1, "Zamir ortada"),
    mc("Hangisi doğru?", ["He looks his little brother after.", "He looks after his little brother."], 1, "Ayrılamaz"),
    mc("\"Babama çekmişim.\"", ["I take after my dad.", "I look after my dad."], 0, "take after"),
    mc("\"Things didn't work out.\" ilişki bağlamında:", ["Spor yapmadılar.", "İlişki yürümedi."], 1, "work out"),
    mc("Resmî bir e-postada:", ["We have decided to decline your offer.", "We've decided to turn your offer down."], 0, "Resmî"),
    gap("I don't get on ___ my neighbour.", ["with"], "get on with"),
    gap("I can't put up ___ this noise any more.", ["with"], "put up with"),
    gap("He asked me out, but I turned ___ down.", ["him"], "Zamir ortada"),
    gap("We had an argument, but we made ___ the next day.", ["up"], "make up"),
    gap("It took him a year to get ___ the break-up.", ["over"], "get over"),
    mc("\"I ran into Ali yesterday.\"", ["Ali'ye çarptım.", "Ali'ye rastladım."], 1, "run into"),
    gap("I've always looked up ___ my grandmother.", ["to"], "look up to"),
    listen("Selin and I went out for four years. We split up last spring because we wanted different things. It was hard, but we've stayed friends. Last week, I ran into her at a concert, and we caught up for hours.", "Konuşan ve Selin şu an ne durumda?", ["Hâlâ çıkıyorlar", "Ayrıldılar ama arkadaşlar", "Hiç konuşmuyorlar"], 1, "\"we've stayed friends\""),
    typ("İngilizcesi: \"Bana her zaman güvenebilirsin.\" (count on)", variants("You can always count on me.", "You can always count on me!"), "You can always count on me."),
    write("Hayatınızda zaman içinde değişen bir ilişkiyi anlatın (bir arkadaşlık, bir aile bağı, bir iş ilişkisi) (150–200 kelime). En az 8 farklı phrasal verb kullanın: ayrılabilen (zamirle), ayrılamayan ve üç parçalı türlerden en az ikişer tane olsun.",
          "My cousin Kerem and I were brought up almost like brothers. We lived on the same street, and our mothers looked after us together while our fathers were at work. Everyone said I took after him, because we were both noisy and full of energy.\n\nWhen we were teenagers, though, we started to grow apart. He took up football and I took up music, and we had different friends. Then, at nineteen, we fell out badly. He borrowed my guitar and broke it, and he made up a silly story about how it happened. I told him off in front of the whole family, and we didn't speak for three years.\n\nI only got over it when I heard he was going through a hard time after losing his job. I called him up and asked if he wanted to meet. We caught up over dinner, apologised, and made up.\n\nToday, he's one of the people I can always count on. I've realised that I don't just love him. I look up to him, because he never lets down the people he loves.",
          ["En az 8 phrasal verb", "Ayrılabilen (zamirle)", "Ayrılamayan ve üç parçalı", "Değişimi anlatan yapı", "Akıcılık"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

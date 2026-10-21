"""C2 Ünite 6: Sokak dili."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("C2", 6, "Sokak dili", "Everyday Slang",
         "Hızlı konuşmadaki indirgenmiş biçimleri (gonna, wanna, dunno, didja) anlayabilir, İngiliz ve Amerikan argosunun yaygın kelimelerini tanıyabilir, mesajlaşma kısaltmalarını ve güncel internet dilini çözebilir, standart dışı dilbilgisi özelliklerini (ain't, innit, she was like) anlayıp bağlamını değerlendirebilir ve hangi ifadenin nerede uygun olduğuna karar verebilirim.",
         ["hızlı konuşmada indirgenmiş biçimler", "İngiliz ve Amerikan argosu", "mesajlaşma kısaltmaları ve internet dili", "standart dışı dilbilgisi: ain't, innit, be like", "argo ve üslup farkındalığı"],
         ["gençlik kültürü", "diziler ve filmler", "sosyal medya"],
         {"title": "Dizi sahnesini çöz", "durationMinutes": 45,
          "goal": "Öğretmen bir dizi ya da filmden (öğretmenin seçeceği, öğrenciler için uygun) argo ve hızlı konuşma içeren kısa bir sahne gösterir. Gruplar sahnedeki indirgenmiş biçimleri ve argo ifadeleri yazıya döker ve standart İngilizceye çevirir. Sonra gruplar aynı sahneyi önce standart İngilizceyle, sonra argo ile canlandırır ve hangi bağlamda hangisinin uygun olduğunu tartışır."})

u.vocab([
    ("slang", "argo", "Slang changes very quickly.", "Argo çok hızlı değişir.", None),
    ("gonna / wanna / gotta", "going to / want to / got to", "I'm gonna be late.", "Geç kalacağım.", "Sadece samimi konuşmada ve mesajlarda; resmî yazıda asla."),
    ("dunno", "don't know", "\"Where is he?\" \"Dunno.\"", "\"Nerede o?\" \"Bilmem.\"", None),
    ("mate", "kanka, dostum (BrE)", "Cheers, mate!", "Sağ ol, kanka!", None),
    ("dude", "dostum, adamım (AmE)", "Dude, that was amazing!", "Dostum, harikaydı!", None),
    ("knackered", "çok yorgun, bitkin (BrE)", "I'm absolutely knackered.", "Tamamen bittim.", None),
    ("gutted", "çok üzgün, hayal kırıklığına uğramış (BrE)", "I was gutted when we lost.", "Kaybettiğimizde yıkıldım.", None),
    ("quid", "sterlin (BrE)", "It cost me twenty quid.", "Bana yirmi sterline patladı.", "Çoğulu da quid: ✗ quids."),
    ("bucks", "dolar (AmE)", "Can you lend me ten bucks?", "Bana on dolar borç verebilir misin?", None),
    ("sorted", "halledildi (BrE)", "Don't worry, it's sorted.", "Merak etme, halloldu.", None),
    ("cheeky", "şımarık ama sevimli, yüzsüz (BrE)", "Fancy a cheeky coffee?", "Hadi bir kahve kaçamağı yapalım mı?", None),
    ("legit", "gerçek, sahiden (samimi)", "Is this website legit?", "Bu site güvenilir mi?", None),
    ("to ghost someone", "birini aniden yok saymak, cevap vermemek", "He ghosted me after our second date.", "İkinci buluşmamızdan sonra bana bir daha dönmedi.", None),
    ("lowkey", "biraz, gizliden (internet dili)", "I'm lowkey nervous about tomorrow.", "Yarın için biraz gerginim.", None),
    ("sus", "şüpheli (internet dili)", "That email looks sus.", "O e-posta şüpheli görünüyor.", None),
    ("cringe", "utandırıcı, rezil (internet dili)", "His dance moves were so cringe.", "Dansı çok utandırıcıydı.", None),
    ("vibe", "hava, enerji, atmosfer", "This café has a great vibe.", "Bu kafenin havası harika.", None),
    ("ain't", "am not / isn't / haven't (standart dışı)", "It ain't over yet.", "Daha bitmedi.", "Standart dışı; şarkılarda, filmlerde ve bazı lehçelerde yaygın."),
    ("innit", "değil mi? (Londra argosu)", "It's cold, innit?", "Soğuk, değil mi?", None),
    ("be like", "demek (alıntı, samimi)", "And she was like, \"No way!\"", "O da \"Yok artık!\" dedi.", None),
    ("tbh", "to be honest (dürüst olmak gerekirse)", "tbh I didn't like the film.", "Dürüst olmak gerekirse filmi beğenmedim.", None),
    ("ngl", "not gonna lie (yalan yok)", "ngl that was really good.", "Yalan yok, gerçekten iyiydi.", None),
    ("register awareness", "üslup farkındalığı", "Register awareness helps you choose the right words.", "Üslup farkındalığı doğru kelimeleri seçmenize yardım eder.", None),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Hızlı konuşmanın sesleri", "Hızlı ve samimi konuşmadaki indirgenmiş biçimleri (gonna, wanna, gotta, dunno, lemme, gimme, didja, whatcha) anlayabilir ve standart İngilizceye çevirebilirim.",
    {"kind": "dialogue", "title": "Kampüste", "lines": [
        {"speaker": "Jake", "text": "Hey! Whatcha doing later?"},
        {"speaker": "Mia", "text": "Dunno yet. Gotta finish my essay first. Why?"},
        {"speaker": "Jake", "text": "Wanna grab some food? There's this new place near the station."},
        {"speaker": "Mia", "text": "Ooh, sounds good. Lemme check my messages... OK, I'm free after seven."},
        {"speaker": "Jake", "text": "Cool. Didja hear about Sam, by the way?"},
        {"speaker": "Mia", "text": "No, what?"},
        {"speaker": "Jake", "text": "He's gonna move to Canada. Kinda crazy, right?"},
        {"speaker": "Mia", "text": "No way! Gimme a sec, I'm gonna text him right now."}],
     "questions": [
        mc("What does Mia have to do first?", ["Go to the station", "Finish her essay", "Call Sam"], 1, "\"Gotta finish my essay first.\""),
        mc("What news does Jake share?", ["Sam is moving to Canada.", "A new restaurant has closed.", "Mia passed her exam."], 0, "\"He's gonna move to Canada.\""),
     ]},
    {"explanation": "Hızlı ve samimi konuşmada kelimeler **birleşir** ve **kısalır**. Bu biçimler ders kitaplarında az yer alır ama dizilerde, filmlerde ve günlük konuşmada **çok yaygındır**.\n\n**Yaygın indirgenmiş biçimler:**\n\n| İndirgenmiş | Standart | Örnek |\n|---|---|---|\n| **gonna** | going to | *I'm **gonna** text him.* |\n| **wanna** | want to / want a | ***Wanna** grab some food?* |\n| **gotta** | (have) got to / got a | *I **gotta** go.* |\n| **dunno** | (I) don't know | ***Dunno** yet.* |\n| **kinda / sorta** | kind of / sort of | *That's **kinda** crazy.* |\n| **lemme** | let me | ***Lemme** check.* |\n| **gimme** | give me | ***Gimme** a sec.* |\n| **whatcha** | what are you / what have you | ***Whatcha** doing?* |\n| **didja** | did you | ***Didja** hear?* |\n| **ya** | you | *See **ya**!* |\n| **'cause / cos** | because | *I left **'cause** I was tired.* |\n| **outta** | out of | *Get **outta** here!* |\n| **lotta** | a lot of | *That's a **lotta** money.* |\n| **y'all** | you all (Güney ABD) | *Are **y'all** coming?* |\n\n**Önemli:**\n\n- **gonna** sadece \"gelecek\" anlamında: *I'm gonna call* (✓), ama *I'm going to London* → ✗ *I'm gonna London*.\n- Bu biçimleri **anlamak** her İngilizce konuşan için önemlidir. **Kullanmak** ise sadece **samimi** konuşma ve mesajlarda uygundur.\n- **Resmî yazıda, sınavlarda ve iş e-postalarında asla kullanmayın.**",
     "examples": [{"en": "I'm gonna be late. (= I'm going to be late.)", "tr": "Geç kalacağım."},
                  {"en": "Whatcha gonna do? (= What are you going to do?)", "tr": "Ne yapacaksın?"},
                  {"en": "Lemme know if you wanna come. (= Let me know if you want to come.)", "tr": "Gelmek istersen haber ver."}],
     "turkishNote": "Türkçede de hızlı konuşmada benzer kısalmalar olur: \"geliyorum\" → \"geliyom\", \"bilmiyorum\" → \"bilmiyom\", \"ne yapıyorsun\" → \"napıyon\". İngilizcedeki \"gonna\", \"wanna\", \"dunno\" da aynı mantıkla oluşur. Türk öğrencilerin İngilizce dizi izlerken en çok zorlandığı nokta bu biçimlerdir. Bunları tanımak dinleme becerinizi büyük ölçüde geliştirir. Ancak tıpkı Türkçede resmî bir dilekçeye \"napıyon\" yazmayacağınız gibi, İngilizce resmî yazıda da bu biçimleri kullanmayın."},
    [
        mc("\"Wanna come?\" standart hali:", ["Do you want to come?", "Will you come?"], 0, "wanna = want to."),
        mc("\"Dunno.\" standart hali:", ["I don't know.", "Don't go."], 0, "dunno."),
        mc("\"I gotta go.\" anlamı:", ["Gitmem lazım.", "Gidebilirim."], 0, "gotta = have got to."),
        mc("Nerede kullanılmaz?", ["Arkadaşa mesajda", "İş başvurusu mektubunda"], 1, "Resmî yazı."),
        gap("Standart: \"Lemme see.\" → ___ me see.", ["Let"], "let me."),
        gap("Standart: \"Gimme a minute.\" → ___ me a minute.", ["Give"], "give me."),
        gap("Standart: \"Whatcha doing?\" → What ___ you doing?", ["are"], "what are you."),
        gap("Standart: \"It's kinda cold.\" → It's ___ of cold.", ["kind"], "kind of."),
        listen("Hey, didja see the game last night? We're gonna watch the final at Tom's place on Saturday. Wanna come? Lemme know by Friday, 'cause he's gotta buy the snacks.", "Neden cumaya kadar haber vermek gerekiyor?", ["Tom'un atıştırmalık alması gerektiği için", "Maç cuma olduğu için", "Biletler tükeneceği için"], 0, "\"'cause he's gotta buy the snacks\""),
        typ("Standart İngilizceye çevirin: \"I dunno what I'm gonna do.\"", variants("I don't know what I'm going to do.", "I do not know what I am going to do.", "I don't know what I am going to do."), "I don't know what I'm going to do."),
    ],
    {"kind": "speaking", "task": speak("Aşağıdaki standart cümleleri, bir arkadaşınızla hızlı ve samimi konuşuyormuş gibi indirgenmiş biçimlerle sesli söyleyin, sonra her birinin ne zaman uygun olmayacağını tek cümleyle açıklayın: (1) What are you going to do this weekend? (2) I don't know. I have got to work on Saturday. (3) Do you want to get a coffee? (4) Let me check my calendar. (5) Give me a second.",
                                       "One: Whatcha gonna do this weekend? Two: Dunno. Gotta work on Saturday. Three: Wanna get a coffee? Four: Lemme check my calendar. Five: Gimme a sec. These forms are fine with friends or in casual messages, but I'd never use them in a job interview, a formal email or an exam essay, because they would sound careless and unprofessional.",
                                       ["Doğru indirgenmiş biçimler", "Doğal telaffuz", "Üslup farkındalığı", "Akıcılık"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "İngiliz ve Amerikan argosu", "Yaygın İngiliz (mate, knackered, gutted, quid, sorted) ve Amerikan (dude, bucks, awesome, beat, bummed) argo kelimelerini tanıyıp anlamlarını bağlamdan çıkarabilirim.",
    {"kind": "text", "title": "İki arkadaştan mesajlar", "body": "From Ollie (London):\n\"Alright mate? Totally knackered after work today. Gutted about the match, can't believe we lost! Fancy a cheeky pint on Friday? I'll sort the tickets for the gig. Only 15 quid each. Brilliant, innit?\"\n\nFrom Tyler (California):\n\"Hey dude! I'm so beat after work. Totally bummed about the game, can't believe we lost! Wanna hang out on Friday? I'll get the tickets for the show. Only 15 bucks each. Awesome, right?\"",
     "questions": [
        mc("How do both friends feel after work?", ["Very tired", "Excited", "Angry"], 0, "knackered / beat."),
        mc("How much are the tickets?", ["15 pounds / 15 dollars", "50 pounds / 50 dollars", "Free"], 0, "15 quid / 15 bucks."),
     ]},
    {"explanation": "**Aynı anlam, iki argo:**\n\n| Anlam | İngiliz (BrE) | Amerikan (AmE) |\n|---|---|---|\n| arkadaş, dostum | **mate** | **dude, buddy, bro** |\n| çok yorgun | **knackered, shattered** | **beat, wiped (out)** |\n| hayal kırıklığına uğramış | **gutted** | **bummed (out)** |\n| para birimi | **quid** (£) | **bucks** ($) |\n| harika | **brilliant, wicked, top** | **awesome, rad, sick** |\n| halletmek / halledildi | **sort (out) / sorted** | **figure out / handled** |\n| Selam, nasılsın? | **Alright? / You alright?** | **What's up? / Sup?** |\n| takılmak | **hang out** (her ikisi), **chill** | **hang out, chill** |\n| kızgın | **cross, fuming** | **mad** |\n\n**Tuzaklar!**\n\n| Kelime | BrE anlamı | AmE anlamı |\n|---|---|---|\n| **pants** | iç çamaşırı; kötü (*That film was pants.*) | pantolon |\n| **chips** | patates kızartması (AmE: *fries*) | cips (BrE: *crisps*) |\n\n**Not:** Bazı argo kelimeler bir ülkede masum, diğerinde kaba olabilir; emin değilseniz **nötr** kelimeyi seçin.\n\n**Cheeky (BrE):** Hem \"yüzsüz, şımarık\" (*Don't be cheeky!*) hem de \"küçük, keyifli bir kaçamak\" (*a cheeky coffee*) anlamına gelir.",
     "examples": [{"en": "I'm absolutely shattered. I'm going to bed.", "tr": "Tamamen bittim. Yatmaya gidiyorum."},
                  {"en": "That was a wicked concert!", "tr": "Harika bir konserdi!"},
                  {"en": "Don't worry about the car. It's all sorted.", "tr": "Araba için merak etme. Her şey halloldu."}],
     "turkishNote": "Türkçede de bölgesel ve kuşaksal argo farkları vardır (\"kanka\", \"moruk\", \"abi\"). İngilizcede İngiliz ve Amerikan argosu arasındaki fark çok büyüktür ve dizi izlerken bu farkı bilmek çok yardımcı olur. Türk öğrencilerin dikkat etmesi gereken önemli bir nokta, bazı kelimelerin iki ülkede farklı anlamlara gelmesidir. Örneğin İngiltere'de \"pants\" iç çamaşırıdır; bir İngiliz'e \"I like your pants\" demek komik bir duruma yol açabilir."},
    [
        mc("\"I'm knackered.\" anlamı:", ["Çok yorgunum.", "Çok mutluyum."], 0, "knackered."),
        mc("\"I was gutted.\" anlamı:", ["Çok üzüldüm / yıkıldım.", "Çok acıktım."], 0, "gutted."),
        mc("Amerikan argosunda \"çok yorgun\":", ["beat", "gutted"], 0, "beat."),
        mc("İngiltere'de \"pants\":", ["pantolon", "iç çamaşırı"], 1, "BrE pants."),
        gap("It only cost me five ___. (BrE: sterlin)", ["quid"], "quid."),
        gap("Can you lend me twenty ___? (AmE: dolar)", ["bucks"], "bucks."),
        gap("Cheers, ___! See you tomorrow. (BrE: kanka)", ["mate"], "mate."),
        gap("Don't worry, it's all ___. (BrE: halledildi)", ["sorted"], "sorted."),
        listen("Alright, mate? Listen, I'm totally shattered, so I'm not gonna make it tonight. Gutted, 'cause I really wanted to see the band. But I'll sort out tickets for the next gig, yeah?", "Konuşan neden bu akşam gelmiyor?", ["Çok yorgun olduğu için", "Parası olmadığı için", "Grubu sevmediği için"], 0, "\"I'm totally shattered\""),
        match([("mate", "dude"), ("knackered", "beat"), ("gutted", "bummed"), ("quid", "bucks"), ("brilliant", "awesome")], "Her İngiliz argo kelimesini Amerikan karşılığıyla eşleştirin."),
    ],
    {"kind": "speaking", "task": speak("Bir arkadaşınıza sesli mesaj bırakın (45 saniye): Bugün çok yorucu bir gün geçirdiniz, sevdiğiniz takım kaybetti ve hafta sonu için bir plan öneriyorsunuz. Mesajı iki kez söyleyin: (1) İngiliz argosuyla (mate, knackered, gutted, quid, sorted, brilliant) (2) Amerikan argosuyla (dude, beat, bummed, bucks, awesome).",
                                       "British version: Alright mate? I'm absolutely knackered. Work was mad today. And I'm gutted about the match. Can't believe we lost in the last minute! Anyway, fancy going to that food festival on Saturday? It's only ten quid to get in. I'll sort the train tickets. Brilliant, yeah? Text me back! American version: Hey dude! I'm so beat. Work was crazy today. And I'm totally bummed about the game. Can't believe we lost in the last minute! Anyway, wanna check out that food festival on Saturday? It's only ten bucks to get in. I'll get the train tickets. Awesome, right? Text me back!",
                                       ["İngiliz argosu", "Amerikan argosu", "Doğal ve samimi ton", "Telaffuz"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "Mesajlaşma ve internet dili", "Yaygın mesajlaşma kısaltmalarını (tbh, ngl, idk, imo, btw, brb, fyi) ve güncel internet dilini (lowkey, sus, cringe, ghost, vibe, flex) anlayabilir ve bunların ne kadar çabuk eskiyebildiğinin farkında olabilirim.",
    {"kind": "dialogue", "title": "Grup sohbeti", "lines": [
        {"speaker": "Zara", "text": "omg did u see Leo's post?? 😂"},
        {"speaker": "Ben", "text": "lol yes. ngl his dance was kinda cringe"},
        {"speaker": "Zara", "text": "tbh I lowkey loved it. the vibe was immaculate ✨"},
        {"speaker": "Ben", "text": "fair. btw did Ella ever reply to u?"},
        {"speaker": "Zara", "text": "nope. she totally ghosted me 🙄"},
        {"speaker": "Ben", "text": "that's sus. idk what's going on with her"},
        {"speaker": "Zara", "text": "imo she's just busy with exams. anyway brb, mum's calling"},
        {"speaker": "Ben", "text": "np, ttyl 👋"}],
     "questions": [
        mc("What does Zara think of Leo's dance?", ["She hated it.", "She secretly loved it.", "She didn't see it."], 1, "\"I lowkey loved it\""),
        mc("Why does Zara think Ella hasn't replied?", ["She is angry.", "She is probably busy with exams.", "She lost her phone."], 1, "\"imo she's just busy with exams\""),
     ]},
    {"explanation": "**1. Mesajlaşma kısaltmaları:**\n\n| Kısaltma | Açılımı | Türkçe |\n|---|---|---|\n| **lol** | laughing out loud | çok komik (genelde sadece gülümseme) |\n| **omg** | oh my God | aman Tanrım |\n| **tbh** | to be honest | dürüst olmak gerekirse |\n| **ngl** | not gonna lie | yalan yok |\n| **idk** | I don't know | bilmiyorum |\n| **imo / imho** | in my (humble) opinion | bence |\n| **btw** | by the way | bu arada |\n| **fyi** | for your information | bilgin olsun |\n| **brb** | be right back | hemen geliyorum |\n| **ttyl** | talk to you later | sonra konuşuruz |\n| **np** | no problem | sorun değil |\n| **irl** | in real life | gerçek hayatta |\n| **smh** | shaking my head | (hayal kırıklığı) |\n| **u / r / ur** | you / are / your | sen / -sin / senin |\n\n**2. Güncel internet dili (2010'lar–2020'ler):**\n\n| İfade | Anlam |\n|---|---|\n| **lowkey / highkey** | biraz, gizliden / açıkça, çok |\n| **sus** | şüpheli (*suspicious*) |\n| **cringe** | utandırıcı |\n| **ghost (someone)** | birine aniden cevap vermeyi bırakmak |\n| **vibe** | hava, atmosfer, enerji |\n| **flex** | hava atmak, gösteriş yapmak |\n| **salty** | küskün, alıngan |\n| **spill the tea** | dedikoduyu anlat |\n| **no cap** | yalan yok, gerçekten |\n| **slay** | harika yapmak |\n\n**Dikkat:**\n\n- İnternet dili **çok hızlı eskir**. Bugün popüler olan bir ifade birkaç yıl sonra **eski moda** hatta **komik** görünebilir.\n- Yaşınıza ve ortama uymayan argo kullanmak **zorlama** görünebilir.\n- Bu kelimeleri **anlamak** önemlidir; kullanmak ise tamamen **isteğe bağlıdır**.\n- **fyi** iş e-postalarında da kullanılabilir; diğerleri genellikle sadece samimi mesajlarda.",
     "examples": [{"en": "tbh I'm not sure about this plan.", "tr": "Dürüst olmak gerekirse bu plandan emin değilim."},
                  {"en": "He keeps flexing his new car on Instagram.", "tr": "Instagram'da sürekli yeni arabasıyla hava atıyor."},
                  {"en": "FYI, the meeting has moved to 3 p.m.", "tr": "Bilginize, toplantı saat 3'e alındı."}],
     "turkishNote": "Türkçe mesajlaşmada da \"slm\", \"nbr\", \"tmm\", \"bşk\" gibi kısaltmalar ve gençler arasında hızla değişen ifadeler vardır. İngilizce internet dili de aynı şekilde çok hızlı değişir. Türk öğrenciler için en önemli nokta, bu ifadeleri sosyal medyada ve dizilerde gördüklerinde anlayabilmektir. Kullanırken ise dikkatli olun: Yanlış bağlamda ya da yaşınıza uymayan bir argo kelime kullanmak, istediğinizin tam tersi bir etki yaratabilir."},
    [
        mc("\"tbh\" anlamı:", ["to be honest", "to be happy"], 0, "tbh."),
        mc("\"brb\" anlamı:", ["Hemen geliyorum.", "Çok komik."], 0, "be right back."),
        mc("\"That's sus.\" anlamı:", ["Bu şüpheli.", "Bu harika."], 0, "sus."),
        mc("\"She ghosted me.\" anlamı:", ["Beni korkuttu.", "Bana aniden cevap vermeyi bıraktı."], 1, "ghost."),
        gap("___, the deadline is Friday. (Bilgin olsun, iş e-postasında da kullanılabilir)", ["FYI", "fyi"], "FYI."),
        gap("I ___ don't want to go, but I'll go anyway. (biraz, gizliden)", ["lowkey"], "lowkey."),
        gap("This café has such a good ___. (atmosfer)", ["vibe"], "vibe."),
        gap("Stop ___ing your new phone! (hava atmak)", ["flex"], "flexing."),
        listen("OK, so, ngl, the party was kinda cringe at first. Nobody was dancing. But then the DJ played some old songs, and honestly, the vibe changed completely. No cap, it was the best night of the year.", "Konuşan partiyi sonunda nasıl buldu?", ["Çok kötü", "Yılın en iyi gecesi", "Sıkıcı"], 1, "\"the best night of the year\""),
        match([("idk", "I don't know"), ("imo", "in my opinion"), ("btw", "by the way"), ("ttyl", "talk to you later"), ("irl", "in real life")], "Her kısaltmayı açılımıyla eşleştirin."),
    ],
    {"kind": "speaking", "task": speak("Aşağıdaki samimi mesajları sesli olarak \"çevirin\": Önce mesajı standart İngilizceyle okuyun, sonra Türkçe karşılığını söyleyin ve son olarak bu mesajın kime gönderilmesinin uygun olmayacağını açıklayın. (1) \"omg ngl that film was lowkey amazing\" (2) \"idk tbh, imo we shd wait\" (3) \"brb, ttyl\" (4) \"he ghosted me, so sus\"",
                                       "One: Oh my God, not going to lie, that film was actually quite amazing. In Turkish: Aman Tanrım, yalan yok, o film gizliden harikaydı. I wouldn't send this to my manager or a teacher. Two: I don't know, to be honest. In my opinion, we should wait. Bilmiyorum açıkçası, bence beklemeliyiz. It's fine for friends, but in a work chat I'd write the full sentence. Three: Be right back, talk to you later. Hemen geliyorum, sonra konuşuruz. Fine for friends, not for a formal email. Four: He stopped replying to me without any explanation, which is very suspicious. Bana aniden cevap vermeyi bıraktı, çok şüpheli. This is very informal and only for close friends.",
                                       ["Doğru açılımlar", "Doğru Türkçe karşılıklar", "Üslup farkındalığı", "Akıcılık"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Standart dışı dilbilgisi", "Konuşmada sık duyulan standart dışı yapıları (ain't, innit, double negative, be like / go alıntıları, me and him went) anlayıp standart İngilizceye çevirebilir ve bunların sosyal ve bölgesel bağlamını değerlendirebilirim.",
    {"kind": "dialogue", "title": "Bir dizi sahnesinden (kurgusal)", "lines": [
        {"speaker": "Danny", "text": "So me and Jordan went to the party last night, right?"},
        {"speaker": "Kai", "text": "Yeah?"},
        {"speaker": "Danny", "text": "And this guy comes up to us and goes, \"You ain't on the list.\""},
        {"speaker": "Kai", "text": "No way."},
        {"speaker": "Danny", "text": "And I was like, \"Mate, we've been invited!\" And he was all, \"I don't know nothing about that.\""},
        {"speaker": "Kai", "text": "That's well annoying, innit?"},
        {"speaker": "Danny", "text": "Tell me about it. Anyway, we ain't going back there, that's for sure."}],
     "questions": [
        mc("What did the man at the door say?", ["That Danny and Jordan were not on the list", "That the party was cancelled", "That they were late"], 0, "\"You ain't on the list.\""),
        mc("Will Danny go back to that place?", ["Yes, next week", "No"], 1, "\"we ain't going back there\""),
     ]},
    {"explanation": "Gerçek hayatta, dizilerde ve şarkılarda **standart dışı** (non-standard) dilbilgisi yapıları çok sık duyulur. Bunlar \"yanlış\" değil, **bölgesel**, **sosyal** ya da **samimi** konuşma biçimleridir. Ancak **sınavlarda ve resmî yazıda** kullanılmazlar.\n\n**1. Yaygın standart dışı yapılar:**\n\n| Standart dışı | Standart | Not |\n|---|---|---|\n| **ain't** | am not / isn't / aren't / haven't / hasn't | *You **ain't** on the list.* = You aren't on the list. |\n| **innit** | isn't it? (her zamana uyan soru eki) | *That's annoying, **innit**?* (Londra) |\n| **double negative** | tek olumsuz | *I don't know **nothing**.* = I don't know **anything**. |\n| **me and him went** | he and I went | konuşmada çok yaygın |\n| **well + sıfat** (BrE) | very | *That's **well** annoying.* |\n| **them + isim** | those | *Look at **them** shoes.* |\n| **was** (çoğulla) | were | *We **was** there.* |\n\n**2. Alıntı fiilleri (quotatives):** Gençler arasında, hikâye anlatırken birinin ne dediğini aktarmak için:\n\n| Yapı | Örnek | Standart |\n|---|---|---|\n| **be like** | *I **was like**, \"Mate, we've been invited!\"* | I said, ... |\n| **go** (şimdiki zamanda anlatım) | *This guy **comes up** and **goes**, \"...\"* | He said, ... |\n| **be all** (AmE) | *He **was all**, \"I don't know.\"* | He said, ... |\n\n**3. Anlatı şimdiki zamanı (narrative present):** Samimi hikâye anlatımında geçmiş olaylar için **şimdiki zaman**: *So **this guy comes up** to us and **goes** ...* Bu, hikâyeyi canlı ve dramatik yapar.\n\n**Tutum:** Dilbilimciler bu yapıları **eksik** değil, **farklı** dil çeşitleri olarak görür. Kimseyi konuşma biçimine göre yargılamayın. Ama kendi yazınızda, **ortama uygun** olanı seçin.",
     "examples": [{"en": "\"I ain't got no money.\" (= I haven't got any money.)", "tr": "\"Hiç param yok.\""},
                  {"en": "\"And she was like, 'Seriously?'\" (= And she said, 'Seriously?')", "tr": "\"O da 'Ciddi misin?' dedi.\""},
                  {"en": "\"It's well good, innit?\" (= It's very good, isn't it?)", "tr": "\"Çok iyi, değil mi?\""}],
     "turkishNote": "Türkçede de standart dışı ve bölgesel yapılar vardır (\"geliyon mu\", \"gideceğiz\" yerine \"gidicez\", yöresel ağızlar). İngilizcede \"ain't\" ve double negative özellikle şarkılarda ve filmlerde çok yaygındır; bunları anlamak dinleme becerinizi güçlendirir. Türk öğrenciler için önemli bir nokta: Bu yapıları duyduğunuzda \"yanlış İngilizce\" diye düşünmeyin; konuşanın bölgesel ya da sosyal kimliğinin bir parçasıdır. Ama sınavlarda ve iş yazışmalarında her zaman standart biçimleri kullanın."},
    [
        mc("\"I ain't hungry.\" standart hali:", ["I'm not hungry.", "I haven't hungry."], 0, "ain't = am not."),
        mc("\"I don't know nothing.\" standart hali:", ["I don't know anything.", "I know nothing about nothing."], 0, "Double negative."),
        mc("\"And she was like, 'No way!'\" anlamı:", ["Ona benziyordu.", "\"Olamaz!\" dedi."], 1, "be like = say."),
        mc("Bu yapılar nerede kullanılmaz?", ["Bir dizi diyaloğunda", "Bir sınav kompozisyonunda"], 1, "Standart yazı."),
        gap("Standart: \"It's cold, innit?\" → It's cold, ___ it?", ["isn't"], "isn't it."),
        gap("Standart: \"We ain't finished yet.\" → We ___ finished yet.", ["haven't"], "ain't = haven't."),
        gap("Standart: \"Me and Ali went to the cinema.\" → Ali and ___ went to the cinema.", ["I"], "Ali and I."),
        gap("Standart: \"That's well funny.\" → That's ___ funny.", ["very", "really"], "well = very."),
        listen("So I'm at the bus stop, right, and this woman comes up to me and goes, \"Is this the bus to the airport?\" And I'm like, \"No, it ain't, you need the number seven.\" And she was all, \"Oh my God, thank you so much!\"", "Kadın hangi otobüse binmeliydi?", ["Havalimanı otobüsü olan yedi numara", "Duraktaki ilk otobüs", "Taksi"], 0, "\"you need the number seven\""),
        typ("Standart İngilizceye çevirin: \"I ain't seen nobody.\"", variants("I haven't seen anybody.", "I haven't seen anyone.", "I have not seen anybody.", "I have not seen anyone."), "I haven't seen anybody."),
    ],
    {"kind": "speaking", "task": speak("Başınıza gelen komik ya da ilginç bir olayı bir arkadaşınıza anlatır gibi iki kez anlatın (her biri 30–45 saniye): (1) Samimi ve gençlik dilinde: anlatı şimdiki zamanı (So I'm walking ..., this guy comes up ...), alıntı fiilleri (go, be like), indirgenmiş biçimler ve argo. (2) Aynı hikâyeyi standart ve nötr İngilizceyle, geçmiş zaman ve said / asked kullanarak.",
                                       "Informal: OK, so I'm at the supermarket, right? And I'm in a massive rush. This old guy comes up to me and goes, \"Excuse me, can you reach that jar for me?\" And I'm like, \"Sure, no problem.\" But then he goes, \"And the one next to it. And that one.\" And I was like, seriously? I was there for, like, twenty minutes! But he was well sweet, though. He even gave me a chocolate bar. Standard: Last week, I was at the supermarket, and I was in a hurry. An elderly man came up to me and asked if I could reach a jar for him. I said that it was no problem. However, he then asked me to reach several more items, so I ended up staying for about twenty minutes. He was very kind, though, and he even gave me a chocolate bar to thank me.",
                                       ["Anlatı şimdiki zamanı ve alıntı fiilleri", "Standart versiyon", "İki üslup arasında net fark", "Doğal anlatım"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Argo ve üslup farkındalığı", "Aynı içeriği samimi argo ile ve standart / nötr İngilizceyle yazabilir, bir metindeki argoyu doğru yorumlayabilir ve hangi ortamda hangi dilin uygun olduğuna bilinçli karar verebilirim.",
    {"kind": "text", "title": "Bir mesaj ve bir e-posta", "body": "Message to a friend:\n\"omg so I'm gonna be late tmrw 🙈 my train got cancelled AGAIN. legit the worst. can u lemme know what I missed? btw the new boss is lowkey scary ngl 😬 ttyl!\"\n\nEmail to a manager:\n\"Dear Ms Özkan,\nI'm afraid I'll be late tomorrow morning, as my train has been cancelled. I expect to arrive at around 10 a.m. Could you please let me know if there is anything important I should catch up on?\nThank you for your understanding.\nBest regards,\nArda\"",
     "questions": [
        mc("Why will Arda be late?", ["Arda overslept.", "Arda's train was cancelled.", "Arda is ill."], 1, "\"my train got cancelled\" / \"my train has been cancelled\""),
        mc("What information appears only in the email?", ["The expected arrival time", "That the train was cancelled"], 0, "\"I expect to arrive at around 10 a.m.\""),
     ]},
    {"explanation": "C2 seviyesinde amaç, argo kullanmak değil, **ne zaman ve nerede kullanılacağını** bilmektir. Bu, C1 Ünite 9'daki **üslup** (register) bilgisinin en uç noktasıdır.\n\n**Mesaj ve e-posta karşılaştırması:**\n\n| Özellik | Arkadaşa mesaj | Yöneticiye e-posta |\n|---|---|---|\n| **Hitap** | yok | *Dear Ms Özkan,* |\n| **İndirgenmiş biçimler** | *gonna, lemme* | yok |\n| **Kısaltmalar** | *omg, tmrw, btw, ngl, ttyl, u* | yok |\n| **Argo** | *legit, lowkey* | yok |\n| **Emojiler** | 🙈 😬 | yok |\n| **Büyük harf** | vurgu için: *AGAIN* | standart |\n| **Bilgi** | duygu odaklı | olgu odaklı (varış saati) |\n| **Kapanış** | *ttyl!* | *Best regards,* |\n\n**Argo kullanırken kendinize sorun:**\n\n1. **Kime** yazıyorum / konuşuyorum? (arkadaş, aile, iş, öğretmen, yabancı)\n2. **Nerede?** (özel mesaj, sosyal medya, iş, okul)\n3. **Karşımdaki** bu dili kullanıyor mu? (Ayna etkisi: karşınızdakinin üslubuna uyun)\n4. Bu ifade **güncel** mi, **eskimiş** mi, ya da **kaba** olabilir mi?\n5. **Yanlış anlaşılma** riski var mı? (BrE / AmE farkları)\n\n**Altın kural:** Emin değilseniz, **nötr** dil her zaman güvenlidir.\n\n**Çift yönlü beceri:** Argoyu **anlamak** (dizi, film, sosyal medya, arkadaşlar) ile argoyu **kullanmak** farklı becerilerdir. C2 seviyesindeki bir konuşmacı her ikisini de yapabilir, ama ikincisini **bilinçli** ve **seçici** yapar.",
     "examples": [{"en": "Informal: legit the worst. (= It's genuinely the worst thing.)", "tr": "Samimi: Gerçekten en kötüsü."},
                  {"en": "Neutral: I'm afraid I'll be late tomorrow.", "tr": "Nötr: Maalesef yarın geç kalacağım."},
                  {"en": "If in doubt, use neutral language.", "tr": "Emin değilsen nötr dil kullan."}],
     "turkishNote": "Türk öğrenciler İngilizce öğrenirken genellikle iki uç arasında kalır: Ya çok kitabi ve resmî konuşur ya da dizilerden öğrendiği argoyu her ortamda kullanır. İkisi de doğal görünmez. Tıpkı Türkçede yöneticinize \"Abi napıyon\" yazmayacağınız ama arkadaşınıza \"Sayın arkadaşım\" diye hitap etmeyeceğiniz gibi, İngilizcede de üslubu ortama göre ayarlamak gerekir. Ayna etkisi iyi bir stratejidir: Karşınızdaki kişi nasıl yazıyorsa, ona yakın bir üslupla cevap verin."},
    [
        mc("Yöneticiye e-postada uygun:", ["I'm gonna be late tmrw.", "I'm afraid I'll be late tomorrow."], 1, "Nötr."),
        mc("Arkadaşa mesajda doğal:", ["Dear Ali, I hope this message finds you well.", "hey! u free tonight?"], 1, "Samimi."),
        mc("Emin değilseniz:", ["En güncel argoyu kullanın.", "Nötr dil kullanın."], 1, "Altın kural."),
        mc("\"Ayna etkisi\" nedir?", ["Karşınızdakinin üslubuna yakın yazmak", "Her zaman resmî yazmak"], 0, "Mirroring."),
        gap("Nötr: \"Could you please let me ___ what I missed?\" (= lemme know)", ["know"], "let me know."),
        gap("Nötr: \"I'm ___ I'll be late.\" (maalesef)", ["afraid"], "I'm afraid."),
        gap("Nötr: \"___ the way, the new manager seems quite strict.\" (= btw)", ["By"], "By the way."),
        gap("Nötr: \"To be ___, I didn't enjoy the film.\" (= tbh)", ["honest"], "To be honest."),
        listen("Hey, it's me. So, the interview was legit amazing. Like, they were super chill, and I think they lowkey liked me. Gonna find out on Friday. Fingers crossed! Call me back, yeah?", "Konuşanın görüşme hakkındaki düşüncesi nedir?", ["Çok kötü geçti.", "Çok iyi geçti ve beğenildiğini düşünüyor.", "Henüz görüşmeye gitmedi."], 1, "\"legit amazing ... they lowkey liked me\""),
        typ("Nötr İngilizceye çevirin: \"ngl the meeting was kinda boring\" (To be honest, ...)", variants("To be honest, the meeting was quite boring.", "To be honest, the meeting was rather boring.", "To be honest, the meeting was a bit boring.", "To be honest, the meeting was somewhat boring.", "To be honest the meeting was quite boring."), "To be honest, the meeting was quite boring."),
    ],
    {"kind": "writing", "task": write("Aşağıdaki durumu üç farklı üslupta yazın: Bir konsere ya da etkinliğe gidemeyeceksiniz çünkü hastalandınız ve biletinizi başkasına vermek istiyorsunuz. (A) Yakın bir arkadaşınıza mesaj (30–50 kelime): indirgenmiş biçimler, kısaltmalar, argo ve emoji kullanın. (B) Bir iş arkadaşınıza nötr bir mesaj (50–70 kelime). (C) Etkinliği düzenleyen şirkete resmî bir e-posta (80–110 kelime): bileti başkasına devretmek için izin isteyin. Sonra 2–3 cümleyle üç metin arasındaki dil farklarını açıklayın.",
                                      "(A) Message to a close friend:\n\"omg I'm sooo gutted 😭 got a horrible cold and can't go tonight. legit can't stop sneezing lol. u wanna take my ticket?? it's free obvs. lemme know asap and I'll send it over 🎟️\"\n\n(B) Message to a colleague:\n\"Hi Emre, unfortunately I've come down with a bad cold, so I won't be able to make it to the concert tonight. I've got a spare ticket now, and I thought you might like it. It's completely free. Just let me know by five o'clock, and I'll email it to you. Hope you can use it!\"\n\n(C) Formal email to the organiser:\n\"Dear Sir or Madam,\nI have a ticket for this evening's concert (booking reference 48812). Unfortunately, due to illness, I am no longer able to attend. I would like to transfer my ticket to a colleague, Mr Emre Şahin, and I would be grateful if you could confirm whether this is possible. If so, please let me know what information you require.\nThank you in advance for your assistance.\nYours faithfully,\nCan Polat\"\n\nComparison:\nThe message to my friend uses slang (gutted, legit), abbreviations (lol, obvs, asap), reduced forms (wanna, lemme) and emojis. The colleague message is friendly but uses standard English. The formal email uses full forms, a booking reference, formal phrases such as \"I would be grateful if\" and a standard opening and closing.",
                                      ["Üç net üslup", "(A) Doğal argo ve kısaltmalar", "(B) Nötr ve samimi", "(C) Resmî kalıplar", "Karşılaştırma analizi"])},
)

u.test([
    mc("\"Wanna go?\" standart hali:", ["Do you want to go?", "Will you go?"], 0, "wanna"),
    mc("\"I'm knackered.\" (BrE)", ["Çok yorgunum.", "Çok kızgınım."], 0, "knackered"),
    mc("Amerikan argosunda \"dolar\":", ["quid", "bucks"], 1, "bucks"),
    mc("\"tbh\" anlamı:", ["to be honest", "to be happy"], 0, "tbh"),
    mc("\"I don't know nothing.\" standart hali:", ["I don't know anything.", "I know something."], 0, "Double negative"),
    gap("Standart: \"Lemme help you.\" → ___ me help you.", ["Let"], "let me"),
    gap("Standart: \"I dunno.\" → I don't ___.", ["know"], "don't know"),
    gap("Cheers, ___! (BrE: kanka)", ["mate"], "mate"),
    gap("I was ___ when we lost the final. (BrE: yıkıldım)", ["gutted"], "gutted"),
    gap("She totally ___ me. She never replied. (cevap vermemek)", ["ghosted"], "ghosted"),
    gap("Standart: \"It's cold, innit?\" → It's cold, ___ it?", ["isn't"], "innit = isn't it"),
    gap("Nötr: \"___ the way, the meeting is at three.\" (= btw)", ["By"], "By the way"),
    listen("So I'm in the café, right, and this guy comes up and goes, \"Is anyone sitting here?\" And I'm like, \"Nah, go ahead.\" Turns out he was, like, a famous actor. I was well shocked, ngl.", "Kafedeki adam kimdi?", ["Konuşanın öğretmeni", "Ünlü bir oyuncu", "Garson"], 1, "\"he was, like, a famous actor\""),
    typ("Standart İngilizceye çevirin: \"We ain't gonna make it.\"", variants("We aren't going to make it.", "We are not going to make it.", "We're not going to make it."), "We aren't going to make it."),
    write("Aşağıdaki durumu iki farklı üslupta yazın ve karşılaştırın: Bir hafta sonu gezisine çıktınız ve harika vakit geçirdiniz, ama dönüşte uçuşunuz iptal oldu. (A) Sosyal medyada ya da yakın arkadaş grubuna samimi bir paylaşım (60–80 kelime): indirgenmiş biçimler, argo, mesajlaşma kısaltmaları ve emoji kullanın. (B) Havayoluna tazminat talep eden resmî bir e-posta (100–130 kelime): standart ve resmî İngilizce, kesin ayrıntılar ve net bir talep. Sonra 2–3 cümleyle iki metin arasındaki dil farklarını açıklayın.",
          "(A) Group chat:\n\"ok so Lisbon was legit AMAZING 😍 the food, the views, the vibe... no cap best weekend ever. BUT then our flight home got cancelled 🙄 like, seriously?? we were stuck at the airport for 6 hrs and nobody told us anything. so done with this airline smh. anyway, home now, totally knackered. ttyl! 😴\"\n\n(B) Formal email to the airline:\n\"Dear Sir or Madam,\nI am writing regarding flight number 1758 from Lisbon to Istanbul on 14 October (booking reference QX7P2L), which was cancelled shortly before departure.\nAs a result, my partner and I were required to wait at the airport for six hours before being transferred to a later flight. During this time, we received very little information from your staff.\nI would therefore be grateful if you could consider our claim for compensation and reimburse the cost of the meals we purchased at the airport. I have attached copies of our boarding passes and receipts.\nI look forward to your reply.\nYours faithfully,\nDeniz Arslan\"\n\nComparison:\nThe group chat uses slang (legit, no cap, vibe, knackered), abbreviations (hrs, smh, ttyl), emojis and capital letters for emotion. The email avoids all of these and uses full forms, precise details such as the flight number and booking reference, and formal phrases such as \"I would therefore be grateful if\".",
          ["İki net üslup", "(A) Doğal argo ve kısaltmalar", "(B) Resmî dil ve kesin ayrıntılar", "Net talep", "Karşılaştırma analizi"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

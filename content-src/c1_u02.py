"""C1 Ünite 2: Sunumlar."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("C1", 2, "Sunumlar", "Presentations",
         "Cleft sentence'larla (It was ... that, What I need is ...) bir bilgiyi öne çıkarabilir, sunum yaparken yönlendirme ifadeleriyle dinleyiciyi yönetebilir, görselleri anlatabilir, soruları profesyonelce cevaplayabilir ve etkili bir sunum metni hazırlayabilirim.",
         ["It-cleft: It was ... that / who", "Wh-cleft: What I need is ... / What happened was ...", "All ... is / The reason ... is that / The thing that", "sunum yönlendirme dili (signposting)", "görselleri anlatma ve soru-cevap"],
         ["iş sunumları", "proje ve fikir sunma", "dinleyiciyle etkileşim"],
         {"title": "Üç dakikada fikrim", "durationMinutes": 45,
          "goal": "Her öğrenci okulunu, işini ya da şehrini iyileştirecek bir fikri 3 dakikalık bir sunumla anlatır. Sunumda en az 3 cleft sentence (What we need is..., It's not money that..., The reason why...) ve açık yönlendirme ifadeleri kullanır. Ardından sınıftan iki soru alır ve kalıplarla cevaplar. Sınıf en ikna edici sunumu oylar."})

u.vocab([
    ("presentation", "sunum", "I have to give a presentation tomorrow.", "Yarın bir sunum yapmam gerekiyor.", "give / deliver a presentation"),
    ("audience", "dinleyici kitlesi", "Know your audience before you speak.", "Konuşmadan önce dinleyicini tanı.", None),
    ("outline", "ana hatlar; ana hatlarıyla anlatmak", "Let me outline the main points.", "Ana noktaları özetleyeyim.", None),
    ("move on (to)", "(bir sonraki konuya) geçmek", "Let's move on to the next slide.", "Bir sonraki slayta geçelim.", None),
    ("highlight", "vurgulamak, öne çıkarmak", "I'd like to highlight three key points.", "Üç önemli noktayı vurgulamak istiyorum.", None),
    ("key", "temel, kilit", "The key issue is cost.", "Temel sorun maliyet.", None),
    ("slide", "slayt", "As you can see on this slide, ...", "Bu slaytta gördüğünüz gibi ...", None),
    ("chart", "grafik, çizelge", "This chart shows our sales.", "Bu grafik satışlarımızı gösteriyor.", None),
    ("figure", "rakam; şekil", "The figures speak for themselves.", "Rakamlar kendileri konuşuyor.", None),
    ("illustrate", "örneklemek, göstermek", "Let me illustrate this with an example.", "Bunu bir örnekle açıklayayım.", None),
    ("summarise", "özetlemek", "To summarise, ...", "Özetlemek gerekirse ...", "AmE: summarize"),
    ("conclude", "sonuçlandırmak", "I'd like to conclude by thanking you all.", "Hepinize teşekkür ederek bitirmek istiyorum.", None),
    ("digress", "konudan sapmak", "Sorry, I'm digressing.", "Pardon, konudan sapıyorum.", None),
    ("elaborate (on)", "ayrıntılandırmak", "Could you elaborate on that point?", "O noktayı biraz açar mısınız?", None),
    ("clarify", "açıklığa kavuşturmak", "Let me clarify what I mean.", "Ne demek istediğimi açıklayayım.", None),
    ("handout", "dağıtılan belge", "You'll find the details in your handout.", "Ayrıntıları dağıtılan belgede bulacaksınız.", None),
    ("nervous", "gergin", "Everyone feels nervous before a presentation.", "Herkes sunumdan önce gergin hisseder.", None),
    ("rehearse", "prova yapmak", "Rehearse your presentation several times.", "Sununu birkaç kez prova et.", None),
    ("engage", "ilgisini çekmek, katılımını sağlamak", "A good story engages the audience.", "İyi bir hikâye dinleyicinin ilgisini çeker.", None),
    ("pitch", "(fikir/ürün) sunumu, satış konuşması", "She made a great pitch to investors.", "Yatırımcılara harika bir sunum yaptı.", None),
    ("stakeholder", "paydaş", "We need to inform all stakeholders.", "Tüm paydaşları bilgilendirmemiz gerek.", None),
    ("in a nutshell", "kısacası", "In a nutshell, we need more time.", "Kısacası daha fazla zamana ihtiyacımız var.", None),
    ("bear in mind", "akılda tutmak", "Bear in mind that the budget is limited.", "Bütçenin sınırlı olduğunu aklınızda tutun.", None),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Asıl önemli olan", "It-cleft (It was ... that / who) yapısıyla bir bilgiyi öne çıkarabilir ve bir yanlış anlamayı düzeltebilirim.",
    {"kind": "dialogue", "title": "Proje toplantısı", "lines": [
        {"speaker": "Director", "text": "So the project was late because the design team didn't finish on time?"},
        {"speaker": "Okan", "text": "Actually, it wasn't the design team that caused the delay. It was the supplier who sent the wrong materials."},
        {"speaker": "Director", "text": "I see. And when did you find out?"},
        {"speaker": "Okan", "text": "It was only last Thursday that we discovered the problem."},
        {"speaker": "Director", "text": "So it's not more people that we need, it's a better supplier."},
        {"speaker": "Okan", "text": "Exactly. And it was Gizem who found a new supplier in just two days."}],
     "questions": [
        mc("What caused the delay?", ["The design team", "The supplier sent the wrong materials.", "There weren't enough people."], 1, "\"It was the supplier who sent the wrong materials.\""),
        mc("Who found a new supplier?", ["Okan", "The director", "Gizem"], 2, "\"it was Gizem who found a new supplier\""),
     ]},
    {"explanation": "**Cleft sentence** (\"bölünmüş cümle\"), bir cümleyi ikiye bölerek **bir bilgiyi öne çıkarır**.\n\n**It + be + [vurgulanan kısım] + that / who + [cümlenin geri kalanı]**\n\n**Normal cümle:** *The supplier caused the delay last week.*\n\n| Vurgulanan | It-cleft |\n|---|---|\n| Kim? | **It was the supplier that / who** caused the delay. |\n| Ne? | **It was the delay that** worried us. |\n| Ne zaman? | **It was last week that** the delay happened. |\n| Nerede? | **It was in Izmir that** we met. |\n| Neden? | **It was because of the rain that** we cancelled. |\n\n**En güçlü kullanım: düzeltme (contrast)**\n\n- ***It wasn't** the design team **that** caused the delay. **It was** the supplier.*\n- ***It's not** money **that** we need, **it's** time.*\n\n**Kurallar:**\n\n- Kişi için **who** ya da **that**; diğerleri için **that**.\n- **be** fiilinin zamanı genellikle cümlenin zamanına uyar: *It **was** ... that ...* (geçmiş) / *It **is** ... that ...* (şimdi)\n- **It was only when / only after ... that ...** = ancak ... -ince: *It was only last Thursday that we discovered it.*\n\n**Konuşmada:** Vurgulanan kelime **yüksek tonla** söylenir.",
     "examples": [{"en": "It was my grandmother who taught me to cook.", "tr": "Bana yemek yapmayı öğreten büyükannemdi."},
                  {"en": "It isn't the price that worries me, it's the quality.", "tr": "Beni endişelendiren fiyat değil, kalite."},
                  {"en": "It was only when I moved abroad that I learned to appreciate home.", "tr": "Evin değerini ancak yurt dışına taşındığımda anladım."}],
     "turkishNote": "Türkçede vurgu, vurgulanan öğeyi fiilin hemen önüne koyarak yapılır: \"Gecikmeye tedarikçi neden oldu\" (vurgu: tedarikçi). İngilizcede kelime sırası sabit olduğu için bu iş için \"It was the supplier that...\" yapısı kullanılır. Türkçedeki \"-an/-en ... -dir\" yapısı da (\"Bana yemek yapmayı öğreten büyükannemdi\") it-cleft'e çok yakındır; çeviri yaparken bu yapıyı düşünün."},
    [
        mc("\"Beni arayan Ali'ydi.\"", ["It was Ali who called me.", "Ali was who called me."], 0, "It was ... who."),
        mc("Hangisi doğru düzeltme?", ["It isn't money that we need, it's time.", "Money isn't we need, time is."], 0, "It isn't ... that ..., it's ..."),
        mc("\"It was in 2010 that we met.\" vurgulanan:", ["Nerede", "Ne zaman"], 1, "Zaman."),
        mc("\"Bunu ancak dün öğrendim.\"", ["It was only yesterday that I found out.", "It was yesterday only I found out."], 0, "It was only ... that."),
        gap("It ___ my sister who told me the news. (geçmiş)", ["was"], "It was."),
        gap("It's not the price ___ worries me, it's the quality.", ["that"], "that."),
        gap("It was in Paris ___ they first met.", ["that"], "Yer + that."),
        gap("It was only ___ I read the report that I understood. (-ince)", ["when", "after"], "It was only when."),
        listen("Everyone thinks it was Edison who invented the light bulb, but it wasn't only him. Several inventors were working on it at the same time. What Edison did was to make it practical and cheap enough for people's homes.", "Konuşan Edison hakkında ne söylüyor?", ["Ampulü tek başına icat etti", "Ampulü pratik ve ucuz hale getirdi", "Ampulle hiç ilgisi yoktu"], 1, "\"What Edison did was to make it practical and cheap\""),
        typ("It-cleft ile vurgulayın (kim?): \"My teacher encouraged me to apply.\"", variants("It was my teacher who encouraged me to apply.", "It was my teacher that encouraged me to apply."), "It was my teacher who encouraged me to apply."),
    ],
    {"kind": "speaking", "task": speak("(1) Hayatınızı etkileyen 3 kişi, yer ya da anı it-cleft ile anlatın (It was ... who / that ...). (2) Hakkınızda ya da şehriniz hakkında yaygın bir yanlış inancı it-cleft ile düzeltin (It's not ... that ..., it's ...).",
                                       "It was my uncle who got me interested in photography. He gave me his old camera when I was twelve. It was in Cappadocia that I took my first good photo, at sunrise. And it was only when I won a small competition that I started to believe in myself. People often think that it's the camera that makes a good photo. But it isn't the camera that matters, it's the eye of the photographer.",
                                       ["It-cleft doğruluğu", "who / that seçimi", "Düzeltme yapısı", "Vurgulu tonlama"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "İhtiyacımız olan şey", "Wh-cleft (What I need is ..., What happened was ...) yapısıyla bir fikri ya da olayı dramatik bir şekilde sunabilirim.",
    {"kind": "text", "title": "Bir girişimcinin sunumu", "body": "Good afternoon, everyone.\n\nWhat I'd like to talk about today is food waste. What surprised me most when I started researching this topic was that nearly a third of all the food we produce is never eaten.\n\nSo what did we do? What we did was to create an app that connects restaurants with people who want to buy their leftover food at a lower price.\n\nWhat happened next was amazing. In just six months, more than 200 restaurants joined.\n\nWhat we need now is investment, so that we can expand to other cities. And what I'm asking you for today is not just money. What I really want is partners who care about this problem as much as we do.",
     "questions": [
        mc("What does the app do?", ["It delivers food.", "It connects restaurants with people who buy leftover food.", "It teaches cooking."], 1, "\"connects restaurants with people who want to buy their leftover food\""),
        mc("What does the speaker really want?", ["Only money", "Partners who care about the problem", "More restaurants"], 1, "\"What I really want is partners who care about this problem\""),
     ]},
    {"explanation": "**Wh-cleft (pseudo-cleft):** *What* + özne + fiil + **is / was** + [vurgulanan bilgi]\n\nDinleyicinin dikkatini **asıl bilgiye** çekmek için \"merak\" yaratır.\n\n| Normal | Wh-cleft |\n|---|---|\n| We need investment. | **What we need is** investment. |\n| The result surprised me. | **What surprised me was** the result. |\n| I'd like to talk about food waste. | **What I'd like to talk about is** food waste. |\n\n**Eylemi vurgulamak: What ... do / did + is / was + (to) + fiil**\n\n| Normal | Wh-cleft |\n|---|---|\n| We created an app. | **What we did was (to) create** an app. |\n| You should rest. | **What you should do is rest.** |\n\n**Olayı vurgulamak: What happened was (that) ...**\n\n- ***What happened was that** the server crashed.*\n\n**Ters sıralama da mümkün:**\n\n- *Investment **is what we need**.* (daha vurgulu sonuç)\n- *That's **what I mean**.*\n\n**Dikkat:**\n\n- **What** = the thing(s) that; ~~The thing what~~ ✗\n- Vurgulanan kısım çoğul olsa bile genellikle **is** kullanılır: *What we need **is** more volunteers.*",
     "examples": [{"en": "What I love about this city is the food.", "tr": "Bu şehirde sevdiğim şey yemekleri."},
                  {"en": "What you need to do is talk to your manager.", "tr": "Yapman gereken şey müdürünle konuşmak."},
                  {"en": "What happened was that we missed the last train.", "tr": "Olan şuydu: son treni kaçırdık."}],
     "turkishNote": "Türkçede \"Bize lazım olan şey yatırım\" ya da \"Olan şuydu: ...\" yapıları wh-cleft'e çok benzer ve doğal bir şekilde kullanılır. İngilizcede de sunumlarda ve tartışmalarda çok yaygındır. Türkçe konuşanların sık yaptığı hata, \"The thing what\" ya da \"What we need, it is\" gibi fazladan kelimeler eklemektir. \"What we need is...\" yapısı tek başına yeterlidir."},
    [
        mc("Hangisi doğru?", ["What we need it is more time.", "What we need is more time."], 1, "What ... is."),
        mc("Hangisi doğru?", ["The thing what I love is music.", "What I love is music."], 1, "What = the thing that."),
        mc("Eylemi vurgulamak:", ["What we did was to call the police.", "What we called was the police."], 0, "What ... did was (to) + fiil."),
        mc("\"What we need is more volunteers.\" fiil:", ["is (doğru)", "are (zorunlu)"], 0, "Genellikle is."),
        gap("What I'd like to talk ___ today is climate change.", ["about"], "talk about."),
        gap("What ___ was that the server crashed. (oldu)", ["happened"], "What happened was."),
        gap("What you should ___ is apologise.", ["do"], "What you should do is."),
        gap("What surprised me ___ the size of the city.", ["was"], "Geçmiş → was."),
        listen("When the project started to fail, what we didn't do was panic. What we did was to sit down together and look at the problem honestly. What we discovered was that we had been trying to do too many things at once.", "Ekip ne keşfetti?", ["Paraları bitmişti", "Aynı anda çok fazla şey yapmaya çalışıyorlardı", "Müşteri yoktu"], 1, "\"we had been trying to do too many things at once\""),
        typ("Wh-cleft ile yeniden yazın: \"I really need a holiday.\" (What I really need)", variants("What I really need is a holiday.", "What I really need is a holiday!"), "What I really need is a holiday."),
    ],
    {"kind": "speaking", "task": speak("Bir sorunu ve çözümünüzü yatırımcılara sunuyormuş gibi kısa bir \"pitch\" yapın (1 dakika). En az 5 wh-cleft kullanın: What I'd like to talk about is ..., What surprised me was ..., What we did was (to) ..., What happened was ..., What we need is ...",
                                       "Good morning. What I'd like to talk about today is loneliness among older people. What surprised me when I started volunteering was how many elderly people go days without speaking to anyone. So what we did was to create a programme that matches university students with older neighbours for a weekly coffee. What happened next was wonderful: both groups said they felt happier. What we need now is funding to bring this programme to every neighbourhood in the city.",
                                       ["Wh-cleft çeşitliliği", "What ... did was (to)", "Pitch yapısı", "Merak yaratan sunum"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "Tek istediğim", "All ... is, The reason ... is that, The thing that ... gibi diğer vurgulu yapıları kullanabilirim.",
    {"kind": "dialogue", "title": "Müşteri görüşmesi", "lines": [
        {"speaker": "Client", "text": "Look, all I want is a website that works. The last company gave us something beautiful, but nobody could find anything."},
        {"speaker": "Designer", "text": "I understand. The reason most websites fail is that they're designed for the company, not for the users."},
        {"speaker": "Client", "text": "Exactly. The thing that annoys me most is the menus. There are too many."},
        {"speaker": "Designer", "text": "The place to start, then, is with your customers. We'll interview ten of them first."},
        {"speaker": "Client", "text": "That's the first time anyone has suggested that."},
        {"speaker": "Designer", "text": "The person who should decide how the website works is the person who uses it."}],
     "questions": [
        mc("What does the client want?", ["A beautiful website", "A website that works", "A cheaper website"], 1, "\"all I want is a website that works\""),
        mc("Why do most websites fail, according to the designer?", ["They're too expensive.", "They're designed for the company, not the users.", "They're too simple."], 1, "\"designed for the company, not for the users\""),
     ]},
    {"explanation": "Wh-cleft'e benzer, ama **what** yerine bir isim kullanan yapılar:\n\n| Yapı | Anlam | Örnek |\n|---|---|---|\n| **All** + özne + fiil + **is** | tek ... şey | **All I want is** a website that works. |\n| **The reason (why)** ... **is that** | ... -in nedeni ... | **The reason (why)** it failed **is that** nobody tested it. |\n| **The thing (that)** ... **is** | ... şey | **The thing that** annoys me **is** the noise. |\n| **The person who** ... **is** | ... kişi | **The person who** helped me most **was** my coach. |\n| **The place where** ... **is** | ... yer | **The place where** I feel happiest **is** the sea. |\n| **The time when** ... **was** | ... zaman | **The time when** I felt proudest **was** ... |\n| **The first / last / only thing** ... **is** | ilk / son / tek şey | **The only thing** I regret **is** not travelling more. |\n\n**All I did was + (to) + fiil:**\n\n- ***All I did was** ask a question!* (Sadece bir soru sordum! → savunma)\n\n**Dikkat:**\n\n- ~~The reason is because~~ → **The reason is that** (resmî dilde \"because\" tekrarı hatalı kabul edilir)\n- **All** = the only thing: ~~All what I want~~ ✗ → **All I want** ✓",
     "examples": [{"en": "All I need is a good night's sleep.", "tr": "Tek ihtiyacım güzel bir gece uykusu."},
                  {"en": "The reason I'm calling is that I have a question about my bill.", "tr": "Aramamın nedeni faturamla ilgili bir sorum olması."},
                  {"en": "The only thing I regret is not learning English earlier.", "tr": "Tek pişmanlığım İngilizceyi daha erken öğrenmemek."}],
     "turkishNote": "Türkçedeki \"Tek istediğim...\", \"... -mesinin sebebi ...\", \"Beni en çok rahatsız eden şey ...\" yapıları bu kalıplarla birebir örtüşür. Türkçe konuşanların en sık hatası \"All what I want\" demektir (Türkçedeki \"bütün istediğim şey\"den); doğrusu \"All I want\". Bir diğer yaygın hata \"The reason is because...\"; resmî İngilizcede \"The reason is that...\" tercih edilir."},
    [
        mc("Hangisi doğru?", ["All what I want is peace.", "All I want is peace."], 1, "All I want."),
        mc("Resmî dilde hangisi doğru?", ["The reason is because it's expensive.", "The reason is that it's expensive."], 1, "The reason is that."),
        mc("\"All I did was ask a question!\" tonu:", ["Savunma (sadece soru sordum!)", "Övünme"], 0, "Savunma."),
        mc("\"The place where I feel calmest is the forest.\" vurgu:", ["Yer", "Zaman"], 0, "Yer."),
        gap("___ I need is five more minutes. (Tek)", ["All"], "All I need is."),
        gap("The reason I'm late ___ that the train was cancelled.", ["is"], "The reason ... is that."),
        gap("The only ___ I regret is not saying goodbye.", ["thing"], "The only thing."),
        gap("The person ___ inspired me most was my teacher.", ["who", "that"], "The person who."),
        listen("People often ask me the secret of my success. The truth is, all I did was keep going when others gave up. The reason I never stopped is that I really loved what I was doing. And the thing I'm proudest of isn't the money. It's the team I built.", "Konuşanın en gurur duyduğu şey ne?", ["Para", "Kurduğu ekip", "Ödüller"], 1, "\"the thing I'm proudest of isn't the money. It's the team I built.\""),
        typ("Vurgulu yapıyla yeniden yazın: \"I only want a cup of tea.\" (All I want)", variants("All I want is a cup of tea.", "All I want is a cup of tea!"), "All I want is a cup of tea."),
    ],
    {"kind": "speaking", "task": speak("Kendinizi bu yapılarla tanıtın: All I need to be happy is ..., The thing that annoys me most is ..., The person who has influenced me most is ..., The place where I feel most at home is ..., The reason I'm learning English is that ..., The only thing I regret is ...",
                                       "All I need to be happy is good food and good friends. The thing that annoys me most is people who are always late. The person who has influenced me most is my aunt, who travelled the world on her own. The place where I feel most at home is my grandparents' village. The reason I'm learning English is that I want to work for an international company. And the only thing I regret is not starting earlier!",
                                       ["Çeşitli vurgulu yapılar", "The reason ... is that", "All ... is", "Akıcılık"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Sunumu yönetmek", "Yönlendirme ifadeleri (signposting), görsel anlatım ve soru-cevap kalıplarıyla bir sunumu profesyonelce yönetebilirim.",
    {"kind": "text", "title": "Sunumdan bir bölüm", "body": "Good morning, everyone, and thank you for coming. My name is Tuba Arıkan, and I'm the marketing manager.\n\nToday, I'd like to talk about our new strategy for young customers. I've divided my presentation into three parts. First, I'll look at the current situation. Then, I'll present our research. And finally, I'll suggest some next steps. Please feel free to interrupt if you have any questions.\n\nSo, let's start with the current situation. As you can see from this chart, sales to customers under 25 have fallen steadily over the last two years.\n\nThat brings me to my second point: why? Let me illustrate this with a quote from one of our focus groups: \"Your brand feels like something my parents would buy.\"\n\nMoving on to my final point...\n\n[Later]\n\nThat's a very good question. If I understand correctly, you're asking whether the new strategy will affect older customers. I'm glad you asked that...",
     "questions": [
        mc("How many parts does the presentation have?", ["Two", "Three", "Four"], 1, "\"three parts\""),
        mc("What does the chart show?", ["Sales to young customers have fallen.", "Sales have doubled.", "Older customers are leaving."], 0, "\"sales to customers under 25 have fallen steadily\""),
     ]},
    {"explanation": "**Sunumun bölümleri ve kalıplar:**\n\n| Bölüm | Kalıplar |\n|---|---|\n| **Açılış** | *Good morning, and thank you for coming.* / *I'd like to talk to you about ...* / *The purpose of this presentation is to ...* |\n| **Plan** | *I've divided my presentation into three parts.* / *First, I'll ... Then, ... Finally, ...* |\n| **Başlama** | *So, let's start with ...* / *I'd like to begin by ...* |\n| **Geçiş** | *Moving on to ...* / *That brings me to my next point.* / *Let's now turn to ...* |\n| **Örnek** | *Let me illustrate this with an example.* / *To give you an idea, ...* |\n| **Vurgu** | *I'd like to highlight ...* / *What's really important here is ...* / *It's worth bearing in mind that ...* |\n| **Konu dışı** | *Sorry, I'm digressing. Back to ...* |\n| **Özet / kapanış** | *To sum up, ...* / *In a nutshell, ...* / *I'd like to finish by ...* / *Thank you for your attention.* |\n\n**Görselleri anlatmak:**\n\n- *As you can see from this chart / on this slide, ...*\n- *This graph shows / illustrates ...*\n- *If you look at the figures on the left, ...*\n- *I'd like to draw your attention to ...*\n\n**Soru-cevap:**\n\n| Durum | Kalıp |\n|---|---|\n| Zaman kazanmak | *That's a very good question.* / *I'm glad you asked that.* |\n| Soruyu kontrol etmek | *If I understand correctly, you're asking ...* |\n| Cevabı bilmiyorsanız | *I'm afraid I don't have that information right now, but I'll find out and get back to you.* |\n| Kapsam dışıysa | *That's slightly outside the scope of today's presentation, but ...* |",
     "examples": [{"en": "That brings me to my next point.", "tr": "Bu beni bir sonraki noktama getiriyor."},
                  {"en": "As you can see from this chart, costs have risen sharply.", "tr": "Bu grafikte gördüğünüz gibi maliyetler keskin bir şekilde arttı."},
                  {"en": "I'm afraid I don't have the exact figures, but I'll get back to you.", "tr": "Maalesef kesin rakamlar elimde yok ama size dönüş yapacağım."}],
     "turkishNote": "Türkçe sunumlarda geçişler genellikle \"Şimdi ...'a geçelim\" gibi tek bir kalıpla yapılır. İngilizce sunumlarda çeşitli yönlendirme ifadeleri dinleyicinin \"haritayı\" kaybetmemesini sağlar ve konuşmacıyı çok daha profesyonel gösterir. Bilmediğiniz bir soruya cevap uydurmak yerine \"I'll get back to you\" demek, İngilizce iş kültüründe gayet kabul görür."},
    [
        mc("Bir sonraki konuya geçmek:", ["Moving on to ...", "Moving off to ..."], 0, "Moving on to."),
        mc("Cevabını bilmediğiniz bir soru:", ["I don't know. Next question.", "I'm afraid I don't have that information, but I'll get back to you."], 1, "Profesyonel."),
        mc("Görsel anlatmak:", ["As you can see from this chart, ...", "As you look this chart, ..."], 0, "As you can see from."),
        mc("\"Sorry, I'm digressing.\" anlamı:", ["Pardon, konudan sapıyorum.", "Pardon, geç kaldım."], 0, "digress."),
        gap("I've ___ my presentation into three parts.", ["divided"], "divided into."),
        gap("That ___ me to my next point.", ["brings"], "That brings me to."),
        gap("Let me ___ this with an example. (örneklemek)", ["illustrate"], "illustrate."),
        gap("If I understand ___, you're asking about the cost.", ["correctly"], "If I understand correctly."),
        match([("Moving on to ...", "geçiş"), ("To sum up, ...", "özet"), ("Let me illustrate ...", "örnek"), ("I'm glad you asked that.", "soru-cevap"), ("I'd like to begin by ...", "başlangıç")], "Kalıpları işlevleriyle eşleştirin."),
        listen("Right, I think that covers the main points. To sum up, we've seen that our costs have risen, that customers want faster delivery, and that a new warehouse could solve both problems. I'd like to finish by thanking the logistics team for their help. Now, are there any questions?", "Konuşan sunumun hangi bölümünde?", ["Açılış", "Kapanış", "Ortası"], 1, "\"To sum up... I'd like to finish by...\""),
    ],
    {"kind": "speaking", "task": speak("Seçtiğiniz bir konuda (şehriniz, bir hobi, işiniz, bir kitap) 2 dakikalık bir mini sunum yapın. Açılış, üç bölümlü bir plan, en az 3 geçiş ifadesi, bir görsel anlatım (As you can see ...) ve bir özetle bitirin. Sonra kendinize hayali bir soru sorun ve kalıplarla cevaplayın.",
                                       "Good morning, everyone, and thank you for being here. Today I'd like to talk about urban gardening. I've divided my talk into three parts. First, I'll explain what urban gardening is. Then, I'll look at the benefits. Finally, I'll show you how to start. So, let's begin. Urban gardening simply means growing food in the city. As you can see on this slide, even a small balcony can produce tomatoes and herbs. That brings me to my second point: the benefits. ... To sum up, urban gardening is cheap, healthy and fun. Thank you. Yes, that's a very good question. If I understand correctly, you're asking how much time it takes...",
                                       ["Açılış ve plan", "Geçiş ifadeleri", "Görsel anlatım", "Özet ve soru-cevap"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Sunum metni", "Cleft sentence'lar, yönlendirme dili ve etkili bir yapıyla dinleyiciyi etkileyen bir sunum metni yazabilirim.",
    {"kind": "text", "title": "Kısa bir konuşmanın metni: Neden okumalıyız?", "body": "Good evening.\n\nLet me start with a question. When was the last time you read a book, not on a screen, just a book, for more than an hour?\n\nFor most of us, it's been a while. And that's what I want to talk about tonight.\n\nI'd like to make three points. First, why reading matters. Second, why we've stopped. And third, what we can do about it.\n\nSo, why does reading matter? It isn't just about information. What reading really gives us is empathy. When we read a novel, we live inside someone else's mind. Studies suggest that people who read fiction regularly are better at understanding other people's feelings.\n\nThat brings me to my second point. Why have we stopped? The reason, I think, is not that we've lost interest. It's that our attention is constantly being taken by our phones.\n\nSo what can we do? All it takes is twenty minutes a day. Leave your phone in another room. Pick up a book. That's it.\n\nTo sum up: reading makes us more human. It was a book that changed my life when I was fifteen. Maybe tonight, one will change yours.\n\nThank you.",
     "questions": [
        mc("What does reading really give us, according to the speaker?", ["Information", "Empathy", "Money"], 1, "\"What reading really gives us is empathy.\""),
        mc("What is the speaker's practical suggestion?", ["Buy an e-reader.", "Read for twenty minutes a day without your phone.", "Join a book club."], 1, "\"All it takes is twenty minutes a day. Leave your phone in another room.\""),
     ]},
    {"explanation": "**Etkili bir sunum metninin yapısı:**\n\n| Bölüm | Teknik | Örnek |\n|---|---|---|\n| **Kanca (hook)** | Soru, şaşırtıcı bir rakam, kısa bir hikâye | *When was the last time you ...?* |\n| **Konu ve plan** | Ne anlatacağınızı söyleyin | *I'd like to make three points.* |\n| **Gelişme** | Her bölüm bir mesaj + kanıt/örnek | *What reading really gives us is empathy.* |\n| **Geçişler** | Signposting | *That brings me to my second point.* |\n| **Çağrı** | Dinleyiciden somut bir eylem | *All it takes is twenty minutes a day.* |\n| **Kapanış** | Özet + başa dönüş + güçlü son | *Maybe tonight, one will change yours.* |\n\n**Konuşma için yazmak ≠ okumak için yazmak:**\n\n- **Kısa cümleler** kullanın; dinleyici geri dönüp okuyamaz.\n- **Tekrar** edin: Ana mesajı başta, ortada ve sonda söyleyin.\n- **Cleft sentence**'larla en önemli bilgiyi **cümlenin sonuna** (dinleyicinin dikkatinin en yüksek olduğu yere) koyun: *What we need is **courage**.*\n- **Doğrudan hitap:** *you, we, us*\n- **Duraklama** yerleri bırakın (yazıda yeni satır).\n\n**Cleft sentence'ların sunumdaki gücü:** Vurgulanan bilgiyi **beklenti yaratarak** sunarlar: *The reason I'm here tonight is ... [duraklama] ... you.*",
     "examples": [{"en": "Let me start with a question.", "tr": "Bir soruyla başlayayım."},
                  {"en": "What I want you to remember is this: small changes matter.", "tr": "Hatırlamanızı istediğim şey şu: küçük değişiklikler önemlidir."},
                  {"en": "It was a single conversation that changed everything.", "tr": "Her şeyi değiştiren tek bir konuşmaydı."}],
     "turkishNote": "Türkçe sunumlarda giriş bölümü bazen uzun teşekkürler ve resmî hitaplarla geçer. İngilizce sunum kültüründe ise ilk 30 saniye dinleyicinin dikkatini çekmek için çok değerlidir: bir soru, bir hikâye ya da şaşırtıcı bir bilgiyle başlamak beklenir. Teşekkürler kısa tutulur ve genellikle sona bırakılır."},
    [
        mc("En etkili açılış:", ["Hello, my name is Can and I will talk about reading.", "When was the last time you read a book for an hour?"], 1, "Kanca."),
        mc("Konuşma için yazarken:", ["Uzun ve karmaşık cümleler", "Kısa ve net cümleler"], 1, "Dinleyici geri dönemez."),
        mc("Bilgi cümlenin neresinde en vurgulu?", ["Başında", "Sonunda"], 1, "End focus."),
        mc("İyi bir kapanış:", ["That's all. Bye.", "To sum up, ... Maybe tonight, one will change yours. Thank you."], 1, "Özet + güçlü son."),
        gap("Let me ___ with a question. (başlamak)", ["start", "begin"], "Let me start with."),
        gap("What I want you to ___ is this: every vote counts. (hatırlamak)", ["remember"], "What I want you to remember."),
        gap("It ___ a single book that changed my life.", ["was"], "It was ... that."),
        gap("All it ___ is ten minutes a day. (gerektirmek)", ["takes"], "All it takes is."),
        listen("Imagine a city with no cars. No traffic, no noise, no pollution. Sounds impossible? It isn't. What I'd like to show you tonight is how three European cities did exactly that, and what we can learn from them.", "Konuşan açılışta hangi tekniği kullanıyor?", ["Bir istatistik", "Hayal ettirmek ve soru sormak", "Bir şaka"], 1, "\"Imagine a city... Sounds impossible?\""),
        order(["What", "we", "need", "is", "not", "more", "money", "but", "more", "time"], "What we need is not more money but more time.", "Wh-cleft + not ... but.", "İhtiyacımız olan daha fazla para değil, daha fazla zaman."),
    ],
    {"kind": "writing", "task": write("TED tarzı 3–4 dakikalık bir konuşmanın metnini yazın (250–300 kelime). Konu: Hayatınızda önemli bulduğunuz bir fikir ya da alışkanlık (yürüyüş, gönüllülük, dil öğrenmek, erken kalkmak, vb.). Bir kancayla başlayın, planınızı söyleyin, en az 4 farklı cleft sentence (It was ... that, What ... is, The reason ... is that, All ... is) ve en az 3 yönlendirme ifadesi kullanın; dinleyiciye somut bir çağrıyla ve güçlü bir kapanışla bitirin. Konuşma için yazın: kısa cümleler, doğrudan hitap.",
                                      "Good evening.\n\nRaise your hand if you've ever said, \"I'm not good at languages.\"\n\nKeep it up if you still believe that.\n\nI used to. For years, I was sure I didn't have \"the gift\". And that's what I want to talk about tonight: the myth of the language gift.\n\nI'd like to make three points. First, why the myth exists. Second, what really makes people successful. And finally, what you can do, starting tomorrow.\n\nSo, let's start with the myth. Why do so many of us believe it? The reason, I think, is that we compare ourselves with children. Children seem to learn effortlessly. But what we forget is that a child hears their language for thousands of hours before they say a full sentence.\n\nThat brings me to my second point. What makes successful language learners different? It isn't talent. It's time and habit. In every study I've read, the best learners are not the most gifted. They're the most consistent.\n\nIt was a simple decision that changed everything for me. I stopped studying for three hours on Sunday, and I started studying for fifteen minutes every single day.\n\nSo, what can you do? All you need is fifteen minutes. A podcast on the bus. Five new words before bed. One conversation a week.\n\nTo sum up: there's no such thing as \"not good at languages\". There's only \"not enough practice yet\".\n\nTomorrow morning, give English your first fifteen minutes. And in a year, I'd love to hear what you say then.\n\nThank you.",
                                      ["Kanca ve plan", "En az 4 cleft sentence", "Yönlendirme ifadeleri", "Konuşmaya uygun dil", "Somut çağrı ve güçlü kapanış"])},
)

u.test([
    mc("\"Beni bu işe ikna eden annemdi.\"", ["It was my mother who persuaded me to take this job.", "My mother was who persuaded me to take this job."], 0, "It was ... who"),
    mc("Hangisi doğru?", ["What we need it is more staff.", "What we need is more staff."], 1, "What ... is"),
    mc("Hangisi doğru?", ["All what I want is a holiday.", "All I want is a holiday."], 1, "All I want"),
    mc("Resmî dilde:", ["The reason is because it's late.", "The reason is that it's late."], 1, "The reason is that"),
    mc("Bir sonraki konuya geçmek:", ["That brings me to my next point.", "That takes me my next point."], 0, "That brings me to"),
    gap("It ___ only when I saw the photo that I recognised him.", ["was"], "It was only when"),
    gap("It isn't the money ___ matters, it's the experience.", ["that"], "It isn't ... that"),
    gap("What ___ was that the bus broke down. (oldu)", ["happened"], "What happened was"),
    gap("What you should ___ is speak to a lawyer.", ["do"], "What you should do is"),
    gap("The only ___ I regret is not travelling more.", ["thing"], "The only thing"),
    gap("As you can see ___ this chart, sales have doubled.", ["from", "on", "in"], "As you can see from"),
    mc("Cevabı bilmediğiniz bir soru:", ["That's a stupid question.", "I'm afraid I don't have that information, but I'll get back to you."], 1, "Profesyonel"),
    listen("What I'd like to highlight today is one simple fact: most accidents at work happen on Monday mornings. The reason, according to our research, is that people are tired and distracted after the weekend. What we're proposing is a short safety briefing every Monday at nine.", "Ne öneriliyor?", ["Pazartesi tatil", "Her pazartesi saat dokuzda kısa bir güvenlik bilgilendirmesi", "Hafta sonu çalışma"], 1, "\"a short safety briefing every Monday at nine\""),
    typ("Wh-cleft ile yeniden yazın: \"The ending of the film surprised me.\" (What surprised me)", variants("What surprised me was the ending of the film.", "What surprised me was the film's ending."), "What surprised me was the ending of the film."),
    write("Şirketinize, okulunuza ya da belediyenize bir öneri sunduğunuz kısa bir sunum metni yazın (220–270 kelime). Kancayla başlayın, planı söyleyin, sorunu ve çözümünüzü anlatın, bir görsele atıfta bulunun (As you can see ...), en az 4 cleft sentence ve en az 4 yönlendirme ifadesi kullanın ve bir çağrıyla bitirin.",
          "Good morning, everyone.\n\nLet me start with a number: forty-five. That's how many minutes the average employee in our building spends every day looking for a parking space, waiting for the lift or queuing for lunch.\n\nWhat I'd like to talk about today is how we can win back that time. I've divided my presentation into three parts: the problem, our solution and the next steps.\n\nSo, let's begin with the problem. As you can see from this chart, our staff numbers have doubled in five years, but our building hasn't changed. It isn't laziness that is making people late for meetings. It's the building itself.\n\nThat brings me to our solution. What we're proposing is a simple three-step plan. First, a flexible start time between eight and ten, so that not everyone arrives at once. Second, an online system for booking parking spaces. And third, a second lunch break at one thirty.\n\nThe reason we believe this will work is that two of our partner companies have already tried it. In both cases, staff satisfaction rose by more than twenty percent.\n\nMoving on to the next steps. All we need from you today is approval for a three-month trial. It would cost almost nothing, and if it doesn't work, we can simply go back to the current system.\n\nTo sum up: forty-five minutes a day is almost four hours a week. Imagine what our team could do with that time.\n\nThank you. I'm happy to take any questions.",
          ["Kanca ve plan", "En az 4 cleft sentence", "Yönlendirme ve görsel dili", "Sorun-çözüm yapısı", "Çağrı ve kapanış"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

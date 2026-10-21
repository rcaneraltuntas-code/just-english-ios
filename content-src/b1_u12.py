"""B1 Ünite 12: Fikrim var."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("B1", 12, "Fikrim var", "In My Opinion",
         "Gündemdeki konular hakkında fikrimi gerekçeleriyle söyleyebilir, kibarca katılıp katılmadığımı belirtebilir, although, despite ve however ile zıt fikirleri bağlayabilir ve artı-eksi tartışan düzenli bir kompozisyon yazabilirim.",
         ["fikir bildirme, katılma ve katılmama", "although / even though + cümle", "despite / in spite of + isim / -ing", "however / on the other hand / in addition", "artı-eksi kompozisyon yapısı"],
         ["gündem konuları", "çevre ve teknoloji", "eğitim ve toplum"],
         {"title": "Tartışma kulübü", "durationMinutes": 45,
          "goal": "Sınıf iki takıma ayrılır ve bir konuyu tartışır (Okullarda telefon yasaklanmalı mı? / Herkes haftada dört gün mü çalışmalı?). Takımlar In my opinion..., Although..., Despite..., However... ile argümanlarını sunar, karşı tarafa I see your point, but... ile cevap verir. Sonunda her öğrenci kendi kişisel görüşünü bir cümleyle özetler ve sınıf oylama yapar."})

u.vocab([
    ("opinion", "fikir, görüş", "In my opinion, it's a good idea.", "Bence iyi bir fikir.", None),
    ("point of view", "bakış açısı", "I understand your point of view.", "Bakış açını anlıyorum.", None),
    ("argument", "argüman; tartışma", "That's a strong argument.", "Bu güçlü bir argüman.", None),
    ("advantage", "avantaj", "One advantage is the price.", "Avantajlardan biri fiyatı.", None),
    ("disadvantage", "dezavantaj", "The main disadvantage is the noise.", "Asıl dezavantajı gürültü.", None),
    ("benefit", "fayda", "Exercise has many benefits.", "Egzersizin birçok faydası var.", None),
    ("issue", "mesele, konu", "Climate change is a global issue.", "İklim değişikliği küresel bir mesele.", None),
    ("environment", "çevre", "We need to protect the environment.", "Çevreyi korumamız gerekiyor.", None),
    ("pollution", "kirlilik", "Air pollution is a big problem in cities.", "Hava kirliliği şehirlerde büyük bir sorun.", None),
    ("social media", "sosyal medya", "Teenagers spend hours on social media.", "Gençler saatlerini sosyal medyada geçiriyor.", None),
    ("ban", "yasaklamak; yasak", "Some schools have banned phones.", "Bazı okullar telefonları yasakladı.", None),
    ("public transport", "toplu taşıma", "Public transport should be cheaper.", "Toplu taşıma daha ucuz olmalı.", None),
    ("waste", "atık; israf", "We produce too much plastic waste.", "Çok fazla plastik atık üretiyoruz.", None),
    ("recycle", "geri dönüştürmek", "Do you recycle glass?", "Camı geri dönüştürüyor musun?", None),
    ("although", "-e rağmen, gerçi", "Although it was cold, we went out.", "Soğuk olmasına rağmen dışarı çıktık.", "+ cümle"),
    ("despite", "-e rağmen", "Despite the rain, we went out.", "Yağmura rağmen dışarı çıktık.", "+ isim / -ing"),
    ("however", "ancak, fakat", "It's cheap. However, it's slow.", "Ucuz. Ancak yavaş.", "Cümle başında, virgülle"),
    ("in addition", "ek olarak, ayrıca", "In addition, it saves time.", "Ayrıca zaman kazandırıyor.", None),
    ("on the other hand", "öte yandan", "On the other hand, it's expensive.", "Öte yandan pahalı.", None),
    ("agree with", "-e katılmak", "I agree with you.", "Sana katılıyorum.", "I'm agree ✗"),
    ("disagree", "katılmamak", "I'm afraid I disagree.", "Korkarım katılmıyorum.", None),
    ("convince", "ikna etmek", "You've convinced me!", "Beni ikna ettin!", None),
    ("in conclusion", "sonuç olarak", "In conclusion, there are pros and cons.", "Sonuç olarak artıları ve eksileri var.", None),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Bence...", "Bir konu hakkında fikrimi söyleyebilir, kibarca katılabilir ya da katılmadığımı belirtebilirim.",
    {"kind": "dialogue", "title": "Okulda telefon yasağı", "lines": [
        {"speaker": "Meltem", "text": "Did you hear? Our school wants to ban phones in classrooms. What do you think?"},
        {"speaker": "Arif", "text": "In my opinion, it's a great idea. Students can't concentrate with phones on their desks."},
        {"speaker": "Meltem", "text": "I see your point, but I'm not sure I agree. We sometimes use phones for research in class."},
        {"speaker": "Arif", "text": "That's true. But the school has computers for that."},
        {"speaker": "Meltem", "text": "Maybe. Personally, I think teachers should decide, not the school."},
        {"speaker": "Arif", "text": "Hmm, you might be right about that."}],
     "questions": [
        mc("What does Arif think about the ban?", ["It's a great idea.", "It's a terrible idea.", "He doesn't care."], 0, "\"In my opinion, it's a great idea.\""),
        mc("Who does Meltem think should decide?", ["The school", "The teachers", "The students"], 1, "\"teachers should decide\""),
     ]},
    {"explanation": "**Fikir bildirmek:**\n\n- **In my opinion**, ... / **Personally, I think** ...\n- **I believe (that)** ... / **As far as I'm concerned**, ...\n- **I'm not sure, but** ... (daha yumuşak)\n\n**Fikir sormak:**\n\n- **What do you think (about** ...**)?** / **What's your opinion on** ...?\n- **How do you feel about** ...?\n\n**Katılmak ve katılmamak (güçlüden yumuşağa):**\n\n| Katılmak | Katılmamak |\n|---|---|\n| **I completely agree.** | **I completely disagree.** (çok sert olabilir) |\n| **I agree with you.** | **I'm afraid I disagree.** |\n| **That's true.** / **Exactly!** | **I'm not sure I agree.** |\n| **You might be right.** | **I see your point, but** ... |\n\n**Dikkat:** **agree** bir fiildir; **be** ile kullanılmaz:\n\n- **I agree.** (~~I am agree.~~) / **I don't agree.** (~~I'm not agree.~~)",
     "examples": [{"en": "Personally, I think public transport should be free.", "tr": "Bence toplu taşıma ücretsiz olmalı."},
                  {"en": "I see your point, but it's too expensive.", "tr": "Ne demek istediğini anlıyorum ama çok pahalı."},
                  {"en": "How do you feel about working from home?", "tr": "Evden çalışma hakkında ne düşünüyorsun?"}],
     "turkishNote": "Türkçedeki \"Katılıyorum\" cümlesini \"I am agree\" diye çevirmek Türkçe konuşanların en sık yaptığı hatalardan biridir. agree bir fiildir: I agree / I don't agree. \"Bence\" için de \"According to me\" yerine \"In my opinion\" ya da \"I think\" kullanın."},
    [
        mc("Hangisi doğru?", ["I am agree with you.", "I agree with you."], 1, "agree bir fiil."),
        mc("\"Bence\"", ["According to me, ...", "In my opinion, ..."], 1, "In my opinion."),
        mc("Kibarca katılmamak:", ["You're wrong!", "I see your point, but ...", "No way!"], 1, "Kibar → I see your point, but."),
        mc("Hangisi doğru?", ["I'm not agree.", "I don't agree."], 1, "don't agree."),
        gap("What do you ___ about the new law?", ["think"], "What do you think about...?"),
        gap("How do you ___ about social media?", ["feel"], "How do you feel about...?"),
        gap("I'm ___ I disagree. (korkarım)", ["afraid"], "I'm afraid I disagree."),
        gap("You ___ be right about that. (olabilir)", ["might", "may", "could"], "You might be right."),
        listen("What do you think about the new bike lanes? – Personally, I love them. Although some drivers complain, I think the city is much safer now.", "Konuşan yeni bisiklet yolları hakkında ne düşünüyor?", ["Sevmiyor", "Çok seviyor", "Kararsız"], 1, "\"Personally, I love them.\""),
        typ("İngilizce yazın: \"Ne demek istediğini anlıyorum ama katılmıyorum.\"", variants("I see your point, but I don't agree.", "I see your point, but I disagree.", "I see what you mean, but I don't agree.", "I see what you mean, but I disagree.", "I understand your point, but I don't agree.", "I see your point but I don't agree.", "I see your point, but I do not agree."), "I see your point, but I don't agree."),
    ],
    {"kind": "speaking", "task": speak("JAI size 4 konu verecek (okullarda üniforma, şehir merkezinde araba yasağı, dört günlük çalışma haftası, çocuklara sosyal medya). Her biri için fikrinizi gerekçesiyle söyleyin. JAI karşı görüş bildirecek; kibarca katılın ya da katılmayın.",
                                       "In my opinion, school uniforms are a good idea, because all students look equal. ... I see your point, but I'm not sure I agree. Uniforms can be expensive for some families. ... Personally, I think a four-day working week would make people happier. ... That's true. You might be right about that.",
                                       ["Fikir kalıpları çeşitli", "Kibar katılma / katılmama", "Gerekçe sunma", "I agree (am agree değil)"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "-e rağmen (1)", "although ve even though ile iki zıt fikri tek cümlede bağlayabilirim.",
    {"kind": "text", "title": "Şehirde bisiklet: Okur yorumları", "body": "\"Although the city has built new bike lanes, I still don't feel safe. Drivers don't respect cyclists.\" – Haluk\n\n\"I cycle to work every day, even though it's 12 kilometres. It's faster than the bus and I feel great!\" – Sevgi\n\n\"Although cycling is good for the environment, it isn't practical for everyone. I have three children!\" – Nazlı\n\n\"Even though it rains a lot here, more people are cycling than ever before. The city should build more lanes.\" – Ozan",
     "questions": [
        mc("Why doesn't Haluk feel safe?", ["The lanes are too narrow.", "Drivers don't respect cyclists.", "It rains a lot."], 1, "\"Drivers don't respect cyclists.\""),
        mc("Why isn't cycling practical for Nazlı?", ["She lives far away.", "She has three children.", "She doesn't have a bike."], 1, "\"I have three children!\""),
     ]},
    {"explanation": "**although / even though** + **cümle (özne + fiil)**, beklenmedik bir zıtlığı bağlar (\"-e rağmen\", \"-diği halde\").\n\n| Yapı | Örnek |\n|---|---|\n| **Although** + cümle, cümle. | **Although** it was cold, we went swimming. |\n| Cümle **although** + cümle. | We went swimming **although** it was cold. |\n| **Even though** (daha güçlü) | I cycle to work **even though** it's 12 km. |\n\n**Virgül:** although başta ise iki cümle arasına virgül gelir.\n\n**Dikkat:** although ile **but** aynı cümlede **kullanılmaz**:\n\n- **Although** it was cold, ~~but~~ we went out.\n- It was cold, **but** we went out. ✓\n- **Although** it was cold, we went out. ✓\n\n**though** konuşmada cümle sonunda da kullanılır (= yine de):\n\n- It was cold. We went out, **though**.",
     "examples": [{"en": "Although he's rich, he lives in a small flat.", "tr": "Zengin olmasına rağmen küçük bir dairede yaşıyor."},
                  {"en": "She went to work even though she was ill.", "tr": "Hasta olduğu halde işe gitti."},
                  {"en": "The film was long. I enjoyed it, though.", "tr": "Film uzundu. Yine de beğendim."}],
     "turkishNote": "Türkçede \"Soğuk olmasına rağmen ama dışarı çıktık\" demeyiz; İngilizcede de although ile but birlikte kullanılmaz. Türkçe konuşanlar bazen \"Although ... but ...\" yapısını Türkçedeki \"gerçi ... ama\" kalıbından aktarır; bu İngilizcede yanlıştır."},
    [
        mc("Hangisi doğru?", ["Although it was late, but we stayed.", "Although it was late, we stayed."], 1, "although + but olmaz."),
        mc("___ he studied hard, he failed the exam.", ["Although", "Because", "So"], 0, "Zıtlık → although."),
        mc("although'dan sonra ne gelir?", ["isim", "cümle (özne + fiil)", "-ing"], 1, "although + cümle."),
        gap("___ though she was tired, she finished the report.", ["Even"], "Even though."),
        gap("Although the hotel was expensive, ___ room was tiny.", ["the"], "although + cümle, cümle."),
        gap("I enjoyed the trip, ___ it rained every day.", ["although", "though", "even though"], "although."),
        gap("It was expensive. I bought it, ___. (yine de)", ["though"], "Cümle sonu though."),
        order(["it", "Although", "was", "cold", "we", "went", "swimming"], "Although it was cold we went swimming.", "Although + cümle + cümle.", "Soğuk olmasına rağmen yüzmeye gittik."),
        listen("Although I love living in the city, I miss the silence of my village. Even though there's so much to do here, I sometimes feel lonely.", "Konuşan şehirde ne özlüyor?", ["Ailesini", "Köyünün sessizliğini", "Eski işini"], 1, "\"I miss the silence of my village\""),
        typ("Birleştirin (Although ile başlayın): \"He's rich. He lives in a small flat.\"", variants("Although he's rich, he lives in a small flat.", "Although he is rich, he lives in a small flat.", "Although he's rich he lives in a small flat."), "Although he's rich, he lives in a small flat."),
    ],
    {"kind": "speaking", "task": speak("Kendi hayatınızdan ya da toplumdan 5 \"beklenmedik zıtlık\" söyleyin: although ve even though kullanın. Bir tanesinde cümle sonunda though kullanın.",
                                       "Although I live near the sea, I rarely swim. I drink coffee every evening even though it keeps me awake. Although my city is very crowded, I love it. Even though electric cars are better for the environment, they're still too expensive for most people. My job is stressful. I really like it, though.",
                                       ["although / even though + cümle", "but ile birlikte kullanılmadı", "Cümle sonu though"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "-e rağmen (2)", "despite ve in spite of ile isim ya da -ing kullanarak zıtlık bildirebilir, although ile farkını bilirim.",
    {"kind": "dialogue", "title": "Haber yorumu", "lines": [
        {"speaker": "Presenter", "text": "Despite the bad weather, thousands of people came to the clean-up event at the beach yesterday."},
        {"speaker": "Reporter", "text": "That's right. In spite of the rain, volunteers collected more than two tonnes of plastic waste."},
        {"speaker": "Presenter", "text": "Amazing. And the youngest volunteer?"},
        {"speaker": "Reporter", "text": "A seven-year-old boy. Despite being so young, he worked for five hours!"},
        {"speaker": "Presenter", "text": "And what did the organisers say?"},
        {"speaker": "Reporter", "text": "They said that although the event was a success, people need to stop throwing rubbish on the beach."}],
     "questions": [
        mc("What was the weather like?", ["Sunny", "Rainy", "Windy"], 1, "\"In spite of the rain\""),
        mc("How much waste did the volunteers collect?", ["Two kilos", "More than two tonnes", "Two bags"], 1, "\"more than two tonnes of plastic waste\""),
     ]},
    {"explanation": "**despite / in spite of** + **isim** ya da **-ing** (cümle değil!)\n\n| Yapı | Örnek |\n|---|---|\n| despite + **isim** | **Despite** the rain, we went out. |\n| in spite of + **isim** | **In spite of** the traffic, we arrived on time. |\n| despite + **-ing** | **Despite being** young, he worked hard. |\n| despite **the fact that** + cümle | **Despite the fact that** it rained, ... |\n\n**although mu despite mı?**\n\n| although + **cümle** | despite + **isim / -ing** |\n|---|---|\n| Although **it rained**, ... | Despite **the rain**, ... |\n| Although **he was** tired, ... | Despite **being** tired, ... / Despite **his tiredness**, ... |\n| Although **she's** young, ... | Despite **her age**, ... |\n\n**Dikkat:** ~~despite of~~ yanlıştır. **despite** ya da **in spite of** kullanın.",
     "examples": [{"en": "Despite the high price, the tickets sold out in an hour.", "tr": "Yüksek fiyata rağmen biletler bir saatte tükendi."},
                  {"en": "In spite of feeling ill, she went to work.", "tr": "Hasta hissetmesine rağmen işe gitti."},
                  {"en": "Despite living in Paris for years, he can't speak French.", "tr": "Yıllardır Paris'te yaşamasına rağmen Fransızca konuşamıyor."}],
     "turkishNote": "Türkçede \"yağmura rağmen\" (isim) ve \"yağmur yağmasına rağmen\" (cümle) yapılarının ikisi de \"rağmen\" ile kurulur. İngilizcede ise isim için despite, cümle için although kullanılır. \"Despite it was raining\" yanlıştır; \"Although it was raining\" ya da \"Despite the rain\" doğrudur. \"despite of\" da sık yapılan bir hatadır."},
    [
        mc("___ the rain, we played football.", ["Although", "Despite"], 1, "İsim → despite."),
        mc("___ it was raining, we played football.", ["Although", "Despite"], 0, "Cümle → although."),
        mc("Hangisi doğru?", ["Despite of the traffic, we were on time.", "Despite the traffic, we were on time."], 1, "despite of yok."),
        mc("Despite ___ tired, she finished the race.", ["she was", "being", "be"], 1, "despite + -ing."),
        gap("In ___ of the cold, they swam in the sea.", ["spite"], "In spite of."),
        gap("Despite ___ (live) in London, he never visited the museum.", ["living"], "despite + -ing."),
        gap("___ the high price, many people bought it. (rağmen; 1 kelime)", ["Despite"], "Despite + isim."),
        gap("Despite the ___ that it was late, they continued working.", ["fact"], "despite the fact that."),
        listen("In spite of the long queue, we waited for two hours to see the exhibition. And despite being tired, we enjoyed every minute.", "Ne kadar beklediler?", ["Yarım saat", "İki saat", "Bütün gün"], 1, "\"we waited for two hours\""),
        typ("despite ile yeniden yazın: \"Although it was cold, we went for a walk.\"", variants("Despite the cold, we went for a walk.", "Despite the cold weather, we went for a walk.", "We went for a walk despite the cold.", "We went for a walk despite the cold weather.", "Despite the fact that it was cold, we went for a walk.", "Despite it being cold, we went for a walk.", "Despite the cold we went for a walk."), "Despite the cold, we went for a walk."),
    ],
    {"kind": "speaking", "task": speak("Tanıdığınız ya da haberlerde duyduğunuz 3 \"başarı hikâyesi\"ni anlatın: Zorluklara rağmen ne başardılar? despite + isim, despite / in spite of + -ing ve although'u en az birer kez kullanın.",
                                       "My grandmother learned to read at 60, despite her age. In spite of having a full-time job, my friend Arda finished his master's degree. Although she had very little money, my cousin opened her own café, and despite the difficult start, it's now very popular.",
                                       ["despite / in spite of + isim / -ing", "although + cümle", "despite of kullanılmadı"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Ancak, öte yandan, ayrıca", "however, on the other hand ve in addition ile cümleler arasında mantıklı bağlantılar kurabilirim.",
    {"kind": "text", "title": "Uzaktan çalışma: Bir uzman görüşü", "body": "Working from home has become very popular in recent years. It has clear advantages. Employees save time and money because they don't travel to work. In addition, many people say they can concentrate better at home.\n\nHowever, there are also some disadvantages. Some workers feel lonely, and it can be difficult to separate work and home life. Moreover, younger employees often miss the chance to learn from experienced colleagues.\n\nOn the one hand, companies can save money on offices. On the other hand, they may find it harder to build a strong team.\n\nIn my view, a mix of office and home working is probably the best solution for most people.",
     "questions": [
        mc("What is one advantage of working from home?", ["People save time and money.", "People meet more colleagues.", "Offices are bigger."], 0, "\"Employees save time and money\""),
        mc("What does the expert think is the best solution?", ["Working only from home", "Working only in the office", "A mix of both"], 2, "\"a mix of office and home working\""),
     ]},
    {"explanation": "**Bağlaçlar (linking words)** iki cümle ya da paragraf arasındaki ilişkiyi gösterir. Çoğu **cümle başında** gelir ve **virgül** alır.\n\n| İşlev | Bağlaç | Örnek |\n|---|---|---|\n| **Zıtlık** | **However,** | It's cheap. **However,** it's slow. |\n| | **On the other hand,** | Cities are exciting. **On the other hand,** they're noisy. |\n| | **but** (cümle içinde) | It's cheap, **but** it's slow. |\n| **Ekleme** | **In addition,** | It saves time. **In addition,** it's cheaper. |\n| | **Moreover,** (resmî) | **Moreover,** it's good for the environment. |\n| | **Also,** / **as well** | It's **also** quieter. / It's quieter **as well**. |\n| **Sonuç** | **So / Therefore,** | It was late, **so** we left. / **Therefore,** ... |\n| **Özet** | **In conclusion,** / **To sum up,** | **In conclusion,** both sides have a point. |\n\n**however mi but mı?**\n\n- **but** iki cümleyi **birleştirir**: It's cheap, **but** it's slow.\n- **However** **yeni bir cümle** başlatır: It's cheap. **However,** it's slow.",
     "examples": [{"en": "The flat is small. However, it's in a great location.", "tr": "Daire küçük. Ancak harika bir konumda."},
                  {"en": "Cycling is healthy. In addition, it doesn't cause pollution.", "tr": "Bisiklet sürmek sağlıklı. Ayrıca kirliliğe yol açmıyor."},
                  {"en": "The train was cancelled. Therefore, we took a taxi.", "tr": "Tren iptal edildi. Bu yüzden taksiye bindik."}],
     "turkishNote": "Türkçede \"ama\" ve \"ancak\" çok benzer kullanılır; İngilizcede ise but cümle içinde, however ise yeni bir cümlenin başında (virgülle) kullanılır. \"It's cheap however it's slow\" yerine \"It's cheap. However, it's slow.\" yazın."},
    [
        mc("Hangisi doğru noktalama?", ["It's cheap, however it's slow.", "It's cheap. However, it's slow."], 1, "However → yeni cümle + virgül."),
        mc("Ekleme:", ["However,", "In addition,", "On the other hand,"], 1, "In addition."),
        mc("Sonuç:", ["Therefore,", "Moreover,", "Although"], 0, "Therefore."),
        mc("It's a great phone. ___, it's very expensive.", ["In addition", "However", "So"], 1, "Zıtlık → However."),
        gap("Walking is free. In ___, it's good for your health.", ["addition"], "In addition."),
        gap("On the one hand, it's fast. On the ___ hand, it's dangerous.", ["other"], "On the other hand."),
        gap("It was raining, ___ we stayed at home.", ["so"], "so."),
        gap("In ___, there are good and bad points. (sonuç olarak)", ["conclusion"], "In conclusion."),
        listen("Living in the countryside is peaceful and the air is clean. However, there aren't many jobs, and in addition, public transport is very limited.", "Kırsal yaşamın dezavantajları neler?", ["Gürültü ve kirlilik", "Az iş ve sınırlı toplu taşıma", "Pahalı evler"], 1, "\"there aren't many jobs... public transport is very limited\""),
        typ("However ile iki cümle yazın: \"Bu daire küçük ama harika bir konumda.\"", variants("The flat is small. However, it's in a great location.", "This flat is small. However, it's in a great location.", "The flat is small. However, it is in a great location.", "This flat is small. However, it is in a great location.", "The flat is small. However, it's in a great area.", "This flat is small. However, it's in a great area."), "The flat is small. However, it's in a great location."),
    ],
    {"kind": "speaking", "task": speak("\"Büyük şehirde yaşamak\" konusunu 1 dakika anlatın. En az 2 avantaj (In addition / Also), 2 dezavantaj (However / On the other hand) söyleyin ve In conclusion ile kendi fikrinizi belirtin.",
                                       "Living in a big city has many advantages. There are lots of jobs and good universities. In addition, there's always something to do, like concerts and exhibitions. However, cities are often noisy and polluted. On the other hand, the countryside is peaceful but boring for young people. In conclusion, I think big cities are better when you're young.",
                                       ["Bağlaçlar doğru ve çeşitli", "However + virgül", "Net bir sonuç"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Kompozisyon yazıyorum", "Bir konunun artılarını ve eksilerini tartışan, paragraflara ayrılmış düzenli bir kompozisyon yazabilirim.",
    {"kind": "text", "title": "Örnek kompozisyon: Çocukların telefonu olmalı mı?", "body": "Nowadays, many children have their own smartphone before the age of ten. Is this a good thing? There are arguments for and against.\n\nOn the one hand, phones have some clear benefits. Parents can contact their children easily, and children can call for help in an emergency. In addition, phones can be useful for learning, for example with language apps.\n\nOn the other hand, there are serious disadvantages. Many experts believe that young children spend too much time on screens. Moreover, although parents can control some apps, children may see things that aren't suitable for their age.\n\nIn conclusion, despite the benefits, I believe that children under twelve don't need a smartphone. A simple phone for calls is a better solution.",
     "questions": [
        mc("What is one benefit of phones for children, according to the essay?", ["Children can call for help in an emergency.", "Children sleep better.", "Phones are cheap."], 0, "\"children can call for help in an emergency\""),
        mc("What is the writer's final opinion?", ["Children should have smartphones.", "Children under twelve don't need a smartphone.", "Phones should be banned for everyone."], 1, "\"children under twelve don't need a smartphone\""),
     ]},
    {"explanation": "**Artı-eksi kompozisyonu (for and against essay)** dört paragraftan oluşur:\n\n| Paragraf | İçerik | Kalıplar |\n|---|---|---|\n| **1. Giriş** | Konuyu tanıt, soruyu sor | **Nowadays**, ... / **There are arguments for and against.** |\n| **2. Artılar** | 2–3 avantaj ve örnek | **On the one hand**, ... / **In addition**, ... / **For example**, ... |\n| **3. Eksiler** | 2–3 dezavantaj | **On the other hand**, ... / **Moreover**, ... / **However**, ... |\n| **4. Sonuç** | Kendi görüşün | **In conclusion**, ... / **Despite** ..., **I believe** ... |\n\n**İyi bir kompozisyon için:**\n\n- Her paragraf **bir ana fikre** odaklansın.\n- Bağlaçları **çeşitli** kullanın (her cümlede \"and\" ve \"but\" değil).\n- Fikir cümlelerini **sadece giriş ya da sonuç**ta verin; ortadaki paragraflarda tarafsız kalın.\n- Kısaltma (don't, it's) yerine yazıda **tam hal** (do not, it is) daha resmîdir, ama B1 seviyesinde kısaltmalar da kabul edilir.\n- Sonunda **yeni bir argüman eklemeyin**; özetleyin ve görüşünüzü belirtin.",
     "examples": [{"en": "Nowadays, more and more people work from home.", "tr": "Günümüzde giderek daha fazla insan evden çalışıyor."},
                  {"en": "There are arguments for and against this idea.", "tr": "Bu fikrin lehinde ve aleyhinde argümanlar var."},
                  {"en": "In conclusion, I believe the advantages are greater than the disadvantages.", "tr": "Sonuç olarak, avantajların dezavantajlardan daha büyük olduğuna inanıyorum."}],
     "turkishNote": "Türkçe kompozisyonlarda giriş paragrafı genellikle daha uzun ve genel olur. İngilizce kompozisyonlarda giriş kısa ve konuya doğrudan girer; her paragrafın ilk cümlesi (topic sentence) o paragrafın ana fikrini söyler. Uzun ve süslü cümleler yerine net ve bağlaçlarla düzenlenmiş cümleler tercih edilir."},
    [
        mc("Kompozisyonda kendi görüşünüzü en çok nerede söylersiniz?", ["Artılar paragrafında", "Sonuç paragrafında", "Her cümlede"], 1, "Sonuçta."),
        mc("Giriş için uygun bir cümle:", ["In conclusion, it's bad.", "Nowadays, many people shop online.", "Moreover, it's cheap."], 1, "Nowadays ile konu tanıtımı."),
        mc("Sonuç paragrafında ne yapılmamalı?", ["Görüş belirtmek", "Yeni bir argüman eklemek", "Özetlemek"], 1, "Yeni argüman eklenmez."),
        gap("There are arguments ___ and against.", ["for"], "for and against."),
        gap("___ example, you can use language apps. (örneğin)", ["For"], "For example."),
        gap("Despite the ___, I think it's a bad idea. (faydalar)", ["benefits", "advantages"], "despite + isim."),
        gap("In conclusion, I ___ that the city needs more parks. (inanıyorum)", ["believe", "think"], "I believe."),
        match([("Nowadays,", "giriş"), ("On the one hand,", "artılar"), ("On the other hand,", "eksiler"), ("Moreover,", "ekleme"), ("In conclusion,", "sonuç")], "Bağlaçları işlevleriyle eşleştirin."),
        listen("Tips for essay writing: start each paragraph with a clear topic sentence. Use a variety of linking words, and remember to give examples. Keep your own opinion for the conclusion.", "Konuşan kendi görüşün nerede verilmesini tavsiye ediyor?", ["Girişte", "Sonuçta", "Her paragrafta"], 1, "\"Keep your own opinion for the conclusion.\""),
        typ("İngilizce yazın: \"Bu fikrin lehinde ve aleyhinde argümanlar var.\"", variants("There are arguments for and against this idea.", "There are arguments for and against the idea.", "There are arguments both for and against this idea.", "There are arguments for and against this."), "There are arguments for and against this idea."),
    ],
    {"kind": "writing", "task": write("Aşağıdaki konulardan birini seçip 4 paragraflık bir artı-eksi kompozisyonu yazın (160–200 kelime): 1) Şehir merkezlerinde arabalar yasaklanmalı mı? 2) Üniversite eğitimi ücretsiz olmalı mı? 3) Herkes haftada dört gün çalışmalı mı? although, despite, however, in addition ve on the other hand'i kullanın.",
                                      "Should cars be banned from city centres?\n\nNowadays, many cities have serious problems with traffic and air pollution. Some people believe that cars should be banned from city centres. There are arguments for and against this idea.\n\nOn the one hand, a ban would make the air much cleaner. People would walk or cycle more, which is better for their health. In addition, city centres would be quieter and safer for children.\n\nOn the other hand, a ban could cause problems. Although public transport is good in some cities, it is not reliable everywhere. Moreover, shop owners might lose customers who come by car. However, the biggest problem would be for older people and people with disabilities, who often need a car to travel.\n\nIn conclusion, despite these disadvantages, I believe that cities should limit cars in the centre. However, the ban should only start when public transport is cheap and reliable, and there should be special permission for people who really need a car.",
                                      ["4 paragraf yapısı", "Bağlaçlar çeşitli ve doğru", "although / despite / however doğru", "Artılar ve eksiler dengeli", "Net bir sonuç ve görüş"])},
)

u.test([
    mc("Hangisi doğru?", ["I am agree.", "I agree."], 1, "agree fiil"),
    mc("\"Bence\"", ["According to me", "In my opinion"], 1, "In my opinion"),
    mc("___ the rain, we went out.", ["Although", "Despite"], 1, "despite + isim"),
    mc("___ it was raining, we went out.", ["Although", "Despite"], 0, "although + cümle"),
    mc("Hangisi doğru?", ["Although it was late, but we stayed.", "Although it was late, we stayed."], 1, "although + but olmaz"),
    mc("Hangisi doğru?", ["Despite of the noise, I slept.", "Despite the noise, I slept."], 1, "despite of yok"),
    gap("Despite ___ (be) ill, she went to work.", ["being"], "despite + -ing"),
    gap("In ___ of the traffic, we arrived on time.", ["spite"], "in spite of"),
    mc("It's fast. ___, it's expensive.", ["However", "In addition"], 0, "Zıtlık"),
    gap("It's healthy. In ___, it's cheap.", ["addition"], "In addition"),
    gap("I see your ___, but I don't agree.", ["point"], "I see your point"),
    gap("In ___, I think it's a good idea. (sonuç olarak)", ["conclusion"], "In conclusion"),
    listen("Although electric cars are better for the environment, they're still expensive. However, prices are falling every year, and in addition, many cities are building more charging stations.", "Konuşan elektrikli arabaların hangi dezavantajından bahsediyor?", ["Yavaş olmaları", "Pahalı olmaları", "Çevreye zararlı olmaları"], 1, "\"they're still expensive\""),
    typ("although ile yeniden yazın: \"Despite the high price, many people bought the phone.\"", variants("Although the price was high, many people bought the phone.", "Although the phone was expensive, many people bought it.", "Although the price was high, a lot of people bought the phone.", "Many people bought the phone although the price was high.", "Although it was expensive, many people bought the phone.", "Although the phone was expensive, many people bought the phone."), "Although the price was high, many people bought the phone."),
    write("\"Sosyal medya hayatımızı iyileştiriyor mu?\" konulu 4 paragraflık bir artı-eksi kompozisyonu yazın (160–200 kelime). Giriş, artılar, eksiler ve sonuç paragrafları olsun; although, despite, however, in addition, on the other hand ve fikir kalıplarını kullanın.",
          "Does social media make our lives better?\n\nNowadays, billions of people use social media every day. Some people think it has improved our lives, while others believe it causes serious problems. There are arguments for and against.\n\nOn the one hand, social media helps people stay in touch with friends and family, even when they live in different countries. In addition, it gives everyone the chance to share their ideas and learn new things. For example, many people use it to find jobs or to start small businesses.\n\nOn the other hand, social media has some clear disadvantages. Many people, especially teenagers, spend too much time looking at their phones. Moreover, although some information online is useful, a lot of it is not true. However, the biggest problem may be that people compare their lives with others' perfect photos and feel unhappy.\n\nIn conclusion, despite its benefits, I believe that social media can be harmful if we use it too much. In my opinion, the best solution is to use it carefully and to spend more time with people face to face.",
          ["4 paragraf yapısı", "Zıtlık bağlaçları doğru", "Ekleme bağlaçları", "Dengeli argümanlar", "Net sonuç ve görüş"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

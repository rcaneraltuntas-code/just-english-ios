"""B2 Ünite 12: Toplum."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("B2", 12, "Toplum", "Society",
         "Bağlaçları ve söylem belirleyicilerini (however, despite, as a result, therefore) doğru noktalamayla kullanabilir, iyi yapılandırılmış paragraflar kurabilir, toplumsal konularda dengeli görüş bildirebilir ve B2 sınav standartlarında bir görüş yazısı (essay) yazabilirim.",
         ["ekleme ve karşıtlık: moreover, however, although, despite", "neden, sonuç ve amaç: due to, as a result, therefore, so that", "paragraf yapısı: topic sentence ve destek", "dengeli görüş bildirme", "görüş yazısı (opinion / for-and-against essay)"],
         ["toplumsal sorunlar", "şehir hayatı ve topluluk", "eğitim ve eşitlik"],
         {"title": "Münazara kulübü", "durationMinutes": 45,
          "goal": "Sınıf iki takıma ayrılır ve güncel bir toplumsal konuyu tartışır (Should public transport be free? Should voting be compulsory?). Her takım 3 argüman hazırlar ve sunarken söylem belirleyicilerini (Firstly, Moreover, However, As a result) kullanır. Karşı takım While it is true that... ile cevap verir. Sonunda herkes kendi görüşünü 4 cümlelik bir paragrafla özetler."})

u.vocab([
    ("issue", "sorun, mesele", "Homelessness is a serious social issue.", "Evsizlik ciddi bir toplumsal sorun.", None),
    ("inequality", "eşitsizlik", "Inequality between rich and poor is growing.", "Zengin ve fakir arasındaki eşitsizlik artıyor.", None),
    ("poverty", "yoksulluk", "Millions of people still live in poverty.", "Milyonlarca insan hâlâ yoksulluk içinde yaşıyor.", None),
    ("homelessness", "evsizlik", "The city has a plan to reduce homelessness.", "Şehrin evsizliği azaltma planı var.", None),
    ("community", "topluluk, toplum", "She does a lot for the local community.", "Yerel topluluk için çok şey yapıyor.", None),
    ("volunteer", "gönüllü; gönüllü olmak", "He volunteers at a food bank every weekend.", "Her hafta sonu bir gıda bankasında gönüllü çalışıyor.", None),
    ("discrimination", "ayrımcılık", "Discrimination at work is illegal.", "İşyerinde ayrımcılık yasa dışıdır.", None),
    ("ageing population", "yaşlanan nüfus", "Many countries have an ageing population.", "Birçok ülkenin yaşlanan bir nüfusu var.", None),
    ("access (to)", "erişim", "Everyone should have access to clean water.", "Herkesin temiz suya erişimi olmalı.", None),
    ("policy", "politika (uygulama)", "The government introduced a new housing policy.", "Hükümet yeni bir konut politikası getirdi.", None),
    ("tackle", "(bir sorunla) mücadele etmek", "We need to tackle climate change now.", "İklim değişikliğiyle hemen mücadele etmeliyiz.", None),
    ("however", "ancak, bununla birlikte", "It's expensive. However, it's worth it.", "Pahalı. Ancak buna değer.", None),
    ("moreover", "üstelik, dahası", "The plan is cheap. Moreover, it's easy to apply.", "Plan ucuz. Üstelik uygulaması kolay.", "resmî"),
    ("nevertheless", "yine de, buna rağmen", "It was risky. Nevertheless, they did it.", "Riskliydi. Yine de yaptılar.", None),
    ("despite", "-e rağmen", "Despite the rain, the event was a success.", "Yağmura rağmen etkinlik başarılıydı.", "+ isim / -ing"),
    ("whereas", "oysa, -iken", "Some people love cities, whereas others prefer villages.", "Bazı insanlar şehirleri severken diğerleri köyleri tercih eder.", None),
    ("therefore", "bu nedenle", "Prices rose. Therefore, sales fell.", "Fiyatlar yükseldi. Bu nedenle satışlar düştü.", None),
    ("as a result", "sonuç olarak", "As a result, many people lost their jobs.", "Sonuç olarak birçok kişi işini kaybetti.", None),
    ("due to", "-den dolayı", "The event was cancelled due to bad weather.", "Etkinlik kötü hava nedeniyle iptal edildi.", "+ isim"),
    ("in conclusion", "sonuç olarak (yazı sonu)", "In conclusion, I believe the benefits outweigh the drawbacks.", "Sonuç olarak, faydaların sakıncalardan ağır bastığına inanıyorum.", None),
    ("outweigh", "-den ağır basmak", "The advantages outweigh the disadvantages.", "Avantajlar dezavantajlardan ağır basıyor.", None),
    ("drawback", "sakınca, dezavantaj", "The main drawback is the cost.", "Asıl sakınca maliyet.", None),
    ("argue", "savunmak, tartışmak", "Some people argue that taxes should be higher.", "Bazı insanlar vergilerin daha yüksek olması gerektiğini savunuyor.", None),
    ("raise awareness", "farkındalık yaratmak", "The campaign aims to raise awareness of mental health.", "Kampanya ruh sağlığı konusunda farkındalık yaratmayı amaçlıyor.", None),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Üstelik ve ancak", "Ekleme ve karşıtlık bildiren bağlaçları ve söylem belirleyicilerini doğru yapı ve noktalamayla kullanabilirim.",
    {"kind": "text", "title": "Görüş köşesi: Ücretsiz toplu taşıma", "body": "Several European cities have made public transport completely free. Should our city do the same?\n\nFree buses and trams would reduce traffic. Moreover, they would help families on low incomes, who spend a large part of their budget on travel. In addition, fewer cars would mean cleaner air.\n\nHowever, the plan has some serious drawbacks. Free transport would cost the city millions every year. Although supporters say the money would come from parking fees, critics doubt that this would be enough.\n\nDespite these concerns, I believe the idea is worth trying. Some cities have seen a big increase in passengers, whereas others have seen very little change in traffic. Nevertheless, even a small improvement in air quality would benefit everyone.",
     "questions": [
        mc("Who would free transport especially help?", ["Tourists", "Families on low incomes", "Car owners"], 1, "\"help families on low incomes\""),
        mc("What is the main drawback?", ["It would be slow.", "It would cost the city millions.", "Nobody would use it."], 1, "\"cost the city millions every year\""),
     ]},
    {"explanation": "**Ekleme:**\n\n| Kelime | Yapı | Örnek |\n|---|---|---|\n| **and, also** | cümle içinde | It's cheap **and** fast. |\n| **In addition, / Moreover, / Furthermore,** | cümle başında + **virgül** | **Moreover,** it's eco-friendly. |\n| **as well as** | + isim / -ing | **As well as** reducing traffic, it would ... |\n\n**Karşıtlık:**\n\n| Kelime | Yapı | Örnek |\n|---|---|---|\n| **but** | iki cümleyi bağlar | It's cheap, **but** it's slow. |\n| **However, / Nevertheless,** | **yeni cümle** başında + virgül | It's cheap. **However,** it's slow. |\n| **although / even though** | + **özne + fiil** | **Although** it's cheap, it's slow. |\n| **despite / in spite of** | + **isim / -ing** | **Despite** the cost, ... / **Despite being** cheap, ... |\n| **whereas / while** | iki zıt durumu karşılaştırır | Cities are noisy, **whereas** villages are quiet. |\n\n**En sık hatalar:**\n\n- ~~Despite it is expensive~~ → **Although** it is expensive / **Despite** the cost / **Despite being** expensive\n- ~~Despite of~~ → **Despite** / **In spite of**\n- ~~It's cheap, however it's slow.~~ → It's cheap. **However,** it's slow. (ya da: It's cheap; however, it's slow.)\n\n**Not:** *Despite the fact that* + özne + fiil de kullanılabilir.",
     "examples": [{"en": "Although the plan is expensive, it would benefit everyone.", "tr": "Plan pahalı olsa da herkese fayda sağlar."},
                  {"en": "Despite the rain, thousands of people joined the protest.", "tr": "Yağmura rağmen binlerce kişi eyleme katıldı."},
                  {"en": "Young people tend to support the idea, whereas older people are less sure.", "tr": "Gençler fikri destekleme eğilimindeyken yaşlılar daha az emin."}],
     "turkishNote": "Türkçede \"-e rağmen\" ve \"-mesine rağmen\" aynı kelimeyle kurulur, ama İngilizcede yapı değişir: despite + isim (yağmura rağmen = despite the rain), although + cümle (yağmasına rağmen = although it was raining). \"Despite it was raining\" Türkçe konuşanların en sık hatasıdır. Ayrıca \"however\" bir bağlaç değildir; iki cümleyi virgülle birleştiremez."},
    [
        mc("Hangisi doğru?", ["Despite it was cold, we went out.", "Although it was cold, we went out."], 1, "although + cümle."),
        mc("Hangisi doğru?", ["Despite the cold, we went out.", "Although the cold, we went out."], 0, "despite + isim."),
        mc("Hangisi doğru?", ["Despite of the cost, they did it.", "Despite the cost, they did it."], 1, "Despite of yok."),
        mc("Doğru noktalama:", ["It's cheap, however it's slow.", "It's cheap. However, it's slow."], 1, "However yeni cümle + virgül."),
        gap("The plan is cheap. ___, it's easy to apply. (Üstelik)", ["Moreover", "Furthermore", "In addition", "What's more"], "Ekleme."),
        gap("___ being very popular, the shop closed. (rağmen)", ["Despite"], "Despite + -ing."),
        gap("Some people prefer cities, ___ others prefer the countryside. (oysa)", ["whereas", "while"], "whereas."),
        gap("It was a difficult year. ___, we achieved our goals. (Yine de)", ["Nevertheless", "However"], "Nevertheless."),
        listen("Living in a big city has many advantages. There are more jobs, and moreover, there's always something to do. However, the cost of living is high. Although I love the energy of the city, I sometimes dream of moving to a small town.", "Konuşanın şehir hakkındaki asıl şikâyeti ne?", ["İş yok", "Hayat pahalı", "Yapacak bir şey yok"], 1, "\"However, the cost of living is high.\""),
        typ("Birleştirin (Despite ile başlayın): \"It was raining. The festival was a success.\"", variants("Despite the rain, the festival was a success.", "Despite the rain the festival was a success.", "Despite the fact that it was raining, the festival was a success."), "Despite the rain, the festival was a success."),
    ],
    {"kind": "speaking", "task": speak("\"Should public transport be free?\" sorusu hakkında 1 dakikalık bir görüş açıklayın. En az 2 ekleme (moreover, in addition, as well as) ve en az 3 karşıtlık (however, although, despite, whereas) yapısı kullanın.",
                                       "I think public transport should be free, at least for students and older people. It would reduce traffic. Moreover, it would help people on low incomes. In addition, it would be good for the environment. However, it would be very expensive for the city. Although some people say the money could come from higher taxes, I don't think that's fair for everyone. Despite these problems, I believe it's worth trying, because young people tend to use buses a lot, whereas older people often drive.",
                                       ["Ekleme yapıları", "Karşıtlık yapıları", "Doğru yapı (despite + isim, although + cümle)"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "Neden ve sonuç", "Neden, sonuç ve amaç bildiren yapıları (due to, as a result, therefore, so that, in order to) doğru kullanabilirim.",
    {"kind": "text", "title": "Haber analizi: Köyler neden boşalıyor?", "body": "Over the last fifty years, millions of people in Turkey have moved from villages to cities. As a result, many villages now have only a few elderly residents.\n\nThe main reason is the lack of jobs. Due to modern farming methods, fewer people are needed to work the land. Young people therefore leave in order to find work or study at university.\n\nAnother factor is access to services. Because many villages don't have hospitals or secondary schools, families move so that their children can get a better education.\n\nConsequently, cities have grown rapidly, which has led to problems such as traffic, high rents and pollution.\n\nIn recent years, however, some young people have started moving back to villages. Thanks to fast internet, they can work remotely and enjoy a quieter life.",
     "questions": [
        mc("Why are fewer people needed to work the land?", ["Because of modern farming methods", "Because the land is poor", "Because of bad weather"], 0, "\"Due to modern farming methods\""),
        mc("Why are some young people moving back?", ["Rents are lower in cities.", "Fast internet lets them work remotely.", "The government pays them."], 1, "\"Thanks to fast internet, they can work remotely\""),
     ]},
    {"explanation": "**Neden:**\n\n| Kelime | Yapı | Örnek |\n|---|---|---|\n| **because / as / since** | + özne + fiil | **Because** there are no jobs, people leave. |\n| **because of / due to / owing to** | + **isim** | **Due to** the lack of jobs, people leave. |\n| **thanks to** | + isim (olumlu sebep) | **Thanks to** the internet, they can work remotely. |\n\n**Sonuç:**\n\n| Kelime | Yapı | Örnek |\n|---|---|---|\n| **so** | cümle içinde | There are no jobs, **so** people leave. |\n| **As a result, / Consequently, / Therefore,** | yeni cümle başında + virgül | **As a result,** villages are empty. |\n| **therefore** (cümle ortasında) | özne + **therefore** + fiil | Young people **therefore** leave. |\n| **lead to / result in** | + isim | Growth **has led to** traffic problems. |\n\n**Amaç:**\n\n| Kelime | Yapı | Örnek |\n|---|---|---|\n| **to / in order to** | + fiil | They leave **in order to** find work. |\n| **so that** | + özne + **can / could / will / would** | They move **so that** their children **can** study. |\n| **in order not to** | + fiil (olumsuz) | **in order not to** be late |\n\n**Dikkat:**\n\n- ~~Due to there are no jobs~~ → **Due to the lack of** jobs / **Because** there are no jobs\n- ~~for to find work~~ → **to** find work / **in order to** find work",
     "examples": [{"en": "Due to the storm, all flights were cancelled.", "tr": "Fırtına nedeniyle bütün uçuşlar iptal edildi."},
                  {"en": "Prices rose sharply. As a result, many people cut back on spending.", "tr": "Fiyatlar keskin bir şekilde yükseldi. Sonuç olarak birçok kişi harcamalarını azalttı."},
                  {"en": "They saved money so that they could buy a house.", "tr": "Ev alabilmek için para biriktirdiler."}],
     "turkishNote": "Türkçede \"-dığı için\" ve \"-den dolayı\" yapıları birbirine yakındır; İngilizcede ise because + cümle, because of / due to + isim kullanılır. \"Due to it was raining\" yanlıştır. Amaç için Türkçedeki \"-mek için\" yapısı \"for to\" diye çevrilmemelidir: \"I came for to see you\" yanlış, \"I came to see you\" doğrudur."},
    [
        mc("Hangisi doğru?", ["Due to the rain, the match was cancelled.", "Due to it rained, the match was cancelled."], 0, "due to + isim."),
        mc("Hangisi doğru?", ["I went there for to study.", "I went there to study."], 1, "to + fiil."),
        mc("Olumlu sebep:", ["Thanks to her help, I passed.", "Due to her help, I passed."], 0, "thanks to (olumlu)."),
        mc("\"so that\" ardından:", ["fiilin yalın hali", "özne + can / could"], 1, "so that + özne + modal."),
        gap("The factory closed. As a ___, 500 people lost their jobs.", ["result"], "As a result."),
        gap("She studied hard so ___ she could get a scholarship.", ["that"], "so that."),
        gap("High rents have led ___ an increase in homelessness.", ["to"], "lead to."),
        gap("The flight was delayed ___ to bad weather.", ["due", "owing"], "due to / owing to."),
        listen("Our neighbourhood has changed a lot. Thanks to the new metro line, it's much easier to get to the city centre. As a result, house prices have risen sharply. Consequently, many young families can't afford to live here any more.", "Metro hattının sonucu ne oldu?", ["Ev fiyatları düştü", "Ev fiyatları keskin bir şekilde yükseldi", "Trafik arttı"], 1, "\"As a result, house prices have risen sharply.\""),
        typ("Birleştirin (so that): \"He spoke slowly. Everyone could understand him.\"", variants("He spoke slowly so that everyone could understand him.", "He spoke slowly, so that everyone could understand him."), "He spoke slowly so that everyone could understand him."),
    ],
    {"kind": "speaking", "task": speak("Şehrinizde ya da ülkenizde son yıllarda değişen bir toplumsal durumu anlatın (göç, kira artışı, uzaktan çalışma, nüfus yaşlanması, vb.). Nedenlerini (due to, because of, as), sonuçlarını (as a result, therefore, has led to) ve insanların bu değişime karşı neler yaptığını (in order to, so that) anlatın.",
                                       "In my city, more and more people are working from home. This is mainly due to the pandemic, when companies had to close their offices. As a result, many people realised that they didn't need to live in the city centre. Therefore, they moved to smaller towns nearby, where houses are cheaper. This has led to higher prices in those towns too. Some companies now offer shared offices in suburbs so that people can work near their homes. People also take online courses in order to learn new digital skills.",
                                       ["Neden yapıları", "Sonuç yapıları", "Amaç yapıları", "Doğru noktalama"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "Paragraf kurmak", "Bir topic sentence, destekleyici cümleler, örnekler ve sonuç cümlesiyle iyi yapılandırılmış bir paragraf yazabilirim.",
    {"kind": "text", "title": "İki paragraf: hangisi daha iyi?", "body": "Paragraph A:\nVolunteering is good. My friend volunteers. It's nice. You meet people. Some people don't have time. I volunteered once at an animal shelter. Also it's good for your CV.\n\nParagraph B:\nVolunteering benefits both the community and the volunteers themselves. Firstly, it provides essential help to people and organisations that cannot afford to pay for it, such as food banks, animal shelters and care homes. Secondly, volunteers often develop valuable skills, including teamwork, communication and leadership, which can improve their job prospects. For instance, a recent survey found that many employers see volunteering experience as an advantage. Finally, research suggests that helping others can reduce stress and increase happiness. For these reasons, volunteering should be encouraged in schools and workplaces.",
     "questions": [
        mc("Which paragraph has a clear topic sentence?", ["Paragraph A", "Paragraph B"], 1, "\"Volunteering benefits both the community and the volunteers themselves.\""),
        mc("How many reasons does Paragraph B give?", ["Two", "Three", "Five"], 1, "Firstly, Secondly, Finally."),
     ]},
    {"explanation": "**İyi bir paragrafın yapısı:**\n\n| Bölüm | İşlev | Örnek |\n|---|---|---|\n| **1. Topic sentence** | Paragrafın ana fikri. Genellikle ilk cümle. | *Volunteering benefits both the community and the volunteers.* |\n| **2. Supporting sentences** | Ana fikri destekleyen gerekçeler | *Firstly, ... Secondly, ...* |\n| **3. Examples / evidence** | Somut örnek, rakam, deneyim | *For instance, ... / such as ...* |\n| **4. Concluding sentence** | Ana fikri bağlayan / özetleyen cümle | *For these reasons, ...* |\n\n**Sıralama:** *Firstly / First of all, ... Secondly, ... Thirdly, ... Finally / Lastly, ...*\n\n**Örnek verme:**\n\n| Yapı | Örnek |\n|---|---|\n| **For example, / For instance,** | cümle başında + virgül |\n| **such as** | + isim: *places **such as** food banks* |\n| **including** | + isim: *skills, **including** teamwork* |\n| **like** | (daha samimi) |\n\n**İyi bir topic sentence:**\n\n- Çok genel değil: ~~Volunteering is good.~~\n- Çok dar değil: ~~I volunteered at an animal shelter.~~\n- Tartışılabilir ve net: ✓ *Volunteering benefits both the community and the volunteers themselves.*\n\n**Kural:** Bir paragraf = **bir ana fikir**. Yeni bir fikir yeni bir paragraf ister.",
     "examples": [{"en": "Social media has changed the way young people communicate.", "tr": "Sosyal medya gençlerin iletişim kurma şeklini değiştirdi. (topic sentence)"},
                  {"en": "Many cities, such as Amsterdam and Copenhagen, have excellent cycle lanes.", "tr": "Amsterdam ve Kopenhag gibi birçok şehrin mükemmel bisiklet yolları var."},
                  {"en": "For these reasons, I believe the law should be changed.", "tr": "Bu nedenlerden dolayı yasanın değişmesi gerektiğine inanıyorum."}],
     "turkishNote": "Türkçe kompozisyonda paragraflar bazen uzun bir girişle ya da bir hikâyeyle başlar ve ana fikir sona saklanır. İngilizce akademik ve sınav yazısında ana fikir genellikle paragrafın ilk cümlesinde (topic sentence) açıkça verilir. Okuyucu sadece ilk cümleleri okuyarak bütün metnin özetini çıkarabilmelidir."},
    [
        mc("En iyi topic sentence:", ["Social media is a thing.", "Social media has both positive and negative effects on teenagers.", "I use Instagram every day."], 1, "Net ve tartışılabilir."),
        mc("Paragrafın son cümlesinin işlevi:", ["Yeni bir fikir eklemek", "Ana fikri bağlamak / özetlemek"], 1, "Concluding sentence."),
        mc("Hangisi doğru?", ["Cities such as London and Paris are expensive.", "Cities for example London and Paris are expensive."], 0, "such as + isim."),
        mc("Bir paragrafta kaç ana fikir olmalı?", ["Bir", "Üç ya da daha fazla"], 0, "Bir paragraf = bir fikir."),
        gap("___, it saves money. Secondly, it's good for the environment. (İlk olarak)", ["Firstly", "First"], "Firstly."),
        gap("Volunteers develop skills, ___ teamwork and leadership. (dahil)", ["including"], "including."),
        gap("For ___, many companies now offer volunteering days. (örneğin)", ["instance", "example"], "For instance / example."),
        gap("For these ___, schools should encourage volunteering. (nedenler)", ["reasons"], "For these reasons."),
        listen("Today I'll show you how to write a good paragraph. Start with a clear topic sentence that tells the reader your main idea. Then give two or three supporting points, each with an example. Finally, finish with a sentence that links back to your main idea. Remember: one paragraph, one idea.", "Konuşana göre paragraf nasıl başlamalı?", ["Bir örnekle", "Net bir topic sentence ile", "Bir soruyla"], 1, "\"Start with a clear topic sentence\""),
        order(["Firstly", "volunteering", "provides", "help", "to", "people", "who", "need", "it"], "Firstly volunteering provides help to people who need it.", "Sıralayıcı + ana cümle.", "İlk olarak, gönüllülük ihtiyacı olan insanlara yardım sağlar."),
    ],
    {"kind": "speaking", "task": speak("Aşağıdaki konulardan birini seçin ve sözlü bir \"paragraf\" kurun (1 dakika): (a) Learning a foreign language at a young age has many benefits. (b) Cities should have more green spaces. Topic sentence ile başlayın, Firstly / Secondly / Finally ile 3 destekleyici nokta verin, en az bir örnek (for instance, such as) ekleyin ve bir sonuç cümlesiyle bitirin.",
                                       "Cities should have more green spaces. Firstly, parks and gardens improve people's physical health, because they encourage walking, running and cycling. Secondly, green spaces are good for mental health. For instance, studies suggest that spending time in nature can reduce stress. Finally, trees and plants help to clean the air and keep cities cooler in summer, which is important as temperatures rise. For these reasons, I believe every neighbourhood should have a park within walking distance.",
                                       ["Topic sentence", "Sıralı destekleyici noktalar", "Örnek", "Sonuç cümlesi"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Dengeli görüş", "Toplumsal konularda farklı görüşleri dengeli bir şekilde sunabilir, karşı görüşü kabul edip cevaplayabilir ve kendi görüşümü belirtebilirim.",
    {"kind": "dialogue", "title": "Radyo programı: Sosyal medya yasakları", "lines": [
        {"speaker": "Host", "text": "Today's question: should children under sixteen be banned from social media? Dr Yalçın, what's your view?"},
        {"speaker": "Dr Yalçın", "text": "On the one hand, there's growing evidence that heavy use can affect young people's mental health. On the other hand, a complete ban might be very difficult to enforce."},
        {"speaker": "Host", "text": "Some parents argue that it's their decision, not the government's."},
        {"speaker": "Dr Yalçın", "text": "That's a valid point. While it is true that parents know their children best, many of them feel they can't control it alone."},
        {"speaker": "Host", "text": "So, where do you stand?"},
        {"speaker": "Dr Yalçın", "text": "Personally, I'm not in favour of a total ban. I believe it would be more effective to teach children how to use social media safely and to make platforms more responsible."}],
     "questions": [
        mc("What is one problem with a ban, according to Dr Yalçın?", ["It's too cheap.", "It might be difficult to enforce.", "Children don't use social media."], 1, "\"very difficult to enforce\""),
        mc("What does Dr Yalçın suggest instead?", ["A total ban", "Teaching children to use it safely", "Doing nothing"], 1, "\"teach children how to use social media safely\""),
     ]},
    {"explanation": "**İki tarafı sunmak:**\n\n| Kalıp | Örnek |\n|---|---|\n| **On the one hand, ... On the other hand, ...** | **On the one hand,** it's cheap. **On the other hand,** it's slow. |\n| **Some people argue / believe / claim that ...** | **Some people argue that** taxes should be higher. |\n| **Others / Critics, however, ...** | **Critics, however,** say it's unfair. |\n| **It could be argued that ...** | **It could be argued that** bans don't work. (kişisiz, resmî) |\n| **Supporters / Opponents of ... say ...** | **Opponents of** the plan say ... |\n\n**Karşı görüşü kabul edip cevaplamak (concession):**\n\n| Kalıp | Örnek |\n|---|---|\n| **While it is true that ..., ...** | **While it is true that** it's expensive, it would save money in the long term. |\n| **That's a valid point, but ...** | (konuşmada) |\n| **Admittedly, ... However, ...** | **Admittedly,** there are risks. **However,** ... |\n\n**Kendi görüşünü belirtmek:**\n\n| Samimi → Resmî |\n|---|\n| I think ... / In my opinion, ... / Personally, I believe ... |\n| From my point of view, ... / In my view, ... |\n| I am (not) in favour of ... / I am strongly against ... |\n| **It seems to me that** ... / **I would argue that** ... |\n\n**Dikkat:** ~~According to me~~ İngilizcede doğal değildir. → **In my opinion** / **In my view**",
     "examples": [{"en": "On the one hand, technology connects us. On the other hand, it can make us feel lonely.", "tr": "Bir yandan teknoloji bizi birbirimize bağlıyor. Öte yandan bizi yalnız hissettirebilir."},
                  {"en": "While it is true that cars are convenient, they cause a lot of pollution.", "tr": "Arabaların kullanışlı olduğu doğru olsa da çok fazla kirliliğe neden oluyorlar."},
                  {"en": "Personally, I am in favour of a four-day working week.", "tr": "Şahsen dört günlük çalışma haftasından yanayım."}],
     "turkishNote": "Türkçedeki \"bana göre\" ifadesini \"according to me\" diye çevirmek çok yaygın bir hatadır; İngilizcede \"according to\" başkalarının görüşü için kullanılır (according to experts). Kendi görüşünüz için \"In my opinion\" ya da \"In my view\" deyin. Ayrıca İngilizce tartışma kültüründe karşı görüşü önce kabul etmek (While it is true that...) daha güçlü ve ikna edici bir izlenim bırakır."},
    [
        mc("Kendi görüşünüz için:", ["According to me, ...", "In my opinion, ..."], 1, "In my opinion."),
        mc("Karşı görüşü kabul etmek:", ["While it is true that ..., ...", "Because ..., ..."], 0, "Concession."),
        mc("Resmî ve kişisiz:", ["I think bans don't work.", "It could be argued that bans don't work."], 1, "It could be argued."),
        mc("\"On the one hand\" ile eşleşen:", ["On the other hand", "On the other side"], 0, "On the other hand."),
        gap("Some people ___ that the law is unfair. (savunuyor)", ["argue", "believe", "claim", "think"], "argue that."),
        gap("I am not in ___ of the new law. (yanında)", ["favour", "favor"], "in favour of."),
        gap("___ it is true that it's expensive, it would save lives. (... doğru olsa da)", ["While", "Although"], "While it is true that."),
        gap("___, there are some risks. However, the benefits are greater. (Kabul etmek gerekir ki)", ["Admittedly"], "Admittedly."),
        listen("Supporters of the new tax say it will raise money for hospitals and schools. Critics, however, argue that it will hit poorer families the hardest. Personally, I think it's a good idea, as long as low-income households are protected.", "Konuşanın görüşü ne?", ["Vergiye tamamen karşı", "Düşük gelirliler korunursa iyi bir fikir", "Fikri yok"], 1, "\"as long as low-income households are protected\""),
        typ("İngilizcesi: \"Bana göre bu iyi bir fikir değil.\"", variants("In my opinion, this isn't a good idea.", "In my opinion, it isn't a good idea.", "In my view, this isn't a good idea.", "In my opinion, this is not a good idea.", "In my opinion, it's not a good idea.", "In my opinion this isn't a good idea."), "In my opinion, this isn't a good idea."),
    ],
    {"kind": "speaking", "task": speak("Bir radyo programına konuk olarak katıldığınızı düşünün. Konu: \"Should university education be free for everyone?\" İki tarafı da sunun (On the one hand / On the other hand, Some people argue / Critics say), karşı görüşü kabul edip cevaplayın (While it is true that ...) ve kendi görüşünüzü belirtin (Personally, I am in favour of / against ...).",
                                       "That's a difficult question. On the one hand, free university education would give everyone the same opportunities, regardless of their family's income. Some people argue that education is a right, not a privilege. On the other hand, it would be extremely expensive, and critics say taxpayers who never went to university would be paying for others. While it is true that it would cost a lot, I think an educated population benefits the whole country in the long run. Personally, I'm in favour of free education, but perhaps students should do some community work in return.",
                                       ["İki tarafı sunma", "Concession", "Kendi görüşünü belirtme", "Akıcı ve dengeli konuşma"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Görüş yazısı", "Giriş, gelişme ve sonuç bölümleriyle, söylem belirleyicileri ve dengeli argümanlar içeren B2 sınav standartlarında bir essay yazabilirim.",
    {"kind": "text", "title": "Örnek essay: Should the minimum voting age be 16?", "body": "In many countries, people can vote from the age of 18. However, some countries, such as Austria, have lowered the voting age to 16. This essay will examine both sides of the argument before giving my own opinion.\n\nThose in favour of votes at 16 argue that young people are directly affected by political decisions, for example on education and the environment. Moreover, at sixteen, many young people work, pay taxes and can even get married in some countries. Therefore, it seems fair that they should have a voice.\n\nOn the other hand, critics claim that most sixteen-year-olds are not mature enough to make political decisions. They also point out that young people might be easily influenced by their parents, teachers or social media.\n\nWhile it is true that some teenagers are not interested in politics, the same can be said of many adults. In fact, research suggests that people who vote at a young age are more likely to keep voting throughout their lives.\n\nIn conclusion, although there are valid concerns, I believe the benefits of lowering the voting age outweigh the drawbacks. If combined with better political education in schools, votes at 16 could create a more active and engaged generation.",
     "questions": [
        mc("Which country is given as an example?", ["Germany", "Austria", "Turkey"], 1, "\"such as Austria\""),
        mc("What is the writer's final opinion?", ["Against lowering the voting age", "The benefits outweigh the drawbacks", "No opinion"], 1, "\"the benefits... outweigh the drawbacks\""),
     ]},
    {"explanation": "**Görüş yazısının (opinion / for-and-against essay) yapısı:**\n\n| Paragraf | İçerik | Kalıplar |\n|---|---|---|\n| **1. Giriş** | Konuyu tanıt, bağlam ver, yazının amacını söyle | *In many countries, ... / Nowadays, ... / This essay will examine ...* |\n| **2. Gelişme 1** | Bir tarafın argümanları + örnekler | *Those in favour of ... argue that ... / Firstly, ... Moreover, ...* |\n| **3. Gelişme 2** | Diğer tarafın argümanları | *On the other hand, critics claim that ... / They also point out that ...* |\n| **4. (İsteğe bağlı) Concession** | Karşı görüşü cevapla | *While it is true that ..., ...* |\n| **5. Sonuç** | Özetle + kendi görüşün | *In conclusion, / To sum up, / All things considered, ... I believe ...* |\n\n**Essay'de kaçınılması gerekenler:**\n\n- **Kısaltmalar:** ~~don't, it's~~ → do not, it is\n- **Çok samimi dil:** ~~stuff, kids, a lot of~~ → things, children, many / a great deal of\n- **Sonuçta yeni argüman** eklemek\n- **\"I\"yi aşırı kullanmak:** Görüşünüzü genellikle giriş ya da sonuçta belirtin.\n- **Kanıtsız mutlak ifadeler:** ~~Everyone knows that ...~~ → *Many people believe that ...*\n\n**Sınav ipucu (B2 First vb.):** Soruyu dikkatle okuyun, istenen her noktaya cevap verin, kelime sınırına uyun (genellikle 140–190 ya da 200–250) ve 5 dakikanızı plan için ayırın.",
     "examples": [{"en": "This essay will examine both sides of the argument.", "tr": "Bu yazı tartışmanın her iki tarafını da inceleyecek."},
                  {"en": "Those in favour of the idea argue that it would reduce crime.", "tr": "Fikri destekleyenler bunun suçu azaltacağını savunuyor."},
                  {"en": "All things considered, I believe the advantages outweigh the disadvantages.", "tr": "Her şey göz önüne alındığında avantajların dezavantajlardan ağır bastığına inanıyorum."}],
     "turkishNote": "Türkçe kompozisyonda giriş-gelişme-sonuç yapısı bilinir, ama İngilizce essay'de her paragrafın tek bir işlevi vardır ve bu işlev topic sentence'ta açıkça belirtilir. Türk öğrencilerin sık yaptığı hata, sonuç bölümünde yeni bir argüman eklemek ya da girişte çok uzun bir genel giriş yapmaktır (\"Since the beginning of human history...\"). Kısa, net ve konuya odaklı bir giriş en iyisidir."},
    [
        mc("Essay girişinde hangisi uygun?", ["Since the beginning of time, humans have always ...", "In many countries, people can vote from the age of 18."], 1, "Kısa ve konuya odaklı."),
        mc("Essay'de hangisi uygun?", ["Kids don't care about politics.", "Many young people are not interested in politics."], 1, "Resmî ve temkinli."),
        mc("Sonuç bölümünde ne yapılmaz?", ["Görüşü belirtmek", "Yeni bir argüman eklemek", "Özetlemek"], 1, "Yeni argüman yok."),
        mc("Hangisi bir sonuç kalıbı?", ["All things considered,", "For instance,"], 0, "All things considered."),
        gap("This essay will ___ both sides of the argument. (incelemek)", ["examine", "discuss", "consider"], "examine."),
        gap("___ in favour of the law argue that it would save lives. (Destekleyenler)", ["Those"], "Those in favour of."),
        gap("The benefits ___ the drawbacks. (ağır basmak)", ["outweigh"], "outweigh."),
        gap("In ___, I believe the law should be changed. (Sonuç olarak)", ["conclusion"], "In conclusion."),
        listen("When you write your essay, plan for five minutes first. Write a short introduction, then two body paragraphs, one for each side. Don't forget your own opinion in the conclusion, and never add a new argument at the end. Finally, check your word count and use formal language.", "Konuşana göre sonuç bölümünde ne yapılmamalı?", ["Görüş bildirmek", "Yeni argüman eklemek", "Özet yapmak"], 1, "\"never add a new argument at the end\""),
        typ("Resmîleştirin: \"Lots of kids don't eat healthy stuff.\"", variants("Many children do not eat healthy food.", "Many children do not eat healthily.", "A large number of children do not eat healthy food."), "Many children do not eat healthy food."),
    ],
    {"kind": "writing", "task": write("Aşağıdaki essay sorusuna cevap verin (200–250 kelime): \"Some people believe that all young people should do one year of community service (helping in hospitals, schools, or environmental projects) after finishing school. Do you agree?\" Giriş, iki gelişme paragrafı ve bir sonuç yazın. Her paragrafa net bir topic sentence koyun; ekleme, karşıtlık, neden-sonuç ve örnek verme yapılarını kullanın; karşı görüşü kabul edip cevaplayın ve resmî bir üslup kullanın.",
                                      "In some countries, young people are expected to spend a period of time serving their community after leaving school. This essay will consider the advantages and disadvantages of making one year of community service compulsory.\n\nThose in favour of the idea argue that it would benefit both society and young people themselves. Firstly, hospitals, schools and environmental organisations often lack staff, and young volunteers could provide valuable support. Moreover, working with people from different backgrounds would help young people develop skills such as teamwork, patience and communication. As a result, they might become more responsible and confident adults.\n\nOn the other hand, critics claim that a compulsory year would delay young people's education and careers. Some students, for instance, might lose motivation to go to university after a year away from studying. In addition, forcing people to volunteer could mean that they do the work without real interest or care.\n\nWhile it is true that a compulsory year has some drawbacks, I believe these could be reduced with careful planning. For example, young people could choose the type of service that suits their interests, and the year could count towards university applications.\n\nIn conclusion, although community service should perhaps not be strictly compulsory, I believe it should be strongly encouraged. All things considered, the benefits for society and for young people outweigh the disadvantages.",
                                      ["Net giriş ve yapı", "Topic sentence'lar", "Söylem belirleyicileri ve doğru noktalama", "Concession ve dengeli argüman", "Resmî üslup ve net sonuç"])},
)

u.test([
    mc("Hangisi doğru?", ["Despite it was late, we continued.", "Although it was late, we continued."], 1, "although + cümle"),
    mc("Hangisi doğru?", ["Due to the strike, trains were cancelled.", "Due to there was a strike, trains were cancelled."], 0, "due to + isim"),
    mc("Doğru noktalama:", ["It's useful, however it's expensive.", "It's useful. However, it's expensive."], 1, "However,"),
    mc("Kendi görüşünüz:", ["According to me, ...", "In my view, ..."], 1, "In my view"),
    mc("Essay'de hangisi uygun?", ["Lots of people think it's a bad idea.", "Many people believe it is a bad idea."], 1, "Resmî"),
    gap("___ the rain, the concert went ahead. (rağmen)", ["Despite"], "Despite + isim"),
    gap("Cities are noisy, ___ villages are usually quiet. (oysa)", ["whereas", "while"], "whereas"),
    gap("The factory closed. As a ___, many people lost their jobs.", ["result"], "As a result"),
    gap("She saved money so ___ she could travel.", ["that"], "so that"),
    gap("___ it is true that it costs a lot, it would help many people. (... doğru olsa da)", ["While", "Although"], "While it is true that"),
    gap("In ___, I believe the advantages outweigh the disadvantages. (Sonuç olarak)", ["conclusion"], "In conclusion"),
    mc("Örnek verme:", ["Many cities, such as Rome and Madrid, are popular.", "Many cities, therefore Rome and Madrid, are popular."], 0, "such as"),
    listen("On the one hand, working from home saves time and money. On the other hand, many people feel isolated. Personally, I'm in favour of a mix: two days in the office and three at home.", "Konuşanın görüşü ne?", ["Tamamen evden çalışmak", "Karma bir model", "Tamamen ofiste çalışmak"], 1, "\"I'm in favour of a mix\""),
    typ("Birleştirin (Although ile başlayın): \"The plan is expensive. It would benefit everyone.\"", variants("Although the plan is expensive, it would benefit everyone.", "Although the plan is expensive it would benefit everyone."), "Although the plan is expensive, it would benefit everyone."),
    write("Aşağıdaki essay sorusuna cevap verin (200–250 kelime): \"Technology has made our lives better, but it has also made people more isolated. Discuss both views and give your own opinion.\" Giriş, iki gelişme ve sonuç paragrafı yazın; topic sentence'lar, ekleme / karşıtlık / neden-sonuç bağlaçları, örnekler, concession ve resmî üslup kullanın.",
          "Over the past twenty years, technology has transformed almost every area of our lives, from the way we work to the way we communicate. While many people believe that it has improved our quality of life, others argue that it has made us more isolated. This essay will examine both views.\n\nThere is no doubt that technology has brought enormous benefits. Firstly, it allows us to stay in touch with friends and family all over the world. For instance, video calls mean that grandparents can see their grandchildren every day, even if they live in another country. Moreover, technology has made many tasks faster and easier, such as banking, shopping and studying. As a result, people have more free time and more opportunities.\n\nOn the other hand, critics claim that technology has damaged face-to-face relationships. Many people spend hours on their phones, even when they are with friends. In addition, some research suggests that heavy use of social media is linked to loneliness, particularly among teenagers.\n\nWhile it is true that technology can be used in unhealthy ways, I would argue that the problem lies in how we use it, not in the technology itself. Used wisely, it can bring people together rather than push them apart.\n\nIn conclusion, although technology has created some new social problems, I believe it has made our lives better overall. The key is to find a healthy balance between our online and offline lives.",
          ["Net giriş ve paragraf yapısı", "Söylem belirleyicileri", "İki görüşün dengeli sunumu", "Concession ve görüş", "Resmî üslup"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

"""A1 Ünite 12: Hafta sonu."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("A1", 12, "Hafta sonu", "Last Weekend",
         "Geçen hafta sonu ve geçmişte neler yaptığımı basit cümlelerle anlatabilir, başkalarına sorabilirim.",
         ["was / were", "past simple: düzenli fiiller (-ed)", "past simple: didn't ve Did ...?", "zaman ifadeleri: yesterday, last, ago", "ilk düzensiz fiiller: went, had"],
         ["hafta sonu etkinlikleri", "geçmiş zaman ifadeleri", "olay sıralama"],
         {"title": "Hafta sonu röportajı", "durationMinutes": 45,
          "goal": "Öğrenciler ikili olarak birbirine geçen hafta sonunu sorar (Where were you? Did you...? What did you do?), not alır ve partnerinin hafta sonunu sınıfa anlatır. Sınıf en ilginç hafta sonunu oylar."})

u.vocab([
    ("yesterday", "dün", "I was at home yesterday.", "Dün evdeydim.", None),
    ("last night", "dün gece", "I watched a film last night.", "Dün gece film izledim.", "yesterday night denmez."),
    ("last weekend", "geçen hafta sonu", "What did you do last weekend?", "Geçen hafta sonu ne yaptın?", "last week, last month, last year"),
    ("ago", "önce", "I started this course two months ago.", "Bu kursa iki ay önce başladım.", "süre + ago"),
    ("visit", "ziyaret etmek", "We visited my grandparents.", "Büyükannemi ve büyükbabamı ziyaret ettik.", None),
    ("stay", "kalmak", "I stayed at home on Sunday.", "Pazar evde kaldım.", None),
    ("relax", "dinlenmek, rahatlamak", "I relaxed in the garden.", "Bahçede dinlendim.", None),
    ("clean", "temizlemek", "We cleaned the flat on Saturday.", "Cumartesi daireyi temizledik.", None),
    ("watch", "izlemek", "Did you watch the match?", "Maçı izledin mi?", None),
    ("listen to", "dinlemek", "I listened to a podcast.", "Bir podcast dinledim.", None),
    ("walk", "yürümek", "We walked by the sea.", "Deniz kenarında yürüdük.", None),
    ("cook", "yemek yapmak", "My husband cooked dinner.", "Eşim akşam yemeği yaptı.", None),
    ("study", "ders çalışmak", "I studied for my exam.", "Sınavıma çalıştım.", "study → studied"),
    ("invite", "davet etmek", "They invited us to dinner.", "Bizi akşam yemeğine davet ettiler.", None),
    ("arrive", "varmak", "We arrived late.", "Geç vardık.", "arrive in + şehir, arrive at + yer"),
    ("start", "başlamak", "The film started at eight.", "Film sekizde başladı.", None),
    ("finish", "bitirmek, bitmek", "I finished my book.", "Kitabımı bitirdim.", None),
    ("went (go)", "gitti (gitmek)", "I went to the cinema.", "Sinemaya gittim.", "Düzensiz: go → went."),
    ("had (have)", "vardı; yedi/içti (sahip olmak)", "We had breakfast in a café.", "Bir kafede kahvaltı yaptık.", "Düzensiz: have → had."),
    ("picnic", "piknik", "We had a picnic in the park.", "Parkta piknik yaptık.", "have a picnic"),
    ("concert", "konser", "The concert was amazing.", "Konser muhteşemdi.", None),
    ("tired", "yorgun", "I was very tired on Sunday evening.", "Pazar akşamı çok yorgundum.", None),
    ("first / then / after that", "önce / sonra / ondan sonra", "First we had lunch, then we walked by the sea.", "Önce öğle yemeği yedik, sonra deniz kenarında yürüdük.", "Olay sıralamak için."),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Neredeydin?", "was / were ile geçmişte nerede olduğumu ve nasıl olduğunu söyleyebilirim.",
    {"kind": "dialogue", "title": "Pazartesi sabahı", "lines": [
        {"speaker": "Nil", "text": "Good morning, Barış! How was your weekend?"},
        {"speaker": "Barış", "text": "It was great, thanks. I was in Eskişehir."},
        {"speaker": "Nil", "text": "Lovely! Who were you with?"},
        {"speaker": "Barış", "text": "I was with my brother. The weather was perfect."},
        {"speaker": "Nil", "text": "My weekend was terrible. I was ill and my kids were at home all weekend!"},
        {"speaker": "Barış", "text": "Oh no! I'm sorry."}],
     "questions": [
        mc("Where was Barış at the weekend?", ["In Ankara", "In Eskişehir", "At home"], 1, "\"I was in Eskişehir.\""),
        mc("How was Nil's weekend?", ["Great", "Terrible", "OK"], 1, "\"My weekend was terrible.\""),
     ]},
    {"explanation": "**was / were**, am / is / are'nin geçmiş halidir.\n\n| Şimdi | Geçmiş |\n|---|---|\n| I **am** | I **was** |\n| He / She / It **is** | He / She / It **was** |\n| You / We / They **are** | You / We / They **were** |\n\n- I **was** at home yesterday.\n- The film **was** boring.\n- We **were** in Bodrum last summer.\n\n**Soru:** **How was** your weekend? / **Where were** you?",
     "examples": [{"en": "It was cold yesterday.", "tr": "Dün hava soğuktu."},
                  {"en": "My parents were in Izmir last week.", "tr": "Annemlerle babam geçen hafta İzmir'deydi."},
                  {"en": "How was the concert? – It was amazing!", "tr": "Konser nasıldı? – Muhteşemdi!"}],
     "turkishNote": "Türkçedeki \"-di\" eki (evdeydim, yorgundum) çoğu zaman was/were'e denk gelir. \"Dün\" = yesterday; \"dün gece\" = last night (yesterday night değil)."},
    [
        mc("I ___ at the gym yesterday.", ["was", "were"], 0, "I → was."),
        mc("They ___ very tired.", ["was", "were"], 1, "they → were."),
        mc("The weather ___ beautiful last weekend.", ["was", "were"], 0, "weather (it) → was."),
        gap("We ___ in Antalya last summer.", ["were"], "we → were."),
        gap("How ___ your holiday? – Great, thanks!", ["was"], "holiday tekil → was."),
        mc("\"Dün gece\"", ["yesterday night", "last night"], 1, "last night"),
        order(["were", "Where", "you", "on", "Saturday", "?"], "Where were you on Saturday?", "Where + were + you + zaman?", "Cumartesi neredeydin?"),
        listen("Last Sunday I was at my aunt's house. My cousins were there too. It was fun.", "Konuşan pazar günü neredeydi?", ["Evde", "Teyzesinin/halasının evinde", "Sinemada"], 1, "\"I was at my aunt's house\""),
        typ("İngilizce yazın: \"Dün hava soğuktu.\"", variants("It was cold yesterday.", "Yesterday it was cold.", "Yesterday, it was cold.", "The weather was cold yesterday."), "It was cold + yesterday."),
        match([("I am", "I was"), ("she is", "she was"), ("we are", "we were"), ("they are", "they were")], "Geçmiş hallerini eşleştirin."),
    ],
    {"kind": "speaking", "task": speak("Geçen hafta sonu neredeydiniz, kiminle birlikteydiniz ve hafta sonunuz nasıldı? Hava nasıldı?",
                                       "Last weekend I was in Bursa. I was with my friends. The weather was sunny but cold. It was a great weekend.",
                                       ["was / were doğru", "Zaman ifadesi", "Hava ve değerlendirme"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "Değildi, mıydı?", "was / were ile olumsuz cümle kurabilir ve soru sorabilirim.",
    {"kind": "dialogue", "title": "Kayıp telefon", "lines": [
        {"speaker": "Police officer", "text": "Where were you at nine o'clock last night?"},
        {"speaker": "Kaya", "text": "I was at a restaurant with my friends."},
        {"speaker": "Police officer", "text": "Was your phone with you?"},
        {"speaker": "Kaya", "text": "Yes, it was. It was in my bag."},
        {"speaker": "Police officer", "text": "Were your friends with you all evening?"},
        {"speaker": "Kaya", "text": "No, they weren't. They weren't there after ten. And my phone wasn't in my bag at eleven!"}],
     "questions": [
        mc("Where was Kaya last night?", ["At home", "At a restaurant", "At the police station"], 1, "\"I was at a restaurant\""),
        mc("When wasn't the phone in the bag?", ["At nine", "At ten", "At eleven"], 2, "\"my phone wasn't in my bag at eleven\""),
     ]},
    {"explanation": "**Olumsuz:** was not = **wasn't**, were not = **weren't**\n\n- I **wasn't** at work yesterday.\n- They **weren't** happy.\n\n**Soru:** Was / Were + özne + ...?\n\n- **Was** it expensive? – Yes, it **was**. / No, it **wasn't**.\n- **Were** you at home? – Yes, I **was**. / No, I **wasn't**.\n\n**Bilgi sorusu:** Where **were** you? / Who **was** with you? / Why **were** you late?",
     "examples": [{"en": "The shop wasn't open on Sunday.", "tr": "Dükkan pazar günü açık değildi."},
                  {"en": "Were you at the party? – No, I wasn't.", "tr": "Partide miydin? – Hayır."},
                  {"en": "Why were you late?", "tr": "Neden geç kaldın?"}],
     "turkishNote": "\"Geç kaldım\" İngilizcede bir be yapısıdır: I was late. \"Partide miydin?\" = Were you at the party? Soru için cümle başına Was/Were gelir, did kullanılmaz: ~~Did you be~~ yanlıştır."},
    [
        mc("Hangisi doğru?", ["I wasn't at school.", "I weren't at school.", "I didn't at school."], 0, "I → wasn't."),
        mc("\"Were you tired?\" (Evet.)", ["Yes, I was.", "Yes, I were.", "Yes, I did."], 0, "Yes, I was."),
        mc("\"Was the film good?\" (Hayır.)", ["No, it wasn't.", "No, it weren't.", "No, it didn't."], 0, "No, it wasn't."),
        gap("The museum ___ open yesterday. It was Monday. (değildi)", ["wasn't", "was not"], "Tekil olumsuz → wasn't."),
        gap("My friends ___ at the party. (değildi)", ["weren't", "were not"], "Çoğul olumsuz → weren't."),
        gap("___ you at home last night? – Yes, I was.", ["Were"], "you → Were."),
        order(["were", "Why", "you", "late", "?"], "Why were you late?", "Why + were + you + sıfat?", "Neden geç kaldın?"),
        listen("Was the hotel nice? – Well, the room was big, but it wasn't clean.", "Odanın sorunu neydi?", ["Küçüktü", "Temiz değildi", "Pahalıydı"], 1, "\"it wasn't clean\""),
        typ("Soru yapın: \"The tickets were cheap.\"", variants("Were the tickets cheap?"), "Were + the tickets + cheap?"),
        mc("\"Dükkan dün kapalıydı.\"", ["The shop was closed yesterday.", "The shop closed is yesterday.", "The shop were closed yesterday."], 0, "shop tekil → was closed."),
    ],
    {"kind": "speaking", "task": speak("JAI dedektif. Dün akşam saat 8'de neredeydiniz? JAI'nin sorularına was/were ile cevap verin; en az bir olumsuz cevap verin, sonra siz de JAI'ye 2 soru sorun.",
                                       "I was at home. No, I wasn't alone. My sister was with me. ... Where were you yesterday? Were you at work?",
                                       ["was/were doğru", "wasn't/weren't doğru", "Was/Were ile soru kurdu"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "Düzenli fiiller", "Düzenli fiillerle geçmişte yaptıklarımı anlatabilirim.",
    {"kind": "text", "title": "Selin'in günlüğü", "body": "Saturday\n\nI stayed in bed until ten. Then I cleaned my room and I cooked pasta for lunch. In the afternoon I visited my grandma. We talked for hours and we watched an old film together.\n\nIn the evening I listened to music and I studied a little for my English exam. I was very happy. It was a perfect, quiet day.",
     "questions": [
        mc("What did Selin cook?", ["Soup", "Pasta", "Pizza"], 1, "\"I cooked pasta for lunch\""),
        mc("Who did she visit?", ["Her friend", "Her grandma", "Her teacher"], 1, "\"I visited my grandma\""),
     ]},
    {"explanation": "**Past simple**, geçmişte olup bitmiş eylemleri anlatır. Düzenli fiiller **-ed** alır ve **her özne için aynıdır**.\n\n- I / You / He / She / We / They **watched** TV.\n\n**Yazım kuralları:**\n\n| Kural | Örnek |\n|---|---|\n| Çoğu fiil: + -ed | walk → walk**ed**, clean → clean**ed** |\n| -e ile bitiyorsa: + -d | live → live**d**, arrive → arrive**d** |\n| ünsüz + y: y → -ied | study → stud**ied**, try → tr**ied** |\n| ünlü + y: + -ed | play → play**ed**, stay → stay**ed** |\n| kısa fiil, ünlü + ünsüz: ikile | stop → sto**pped**, plan → pla**nned** |\n\n**Telaffuz:** -ed üç şekilde okunur:\n\n- /t/: walked, watched, cooked\n- /d/: played, cleaned, stayed\n- /ɪd/ (ekstra hece): **t** veya **d** ile biten fiillerde: visit**ed**, start**ed**, need**ed**",
     "examples": [{"en": "We walked by the sea.", "tr": "Deniz kenarında yürüdük."},
                  {"en": "She studied all weekend.", "tr": "Bütün hafta sonu ders çalıştı."},
                  {"en": "The film started at nine.", "tr": "Film dokuzda başladı."}],
     "turkishNote": "Türkçede geçmiş zaman kişiye göre değişir (yaptım, yaptı, yaptık); İngilizcede değişmez: I cooked, she cooked, we cooked. Sık yapılan bir hata \"walked\" kelimesini iki heceli (walk-ed) okumaktır; doğrusu tek hecedir: /wɔːkt/."},
    [
        gap("Yesterday I ___ my room. (clean)", ["cleaned"], "clean + -ed."),
        gap("She ___ for her exam. (study)", ["studied"], "ünsüz + y → -ied."),
        gap("We ___ football in the park. (play)", ["played"], "ünlü + y → + -ed."),
        gap("They ___ in Izmir for ten years. (live)", ["lived"], "-e → + -d."),
        gap("The bus ___ at the station. (stop)", ["stopped"], "stop → stopped."),
        mc("Hangisi doğru?", ["He watchs a film yesterday.", "He watched a film yesterday.", "He watched a film tomorrow."], 1, "Geçmiş → watched."),
        mc("Hangi fiilin -ed'i ekstra hece (/ɪd/) olarak okunur?", ["walked", "played", "visited"], 2, "t ile biten fiil → /ɪd/."),
        listen("On Sunday I cooked breakfast for my family. Then we walked to the park and played with the dog.", "Konuşan kahvaltıdan sonra ne yaptı?", ["Evi temizledi", "Parka yürüdü", "Film izledi"], 1, "\"Then we walked to the park\""),
        typ("İngilizce yazın: \"Dün gece bir podcast dinledim.\"", variants("I listened to a podcast last night.", "Last night I listened to a podcast.", "Last night, I listened to a podcast."), "listened to + a podcast + last night."),
        order(["visited", "We", "our", "grandparents", "last", "weekend"], "We visited our grandparents last weekend.", "Özne + fiil-ed + nesne + zaman.", "Geçen hafta sonu büyükanne ve büyükbabamızı ziyaret ettik."),
    ],
    {"kind": "writing", "task": write("Selin gibi geçen cumartesi için kısa bir günlük yazın. En az 5 düzenli fiil kullanın.",
                                      "Saturday\nI stayed at home in the morning and I cleaned the kitchen. In the afternoon I walked to the market. In the evening my friends visited me. We cooked dinner together and we watched a comedy.",
                                      ["-ed yazımı doğru", "En az 5 düzenli fiil", "Zaman ifadeleri (in the morning, then...)"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Yaptın mı?", "Geçmişle ilgili Did ...? soruları sorup didn't ile olumsuz cümle kurabilirim.",
    {"kind": "dialogue", "title": "Ev arkadaşları", "lines": [
        {"speaker": "Emre", "text": "Did you clean the kitchen?"},
        {"speaker": "Tolga", "text": "Yes, I did. I cleaned it this morning."},
        {"speaker": "Emre", "text": "Thanks! Did you call the landlord?"},
        {"speaker": "Tolga", "text": "No, I didn't. I didn't have time. Sorry!"},
        {"speaker": "Emre", "text": "No problem. What did you do yesterday evening?"},
        {"speaker": "Tolga", "text": "I worked late. I arrived home at eleven."}],
     "questions": [
        mc("Did Tolga clean the kitchen?", ["Yes, he did.", "No, he didn't."], 0, "\"Yes, I did.\""),
        mc("Why didn't Tolga call the landlord?", ["He didn't have time.", "He forgot the number.", "The landlord was busy."], 0, "\"I didn't have time.\""),
     ]},
    {"explanation": "Present simple'daki do / does, geçmişte **did** olur. did'den sonra fiil **yalın** haline döner.\n\n**Olumsuz:** didn't + yalın fiil\n\n- I **didn't watch** TV. (~~didn't watched~~)\n- She **didn't call** me.\n\n**Soru:** Did + özne + yalın fiil?\n\n- **Did** you **enjoy** the film? – Yes, I **did**. / No, I **didn't**.\n\n**Bilgi sorusu:** Soru kelimesi + did + özne + yalın fiil?\n\n- **What did** you **do** at the weekend?\n- **Where did** they **stay**?\n\n**Dikkat:** be fiilinde did kullanılmaz: Were you tired? (~~Did you be tired?~~)",
     "examples": [{"en": "Did you watch the match? – No, I didn't.", "tr": "Maçı izledin mi? – Hayır."},
                  {"en": "We didn't stay long.", "tr": "Uzun kalmadık."},
                  {"en": "What did you cook?", "tr": "Ne pişirdin?"}],
     "turkishNote": "En sık hata, did'den sonra fiile yine -ed eklemektir: \"Did you watched?\" ya da \"I didn't watched.\" Geçmiş bilgisini did taşıdığı için fiil yalın kalır: Did you watch? / I didn't watch."},
    [
        mc("Hangisi doğru?", ["Did you watched the film?", "Did you watch the film?", "Do you watched the film?"], 1, "Did + yalın fiil.", {0: "did'den sonra -ed olmaz."}),
        mc("Hangisi doğru?", ["I didn't cooked.", "I didn't cook.", "I not cooked."], 1, "didn't + yalın fiil."),
        mc("\"Did she call you?\" (Evet.)", ["Yes, she called.", "Yes, she did.", "Yes, she was."], 1, "Yes, she did."),
        gap("We ___ visit the museum. It was closed. (yapmadık)", ["didn't", "did not"], "Olumsuz: didn't."),
        gap("Did you ___ the party? (enjoy)", ["enjoy"], "Did + yalın fiil."),
        gap("What ___ you do last weekend?", ["did"], "Geçmiş bilgi sorusu → did."),
        order(["did", "Where", "you", "stay", "in", "Rome", "?"], "Where did you stay in Rome?", "Soru kelimesi + did + özne + yalın fiil?", "Roma'da nerede kaldın?"),
        listen("Did you walk to work today? – No, I didn't. It rained all morning, so I travelled by bus.", "Konuşan bugün işe yürüdü mü?", ["Evet", "Hayır, otobüsle gitti", "Hayır, evde kaldı"], 1, "\"No, I didn't ... I travelled by bus.\""),
        typ("Olumsuz yapın: \"I finished my homework.\"", variants("I didn't finish my homework.", "I did not finish my homework."), "didn't + finish."),
        mc("Hangisi doğru?", ["Did you be at home?", "Were you at home?"], 1, "be ile did kullanılmaz."),
    ],
    {"kind": "speaking", "task": speak("JAI'ye dünkü günü hakkında 4 soru sorun (3 tane Did you...?, 1 tane What/Where did...?). Sonra JAI size soracak; kısa cevap verin.",
                                       "Did you work yesterday? Did you cook dinner? Did you watch TV? What did you do in the evening? ... Yes, I did. / No, I didn't.",
                                       ["Did + yalın fiil düzeni", "Kısa cevaplar doğru", "Bilgi sorusu kurdu"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Hafta sonumu anlatıyorum", "Geçen hafta sonumu sıralı olarak ve zaman ifadeleriyle anlatabilirim.",
    {"kind": "dialogue", "title": "Kahve molası", "lines": [
        {"speaker": "Gizem", "text": "What did you do last weekend?"},
        {"speaker": "Ozan", "text": "On Saturday I went to Şile with some friends. First we had breakfast in a village café."},
        {"speaker": "Gizem", "text": "Nice! And then?"},
        {"speaker": "Ozan", "text": "Then we walked on the beach. After that we had a picnic. We arrived home at nine."},
        {"speaker": "Gizem", "text": "And on Sunday?"},
        {"speaker": "Ozan", "text": "I was very tired, so I stayed at home and relaxed. What about you?"}],
     "questions": [
        mc("What did Ozan do first on Saturday?", ["He walked on the beach.", "He had breakfast.", "He had a picnic."], 1, "\"First we had breakfast in a village café.\""),
        mc("Why did Ozan stay at home on Sunday?", ["It rained.", "He was tired.", "He worked."], 1, "\"I was very tired, so I stayed at home\""),
     ]},
    {"explanation": "**Zaman ifadeleri:**\n\n| | |\n|---|---|\n| yesterday | yesterday morning / afternoon / evening |\n| last | last night, last weekend, last week, last year |\n| ago | two days ago, a week ago, ten years ago |\n| on / in / at | on Saturday, in July, at seven o'clock |\n\n**last** ve **ago** ile **on/in/at kullanılmaz**: ~~on last Saturday~~, ~~in two years ago~~.\n\n**Sıralama:** **First**, ... **Then** ... **After that**, ... \n\n**İlk iki düzensiz fiil:** Bazı fiiller -ed almaz. A2'de bunları ayrıntılı göreceğiz; şimdilik en sık kullanılan ikisi:\n\n- go → **went**: I **went** to the cinema.\n- have → **had**: We **had** lunch. / I **had** a great time.\n\nSoru ve olumsuzda yine yalın hal: **Did** you **go**? / I **didn't have** time.",
     "examples": [{"en": "I went to Ankara three days ago.", "tr": "Üç gün önce Ankara'ya gittim."},
                  {"en": "First we had lunch, then we visited the museum.", "tr": "Önce öğle yemeği yedik, sonra müzeyi gezdik."},
                  {"en": "Did you have a good weekend?", "tr": "Hafta sonun iyi geçti mi?"}],
     "turkishNote": "Türkçede \"iki gün önce\" deriz; İngilizcede ago süreden sonra gelir: two days ago (ago two days değil). \"Geçen cumartesi\" = last Saturday (on last Saturday değil)."},
    [
        mc("Hangisi doğru?", ["on last Saturday", "last Saturday"], 1, "last ile on kullanılmaz."),
        mc("\"Üç yıl önce\"", ["ago three years", "three years ago", "before three years"], 1, "süre + ago."),
        gap("I ___ to the cinema last night. (go)", ["went"], "go → went."),
        gap("We ___ a picnic in the park. (have)", ["had"], "have → had."),
        gap("Did you ___ to the concert? (go)", ["go"], "did + yalın fiil: go."),
        mc("Hangisi doğru?", ["I didn't went.", "I didn't go."], 1, "didn't + yalın fiil."),
        order(["First", "we", "had", "breakfast", "then", "we", "walked", "by", "the", "sea"], "First we had breakfast, then we walked by the sea.", "First ..., then ...", "Önce kahvaltı yaptık, sonra deniz kenarında yürüdük."),
        listen("Last Friday I went to a concert with my sister. After that we had dinner in Kadıköy. We arrived home very late.", "Konserden sonra ne yaptılar?", ["Eve gittiler", "Akşam yemeği yediler", "Yürüdüler"], 1, "\"After that we had dinner\""),
        typ("İngilizce yazın: \"Hafta sonun iyi geçti mi?\"", variants("Did you have a good weekend?", "Did you have a nice weekend?", "How was your weekend?"), "Did you have a good weekend?"),
        match([("two days", "ago"), ("last", "night"), ("on", "Saturday"), ("yesterday", "morning")], "Zaman ifadelerini tamamlayın."),
    ],
    {"kind": "speaking", "task": speak("Geçen hafta sonunuzu JAI'ye anlatın: cumartesi ve pazar ne yaptınız? First / then / after that kullanın, en az bir yerde was/were ve went/had kullanın.",
                                       "On Saturday I went to the market with my mum. First we walked around, then we had tea in a café. After that we cooked together. On Sunday I was tired, so I stayed at home and watched a film.",
                                       ["Past simple doğru (-ed, went, had)", "Sıralama ifadeleri", "Zaman ifadeleri doğru"])},
)

u.test([
    mc("We ___ in Bodrum last summer.", ["was", "were"], 1, "we → were."),
    gap("How ___ the film? – It was boring.", ["was"], "film → was."),
    mc("\"Were you at work yesterday?\" (Hayır.)", ["No, I wasn't.", "No, I weren't.", "No, I didn't."], 0, "No, I wasn't."),
    gap("The shops ___ open on Sunday. (değildi)", ["weren't", "were not"], "Çoğul olumsuz."),
    gap("She ___ for three hours. (study)", ["studied"], "study → studied"),
    gap("We ___ in a nice hotel. (stay)", ["stayed"], "stay → stayed"),
    mc("Hangi fiil /ɪd/ ile biter?", ["cleaned", "started", "cooked"], 1, "t ile biten → /ɪd/."),
    mc("Hangisi doğru?", ["Did you enjoyed it?", "Did you enjoy it?"], 1, "Did + yalın fiil."),
    gap("I ___ watch the match. I was busy. (izlemedim)", ["didn't", "did not"], "didn't + yalın fiil."),
    mc("Hangisi doğru?", ["I went to Izmir two weeks ago.", "I went to Izmir ago two weeks.", "I go to Izmir two weeks ago."], 0, "went + süre + ago."),
    mc("Hangisi doğru?", ["on last weekend", "last weekend"], 1, "last ile on yok."),
    order(["did", "What", "you", "do", "yesterday", "?"], "What did you do yesterday?", "What + did + you + do + zaman?", "Dün ne yaptın?"),
    listen("I didn't go out on Saturday. I cleaned the house and cooked for my family. But on Sunday I went to the cinema.", "Konuşan ne zaman sinemaya gitti?", ["Cumartesi", "Pazar", "Hiç gitmedi"], 1, "\"on Sunday I went to the cinema\""),
    typ("İngilizce yazın: \"Dün evdeydim.\"", variants("I was at home yesterday.", "Yesterday I was at home.", "Yesterday, I was at home."), "I was at home + yesterday."),
    write("Bir arkadaşınıza e-posta yazın: geçen hafta sonu neredeydiniz, neler yaptınız (sıralı), nasıldı? Sonunda ona da hafta sonunu sorun (6–8 cümle).",
          "Hi Ayşe,\nHow are you? Last weekend I was in Eskişehir with my cousin. On Saturday morning we visited the Odunpazarı houses. Then we had lunch by the river. After that we walked in the park. On Sunday it rained, so we stayed at the hotel and watched films. It was a lovely weekend! What did you do?",
          ["was/were doğru", "Düzenli fiiller ve went/had doğru", "Zaman ve sıralama ifadeleri", "Did ile soru"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

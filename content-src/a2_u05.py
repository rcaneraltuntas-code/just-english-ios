"""A2 Ünite 5: Sağlık."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("A2", 5, "Sağlık", "Health",
         "Doktora ya da eczacıya şikayetlerimi anlatabilir, verilen talimatları anlayabilir ve başkalarına sağlıkla ilgili tavsiye verebilirim.",
         ["What's the matter? / I have a ... / My ... hurts", "should / shouldn't (tavsiye)", "Should I ...? / Why don't you ...?", "talimatlar: Take ... twice a day"],
         ["vücut bölümleri", "hastalıklar ve belirtiler", "ilaç ve sağlıklı yaşam"],
         {"title": "Sağlık köşesi", "durationMinutes": 45,
          "goal": "Öğrenciler sırayla 'hasta' ve 'doktor' olur. Hasta bir şikayet kartı çeker ve belirtilerini anlatır; doktor sorular sorup should/shouldn't ile tavsiye verir. Sonunda sınıf, bir dergi için 'Sağlıklı yaşam için 10 tavsiye' listesi hazırlar."})

u.vocab([
    ("head", "baş", "My head hurts.", "Başım ağrıyor.", None),
    ("throat", "boğaz", "I have a sore throat.", "Boğazım ağrıyor.", "sore throat = boğaz ağrısı"),
    ("stomach", "mide, karın", "I have a stomach ache.", "Midem ağrıyor.", "Okunuşu: /ˈstʌmək/"),
    ("back", "sırt, bel", "My back hurts after work.", "İşten sonra belim ağrıyor.", None),
    ("tooth (teeth)", "diş (dişler)", "I have a terrible toothache.", "Korkunç bir diş ağrım var.", "Düzensiz çoğul."),
    ("ear", "kulak", "The baby has an ear infection.", "Bebeğin kulak enfeksiyonu var.", None),
    ("knee", "diz", "I hurt my knee playing football.", "Futbol oynarken dizimi incittim.", "k okunmaz: /niː/"),
    ("ache", "ağrı", "I have a headache.", "Başım ağrıyor.", "headache, stomach ache, toothache, backache, earache"),
    ("hurt", "ağrımak; incitmek", "My leg hurts.", "Bacağım ağrıyor.", "hurt → hurt → hurt"),
    ("cold", "soğuk algınlığı", "I think I'm getting a cold.", "Sanırım soğuk alıyorum.", "have a cold"),
    ("flu", "grip", "She's in bed with flu.", "Gripten yatıyor.", "the flu da denir."),
    ("temperature", "ateş; sıcaklık", "He has a high temperature.", "Ateşi yüksek.", "fever da kullanılır."),
    ("cough", "öksürük; öksürmek", "I have a bad cough.", "Kötü bir öksürüğüm var.", "Okunuşu: /kɒf/"),
    ("sneeze", "hapşırmak", "I can't stop sneezing.", "Hapşırmayı durduramıyorum.", None),
    ("feel sick", "midesi bulanmak", "I feel sick. I don't want to eat.", "Midem bulanıyor. Yemek istemiyorum.", "Amerikan: feel nauseous."),
    ("dizzy", "başı dönen", "I feel dizzy when I stand up.", "Ayağa kalkınca başım dönüyor.", None),
    ("medicine", "ilaç", "Take this medicine after meals.", "Bu ilacı yemeklerden sonra al.", None),
    ("tablet / pill", "tablet, hap", "Take two tablets twice a day.", "Günde iki kez iki tablet al.", None),
    ("prescription", "reçete", "You need a prescription for these.", "Bunlar için reçete gerekiyor.", None),
    ("rest", "dinlenmek; dinlenme", "You should rest for a few days.", "Birkaç gün dinlenmelisin.", None),
    ("should", "-meli / -malı", "You should drink more water.", "Daha çok su içmelisin.", "should + yalın fiil"),
    ("healthy", "sağlıklı", "Fruit and vegetables are healthy.", "Meyve ve sebze sağlıklıdır.", "unhealthy (sağlıksız)"),
    ("Get well soon!", "Geçmiş olsun!", "I heard you're ill. Get well soon!", "Hasta olduğunu duydum. Geçmiş olsun!", None),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Neren ağrıyor?", "Vücudumun ağrıyan yerini ve nasıl hissettiğimi anlatabilirim.",
    {"kind": "dialogue", "title": "İş yerinde", "lines": [
        {"speaker": "Selin", "text": "You don't look well, Arda. What's the matter?"},
        {"speaker": "Arda", "text": "I have a terrible headache, and my back hurts too."},
        {"speaker": "Selin", "text": "Oh no. Is it because of the new chair?"},
        {"speaker": "Arda", "text": "Maybe. I sit at this desk for ten hours every day."},
        {"speaker": "Selin", "text": "Do you feel dizzy?"},
        {"speaker": "Arda", "text": "A little. I think I need some fresh air."}],
     "questions": [
        mc("What's wrong with Arda?", ["Headache and backache", "Stomach ache", "A cold"], 0, "\"I have a terrible headache, and my back hurts too.\""),
        mc("What does Arda need?", ["Medicine", "Fresh air", "A new desk"], 1, "\"I think I need some fresh air.\""),
     ]},
    {"explanation": "**Sormak:**\n\n- **What's the matter?** / **What's wrong?** (Neyin var?)\n- **How do you feel?** / **Are you OK?**\n\n**Ağrıları anlatmak — üç yol:**\n\n| Yapı | Örnek |\n|---|---|\n| I have a + ...ache | I have a **headache** / **stomach ache** / **toothache** / **backache** / **earache** |\n| My + vücut bölümü + **hurts** | My **knee hurts**. / My **eyes hurt**. |\n| I have a sore + ... | I have a **sore throat**. |\n\n**Nasıl hissettiğini söylemek:** I feel **sick** / **dizzy** / **tired** / **terrible** / **better**.\n\nİngiliz İngilizcesinde **I've got a headache** de çok yaygındır; anlamı aynıdır.",
     "examples": [{"en": "My eyes hurt after a long day at the computer.", "tr": "Uzun bir bilgisayar gününden sonra gözlerim ağrıyor."},
                  {"en": "I have a sore throat and I feel tired.", "tr": "Boğazım ağrıyor ve yorgun hissediyorum."},
                  {"en": "What's the matter? – I feel sick.", "tr": "Neyin var? – Midem bulanıyor."}],
     "turkishNote": "Türkçede \"başım ağrıyor\" deriz; İngilizcede \"my head aches\" çok az kullanılır, doğal olan \"I have a headache\" demektir. \"I feel sick\" Türkçedeki \"hasta hissediyorum\" değil, \"midem bulanıyor\" anlamındadır. Hasta olduğunuzu söylemek için \"I'm ill\" ya da \"I'm not well\" deyin."},
    [
        match([("head", "baş"), ("throat", "boğaz"), ("stomach", "mide"), ("knee", "diz"), ("back", "sırt, bel")], "Vücut bölümlerini eşleştirin."),
        mc("\"Başım ağrıyor.\" En doğal söyleyiş:", ["I have a headache.", "My head is aching me.", "I have head pain."], 0, "I have a headache."),
        mc("Hangisi doğru?", ["My knee hurt.", "My knee hurts.", "My knee is hurt me."], 1, "Tekil özne → hurts."),
        mc("Hangisi doğru?", ["My eyes hurts.", "My eyes hurt."], 1, "Çoğul → hurt."),
        gap("I have a sore ___. I can't speak. (boğaz)", ["throat"], "sore throat."),
        gap("What's the ___? – I feel dizzy.", ["matter"], "What's the matter?"),
        mc("\"I feel sick\" ne demek?", ["Midem bulanıyor.", "Çok hastayım.", "Ateşim var."], 0, "feel sick = midesi bulanmak."),
        listen("I can't eat anything. I have a stomach ache and I feel sick.", "Konuşanın sorunu ne?", ["Diş ağrısı", "Mide ağrısı ve bulantı", "Baş dönmesi"], 1, "\"stomach ache ... feel sick\""),
        typ("İngilizce yazın: \"Dişim ağrıyor.\"", variants("I have a toothache.", "I've got a toothache.", "I have toothache.", "I've got toothache.", "My tooth hurts."), "I have a toothache. / My tooth hurts."),
        order(["you", "How", "do", "feel", "today", "?"], "How do you feel today?", "How do you feel + zaman?", "Bugün nasıl hissediyorsun?"),
    ],
    {"kind": "speaking", "task": speak("JAI size \"What's the matter?\" diye soracak. Üç farklı şikayeti (biri hurts, biri ...ache, biri feel ile) anlatın.",
                                       "I have a headache and my neck hurts. I also feel very tired. I think I work too much.",
                                       ["I have a ...ache doğru", "My ... hurts doğru", "I feel + sıfat"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "Doktorda", "Doktora belirtilerimi anlatabilir ve sorularına cevap verebilirim.",
    {"kind": "dialogue", "title": "Muayenehanede", "lines": [
        {"speaker": "Doctor", "text": "Good morning. How can I help you?"},
        {"speaker": "Leyla", "text": "I feel terrible. I have a bad cough and a sore throat."},
        {"speaker": "Doctor", "text": "When did it start?"},
        {"speaker": "Leyla", "text": "Three days ago. And last night I had a high temperature."},
        {"speaker": "Doctor", "text": "Let me check. ... Yes, it's flu. Are you allergic to anything?"},
        {"speaker": "Leyla", "text": "No, I'm not."},
        {"speaker": "Doctor", "text": "OK. Here's a prescription. You need to rest for a few days."}],
     "questions": [
        mc("When did Leyla's illness start?", ["Yesterday", "Three days ago", "Last week"], 1, "\"Three days ago.\""),
        mc("What does the doctor say it is?", ["A cold", "Flu", "An allergy"], 1, "\"Yes, it's flu.\""),
     ]},
    {"explanation": "**Hastalıklar:**\n\n| | |\n|---|---|\n| have **a cold** | soğuk algınlığı |\n| have **flu** / **the flu** | grip |\n| have **a temperature** / **a fever** | ateş |\n| have **a cough** | öksürük |\n| have **an allergy** / be **allergic to** ... | alerji |\n| have **an infection** | enfeksiyon |\n\n**Doktorun soruları:**\n\n- How can I help you? / What seems to be the problem?\n- **When did** it **start**? – Two days ago. / Yesterday.\n- Are you **allergic to** anything? – Yes, I'm allergic to penicillin.\n- Are you taking any medicine?\n\n**Doktorun cevapları:** Let me check. / It's nothing serious. / Here's a prescription.",
     "examples": [{"en": "I think I have a cold. I keep sneezing.", "tr": "Sanırım soğuk algınlığım var. Sürekli hapşırıyorum."},
                  {"en": "I'm allergic to cats.", "tr": "Kedilere alerjim var."},
                  {"en": "It's nothing serious. You'll be fine.", "tr": "Ciddi bir şey değil. İyileşeceksin."}],
     "turkishNote": "\"Ateşim var\" = I have a temperature (fever). \"Grip oldum\" = I have flu / I've got the flu. \"-e alerjim var\" İngilizcede \"allergic to\" ile söylenir: I'm allergic to nuts (fındık/fıstığa). \"keep + -ing\" = sürekli ... -mek: I keep sneezing."},
    [
        match([("cold", "soğuk algınlığı"), ("flu", "grip"), ("temperature", "ateş"), ("cough", "öksürük"), ("prescription", "reçete")], "Eşleştirin."),
        gap("I'm allergic ___ nuts.", ["to"], "allergic to."),
        gap("When did it ___? – Two days ago. (başlamak)", ["start", "begin"], "When did it start?"),
        mc("\"Ateşim var.\"", ["I have a temperature.", "I am fire.", "I have hot."], 0, "have a temperature."),
        mc("Hangisi doğru?", ["I have a flu.", "I have flu."], 1, "flu → a almaz (the flu olabilir)."),
        gap("I keep ___. Maybe it's an allergy. (sneeze)", ["sneezing"], "keep + -ing."),
        mc("Doktor muayene etmeden önce:", ["Let me check.", "Get well soon.", "Here's your bill."], 0, "Let me check = Bir bakayım."),
        listen("I have a cough and a runny nose, but no temperature. It started yesterday.", "Hangisi konuşanda YOK?", ["Öksürük", "Burun akıntısı", "Ateş"], 2, "\"but no temperature\""),
        typ("İngilizce yazın: \"Kedilere alerjim var.\"", variants("I'm allergic to cats.", "I am allergic to cats.", "I have an allergy to cats."), "I'm allergic to cats."),
        order(["you", "Are", "taking", "any", "medicine", "?"], "Are you taking any medicine?", "Are you taking + any + isim?", "Herhangi bir ilaç kullanıyor musun?"),
    ],
    {"kind": "speaking", "task": speak("JAI doktor. Muayeneye girin: belirtilerinizi anlatın, ne zaman başladığını söyleyin ve doktorun sorularına cevap verin (alerji, ilaç).",
                                       "Good morning. I have a sore throat and a bad cough. It started four days ago. Yesterday I had a temperature. No, I'm not allergic to anything. I'm not taking any medicine.",
                                       ["Belirtiler doğru ifade edildi", "When did it start? cevabı (ago)", "allergic to doğru"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "Tavsiye vermek", "should ve shouldn't ile birine tavsiye verebilirim.",
    {"kind": "text", "title": "Dergi köşesi: Dr. Yasemin cevaplıyor", "body": "Dear Dr Yasemin,\nI always feel tired, and I often have headaches. I work on a computer all day and I drink about six cups of coffee. What should I do?\n— Tired Tolga\n\nDear Tolga,\nYou should take a short break every hour and look away from the screen. You shouldn't drink so much coffee. Two cups a day is enough. You should drink more water and go for a walk at lunchtime. And you should go to bed before midnight! If the headaches don't stop, you should see a doctor.\n— Dr Yasemin",
     "questions": [
        mc("How much coffee does Tolga drink?", ["Two cups", "About six cups", "None"], 1, "\"about six cups of coffee\""),
        mc("What does Dr Yasemin say about coffee?", ["Drink more", "Two cups a day is enough", "Stop completely"], 1, "\"Two cups a day is enough.\""),
     ]},
    {"explanation": "**should** + yalın fiil → tavsiye (bence yapman iyi olur)\n\n**shouldn't** + yalın fiil → olumsuz tavsiye (bence yapmasan iyi olur)\n\n- You **should** drink more water.\n- You **shouldn't** eat so much sugar.\n- He **should** see a doctor.\n\n**can** gibi **should** de her özneyle aynıdır; -s, to veya do almaz:\n\n- ~~He shoulds~~ / ~~You should to rest~~ / ~~You don't should~~\n\n**Yumuşatmak:** I think you should... / I don't think you should... (I think you shouldn't yerine)",
     "examples": [{"en": "You should go to bed early tonight.", "tr": "Bu akşam erken yatmalısın."},
                  {"en": "You shouldn't lift heavy things with a bad back.", "tr": "Belin ağrıyorken ağır şeyler kaldırmamalısın."},
                  {"en": "I don't think you should go to work today.", "tr": "Bence bugün işe gitmemelisin."}],
     "turkishNote": "should, Türkçedeki \"-meli\" ekine denk gelir ama bir emir değil, tavsiyedir: \"You should rest\" = Dinlenmelisin (bence). Zorunluluk için have to / must kullanılır (8. ünite). İngilizcede \"I don't think you should\" yapısı \"I think you shouldn't\"tan daha doğaldır."},
    [
        mc("Hangisi doğru?", ["You should to rest.", "You should rest.", "You should resting."], 1, "should + yalın fiil."),
        mc("Hangisi doğru?", ["She shoulds see a doctor.", "She should see a doctor."], 1, "should her özneyle aynı."),
        gap("You ___ eat so much fast food. It's unhealthy. (shouldn't)", ["shouldn't", "should not"], "Olumsuz tavsiye."),
        gap("You have a temperature. You should ___ in bed. (stay)", ["stay"], "should + yalın fiil."),
        gap("I don't ___ you should go out in this cold.", ["think"], "I don't think you should..."),
        mc("Bir arkadaşınızın dişi ağrıyor:", ["You should see a dentist.", "You shouldn't see a dentist.", "You should eat sweets."], 0, "Mantıklı tavsiye."),
        order(["should", "You", "take", "a", "break", "every", "hour"], "You should take a break every hour.", "You should + fiil + nesne + zaman.", "Her saat ara vermelisin."),
        listen("You have a bad back, so you shouldn't carry heavy bags. And you should do some gentle exercise, like swimming.", "Hangi egzersiz öneriliyor?", ["Koşu", "Yüzme", "Ağırlık kaldırma"], 1, "\"gentle exercise, like swimming\""),
        typ("İngilizce yazın: \"Daha çok su içmelisin.\"", variants("You should drink more water."), "You should + drink more water."),
        match([("I have a cold.", "You should drink hot tea."), ("I'm always tired.", "You should sleep more."), ("My eyes hurt.", "You shouldn't look at your phone so much."), ("I have toothache.", "You should see a dentist.")], "Şikayetleri tavsiyelerle eşleştirin."),
    ],
    {"kind": "writing", "task": write("Dr. Yasemin'e bir okuyucu daha yazdı: \"Geceleri uyuyamıyorum, sabahları çok yorgunum.\" Ona 5 tavsiyeli bir cevap yazın (should / shouldn't / I don't think you should).",
                                      "Dear reader,\nYou shouldn't drink coffee or tea after 4 pm. You should turn off your phone an hour before bed. I don't think you should eat a big dinner late at night. You should go to bed at the same time every day. And you should try some light exercise in the morning.\n— Dr Yasemin",
                                      ["should / shouldn't + yalın fiil", "I don't think you should kullandı", "Tavsiyeler mantıklı"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Ne yapmalıyım?", "Tavsiye isteyebilir ve farklı yollarla öneride bulunabilirim.",
    {"kind": "dialogue", "title": "Spor yaralanması", "lines": [
        {"speaker": "Onur", "text": "I hurt my knee playing football yesterday. Should I go to the hospital?"},
        {"speaker": "Ayşe", "text": "Can you walk on it?"},
        {"speaker": "Onur", "text": "Yes, but it hurts a lot."},
        {"speaker": "Ayşe", "text": "Why don't you put some ice on it first? And you shouldn't play football this week."},
        {"speaker": "Onur", "text": "OK. Should I take a painkiller?"},
        {"speaker": "Ayşe", "text": "Yes, but if it doesn't get better in two days, you should definitely see a doctor."}],
     "questions": [
        mc("What did Onur hurt?", ["His back", "His knee", "His foot"], 1, "\"I hurt my knee playing football\""),
        mc("What does Ayşe suggest first?", ["Going to the hospital", "Putting ice on it", "Playing again"], 1, "\"Why don't you put some ice on it first?\""),
     ]},
    {"explanation": "**Tavsiye istemek:**\n\n- **Should I** + fiil? → Should I take a painkiller? – Yes, you **should**. / No, you **shouldn't**.\n- **What should I** do?\n- **Do you think I should** + fiil?\n\n**Öneri sunmanın diğer yolları:**\n\n| Kalıp | Örnek |\n|---|---|\n| Why don't you + fiil? | **Why don't you** put some ice on it? |\n| Try + -ing | **Try drinking** some ginger tea. |\n| If I were you, I'd + fiil | **If I were you, I'd** see a doctor. |\n\n**Tavsiyeye cevap:** That's a good idea. / Thanks, I'll try that. / I don't think that's a good idea.",
     "examples": [{"en": "Should I call the doctor? – Yes, I think you should.", "tr": "Doktoru aramalı mıyım? – Evet, bence aramalısın."},
                  {"en": "Why don't you take a day off?", "tr": "Neden bir gün izin almıyorsun?"},
                  {"en": "If I were you, I'd stay at home.", "tr": "Yerinde olsam evde kalırdım."}],
     "turkishNote": "\"Why don't you...?\" şikayet gibi duyulsa da aslında arkadaşça bir öneridir: \"Neden ... yapmıyorsun?\" değil, \"... yapsana\" anlamında. \"If I were you\" bir kalıptır; I was değil I were denir. Bu yapının dilbilgisini B1'de göreceğiz."},
    [
        mc("Hangisi doğru?", ["Do I should rest?", "Should I rest?", "Should I to rest?"], 1, "Should + I + yalın fiil?"),
        mc("\"Should I take a painkiller?\" (Evet.)", ["Yes, you should.", "Yes, you do.", "Yes, I should."], 0, "Yes, you should."),
        gap("Why don't you ___ some ice on it? (put)", ["put"], "Why don't you + yalın fiil?"),
        gap("Try ___ some ginger tea. (drink)", ["drinking"], "Try + -ing."),
        gap("If I ___ you, I'd see a doctor.", ["were"], "If I were you."),
        mc("Bir tavsiyeyi kabul etmek:", ["That's a good idea. Thanks!", "You shouldn't.", "Should I?"], 0, "That's a good idea."),
        order(["I", "What", "should", "do", "?"], "What should I do?", "What + should + I + do?", "Ne yapmalıyım?"),
        listen("I can't sleep at night. – Why don't you try reading a book instead of looking at your phone? – Good idea, I'll try that.", "Ne öneriliyor?", ["Telefona bakmak", "Telefon yerine kitap okumak", "İlaç almak"], 1, "\"try reading a book instead of looking at your phone\""),
        typ("İngilizce yazın: \"Yerinde olsam evde kalırdım.\"", variants("If I were you, I'd stay at home.", "If I were you, I would stay at home.", "If I were you I'd stay at home.", "If I were you, I'd stay home."), "If I were you, I'd + stay at home."),
        typ("İngilizce yazın: \"Neden bir gün izin almıyorsun?\"", variants("Why don't you take a day off?"), "Why don't you + take a day off?"),
    ],
    {"kind": "speaking", "task": speak("JAI'nin bir sağlık sorunu var ve sizden tavsiye istiyor. En az 4 farklı kalıpla tavsiye verin (should, shouldn't, Why don't you, If I were you).",
                                       "You should rest and drink a lot of water. You shouldn't go to the gym this week. Why don't you take a hot shower? If I were you, I'd see a doctor tomorrow.",
                                       ["Farklı tavsiye kalıpları", "Yalın fiil doğru", "Tavsiyeler duruma uygun"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Eczanede", "Eczacıdan ilaç isteyebilir ve kullanım talimatlarını anlayabilirim.",
    {"kind": "dialogue", "title": "Eczane", "lines": [
        {"speaker": "Pharmacist", "text": "Hello. Can I help you?"},
        {"speaker": "Tourist", "text": "Yes, please. I have a cold and a sore throat. Do you have anything for it?"},
        {"speaker": "Pharmacist", "text": "Try these tablets. Take two tablets three times a day, after meals."},
        {"speaker": "Tourist", "text": "Can I take them with coffee?"},
        {"speaker": "Pharmacist", "text": "It's better with water. And you shouldn't drive. They can make you sleepy."},
        {"speaker": "Tourist", "text": "OK, thank you. How much are they?"},
        {"speaker": "Pharmacist", "text": "Eighty-five lira. Get well soon!"}],
     "questions": [
        mc("How often should the tourist take the tablets?", ["Once a day", "Twice a day", "Three times a day"], 2, "\"three times a day, after meals\""),
        mc("Why shouldn't the tourist drive?", ["The tablets can make you sleepy.", "The roads are dangerous.", "There's no car."], 0, "\"They can make you sleepy.\""),
     ]},
    {"explanation": "**İlaç istemek:**\n\n- Do you have anything **for** a headache / a cough?\n- Can I have something **for** my stomach?\n- Do I need a prescription?\n\n**Talimatları anlamak:**\n\n| İfade | Anlam |\n|---|---|\n| once / twice / three times a day | günde bir / iki / üç kez |\n| before / after meals | yemeklerden önce / sonra |\n| with water | su ile |\n| on an empty stomach | aç karnına |\n| every four hours | dört saatte bir |\n| Don't take more than ... | ...'dan fazla almayın |\n\n**Sağlıklı yaşam için:** eat healthily, get enough sleep, do exercise, drink plenty of water, avoid stress",
     "examples": [{"en": "Do you have anything for a sore throat?", "tr": "Boğaz ağrısı için bir şeyiniz var mı?"},
                  {"en": "Take one tablet every six hours.", "tr": "Altı saatte bir bir tablet alın."},
                  {"en": "Don't take more than four tablets a day.", "tr": "Günde dört tabletten fazla almayın."}],
     "turkishNote": "\"Günde iki kez\" = twice a day (two times a day da anlaşılır ama twice daha doğaldır). \"Baş ağrısı için\" = for a headache (against değil). \"İlaç içmek\" İngilizcede take medicine'dir: drink medicine sadece şurup için kullanılabilir."},
    [
        mc("\"Günde iki kez\"", ["two a day", "twice a day", "double a day"], 1, "twice a day."),
        mc("Hangisi doğru?", ["Do you have anything against a headache?", "Do you have anything for a headache?"], 1, "something for + şikayet."),
        mc("\"İlacımı aldım.\"", ["I drank my medicine.", "I took my medicine."], 1, "take medicine."),
        gap("Take one tablet ___ meals. (yemeklerden sonra)", ["after"], "after meals."),
        gap("Take these tablets on an empty ___. (aç karnına)", ["stomach"], "on an empty stomach."),
        gap("Don't take ___ than six tablets a day. (fazla)", ["more"], "more than."),
        order(["Take", "two", "tablets", "three", "times", "a", "day"], "Take two tablets three times a day.", "Take + miktar + sıklık.", "Günde üç kez iki tablet alın."),
        listen("Take one spoonful of this syrup every four hours. Don't take it on an empty stomach.", "Şurup ne sıklıkla alınmalı?", ["Dört saatte bir", "Günde dört kez", "Aç karnına"], 0, "\"every four hours\""),
        typ("İngilizce yazın: \"Boğaz ağrısı için bir şeyiniz var mı?\"", variants("Do you have anything for a sore throat?", "Have you got anything for a sore throat?"), "Do you have anything for + a sore throat?"),
        match([("eat", "healthily"), ("get enough", "sleep"), ("drink plenty of", "water"), ("avoid", "stress")], "Sağlıklı yaşam kalıplarını eşleştirin."),
    ],
    {"kind": "speaking", "task": speak("JAI eczacı. Bir şikayetinizi anlatın ve ilaç isteyin; ilacı nasıl kullanacağınızı sorun, eczacının talimatlarını tekrar ederek kontrol edin ve fiyatını sorun.",
                                       "Hello. I have a headache and a temperature. Do you have anything for it? How often should I take them? So, one tablet every six hours, after meals. Can I drive? How much is it?",
                                       ["İlaç isteme kalıbı", "Talimatları anladı ve tekrar etti", "Should I...? soruları"])},
)

u.test([
    mc("\"Başım ağrıyor.\"", ["I have a headache.", "I have a head ache me."], 0, "I have a headache."),
    mc("Hangisi doğru?", ["My back hurt.", "My back hurts."], 1, "Tekil → hurts"),
    gap("I have a sore ___. I can't swallow. (boğaz)", ["throat"], "sore throat"),
    gap("I'm allergic ___ penicillin.", ["to"], "allergic to"),
    mc("Hangisi doğru?", ["I have a flu.", "I have flu."], 1, "flu"),
    mc("Hangisi doğru?", ["You should to see a doctor.", "You should see a doctor."], 1, "should + yalın fiil"),
    gap("You ___ smoke. It's bad for you. (shouldn't)", ["shouldn't", "should not"], "shouldn't"),
    mc("\"Should I call him?\" (Hayır.)", ["No, you shouldn't.", "No, you don't."], 0, "No, you shouldn't."),
    gap("Why don't you ___ a day off? (take)", ["take"], "Why don't you + yalın fiil"),
    gap("If I ___ you, I'd rest.", ["were"], "If I were you"),
    mc("\"Günde üç kez\"", ["three times a day", "three a day times"], 0, "three times a day"),
    mc("\"İlaç almak\"", ["drink medicine", "take medicine"], 1, "take medicine"),
    listen("You have a high temperature. You should stay in bed for two days and take these tablets twice a day.", "Kaç gün yatakta kalmalı?", ["Bir", "İki", "Üç"], 1, "\"stay in bed for two days\""),
    typ("İngilizce yazın: \"Ne yapmalıyım?\"", variants("What should I do?"), "What should I do?"),
    write("Hasta bir arkadaşınıza mesaj yazın: geçmiş olsun deyin, nasıl olduğunu sorun ve en az 4 tavsiye verin (farklı kalıplarla). 50–70 kelime.",
          "Hi Ece, I heard you have flu. Get well soon! How do you feel today? You should stay in bed and rest. You shouldn't go to work this week. Why don't you drink some hot soup? My mum makes great chicken soup. If I were you, I'd call the doctor if the temperature doesn't go down. Take care!",
          ["Geçmiş olsun ve soru", "should / shouldn't doğru", "Why don't you / If I were you", "Sağlık kelimeleri"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

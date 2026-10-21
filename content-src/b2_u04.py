"""B2 Ünite 4: Hizmetler."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("B2", 4, "Hizmetler", "Services",
         "Edilgen yapıyı bütün zamanlarda ve modallarla kullanabilir, başkasına yaptırdığım işleri have / get something done ile anlatabilir ve kötü bir hizmet hakkında resmî ve etkili bir şikâyet yazabilirim.",
         ["passive: continuous ve perfect zamanlar", "passive: modallar ve gelecek (will be done, must be done)", "have something done", "get something done, get / have someone do", "şikâyet ve talep dilinde passive"],
         ["hizmetler", "ev işleri ve tamirat", "müşteri hizmetleri ve şikâyetler"],
         {"title": "Müşteri hizmetleri", "durationMinutes": 45,
          "goal": "Öğrenciler ikili olarak müşteri ve müşteri temsilcisi rollerini oynar. Müşteri bir sorun bildirir (siparişi gelmemiş, tamir edilen telefonu hâlâ bozuk); temsilci passive ile açıklama yapar (Your order has been dispatched... It's being repaired...). Ardından gruplar hafta içi hangi işleri kendilerinin yaptığını, hangilerini yaptırdığını (I have my hair cut... I get my car serviced...) karşılaştırır."})

u.vocab([
    ("repair", "tamir etmek; tamir", "My laptop is being repaired.", "Dizüstü bilgisayarım tamir ediliyor.", None),
    ("service (a car)", "bakımını yapmak", "I need to get my car serviced.", "Arabamın bakımını yaptırmam gerek.", None),
    ("deliver", "teslim etmek", "The parcel will be delivered tomorrow.", "Paket yarın teslim edilecek.", "delivery (teslimat)"),
    ("dispatch", "göndermek, kargoya vermek", "Your order has been dispatched.", "Siparişiniz kargoya verildi.", None),
    ("install", "kurmak", "The new boiler was installed last week.", "Yeni kombi geçen hafta kuruldu.", None),
    ("plumber", "tesisatçı", "We need a plumber. The pipe's leaking.", "Tesisatçı lazım. Boru sızdırıyor.", "b okunmaz: /ˈplʌmə/"),
    ("electrician", "elektrikçi", "The electrician fixed the lights.", "Elektrikçi ışıkları tamir etti.", None),
    ("decorate", "boyamak, dekore etmek", "We're having the living room decorated.", "Oturma odasını boyatıyoruz.", None),
    ("dry-clean", "kuru temizleme yapmak", "I had my suit dry-cleaned.", "Takımımı kuru temizlemeye verdim.", None),
    ("leak", "sızdırmak; sızıntı", "The roof is leaking.", "Çatı akıyor.", None),
    ("broken down", "bozulmuş (makine, araba)", "The lift has broken down again.", "Asansör yine bozuldu.", "break down"),
    ("out of order", "arızalı", "The machine is out of order.", "Makine arızalı.", None),
    ("refund", "para iadesi", "I'd like a full refund.", "Paramın tamamını geri istiyorum.", None),
    ("replacement", "yenisi, yedek", "They sent me a replacement.", "Bana yenisini gönderdiler.", None),
    ("compensation", "tazminat", "I expect some compensation.", "Bir tazminat bekliyorum.", None),
    ("complaint", "şikâyet", "I'd like to make a complaint.", "Bir şikâyette bulunmak istiyorum.", "complain (fiil)"),
    ("faulty", "kusurlu, arızalı", "The product was faulty.", "Ürün arızalıydı.", None),
    ("warranty", "garanti", "Is it still under warranty?", "Hâlâ garanti kapsamında mı?", None),
    ("appointment", "randevu", "I've made an appointment at the hairdresser's.", "Kuaförden randevu aldım.", None),
    ("chores", "ev işleri", "I hate doing household chores.", "Ev işlerinden nefret ediyorum.", None),
    ("ironing", "ütü", "I'll do the ironing later.", "Ütüyü sonra yaparım.", None),
    ("DIY", "kendin yap (ev tamiri vb.)", "He's very good at DIY.", "Ev tamiratında çok iyidir.", "do-it-yourself"),
    ("customer service", "müşteri hizmetleri", "I called customer service three times.", "Müşteri hizmetlerini üç kez aradım.", None),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Yapılıyor, yapıldı", "Passive'i present continuous, present perfect ve past perfect zamanlarında kullanabilirim.",
    {"kind": "dialogue", "title": "Otel resepsiyonunda", "lines": [
        {"speaker": "Guest", "text": "Excuse me, I booked a sea-view room, but my room faces the car park."},
        {"speaker": "Receptionist", "text": "I'm very sorry. The sea-view rooms on the third floor are being renovated this week."},
        {"speaker": "Guest", "text": "But nobody told me. And the lift has been out of order since this morning."},
        {"speaker": "Receptionist", "text": "Yes, I apologise. The technician has been called, and the lift is being checked right now."},
        {"speaker": "Guest", "text": "When I arrived, I was told that breakfast had already been served. It was only 9:30!"},
        {"speaker": "Receptionist", "text": "That's not right. Breakfast is served until 10:30. A complimentary breakfast will be brought to your room tomorrow."}],
     "questions": [
        mc("Why can't the guest have a sea-view room?", ["They are fully booked.", "They are being renovated.", "They are too expensive."], 1, "\"The sea-view rooms... are being renovated this week.\""),
        mc("What has happened about the lift?", ["It has been repaired.", "The technician has been called.", "It has been closed forever."], 1, "\"The technician has been called\""),
     ]},
    {"explanation": "B1'de present simple ve past simple passive'i öğrendiniz. Passive **her zamanda** kullanılabilir: **be** fiili zamana göre değişir, ana fiil hep **V3**'tür.\n\n| Zaman | Active | Passive |\n|---|---|---|\n| Present continuous | They **are renovating** the rooms. | The rooms **are being renovated**. |\n| Past continuous | They **were cleaning** the pool. | The pool **was being cleaned**. |\n| Present perfect | They **have called** the technician. | The technician **has been called**. |\n| Past perfect | They **had served** breakfast. | Breakfast **had been served**. |\n\n**Formül:** be (zamana göre) + V3\n\n- **being** + V3 → süren eylem (continuous)\n- **been** + V3 → perfect zamanlar\n\n**Olumsuz ve soru:**\n\n- The lift **hasn't been repaired** yet.\n- **Has** the room **been cleaned**?\n- **Is** my car **being serviced** today?",
     "examples": [{"en": "The road is being repaired, so there's a diversion.", "tr": "Yol tamir ediliyor, bu yüzden güzergâh değişti."},
                  {"en": "Your order has been dispatched.", "tr": "Siparişiniz kargoya verildi."},
                  {"en": "When we arrived, all the tickets had been sold.", "tr": "Vardığımızda bütün biletler satılmıştı."}],
     "turkishNote": "Türkçedeki \"tamir ediliyor\" (is being repaired), \"gönderildi\" (has been sent) ve \"satılmıştı\" (had been sold) yapıları İngilizcedeki passive zamanlara oldukça iyi denk gelir. Türkçe konuşanların en sık hatası being ile been'i karıştırmaktır: \"The room is been cleaned\" yanlıştır; continuous için being, perfect için been kullanın."},
    [
        mc("\"Oda temizleniyor.\" (şu an)", ["The room is been cleaned.", "The room is being cleaned."], 1, "Continuous → being."),
        mc("\"Paket gönderildi.\" (sonuç önemli)", ["The parcel has been sent.", "The parcel has being sent."], 0, "Perfect → been."),
        mc("When I got there, the shop ___.", ["had been closed", "had being closed"], 0, "Past perfect → had been."),
        gap("Our kitchen ___ being redecorated at the moment.", ["is"], "is being + V3."),
        gap("Has your car ___ repaired yet?", ["been"], "has been + V3."),
        gap("The meeting ___ been cancelled. (present perfect)", ["has"], "has been."),
        gap("While I was waiting, my bag ___ being checked by security.", ["was"], "was being + V3."),
        gap("The tickets ___ (sell) before we arrived. (past perfect passive)", ["had been sold"], "had been + V3."),
        listen("I'm sorry, sir. Your suit hasn't been cleaned yet. It's being done right now, and it'll be ready in about an hour.", "Takım elbise şu an ne durumda?", ["Temizlendi, hazır", "Şu an temizleniyor", "Kayboldu"], 1, "\"It's being done right now\""),
        typ("İngilizce yazın: \"Yol tamir ediliyor.\"", variants("The road is being repaired.", "The road's being repaired.", "The road is being fixed.", "The road's being fixed."), "The road is being repaired."),
    ],
    {"kind": "speaking", "task": speak("Şehrinizde ya da binanızda şu sıralar neler yapılıyor (is being + V3), son zamanlarda neler yapıldı (has been + V3)? En az 6 passive cümle kurun.",
                                       "In my city, a new metro line is being built, and the main square is being redesigned. Several old buildings have been demolished, and a new park has been opened near the river. In my building, the lift is being repaired this week, and the stairs have just been painted.",
                                       ["is being + V3", "has been + V3", "being / been doğru"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "Yapılmalı, yapılacak", "Passive'i modallarla ve gelecek zamanla kullanarak kurallar, talimatlar ve planlar anlatabilirim.",
    {"kind": "text", "title": "Kiracılar için bilgilendirme", "body": "Dear Residents,\n\nPlease note the following changes:\n\n• The building's water system will be checked on Monday 14 April between 9 am and 2 pm. Water will be turned off during this time.\n\n• All rubbish must be put in the correct bins. Plastic and glass should be separated from food waste.\n\n• Bicycles must not be left in the entrance hall. They can be stored in the basement.\n\n• Any problems with heating or electricity should be reported to the building manager immediately. Repairs will be carried out within 48 hours.\n\n• The new security cameras are going to be installed next month.\n\nThank you for your cooperation.\nThe Management",
     "questions": [
        mc("What will happen on Monday?", ["The cameras will be installed.", "The water system will be checked.", "The bins will be changed."], 1, "\"The building's water system will be checked on Monday\""),
        mc("Where can bicycles be stored?", ["In the entrance hall", "In the basement", "Outside"], 1, "\"They can be stored in the basement.\""),
     ]},
    {"explanation": "**Modal + be + V3**\n\n| Modal | Active | Passive |\n|---|---|---|\n| **will** | They **will check** the system. | The system **will be checked**. |\n| **be going to** | They **are going to install** cameras. | Cameras **are going to be installed**. |\n| **must** | You **must put** rubbish in the bins. | Rubbish **must be put** in the bins. |\n| **should** | You **should report** problems. | Problems **should be reported**. |\n| **can** | You **can store** bikes in the basement. | Bikes **can be stored** in the basement. |\n| **mustn't** | You **mustn't leave** bikes here. | Bikes **must not be left** here. |\n\n**Modal perfect passive** (geçmişe dair):\n\n- The parcel **should have been delivered** yesterday. (Dün teslim edilmiş olmalıydı.)\n- It **can't have been stolen**. (Çalınmış olamaz.) → (Ünite 7'de ayrıntılı)\n\n**Neden passive?** Duyurular, kurallar ve resmî talimatlarda kimin yapacağı belli ya da önemsizdir; odak **eylemin kendisi**dir. Ayrıca passive daha **resmî ve tarafsız** bir ton verir.",
     "examples": [{"en": "The form must be signed and returned by Friday.", "tr": "Form imzalanmalı ve cumaya kadar iade edilmeli."},
                  {"en": "Your new sofa will be delivered between 9 and 12.", "tr": "Yeni kanepeniz 9 ile 12 arasında teslim edilecek."},
                  {"en": "This problem should have been fixed months ago.", "tr": "Bu sorunun aylar önce çözülmüş olması gerekirdi."}],
     "turkishNote": "Türkçedeki \"-ılmalı\" (imzalanmalı), \"-ılacak\" (teslim edilecek) ve \"-ılabilir\" (saklanabilir) yapıları İngilizcedeki modal passive'e denk gelir. Formül her zaman aynıdır: modal + be + V3. \"Must signed\" ya da \"will delivered\" gibi be'siz hatalardan kaçının."},
    [
        mc("\"Form cumaya kadar imzalanmalı.\"", ["The form must signed by Friday.", "The form must be signed by Friday."], 1, "must + be + V3."),
        mc("\"Paket yarın teslim edilecek.\"", ["The parcel will be delivered tomorrow.", "The parcel will deliver tomorrow."], 0, "will be + V3."),
        mc("\"Bisikletler buraya bırakılmamalı.\"", ["Bikes must not be left here.", "Bikes must not leave here."], 0, "must not be + V3."),
        gap("Problems should ___ reported to the manager.", ["be"], "should be + V3."),
        gap("The new cameras are going to be ___ (install) next week.", ["installed"], "going to be + V3."),
        gap("This dress can only be ___ (wash) by hand.", ["washed"], "can be + V3."),
        gap("The parcel should have ___ delivered yesterday.", ["been"], "should have been + V3."),
        gap("All the rooms ___ be cleaned before the guests arrive. (zorunluluk)", ["must", "have to", "should"], "must be + V3."),
        listen("Attention, please. The swimming pool will be closed tomorrow for cleaning. Towels can be collected from reception, and lockers must be emptied by 6 pm today.", "Dolaplar ne zamana kadar boşaltılmalı?", ["Yarın sabah", "Bugün akşam 6'ya kadar", "Havuz açılınca"], 1, "\"lockers must be emptied by 6 pm today\""),
        typ("Passive yapın: \"You must pay the bill within 30 days.\"", variants("The bill must be paid within 30 days.", "The bill must be paid within thirty days."), "The bill must be paid within 30 days."),
    ],
    {"kind": "speaking", "task": speak("Ev arkadaşlarınız için ya da iş yerinizdeki ortak mutfak için 6 kural ve 2 gelecek planı içeren bir duyuru hazırlayın ve JAI'ye okuyun. must be / should be / can be / must not be + V3 ve will be + V3 kullanın.",
                                       "Kitchen rules: All dishes must be washed immediately after use. Food should be labelled with your name. The fridge will be cleaned every Friday, so old food must be removed by Thursday. Coffee cups can be left in the dishwasher. The microwave must not be used for metal containers. A new coffee machine is going to be installed next month.",
                                       ["Modal + be + V3", "will / going to be + V3", "Resmî duyuru tonu"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "Yaptırıyorum", "have something done yapısıyla başkasına yaptırdığım işleri ve aldığım hizmetleri anlatabilirim.",
    {"kind": "dialogue", "title": "Yoğun bir cumartesi", "lines": [
        {"speaker": "Ayşe", "text": "You look different! Have you had your hair cut?"},
        {"speaker": "Burcu", "text": "Yes, I had it done this morning. And I'm having my nails done this afternoon."},
        {"speaker": "Ayşe", "text": "Busy day! I'm having the car serviced. It's been making a strange noise."},
        {"speaker": "Burcu", "text": "Oh, and did you have your kitchen painted in the end?"},
        {"speaker": "Ayşe", "text": "Not yet. We're going to have it done next month. We're also having a new dishwasher installed."},
        {"speaker": "Burcu", "text": "Wow. You'll have a whole new kitchen!"}],
     "questions": [
        mc("What did Burcu have done this morning?", ["Her nails", "Her hair", "Her car"], 1, "\"Have you had your hair cut? – Yes, I had it done this morning.\""),
        mc("When is Ayşe going to have the kitchen painted?", ["This afternoon", "Next month", "Last week"], 1, "\"We're going to have it done next month.\""),
     ]},
    {"explanation": "**have + nesne + V3** → Bir işi **başkasına yaptırmak** (genellikle para ödeyerek, bir hizmet olarak).\n\n| Kendim yaparım | Başkasına yaptırırım |\n|---|---|\n| I **cut** my hair. (kendim kestim) | I **had my hair cut**. (kuaförde kestirdim) |\n| I'm **painting** the kitchen. | I'm **having the kitchen painted**. |\n| I **serviced** my car. | I **had my car serviced**. |\n\n**have her zamanda kullanılabilir:**\n\n| Zaman | Örnek |\n|---|---|\n| Present simple | I **have** my car **serviced** every year. |\n| Present continuous | I'm **having** my nails **done** today. |\n| Past simple | I **had** my hair **cut** yesterday. |\n| Present perfect | **Have** you **had** your hair **cut**? |\n| going to | We're **going to have** the kitchen **painted**. |\n| Modal | You **should have** your eyes **tested**. |\n\n**Sözcük sırası çok önemlidir:**\n\n- I had **my hair cut**. (Saçımı kestirdim.) ✓\n- I had cut my hair. (Saçımı kesmiştim — past perfect, kendim!) ✗ anlamı farklı",
     "examples": [{"en": "I need to have my eyes tested.", "tr": "Gözlerimi muayene ettirmem lazım."},
                  {"en": "We're having our house painted next week.", "tr": "Gelecek hafta evimizi boyatıyoruz."},
                  {"en": "Where do you have your suits made?", "tr": "Takım elbiselerini nerede diktiriyorsun?"}],
     "turkishNote": "Türkçedeki ettirgen ek (-dır, -tir: kestirdim, boyattık, yaptırdım) İngilizcede have + nesne + V3 ile karşılanır. \"I cut my hair yesterday\" demek \"saçımı kendim kestim\" anlamına gelir; kuaförde kestirdiyseniz \"I had my hair cut\" demelisiniz. Sözcük sırasına dikkat: had + nesne + V3."},
    [
        mc("\"Dün saçımı kestirdim.\"", ["I cut my hair yesterday.", "I had my hair cut yesterday."], 1, "Başkasına → had + nesne + V3."),
        mc("Hangisi doğru sıralama?", ["I had cut my hair.", "I had my hair cut."], 1, "had + nesne + V3."),
        mc("\"Arabanın bakımını her yıl yaptırırım.\"", ["I have my car serviced every year.", "I service my car every year."], 0, "Hizmet → have + nesne + V3."),
        gap("We're ___ our kitchen redecorated next month.", ["having"], "having + nesne + V3."),
        gap("Have you had your eyes ___ (test) recently?", ["tested"], "V3."),
        gap("You should have that tooth ___ (look) at.", ["looked"], "have + nesne + V3."),
        gap("I'm going to have my photo ___ (take) for my passport.", ["taken"], "take → taken."),
        order(["had", "I", "my", "car", "washed", "yesterday"], "I had my car washed yesterday.", "had + nesne + V3.", "Dün arabamı yıkattım."),
        listen("I can't come out tonight, sorry. I'm having my new washing machine installed, and they said they'd come between six and eight.", "Konuşan neden bu akşam çıkamıyor?", ["Çamaşır yıkıyor", "Yeni çamaşır makinesi kurduruyor", "Makineyi tamir ediyor"], 1, "\"I'm having my new washing machine installed\""),
        typ("İngilizce yazın: \"Gelecek hafta evimizi boyatıyoruz.\"", variants("We're having our house painted next week.", "We are having our house painted next week.", "We're going to have our house painted next week.", "We are going to have our house painted next week.", "Next week we're having our house painted.", "Next week, we're having our house painted."), "We're having our house painted next week."),
    ],
    {"kind": "speaking", "task": speak("Hangi işleri kendiniz yapıyorsunuz, hangilerini yaptırıyorsunuz? En az 6 cümle kurun: düzenli olarak yaptırdığınız (have ... done), geçenlerde yaptırdığınız (had ... done) ve yakında yaptıracağınız (going to have ... done) şeyler. Kendiniz yaptıklarınızla karşılaştırın.",
                                       "I have my hair cut every six weeks. I never iron my shirts; I have them done at the dry cleaner's. Last month I had my car serviced, and I had my laptop repaired. But I do all the cooking and cleaning myself. Next month, we're going to have a new air conditioner installed. I should also have my eyes tested.",
                                       ["have + nesne + V3 sırası", "Farklı zamanlar", "Kendim yaparım ile karşılaştırma"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Get ile yaptırmak", "get something done, get / have someone do ve get passive yapılarını kullanabilirim.",
    {"kind": "text", "title": "Forum: Kötü tamirci deneyimleri", "body": "@Serkan_K: I got my phone screen replaced at a small shop last month. Two days later, it got broken again. I'm sure they used a cheap screen!\n\n@NurA: I know the feeling. I finally got the landlord to fix our heating after three weeks of emails. We were freezing!\n\n@Hakan77: My advice: always get a written quote before you have anyone do any work. I had a builder repair my roof once, and the final bill was double the price he'd told me.\n\n@SeymaT: Has anyone got their washing machine fixed recently? Mine's making a terrible noise. I'll get my brother to look at it first. He's good at DIY.",
     "questions": [
        mc("What happened to Serkan's phone?", ["It got stolen.", "The screen got broken again.", "It was never repaired."], 1, "\"it got broken again\""),
        mc("What is Hakan's advice?", ["Always do DIY.", "Get a written quote first.", "Never use builders."], 1, "\"always get a written quote\""),
     ]},
    {"explanation": "**1. get + nesne + V3** = have + nesne + V3 (yaptırmak)\n\n- I **got** my phone screen **replaced**. = I **had** it replaced.\n- get daha **günlük** ve bazen **zorluk / çaba** vurgusu taşır: I finally **got** the car **fixed**!\n\n**2. Birine bir şey yaptırmak (kişi belli):**\n\n| Yapı | Örnek | Not |\n|---|---|---|\n| **get** + kişi + **to** + fiil | I **got** my brother **to** fix it. | ikna etme, çaba |\n| **have** + kişi + fiil (to yok) | I **had** a builder **repair** the roof. | hizmet, talimat |\n\n**3. get passive** (günlük dil): be yerine get\n\n- My phone **got broken**. (= was broken)\n- He **got fired**. / They **got married**. / I **got stuck** in traffic.\n- Genellikle **beklenmedik, istenmeyen** ya da **değişim** bildiren durumlarda kullanılır.\n\n**Kaza ve başa gelen olumsuz olaylar için have / get:**\n\n- I **had** my wallet **stolen**. (Cüzdanımı çaldırdım. — Ben istemedim!)\n- She **got** her bag **snatched**.",
     "examples": [{"en": "I finally got my landlord to fix the heating.", "tr": "Sonunda ev sahibime kaloriferi tamir ettirdim."},
                  {"en": "We had a decorator paint the whole flat.", "tr": "Bütün daireyi bir boyacıya boyattık."},
                  {"en": "I had my bike stolen outside the library.", "tr": "Bisikletimi kütüphanenin önünde çaldırdım."}],
     "turkishNote": "\"Cüzdanımı çaldırdım\" cümlesi Türkçede de ettirgen gibi görünür ama istemediğimiz bir olayı anlatır; İngilizcede de \"I had my wallet stolen\" aynı şekilde kullanılır. \"get someone to do\" yapısında to unutulmamalı, \"have someone do\" yapısında ise to kullanılmamalıdır: I got him to help ✓ / I had him help ✓ / I got him help ✗."},
    [
        mc("\"Kardeşime tamir ettirdim.\" (ikna ettim)", ["I got my brother fix it.", "I got my brother to fix it."], 1, "get + kişi + to."),
        mc("\"Bir elektrikçiye kontrol ettirdim.\"", ["I had an electrician to check it.", "I had an electrician check it."], 1, "have + kişi + fiil (to yok)."),
        mc("\"Cüzdanımı çaldırdım.\"", ["I stole my wallet.", "I had my wallet stolen."], 1, "İstenmeyen olay → had + nesne + V3."),
        mc("Günlük dil: \"My phone ___ broken.\"", ["got", "had"], 0, "get passive."),
        gap("I finally got the car ___ (fix).", ["fixed"], "get + nesne + V3."),
        gap("Can you get your sister ___ help us?", ["to"], "get + kişi + to."),
        gap("I'll have the receptionist ___ (call) you a taxi.", ["call"], "have + kişi + yalın fiil."),
        gap("We got ___ (stick) in traffic for two hours.", ["stuck"], "get stuck."),
        listen("Last summer I had my passport stolen in Rome. I had to go to the embassy, and I finally got them to issue a temporary one after two days.", "Konuşanın başına ne geldi?", ["Pasaportunu kaybetti", "Pasaportunu çaldırdı", "Pasaportunun süresi doldu"], 1, "\"I had my passport stolen\""),
        typ("İngilizce yazın: \"Sonunda ev sahibime kaloriferi tamir ettirdim.\"", variants("I finally got my landlord to fix the heating.", "I finally got the landlord to fix the heating.", "I finally got my landlord to repair the heating.", "I finally got the landlord to repair the heating.", "Finally, I got my landlord to fix the heating.", "I finally had my landlord fix the heating."), "I finally got my landlord to fix the heating."),
    ],
    {"kind": "speaking", "task": speak("Bir tamir ya da hizmet sürecinin nasıl zorlaştığını anlatın. get something done, get someone to do, have someone do ve get passive (got broken / got stuck / got lost) yapılarını en az birer kez kullanın.",
                                       "Last winter, our boiler got broken just before New Year. I called the landlord, but it took a week to get him to send someone. In the end, I had a plumber come on a Sunday, and I paid him myself. He got the boiler fixed in an hour! Then I got my landlord to pay me back.",
                                       ["get + nesne + V3", "get + kişi + to / have + kişi + fiil", "get passive"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Şikâyet yazıyorum", "Kötü bir hizmet hakkında passive ve resmî dil kullanarak etkili bir şikâyet e-postası yazabilirim.",
    {"kind": "text", "title": "Örnek şikâyet e-postası", "body": "Subject: Complaint about order #48213\n\nDear Sir or Madam,\n\nI am writing to complain about the service I received from your company.\n\nOn 3 March, I ordered a dining table from your website. I was told that it would be delivered within five working days. However, it was not delivered until 21 March, and I was not informed about the delay.\n\nWhen the table finally arrived, I discovered that one of the legs had been damaged. I have attached photos of the damage. I have called your customer service three times, but my calls have not been returned.\n\nI would like the table to be replaced as soon as possible. Alternatively, I expect a full refund. I also believe that some compensation should be offered for the inconvenience.\n\nI look forward to receiving your reply within seven days.\n\nYours faithfully,\nZeynep Kılıç",
     "questions": [
        mc("What was wrong with the table?", ["It was the wrong colour.", "One of the legs had been damaged.", "It was too small."], 1, "\"one of the legs had been damaged\""),
        mc("What does Zeynep want?", ["A discount on her next order", "A replacement or a full refund", "Only an apology"], 1, "\"I would like the table to be replaced... Alternatively, I expect a full refund.\""),
     ]},
    {"explanation": "**Resmî şikâyet e-postasının yapısı:**\n\n| Bölüm | Kalıplar |\n|---|---|\n| **Selamlama** | Dear Sir or Madam, (isim bilinmiyorsa) / Dear Mr / Ms ..., |\n| **Amaç** | I am writing to **complain about** ... / to **express my dissatisfaction with** ... |\n| **Olay** | On [date], I ordered / bought ... / I **was told** that ... / I **was promised** ... |\n| **Sorun** | However, ... / Unfortunately, ... / ... **had been damaged** / **was not delivered** |\n| **Yapılan girişimler** | I **have contacted** ... / My calls **have not been returned**. |\n| **Talep** | I would like ... **to be replaced / refunded** / I expect a full refund. |\n| **Kapanış** | I look forward to receiving your reply. / Yours **faithfully**, (Dear Sir or Madam ile) / Yours **sincerely**, (isimle) |\n\n**Passive neden etkili?**\n\n- Daha **resmî ve tarafsız** bir ton verir.\n- Suçlamayı **kişiselleştirmeden** sorunu ortaya koyar: *The table **was damaged*** (siz zarar verdiniz demek yerine).\n- **I was told / I was promised** → verilen sözleri hatırlatır.\n\n**Dikkat:**\n\n- Kısaltma kullanmayın: I am (~~I'm~~), was not (~~wasn't~~).\n- Öfkeli değil, **kararlı ve net** olun.",
     "examples": [{"en": "I was promised that the problem would be solved within 24 hours.", "tr": "Sorunun 24 saat içinde çözüleceğine dair söz verildi."},
                  {"en": "I would like my money to be refunded in full.", "tr": "Paramın tamamının iade edilmesini istiyorum."},
                  {"en": "I am writing to express my dissatisfaction with your service.", "tr": "Hizmetinizden duyduğum memnuniyetsizliği bildirmek için yazıyorum."}],
     "turkishNote": "Türkçe şikâyet yazılarında bazen duygusal ve uzun cümleler kullanılır. İngilizce resmî yazılarda kısa, net ve olgulara dayalı cümleler daha etkilidir. \"Yours faithfully\" (alıcının adını bilmiyorsanız) ile \"Yours sincerely\" (adını biliyorsanız) arasındaki farka dikkat edin."},
    [
        mc("İsmini bilmediğiniz birine resmî e-posta:", ["Dear Sir or Madam,", "Hi there,", "Dear friend,"], 0, "Dear Sir or Madam."),
        mc("\"Dear Sir or Madam\" ile başlayan e-postanın kapanışı:", ["Yours sincerely,", "Yours faithfully,", "Love,"], 1, "Yours faithfully."),
        mc("Daha resmî ve tarafsız:", ["You damaged my table.", "The table was damaged."], 1, "Passive → tarafsız."),
        gap("I am writing to ___ about the service I received.", ["complain"], "complain about."),
        gap("I was ___ that it would be delivered on Monday. (söylendi)", ["told", "promised"], "I was told."),
        gap("My emails have not ___ answered.", ["been"], "have not been + V3."),
        gap("I would like the product ___ be replaced.", ["to"], "would like + nesne + to be + V3."),
        gap("I look forward to ___ (receive) your reply.", ["receiving"], "look forward to + -ing."),
        listen("Hello, I'm calling about my order. I was told it would be delivered yesterday, but it still hasn't arrived, and I haven't been given any tracking number.", "Müşteriye ne verilmemiş?", ["Fatura", "Takip numarası", "İndirim"], 1, "\"I haven't been given any tracking number\""),
        typ("İngilizce yazın: \"Paramın tamamının iade edilmesini istiyorum.\" (resmî)", variants("I would like a full refund.", "I would like my money to be refunded in full.", "I would like to receive a full refund.", "I would like my money to be fully refunded.", "I would like a full refund, please.", "I would like the full amount to be refunded."), "I would like a full refund."),
    ],
    {"kind": "writing", "task": write("Aşağıdaki durumlardan biri hakkında resmî bir şikâyet e-postası yazın (180–220 kelime): 1) Bir otelde rezervasyonunuz kaybolmuş ve size daha kötü bir oda verilmiş. 2) Tamire verdiğiniz telefonunuz iki hafta geç ve hâlâ arızalı olarak geri gelmiş. 3) Bir dil kursu söz verdiği hizmetleri sağlamamış. En az 6 farklı passive yapı (farklı zamanlar ve modallar) kullanın ve net bir talepte bulunun.",
                                      "Subject: Complaint about phone repair (Ref. 2291)\n\nDear Sir or Madam,\n\nI am writing to complain about the repair service I received at your branch in Kadıköy.\n\nOn 2 May, I left my phone at your shop because the screen had been cracked. I was told that it would be repaired within three working days. However, I was not contacted until 17 May, two weeks later than promised.\n\nWhen I collected the phone, I was assured that it had been fully tested. Unfortunately, the touch screen stopped working the same evening. I have returned to the shop twice since then, but the problem has still not been solved, and I have been asked to wait another week.\n\nI have been a loyal customer of your company for five years, and I am extremely disappointed. I would like my phone to be repaired properly within the next three days, or replaced with a new one. I also believe that the repair fee should be refunded.\n\nI have attached a copy of my receipt. I look forward to receiving your reply.\n\nYours faithfully,\nEmre Yüksel",
                                      ["Resmî e-posta yapısı", "En az 6 farklı passive", "Net talep", "Resmî ve kararlı ton", "Kısaltma yok"])},
)

u.test([
    mc("\"Oda şu an temizleniyor.\"", ["The room is been cleaned.", "The room is being cleaned."], 1, "being"),
    mc("\"Siparişiniz kargoya verildi.\"", ["Your order has been dispatched.", "Your order has dispatched."], 0, "has been + V3"),
    mc("\"Form imzalanmalı.\"", ["The form must sign.", "The form must be signed."], 1, "must be + V3"),
    mc("\"Saçımı kestirdim.\"", ["I cut my hair.", "I had my hair cut."], 1, "have + nesne + V3"),
    mc("\"Kardeşime yardım ettirdim.\" (ikna ettim)", ["I got my brother help me.", "I got my brother to help me."], 1, "get + kişi + to"),
    mc("\"Dear Sir or Madam\" → kapanış:", ["Yours sincerely", "Yours faithfully"], 1, "faithfully"),
    gap("When we arrived, all the food ___ been eaten.", ["had"], "had been + V3"),
    gap("The new bridge ___ be opened next year.", ["will"], "will be + V3"),
    gap("I'm having my car ___ (service) tomorrow.", ["serviced"], "have + nesne + V3"),
    gap("I had a plumber ___ (fix) the pipe.", ["fix"], "have + kişi + yalın fiil"),
    gap("I had my bike ___ (steal) last week.", ["stolen"], "had + nesne + V3"),
    gap("I would like the item ___ be replaced.", ["to"], "would like + to be"),
    listen("I'm sorry, madam. Your dress hasn't been altered yet because our tailor is ill. It will be finished by Thursday, and it can be delivered to your home if you prefer.", "Elbise ne zaman bitmiş olacak?", ["Bugün", "Perşembeye kadar", "Gelecek hafta"], 1, "\"It will be finished by Thursday\""),
    typ("İngilizce yazın: \"Gözlerimi muayene ettirmem lazım.\"", variants("I need to have my eyes tested.", "I need to get my eyes tested.", "I need to have my eyes checked.", "I need to get my eyes checked.", "I have to have my eyes tested.", "I have to get my eyes tested."), "I need to have my eyes tested."),
    write("Yeni taşındığınız bir dairede birçok sorun var. Ev sahibinize resmî ama kibar bir e-posta yazın (160–200 kelime): Hangi sorunlar fark edildi, nelerin yapılması gerekiyor, siz kendiniz neleri yaptırdınız ve ondan ne talep ediyorsunuz? Farklı passive zamanları, modal passive ve have / get something done yapılarını kullanın.",
          "Dear Mr Aksoy,\n\nI am writing about several problems in the flat, which I moved into on 1 September.\n\nFirstly, the kitchen tap had not been repaired before I arrived, even though I was told it would be fixed. It is still leaking, and the cupboard underneath has been damaged by the water. Secondly, the heating has not been working properly since last week. I have had an electrician check the system, and he says the boiler needs to be replaced.\n\nIn addition, the bedroom window cannot be closed completely, so the room gets very cold at night. I have also noticed that the walls in the bathroom have not been painted for a long time.\n\nI had the tap temporarily fixed by a plumber last Friday, and I paid 800 lira for the visit. I have attached the receipt, and I would be grateful if this amount could be refunded.\n\nI would appreciate it if the boiler and the window could be repaired as soon as possible, ideally before the end of this month.\n\nThank you for your help. I look forward to hearing from you.\n\nYours sincerely,\nDeniz Akın",
          ["Farklı passive zamanlar", "Modal passive", "have / get something done", "Resmî ve kibar ton", "Net talepler"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

"""B2 Ünite 9: İkna."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("B2", 9, "İkna", "Persuasion",
         "Dolaylı ve yumuşatılmış yapılarla kibar ricada bulunabilir, resmî ve samimi üslup arasında geçiş yapabilir, bir fikri ikna edici gerekçelerle savunabilir ve iş hayatında kullanılabilecek resmî bir rica e-postası yazabilirim.",
         ["kibar rica: I was wondering if, Would you mind, Would it be possible", "yumuşatma: geçmiş zamanla mesafe, I'm afraid, slightly", "resmî kelime seçimi (register)", "ikna dili", "resmî e-posta ve iş yazışması"],
         ["iş yazışmaları", "müzakere ve rica", "ikna ve gerekçe"],
         {"title": "Ricam var", "durationMinutes": 45,
          "goal": "Öğrenciler ikili gruplarda zor bir rica senaryosu alır (patrondan izin istemek, bir otelden ücret iadesi, komşudan gürültüyü azaltmasını istemek). Önce çok kaba, sonra çok kibar ve en son \"tam kıvamında\" bir versiyonunu canlandırırlar. Sınıf hangi yapıların en ikna edici olduğunu tartışır."})

u.vocab([
    ("request", "rica, talep; rica etmek", "I'd like to make a request.", "Bir ricada bulunmak istiyorum.", None),
    ("enquire", "bilgi almak, sormak (resmî)", "I am writing to enquire about your courses.", "Kurslarınız hakkında bilgi almak için yazıyorum.", "AmE: inquire"),
    ("regarding", "ile ilgili olarak", "I'm writing regarding your invoice.", "Faturanızla ilgili olarak yazıyorum.", None),
    ("assist", "yardımcı olmak (resmî)", "How can I assist you?", "Size nasıl yardımcı olabilirim?", None),
    ("require", "gerektirmek, ihtiyaç duymak (resmî)", "Please let us know if you require any further information.", "Ek bilgiye ihtiyaç duyarsanız lütfen bildirin.", None),
    ("grateful", "minnettar", "I would be grateful if you could reply soon.", "Kısa sürede cevap verirseniz minnettar olurum.", None),
    ("appreciate", "takdir etmek, minnettar olmak", "I'd really appreciate your help.", "Yardımınız için çok minnettar olurum.", None),
    ("convenient", "uygun", "Would Monday be convenient for you?", "Pazartesi sizin için uygun olur mu?", None),
    ("attached", "ekte", "Please find attached my CV.", "Özgeçmişim ekte yer almaktadır.", None),
    ("further", "ek, daha fazla", "For further details, please contact us.", "Daha fazla ayrıntı için lütfen bize ulaşın.", None),
    ("in advance", "şimdiden", "Thank you in advance for your help.", "Yardımınız için şimdiden teşekkürler.", None),
    ("at your earliest convenience", "en kısa sürede (size uygun olan ilk fırsatta)", "Please reply at your earliest convenience.", "Lütfen en kısa sürede cevap verin.", None),
    ("unfortunately", "maalesef", "Unfortunately, we are unable to accept your offer.", "Maalesef teklifinizi kabul edemiyoruz.", None),
    ("be unable to", "yapamamak (resmî)", "We are unable to offer a refund.", "Ücret iadesi yapamıyoruz.", None),
    ("proposal", "öneri, teklif", "I'd like to present a proposal.", "Bir öneri sunmak istiyorum.", None),
    ("benefit", "fayda; fayda sağlamak", "This change would benefit everyone.", "Bu değişiklik herkese fayda sağlar.", None),
    ("persuade", "ikna etmek", "She persuaded me to apply.", "Başvurmam için beni ikna etti.", None),
    ("convince", "inandırmak, ikna etmek", "I'm not convinced it's a good idea.", "İyi bir fikir olduğuna ikna olmadım.", None),
    ("compromise", "uzlaşma, orta yol", "Let's try to find a compromise.", "Bir orta yol bulmaya çalışalım.", None),
    ("negotiate", "pazarlık etmek, müzakere etmek", "We need to negotiate a better price.", "Daha iyi bir fiyat için pazarlık yapmamız gerek.", None),
    ("deadline", "son tarih", "Could we extend the deadline?", "Son tarihi uzatabilir miyiz?", None),
    ("extend", "uzatmak", "They agreed to extend my contract.", "Sözleşmemi uzatmayı kabul ettiler.", None),
    ("look forward to", "dört gözle beklemek", "I look forward to hearing from you.", "Sizden haber almayı dört gözle bekliyorum.", "+ -ing"),
    ("on behalf of", "adına", "I'm writing on behalf of my team.", "Ekibim adına yazıyorum.", None),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Acaba ... mümkün mü?", "I was wondering if, Would you mind ve Would it be possible gibi yapılarla kibar ricalarda bulunabilirim.",
    {"kind": "dialogue", "title": "Yöneticiyle konuşma", "lines": [
        {"speaker": "Aslı", "text": "Sorry to bother you, Mr Demir. Have you got a minute?"},
        {"speaker": "Mr Demir", "text": "Of course, Aslı. Come in."},
        {"speaker": "Aslı", "text": "I was wondering if I could work from home on Fridays. My commute takes nearly two hours."},
        {"speaker": "Mr Demir", "text": "Hmm. I'll need to think about it. Would you mind sending me a short proposal?"},
        {"speaker": "Aslı", "text": "Not at all. Would it be possible to try it for a month first?"},
        {"speaker": "Mr Demir", "text": "That sounds reasonable. Send me the details and we'll discuss it next week."}],
     "questions": [
        mc("What does Aslı want?", ["A pay rise", "To work from home on Fridays", "A new office"], 1, "\"work from home on Fridays\""),
        mc("What does Mr Demir ask her to do?", ["Send a short proposal", "Talk to HR", "Come back tomorrow"], 0, "\"Would you mind sending me a short proposal?\""),
     ]},
    {"explanation": "Bir şeyi ne kadar **dolaylı** isterseniz o kadar **kibar** olursunuz.\n\n| Kibarlık | Yapı |\n|---|---|\n| Doğrudan | **Can** I work from home? |\n| Kibar | **Could** I work from home? |\n| Daha kibar | **Would it be possible** (for me) **to** work from home? |\n| Daha kibar | **Do you think I could** work from home? |\n| Çok kibar | **I was wondering if** I could work from home. |\n\n**Would you mind ...?**\n\n| Yapı | Anlam |\n|---|---|\n| **Would you mind** + **-ing**? | Sizin bir şey yapmanızı rica ederim. |\n| *Would you mind **sending** me the file?* | Dosyayı gönderir misiniz? |\n| **Would you mind if I** + past? | Ben bir şey yapabilir miyim? |\n| *Would you mind **if I opened** the window?* | Pencereyi açmamın sakıncası var mı? |\n\n**Dikkat:** \"Would you mind\" sorusunu **kabul ederken \"No\"** denir, çünkü soru \"sakıncası var mı?\" demektir:\n\n- *Would you mind waiting?* → **Not at all.** / **No, of course not.** (Hayır, sakıncası yok = tamam.)\n\n**Ricaya giriş:** *Sorry to bother you, but ...* / *I hope you don't mind me asking, but ...*",
     "examples": [{"en": "I was wondering if you could help me with this report.", "tr": "Acaba bu raporda bana yardım edebilir misiniz diye düşünüyordum."},
                  {"en": "Would you mind closing the door?", "tr": "Kapıyı kapatır mısınız?"},
                  {"en": "Would it be possible to change my appointment?", "tr": "Randevumu değiştirmek mümkün olur mu?"}],
     "turkishNote": "Türkçede kibarlık genellikle \"-ebilir misiniz\", \"rica etsem\", \"acaba\" gibi kelimelerle sağlanır. İngilizcede \"I was wondering if\" Türkçedeki \"acaba\"ya çok yakındır. Türkçe konuşanların en sık hatası \"Would you mind\" sorusuna \"Yes\" diyerek kabul etmektir: \"Yes\" aslında \"Evet, sakıncası var\" anlamına gelir! Ayrıca \"Would you mind to send\" yanlıştır; \"mind\" -ing alır."},
    [
        mc("En kibar olanı:", ["Can you help me?", "I was wondering if you could help me."], 1, "I was wondering if."),
        mc("Hangisi doğru?", ["Would you mind to wait?", "Would you mind waiting?"], 1, "mind + -ing."),
        mc("\"Would you mind helping me?\" Kabul etmek için:", ["Yes, I would.", "Not at all."], 1, "Sakıncası yok → Not at all."),
        mc("\"Pencereyi açmamın sakıncası var mı?\"", ["Would you mind if I opened the window?", "Would you mind opening the window?"], 0, "Ben → if I + past."),
        gap("I was ___ if I could leave early today.", ["wondering"], "I was wondering if."),
        gap("Would it be ___ to reschedule the meeting?", ["possible"], "Would it be possible to."),
        gap("Would you mind ___ (repeat) that, please?", ["repeating"], "mind + -ing."),
        gap("Sorry to ___ you, but have you got a minute?", ["bother"], "Sorry to bother you."),
        listen("Excuse me, I hope you don't mind me asking, but would it be possible to swap seats? My friend is sitting just behind you, and we'd love to sit together.", "Konuşan ne istiyor?", ["Pencere kenarı", "Koltuk değiştirmek", "Bir içecek"], 1, "\"would it be possible to swap seats?\""),
        typ("Kibarlaştırın (I was wondering if): \"Can you give me a lift?\"", variants("I was wondering if you could give me a lift.", "I was wondering if you could give me a lift?"), "I was wondering if you could give me a lift."),
    ],
    {"kind": "speaking", "task": speak("Aşağıdaki ricaları üç farklı kibarlık düzeyinde (Could you / Would you mind / I was wondering if) söyleyin: (1) Komşunuzdan müziğin sesini kısmasını istemek. (2) Öğretmeninizden ödevin teslim tarihini uzatmasını istemek. (3) Bir iş arkadaşınızdan sunumunuza göz atmasını istemek. Her ricaya kısa bir gerekçe ekleyin.",
                                       "One: Could you turn the music down, please? Would you mind turning the music down? I've got an exam tomorrow. Two: Could I have a few more days for the essay? I was wondering if it would be possible to extend the deadline, because I've been ill all week. Three: Would you mind having a look at my presentation? I was wondering if you could give me some feedback before Monday.",
                                       ["Kibarlık düzeyleri", "Would you mind + -ing", "Gerekçe ekleme"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "Yumuşatarak söylemek", "Olumsuz haberleri ve eleştirileri yumuşatma teknikleriyle diplomatik bir şekilde iletebilirim.",
    {"kind": "text", "title": "Bir müşteriye yanıt: iki versiyon", "body": "Version A:\n\"Your order is late. We can't deliver it this week. There is a problem with our supplier. You have to wait until next month.\"\n\nVersion B:\n\"I'm afraid there has been a slight delay with your order. Unfortunately, we won't be able to deliver it this week, as there seems to be a small problem with our supplier. We were hoping to send it by Friday, but it looks as though it may not arrive until early next month. We do apologise for any inconvenience.\"",
     "questions": [
        mc("Which version sounds more professional?", ["Version A", "Version B"], 1, "Yumuşatılmış dil."),
        mc("When will the order probably arrive?", ["This Friday", "Early next month", "Next year"], 1, "\"may not arrive until early next month\""),
     ]},
    {"explanation": "Kötü haber verirken, eleştiri yaparken ya da hayır derken **yumuşatma** (softening) teknikleri kullanılır.\n\n| Teknik | Doğrudan | Yumuşatılmış |\n|---|---|---|\n| **I'm afraid / Unfortunately** | It's late. | **I'm afraid** it's a little late. |\n| **Küçültücüler:** slight, a bit, a little, small | There's a problem. | There's **a slight** problem. |\n| **seem / appear** | You made a mistake. | There **seems to be** a mistake. |\n| **Geçmiş zamanla mesafe** | We hope to send it. | We **were hoping** to send it. |\n| **Olumsuz + olumlu sıfat** | It's bad. | It's **not ideal**. / It's **not very** good. |\n| **Modal'larla belirsizlik** | It won't arrive. | It **may not** arrive. |\n| **Kişisizleştirme (passive)** | You didn't pay. | The payment **hasn't been received**. |\n\n**Geçmiş zamanla mesafe:** Şu an için konuşsanız bile geçmiş (sürekli) zaman ricayı daha az ısrarcı yapar:\n\n- *I **wanted** to ask you something.*\n- *We **were wondering** if you could ...*\n- *I **was hoping** you might help.*\n\n**Olumsuz durumu kabul etme:** *We do apologise for any inconvenience.* (**do** vurgu için)",
     "examples": [{"en": "I'm afraid we won't be able to attend the meeting.", "tr": "Maalesef toplantıya katılamayacağız."},
                  {"en": "There seems to be a small mistake in the invoice.", "tr": "Faturada küçük bir hata var gibi görünüyor."},
                  {"en": "Your idea isn't bad, but it might not be ideal for this project.", "tr": "Fikriniz kötü değil, ama bu proje için ideal olmayabilir."}],
     "turkishNote": "Türkçede yumuşatma için \"maalesef\", \"biraz\", \"galiba\", \"-ebilir\" gibi kelimeler kullanılır; İngilizcede de benzer araçlar var, ama iş dünyasında çok daha sistematik kullanılır. Türkçeden doğrudan çevrilen \"You did this wrong\" gibi cümleler İngilizcede çok kaba algılanabilir. \"There seems to be a mistake\" gibi kişisizleştirilmiş yapılar suçlamadan sorunu belirtmenin en iyi yoludur."},
    [
        mc("En diplomatik:", ["You made a mistake.", "There seems to be a mistake."], 1, "Kişisizleştirme + seem."),
        mc("\"I'm afraid\" burada ne anlama gelir? \"I'm afraid we're fully booked.\"", ["Korkuyorum", "Maalesef"], 1, "Yumuşatma."),
        mc("Geçmiş zamanla mesafe:", ["I hope you can help.", "I was hoping you could help."], 1, "Daha kibar."),
        mc("\"It's bad\" yumuşatılmışı:", ["It's terrible.", "It's not ideal."], 1, "Olumsuz + olumlu."),
        gap("There's a ___ problem with your booking. (küçük, hafif)", ["slight", "small"], "slight / small."),
        gap("___, we are unable to offer a refund. (Maalesef)", ["Unfortunately"], "Unfortunately."),
        gap("We do apologise for any ___. (rahatsızlık)", ["inconvenience"], "inconvenience."),
        gap("The payment ___ not been received yet.", ["has"], "Edilgen ile kişisizleştirme."),
        listen("Thank you for your report. It's very detailed. However, I'm afraid there seem to be a few small errors in the figures, and the conclusion might be a bit too long. Would you mind having another look before Friday?", "Yönetici raporla ilgili ne düşünüyor?", ["Mükemmel", "İyi ama birkaç küçük hata var", "Tamamen yanlış"], 1, "\"very detailed. However... a few small errors\""),
        typ("Yumuşatın: \"You sent the wrong file.\" (seems)", variants("It seems the wrong file was sent.", "There seems to be a problem with the file.", "It seems that the wrong file was sent.", "I think the wrong file may have been sent."), "It seems the wrong file was sent."),
    ],
    {"kind": "speaking", "task": speak("Bir iş ortamında bu üç kötü haberi diplomatik bir dille verin: (1) Bir müşteriye ürününün iki hafta gecikeceğini söylemek. (2) Bir iş arkadaşına raporunda hatalar olduğunu söylemek. (3) Bir toplantı davetini reddetmek. I'm afraid, unfortunately, seem, slight, geçmiş zamanla mesafe ve modal'ları kullanın.",
                                       "One: I'm afraid there's been a slight delay with your order. Unfortunately, it may not arrive for another two weeks. We do apologise for the inconvenience. Two: I had a look at your report. It's really good, but there seem to be a couple of small errors in the figures. Would you mind checking them again? Three: Thank you for the invitation. I was hoping to come, but unfortunately I won't be able to attend, as I have another meeting at that time.",
                                       ["Yumuşatma teknikleri", "Diplomatik üslup", "Olumlu ile olumsuzu dengeleme"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "Resmî mi, samimi mi?", "Aynı mesajı resmî ve samimi üslupta ifade edebilir ve bağlama uygun kelimeyi seçebilirim.",
    {"kind": "text", "title": "Aynı mesaj, iki üslup", "body": "Message to a friend:\n\"Hi Burcu! Just wanted to ask about the course you told me about. How much is it, and when does it start? Can you send me the link? Thanks a lot!\"\n\nEmail to a language school:\n\"Dear Sir or Madam,\nI am writing to enquire about your advanced Spanish course. I would be grateful if you could provide information regarding the fees and start dates. In addition, I would appreciate it if you could send me a copy of the course programme.\nThank you in advance for your assistance.\nYours faithfully,\nSevgi Çelik\"",
     "questions": [
        mc("What does Sevgi want to know?", ["The teacher's name", "The fees and start dates", "The school's address"], 1, "\"information regarding the fees and start dates\""),
        mc("Which message uses \"enquire\"?", ["The message to a friend", "The email to the school"], 1, "Resmî."),
     ]},
    {"explanation": "**Register (üslup):** Kime yazdığınıza göre kelime ve yapı seçimi değişir.\n\n| Samimi | Resmî |\n|---|---|\n| ask about | **enquire about** |\n| get | **receive / obtain** |\n| need | **require** |\n| help | **assist / assistance** |\n| about | **regarding / concerning** |\n| want | **would like / wish to** |\n| give | **provide** |\n| also | **in addition / furthermore** |\n| but | **however** |\n| sorry | **I apologise / We regret** |\n| can't | **am unable to** |\n| tell | **inform** |\n| start / end | **commence / conclude** (çok resmî) |\n\n**Resmî yazının diğer özellikleri:**\n\n- **Kısaltma yok:** I'm → I am, can't → cannot\n- **Edilgen yapılar daha sık:** *Your application has been received.*\n- **Phrasal verb'ler yerine tek kelime:** find out → discover, put off → postpone\n- **Uzun ve kibar ricalar:** *I would be grateful if you could ...* / *I would appreciate it if you could ...*\n\n**Dikkat:** Çok resmî dili arkadaşlara kullanmak tuhaf, hatta komik durur!",
     "examples": [{"en": "I would be grateful if you could send me further information.", "tr": "Bana ek bilgi gönderirseniz minnettar olurum."},
                  {"en": "We regret to inform you that the event has been cancelled.", "tr": "Etkinliğin iptal edildiğini üzülerek bildiririz."},
                  {"en": "Please do not hesitate to contact me if you require any assistance.", "tr": "Herhangi bir yardıma ihtiyacınız olursa benimle iletişime geçmekten çekinmeyin."}],
     "turkishNote": "Türkçede resmî yazışmada \"Sayın\", \"arz ederim\", \"bilgilerinize sunarım\" gibi kalıplar kullanılır. İngilizce resmî yazı daha sadedir ama kelime seçimi çok önemlidir. Türkçe konuşanlar bazen iki uç arasında kalır: ya fazla samimi (\"Hi, I want info\") ya da fazla süslü yazarlar. B2 seviyesinde amaç, açık, kibar ve profesyonel olmaktır."},
    [
        mc("Resmî: \"I want to ask about the job.\"", ["I wish to enquire about the position.", "I wanna ask about the job."], 0, "Resmî."),
        mc("\"need\" resmî karşılığı:", ["require", "acquire"], 0, "require."),
        mc("\"about\" resmî karşılığı:", ["regarding", "around"], 0, "regarding."),
        mc("Resmî bir e-postada:", ["I can't come.", "I am unable to attend."], 1, "Resmî."),
        gap("I would be ___ if you could reply by Friday. (minnettar)", ["grateful"], "would be grateful."),
        gap("We regret to ___ you that your application was unsuccessful. (bildirmek)", ["inform"], "inform."),
        gap("Please do not ___ to contact me. (çekinmeyin)", ["hesitate"], "do not hesitate."),
        gap("I would ___ it if you could send me a copy. (minnettar olurum)", ["appreciate"], "appreciate it if."),
        match([("get", "receive"), ("help", "assist"), ("give", "provide"), ("tell", "inform"), ("but", "however")], "Samimi kelimeyi resmî karşılığıyla eşleştirin."),
        listen("Good morning. I'm calling regarding the invoice I received yesterday. I'm afraid there seems to be an error. I was charged twice for the same service. I would be grateful if you could look into it and inform me when it has been corrected.", "Konuşan neden arıyor?", ["Yeni bir hizmet almak için", "Faturada iki kez ücretlendirildiği için", "Bir randevuyu iptal etmek için"], 1, "\"I was charged twice for the same service.\""),
    ],
    {"kind": "speaking", "task": speak("Aynı mesajı iki kez söyleyin: önce bir arkadaşa sesli mesaj olarak, sonra bir otelin rezervasyon bölümüne telefonda. Mesaj: Haziranda 3 gece kalmak istiyorsunuz, fiyatı ve kahvaltının dahil olup olmadığını soruyorsunuz, havaalanı transferi var mı öğrenmek istiyorsunuz.",
                                       "To a friend: Hey Aylin! So, I'm thinking of staying at that hotel you told me about for three nights in June. Do you know how much it is? Is breakfast included? Oh, and can they pick us up from the airport? Thanks! To the hotel: Good morning. I'm calling to enquire about availability for three nights in June. Could you tell me the price per night, and whether breakfast is included? I would also like to know if you provide an airport transfer service. Thank you very much.",
                                       ["Samimi üslup", "Resmî kelime seçimi", "Dolaylı sorular", "Üsluplar arası net fark"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "İkna etmek", "Bir öneriyi faydalarını vurgulayarak, itirazları önceden cevaplayarak ve uzlaşma önererek ikna edici bir şekilde savunabilirim.",
    {"kind": "dialogue", "title": "Toplantıda bir öneri", "lines": [
        {"speaker": "Kerim", "text": "I'd like to suggest that we move the team meeting from Monday morning to Tuesday afternoon."},
        {"speaker": "Manager", "text": "Why? Monday's always been fine."},
        {"speaker": "Kerim", "text": "Well, on Monday mornings, most of us are dealing with emails from the weekend. If we met on Tuesday, everyone would be better prepared."},
        {"speaker": "Manager", "text": "But some people work from home on Tuesdays."},
        {"speaker": "Kerim", "text": "That's true, but we could easily do it online. In fact, it would save time, because nobody would need to book a room."},
        {"speaker": "Manager", "text": "I'm still not entirely convinced."},
        {"speaker": "Kerim", "text": "How about trying it for a month? If it doesn't work, we can always go back to Monday."},
        {"speaker": "Manager", "text": "OK, that seems fair. Let's give it a try."}],
     "questions": [
        mc("Why does Kerim want to change the day?", ["Monday is a holiday.", "People are busy with emails on Monday mornings.", "The room isn't available."], 1, "\"dealing with emails from the weekend\""),
        mc("What compromise does Kerim suggest?", ["Meeting every day", "Trying it for a month", "Cancelling the meeting"], 1, "\"How about trying it for a month?\""),
     ]},
    {"explanation": "**İkna edici konuşmanın adımları:**\n\n| Adım | Kalıplar |\n|---|---|\n| **1. Öneri** | *I'd like to suggest that we ...* / *What if we ...?* / *I think we should consider ...* |\n| **2. Fayda** | *This would mean that ...* / *The main advantage is ...* / *It would save / help / allow us to ...* |\n| **3. Koşul** | *If we ..., we would ...* (2nd conditional) |\n| **4. İtirazı kabul edip cevaplamak** | *That's true, but ...* / *I see your point, however ...* / *I understand your concern, but ...* |\n| **5. Güçlendirme** | *In fact, ...* / *It would not only save time but also ...* / *On top of that, ...* |\n| **6. Uzlaşma** | *How about ...?* / *Why don't we try ...?* / *Would you be willing to ...?* / *What if we met halfway?* |\n\n**suggest yapıları:**\n\n- *I suggest **that we move** the meeting.* (that + özne + fiilin yalın hali)\n- *I suggest **moving** the meeting.* (-ing)\n- ~~I suggest to move the meeting.~~ ✗\n\n**Retorik soru:** *Wouldn't it be better if ...?* / *Isn't it worth trying?*",
     "examples": [{"en": "I'd like to suggest that we start a recycling programme.", "tr": "Bir geri dönüşüm programı başlatmamızı önermek istiyorum."},
                  {"en": "I see your point, but it would actually save us money in the long run.", "tr": "Ne demek istediğinizi anlıyorum ama aslında uzun vadede bize para kazandırır."},
                  {"en": "Wouldn't it be better to try it first?", "tr": "Önce denemek daha iyi olmaz mı?"}],
     "turkishNote": "Türkçede \"önermek\" fiili \"-mesini önermek\" yapısıyla kullanılır ve doğrudan \"suggest to do\" diye çevrilmeye çalışılır. Bu yanlıştır: \"I suggest to go\" değil, \"I suggest going\" ya da \"I suggest that we go\" deyin. İkna ederken Türkçede yaygın olan \"Kesinlikle böyle yapmalıyız\" gibi kesin ifadeler İngilizcede ısrarcı algılanabilir; itirazı önce kabul etmek (That's true, but...) daha ikna edicidir."},
    [
        mc("Hangisi doğru?", ["I suggest to change the plan.", "I suggest changing the plan."], 1, "suggest + -ing."),
        mc("Hangisi doğru?", ["I suggest that we change the plan.", "I suggest us to change the plan."], 0, "suggest that + özne + V1."),
        mc("İtirazı kabul edip cevaplamak:", ["You're wrong.", "I see your point, but ..."], 1, "Diplomatik."),
        mc("Uzlaşma önerisi:", ["How about trying it for a week?", "We must do it now."], 0, "Uzlaşma."),
        gap("I'd like to ___ that we hire another designer. (önermek)", ["suggest"], "suggest that."),
        gap("If we changed suppliers, we ___ save 20%.", ["would", "could"], "2nd conditional."),
        gap("I understand your ___, but the benefits are clear. (endişe)", ["concern"], "I understand your concern."),
        gap("___ it be better to wait until next year? (olmaz mı)", ["Wouldn't"], "Retorik soru."),
        listen("I know some of you are worried about the cost of new laptops. That's a fair point. But our current laptops are seven years old, and they break down almost every week. If we replaced them, we'd save hours of lost work. And the IT company has offered us a 15% discount if we order before March.", "Konuşanın en önemli argümanı ne?", ["Yeni bilgisayarlar daha güzel", "Eski bilgisayarlar sürekli bozuluyor ve zaman kaybettiriyor", "Herkes istiyor"], 1, "\"they break down almost every week... we'd save hours of lost work\""),
        typ("İngilizcesi: \"Önce denemeyi öneriyorum.\" (suggest + -ing)", variants("I suggest trying it first.", "I suggest trying first."), "I suggest trying it first."),
    ],
    {"kind": "speaking", "task": speak("Okulunuzda, işyerinizde ya da mahallenizde değişmesini istediğiniz bir şeyi öneren 1–2 dakikalık ikna edici bir konuşma yapın. Öneriyi sunun, en az iki fayda söyleyin, bir itirazı önceden cevaplayın (That's true, but ...) ve sonunda bir uzlaşma önerin.",
                                       "I'd like to suggest that our office introduces flexible working hours. The main advantage is that people could avoid the rush-hour traffic, which would mean less stress and more energy. It would also help parents who need to pick up their children from school. Some people might say that it would be hard to organise meetings. That's true, but we could have core hours from ten to three, when everyone must be available. How about trying it for three months? If it doesn't work, we can always go back to the old system.",
                                       ["Öneri kalıpları ve suggest", "Fayda ve koşul cümleleri", "İtirazı cevaplama", "Uzlaşma önerisi"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Resmî rica e-postası", "Doğru yapı, açılış-kapanış ve kibar dil kullanarak iş hayatına uygun ikna edici bir rica e-postası yazabilirim.",
    {"kind": "text", "title": "Örnek e-posta: Sponsorluk ricası", "body": "Subject: Request for sponsorship – Children's Reading Festival\n\nDear Ms Aksoy,\n\nI am writing on behalf of the Kadıköy Parents' Association to ask whether your bookshop would consider sponsoring our first Children's Reading Festival, which will take place on 14 May.\n\nThe festival aims to encourage children aged 6 to 12 to read for pleasure. We are expecting around 500 families, and the programme will include storytelling sessions, workshops with local authors and a book swap.\n\nWe would be very grateful if you could provide 100 books as prizes. In return, your bookshop's logo would appear on all our posters and on our social media pages, which have more than 8,000 followers. We would also be happy to offer you a stand at the festival.\n\nI have attached a short description of the programme. If you require any further information, please do not hesitate to contact me.\n\nThank you for considering our request. I look forward to hearing from you.\n\nYours sincerely,\n\nTolga Yurt\nChair, Kadıköy Parents' Association",
     "questions": [
        mc("What does the association ask for?", ["Money", "100 books as prizes", "A venue"], 1, "\"provide 100 books as prizes\""),
        mc("What does the bookshop get in return?", ["Free tickets", "Its logo on posters and social media, and a stand", "A discount"], 1, "\"your bookshop's logo would appear... offer you a stand\""),
     ]},
    {"explanation": "**Resmî rica e-postasının yapısı:**\n\n| Bölüm | Kalıplar |\n|---|---|\n| **Konu (Subject)** | Kısa ve net: *Request for ... / Enquiry regarding ...* |\n| **Hitap** | *Dear Mr / Ms + soyadı,* (ismi biliyorsanız) / *Dear Sir or Madam,* (bilmiyorsanız) |\n| **Amaç** | *I am writing to request / ask whether / enquire about ...* / *I am writing on behalf of ...* |\n| **Arka plan** | Kim olduğunuzu ve durumu kısaca açıklayın. |\n| **Rica** | *I would be grateful if you could ...* / *I would appreciate it if you could ...* / *Would it be possible to ...?* |\n| **Karşılık / fayda** | *In return, ...* / *This would allow you to ...* |\n| **Ek ve iletişim** | *I have attached ... / Please find attached ...* / *If you require any further information, please do not hesitate to contact me.* |\n| **Kapanış cümlesi** | *Thank you for considering my request.* / *I look forward to hearing from you.* |\n| **Kapanış** | **Yours sincerely,** (ismi biliyorsanız) / **Yours faithfully,** (Dear Sir or Madam ile) / **Kind regards,** (yarı resmî) |\n\n**Dikkat:**\n\n- *I look forward to **hearing** from you.* (to + **-ing**; ~~to hear~~)\n- **Ms** evli/bekâr ayrımı yapmayan güvenli unvandır.\n- Paragraflar kısa olmalı; her paragrafta tek fikir.",
     "examples": [{"en": "I am writing to request an extension to the deadline.", "tr": "Son tarihin uzatılmasını talep etmek için yazıyorum."},
                  {"en": "Please find attached the documents you requested.", "tr": "Talep ettiğiniz belgeler ektedir."},
                  {"en": "I look forward to hearing from you at your earliest convenience.", "tr": "En kısa sürede sizden haber almayı bekliyorum."}],
     "turkishNote": "Türkçe resmî yazışmalarda \"Saygılarımla\" her duruma uyar; İngilizcede ise Yours sincerely (alıcının adını biliyorsanız) ve Yours faithfully (Dear Sir or Madam ile) ayrımı vardır. En sık hata \"I look forward to hear from you\" demektir: buradaki \"to\" bir edattır ve -ing alır. Ayrıca Türkçedeki \"Sayın Ahmet Bey\" yapısını \"Dear Mr Ahmet\" diye çevirmeyin: Mr / Ms soyadıyla kullanılır (Dear Mr Yılmaz)."},
    [
        mc("Alıcının adını bilmiyorsanız:", ["Dear Sir or Madam,", "Hi there,"], 0, "Resmî."),
        mc("\"Dear Ms Aksoy\" ile kapanış:", ["Yours faithfully,", "Yours sincerely,"], 1, "İsim biliniyor → sincerely."),
        mc("Hangisi doğru?", ["I look forward to hear from you.", "I look forward to hearing from you."], 1, "to + -ing."),
        mc("\"Sayın Ahmet Yılmaz\" İngilizce:", ["Dear Mr Ahmet,", "Dear Mr Yılmaz,"], 1, "Soyadı."),
        gap("I am writing on ___ of our company. (adına)", ["behalf"], "on behalf of."),
        gap("Please find ___ my CV. (ekte)", ["attached"], "Please find attached."),
        gap("Thank you for ___ (consider) my request.", ["considering"], "for + -ing."),
        gap("If you require any ___ information, please contact me. (ek)", ["further"], "further information."),
        listen("Hi, it's Meral from accounts. Just a quick note about your email to the client. It's very good, but you started with \"Dear Sir or Madam\" and finished with \"Yours sincerely\". Since you don't know their name, it should be \"Yours faithfully\". Otherwise, it's perfect.", "Meral hangi hatayı fark etti?", ["Konu satırı eksik", "Kapanış hitapla uyumlu değil", "Çok uzun"], 1, "\"it should be Yours faithfully\""),
        order(["I", "would", "be", "grateful", "if", "you", "could", "send", "me", "the", "details"], "I would be grateful if you could send me the details.", "would be grateful if + could.", "Bana ayrıntıları gönderirseniz minnettar olurum."),
    ],
    {"kind": "writing", "task": write("Aşağıdaki durumlardan birini seçin ve resmî bir rica e-postası yazın (150–200 kelime): (a) Çalıştığınız şirketin müdürüne, ekibiniz için bir İngilizce kursunun ücretini karşılamasını rica edin. (b) Belediyeye, mahallenizdeki parka çocuk oyun alanı yapılmasını rica edin. Konu satırı, uygun hitap, amaç, arka plan, kibar rica, fayda / gerekçe, iletişim cümlesi ve doğru kapanışı kullanın.",
                                      "Subject: Request for funding – English course for the sales team\n\nDear Mr Kaya,\n\nI am writing on behalf of the sales team to ask whether the company would be willing to cover the cost of a business English course for our six team members.\n\nAs you know, we have recently started working with several clients in Germany and the Netherlands, and all of our meetings and emails are now in English. Although most of the team can communicate, many of us feel that we are not as confident or professional as we would like to be.\n\nThe course we have found is run by a local language school. It consists of two evening classes a week for three months and costs 4,500 TL per person.\n\nWe believe this would benefit the company directly. Better communication would help us build stronger relationships with our clients and avoid costly misunderstandings. In return, we would be happy to attend the classes outside working hours.\n\nI have attached the course programme and the price list. If you require any further information, please do not hesitate to contact me.\n\nThank you for considering our request. I look forward to hearing from you.\n\nYours sincerely,\n\nElif Öztürk\nSales Executive",
                                      ["Konu satırı ve doğru hitap", "Açık amaç ve arka plan", "Kibar rica kalıpları", "Fayda ve gerekçe", "Doğru kapanış ve resmî üslup"])},
)

u.test([
    mc("En kibar olanı:", ["Can I leave early?", "I was wondering if I could leave early."], 1, "I was wondering if"),
    mc("Hangisi doğru?", ["Would you mind to close the door?", "Would you mind closing the door?"], 1, "mind + -ing"),
    mc("\"Would you mind waiting?\" Kabul etmek için:", ["Yes, I would.", "No, not at all."], 1, "Not at all"),
    mc("En diplomatik:", ["You made a mistake in the report.", "There seems to be a small mistake in the report."], 1, "Yumuşatma"),
    mc("Hangisi doğru?", ["I suggest to wait.", "I suggest waiting."], 1, "suggest + -ing"),
    gap("I am writing to ___ about your courses. (bilgi almak, resmî)", ["enquire", "inquire"], "enquire"),
    gap("I would be ___ if you could reply soon. (minnettar)", ["grateful"], "grateful"),
    gap("I look forward to ___ (hear) from you.", ["hearing"], "to + -ing"),
    gap("___, we are unable to accept your offer. (Maalesef)", ["Unfortunately"], "Unfortunately"),
    gap("Please find ___ the contract. (ekte)", ["attached"], "attached"),
    mc("\"Dear Sir or Madam\" ile kapanış:", ["Yours sincerely,", "Yours faithfully,"], 1, "faithfully"),
    mc("\"help\" resmî karşılığı:", ["assist", "insist"], 0, "assist"),
    listen("I understand your concern about the cost, and that's a fair point. But if we hired a second receptionist, customers wouldn't have to wait so long, and we'd probably get fewer complaints. How about trying it for the summer, when we're busiest?", "Konuşan nasıl bir uzlaşma öneriyor?", ["Hiç kimseyi işe almamak", "Yaz boyunca denemek", "Maaşları düşürmek"], 1, "\"How about trying it for the summer\""),
    typ("Resmîleştirin: \"I want to ask about the job.\" (wish, enquire, position)", variants("I wish to enquire about the position.", "I would like to enquire about the position.", "I wish to inquire about the position.", "I would like to inquire about the position."), "I wish to enquire about the position."),
    write("Bir otelde kaldınız ve sorunlar yaşadınız (oda temiz değildi, klima çalışmadı, söz verilen deniz manzarası yoktu). Otel müdürüne resmî bir e-posta yazın (150–200 kelime) ve kısmi bir ücret iadesi rica edin. Yumuşatma teknikleri, resmî kelimeler, kibar rica kalıpları ve doğru açılış-kapanış kullanın; tonunuz kızgın değil, kararlı ve kibar olsun.",
          "Subject: Request for a partial refund – Booking no. 48213\n\nDear Sir or Madam,\n\nI am writing regarding my recent stay at your hotel from 3 to 7 August.\n\nI had booked a double room with a sea view, as advertised on your website. Unfortunately, the room I was given overlooked the car park, and I was informed that no sea-view rooms were available.\n\nIn addition, I am afraid there were a number of other problems. The room did not seem to have been cleaned properly before our arrival, and the air conditioning stopped working on the second night. Although I reported this to reception, it was not repaired until the final day of our stay.\n\nI have stayed at your hotel twice before and have always been very satisfied, which is why I was particularly disappointed on this occasion.\n\nI would therefore be grateful if you could consider offering me a partial refund for the difference in price between a standard room and a sea-view room. I have attached a copy of my booking confirmation.\n\nThank you for your attention to this matter. I look forward to hearing from you at your earliest convenience.\n\nYours faithfully,\n\nGökhan Tekin",
          ["Doğru yapı ve açılış-kapanış", "Yumuşatma ve diplomatik ton", "Resmî kelime seçimi", "Açık ve kibar rica", "Kararlı ama kibar üslup"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

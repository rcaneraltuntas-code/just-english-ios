"""A2 Ünite 10: Davetler."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("A2", 10, "Davetler", "Invitations",
         "Birini kibarca davet edebilir, bir daveti uygun şekilde kabul ya da reddedebilir, öneride bulunabilir ve bir davette sohbet edebilirim.",
         ["Would you like (to) ...? ve Do you like ...? farkı", "I'd love to / I'm afraid I can't", "Let's / How about -ing / Why don't we / Shall we", "resmi ve samimi davetiyeler", "sosyal ortamda ikram ve teşekkür"],
         ["sosyal etkinlikler", "kutlamalar", "davet ve cevap ifadeleri"],
         {"title": "Parti planlayıcıları", "durationMinutes": 45,
          "goal": "Gruplar bir etkinlik planlar (doğum günü, mezuniyet, iş yemeği). Önce Let's / How about / Shall we ile karar verirler, sonra her öğrenci başka gruptan birini davet eder. Davet edilen kişi rol kartına göre kabul ya da kibarca reddeder. Son olarak etkinlik canlandırılır: karşılama, ikram ve vedalaşma."})

u.vocab([
    ("invite", "davet etmek", "They invited us to their wedding.", "Bizi düğünlerine davet ettiler.", "invite someone to something"),
    ("invitation", "davet, davetiye", "Thanks for the invitation!", "Davetin için teşekkürler!", None),
    ("would like", "istemek (kibar)", "Would you like to come?", "Gelmek ister misin?", "I'd like = I would like"),
    ("I'd love to", "Çok isterim", "Dinner on Friday? I'd love to!", "Cuma akşam yemeği mi? Çok isterim!", None),
    ("I'm afraid", "Korkarım, maalesef", "I'm afraid I can't come.", "Maalesef gelemiyorum.", "Kibar ret ifadesi."),
    ("accept", "kabul etmek", "I'm happy to accept your invitation.", "Davetinizi kabul etmekten mutluluk duyarım.", None),
    ("refuse / decline", "reddetmek", "It's hard to refuse an invitation.", "Bir daveti reddetmek zor.", "decline daha resmi."),
    ("celebrate", "kutlamak", "We're celebrating our anniversary.", "Yıldönümümüzü kutluyoruz.", None),
    ("anniversary", "yıldönümü", "It's our tenth wedding anniversary.", "Onuncu evlilik yıldönümümüz.", None),
    ("housewarming", "ev hayırlısı (partisi)", "We're having a housewarming party.", "Ev hayırlısı partisi veriyoruz.", None),
    ("graduation", "mezuniyet", "My graduation ceremony is in June.", "Mezuniyet törenim haziranda.", None),
    ("engagement", "nişan", "They had a big engagement party.", "Büyük bir nişan partisi verdiler.", None),
    ("guest", "misafir", "We have twenty guests.", "Yirmi misafirimiz var.", None),
    ("host", "ev sahibi", "The host made a lovely dinner.", "Ev sahibi harika bir yemek yaptı.", None),
    ("dress code", "kıyafet kuralı", "What's the dress code? – Smart casual.", "Kıyafet kuralı ne? – Şık günlük.", None),
    ("RSVP", "LCV (lütfen cevap veriniz)", "Please RSVP by 10 May.", "Lütfen 10 Mayıs'a kadar cevap verin.", "Fransızca répondez s'il vous plaît'den."),
    ("bring", "getirmek", "Shall I bring anything?", "Bir şey getireyim mi?", "bring → brought"),
    ("Help yourself!", "Buyurun, alın!", "There's food in the kitchen. Help yourself!", "Mutfakta yemek var. Buyurun!", None),
    ("make yourself at home", "kendi evin gibi rahat ol", "Come in and make yourself at home.", "Gel, kendi evin gibi rahat ol.", None),
    ("look forward to", "dört gözle beklemek", "I'm looking forward to the party!", "Partiyi dört gözle bekliyorum!", "look forward to + isim / -ing"),
    ("get together", "bir araya gelmek", "Let's get together next week.", "Gelecek hafta bir araya gelelim.", None),
    ("thank you for having me", "ağırladığınız için teşekkürler", "Thank you for having me. It was lovely.", "Beni ağırladığınız için teşekkürler. Çok güzeldi.", "Ayrılırken söylenir."),
    ("another time", "başka bir zaman", "Maybe another time?", "Belki başka bir zaman?", None),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Gelmek ister misin?", "Would you like (to) ...? ile kibarca davet edebilir ve I'd love to ile kabul edebilirim.",
    {"kind": "dialogue", "title": "Koridorda", "lines": [
        {"speaker": "Burcu", "text": "Hi, Tolga. Would you like to come to my birthday party on Saturday?"},
        {"speaker": "Tolga", "text": "I'd love to! Where is it?"},
        {"speaker": "Burcu", "text": "At my flat. We're having a barbecue on the balcony."},
        {"speaker": "Tolga", "text": "Great. Would you like me to bring anything?"},
        {"speaker": "Burcu", "text": "Maybe some drinks? And would you like to bring your sister too?"},
        {"speaker": "Tolga", "text": "That's very kind. I'll ask her. See you on Saturday!"}],
     "questions": [
        mc("What kind of party is it?", ["A dinner in a restaurant", "A barbecue at Burcu's flat", "A picnic"], 1, "\"We're having a barbecue on the balcony.\""),
        mc("What does Burcu ask Tolga to bring?", ["Food", "Drinks", "Music"], 1, "\"Maybe some drinks?\""),
     ]},
    {"explanation": "**Would you like to** + fiil? → kibar davet (… ister misin?)\n\n- **Would you like to** come to dinner?\n- **Would you like to** join us?\n\n**Would you like** + isim? → kibar teklif\n\n- **Would you like** a coffee?\n\n**Kabul etmek:** **I'd love to!** / Yes, please. / That sounds great! / Thanks, I'd like that.\n\n**Do you like ...? ile karıştırmayın:**\n\n| Would you like ...? | Do you like ...? |\n|---|---|\n| Şimdi / gelecekte ister misin? | Genelde sever misin? |\n| Would you like a tea? – Yes, please. | Do you like tea? – Yes, I do. |\n\n**Would you like me to** + fiil? → … yapmamı ister misin? (teklif)",
     "examples": [{"en": "Would you like to go to the cinema tonight?", "tr": "Bu akşam sinemaya gitmek ister misin?"},
                  {"en": "Would you like a piece of cake? – Yes, please!", "tr": "Bir dilim pasta ister misin? – Evet, lütfen!"},
                  {"en": "Would you like me to pick you up?", "tr": "Seni almamı ister misin?"}],
     "turkishNote": "\"Ister misin?\" sorusu İngilizcede \"Do you want...?\" ile de sorulabilir ama \"Would you like...?\" çok daha kibardır ve davetlerde, iş ortamında tercih edilir. \"I'd love to\" cevabında fiil tekrar edilmez: \"I'd love to come\" da olur ama sadece \"I'd love to!\" çok doğaldır."},
    [
        mc("Kibar davet:", ["Would you like to come to my party?", "Do you like to come to my party?", "You want come to my party?"], 0, "Would you like to + fiil?"),
        mc("\"Would you like a tea?\" cevabı:", ["Yes, I do.", "Yes, please.", "Yes, I like."], 1, "Teklif → Yes, please."),
        mc("\"Do you like tea?\" cevabı:", ["Yes, I do.", "Yes, please."], 0, "Genel tercih → Yes, I do."),
        gap("Would you like ___ join us for dinner?", ["to"], "would like to + fiil."),
        gap("Dinner on Friday? I'd ___ to!", ["love"], "I'd love to."),
        gap("Would you like ___ to bring anything? (benim getirmemi)", ["me"], "Would you like me to...?"),
        order(["you", "Would", "like", "to", "go", "to", "the", "cinema", "?"], "Would you like to go to the cinema?", "Would you like to + fiil?", "Sinemaya gitmek ister misin?"),
        listen("Would you like to come to our housewarming party next Friday? – That sounds great! What time?", "Davet edilen kişi ne diyor?", ["Kabul ediyor", "Reddediyor", "Emin değil"], 0, "\"That sounds great!\""),
        typ("İngilizce yazın: \"Seni almamı ister misin?\"", variants("Would you like me to pick you up?", "Do you want me to pick you up?"), "Would you like me to + pick you up?"),
        match([("Would you like a coffee?", "Yes, please."), ("Do you like coffee?", "Yes, I do."), ("Would you like to come?", "I'd love to!"), ("Would you like me to help?", "That's very kind.")], "Soruları cevaplarla eşleştirin."),
    ],
    {"kind": "speaking", "task": speak("JAI'yi 3 farklı etkinliğe davet edin (Would you like to...?). Sonra JAI'ye bir ikramda bulunun (Would you like a...?) ve bir yardım teklif edin (Would you like me to...?).",
                                       "Would you like to come to my graduation? Would you like to go for a walk on Sunday? Would you like to join our book club? Would you like a coffee? Would you like me to send you the address?",
                                       ["Would you like to + fiil", "Would you like + isim", "Would you like me to + fiil"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "Maalesef gelemiyorum", "Bir daveti kibarca reddedebilir, sebep gösterebilir ve başka bir zaman önerebilirim.",
    {"kind": "dialogue", "title": "Telefonda", "lines": [
        {"speaker": "Nur", "text": "Hi, Emre! We're having a dinner party on Friday. Would you like to come?"},
        {"speaker": "Emre", "text": "Oh, thanks for asking! I'd love to, but I'm afraid I can't. I'm working late on Friday."},
        {"speaker": "Nur", "text": "That's a shame. What about Saturday? We're going to a concert."},
        {"speaker": "Emre", "text": "Sorry, I'm visiting my parents this weekend."},
        {"speaker": "Nur", "text": "No problem. Maybe another time?"},
        {"speaker": "Emre", "text": "Definitely. Let's get together next week. I'll call you."}],
     "questions": [
        mc("Why can't Emre come on Friday?", ["He's visiting his parents.", "He's working late.", "He's ill."], 1, "\"I'm working late on Friday.\""),
        mc("What does Emre suggest?", ["Getting together next week", "Going to the concert", "Coming on Saturday"], 0, "\"Let's get together next week.\""),
     ]},
    {"explanation": "**Kibar bir ret üç adımdan oluşur:**\n\n1. **Teşekkür / olumlu tepki:** Thanks for asking! / That's very kind of you. / I'd love to, **but** ...\n2. **Özür + sebep:** **I'm afraid** I can't. I'm busy. / Sorry, I've got other plans. / I'm working that day.\n3. **Alternatif:** Maybe another time? / How about next week? / Can we do it on Sunday instead?\n\n**Davet eden kişinin cevabı:**\n\n- That's a shame. / What a pity! (Ne yazık.)\n- No problem. / Never mind. (Önemli değil.)\n\nSadece \"No\" ya da \"I don't want to\" demek İngilizcede **kaba** duyulur.\n\nSebepler için present continuous (ayarlanmış plan) çok kullanılır: I**'m meeting** a client. / We**'re going** away.",
     "examples": [{"en": "That's very kind of you, but I'm afraid I can't.", "tr": "Çok naziksiniz ama maalesef gelemiyorum."},
                  {"en": "I'd love to, but I've got other plans.", "tr": "Çok isterdim ama başka planlarım var."},
                  {"en": "What a pity! Maybe another time.", "tr": "Ne yazık! Belki başka zaman."}],
     "turkishNote": "\"I'm afraid\" burada \"korkuyorum\" anlamında değil, kibarca kötü bir haber vermek içindir: I'm afraid I can't = Maalesef yapamıyorum. Türkçede \"Kusura bakma\" ile başlamak gibidir. İngilizcede ret cümlesine bir teşekkür ve bir sebep eklemek çok önemlidir."},
    [
        mc("En kibar ret:", ["No, I can't.", "I'd love to, but I'm afraid I'm busy.", "I don't want to."], 1, "Olumlu + özür + sebep."),
        mc("\"I'm afraid I can't come.\" Anlamı:", ["Gelmekten korkuyorum.", "Maalesef gelemiyorum.", "Gelmem lazım."], 1, "I'm afraid = maalesef."),
        gap("I'd love to, ___ I'm working that day.", ["but"], "I'd love to, but..."),
        gap("Thanks for ___! (sorduğun için)", ["asking"], "Thanks for asking."),
        gap("That's a ___. Maybe another time? (Ne yazık.)", ["shame", "pity"], "That's a shame / pity."),
        gap("Sorry, I've got other ___. (planlar)", ["plans"], "other plans."),
        order(["very", "That's", "kind", "of", "you"], "That's very kind of you.", "That's very kind of you.", "Çok naziksin."),
        listen("Would you like to come to the cinema tonight? – Oh, I'm sorry, I can't. I'm meeting my cousin at the airport. How about tomorrow?", "Neden bu akşam gelemiyor?", ["Hasta", "Kuzenini havalimanından alacak", "Çalışıyor"], 1, "\"I'm meeting my cousin at the airport\""),
        typ("İngilizce yazın: \"Çok isterdim ama başka planlarım var.\"", variants("I'd love to, but I've got other plans.", "I'd love to, but I have other plans.", "I'd love to but I've got other plans.", "I'd love to but I have other plans."), "I'd love to, but + I've got other plans."),
        match([("Thanks for asking!", "olumlu tepki"), ("I'm afraid I can't.", "özür"), ("I'm working late.", "sebep"), ("Maybe another time?", "alternatif")], "Kibar retin adımlarını eşleştirin."),
    ],
    {"kind": "speaking", "task": speak("JAI sizi 3 farklı etkinliğe davet edecek. Birini kabul edin, ikisini kibarca reddedin (teşekkür + özür + sebep + alternatif).",
                                       "Oh, thanks for asking! I'd love to, but I'm afraid I can't. I'm visiting my grandmother on Saturday. How about next weekend? ... A concert? That sounds great! I'd love to come.",
                                       ["Kibar ret yapısı (3 adım)", "Sebep için present continuous", "Kabul ifadesi"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "Ne yapalım?", "Bir grup içinde öneride bulunabilir, önerilere tepki verip ortak karar alabilirim.",
    {"kind": "dialogue", "title": "Sürpriz parti", "lines": [
        {"speaker": "Ece", "text": "It's Selin's birthday next week. Let's organise a surprise party!"},
        {"speaker": "Can", "text": "Good idea! Why don't we have it at my place? It's big enough."},
        {"speaker": "Deniz", "text": "How about inviting her old school friends too?"},
        {"speaker": "Ece", "text": "Hmm, I'm not sure. I don't have their numbers."},
        {"speaker": "Can", "text": "What about asking her sister? She knows everyone."},
        {"speaker": "Ece", "text": "That's a great idea. Shall we meet tomorrow to plan the food?"},
        {"speaker": "Deniz", "text": "Sure. Let's meet at the café at six."}],
     "questions": [
        mc("Where will the party be?", ["At Ece's house", "At Can's place", "At a café"], 1, "\"Why don't we have it at my place?\""),
        mc("Who knows Selin's old school friends?", ["Ece", "Selin's sister", "Deniz"], 1, "\"What about asking her sister? She knows everyone.\""),
     ]},
    {"explanation": "**Öneri yapmak:**\n\n| Kalıp | Ardından | Örnek |\n|---|---|---|\n| Let's | yalın fiil | **Let's** order pizza. |\n| Why don't we | yalın fiil | **Why don't we** meet at six? |\n| Shall we | yalın fiil | **Shall we** go now? |\n| How about / What about | **-ing** / isim | **How about** inviting Ali? / **What about** Friday? |\n| We could | yalın fiil | **We could** have it outside. |\n\n**Olumlu tepki:** Good idea! / That's a great idea. / Sure. / Why not?\n\n**Kararsız / olumsuz tepki:** I'm not sure. / Hmm, maybe. / I'd rather not. / I don't think that's a good idea, because ...\n\n**Let's not** + fiil → olumsuz öneri: **Let's not** tell her!",
     "examples": [{"en": "Why don't we go to the new Italian restaurant?", "tr": "Neden yeni İtalyan restoranına gitmiyoruz?"},
                  {"en": "How about having a picnic?", "tr": "Pikniğe ne dersiniz?"},
                  {"en": "We could watch a film at home.", "tr": "Evde film izleyebiliriz."}],
     "turkishNote": "How about / What about sonrası fiil -ing alır: How about going (How about go değil). Diğer kalıplarda (Let's, Why don't we, Shall we, We could) yalın fiil gelir. Türkçedeki \"-elim\" (gidelim) çoğu zaman Let's ile, \"-elim mi?\" (gidelim mi?) Shall we ile söylenir."},
    [
        mc("Hangisi doğru?", ["How about go to the beach?", "How about going to the beach?"], 1, "How about + -ing."),
        mc("Hangisi doğru?", ["Why don't we to meet at six?", "Why don't we meet at six?"], 1, "Why don't we + yalın fiil."),
        mc("\"Gidelim mi?\"", ["Shall we go?", "Do we go?", "Let's we go?"], 0, "Shall we + fiil?"),
        gap("Let's ___ pizza tonight. (order)", ["order"], "Let's + yalın fiil."),
        gap("What about ___ Ali? (invite)", ["inviting"], "What about + -ing."),
        gap("We ___ have the party in the garden. (-ebiliriz)", ["could"], "We could + fiil."),
        gap("Let's ___ tell her. It's a surprise! (söylemeyelim)", ["not"], "Let's not."),
        order(["we", "Why", "don't", "have", "it", "at", "my", "place", "?"], "Why don't we have it at my place?", "Why don't we + fiil?", "Neden bizim evde yapmıyoruz?"),
        listen("Shall we go to the cinema? – Hmm, I'm not sure. The films this week aren't very good. How about going bowling?", "İkinci konuşan ne öneriyor?", ["Sinema", "Bowling", "Evde kalmak"], 1, "\"How about going bowling?\""),
        typ("İngilizce yazın: \"Pikniğe gitmeye ne dersin?\"", variants("How about going on a picnic?", "How about having a picnic?", "What about going on a picnic?", "What about having a picnic?"), "How about + going on a picnic?"),
    ],
    {"kind": "speaking", "task": speak("JAI ile bir arkadaşınız için veda partisi planlayın: yer, tarih, yemek, müzik ve hediye hakkında öneriler yapın (en az 4 farklı kalıp) ve JAI'nin önerilerine tepki verin.",
                                       "Let's have the party on Friday evening. Why don't we have it in the garden? How about ordering food from the Turkish restaurant? We could make a playlist of her favourite songs. Shall we buy her a nice bag? ... Hmm, I'm not sure. That's a great idea!",
                                       ["Farklı öneri kalıpları", "-ing / yalın fiil doğru", "Tepki ifadeleri"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Davetiye", "Resmi ve samimi bir davetiye yazıp yazılı bir davete cevap verebilirim.",
    {"kind": "text", "title": "İki davetiye", "body": "1)\nMr and Mrs Aydın request the pleasure of your company at the wedding of their daughter Elif to Mr Kerem Demir.\nSaturday 14 June, 7 pm\nGarden Hotel, Bebek, Istanbul\nDress code: formal\nPlease RSVP by 1 June.\n\n2)\nHi everyone!\nGuess what? I've finally got my own flat! 🏠 I'm having a housewarming party next Friday from 8 pm. Bring something to drink and your dancing shoes!\nLet me know if you can come.\nLove, Duygu",
     "questions": [
        mc("When should guests reply to the wedding invitation?", ["By 14 June", "By 1 June", "On Friday"], 1, "\"Please RSVP by 1 June.\""),
        mc("What should guests bring to Duygu's party?", ["Food", "Something to drink", "A present"], 1, "\"Bring something to drink\""),
     ]},
    {"explanation": "**Resmi ve samimi davet dili:**\n\n| Resmi | Samimi |\n|---|---|\n| We would like to invite you to ... | Would you like to come to ...? |\n| request the pleasure of your company | I'm having a party! |\n| Please RSVP by ... | Let me know if you can come. |\n| Dress code: formal | Wear something comfy! |\n\n**Kabul cevabı:**\n\n- Resmi: Thank you for your kind invitation. I would be delighted to attend.\n- Samimi: Thanks! I'd love to come. **I'm looking forward to** it!\n\n**Ret cevabı:**\n\n- Resmi: Thank you for your invitation. Unfortunately, I will not be able to attend because ...\n- Samimi: Thanks so much, but I'm afraid I can't make it. I'm ...\n\n**look forward to** + isim / -ing: I'm looking forward **to seeing** you. (to see değil)",
     "examples": [{"en": "We would like to invite you to our annual dinner.", "tr": "Sizi yıllık yemeğimize davet etmek isteriz."},
                  {"en": "Unfortunately, I won't be able to attend.", "tr": "Maalesef katılamayacağım."},
                  {"en": "I'm looking forward to seeing you!", "tr": "Seni görmeyi dört gözle bekliyorum!"}],
     "turkishNote": "\"look forward to\" kalıbındaki to bir edattır; bu yüzden ardından fiil -ing alır: looking forward to meeting you. \"can't make it\" = gelemeyeceğim (günlük dil). Resmi davetiyelerde \"Mr and Mrs\" kalıbı ve üçüncü tekil anlatım kullanılır."},
    [
        mc("Resmi kabul:", ["Cool, I'll come!", "I would be delighted to attend.", "Yes, OK."], 1, "Resmi → delighted to attend."),
        mc("Samimi ret:", ["Unfortunately, I will not be able to attend.", "Sorry, I can't make it. I'm away that weekend."], 1, "Samimi → can't make it."),
        mc("Hangisi doğru?", ["I'm looking forward to see you.", "I'm looking forward to seeing you."], 1, "look forward to + -ing."),
        gap("Please ___ by 10 May. (cevap verin)", ["RSVP", "reply"], "RSVP."),
        gap("Thank you for your kind ___.", ["invitation"], "invitation (isim)."),
        gap("I'm afraid I can't make ___. (gelemem)", ["it"], "make it."),
        gap("Let me ___ if you can come.", ["know"], "Let me know."),
        order(["would", "We", "like", "to", "invite", "you", "to", "our", "wedding"], "We would like to invite you to our wedding.", "Resmi davet kalıbı.", "Sizi düğünümüze davet etmek isteriz."),
        listen("Hi Duygu, thanks for the invitation! I'd love to come. Shall I bring some snacks? Can't wait!", "Konuşan ne teklif ediyor?", ["İçecek getirmek", "Atıştırmalık getirmek", "Müzik getirmek"], 1, "\"Shall I bring some snacks?\""),
        typ("İngilizce yazın: \"Maalesef katılamayacağım.\" (resmi)", variants("Unfortunately, I won't be able to attend.", "Unfortunately, I will not be able to attend.", "Unfortunately I won't be able to attend.", "Unfortunately I will not be able to attend."), "Unfortunately, + I won't be able to attend."),
    ],
    {"kind": "writing", "task": write("İki kısa mesaj yazın: (1) Duygu'nun ev partisine samimi bir kabul cevabı (bir şey getirmeyi teklif edin), (2) Elif ve Kerem'in düğününe resmi bir ret cevabı (sebep ve iyi dilekler).",
                                      "1) Hi Duygu! Congratulations on your new flat! Thanks for the invitation. I'd love to come. Shall I bring some cake? I'm looking forward to it!\n\n2) Dear Mr and Mrs Aydın,\nThank you very much for your kind invitation to Elif and Kerem's wedding. Unfortunately, I will not be able to attend because I will be abroad for work. I wish them a very happy life together.\nBest wishes,\nAhmet Kaya",
                                      ["Samimi dil doğru", "Resmi dil doğru", "look forward to + isim/-ing", "Teklif ve sebep"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Partide", "Bir davette misafir ya da ev sahibi olarak uygun ifadeleri kullanabilirim.",
    {"kind": "dialogue", "title": "Ev partisi", "lines": [
        {"speaker": "Duygu", "text": "Hi, Ahmet! Come in, come in. Make yourself at home."},
        {"speaker": "Ahmet", "text": "Thanks! This is for you. Congratulations on the new flat!"},
        {"speaker": "Duygu", "text": "Oh, flowers! That's so kind of you. Would you like something to drink?"},
        {"speaker": "Ahmet", "text": "I'd love a lemonade, please."},
        {"speaker": "Duygu", "text": "Here you are. The food is in the kitchen. Help yourself!"},
        {"speaker": "Ahmet", "text": "Thanks. Your flat is lovely. When did you move in?"},
        {"speaker": "Duygu", "text": "Just two weeks ago!"},
        {"speaker": "Ahmet", "text": "(Later) I'm afraid I have to go. Thank you for having me. It was a great party!"}],
     "questions": [
        mc("What did Ahmet bring?", ["A cake", "Flowers", "A bottle of lemonade"], 1, "\"Oh, flowers!\""),
        mc("What does Ahmet say when he leaves?", ["Make yourself at home.", "Thank you for having me.", "Help yourself!"], 1, "\"Thank you for having me.\""),
     ]},
    {"explanation": "**Ev sahibinin ifadeleri:**\n\n- Come in! / Welcome! / Make yourself at home.\n- Would you like something to drink / eat?\n- Help yourself! (Buyurun, kendiniz alın.)\n- Can I get you anything else?\n\n**Misafirin ifadeleri:**\n\n- This is for you. (Hediye verirken)\n- What a lovely flat! / The food is delicious!\n- Could I have some water, please?\n- I'm afraid I have to go. / I should get going.\n- **Thank you for having me.** / Thanks for a lovely evening.\n\n**Kutlama ifadeleri:**\n\n| Durum | İfade |\n|---|---|\n| doğum günü | Happy birthday! |\n| yeni ev, iş, mezuniyet, nişan | **Congratulations on** your new job! |\n| düğün | Congratulations! I wish you a happy life together. |\n| yeni yıl | Happy New Year! |",
     "examples": [{"en": "Congratulations on your graduation!", "tr": "Mezuniyetin kutlu olsun!"},
                  {"en": "Can I get you anything else?", "tr": "Başka bir şey getireyim mi?"},
                  {"en": "Thanks for a lovely evening.", "tr": "Güzel bir akşam için teşekkürler."}],
     "turkishNote": "Türkçedeki \"Hoş geldiniz\" için \"Welcome!\" ya da \"Come in!\", \"Ellerinize sağlık\" için \"The food was delicious, thank you!\" denebilir; birebir karşılığı yoktur. \"Congratulations\" her zaman -s ile biter ve ardından on gelir: Congratulations on your new baby."},
    [
        mc("Misafir gelince ev sahibi:", ["Make yourself at home.", "Thank you for having me.", "I have to go."], 0, "Karşılama."),
        mc("Misafir ayrılırken:", ["Help yourself!", "Thank you for having me.", "Come in!"], 1, "Teşekkür ederek ayrılma."),
        mc("Hangisi doğru?", ["Congratulation for your new job!", "Congratulations on your new job!"], 1, "Congratulations on."),
        gap("The food is in the kitchen. Help ___!", ["yourself"], "Help yourself."),
        gap("This is ___ you. (Hediye)", ["for"], "This is for you."),
        gap("I'm afraid I have ___ go.", ["to"], "have to go."),
        gap("Can I get you anything ___? (başka)", ["else"], "anything else."),
        order(["for", "Thanks", "a", "lovely", "evening"], "Thanks for a lovely evening.", "Thanks for + isim.", "Güzel bir akşam için teşekkürler."),
        listen("Welcome! Let me take your coat. Would you like some tea or coffee? – A coffee would be lovely, thanks.", "Misafir ne istiyor?", ["Çay", "Kahve", "Su"], 1, "\"A coffee would be lovely\""),
        match([("Happy", "birthday!"), ("Congratulations on", "your engagement!"), ("Make yourself", "at home."), ("Thank you for", "having me.")], "İfadeleri tamamlayın."),
    ],
    {"kind": "speaking", "task": speak("JAI ev sahibi, siz misafirsiniz. Partiye gelin (hediye verin ve tebrik edin), bir ikramı kabul edin, ev veya yemek hakkında iltifat edin, kısa bir sohbet edin ve teşekkür ederek ayrılın.",
                                       "Hi! This is for you. Congratulations on your new job! ... Yes, I'd love some juice, please. ... Your house is beautiful! The food is delicious. ... I'm afraid I have to go now. Thank you for having me. It was a lovely evening!",
                                       ["Tebrik ifadesi doğru", "Kabul ve iltifat", "Kibar ayrılış (Thank you for having me)"])},
)

u.test([
    mc("Kibar davet:", ["Would you like to come?", "Do you like to come?"], 0, "Would you like to"),
    mc("\"Would you like a coffee?\" cevabı:", ["Yes, I do.", "Yes, please."], 1, "Yes, please"),
    gap("Would you like ___ to help you? (benim)", ["me"], "Would you like me to"),
    mc("En kibar ret:", ["No.", "I'd love to, but I'm afraid I can't."], 1, "Kibar ret"),
    gap("I'm ___ I can't come. I'm busy. (maalesef)", ["afraid"], "I'm afraid"),
    gap("That's a ___! Maybe another time.", ["shame", "pity"], "That's a shame"),
    mc("Hangisi doğru?", ["How about watch a film?", "How about watching a film?"], 1, "How about + -ing"),
    gap("Why don't we ___ at seven? (meet)", ["meet"], "Why don't we + yalın fiil"),
    gap("___ we go? (gidelim mi)", ["Shall"], "Shall we"),
    mc("Hangisi doğru?", ["I'm looking forward to meet you.", "I'm looking forward to meeting you."], 1, "look forward to + -ing"),
    mc("Resmi ret:", ["Sorry, can't make it!", "Unfortunately, I will not be able to attend."], 1, "Resmi"),
    mc("Hangisi doğru?", ["Congratulations for your wedding!", "Congratulations on your wedding!"], 1, "on"),
    listen("I'd love to come to your party, but I'm afraid I'm working on Saturday night. Can we meet for lunch on Sunday instead?", "Konuşan ne öneriyor?", ["Cumartesi akşamı buluşmak", "Pazar öğle yemeği", "Partiye gelmek"], 1, "\"Can we meet for lunch on Sunday instead?\""),
    typ("İngilizce yazın: \"Beni ağırladığınız için teşekkürler.\"", variants("Thank you for having me.", "Thanks for having me.", "Thank you for having me!", "Thanks for having me!"), "Thank you for having me."),
    write("Arkadaşlarınızı bir etkinliğe davet eden samimi bir mesaj yazın (tarih, saat, yer, ne getirmeleri gerektiği). Sonra bir arkadaşınızın bu davete yazdığı kibar ret mesajını da yazın (60–80 kelime toplam).",
          "Hi everyone! I passed my driving test! 🚗 Let's celebrate! I'm having a picnic in Fenerbahçe Park on Sunday at 1 pm. Would you like to come? Please bring some food or drinks. Let me know if you can make it!\n\nReply: Congratulations! That's amazing news. I'd love to come, but I'm afraid I can't. I'm visiting my grandparents in Bursa this weekend. Why don't we have dinner next week to celebrate? Have fun!",
          ["Davet bilgileri tam", "Would you like / Let's doğru", "Kibar ret yapısı", "Tebrik ve alternatif öneri"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

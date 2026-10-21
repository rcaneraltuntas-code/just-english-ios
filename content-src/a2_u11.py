"""A2 Ünite 11: Yolculuk."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("A2", 11, "Yolculuk", "Travel",
         "Havalimanında, istasyonda ve otelde işlerimi halledebilir, bir sorunu kibarca bildirebilir ve bir yolculuğu ya da konaklamayı değerlendirebilirim.",
         ["ulaşım ve otel ifadeleri", "Could I ...? / Could you ...? (kibar rica)", "too + sıfat / (not) + sıfat + enough / enough + isim", "tarz zarfları: slowly, carefully, well, fast, hard"],
         ["havalimanı ve tren", "otel", "seyahat sorunları"],
         {"title": "Resepsiyon", "durationMinutes": 45,
          "goal": "Sınıf bir otele dönüşür. Resepsiyon görevlileri ve misafirler rol kartları alır. Misafirler oda ayırtır, giriş yapar ve kartlarındaki sorunu (oda çok gürültülü, yeterince havlu yok, Wi-Fi çok yavaş) kibarca bildirir; görevliler çözüm sunar. Sonunda misafirler otel için kısa bir değerlendirme yazar."})

u.vocab([
    ("check in", "giriş yapmak (otel, uçuş)", "We checked in at the airport two hours early.", "Havalimanında iki saat erken check-in yaptık.", "check out = çıkış yapmak"),
    ("boarding pass", "biniş kartı", "Can I see your boarding pass, please?", "Biniş kartınızı görebilir miyim?", None),
    ("gate", "kapı (havalimanı)", "The flight leaves from gate 12.", "Uçuş 12 numaralı kapıdan kalkıyor.", None),
    ("delayed", "rötarlı, gecikmeli", "Our flight is delayed by an hour.", "Uçuşumuz bir saat rötarlı.", None),
    ("cancelled", "iptal edilmiş", "The train was cancelled because of snow.", "Tren kar yüzünden iptal edildi.", None),
    ("luggage", "bagaj", "How much luggage do you have?", "Ne kadar bagajınız var?", "Sayılamaz: a luggage değil."),
    ("platform", "peron", "The train to Ankara leaves from platform 3.", "Ankara treni 3. perondan kalkıyor.", None),
    ("single / return", "tek yön / gidiş-dönüş", "A return ticket to Izmir, please.", "İzmir'e gidiş-dönüş bir bilet lütfen.", "Amerikan: one-way / round-trip."),
    ("reception", "resepsiyon", "Please leave your key at reception.", "Lütfen anahtarınızı resepsiyona bırakın.", None),
    ("reservation", "rezervasyon", "I have a reservation for two nights.", "İki gecelik rezervasyonum var.", None),
    ("single / double room", "tek / çift kişilik oda", "I'd like a double room, please.", "Çift kişilik bir oda istiyorum lütfen.", None),
    ("towel", "havlu", "Could I have some more towels, please?", "Biraz daha havlu alabilir miyim?", None),
    ("air conditioning", "klima", "The air conditioning doesn't work.", "Klima çalışmıyor.", None),
    ("view", "manzara", "Does the room have a sea view?", "Odanın deniz manzarası var mı?", None),
    ("noisy", "gürültülü", "The room is too noisy.", "Oda çok gürültülü.", None),
    ("too", "fazla, aşırı", "It's too hot in here.", "Burası fazla sıcak.", "too + sıfat"),
    ("enough", "yeterli, yeterince", "There aren't enough towels.", "Yeterince havlu yok.", "enough + isim / sıfat + enough"),
    ("slowly", "yavaşça", "Could you speak more slowly, please?", "Daha yavaş konuşabilir misiniz lütfen?", None),
    ("carefully", "dikkatlice", "Drive carefully. The road is icy.", "Dikkatli sür. Yol buzlu.", None),
    ("well", "iyi (zarf)", "The staff speak English well.", "Personel iyi İngilizce konuşuyor.", "good (sıfat) → well (zarf)"),
    ("hard", "çok, sıkı (zarf)", "The cleaners work very hard.", "Temizlikçiler çok çalışıyor.", "hardly farklı anlamdadır."),
    ("complain", "şikayet etmek", "I'd like to complain about my room.", "Odam hakkında şikayette bulunmak istiyorum.", None),
    ("review", "değerlendirme, yorum", "I wrote a review of the hotel.", "Otel hakkında bir yorum yazdım.", None),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Havalimanı ve istasyon", "Havalimanında ve istasyonda gerekli işleri halledebilir, duyuruları anlayabilirim.",
    {"kind": "dialogue", "title": "Check-in bankosu", "lines": [
        {"speaker": "Agent", "text": "Good morning. Where are you flying to today?"},
        {"speaker": "Sena", "text": "To London. Here's my passport."},
        {"speaker": "Agent", "text": "Thank you. How many bags are you checking in?"},
        {"speaker": "Sena", "text": "Just one. Could I have a window seat, please?"},
        {"speaker": "Agent", "text": "Of course. Here's your boarding pass. Your flight leaves from gate 14, but I'm afraid it's delayed by forty minutes."},
        {"speaker": "Sena", "text": "Oh, OK. What time does boarding start?"},
        {"speaker": "Agent", "text": "At ten fifteen. Have a good flight!"}],
     "questions": [
        mc("Where is Sena flying?", ["To Paris", "To London", "To Ankara"], 1, "\"To London.\""),
        mc("How long is the delay?", ["Fourteen minutes", "Forty minutes", "Four hours"], 1, "\"it's delayed by forty minutes\""),
     ]},
    {"explanation": "**Havalimanında:**\n\n| İfade | Anlam |\n|---|---|\n| check in (bags) | check-in yapmak, bagaj vermek |\n| go through security | güvenlik kontrolünden geçmek |\n| boarding pass | biniş kartı |\n| gate | kapı |\n| board / boarding | uçağa binmek / biniş |\n| delayed / cancelled | rötarlı / iptal |\n| window / aisle seat | cam kenarı / koridor koltuğu |\n\n**İstasyonda:**\n\n- A **single / return** ticket to Eskişehir, please.\n- What time is the **next** train to Ankara?\n- Which **platform** does it leave from?\n- Do I have to **change** trains? (aktarma)\n\n**Duyurular:** \"Flight JE 1985 to London is now boarding at gate 14.\" / \"The 10:30 train to Ankara is delayed.\"",
     "examples": [{"en": "Could I have an aisle seat, please?", "tr": "Koridor tarafında bir koltuk alabilir miyim lütfen?"},
                  {"en": "What time is the next train to Izmir?", "tr": "İzmir'e bir sonraki tren saat kaçta?"},
                  {"en": "Do I have to change trains?", "tr": "Aktarma yapmam gerekiyor mu?"}],
     "turkishNote": "\"Uçağa binmek\" = get on the plane ya da board. \"Uçaktan inmek\" = get off the plane. Rötar süresi \"by\" ile söylenir: delayed by an hour (bir saat rötarlı). \"luggage\" sayılamaz: How much luggage? / a piece of luggage."},
    [
        match([("boarding pass", "biniş kartı"), ("gate", "kapı"), ("delayed", "rötarlı"), ("aisle seat", "koridor koltuğu"), ("platform", "peron")], "Eşleştirin."),
        mc("İzmir'e gidip geri döneceksiniz:", ["A single ticket to Izmir, please.", "A return ticket to Izmir, please."], 1, "Gidiş-dönüş → return."),
        mc("Hangisi doğru?", ["How many luggages do you have?", "How much luggage do you have?"], 1, "luggage sayılamaz."),
        gap("Our flight is delayed ___ two hours.", ["by"], "delayed by."),
        gap("Which ___ does the train leave from? (peron)", ["platform"], "platform."),
        gap("Do I have to ___ trains? (aktarma)", ["change"], "change trains."),
        order(["time", "What", "is", "the", "next", "train", "to", "Ankara", "?"], "What time is the next train to Ankara?", "What time is the next train to + yer?", "Ankara'ya bir sonraki tren saat kaçta?"),
        listen("Attention please. Flight PC 2210 to Berlin is now boarding at gate 7. Passengers should go to the gate immediately.", "Berlin uçuşu hangi kapıdan?", ["Kapı 2", "Kapı 7", "Kapı 10"], 1, "\"boarding at gate 7\""),
        listen("We're sorry, but the 6:15 train to Eskişehir is cancelled today because of a technical problem.", "Tren neden iptal oldu?", ["Kar yüzünden", "Teknik bir sorun yüzünden", "Grev yüzünden"], 1, "\"because of a technical problem\""),
        typ("İngilizce yazın: \"Cam kenarı bir koltuk alabilir miyim lütfen?\"", variants("Could I have a window seat, please?", "Can I have a window seat, please?", "Could I have a window seat please?", "Can I have a window seat please?"), "Could I have + a window seat, please?"),
    ],
    {"kind": "speaking", "task": speak("JAI havalimanı görevlisi. Check-in yapın: nereye uçtuğunuzu söyleyin, bagaj verin, koltuk tercihi isteyin ve kapı numarası ile biniş saatini sorun.",
                                       "Good morning. I'm flying to Amsterdam. Here's my passport. I'm checking in one bag. Could I have an aisle seat, please? Which gate does it leave from? What time does boarding start?",
                                       ["Havalimanı kelimeleri", "Could I have...? doğru", "Kapı ve saat sorusu"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "Otelde", "Otelde oda ayırtabilir, giriş yapabilir ve kibarca rica edebilirim.",
    {"kind": "dialogue", "title": "Resepsiyonda", "lines": [
        {"speaker": "Receptionist", "text": "Good evening. Welcome to the Sea Breeze Hotel. How can I help you?"},
        {"speaker": "Mr Kurt", "text": "Hello. I have a reservation for three nights. My name's Kurt."},
        {"speaker": "Receptionist", "text": "Ah yes, Mr Kurt. A double room with a sea view. Could you fill in this form, please?"},
        {"speaker": "Mr Kurt", "text": "Sure. Could I ask what time breakfast is?"},
        {"speaker": "Receptionist", "text": "From seven to ten in the garden restaurant. Your room is 305, on the third floor. The lift is on your left."},
        {"speaker": "Mr Kurt", "text": "Thank you. And could you wake me up at six tomorrow?"},
        {"speaker": "Receptionist", "text": "Of course. Enjoy your stay!"}],
     "questions": [
        mc("How many nights is Mr Kurt staying?", ["Two", "Three", "Five"], 1, "\"a reservation for three nights\""),
        mc("Where is breakfast?", ["In the room", "In the garden restaurant", "On the third floor"], 1, "\"in the garden restaurant\""),
     ]},
    {"explanation": "**Could** ile rica etmek, **can**'den daha kibardır.\n\n| Kalıp | Kullanım | Örnek |\n|---|---|---|\n| **Could I** + fiil? | izin / bir şey istemek | **Could I** have a map? / **Could I** pay by card? |\n| **Could you** + fiil? | birinden bir şey yapmasını istemek | **Could you** call a taxi? |\n| **Could you tell me** + soru? | bilgi istemek | **Could you tell me** where the lift is? |\n\n**Cevaplar:** Of course. / Certainly. / Sure. / I'm afraid not.\n\n**Otel ifadeleri:**\n\n- I have a reservation **for** two nights.\n- I'd like a single / double room **with** a sea view.\n- Is breakfast **included**? (Kahvaltı dahil mi?)\n- What time is **check-out**?\n\n**Dikkat:** Could you tell me **where the lift is**? (where is the lift değil; soru yapısı düz cümleye döner)",
     "examples": [{"en": "Could I have a late check-out, please?", "tr": "Geç çıkış yapabilir miyim lütfen?"},
                  {"en": "Could you recommend a good restaurant?", "tr": "İyi bir restoran önerebilir misiniz?"},
                  {"en": "Could you tell me what time the pool opens?", "tr": "Havuzun saat kaçta açıldığını söyleyebilir misiniz?"}],
     "turkishNote": "\"Could\" burada geçmiş zaman değil, kibarlık bildirir: \"Could you help me?\" = Bana yardım edebilir misiniz? Türkçedeki \"-ebilir misiniz\" kibar sorusunun tam karşılığıdır. Otelde \"Is breakfast included?\" sorusu çok işe yarar."},
    [
        mc("En kibar rica:", ["Give me a map.", "Could I have a map, please?", "I want a map."], 1, "Could I have...?"),
        mc("Birinden taksi çağırmasını istemek:", ["Could I call a taxi?", "Could you call a taxi for me, please?"], 1, "Could you + fiil?"),
        mc("Hangisi doğru?", ["Could you tell me where is the lift?", "Could you tell me where the lift is?"], 1, "Dolaylı soru → düz cümle düzeni."),
        gap("I have a reservation ___ two nights.", ["for"], "a reservation for."),
        gap("Is breakfast ___? (dahil)", ["included"], "included."),
        gap("I'd like a double room ___ a sea view.", ["with"], "with a view."),
        order(["you", "Could", "recommend", "a", "good", "restaurant", "?"], "Could you recommend a good restaurant?", "Could you + fiil + nesne?", "İyi bir restoran önerebilir misiniz?"),
        listen("Check-out is at twelve, but you could leave your bags at reception until five if you like.", "Bagajlar resepsiyonda saat kaça kadar kalabilir?", ["12'ye", "5'e", "Kalamaz"], 1, "\"until five\""),
        typ("İngilizce yazın: \"Kahvaltı dahil mi?\"", variants("Is breakfast included?", "Is the breakfast included?"), "Is breakfast included?"),
        typ("İngilizce yazın: \"Geç çıkış yapabilir miyim lütfen?\"", variants("Could I have a late check-out, please?", "Could I have a late checkout, please?", "Can I have a late check-out, please?", "Could I check out late, please?", "Could I have a late check-out please?"), "Could I have + a late check-out, please?"),
    ],
    {"kind": "speaking", "task": speak("JAI resepsiyon görevlisi. Telefonla bir oda ayırtın (tarih, kaç gece, oda türü), kahvaltının dahil olup olmadığını sorun ve iki kibar ricada bulunun (Could I / Could you).",
                                       "Hello, I'd like to book a double room for two nights, from the 5th to the 7th of July. Is breakfast included? Could I have a room with a sea view? Could you tell me how far the hotel is from the airport?",
                                       ["Rezervasyon ifadeleri", "Could I / Could you doğru", "Could you tell me + düz cümle"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "Fazla mı, yeterli mi?", "too ve enough ile bir şeyin neden uygun olmadığını açıklayabilirim.",
    {"kind": "dialogue", "title": "Oda sorunu", "lines": [
        {"speaker": "Guest", "text": "Excuse me. I'm afraid there's a problem with my room."},
        {"speaker": "Receptionist", "text": "I'm sorry to hear that. What's the matter?"},
        {"speaker": "Guest", "text": "Well, it's too noisy. It's next to the lift. And it isn't big enough for three people."},
        {"speaker": "Receptionist", "text": "I see. Anything else?"},
        {"speaker": "Guest", "text": "Yes, there aren't enough towels, and the air conditioning is too loud."},
        {"speaker": "Receptionist", "text": "I'm very sorry. We have a bigger, quieter room on the fifth floor. Would you like to move?"},
        {"speaker": "Guest", "text": "Yes, please. Thank you."}],
     "questions": [
        mc("Why is the room noisy?", ["It's next to the street.", "It's next to the lift.", "The TV is loud."], 1, "\"It's next to the lift.\""),
        mc("What does the receptionist offer?", ["Free breakfast", "A different room", "More towels only"], 1, "\"We have a bigger, quieter room... Would you like to move?\""),
     ]},
    {"explanation": "**too + sıfat** → gereğinden fazla (sorun var)\n\n- It's **too** noisy. (Fazla gürültülü.)\n- This bag is **too** heavy **to** carry. (Taşınamayacak kadar ağır.)\n\n**(not) + sıfat + enough** → yeterince (değil)\n\n- The room **isn't big enough**. (Yeterince büyük değil.)\n- Are you **old enough** to drive?\n\n**enough + isim** → yeterli miktarda\n\n- There **aren't enough towels**.\n- We don't have **enough time**.\n\n| | Konum |\n|---|---|\n| too | sıfattan **önce** |\n| enough (sıfatla) | sıfattan **sonra** |\n| enough (isimle) | isimden **önce** |\n\n**too ve very:** very hot (çok sıcak, ama sorun olmayabilir) / too hot (fazla sıcak, rahatsız edici)",
     "examples": [{"en": "The coffee is too hot to drink.", "tr": "Kahve içilemeyecek kadar sıcak."},
                  {"en": "The bed isn't long enough for me.", "tr": "Yatak benim için yeterince uzun değil."},
                  {"en": "We didn't have enough money for a taxi.", "tr": "Taksi için yeterli paramız yoktu."}],
     "turkishNote": "Türkçede \"çok\" kelimesi hem very hem too anlamında kullanılır; İngilizcede seçim önemlidir: \"This hotel is very expensive\" (çok pahalı, belki yine kalırız) ≠ \"This hotel is too expensive\" (fazla pahalı, kalamayız). enough'un yeri de Türkçeden farklıdır: \"yeterince büyük\" = big enough (enough big değil)."},
    [
        mc("Oda 40°C, kimse uyuyamıyor:", ["It's very hot.", "It's too hot."], 1, "Sorun var → too."),
        mc("Hangisi doğru?", ["The room isn't enough big.", "The room isn't big enough."], 1, "sıfat + enough."),
        mc("Hangisi doğru?", ["We don't have time enough.", "We don't have enough time."], 1, "enough + isim."),
        gap("This suitcase is ___ heavy. I can't lift it.", ["too"], "too + sıfat."),
        gap("He isn't old ___ to drive. He's only 15.", ["enough"], "old enough."),
        gap("There aren't ___ chairs for everyone.", ["enough"], "enough + isim."),
        gap("The tea is too hot ___ drink.", ["to"], "too ... to + fiil."),
        order(["isn't", "The", "bed", "long", "enough", "for", "me"], "The bed isn't long enough for me.", "isn't + sıfat + enough + for.", "Yatak benim için yeterince uzun değil."),
        listen("We couldn't stay at that hotel. It was too far from the centre and the rooms weren't clean enough.", "Otelin sorunu neydi?", ["Çok pahalı ve küçük", "Merkeze çok uzak ve odalar yeterince temiz değil", "Çok gürültülü"], 1, "\"too far... weren't clean enough\""),
        typ("İngilizce yazın: \"Yeterince havlu yok.\"", variants("There aren't enough towels.", "There are not enough towels."), "There aren't + enough towels."),
    ],
    {"kind": "speaking", "task": speak("JAI resepsiyon görevlisi. Odanızla ilgili 4 sorunu kibarca bildirin: 2 tanesinde too, 1 tanesinde (not) ... enough, 1 tanesinde enough + isim kullanın. JAI'nin çözümünü kabul edin.",
                                       "Excuse me, I'm afraid there's a problem with my room. It's too cold and the Wi-Fi is too slow. The bed isn't comfortable enough, and there aren't enough pillows. ... Yes, that's great. Thank you.",
                                       ["too + sıfat", "sıfat + enough", "enough + isim", "Kibar şikayet dili"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Nasıl yaptı?", "Tarz zarfları ile bir eylemin nasıl yapıldığını anlatabilirim.",
    {"kind": "text", "title": "Tur rehberi değerlendirmesi", "body": "Our guide, Mustafa, was fantastic!\n\nHe spoke English and German perfectly, and he explained everything clearly. He drove the minibus carefully on the mountain roads, so we felt safe.\n\nHe worked really hard. He answered all our questions patiently, even the silly ones! On the last day it rained heavily, but he quickly found a lovely café for us.\n\nThe only problem: he walked very fast! We had to run to keep up. 😄\n\n★★★★★",
     "questions": [
        mc("How did Mustafa drive?", ["Fast", "Carefully", "Badly"], 1, "\"He drove the minibus carefully\""),
        mc("What was the only problem?", ["He spoke badly.", "He walked very fast.", "He was late."], 1, "\"he walked very fast!\""),
     ]},
    {"explanation": "**Tarz zarfları** bir eylemin **nasıl** yapıldığını anlatır. Genellikle **fiilden ya da nesneden sonra** gelir.\n\n**Yapılış:** sıfat + **-ly**\n\n| Sıfat | Zarf |\n|---|---|\n| slow | slow**ly** |\n| careful | careful**ly** |\n| quiet | quiet**ly** |\n| easy | eas**ily** (y → ily) |\n| heavy | heav**ily** |\n\n**Düzensiz zarflar:**\n\n| Sıfat | Zarf |\n|---|---|\n| good | **well** |\n| fast | **fast** |\n| hard | **hard** |\n| early / late | **early / late** |\n\n**Sıfat mı, zarf mı?**\n\n- He's a **careful** driver. (sıfat → isimden önce)\n- He drives **carefully**. (zarf → fiilden sonra)\n\n**Dikkat:** ~~hardly~~ \"çok çalışmak\" değil, \"neredeyse hiç\" demektir.",
     "examples": [{"en": "Could you speak more slowly, please?", "tr": "Daha yavaş konuşabilir misiniz lütfen?"},
                  {"en": "She speaks English very well.", "tr": "Çok iyi İngilizce konuşuyor."},
                  {"en": "We arrived late because the bus drove slowly.", "tr": "Otobüs yavaş gittiği için geç vardık."}],
     "turkishNote": "Türkçede sıfat ve zarf çoğu zaman aynı kelimedir: \"iyi bir sürücü\" / \"iyi sürer\". İngilizcede fark zorunludur: a good driver / drives well. \"He speaks English good\" çok yaygın bir hatadır; doğrusu \"He speaks English well.\""},
    [
        mc("Hangisi doğru?", ["She speaks English good.", "She speaks English well."], 1, "Fiili niteleyen → well."),
        mc("Hangisi doğru?", ["He's a careful driver.", "He's a carefully driver."], 0, "İsimden önce → sıfat."),
        mc("Hangisi doğru?", ["He drives careful.", "He drives carefully."], 1, "Fiilden sonra → zarf."),
        gap("Could you speak more ___, please? (slow)", ["slowly"], "slow → slowly."),
        gap("It rained ___ all night. (heavy)", ["heavily"], "heavy → heavily."),
        gap("The cleaners work very ___. (hard)", ["hard"], "hard → hard."),
        gap("She passed the exam ___. (easy)", ["easily"], "easy → easily."),
        mc("\"He hardly works.\" Anlamı:", ["Çok çalışır.", "Neredeyse hiç çalışmaz."], 1, "hardly = neredeyse hiç."),
        listen("The receptionist was lovely. She spoke to us politely and explained the city map very clearly.", "Görevli haritayı nasıl açıkladı?", ["Hızlıca", "Çok açık bir şekilde", "Kaba bir şekilde"], 1, "\"very clearly\""),
        typ("İngilizce yazın: \"Çok iyi İngilizce konuşuyor.\" (he)", variants("He speaks English very well.", "He speaks very good English."), "He speaks English + very well."),
    ],
    {"kind": "speaking", "task": speak("Yakın zamanda yaptığınız bir yolculuktaki 3 kişiyi (sürücü, rehber, garson, pilot...) tarz zarflarıyla anlatın. En az 5 farklı zarf kullanın.",
                                       "Our taxi driver drove very fast, but he drove safely. The waiter at the hotel spoke English well and served us quickly. Our guide explained the history clearly and answered our questions patiently.",
                                       ["-ly zarfları doğru", "well / fast / hard doğru", "Zarf fiilden sonra"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Değerlendirme yazmak", "Bir otel ya da yolculuk için dengeli bir değerlendirme yazabilir ve şikayetimi kibarca iletebilirim.",
    {"kind": "text", "title": "Otel yorumları", "body": "★★★★☆ \"Great location, small rooms\" – Melis, Ankara\nThe hotel is in the perfect place, five minutes from the beach. The staff were friendly and worked hard. Breakfast was delicious. However, our room was too small for a family of four, and the walls weren't thick enough. We heard everything!\n\n★★☆☆☆ \"Disappointing\" – Robert, Manchester\nThe photos online look amazing, but the reality is different. The pool was too crowded, and there weren't enough sunbeds. The Wi-Fi worked very slowly. I complained at reception, and they answered politely, but nothing changed.",
     "questions": [
        mc("What was good about the hotel for Melis?", ["The room size", "The location and breakfast", "The walls"], 1, "\"in the perfect place... Breakfast was delicious.\""),
        mc("What was Robert's problem at the pool?", ["It was too cold.", "It was too crowded.", "It was closed."], 1, "\"The pool was too crowded\""),
     ]},
    {"explanation": "**İyi bir değerlendirmenin yapısı:**\n\n1. **Başlık ve puan:** \"Great location, small rooms\" ★★★★☆\n2. **Olumlu yanlar:** The staff were friendly. Breakfast was delicious.\n3. **Olumsuz yanlar:** **However**, the room was too small.\n4. **Sonuç / tavsiye:** I would recommend it for couples, but not for families.\n\n**Bağlaçlar:**\n\n- **but** (cümle içinde): The room was nice, **but** it was small.\n- **However,** (yeni cümle başında, virgülle): The room was nice. **However,** it was small.\n- **also / too**: The staff were **also** helpful. / The food was great **too**.\n\n**Kibar şikayet:**\n\n- I'm afraid there's a problem with ...\n- I'd like to complain about ...\n- Could you possibly ...?\n- I'm not happy with ...",
     "examples": [{"en": "The room was clean. However, it was too noisy.", "tr": "Oda temizdi. Ancak fazla gürültülüydü."},
                  {"en": "I would recommend this hotel to families.", "tr": "Bu oteli ailelere tavsiye ederim."},
                  {"en": "I'd like to complain about the Wi-Fi.", "tr": "Wi-Fi hakkında şikayette bulunmak istiyorum."}],
     "turkishNote": "\"However\" resmi yazıda \"but\"tan daha uygundur ve genellikle yeni cümlenin başına gelip ardından virgül alır. \"recommend\" kalıbı: recommend something to someone (birine bir şeyi tavsiye etmek). İngilizcede \"staff\" çoğul fiil alabilir: The staff were friendly."},
    [
        mc("Resmi yazıda yeni cümle başında:", ["But the room was small.", "However, the room was small."], 1, "However, + cümle."),
        mc("Kibar şikayet:", ["Your Wi-Fi is terrible!", "I'm afraid there's a problem with the Wi-Fi."], 1, "I'm afraid there's a problem with..."),
        gap("The food was great. ___, the service was slow.", ["However"], "However,"),
        gap("I would ___ this hotel to couples. (tavsiye etmek)", ["recommend"], "recommend."),
        gap("I'd like to complain ___ the noise.", ["about"], "complain about."),
        gap("The staff were friendly. The rooms were ___ clean. (de, ayrıca)", ["also"], "also."),
        order(["was", "The", "location", "perfect", "but", "the", "room", "was", "too", "small"], "The location was perfect but the room was too small.", "Olumlu + but + olumsuz.", "Konum mükemmeldi ama oda fazla küçüktü."),
        listen("Overall, I enjoyed my stay. The beds were comfortable enough and the staff worked hard. However, the restaurant was too expensive, so we ate outside.", "Neden dışarıda yemek yediler?", ["Restoran kapalıydı", "Restoran fazla pahalıydı", "Yemekler kötüydü"], 1, "\"the restaurant was too expensive\""),
        typ("İngilizce yazın: \"Bu oteli ailelere tavsiye ederim.\"", variants("I would recommend this hotel to families.", "I'd recommend this hotel to families.", "I recommend this hotel to families.", "I would recommend this hotel for families.", "I'd recommend this hotel for families."), "I would recommend + this hotel + to families."),
        match([("Title", "\"Great location, small rooms\""), ("Positive", "The staff were friendly."), ("Negative", "However, the room was too small."), ("Conclusion", "I would recommend it to couples.")], "Değerlendirme bölümlerini eşleştirin."),
    ],
    {"kind": "writing", "task": write("Kaldığınız (ya da hayal ettiğiniz) bir otel için bir değerlendirme yazın (80–100 kelime): başlık, puan, olumlu yanlar, However ile olumsuz yanlar, too/enough, en az 2 tarz zarfı ve bir tavsiye.",
                                      "★★★★☆ \"Lovely staff, slow Wi-Fi\"\nWe stayed at the Blue Bay Hotel in Fethiye for five nights. The location was great and the rooms were very clean. The staff spoke English well and helped us quickly when we had a problem. Breakfast was delicious too. However, the Wi-Fi was too slow, and there weren't enough sunbeds by the pool in the afternoon. I would definitely recommend this hotel to couples and families.",
                                      ["Yapı (başlık, olumlu, olumsuz, tavsiye)", "too / enough doğru", "Tarz zarfları doğru", "However doğru kullanıldı"])},
)

u.test([
    mc("Gidip döneceksiniz:", ["A single ticket", "A return ticket"], 1, "return"),
    mc("Hangisi doğru?", ["How many luggages?", "How much luggage?"], 1, "luggage sayılamaz"),
    gap("The flight is delayed ___ an hour.", ["by"], "delayed by"),
    mc("En kibar rica:", ["Give me the key.", "Could I have the key, please?"], 1, "Could I"),
    mc("Hangisi doğru?", ["Could you tell me where is the station?", "Could you tell me where the station is?"], 1, "Dolaylı soru"),
    gap("Is breakfast ___? (dahil)", ["included"], "included"),
    mc("Oda kalmak için fazla pahalı:", ["It's very expensive.", "It's too expensive."], 1, "too"),
    mc("Hangisi doğru?", ["The room isn't enough big.", "The room isn't big enough."], 1, "sıfat + enough"),
    gap("There isn't ___ time to see everything.", ["enough"], "enough + isim"),
    mc("Hangisi doğru?", ["He speaks English good.", "He speaks English well."], 1, "well"),
    gap("Please drive ___. The road is icy. (careful)", ["carefully"], "carefully"),
    gap("The room was nice. ___, it was too noisy.", ["However"], "However,"),
    listen("Could I have a room on a higher floor, please? This one is too noisy because it's next to the street.", "Misafir neden oda değiştirmek istiyor?", ["Oda fazla küçük", "Oda sokağa yakın, fazla gürültülü", "Manzara yok"], 1, "\"too noisy because it's next to the street\""),
    typ("İngilizce yazın: \"Daha yavaş konuşabilir misiniz lütfen?\"", variants("Could you speak more slowly, please?", "Could you speak more slowly please?", "Can you speak more slowly, please?", "Could you speak slower, please?"), "Could you speak + more slowly, please?"),
    write("Bir otele kibar bir şikayet e-postası yazın (70–90 kelime): kaldığınız tarihi, 3 sorunu (too / enough kullanarak), personelin nasıl davrandığını (tarz zarfı) ve ne istediğinizi yazın.",
          "Dear Manager,\nI stayed at your hotel from 3 to 6 August in room 214. I'm afraid I had some problems. The room was too hot because the air conditioning didn't work, and it wasn't big enough for two people. Also, there weren't enough towels. The receptionist spoke to me politely, but nobody fixed the problems. Could you possibly give me a partial refund?\nYours faithfully,\nCan Öztürk",
          ["Kibar ve resmi dil", "too / enough doğru", "Tarz zarfı doğru", "Net bir talep"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

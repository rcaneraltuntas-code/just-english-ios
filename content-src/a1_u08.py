"""A1 Ünite 8: Şehirde."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("A1", 8, "Şehirde", "In Town",
         "Şehirde bir yerin nerede olduğunu sorabilir, yol tarif edebilir ve ulaşımla ilgili basit ricalarda bulunabilirim.",
         ["emir cümleleri (olumlu ve olumsuz)", "yol tarifi ifadeleri", "can (rica ve izin)", "ulaşım: by bus, on foot"],
         ["şehirdeki yerler", "yön ifadeleri", "ulaşım"],
         {"title": "Kayıp turist", "durationMinutes": 45,
          "goal": "Öğrencilere aynı şehir haritası verilir; biri turist olur ve bir yere nasıl gideceğini sorar, diğeri tarif eder. Turist doğru yere vardı mı, haritada kontrol edilir."})

u.vocab([
    ("bank", "banka", "Is there a bank near here?", "Buralarda banka var mı?", None),
    ("pharmacy", "eczane", "The pharmacy is on the corner.", "Eczane köşede.", "İngiliz İngilizcesinde chemist's da denir."),
    ("post office", "postane", "The post office opens at nine.", "Postane dokuzda açılır.", None),
    ("supermarket", "süpermarket", "I go to the supermarket on Saturdays.", "Cumartesileri süpermarkete giderim.", None),
    ("museum", "müze", "The museum is closed on Mondays.", "Müze pazartesileri kapalı.", None),
    ("station", "istasyon", "Where's the train station?", "Tren istasyonu nerede?", None),
    ("bus stop", "otobüs durağı", "The bus stop is opposite the bank.", "Otobüs durağı bankanın karşısında.", None),
    ("square", "meydan", "The café is in the main square.", "Kafe ana meydanda.", None),
    ("street", "sokak, cadde", "Go along this street.", "Bu cadde boyunca gidin.", None),
    ("corner", "köşe", "It's on the corner.", "Köşede.", "on the corner (köşede)"),
    ("traffic lights", "trafik ışıkları", "Turn right at the traffic lights.", "Işıklardan sağa dönün.", "Her zaman çoğul."),
    ("turn left / right", "sola / sağa dönmek", "Turn left at the bank.", "Bankadan sola dönün.", None),
    ("go straight on", "düz gitmek", "Go straight on for 200 metres.", "200 metre düz gidin.", "Amerikan: go straight ahead."),
    ("cross", "karşıya geçmek", "Cross the road at the lights.", "Yolun karşısına ışıklardan geçin.", None),
    ("first / second / third", "birinci / ikinci / üçüncü", "Take the second street on the left.", "Soldaki ikinci sokağa girin.", None),
    ("near", "yakın, yakınında", "Is it near here?", "Buraya yakın mı?", None),
    ("far", "uzak", "It isn't far.", "Uzak değil.", None),
    ("map", "harita", "Can you show me on the map?", "Bana haritada gösterebilir misiniz?", None),
    ("by bus / by train / by car", "otobüsle / trenle / arabayla", "I go to work by bus.", "İşe otobüsle giderim.", "by + araç (the yok)."),
    ("on foot", "yürüyerek", "It's ten minutes on foot.", "Yürüyerek on dakika.", "by foot değil, on foot."),
    ("get off", "(araçtan) inmek", "Get off at the third stop.", "Üçüncü durakta inin.", "Binmek: get on."),
    ("ticket", "bilet", "Two tickets to Ankara, please.", "Ankara'ya iki bilet lütfen.", None),
    ("Excuse me", "Affedersiniz", "Excuse me, where's the museum?", "Affedersiniz, müze nerede?", "Birine bir şey sormadan önce söylenir."),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Şehirdeki yerler", "Şehirdeki yerlerin adını söyleyip nerede olduklarını sorabilirim.",
    {"kind": "dialogue", "title": "Turizm ofisi", "lines": [
        {"speaker": "Tourist", "text": "Excuse me, is there a pharmacy near here?"},
        {"speaker": "Officer", "text": "Yes, there's one on Atatürk Street, next to the post office."},
        {"speaker": "Tourist", "text": "And where's the museum?"},
        {"speaker": "Officer", "text": "It's in the main square, opposite the bank."},
        {"speaker": "Tourist", "text": "Is it far?"},
        {"speaker": "Officer", "text": "No, it isn't. It's five minutes on foot."}],
     "questions": [
        mc("Where's the pharmacy?", ["Next to the post office", "Opposite the bank", "In the main square"], 0, "\"next to the post office\""),
        mc("How far is the museum?", ["Five minutes by bus", "Five minutes on foot", "Fifteen minutes on foot"], 1, "\"It's five minutes on foot.\""),
     ]},
    {"explanation": "Bir yer sormanın iki yolu var:\n\n- Belirli bir yer: **Where's the** museum? (Şehirde bir tane müze var, hangisi olduğu belli.)\n- Herhangi biri: **Is there a** pharmacy **near here**? (Herhangi bir eczane.)\n\nSoru sormadan önce **Excuse me** deriz.\n\nCevapta 4. ünitedeki yer edatlarını kullanırız: next to, opposite, between, on the corner, in the square, on ... Street.",
     "examples": [{"en": "Excuse me, where's the station?", "tr": "Affedersiniz, istasyon nerede?"},
                  {"en": "Is there a bank near here?", "tr": "Buralarda banka var mı?"},
                  {"en": "It's on the corner of Park Street.", "tr": "Park Caddesi'nin köşesinde."}],
     "turkishNote": "Cadde adlarıyla \"on\" kullanılır: on Atatürk Street (Atatürk Caddesi'nde). \"in Atatürk Street\" İngiliz İngilizcesinde de duyulur ama \"on\" daha yaygındır. Meydanda ise \"in the square\" denir."},
    [
        match([("pharmacy", "eczane"), ("post office", "postane"), ("station", "istasyon"), ("square", "meydan"), ("museum", "müze")], "Yerleri eşleştirin."),
        mc("Herhangi bir ATM arıyorsunuz:", ["Where's the ATM?", "Is there an ATM near here?"], 1, "Herhangi biri → Is there a/an ... near here?"),
        mc("Şehirdeki tek tren istasyonunu arıyorsunuz:", ["Where's the station?", "Is there a station?"], 0, "Belirli yer → Where's the ...?"),
        gap("___ me, where's the bus stop?", ["Excuse"], "Soru öncesi: Excuse me."),
        gap("The bank is ___ the corner.", ["on"], "köşede = on the corner."),
        gap("The café is ___ the main square.", ["in"], "meydanda = in the square."),
        order(["there", "Is", "a", "near", "supermarket", "here", "?"], "Is there a supermarket near here?", "Is there a + yer + near here?", "Buralarda süpermarket var mı?"),
        listen("The post office? It's on Park Street, between the bank and the bakery.", "Postane nerede?", ["Bankayla fırının arasında", "Bankanın karşısında", "Meydanda"], 0, "\"between the bank and the bakery\""),
        typ("İngilizce yazın: \"Affedersiniz, müze nerede?\"", variants("Excuse me, where's the museum?", "Excuse me, where is the museum?"), "Excuse me, where's the museum?"),
        mc("\"Is it far?\" (Uzak değil.)", ["No, it isn't.", "No, it doesn't.", "No, far."], 0, "be sorusu → No, it isn't."),
    ],
    {"kind": "speaking", "task": speak("Bir turiste, mahallenizdeki üç yerin nerede olduğunu anlatın.",
                                       "The bank is on Atatürk Street. There's a pharmacy next to the bank. The bus stop is opposite the supermarket.",
                                       ["Yer isimleri doğru", "Yer edatları doğru", "there is / the doğru"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "Emir cümleleri", "Talimat ve uyarıları emir cümlesiyle verebilirim.",
    {"kind": "dialogue", "title": "Müzede", "lines": [
        {"speaker": "Guide", "text": "Welcome to the museum! Please listen carefully."},
        {"speaker": "Guide", "text": "Stay with the group and don't touch the paintings."},
        {"speaker": "Guide", "text": "Don't use your camera flash, please."},
        {"speaker": "Guide", "text": "Turn off your phones in the cinema room."},
        {"speaker": "Guide", "text": "And enjoy the visit!"}],
     "questions": [
        mc("What can't visitors use?", ["Their phones", "Their camera flash", "Their maps"], 1, "\"Don't use your camera flash.\""),
        mc("Where do they turn off their phones?", ["In the café", "In the cinema room", "At the door"], 1, "\"Turn off your phones in the cinema room.\""),
     ]},
    {"explanation": "**Emir cümlesi** fiilin yalın hali ile başlar. Özne (you) söylenmez.\n\n- **Turn** left.\n- **Open** the window, please.\n- **Be** careful!\n\n**Olumsuz emir:** **Don't** + fiil\n\n- **Don't** park here.\n- **Don't** be late!\n\nKibar olmak için **please** eklenir: Please sit down. / Sit down, please.",
     "examples": [{"en": "Close the door, please.", "tr": "Kapıyı kapatın lütfen."},
                  {"en": "Don't worry!", "tr": "Merak etme!"},
                  {"en": "Be quiet in the library.", "tr": "Kütüphanede sessiz olun."}],
     "turkishNote": "Türkçede emir kipi sen/siz için farklıdır (kapat / kapatın). İngilizcede tek bir biçim vardır: Close the door. Kibarlık \"please\" ile sağlanır. \"Don't be late\" kalıbındaki \"be\" unutulmamalı: \"Don't late\" yanlıştır."},
    [
        match([("Turn", "left"), ("Don't", "park here"), ("Be", "careful"), ("Close", "the window")], "Emir cümlelerini tamamlayın."),
        mc("\"Geç kalma!\"", ["Don't late!", "Don't be late!", "Not be late!"], 1, "be ile: Don't be late.", {0: "\"late\" bir sıfat; önüne be gerekir."}),
        mc("Hangisi bir emir cümlesi?", ["You turn left.", "Turn left.", "Turning left."], 1, "Emir fiille başlar, özne yoktur."),
        gap("___ touch the paintings! (dokunmayın)", ["Don't", "Do not"], "Olumsuz emir: Don't + fiil."),
        gap("___ quiet, please. The baby is asleep.", ["Be"], "Sıfatla emir: Be + sıfat."),
        mc("Kibar bir rica:", ["Sit down!", "Please sit down.", "You sit."], 1, "please ile kibar."),
        order(["your", "Turn", "off", "phone", "please"], "Turn off your phone please.", "Fiil + nesne + please.", "Telefonunuzu kapatın lütfen."),
        listen("Don't cross the road here. Go to the traffic lights and cross there.", "Nerede karşıya geçmeli?", ["Burada", "Trafik ışıklarında", "Köşede"], 1, "\"Go to the traffic lights and cross there.\""),
        typ("Olumsuz emir yapın: \"Park here.\"", variants("Don't park here."), "Don't + park here."),
        mc("Tabelada \"No smoking\" yazıyor. Aynı anlam:", ["Don't smoke.", "Smoke here.", "You smoke."], 0, "No smoking = Don't smoke."),
    ],
    {"kind": "speaking", "task": speak("Evinize gelen bir misafire 3 kural söyleyin (2 olumlu, 1 olumsuz emir).",
                                       "Take off your shoes, please. Sit down and relax. Don't open the balcony door, the cat is outside.",
                                       ["Fiille başladı", "Don't + fiil doğru", "please kullandı"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "Yol tarifi", "Bir yere nasıl gidileceğini sorup tarif edebilirim.",
    {"kind": "dialogue", "title": "Sokakta", "lines": [
        {"speaker": "Mia", "text": "Excuse me, how do I get to the train station?"},
        {"speaker": "Man", "text": "Go straight on and turn left at the traffic lights."},
        {"speaker": "Mia", "text": "Left at the traffic lights. OK."},
        {"speaker": "Man", "text": "Then take the second right. The station is at the end of the street, on your left."},
        {"speaker": "Mia", "text": "Thank you very much!"},
        {"speaker": "Man", "text": "You're welcome."}],
     "questions": [
        mc("Where does Mia turn left?", ["At the station", "At the traffic lights", "At the second street"], 1, "\"turn left at the traffic lights\""),
        mc("Where is the station?", ["On the right", "At the end of the street, on the left", "Next to the lights"], 1, "\"at the end of the street, on your left\""),
     ]},
    {"explanation": "**Yol sormak:**\n\n- **How do I get to** the station?\n- **Can you tell me the way to** the museum?\n\n**Yol tarif etmek:**\n\n| İfade | Anlam |\n|---|---|\n| Go straight on. | Düz gidin. |\n| Turn left / right. | Sola / sağa dönün. |\n| Take the first / second left. | Soldaki birinci / ikinci sokağa girin. |\n| Go past the bank. | Bankayı geçin. |\n| Cross the road. | Karşıya geçin. |\n| It's on your left / right. | Solunuzda / sağınızda. |\n| at the end of the street | sokağın sonunda |",
     "examples": [{"en": "Go past the park and turn right.", "tr": "Parkı geçip sağa dönün."},
                  {"en": "Take the first left.", "tr": "İlk soldan girin."},
                  {"en": "The bank is on your right.", "tr": "Banka sağınızda."}],
     "turkishNote": "\"Sağa dön\" = turn right (turn to right değil). \"sağınızda\" = on your right. Teşekküre cevap olarak \"You're welcome\" (rica ederim) denir."},
    [
        match([("Go straight on.", "Düz gidin."), ("Turn right.", "Sağa dönün."), ("Take the first left.", "İlk soldan girin."), ("Go past the bank.", "Bankayı geçin."), ("It's on your left.", "Solunuzda.")], "İfadeleri eşleştirin."),
        gap("Turn ___ at the traffic lights. (sağa)", ["right"], "sağ = right"),
        gap("Take the ___ left. (ikinci)", ["second"], "ikinci = second"),
        gap("The museum is ___ your right.", ["on"], "on your right"),
        mc("Hangisi doğru?", ["Turn to left.", "Turn left.", "Turn the left."], 1, "Turn left (to/the yok)."),
        order(["do", "How", "get", "I", "to", "the", "station", "?"], "How do I get to the station?", "How do I get to + yer?", "İstasyona nasıl giderim?"),
        listen("Go straight on, go past the supermarket and take the first right. The pharmacy is on your left.", "Eczane nerede?", ["İlk sağdan girince solda", "Süpermarketin yanında", "İlk soldan girince sağda"], 0, "\"take the first right ... on your left\""),
        listen("Turn left at the bank, then go straight on. The bus stop is at the end of the street.", "Otobüs durağı nerede?", ["Bankanın yanında", "Sokağın sonunda", "Köşede"], 1, "\"at the end of the street\""),
        typ("İngilizce yazın: \"Işıklardan sola dönün.\"", variants("Turn left at the traffic lights.", "Turn left at the lights."), "Turn left + at the traffic lights."),
        mc("\"Thank you!\" sözüne cevap:", ["You're welcome.", "Yes, please.", "Excuse me."], 0, "Rica ederim = You're welcome."),
    ],
    {"kind": "speaking", "task": speak("JAI evinizin yakınında kayboldu. Ona evinizden en yakın markete nasıl gideceğini tarif edin.",
                                       "Go out of my building and turn right. Go straight on and take the second left. The supermarket is on your right, next to the bank.",
                                       ["Emir cümleleriyle tarif", "left/right ve first/second doğru", "on your left/right kullandı"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Rica ve izin", "can ile kibarca rica edip izin isteyebilirim.",
    {"kind": "dialogue", "title": "Otoparkta", "lines": [
        {"speaker": "Driver", "text": "Excuse me, can I park here?"},
        {"speaker": "Attendant", "text": "Sorry, you can't. It's only for buses."},
        {"speaker": "Driver", "text": "Oh. Can you help me? Where can I park?"},
        {"speaker": "Attendant", "text": "You can park behind the museum. It's free after six."},
        {"speaker": "Driver", "text": "Great. Can you show me on the map?"},
        {"speaker": "Attendant", "text": "Sure. Here it is."}],
     "questions": [
        mc("Can the driver park there?", ["Yes, he can.", "No, he can't."], 1, "\"Sorry, you can't. It's only for buses.\""),
        mc("Where can he park?", ["In front of the museum", "Behind the museum", "Next to the buses"], 1, "\"You can park behind the museum.\""),
     ]},
    {"explanation": "**can** her özneyle aynıdır ve ardından **yalın fiil** gelir.\n\n- **İzin istemek:** **Can I** park here? – Yes, you **can**. / No, you **can't**.\n- **Rica etmek:** **Can you** help me? – Sure. / Of course.\n- **Olasılık / izin:** You **can** park behind the museum. You **can't** smoke here.\n\n**can** ile -s, do/does ya da to kullanılmaz: ~~He cans~~, ~~Do you can~~, ~~can to go~~.",
     "examples": [{"en": "Can I sit here?", "tr": "Buraya oturabilir miyim?"},
                  {"en": "Can you repeat that, please?", "tr": "Tekrar eder misiniz lütfen?"},
                  {"en": "You can't take photos here.", "tr": "Burada fotoğraf çekemezsiniz."}],
     "turkishNote": "\"Can you...?\" Türkçedeki \"...ebilir misiniz?\" ricasının tam karşılığıdır. Daha da kibar olmak için \"Could you...?\" denir. Yeteneği anlatan can (I can swim) 9. ünitede gelecek."},
    [
        mc("İzin istemek: \"Buraya oturabilir miyim?\"", ["Can I sit here?", "Can you sit here?", "Do I can sit here?"], 0, "Can I + fiil?"),
        mc("Rica: \"Bana yardım edebilir misiniz?\"", ["Can I help you?", "Can you help me?", "You can help me."], 1, "Can you + fiil + me?"),
        gap("You ___ smoke here. It's a hospital.", ["can't", "cannot"], "Yasak → can't."),
        mc("Hangisi doğru?", ["Can I to park here?", "Can I park here?", "Do I can park here?"], 1, "can + yalın fiil (to yok)."),
        mc("\"Can I use your pen?\" (Evet.)", ["Yes, you can.", "Yes, I can.", "Yes, you do."], 0, "Yes, you can. / Sure."),
        order(["you", "Can", "show", "me", "on", "the", "map", "?"], "Can you show me on the map?", "Can you + fiil + me + ...?", "Bana haritada gösterebilir misiniz?"),
        listen("Excuse me, can I take photos in the museum? – Yes, you can, but you can't use the flash.", "Müzede ne yasak?", ["Fotoğraf çekmek", "Flaş kullanmak", "Telefon kullanmak"], 1, "\"you can't use the flash\""),
        typ("İngilizce yazın: \"Tekrar eder misiniz lütfen?\"", variants("Can you repeat that, please?", "Can you repeat, please?", "Could you repeat that, please?", "Can you say that again, please?"), "Can you repeat that, please?"),
        gap("___ I pay by card? – Yes, of course.", ["Can"], "İzin: Can I...?"),
        mc("Hangisi doğru?", ["She cans drive.", "She can drive.", "She can drives."], 1, "can her özneyle aynı, fiil yalın."),
    ],
    {"kind": "speaking", "task": speak("Bir otel resepsiyonundasınız. JAI resepsiyonist. 2 izin isteyin ve 1 rica edin.",
                                       "Can I leave my bag here? Can I pay by card? Can you call a taxi for me, please?",
                                       ["Can I (izin) doğru", "Can you (rica) doğru", "Fiil yalın, please kullandı"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Ulaşım", "Bir yere hangi araçla gidileceğini sorup söyleyebilirim.",
    {"kind": "dialogue", "title": "Metro gişesi", "lines": [
        {"speaker": "Tourist", "text": "Excuse me, how do I get to Taksim?"},
        {"speaker": "Officer", "text": "Take the M2 metro line. Get off at Taksim station."},
        {"speaker": "Tourist", "text": "How many stops is it?"},
        {"speaker": "Officer", "text": "It's four stops from here."},
        {"speaker": "Tourist", "text": "And can I buy a ticket here?"},
        {"speaker": "Officer", "text": "Yes. Buy an Istanbulkart. You can use it on buses, ferries and the metro."}],
     "questions": [
        mc("Where does the tourist get off?", ["At the fourth stop, Taksim", "At the second stop", "At the ferry"], 0, "\"It's four stops... Get off at Taksim station.\""),
        mc("Where can you use an Istanbulkart?", ["Only on the metro", "On buses, ferries and the metro", "Only on buses"], 1, "\"on buses, ferries and the metro\""),
     ]},
    {"explanation": "**Araçla gitmek:** **by** + araç (the yok): by bus, by train, by car, by taxi, by metro, by ferry, by plane\n\n**Yürüyerek:** **on foot** (~~by foot~~ değil)\n\n**Toplu taşıma ifadeleri:**\n\n- **take** the bus / the metro / a taxi (otobüse / metroya binmek)\n- **get on** (binmek) / **get off** (inmek)\n- How many stops is it? (Kaç durak?)\n- How do you get to work? – I go **by** bus.",
     "examples": [{"en": "I go to school by bus.", "tr": "Okula otobüsle giderim."},
                  {"en": "Take the number 25 bus.", "tr": "25 numaralı otobüse binin."},
                  {"en": "Get off at the third stop.", "tr": "Üçüncü durakta inin."}],
     "turkishNote": "Türkçede \"otobüse binmek\" deriz; İngilizcede genellikle \"take the bus\" denir. \"by\" ile araç arasında \"the\" ya da \"a\" olmaz: by car (by the car değil). Ama \"in my car\" (benim arabamla) denir."},
    [
        match([("by", "bus"), ("on", "foot"), ("get", "off"), ("take", "a taxi")], "İfadeleri tamamlayın."),
        mc("Hangisi doğru?", ["I go to work by foot.", "I go to work on foot.", "I go to work with foot."], 1, "Yürüyerek = on foot."),
        mc("Hangisi doğru?", ["by the car", "by car", "with car"], 1, "by + araç (the yok)."),
        gap("Get ___ at the next stop. (inin)", ["off"], "inmek = get off."),
        gap("___ the metro to Kadıköy. (binin)", ["Take"], "Metroya binmek = take the metro."),
        order(["you", "How", "get", "do", "work", "to", "?"], "How do you get to work?", "How do you get to + yer?", "İşe nasıl gidiyorsun?"),
        listen("I usually go to work by ferry, but on rainy days I take the metro.", "Konuşan genellikle işe nasıl gidiyor?", ["Metroyla", "Vapurla", "Otobüsle"], 1, "\"I usually go to work by ferry\""),
        typ("İngilizce yazın: \"İşe otobüsle giderim.\"", variants("I go to work by bus."), "go to work + by bus."),
        gap("How many ___ is it? (durak)", ["stops"], "durak = stop, çoğul: stops."),
        mc("\"How do you get to school?\" sorusuna uygun cevap:", ["By train.", "At eight.", "Yes, I do."], 0, "Nasıl → araç."),
    ],
    {"kind": "writing", "task": write("Bir arkadaşınıza evinizden şehir merkezine nasıl geleceğini yazın: hangi araç, nerede inmeli, sonra nasıl yürümeli.",
                                      "Take the number 12 bus from the station. Get off at the fifth stop, Cumhuriyet Square. Then go straight on and turn left at the bank. My flat is on your right.",
                                      ["take / get off doğru", "Emir cümleleri", "Yön ifadeleri doğru", "by / on foot doğru"])},
)

u.test([
    mc("Herhangi bir eczane arıyorsunuz:", ["Where's the pharmacy?", "Is there a pharmacy near here?"], 1, "Herhangi biri → Is there a ...?"),
    gap("The bank is ___ the corner.", ["on"], "on the corner"),
    mc("\"Geç kalma!\"", ["Don't be late!", "Don't late!", "Not late!"], 0, "Don't be + sıfat."),
    gap("___ park here. It's for buses. (Park etmeyin)", ["Don't", "Do not"], "Olumsuz emir."),
    mc("Hangisi doğru?", ["Turn to right.", "Turn right.", "Turn the right."], 1, "Turn right."),
    gap("Take the ___ left. (birinci)", ["first"], "birinci = first"),
    order(["get", "How", "do", "I", "to", "museum", "the", "?"], "How do I get to the museum?", "How do I get to + yer?", "Müzeye nasıl giderim?"),
    mc("İzin: \"Kartla ödeyebilir miyim?\"", ["Can you pay by card?", "Can I pay by card?", "Do I can pay by card?"], 1, "Can I + fiil?"),
    mc("Hangisi doğru?", ["Can you to help me?", "Can you help me?", "Do you can help me?"], 1, "can + yalın fiil."),
    mc("Hangisi doğru?", ["I go to school by foot.", "I go to school on foot."], 1, "on foot"),
    gap("Get ___ the bus at the third stop. (inin)", ["off"], "get off"),
    listen("Go straight on and take the second left. The museum is on your right, opposite the park.", "Müze nerede?", ["İkinci soldan girince sağda", "İkinci sağdan girince solda", "Parkın yanında"], 0, "\"take the second left ... on your right\""),
    typ("İngilizce yazın: \"Sağınızda.\"", variants("It's on your right.", "It is on your right.", "On your right."), "on your right"),
    mc("\"Thank you very much!\" sözüne cevap:", ["You're welcome.", "Excuse me.", "Yes, please."], 0, "Rica ederim."),
    write("Bir turiste, şehrinizdeki en sevdiğiniz yere nasıl gideceğini 5 cümleyle tarif edin.",
          "Take the metro to Şişhane and get off there. Go straight on and cross the road at the traffic lights. Turn right and go past the bookshop. The Galata Tower is at the end of the street. You can't miss it!",
          ["Emir cümleleri doğru", "Yön ifadeleri doğru", "Ulaşım ifadeleri doğru", "Yer edatları doğru"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

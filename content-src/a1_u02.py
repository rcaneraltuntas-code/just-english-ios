"""A1 Ünite 2: Ailem."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Unit, gap, listen, match, mc, order, speak, typ, variants, write  # noqa: E402

u = Unit("A1", 2, "Ailem", "My Family",
         "Ailemi ve arkadaşlarımı tanıtabilir, onların nasıl göründüğünü basitçe anlatabilirim.",
         ["iyelik sıfatları (my, your, his, her, our, their)", "iyelik 's", "have / has (aile)",
          "sıfatlar: görünüş"],
         ["aile üyeleri", "görünüş sıfatları"],
         {"title": "Aile fotoğrafı", "durationMinutes": 45,
          "goal": "Her öğrenci telefonundan bir aile fotoğrafı gösterip 4–5 cümleyle ailesini tanıtır, diğerleri soru sorar."})

u.vocab([
    ("mother", "anne", "My mother is a doctor.", "Annem bir doktor.", "Günlük konuşmada: mum (İngiliz), mom (Amerikan)"),
    ("father", "baba", "His father is from Ankara.", "Onun babası Ankaralı.", "Günlük konuşmada: dad"),
    ("parents", "anne baba, ebeveyn", "Her parents are teachers.", "Onun annesi ve babası öğretmen.", "Her zaman çoğul: anne ve baba birlikte."),
    ("brother", "erkek kardeş, ağabey", "I have one brother.", "Bir erkek kardeşim var.", "Ağabey de kardeş de brother'dır. Gerekirse older/younger eklenir."),
    ("sister", "kız kardeş, abla", "My sister is twenty.", "Kız kardeşim yirmi yaşında.", None),
    ("son", "oğul", "They have a son.", "Onların bir oğulları var.", "Telaffuzu \"sun\" (güneş) ile aynıdır."),
    ("daughter", "kız evlat", "Their daughter is a student.", "Onların kızı öğrenci.", "\"gh\" okunmaz: /ˈdɔːtə/"),
    ("husband", "koca, eş (erkek)", "Her husband is Italian.", "Onun kocası İtalyan.", None),
    ("wife", "karı, eş (kadın)", "His wife is a nurse.", "Onun karısı hemşire.", None),
    ("grandmother", "büyükanne, nine", "My grandmother is eighty.", "Büyükannem seksen yaşında.", "Günlük konuşmada: grandma"),
    ("grandfather", "büyükbaba, dede", "My grandfather is from Rize.", "Dedem Rizeli.", "Günlük konuşmada: grandpa"),
    ("aunt", "teyze, hala, yenge", "My aunt lives in London.", "Teyzem Londra'da yaşıyor.", "İngilizcede teyze ve hala aynı kelimedir."),
    ("uncle", "amca, dayı, enişte", "Our uncle is a chef.", "Amcamız bir aşçı.", "İngilizcede amca ve dayı aynı kelimedir."),
    ("cousin", "kuzen", "Selin is my cousin.", "Selin benim kuzenim.", None),
    ("child / children", "çocuk / çocuklar", "They have three children.", "Onların üç çocuğu var.", "Düzensiz çoğul: childs değil, children."),
    ("only child", "tek çocuk", "I'm an only child.", "Ben tek çocuğum.", None),
    ("married", "evli", "My brother is married.", "Ağabeyim evli.", None),
    ("tall", "uzun boylu", "My father is very tall.", "Babam çok uzun boylu.", "İnsanlar için long değil, tall kullanılır."),
    ("short", "kısa (boylu); kısa", "She has short hair.", "Onun kısa saçları var.", None),
    ("young", "genç", "Their parents are young.", "Onların anne babası genç.", None),
    ("hair", "saç", "He has dark hair.", "Onun koyu renk saçları var.", "Sayılamaz: hairs değil, hair."),
    ("slim", "ince, zayıf", "My sister is tall and slim.", "Kız kardeşim uzun boylu ve ince.", None),
    ("friendly", "cana yakın, arkadaş canlısı", "My cousins are very friendly.", "Kuzenlerim çok cana yakın.", None),
])

# ---------------- Ders 1 ----------------
u.lesson(
    "Aile üyeleri", "Aile üyelerimin adını söyleyebilir ve onları tanıtabilirim.",
    {"kind": "dialogue", "title": "Bir fotoğraf", "lines": [
        {"speaker": "Ali", "text": "Is this your family, Elif?"},
        {"speaker": "Elif", "text": "Yes, it is. This is my mother and this is my father."},
        {"speaker": "Ali", "text": "And who's this?"},
        {"speaker": "Elif", "text": "That's my brother, Can. And this is my grandmother."},
        {"speaker": "Ali", "text": "She looks very happy!"},
        {"speaker": "Elif", "text": "She is! She's eighty and she's very funny."}],
     "questions": [
        mc("Who is Can?", ["Elif's father", "Elif's brother", "Elif's cousin"], 1, "Elif \"That's my brother, Can.\" diyor."),
        mc("How old is Elif's grandmother?", ["18", "80", "90"], 1, "\"She's eighty.\" = 80"),
     ]},
    {"explanation": "Aileyi tanıtırken **This is my ...** kalıbını kullanırız. Uzaktaki biri ya da fotoğrafta uzaktaki kişi için **That's my ...** denir.\n\n"
                    "| Kadın | Erkek | İkisi birlikte |\n|---|---|---|\n| mother | father | parents |\n| sister | brother | — |\n| daughter | son | children |\n| wife | husband | — |\n| grandmother | grandfather | grandparents |\n| aunt | uncle | — |\n\n**cousin** (kuzen) hem kız hem erkek için kullanılır.",
     "examples": [{"en": "This is my sister, Ayşe.", "tr": "Bu benim kız kardeşim, Ayşe."},
                  {"en": "Who's that?", "tr": "Şu kim?"},
                  {"en": "These are my parents.", "tr": "Bunlar benim annem ve babam."}],
     "turkishNote": "Türkçede abla/kız kardeş, ağabey/erkek kardeş, teyze/hala, amca/dayı ayrı kelimelerdir. İngilizcede her biri için tek kelime var: sister, brother, aunt, uncle. Yaşı belirtmek gerekirse \"older sister\" (abla), \"younger brother\" (küçük erkek kardeş) denir."},
    [
        match([("mother", "anne"), ("son", "oğul"), ("aunt", "teyze / hala"), ("uncle", "amca / dayı"), ("cousin", "kuzen")], "Aile kelimelerini Türkçeleriyle eşleştirin."),
        mc("Annenizin annesi sizin neyiniz olur?", ["aunt", "grandmother", "sister"], 1, "Annenin annesi = grandmother (büyükanne)."),
        mc("Babanızın erkek kardeşi:", ["uncle", "cousin", "grandfather"], 0, "Amca ve dayı İngilizcede aynı kelimedir: uncle."),
        gap("My father's wife is my ___.", ["mother"], "Babanın eşi = anne (mother). Üvey anne ise stepmother'dır."),
        gap("My aunt's son is my ___.", ["cousin"], "Teyzenin ya da halanın oğlu = kuzen (cousin)."),
        mc("\"parents\" kimleri kapsar?", ["Anne ve baba", "Bütün akrabalar", "Kardeşler"], 0, "parents = anne ve baba. Bütün akrabalar için relatives kullanılır.", {1: "Dikkat: parents yalnızca anne ve babadır. Akrabalar = relatives."}),
        order(["is", "This", "my", "brother"], "This is my brother.", "This is + kişi.", "Bu benim erkek kardeşim."),
        listen("This is my uncle, Mehmet. He's my mother's brother.", "Mehmet konuşanın neyi?", ["Babası", "Dayısı", "Kuzeni"], 1, "\"my mother's brother\" = annesinin erkek kardeşi, yani dayısı (uncle)."),
        typ("İngilizce yazın: \"Bu benim büyükannem.\"", variants("This is my grandmother.", "This is my grandma."), "This is my + aile üyesi."),
        mc("Kız kardeşinizi tanıtıyorsunuz. O, sizden uzakta duruyor:", ["This is my sister.", "That's my sister.", "Those are my sister."], 1, "Uzaktaki tek kişi için that kullanılır.", {2: "those çoğul içindir. Tek kişi için that."}),
    ],
    {"kind": "speaking", "task": speak("Ailenizden üç kişiyi tanıtın (This is my ...).",
                                       "This is my mother, Ayşe. This is my father, Ahmet. And this is my sister, Elif.",
                                       ["This is my ... kalıbını kullandı", "Aile kelimeleri doğru", "İsimleri ekledi"])},
)

# ---------------- Ders 2 ----------------
u.lesson(
    "Benim, senin, onun", "my, your, his, her, our, their ile kimin neyi olduğunu söyleyebilirim.",
    {"kind": "dialogue", "title": "Partide", "lines": [
        {"speaker": "Mia", "text": "Hi! I'm Mia. What's your name?"},
        {"speaker": "Tom", "text": "I'm Tom. And this is my friend, Ken."},
        {"speaker": "Mia", "text": "Nice to meet you, Ken. Is that your sister?"},
        {"speaker": "Ken", "text": "No, she isn't. That's Tom's sister. Her name is Lisa."},
        {"speaker": "Mia", "text": "And who are they?"},
        {"speaker": "Tom", "text": "They're our neighbours. Their son is in my class."}],
     "questions": [
        mc("Who is Lisa?", ["Ken's sister", "Tom's sister", "Mia's sister"], 1, "\"That's Tom's sister. Her name is Lisa.\""),
        mc("Who is in Tom's class?", ["The neighbours' son", "Ken's brother", "Lisa"], 0, "\"Their son is in my class.\""),
     ]},
    {"explanation": "İyelik sıfatları ismin önüne gelir ve \"kimin\" olduğunu gösterir.\n\n| Özne | İyelik | Örnek |\n|---|---|---|\n| I | my | my car |\n| you | your | your phone |\n| he | his | his mother |\n| she | her | her father |\n| it | its | its name |\n| we | our | our house |\n| they | their | their children |\n\nİyelik sıfatı değişmez: my brother, my brothers.",
     "examples": [{"en": "His name is Ali.", "tr": "Onun (erkek) adı Ali."},
                  {"en": "Her name is Elif.", "tr": "Onun (kadın) adı Elif."},
                  {"en": "Their house is big.", "tr": "Onların evi büyük."}],
     "turkishNote": "his ve her, sahip olanın cinsiyetine göre seçilir, sahip olunan şeye göre değil. Ali'nin annesi → his mother (Ali erkek olduğu için). Elif'in babası → her father. Ayrıca \"its\" (onun) ile \"it's\" (it is) farklıdır: The cat is happy. Its name is Tom."},
    [
        match([("I", "my"), ("he", "his"), ("she", "her"), ("we", "our"), ("they", "their")], "Özne → iyelik sıfatı"),
        gap("Ali is my friend. ___ sister is a doctor.", ["His"], "Ali erkek, bu yüzden his.", "Ali erkek"),
        gap("Elif is a student. ___ father is a teacher.", ["Her"], "Elif kadın, bu yüzden her."),
        mc("Tom and Lisa have a dog. ___ dog is small.", ["Their", "There", "They're"], 0, "Onların = their. There (orada) ve they're (they are) sesçe benzer ama farklıdır.",
           {1: "there \"orada\" demektir. Sahiplik için their.", 2: "they're = they are. Sahiplik için their."}),
        mc("Ali'nin annesi için hangisi doğru?", ["her mother", "his mother", "its mother"], 1, "Sahip olan Ali (erkek), bu yüzden his. Annenin kadın olması önemli değil.",
           {0: "Dikkat! Sahip olana bakılır: Ali erkek → his."}),
        gap("We're from Izmir. ___ house is near the sea.", ["Our"], "we → our"),
        mc("What's ___ name? – My name is Can.", ["you", "your", "you're"], 1, "Senin = your. you're = you are."),
        order(["name", "Her", "Selin", "is"], "Her name is Selin.", "İyelik sıfatı + isim + is + ...", "Onun adı Selin."),
        listen("This is my friend Ken. His family is from Japan. His sister's name is Yuki.", "Yuki kimin kız kardeşi?", ["Konuşanın", "Ken'in", "Tom'un"], 1, "\"His sister's name is Yuki\": his = Ken'in."),
        typ("İngilizce yazın: \"Onların evi büyük.\"", variants("Their house is big."), "their + house"),
    ],
    {"kind": "writing", "task": write("Bir arkadaşınızı ve onun ailesini 3 cümleyle anlatın (his/her kullanın).",
                                      "This is my friend Deniz. Her mother is a teacher. Her brother's name is Ozan.",
                                      ["his/her doğru seçildi", "İyelik sıfatı ismin önünde", "is doğru kullanıldı"])},
)

# ---------------- Ders 3 ----------------
u.lesson(
    "Ali'nin kız kardeşi", "'s ile birinin akrabasını ya da eşyasını söyleyebilirim.",
    {"kind": "dialogue", "title": "Aile ağacı", "lines": [
        {"speaker": "Teacher", "text": "Look at Can's family tree. Who's Ayşe?"},
        {"speaker": "Student", "text": "She's Can's mother."},
        {"speaker": "Teacher", "text": "Right. And who's Murat?"},
        {"speaker": "Student", "text": "He's Ayşe's brother, so he's Can's uncle."},
        {"speaker": "Teacher", "text": "Very good! And Murat's children are Can's...?"},
        {"speaker": "Student", "text": "Cousins!"}],
     "questions": [
        mc("Who is Murat?", ["Can's father", "Can's uncle", "Can's cousin"], 1, "Murat, Can'in annesinin erkek kardeşi: uncle."),
        mc("What are Murat's children to Can?", ["brothers", "cousins", "sons"], 1, "\"Cousins!\""),
     ]},
    {"explanation": "İsimden sonra **'s** getirerek sahipliği gösteririz. Türkçedeki \"-in\" ekine benzer.\n\n- Ali**'s** sister = Ali'nin kız kardeşi\n- my mother**'s** car = annemin arabası\n\nÇoğul ve -s ile biten isimlerde yalnızca kesme işareti eklenir: my parents**'** house (annemle babamın evi).\n\nKimin olduğunu sormak için: **Whose** bag is this? – It's Tom's.",
     "examples": [{"en": "Elif's brother is a student.", "tr": "Elif'in erkek kardeşi öğrenci."},
                  {"en": "This is my parents' car.", "tr": "Bu annemle babamın arabası."},
                  {"en": "Whose phone is this? – It's Ali's.", "tr": "Bu kimin telefonu? – Ali'nin."}],
     "turkishNote": "Türkçede ek ismin sonuna gelir ve sahip olunan şey de ek alır (Ali'nin kardeş-i). İngilizcede yalnızca sahip olan 's alır: Ali's sister. Dikkat: \"Ali's tall\" cümlesindeki 's ise \"is\"in kısaltmasıdır (Ali is tall)."},
    [
        mc("\"Elif'in annesi\" İngilizcede:", ["Elif mother", "Elif's mother", "mother's Elif"], 1, "Sahip olan + 's + sahip olunan."),
        gap("This is Tom___ bike.", ["'s"], "Tom'un bisikleti = Tom's bike."),
        gap("My parents___ house is in Bursa.", ["'"], "Çoğul -s ile biten isimde yalnızca kesme işareti: parents'."),
        mc("\"Ali's tall.\" cümlesindeki 's nedir?", ["Sahiplik ('in)", "is'in kısaltması"], 1, "Ali's tall = Ali is tall. Ardından bir isim değil sıfat geliyor."),
        mc("\"Ali's car\" cümlesindeki 's nedir?", ["Sahiplik ('in)", "is'in kısaltması"], 0, "Ardından bir isim (car) geliyor, yani sahiplik: Ali'nin arabası."),
        order(["Whose", "is", "this", "bag", "?"], "Whose bag is this?", "Whose + isim + is + this?", "Bu kimin çantası?"),
        gap("___ book is this? – It's Elif's.", ["Whose"], "Kimin = whose."),
        listen("This is my cousin Deniz. Deniz's father is my uncle Murat. Deniz's mother is a doctor.", "Deniz'in annesinin mesleği ne?", ["Öğretmen", "Doktor", "Hemşire"], 1, "\"Deniz's mother is a doctor.\""),
        typ("İngilizce yazın: \"Bu Can'in telefonu.\"", variants("This is Can's phone."), "Can's + phone"),
        mc("Annenizin kız kardeşinin oğlu sizin neyinizdir?", ["My cousin", "My uncle", "My brother"], 0, "Teyzenin oğlu = kuzen (cousin)."),
    ],
    {"kind": "speaking", "task": speak("JAI size aile ağacınızla ilgili sorular soracak (örneğin \"Who's your mother's sister?\"). 's kullanarak cevaplayın.",
                                       "My mother's sister is my aunt, Zeynep. Her son is my cousin, Ege.",
                                       ["'s ile sahiplik doğru", "Aile kelimeleri doğru", "his/her doğru"])},
)

# ---------------- Ders 4 ----------------
u.lesson(
    "Kaç kardeşin var?", "Kaç kardeşim olduğunu söyleyip başkalarına sorabilirim.",
    {"kind": "dialogue", "title": "Yeni arkadaş", "lines": [
        {"speaker": "Lucas", "text": "Do you have any brothers or sisters, Deniz?"},
        {"speaker": "Deniz", "text": "Yes, I have two sisters. They're twins!"},
        {"speaker": "Lucas", "text": "Wow! How old are they?"},
        {"speaker": "Deniz", "text": "They're twelve. And you?"},
        {"speaker": "Lucas", "text": "I don't have any brothers or sisters. I'm an only child."},
        {"speaker": "Deniz", "text": "But you have a lot of cousins, right?"},
        {"speaker": "Lucas", "text": "Yes! My mother has five brothers and sisters, so I have fourteen cousins."}],
     "questions": [
        mc("How many sisters does Deniz have?", ["One", "Two", "Three"], 1, "\"I have two sisters.\""),
        mc("What does \"only child\" mean?", ["The youngest child", "A child with no brothers or sisters", "A child with one sister"], 1, "Lucas'ın kardeşi yok: \"I don't have any brothers or sisters. I'm an only child.\""),
     ]},
    {"explanation": "Sahip olduklarımızı **have** ile söyleriz. **he, she, it** ile **has** olur.\n\n- I / you / we / they **have** a brother.\n- he / she / it **has** a brother.\n\nSoru ve olumsuz için şimdilik bu kalıpları öğrenelim (geniş zamanı 5. ünitede ayrıntılı göreceğiz):\n\n- **Do you have** any brothers or sisters?\n- **How many** cousins **do you have**?\n- I **don't have** any brothers.",
     "examples": [{"en": "I have one brother and one sister.", "tr": "Bir erkek, bir kız kardeşim var."},
                  {"en": "She has three children.", "tr": "Onun üç çocuğu var."},
                  {"en": "How many cousins do you have?", "tr": "Kaç kuzenin var?"}],
     "turkishNote": "Türkçede \"var\" kelimesi her yerde aynıdır. İngilizcede sahiplik için have/has kullanılır: \"Bir kardeşim var\" = I have a brother. \"There is\" ise bir yerde bir şeyin bulunduğunu anlatır (4. ünite). \"I have\" ile \"there is\"i karıştırmayın."},
    [
        match([("I", "have"), ("she", "has"), ("they", "have"), ("he", "has"), ("we", "have")], "he/she/it → has, diğerleri → have"),
        gap("My brother ___ two children.", ["has"], "my brother = he → has"),
        gap("We ___ a big family.", ["have"], "we → have"),
        mc("Hangisi doğru?", ["She have a sister.", "She has a sister.", "She is a sister have."], 1, "she → has", {0: "she ile have değil, has kullanılır."}),
        order(["many", "How", "cousins", "you", "have", "do", "?"], "How many cousins do you have?", "How many + çoğul isim + do you have?", "Kaç kuzenin var?"),
        mc("\"Do you have any brothers?\" Kardeşiniz yok. Cevabınız:", ["No, I don't. I'm an only child.", "No, I haven't brothers.", "No, I'm not."], 0, "Do you have...? sorusuna kısa cevap: No, I don't."),
        gap("I don't have ___ sisters.", ["any"], "Olumsuz ve soru cümlelerinde çoğul isimden önce any kullanılır."),
        listen("I have one brother and two sisters. My brother is married and he has a daughter.", "Konuşanın kaç kardeşi var?", ["İki", "Üç", "Dört"], 1, "1 brother + 2 sisters = 3 kardeş."),
        typ("İngilizce yazın: \"İki erkek kardeşim var.\"", variants("I have two brothers.", "I've got two brothers."), "I have + two + çoğul isim."),
        mc("Hangisi doğru?", ["My aunt has two childs.", "My aunt has two children.", "My aunt have two children."], 1, "child'ın çoğulu düzensizdir: children. aunt → has."),
    ],
    {"kind": "speaking", "task": speak("JAI size kardeşlerinizi ve kuzenlerinizi soracak. Kaç tane olduklarını ve yaşlarını söyleyin.",
                                       "I have one brother. He's twenty-five. I have six cousins.",
                                       ["have/has doğru", "Sayılar doğru", "Çoğul isimler doğru (brothers, cousins)"])},
)

# ---------------- Ders 5 ----------------
u.lesson(
    "Nasıl biri?", "Aile üyelerimin görünüşünü basit sıfatlarla anlatabilirim.",
    {"kind": "dialogue", "title": "Havaalanında", "lines": [
        {"speaker": "Elif", "text": "Can you meet my cousin at the airport? Her name's Sara."},
        {"speaker": "Tom", "text": "Sure. What does she look like?"},
        {"speaker": "Elif", "text": "She's tall and slim. She has long dark hair."},
        {"speaker": "Tom", "text": "Is she young?"},
        {"speaker": "Elif", "text": "Yes, she's twenty-two. And she's very friendly!"}],
     "questions": [
        mc("What does Sara look like?", ["Short with fair hair", "Tall with long dark hair", "Tall with short hair"], 1, "\"She's tall and slim. She has long dark hair.\""),
        mc("How old is Sara?", ["20", "22", "32"], 1, "\"She's twenty-two.\""),
     ]},
    {"explanation": "Birinin görünüşünü sormak için: **What does he/she look like?**\n\nCevap vermek için iki kalıp var:\n\n- **be** + sıfat → She**'s** tall. He**'s** young.\n- **have/has** + sıfat + hair → She **has** long dark hair.\n\nSıfatlar ismin **önüne** gelir ve hiçbir zaman çoğul eki almaz: two tall brothers.",
     "examples": [{"en": "My father is tall.", "tr": "Babam uzun boylu."},
                  {"en": "My sister has short fair hair.", "tr": "Kız kardeşimin kısa sarı saçları var."},
                  {"en": "What does your brother look like?", "tr": "Ağabeyin nasıl görünüyor?"}],
     "turkishNote": "İnsan boyu için \"long\" değil \"tall\" kullanılır: a tall man. \"long\" saç, yol gibi şeyler içindir: long hair. Ayrıca \"hair\" sayılamaz, \"hairs\" denmez. Sıfatlar da çoğul olmaz: \"talls brothers\" değil, \"tall brothers\"."},
    [
        match([("tall", "uzun boylu"), ("short", "kısa"), ("young", "genç"), ("slim", "ince, zayıf"), ("friendly", "cana yakın")], "Sıfatları eşleştirin."),
        mc("Hangisi doğru?", ["My brother is long.", "My brother is tall.", "My brother has tall."], 1, "İnsan boyu için tall.", {0: "long insan boyu için kullanılmaz. tall deyin."}),
        mc("Hangisi doğru?", ["She has long hair.", "She has long hairs.", "She is long hair."], 0, "hair sayılamaz, -s almaz; görünüş için has + hair."),
        gap("He ___ short dark hair.", ["has"], "Saç için has kullanılır."),
        gap("My grandmother ___ very friendly.", ["is"], "Kişilik ve görünüş sıfatı için be: is."),
        order(["does", "What", "look", "she", "like", "?"], "What does she look like?", "Görünüş sorusu: What does ... look like?", "O nasıl görünüyor?"),
        mc("\"İki uzun boylu ağabeyim var.\"", ["I have two talls brothers.", "I have two tall brothers.", "I have two brothers tall."], 1, "Sıfat ismin önüne gelir ve çoğul eki almaz."),
        listen("My uncle is tall and he has short dark hair. He's fifty-five.", "Amcanın saçı nasıl?", ["Uzun ve koyu renk", "Kısa ve koyu renk", "Kısa ve sarı"], 1, "\"short dark hair\" = kısa, koyu renk saç"),
        typ("İngilizce yazın: \"Annem genç ve cana yakın.\"", variants("My mother is young and friendly.", "My mum is young and friendly.", "My mom is young and friendly."), "be + sıfat + and + sıfat"),
        mc("\"Your sister is very friendly!\" cümlesine uygun bir cevap:", ["Yes, she is!", "Yes, she has!", "Yes, she does friendly!"], 0, "be ile kurulan cümleye be ile kısa cevap: Yes, she is."),
    ],
    {"kind": "speaking", "task": speak("Ailenizden birini anlatın: kim, kaç yaşında, nasıl görünüyor?",
                                       "This is my brother, Emre. He's thirty. He's tall and he has short dark hair. He's very friendly.",
                                       ["Aile ilişkisini söyledi", "be + sıfat doğru", "has + hair doğru", "Sıfat sırası doğru"])},
)

u.test([
    mc("Babanızın babası:", ["uncle", "grandfather", "cousin"], 1, "Babanın babası = grandfather."),
    mc("Annenizin kız kardeşi:", ["aunt", "sister", "cousin"], 0, "Teyze = aunt."),
    gap("Ayşe is a teacher. ___ husband is a doctor.", ["Her"], "Ayşe kadın → her."),
    gap("Can and Ece are married. ___ son is five.", ["Their"], "Onların = their."),
    mc("Ali'nin annesi:", ["Ali's mother", "her mother of Ali", "Ali mother's"], 0, "Ali's mother"),
    mc("Hangisi doğru?", ["She have two brothers.", "She has two brothers.", "She has two brother."], 1, "she → has, two → çoğul brothers."),
    gap("How ___ cousins do you have?", ["many"], "Kaç tane = how many."),
    mc("\"Do you have any sisters?\" Kız kardeşiniz yok:", ["No, I don't.", "No, I'm not.", "No, I haven't sisters."], 0, "Do you have...? → No, I don't."),
    order(["parents'", "This", "my", "is", "car"], "This is my parents' car.", "Çoğul isimde kesme işareti: parents'.", "Bu annemle babamın arabası."),
    mc("Hangisi doğru?", ["My father is very long.", "My father is very tall.", "My father has very tall."], 1, "İnsan boyu = tall."),
    gap("She ___ long fair hair.", ["has"], "Saç için has."),
    listen("My sister is twenty-eight. She's married and she has a son. His name is Arda.", "Arda kimin oğlu?", ["Konuşanın", "Konuşanın kız kardeşinin", "Konuşanın annesinin"], 1, "\"My sister ... has a son. His name is Arda.\" Arda, kız kardeşin oğlu."),
    typ("Çoğulunu yazın: child", ["children", "Children"], "child → children (düzensiz çoğul)"),
    mc("What does your brother look like?", ["He's a doctor.", "He's tall with dark hair.", "He likes football."], 1, "look like görünüşü sorar."),
    write("Ailenizi 5 cümleyle tanıtın: kaç kişisiniz, kimler var, biri nasıl görünüyor?",
          "I have a small family. My mother's name is Ayşe and my father's name is Ali. I have one sister. Her name is Ece. She's tall and she has long dark hair.",
          ["Aile kelimeleri doğru", "have/has doğru", "his/her ve 's doğru", "Görünüş sıfatları doğru yerde"]),
])

if __name__ == "__main__":
    u.save(sys.argv[1])

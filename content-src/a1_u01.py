"""A1 Ünite 1 kaynak dosyası: uygulama JSON'u ve öğretmen inceleme Markdown'u üretir."""
import json, sys

U = "a1-u01"
cards = [
 # (en, tr, example, example_tr, note)
 ("hello","merhaba","Hello! I'm Deniz.","Merhaba! Ben Deniz.",None),
 ("hi","selam","Hi, Tom!","Selam, Tom!","Arkadaşlar arasında kullanılır."),
 ("good morning","günaydın","Good morning, Mrs Smith.","Günaydın, Bayan Smith.",None),
 ("good afternoon","tünaydın / iyi günler","Good afternoon, everyone.","Herkese iyi günler.","Öğleden sonra selamlaşırken."),
 ("good evening","iyi akşamlar","Good evening! Welcome.","İyi akşamlar! Hoş geldiniz.","Karşılaşırken söylenir."),
 ("good night","iyi geceler","Good night, Mum.","İyi geceler, anne.","Yalnızca ayrılırken ya da yatarken söylenir, selamlaşmada değil."),
 ("goodbye","hoşça kal","Goodbye, see you tomorrow.","Hoşça kal, yarın görüşürüz.",None),
 ("see you","görüşürüz","See you later!","Sonra görüşürüz!",None),
 ("Nice to meet you.","Tanıştığımıza memnun oldum.","Hi, I'm Ali. – Nice to meet you, Ali.","Selam, ben Ali. – Tanıştığımıza memnun oldum, Ali.",None),
 ("name","isim, ad","My name is Elif.","Benim adım Elif.",None),
 ("country","ülke","Turkey is a big country.","Türkiye büyük bir ülke.",None),
 ("Turkey / Turkish","Türkiye / Türk, Türkçe","I'm from Turkey. I'm Turkish.","Türkiye'denim. Türk'üm.","Milliyetler büyük harfle yazılır: Turkish."),
 ("England / English","İngiltere / İngiliz, İngilizce","She's from England. She's English.","O İngiltere'den. İngiliz.",None),
 ("the USA / American","ABD / Amerikalı","They're from the USA. They're American.","Onlar ABD'den. Amerikalılar.","the USA, the UK: \"the\" ile kullanılır."),
 ("Germany / German","Almanya / Alman, Almanca","Hans is from Germany.","Hans Almanya'dan.",None),
 ("Spain / Spanish","İspanya / İspanyol","Carmen is Spanish.","Carmen İspanyol.",None),
 ("Japan / Japanese","Japonya / Japon","Yuki is from Japan.","Yuki Japonya'dan.",None),
 ("Brazil / Brazilian","Brezilya / Brezilyalı","Lucas is Brazilian.","Lucas Brezilyalı.",None),
 ("old","yaşında; yaşlı, eski","I'm 25 years old.","25 yaşındayım.","Yaş \"be\" ile söylenir: I am 25. (\"I have 25\" yanlıştır.)"),
 ("friend","arkadaş","This is my friend, Can.","Bu benim arkadaşım, Can.",None),
 ("student","öğrenci","I'm a student.","Ben bir öğrenciyim.","Tekil meslek ve rollerde a/an kullanılır."),
 ("teacher","öğretmen","She's an English teacher.","O bir İngilizce öğretmeni.",None),
]
vocab = [{"id":f"{U}-v{i+1:02d}","en":c[0],"tr":c[1],"example":c[2],"exampleTr":c[3],**({"note":c[4]} if c[4] else {})} for i,c in enumerate(cards)]

def mc(prompt, options, answer, why, wrong=None):
    d={"type":"multipleChoice","prompt":prompt,"options":options,"answerIndex":answer,"explanation":why}
    if wrong: d["wrongFeedback"]=wrong
    return d
def gap(text, answers, why, hint=None):
    d={"type":"gapFill","text":text,"answers":answers,"explanation":why}
    if hint: d["hint"]=hint
    return d
def order(words, answer, why, tr=None):
    d={"type":"ordering","words":words,"answer":answer,"explanation":why}
    if tr: d["translation"]=tr
    return d
def match(pairs, why): return {"type":"matching","pairs":[{"left":a,"right":b} for a,b in pairs],"explanation":why}
def typ(prompt, accepted, why): return {"type":"typeAnswer","prompt":prompt,"accepted":accepted,"explanation":why}
def listen(audio, prompt, options, answer, why): return {"type":"listening","audioText":audio,"prompt":prompt,"options":options,"answerIndex":answer,"explanation":why}
def speak(prompt, target, rubric): return {"type":"speaking","prompt":prompt,"modelAnswer":target,"rubric":rubric}
def write(prompt, model, rubric): return {"type":"writing","prompt":prompt,"modelAnswer":model,"rubric":rubric}

lessons = []
def lesson(title, goal, discover, learn, practice, use, warmup=None):
    n=len(lessons)+1
    lid=f"{U}-l{n}"
    for i,ex in enumerate(practice): ex["id"]=f"{lid}-p{i+1:02d}"
    for i,q in enumerate(discover["questions"]): q["id"]=f"{lid}-d{i+1:02d}"
    use["id"]=f"{lid}-use"
    lessons.append({"id":lid,"number":n,"title":title,"goal":goal,"warmup":warmup or {"source":"review","count":6},
                    "discover":discover,"learn":learn,"practice":practice,"use":use})

# ---------------- Ders 1: Selam! ----------------
lesson("Selam!","İnsanlarla selamlaşıp adımı söyleyebilirim.",
 {"kind":"dialogue","title":"İlk gün","lines":[
   {"speaker":"Emma","text":"Good morning! I'm Emma. I'm your teacher."},
   {"speaker":"Deniz","text":"Good morning! My name is Deniz."},
   {"speaker":"Emma","text":"Nice to meet you, Deniz."},
   {"speaker":"Deniz","text":"Nice to meet you, too."},
   {"speaker":"Emma","text":"And what's your name?"},
   {"speaker":"Ali","text":"Hi! I'm Ali."}],
  "questions":[
   mc("What's the teacher's name?",["Deniz","Emma","Ali"],1,"Öğretmen \"I'm Emma. I'm your teacher.\" diyor."),
   mc("What time of day is it?",["Morning","Evening","Night"],0,"Herkes \"Good morning\" diyor, yani sabah."),
  ]},
 {"explanation":"Kendimizi tanıtmanın iki yolu var:\n\n- **I'm** + isim → I'm Deniz. (Günlük, doğal)\n- **My name is** + isim → My name is Deniz. (Biraz daha resmi)\n\nKarşımızdakinin adını sormak için: **What's your name?**\n\nTanıştıktan sonra **Nice to meet you.** deriz. Cevap: **Nice to meet you, too.**",
  "examples":[{"en":"Hi! I'm Can.","tr":"Selam! Ben Can."},{"en":"My name is Elif.","tr":"Benim adım Elif."},{"en":"What's your name?","tr":"Adın ne?"}],
  "turkishNote":"\"Good night\" bir selamlaşma değildir. Akşam birine rastladığınızda \"Good evening\" deyin. \"Good night\" yalnızca ayrılırken ya da yatmadan önce söylenir."},
 [
  match([("Good morning","Günaydın"),("Good evening","İyi akşamlar"),("Good night","İyi geceler"),("Goodbye","Hoşça kal")],"Sabah, akşam ve gece selamlarını ayırt edin."),
  mc("Saat 20:00. Bir arkadaşınızla karşılaşıyorsunuz. Ne dersiniz?",["Good night!","Good evening!","Good morning!"],1,"Akşam karşılaşınca \"Good evening\" denir. \"Good night\" yalnızca ayrılırken söylenir.",
     {"0":"Dikkat! \"Good night\" yalnızca vedalaşırken kullanılır."}),
  gap("___ name is Deniz.",["My"],"\"Benim adım\" = My name.", "Benim"),
  gap("Hi, ___ Tom.",["I'm","I am"],"\"Ben ...\" = I'm ... (I am'in kısa hali)"),
  order(["your","What's","name","?"],"What's your name?","Soru kelimesi (What) başa gelir.","Adın ne?"),
  mc("\"Nice to meet you.\" cümlesine en doğal cevap hangisi?",["Nice to meet you, too.","Yes, I am.","Good night."],0,"Aynı cümleyi \"too\" (de/da) ekleyerek geri söyleriz."),
  listen("Hi! My name is Sara. Nice to meet you.","Konuşanın adı ne?",["Sara","Sam","Zara"],0,"\"My name is Sara.\""),
  order(["is","My","Elif","name"],"My name is Elif.","İngilizcede özne (My name) önce, fiil (is) sonra gelir.","Benim adım Elif."),
  typ("İngilizce yazın: \"Selam! Ben Can.\"",["Hi! I'm Can.","Hi, I'm Can.","Hi! I am Can.","Hi, I am Can.","Hello! I'm Can.","Hello, I'm Can.","Hello! I am Can.","Hello, I am Can."],"\"Ben ...\" = I'm ..."),
  mc("Sabah 9'da öğretmeninizi selamlıyorsunuz:",["Good morning!","Good evening!","Goodbye!"],0,"Sabah selamı: Good morning."),
 ],
 {"kind":"speaking","task":speak("Kendinizi tanıtın: selam verin ve adınızı söyleyin.","Hello! My name is Deniz. Nice to meet you.",
   ["Bir selamlaşma kelimesi kullandı (Hello/Hi/Good morning)","Adını I'm ya da My name is ile söyledi","Nice to meet you dedi"])},
 warmup={"source":"none","note":"İlk ders, tekrar edilecek kart yok."})

# ---------------- Ders 2: Ben ve sen ----------------
lesson("Ben, sen, o","\"to be\" fiiliyle kendimi ve başkalarını anlatabilirim.",
 {"kind":"dialogue","title":"Sınıfta","lines":[
   {"speaker":"Deniz","text":"Ali, this is Mia. She's my friend."},
   {"speaker":"Ali","text":"Hi, Mia! I'm Ali."},
   {"speaker":"Mia","text":"Hi, Ali! Are you a student here?"},
   {"speaker":"Ali","text":"Yes, I am. Deniz and I are classmates."},
   {"speaker":"Mia","text":"Great! And who's he?"},
   {"speaker":"Deniz","text":"He's Mr Brown. He's our teacher."}],
  "questions":[
   mc("Who is Mia?",["Deniz's teacher","Deniz's friend","Ali's sister"],1,"Deniz \"She's my friend.\" diyor."),
   mc("Who is Mr Brown?",["A student","A teacher","Mia's friend"],1,"\"He's our teacher.\""),
  ]},
 {"explanation":"**to be** fiili Türkçedeki \"-im, -sin, -dir\" eklerinin karşılığıdır.\n\n| Özne | to be | Kısa hali |\n|---|---|---|\n| I | am | I'm |\n| you | are | you're |\n| he / she / it | is | he's / she's / it's |\n| we | are | we're |\n| they | are | they're |\n\n**he** erkek, **she** kadın, **it** ise eşya ve hayvanlar için kullanılır. Türkçedeki \"o\" İngilizcede üçe ayrılır.",
  "examples":[{"en":"I'm a student.","tr":"Ben öğrenciyim."},{"en":"She's my friend.","tr":"O benim arkadaşım."},{"en":"It's a book.","tr":"O bir kitap."},{"en":"They're teachers.","tr":"Onlar öğretmen."}],
  "turkishNote":"Türkçede \"Ben öğrenciyim\" derken ayrı bir fiil yoktur. İngilizcede ise am/is/are mutlaka gerekir. \"I student\" yanlıştır, doğrusu \"I'm a student\". Tek bir meslek ya da rol söylerken \"a\" ekleriz."},
 [
  match([("I","am"),("she","is"),("they","are"),("you","are"),("it","is")],"I → am; he/she/it → is; you/we/they → are."),
  gap("She ___ my friend.",["is"],"she → is"),
  gap("We ___ students.",["are"],"we → are"),
  gap("I ___ a teacher.",["am"],"I → am"),
  mc("Mr Brown is a teacher. ___ is from London.",["She","He","It"],1,"Mr (Bay) bir erkek, bu yüzden He."),
  mc("This is my phone. ___ is new.",["He","She","It"],2,"Eşyalar için it kullanılır."),
  mc("Hangisi doğru?",["I student.","I'm a student.","I'm student."],1,"to be fiili (am) ve tekil meslekte \"a\" gerekir.",{"0":"Fiil eksik! İngilizcede \"am\" olmadan cümle kurulmaz.","2":"Tek kişiden bahsederken meslekten önce \"a\" gelir."}),
  order(["are","They","my","friends"],"They are my friends.","Özne + to be + geri kalanı.","Onlar benim arkadaşlarım."),
  typ("Kısaltın: \"They are\"",["They're","they're"],"they + are = they're"),
  listen("This is Ken. He's from Japan. He's a student.","Ken kim?",["Bir öğretmen","Bir öğrenci","Bir doktor"],1,"\"He's a student.\""),
 ],
 {"kind":"writing","task":write("Bir arkadaşınızı 2–3 cümleyle tanıtın.","This is Selin. She's my friend. She's a teacher.",
   ["Arkadaşını This is ile tanıttı","He/She doğru seçildi","is doğru kullanıldı","Meslekten önce a/an var"])})

# ---------------- Ders 3: Nerelisin? ----------------
lesson("Nerelisin?","Nereli olduğumu söyleyip başkalarına sorabilirim.",
 {"kind":"dialogue","title":"Dil okulunda","lines":[
   {"speaker":"Lucas","text":"Hi, I'm Lucas. Where are you from?"},
   {"speaker":"Deniz","text":"I'm from Turkey. I'm from Izmir. And you?"},
   {"speaker":"Lucas","text":"I'm from Brazil. I'm Brazilian."},
   {"speaker":"Deniz","text":"Cool! And where's Yuki from?"},
   {"speaker":"Lucas","text":"She's from Japan. She's Japanese."}],
  "questions":[
   mc("Where is Lucas from?",["Spain","Brazil","Japan"],1,"\"I'm from Brazil.\""),
   mc("What nationality is Yuki?",["Japanese","Chinese","Turkish"],0,"\"She's Japanese.\""),
  ]},
 {"explanation":"Nereli olduğunu sormak: **Where are you from?**\n\nCevap vermenin iki yolu var:\n\n- **I'm from** + ülke → I'm from Turkey.\n- **I'm** + milliyet → I'm Turkish.\n\nBaşkası için: **Where is he/she from?** → **He's/She's from Spain.**",
  "examples":[{"en":"Where are you from?","tr":"Nerelisin?"},{"en":"I'm from Turkey.","tr":"Türkiye'denim."},{"en":"She's Spanish.","tr":"O İspanyol."}],
  "turkishNote":"Ülke ve milliyet isimleri her zaman büyük harfle başlar: Turkish, English. Ayrıca \"I'm from Turkish\" yanlıştır. \"from\" ülkeyle (Turkey), milliyet ise \"from\" olmadan (I'm Turkish) kullanılır."},
 [
  match([("Turkey","Turkish"),("Germany","German"),("Spain","Spanish"),("Japan","Japanese"),("Brazil","Brazilian")],"Ülke → milliyet"),
  mc("Hangisi doğru?",["I'm from Turkish.","I'm from Turkey.","I'm Turkey."],1,"from + ülke (Turkey). Milliyet ise from olmadan kullanılır: I'm Turkish.",{"0":"\"from\" ülkeyle kullanılır: from Turkey.","2":"Ülke adıyla \"from\" gerekir: I'm from Turkey."}),
  gap("Where ___ you from?",["are"],"you → are"),
  gap("Hans is ___ Germany.",["from"],"Ülkeden önce from gelir."),
  gap("Carmen is from Spain. She's ___.",["Spanish"],"Spain → Spanish"),
  order(["is","Where","from","she","?"],"Where is she from?","Soru kelimesi + is + özne + from?","O nereli?"),
  mc("They're from the USA. They're ___.",["English","American","Americans from"],1,"the USA → American"),
  listen("Hello, I'm Pierre. I'm from France. I'm French.","Pierre nereli?",["İngiltere","Fransa","İspanya"],1,"\"I'm from France.\""),
  typ("İngilizce yazın: \"Türkiye'denim.\"",["I'm from Turkey.","I am from Turkey.","I'm from Turkey","I am from Turkey","I'm from Türkiye.","I am from Türkiye.","I'm from Türkiye","I am from Türkiye"],"I'm from + ülke"),
  mc("Hangisi yazım açısından doğru?",["I'm turkish.","I'm Turkish.","I'm TURKISH."],1,"Milliyetler büyük harfle başlar."),
 ],
 {"kind":"speaking","task":speak("JAI size \"Where are you from?\" diye soruyor. Ülkenizi ve şehrinizi söyleyin.","I'm from Turkey. I'm from Ankara. I'm Turkish.",
   ["I'm from + ülke yapısını kullandı","Milliyeti doğru söyledi","Telaffuz anlaşılır"])})

# ---------------- Ders 4: Sayılar ve yaş ----------------
lesson("Kaç yaşındasın?","0–20 arası sayıları kullanıp yaşımı söyleyebilirim.",
 {"kind":"dialogue","title":"Kayıt masası","lines":[
   {"speaker":"Receptionist","text":"Hello! What's your name, please?"},
   {"speaker":"Elif","text":"Elif Kaya."},
   {"speaker":"Receptionist","text":"How old are you, Elif?"},
   {"speaker":"Elif","text":"I'm nineteen."},
   {"speaker":"Receptionist","text":"And what's your phone number?"},
   {"speaker":"Elif","text":"It's five-three-two, four-one-eight, seven-seven-zero-six."}],
  "questions":[
   mc("How old is Elif?",["9","19","90"],1,"\"I'm nineteen.\" = 19"),
   mc("Elif's phone number begins with…",["532","523","352"],0,"five-three-two = 532"),
  ]},
 {"explanation":"**Sayılar:** 0 zero, 1 one, 2 two, 3 three, 4 four, 5 five, 6 six, 7 seven, 8 eight, 9 nine, 10 ten, 11 eleven, 12 twelve, 13 thirteen, 14 fourteen, 15 fifteen, 16 sixteen, 17 seventeen, 18 eighteen, 19 nineteen, 20 twenty\n\nYaş sormak: **How old are you?**\nCevap: **I'm 25.** ya da **I'm 25 years old.**\n\nTelefon numaraları rakam rakam okunur. 0 için \"zero\" ya da \"oh\" denir. Yan yana iki aynı rakam için \"double\" da kullanılabilir: 77 = double seven.",
  "examples":[{"en":"How old are you?","tr":"Kaç yaşındasın?"},{"en":"I'm 19.","tr":"19 yaşındayım."},{"en":"He's twelve years old.","tr":"O on iki yaşında."}],
  "turkishNote":"İngilizcede yaş \"have\" ile değil, \"be\" ile söylenir. \"I have 25 years\" yanlıştır, doğrusu \"I'm 25\". \"I'm 25 years\" da eksiktir; ya \"I'm 25\" ya da \"I'm 25 years old\" deyin."},
 [
  match([("13","thirteen"),("15","fifteen"),("12","twelve"),("20","twenty"),("8","eight")],"Sayıları eşleştirin. -teen ile biten sayılar 13–19 arasıdır."),
  mc("\"Eleven\" kaçtır?",["7","11","12"],1,"eleven = 11"),
  mc("Hangisi doğru?",["I have 20 years.","I'm 20 years.","I'm 20."],2,"Yaş be ile söylenir: I'm 20 / I'm 20 years old.",{"0":"Yaş \"have\" ile söylenmez. I'm 20 deyin.","1":"\"years\" kullanırsanız sonuna \"old\" ekleyin: I'm 20 years old."}),
  gap("How ___ are you?",["old"],"Yaş sorusu: How old...?"),
  gap("She ___ seventeen.",["is"],"she → is"),
  listen("I'm fourteen years old.","Konuşan kaç yaşında?",["4","14","40"],1,"fourteen = 14 (-teen)"),
  listen("My number is zero-five-four-four, six-one-two.","Numara hangisi?",["0544 612","0545 612","0544 621"],0,"zero-five-four-four, six-one-two"),
  typ("Rakamla yazın: \"sixteen\"",["16"],"sixteen = 16"),
  typ("Yazıyla yazın: 18",["eighteen","Eighteen"],"18 = eighteen. Dikkat: \"eightteen\" değil, tek t ile yazılır."),
  order(["you","old","How","are","?"],"How old are you?","How old + are + you?","Kaç yaşındasın?"),
 ],
 {"kind":"speaking","task":speak("Adınızı, nereli olduğunuzu ve yaşınızı söyleyin.","Hi, I'm Deniz. I'm from Turkey. I'm twenty-three years old.",
   ["Adını söyledi","Nereli olduğunu söyledi","Yaşı be ile söyledi (I'm ...)","Sayıları doğru telaffuz etti"])})

# ---------------- Ders 5: Soru ve olumsuz ----------------
lesson("Evet, öyleyim. Hayır, değilim.","\"to be\" ile soru sorup olumsuz cevap verebilirim.",
 {"kind":"dialogue","title":"Yanlış tahmin","lines":[
   {"speaker":"Tom","text":"Are you Spanish?"},
   {"speaker":"Deniz","text":"No, I'm not. I'm Turkish."},
   {"speaker":"Tom","text":"Oh, sorry! Is Ali Turkish, too?"},
   {"speaker":"Deniz","text":"Yes, he is. We're from Izmir."},
   {"speaker":"Tom","text":"Are Mia and Yuki from Japan?"},
   {"speaker":"Deniz","text":"No, they aren't. Yuki is from Japan, but Mia isn't. She's from England."}],
  "questions":[
   mc("What nationality is Deniz?",["Spanish","Turkish","English"],1,"\"No, I'm not. I'm Turkish.\""),
   mc("Where is Mia from?",["Japan","England","Turkey"],1,"\"She's from England.\""),
  ]},
 {"explanation":"**Soru:** to be fiili öznenin önüne geçer.\n\n- You are Turkish. → **Are you** Turkish?\n- He is a teacher. → **Is he** a teacher?\n\n**Olumsuz:** to be fiilinden sonra **not** gelir.\n\n- I am not → **I'm not**\n- is not → **isn't**\n- are not → **aren't**\n\n**Kısa cevaplar:**\n\n- Yes, I am. / No, I'm not.\n- Yes, she is. / No, she isn't.\n- Yes, they are. / No, they aren't.",
  "examples":[{"en":"Are you a student? – Yes, I am.","tr":"Öğrenci misin? – Evet."},{"en":"Is this your bag? – No, it isn't.","tr":"Bu senin çantan mı? – Hayır."},{"en":"We aren't from London.","tr":"Biz Londralı değiliz."}],
  "turkishNote":"Olumlu kısa cevaplarda kısaltma yapılmaz. \"Yes, I'm.\" yanlıştır, doğrusu \"Yes, I am.\" Olumsuzda ise kısaltma doğaldır: No, I'm not. Ayrıca \"I amn't\" diye bir kısaltma yoktur."},
 [
  mc("\"Are you a teacher?\" Siz öğrencisiniz. Cevabınız:",["Yes, I am.","No, I'm not.","No, I amn't."],1,"Öğretmen değilsiniz, yani No, I'm not.",{"2":"\"amn't\" diye bir kısaltma yok. No, I'm not deyin."}),
  mc("Hangisi doğru?",["Yes, I'm.","Yes, I am."],1,"Olumlu kısa cevapta kısaltma yapılmaz."),
  gap("___ she from Spain? – Yes, she is.",["Is"],"she → is, soruda başa gelir."),
  gap("They ___ from England. They're from the USA.",["aren't","are not"],"Olumsuz: are not = aren't"),
  gap("He ___ a student. He's a teacher.",["isn't","is not"],"Olumsuz: is not = isn't"),
  order(["you","Are","Turkish","?"],"Are you Turkish?","Soruda to be başa gelir.","Türk müsün?"),
  order(["not","I'm","English"],"I'm not English.","Olumsuz: I'm + not","İngiliz değilim."),
  mc("\"Is Ali from Izmir?\" (Ali İzmirli.)",["Yes, he is.","Yes, he's.","Yes, Ali is it."],0,"Kısa cevap: Yes, he is."),
  listen("Is Emma a teacher? Yes, she is. Is she from the USA? No, she isn't. She's from England.","Emma nereli?",["ABD","İngiltere","İspanya"],1,"\"She's from England.\""),
  typ("İngilizce yazın: \"Biz öğrenci değiliz.\"",["We aren't students.","We are not students.","We're not students.","We aren't students","We are not students","We're not students"],"we + aren't + students (çoğul olduğu için a yok)"),
 ],
 {"kind":"speaking","task":speak("JAI size 3 evet/hayır sorusu soracak (örneğin \"Are you from Spain?\"). Kısa cevaplarla yanıtlayın ve doğru bilgiyi ekleyin.","No, I'm not. I'm from Turkey.",
   ["Kısa cevap biçimi doğru (Yes, I am / No, I'm not)","Olumlu kısa cevapta kısaltma yok","Doğru bilgiyi tam cümleyle ekledi"])})

# ---------------- Ünite sonu testi ----------------
test = [
 mc("Akşam 19:00'da komşunuzla karşılaşıyorsunuz:",["Good night!","Good evening!","Good morning!"],1,"Karşılaşırken akşam selamı: Good evening."),
 mc("___ name is Can.",["I","My","Me"],1,"Benim adım = My name"),
 gap("Nice to meet you. – Nice to meet you, ___.",["too"],"Karşılık verirken too eklenir."),
 gap("You ___ my best friend.",["are"],"you → are"),
 mc("This is my sister. ___ is a doctor.",["He","She","It"],1,"Kız kardeş → she"),
 mc("Hangisi doğru?",["I'm a student.","I student.","I'm student."],0,"I'm + a + meslek"),
 mc("Hangisi doğru?",["She's from Spanish.","She's from Spain.","She from Spain."],1,"from + ülke, ve is gerekli."),
 gap("Yuki is from Japan. She's ___.",["Japanese"],"Japan → Japanese"),
 order(["from","Where","they","are","?"],"Where are they from?","Where + are + they + from?","Onlar nereli?"),
 mc("Hangisi doğru?",["I have 30 years.","I'm 30.","I'm 30 years."],1,"Yaş be ile: I'm 30 (years old)."),
 typ("Yazıyla yazın: 15",["fifteen","Fifteen"],"15 = fifteen"),
 listen("Hi, I'm Marco. I'm twenty. I'm from Italy.","Marco kaç yaşında?",["12","20","22"],1,"twenty = 20"),
 mc("\"Are you from Ankara?\" (İstanbulsunuz.)",["Yes, I am.","No, I'm not.","No, I amn't."],1,"No, I'm not."),
 gap("My parents ___ teachers. They're doctors.",["aren't","are not"],"Olumsuz çoğul: aren't"),
 write("Kendinizi 4 cümleyle tanıtın: adınız, nereli olduğunuz, yaşınız ve mesleğiniz/okulunuz.","Hi! My name is Elif. I'm from Turkey. I'm nineteen years old. I'm a student.",
   ["Selamlaşma ve isim","from + ülke","Yaş be ile","Meslekte a/an","Büyük harf ve noktalama doğru"]),
]
for i,q in enumerate(test): q["id"]=f"{U}-t{i+1:02d}"

unit = {"id":U,"level":"A1","number":1,"title":"Merhaba!","titleEn":"Hello!",
 "canDo":"Kendimi tanıtabilirim: adımı, nereli olduğumu ve yaşımı söyleyebilir, başkalarına aynı soruları sorabilirim.",
 "grammar":["to be: am / is / are","özne zamirleri","to be: soru, olumsuz, kısa cevaplar"],
 "vocabularyThemes":["selamlaşma","ülkeler ve milliyetler","sayılar 0–20"],
 "liveClass":{"title":"Tanışma partisi","goal":"Öğrenciler eşleşip birbirine ad, ülke/şehir ve yaş sorar, sonra eşini gruba tanıtır.","durationMinutes":45},
 "vocabulary":vocab,"lessons":lessons,"unitTest":{"passPercent":80,"questions":test}}

# ---------- validation ----------
ids=set()
def check(ex, where):
    assert ex["id"] not in ids, ex["id"]; ids.add(ex["id"])
    t=ex["type"]
    if t in("multipleChoice","listening"):
        assert 0<=ex["answerIndex"]<len(ex["options"]), where
        assert len(set(ex["options"]))==len(ex["options"]), where
    if t=="gapFill": assert ex["text"].count("___")==1 and ex["answers"], where
    if t=="ordering": assert sorted(ex["answer"].replace("?"," ?").replace("."," .").split())==sorted(ex["words"]+([] if ex["answer"][-1] not in ".?" or ex["answer"][-1] in ex["words"] else [ex["answer"][-1]])), (where, ex)
    if t=="matching":
        assert len({p['left'] for p in ex["pairs"]})==len(ex["pairs"]), where
for l in lessons:
    for q in l["discover"]["questions"]+l["practice"]: check(q,l["id"])
for q in test: check(q,"test")
assert len(test)==15
json.dump(unit, open(sys.argv[1],"w"), ensure_ascii=False, indent=2)
print("ok", len(lessons), sum(len(l["practice"]) for l in lessons), len(vocab), len(test))

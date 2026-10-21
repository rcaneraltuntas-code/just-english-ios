import json, sys
G,V,R="grammar","vocabulary","reading"
items=[]
def add(level, skill, prompt, options, answer, expl, passage=None):
    n=sum(1 for i in items if i["level"]==level)+1
    d={"id":f"pl-{level.lower()}-{n:02d}","level":level,"skill":skill}
    if passage: d["passage"]=passage
    d.update(prompt=prompt, options=options, answerIndex=answer, explanation=expl)
    items.append(d)

# ---------- A1 ----------
add("A1",G,"My sister ___ a teacher.",["is","are","am","be"],0,
 "Tekil üçüncü şahıs (my sister = she) ile \"to be\" fiili \"is\" olur.")
add("A1",V,"Which word is a day of the week?",["March","Thursday","Summer","Morning"],1,
 "Thursday (perşembe) haftanın bir günüdür. March bir ay, summer bir mevsim, morning ise günün bir bölümüdür.")
add("A1",R,"Where does Tom work?",["In a school","In a hospital","In a shop","At home"],1,
 "Metinde \"I work in a hospital near my flat\" deniyor. Tom bir hemşire ve hastanede çalışıyor.",
 passage="Hi! My name is Tom. I am 28 years old and I live in Izmir. I am a nurse. I work in a hospital near my flat. I start work at 7 o'clock in the morning.")
add("A1",G,"___ you like coffee?",["Are","Is","Do","Does"],2,
 "Geniş zamanda \"you\" ile soru yardımcı fiil \"do\" ile kurulur: Do you like...? \"Like\" bir eylem olduğu için \"are\" kullanılmaz.")
add("A1",V,"I'm hungry. I want to ___ something.",["drink","eat","sleep","wear"],1,
 "Aç olan biri bir şey yemek ister: eat. Drink içmek, sleep uyumak, wear giymek demektir.")
add("A1",R,"What time does Tom start work?",["6 o'clock","7 o'clock","8 o'clock","9 o'clock"],1,
 "Metnin son cümlesi: \"I start work at 7 o'clock in the morning.\"",
 passage="Hi! My name is Tom. I am 28 years old and I live in Izmir. I am a nurse. I work in a hospital near my flat. I start work at 7 o'clock in the morning.")
add("A1",G,"There ___ two books on the table.",["is","are","has","have"],1,
 "\"There is/are\" yapısında çoğul isimle (two books) \"are\" kullanılır. Türkçedeki \"var\" anlamını verir; \"have\" kullanılmaz.")
add("A1",V,"The opposite of \"cheap\" is ___.",["expensive","small","new","easy"],0,
 "Cheap (ucuz) kelimesinin zıttı expensive (pahalı) olur.")

# ---------- A2 ----------
add("A2",G,"Yesterday we ___ to the cinema.",["go","goes","went","have gone"],2,
 "\"Yesterday\" geçmişte bitmiş bir zamanı gösterir, bu yüzden simple past kullanılır: go → went (düzensiz fiil). Bitmiş bir zaman ifadesiyle present perfect kullanılmaz.")
add("A2",V,"Can you ___ me the salt, please?",["pass","borrow","take","bring up"],0,
 "Sofrada bir şeyi uzatmak için \"pass\" kullanılır: Can you pass me the salt?")
add("A2",R,"Why did Elif take a taxi?",["She was late.","It was raining.","The bus didn't come.","She was tired."],2,
 "Metinde otobüsün hiç gelmediği (\"the bus never came\") söyleniyor. Elif bu yüzden taksiye bindi.",
 passage="Last Monday Elif waited at the bus stop for twenty minutes, but the bus never came. She didn't want to be late for her job interview, so she took a taxi. The interview went well, and the company called her two days later.")
add("A2",G,"This bag is ___ than that one.",["heavy","heavier","more heavy","heaviest"],1,
 "\"Than\" karşılaştırma yapar. \"-y\" ile biten tek/iki heceli sıfatlarda y → i olur ve -er eklenir: heavy → heavier.")
add("A2",V,"I'm going to the ___ to buy some bread.",["bakery","library","pharmacy","garage"],0,
 "Ekmek fırından (bakery) alınır. Library kütüphane, pharmacy eczane, garage ise garaj/oto tamirci demektir.")
add("A2",R,"When did the company call Elif?",["On Monday","The same day","Two days after the interview","A week later"],2,
 "Son cümle: \"the company called her two days later.\"",
 passage="Last Monday Elif waited at the bus stop for twenty minutes, but the bus never came. She didn't want to be late for her job interview, so she took a taxi. The interview went well, and the company called her two days later.")
add("A2",G,"I ___ TV when the phone rang.",["watched","was watching","am watching","watch"],1,
 "Devam eden bir eylem (TV izlemek) başka kısa bir eylemle (telefon çaldı) kesildiğinde past continuous kullanılır: was watching.")
add("A2",V,"My flight was ___ because of the snow, so I waited three hours.",["delayed","missed","landed","booked"],0,
 "Delayed \"rötar yaptı / ertelendi\" demektir. Kar yüzünden üç saat beklemek bu anlama uyar.")

# ---------- B1 ----------
add("B1",G,"I've lived in Ankara ___ 2019.",["for","since","from","during"],1,
 "\"Since\" bir başlangıç noktasıyla (2019) kullanılır, \"for\" ise süreyle (for five years). Türkçedeki \"-den beri\" anlamı since ile verilir.")
add("B1",V,"Could you ___ the music down? I'm trying to study.",["turn","put","take","get"],0,
 "\"Turn down\" sesi kısmak demektir. \"Turn up\" ise sesi açmaktır.")
add("B1",R,"What is the main reason the writer gives for learning a language in the morning?",
 ["It is easier to find a teacher.","The brain is more rested.","There is less noise outside.","Classes are cheaper."],1,
 "Metin sabahları beynin dinlenmiş olduğunu ve yeni bilgiyi daha kolay sakladığını söylüyor.",
 passage="Many people prefer to study a new language in the evening, after work. However, research suggests that the morning may be a better time. After a good night's sleep, the brain is rested and stores new information more easily. Even fifteen minutes before breakfast can make a real difference if you do it every day.")
add("B1",G,"If it ___ tomorrow, we'll cancel the picnic.",["will rain","rains","rained","would rain"],1,
 "Birinci tip koşul cümlesinde \"if\" kısmında simple present kullanılır: If it rains..., we'll... \"If\" kısmında \"will\" kullanılmaz.")
add("B1",V,"She's very ___; she always tells the truth.",["honest","proud","polite","shy"],0,
 "Her zaman doğruyu söyleyen biri honest (dürüst) olur. Polite kibar, proud gururlu, shy utangaç demektir.")
add("B1",R,"According to the text, what is the key to success?",["Studying for hours at night","Studying a little every day","Eating breakfast first","Finding a quiet room"],1,
 "Son cümle her gün kısa süre çalışmanın (\"fifteen minutes... every day\") fark yarattığını söylüyor.",
 passage="Many people prefer to study a new language in the evening, after work. However, research suggests that the morning may be a better time. After a good night's sleep, the brain is rested and stores new information more easily. Even fifteen minutes before breakfast can make a real difference if you do it every day.")
add("B1",G,"The museum ___ in 1890.",["built","was built","has built","is building"],1,
 "Müze kendini inşa etmez, birileri onu inşa eder. Bu yüzden edilgen (passive) yapı gerekir: was built.")
add("B1",V,"I'm really looking forward ___ you next week.",["to see","to seeing","seeing","for seeing"],1,
 "\"Look forward to\" kalıbında \"to\" bir edattır, bu yüzden ardından fiil -ing alır: looking forward to seeing.")

# ---------- B2 ----------
add("B2",G,"By the time we arrived, the film ___.",["already started","has already started","had already started","was already starting"],2,
 "Geçmişteki bir andan (we arrived) daha önce tamamlanmış bir eylem için past perfect kullanılır: had already started.")
add("B2",V,"The meeting was ___ until next Friday because the manager was ill.",["put off","put out","put up","put on"],0,
 "\"Put off\" ertelemek demektir. Put out söndürmek, put up misafir etmek/asmak, put on giymek anlamına gelir.")
add("B2",R,"What does the writer suggest about remote work?",
 ["It suits everyone equally.","Its benefits depend on the person and the job.","It always reduces productivity.","Companies should ban it."],1,
 "Metin uzaktan çalışmanın bazıları için harika, bazıları için yalnızlaştırıcı olduğunu söylüyor. Yani faydası kişiye ve işe göre değişiyor.",
 passage="When offices closed in 2020, many predicted that remote work would be a temporary inconvenience. Instead, it has reshaped how millions of people work. For some, the lack of a commute has meant more time with family and fewer distractions. Others, however, report feeling isolated and find it hard to separate their job from their private life. The truth, it seems, is that remote work is neither a miracle nor a disaster; its value depends largely on the individual and the nature of the work.")
add("B2",G,"I wish I ___ more time to travel when I was younger.",["have","had","had had","would have"],2,
 "Geçmişe dair pişmanlıkta \"wish\" + past perfect kullanılır: I wish I had had more time. (Keşke daha fazla zamanım olsaydı.)")
add("B2",V,"Despite the ___ weather, thousands of fans came to the concert.",["appalling","appealing","approving","applying"],0,
 "Appalling \"berbat, korkunç\" demektir. \"Despite\" ile verilen zıtlık, havanın kötü olduğunu gösterir. Appealing ise \"çekici\" anlamına gelir.")
add("B2",R,"The word \"isolated\" in the text is closest in meaning to:",["lonely and cut off","busy and stressed","bored and tired","free and relaxed"],0,
 "Isolated, insanlardan kopuk ve yalnız hissetmek demektir.",
 passage="When offices closed in 2020, many predicted that remote work would be a temporary inconvenience. Instead, it has reshaped how millions of people work. For some, the lack of a commute has meant more time with family and fewer distractions. Others, however, report feeling isolated and find it hard to separate their job from their private life. The truth, it seems, is that remote work is neither a miracle nor a disaster; its value depends largely on the individual and the nature of the work.")
add("B2",G,"He denied ___ the window.",["to break","breaking","break","to have broke"],1,
 "\"Deny\" fiilinden sonra fiil -ing alır: denied breaking. Aynı şekilde avoid, admit ve suggest de -ing alır.")
add("B2",V,"We need to ___ a decision before the end of the day.",["do","make","take place","get"],1,
 "İngilizcede karar \"make\" ile kurulur: make a decision. (İngiliz İngilizcesinde \"take a decision\" da kullanılır, ancak seçeneklerde yalnızca make var.)")

# ---------- C1 ----------
add("C1",G,"___ had I sat down than the phone rang.",["Hardly","No sooner","Barely","Scarcely"],1,
 "\"No sooner ... than\" kalıbında devrik yapı kullanılır: No sooner had I sat down than... Hardly, scarcely ve barely ise \"when\" ile kullanılır.")
add("C1",V,"The new policy has been widely criticised, but the government remains ___ that it will work.",["adamant","adverse","ambiguous","apathetic"],0,
 "Adamant, eleştirilere rağmen fikrinden dönmeyen, \"kesin kararlı\" demektir. Adverse olumsuz, ambiguous belirsiz, apathetic ise ilgisiz anlamına gelir.")
add("C1",R,"What is the writer's main point?",
 ["Multitasking makes people more efficient.","People who think they multitask well are often the worst at it.","Only young people can multitask.","Technology has solved the problem of distraction."],1,
 "Metin, çoklu görevde iyi olduğunu düşünenlerin testlerde genellikle en kötü sonucu aldığını vurguluyor.",
 passage="We like to think of ourselves as accomplished multitaskers, answering emails while listening in on a conference call. Yet a growing body of evidence suggests that what we call multitasking is in fact rapid task-switching, and that each switch carries a hidden cost in attention and accuracy. Ironically, studies have found that those most confident in their ability to juggle tasks tend to perform worst when tested, perhaps precisely because their confidence leads them to attempt it more often.")
add("C1",G,"It's high time the council ___ something about the traffic.",["does","did","has done","will do"],1,
 "\"It's high time\" kalıbından sonra şimdiki/gelecek zamanı kastetsek de past simple kullanılır: It's high time they did something.")
add("C1",V,"Her argument didn't ___ water; there were too many gaps in the logic.",["hold","keep","carry","bear"],0,
 "\"Not hold water\" bir deyimdir ve \"tutarlı olmamak, ikna edici olmamak\" demektir.")
add("C1",R,"According to the text, why might confident multitaskers perform badly?",
 ["They are less intelligent.","They multitask more often because of their confidence.","They use older technology.","They never practise."],1,
 "Son cümle: \"perhaps precisely because their confidence leads them to attempt it more often.\"",
 passage="We like to think of ourselves as accomplished multitaskers, answering emails while listening in on a conference call. Yet a growing body of evidence suggests that what we call multitasking is in fact rapid task-switching, and that each switch carries a hidden cost in attention and accuracy. Ironically, studies have found that those most confident in their ability to juggle tasks tend to perform worst when tested, perhaps precisely because their confidence leads them to attempt it more often.")
add("C1",G,"Not only ___ late, but he also forgot the tickets.",["he arrived","did he arrive","he did arrive","arrived he"],1,
 "Cümle \"Not only\" ile başladığında devrik yapı gerekir: Not only did he arrive late...")
add("C1",V,"The CEO's speech was full of ___ promises that nobody really believed.",["hollow","hallowed","shallow-minded","hefty"],0,
 "Hollow promises \"içi boş vaatler\" demektir ve doğal bir eşdizimdir (collocation). Hallowed ise \"kutsal\" anlamına gelir.")

# ---------- C2 ----------
add("C2",G,"Were the government ___ the tax, there would be widespread protests.",["to raise","raising","raise","raised"],0,
 "\"Were ... to + fiil\" yapısı, \"if\" yerine kullanılan resmi ve devrik bir koşul cümlesidir: Were the government to raise... = If the government raised...")
add("C2",V,"His account of events was so ___ that even his supporters began to doubt him.",["implausible","impeccable","imperative","impervious"],0,
 "Implausible \"inanılması güç\" demektir. Destekçilerinin bile şüphelenmesi bu anlama uyar. Impeccable kusursuz, impervious ise etkilenmez anlamına gelir.")
add("C2",R,"What does the writer imply about the word \"literally\"?",
 ["Its new meaning should be banned.","Its shift in meaning is part of a normal linguistic process.","It has always meant \"figuratively\".","Dictionaries have refused to accept its new use."],1,
 "Yazar, dildeki değişimi \"canlı bir dilin işareti\" olarak görüyor. Kelimenin anlam kaymasını doğal bir süreç sayıyor.",
 passage="Purists bristle when they hear \"literally\" used to mean its very opposite, as in \"I literally died laughing\". Yet the history of English is littered with such reversals: \"nice\" once meant foolish, and \"awful\" meant worthy of awe. Lexicographers, whose job is to describe rather than prescribe, have duly recorded the intensifying sense of \"literally\". To lament the change is understandable; to imagine it can be reversed is to misunderstand what a living language is.")
add("C2",G,"Little ___ that his decision would change the course of the company.",["he knew","did he know","he did know","knew he"],1,
 "Olumsuz anlamlı \"Little\" cümle başına geldiğinde devrik yapı gerekir: Little did he know... (Hiç bilmiyordu ki...)")
add("C2",V,"The negotiations reached a(n) ___, with neither side willing to make concessions.",["impasse","epitome","outset","respite"],0,
 "Impasse \"çıkmaz\" demektir. İki tarafın da taviz vermemesi bu anlama uyar. Respite kısa bir mola, outset başlangıç demektir.")
add("C2",R,"Why does the writer mention \"nice\" and \"awful\"?",
 ["To show that English is becoming simpler","To give examples of words whose meanings have changed over time","To criticise lexicographers","To argue that old meanings are better"],1,
 "Bu iki kelime, anlamı zamanla tersine dönmüş kelimelere örnek olarak veriliyor.",
 passage="Purists bristle when they hear \"literally\" used to mean its very opposite, as in \"I literally died laughing\". Yet the history of English is littered with such reversals: \"nice\" once meant foolish, and \"awful\" meant worthy of awe. Lexicographers, whose job is to describe rather than prescribe, have duly recorded the intensifying sense of \"literally\". To lament the change is understandable; to imagine it can be reversed is to misunderstand what a living language is.")
add("C2",G,"So ___ was the storm that the ferry service was suspended for a week.",["severe","severely","severity","a severe"],0,
 "\"So + sıfat + was + özne + that\" devrik vurgu yapısıdır: So severe was the storm that... Burada bir sıfat gerekir.")
add("C2",V,"The minister's remarks were deliberately ___, allowing him to deny any specific commitment later.",["equivocal","unequivocal","eloquent","explicit"],0,
 "Equivocal \"bilerek muğlak bırakılmış\" demektir. Bu sayede bakan sonradan bir taahhütte bulunmadığını söyleyebilir. Unequivocal ve explicit ise tam tersine \"açık, net\" demektir.")

# validate
from collections import Counter
c=Counter(i["level"] for i in items); assert all(v==8 for v in c.values()), c
for i in items:
    assert 0<=i["answerIndex"]<len(i["options"]) and len(set(i["options"]))==len(i["options"]), i["id"]
json.dump(items, open(sys.argv[1],"w"), ensure_ascii=False, indent=2)
print(len(items), c)

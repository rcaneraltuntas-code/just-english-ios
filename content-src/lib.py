"""Ünite içeriği yazmak için ortak yardımcılar ve doğrulama.

Her ünite dosyası bir `Unit` oluşturur, derslerini ve testini ekler, sonra
`unit.save(sys.argv[1])` çağırır. Kaydetmeden önce tüm içerik doğrulanır;
bir hata varsa betik durur ve JSON yazılmaz.
"""
import json
import re


def mc(prompt, options, answer, why, wrong=None):
    d = {"type": "multipleChoice", "prompt": prompt, "options": options, "answerIndex": answer, "explanation": why}
    if wrong:
        d["wrongFeedback"] = {str(k): v for k, v in wrong.items()}
    return d


def gap(text, answers, why, hint=None):
    d = {"type": "gapFill", "text": text, "answers": answers, "explanation": why}
    if hint:
        d["hint"] = hint
    return d


def order(words, answer, why, tr=None):
    d = {"type": "ordering", "words": words, "answer": answer, "explanation": why}
    if tr:
        d["translation"] = tr
    return d


def match(pairs, why):
    return {"type": "matching", "pairs": [{"left": a, "right": b} for a, b in pairs], "explanation": why}


def typ(prompt, accepted, why):
    return {"type": "typeAnswer", "prompt": prompt, "accepted": accepted, "explanation": why}


def listen(audio, prompt, options, answer, why):
    return {"type": "listening", "audioText": audio, "prompt": prompt, "options": options,
            "answerIndex": answer, "explanation": why}


def speak(prompt, model, rubric):
    return {"type": "speaking", "prompt": prompt, "modelAnswer": model, "rubric": rubric}


def write(prompt, model, rubric):
    return {"type": "writing", "prompt": prompt, "modelAnswer": model, "rubric": rubric}


def variants(*sentences):
    """Yazarak cevaplarda kabul edilen biçimleri üretir: kısaltmalı/kısaltmasız, sondaki noktalı/noktasız."""
    contractions = [("I'm", "I am"), ("you're", "you are"), ("he's", "he is"), ("she's", "she is"),
                    ("it's", "it is"), ("we're", "we are"), ("they're", "they are"), ("isn't", "is not"),
                    ("aren't", "are not"), ("don't", "do not"), ("doesn't", "does not"), ("can't", "cannot"),
                    ("there's", "there is"), ("what's", "what is"), ("wasn't", "was not"), ("weren't", "were not"),
                    ("didn't", "did not"), ("I'd", "I would")]
    out = []
    for s in sentences:
        forms = {s}
        for short, long in contractions:
            for f in list(forms):
                for a, b in ((short, long), (short.capitalize(), long.capitalize())):
                    if a in f:
                        forms.add(f.replace(a, b))
        for f in list(forms):
            forms.add(f.rstrip(".!?"))
        out += sorted(forms - set(out), key=lambda x: (x != s, len(x)))
    return out


class Unit:
    def __init__(self, level, number, title, title_en, can_do, grammar, themes, live_class):
        self.id = f"{level.lower()}-u{number:02d}"
        self.data = {"id": self.id, "level": level, "number": number, "title": title, "titleEn": title_en,
                     "canDo": can_do, "grammar": grammar, "vocabularyThemes": themes,
                     "liveClass": live_class, "vocabulary": [], "lessons": [], "unitTest": None}

    def vocab(self, rows):
        """rows: (en, tr, example, example_tr, note|None)"""
        start = len(self.data["vocabulary"])
        for i, (en, tr, ex, ex_tr, note) in enumerate(rows):
            v = {"id": f"{self.id}-v{start + i + 1:02d}", "en": en, "tr": tr, "example": ex, "exampleTr": ex_tr}
            if note:
                v["note"] = note
            self.data["vocabulary"].append(v)

    def lesson(self, title, goal, discover, learn, practice, use, warmup=None):
        n = len(self.data["lessons"]) + 1
        lid = f"{self.id}-l{n}"
        for i, q in enumerate(discover["questions"]):
            q["id"] = f"{lid}-d{i + 1:02d}"
        for i, ex in enumerate(practice):
            ex["id"] = f"{lid}-p{i + 1:02d}"
        use["id"] = f"{lid}-use"
        self.data["lessons"].append({"id": lid, "number": n, "title": title, "goal": goal,
                                     "warmup": warmup or {"source": "review", "count": 6},
                                     "discover": discover, "learn": learn, "practice": practice, "use": use})

    def test(self, questions, pass_percent=80):
        for i, q in enumerate(questions):
            q["id"] = f"{self.id}-t{i + 1:02d}"
        self.data["unitTest"] = {"passPercent": pass_percent, "questions": questions}

    # ---------- doğrulama ----------
    def validate(self):
        d = self.data
        errors = []
        ids = set()

        def err(where, msg):
            errors.append(f"{where}: {msg}")

        def check(ex, where):
            if ex["id"] in ids:
                err(where, f"tekrar eden id {ex['id']}")
            ids.add(ex["id"])
            t = ex["type"]
            if t in ("multipleChoice", "listening"):
                if not 0 <= ex["answerIndex"] < len(ex["options"]):
                    err(where, "answerIndex aralık dışında")
                if len(set(ex["options"])) != len(ex["options"]):
                    err(where, "tekrar eden seçenek")
                for k in ex.get("wrongFeedback", {}):
                    if int(k) == ex["answerIndex"] or not 0 <= int(k) < len(ex["options"]):
                        err(where, f"wrongFeedback anahtarı geçersiz: {k}")
            elif t == "gapFill":
                if ex["text"].count("___") != 1:
                    err(where, "boşluk sayısı 1 değil")
                if not ex["answers"]:
                    err(where, "cevap yok")
            elif t == "ordering":
                tokens = re.findall(r"[\w'’-]+|[?.!,]", ex["answer"])
                words = ex["words"]
                # Nokta ve virgül kelime olarak verilmediyse otomatik eklenir.
                core = [w for w in tokens if w not in ".!," or w in words]
                if sorted(core) != sorted(words):
                    err(where, f"kelimeler cevapla uyuşmuyor: {words} / {ex['answer']}")
            elif t == "matching":
                if len({p["left"] for p in ex["pairs"]}) != len(ex["pairs"]):
                    err(where, "tekrar eden sol öğe")
                if len(ex["pairs"]) < 3:
                    err(where, "en az 3 çift")
            elif t == "typeAnswer":
                if not ex["accepted"]:
                    err(where, "kabul edilen cevap yok")
            elif t in ("speaking", "writing"):
                if len(ex["rubric"]) < 2:
                    err(where, "ölçüt az")
            else:
                err(where, f"bilinmeyen tür {t}")
            if t not in ("speaking", "writing") and not ex.get("explanation"):
                err(where, "açıklama yok")

        if not 15 <= len(d["vocabulary"]) <= 30:
            err("vocabulary", f"kart sayısı {len(d['vocabulary'])}")
        if len({v["en"] for v in d["vocabulary"]}) != len(d["vocabulary"]):
            err("vocabulary", "tekrar eden kelime")
        if len(d["lessons"]) != 5:
            err("lessons", f"ders sayısı {len(d['lessons'])}")
        for l in d["lessons"]:
            if not 8 <= len(l["practice"]) <= 12:
                err(l["id"], f"alıştırma sayısı {len(l['practice'])}")
            if len(l["discover"]["questions"]) < 2:
                err(l["id"], "keşfet sorusu az")
            for q in l["discover"]["questions"] + l["practice"] + [l["use"]["task"] | {"id": l["use"]["id"]}]:
                check(q, l["id"])
            kinds = {ex["type"] for ex in l["practice"]}
            if not {"typeAnswer", "ordering", "gapFill"} & kinds:
                err(l["id"], "üretim alıştırması yok (boşluk/sıralama/yazma)")
            if "listening" not in kinds:
                err(l["id"], "dinleme alıştırması yok")
        t = d["unitTest"]
        if not t or len(t["questions"]) != 15:
            err("unitTest", "15 soru olmalı")
        else:
            for q in t["questions"]:
                check(q, "unitTest")
        if errors:
            raise SystemExit("İçerik hataları:\n  " + "\n  ".join(errors))

    def save(self, path):
        self.validate()
        with open(path, "w") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)
        d = self.data
        print(f"ok {self.id}: {len(d['lessons'])} ders, "
              f"{sum(len(l['practice']) for l in d['lessons'])} alıştırma, "
              f"{len(d['vocabulary'])} kart, {len(d['unitTest']['questions'])} test sorusu")

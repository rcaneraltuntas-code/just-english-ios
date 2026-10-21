"""Bir ünite JSON'unu öğretmenlerin inceleyebileceği okunur Markdown'a çevirir.

Kullanım: python3 render_review.py ../JustEnglish/Resources/Content/a1-u01.json > a1-u01.md
"""
import json, sys

TYPES = {"multipleChoice": "Çoktan seçmeli", "gapFill": "Boşluk doldurma", "ordering": "Cümle kurma",
         "matching": "Eşleştirme", "typeAnswer": "Yazarak cevap", "listening": "Dinleme",
         "speaking": "Konuşma", "writing": "Yazma"}

def sentence(text):
    """Cümle sonuna, zaten noktalama yoksa nokta ekler."""
    return text if text[-1:] in ".?!" else text + "."

def exercise(n, ex):
    t = ex["type"]; head = f"{n}. *{TYPES[t]}*"
    if t in ("multipleChoice", "listening"):
        pre = f"(Ses: \"{ex['audioText']}\") " if t == "listening" else ""
        opts = " / ".join(f"**{o}**" if i == ex["answerIndex"] else o for i, o in enumerate(ex["options"]))
        return f"{head}: {pre}{ex['prompt']} → {sentence(opts) if not opts.endswith('**') else opts + '.'} {ex['explanation']}"
    if t == "gapFill":
        return f"{head}: {ex['text']} → **{' / '.join(ex['answers'])}**. {ex['explanation']}"
    if t == "ordering":
        return f"{head}: [{' · '.join(ex['words'])}] → **{ex['answer']}** {ex['explanation']}"
    if t == "matching":
        return f"{head}: " + ", ".join(f"{p['left']} = {p['right']}" for p in ex["pairs"]) + f". {ex['explanation']}"
    if t == "typeAnswer":
        extra = f" (+{len(ex['accepted']) - 1} kabul edilen varyant)" if len(ex["accepted"]) > 1 else ""
        return f"{head}: {ex['prompt']} → **{ex['accepted'][0]}**{extra}. {ex['explanation']}"
    if t in ("speaking", "writing"):
        return f"{head}: {ex['prompt']} Örnek: *{ex['modelAnswer']}* Ölçütler: {'; '.join(ex['rubric'])}."
    raise ValueError(t)

u = json.load(open(sys.argv[1]))
out = [f"# {u['level']} Ünite {u['number']}: {u['title']} ({u['titleEn']})", "",
       f"**Yapabilirim:** {u['canDo']}", "",
       f"**Dilbilgisi:** {', '.join(u['grammar'])} · **Kelime:** {', '.join(u['vocabularyThemes'])}", ""]
for l in u["lessons"]:
    d = l["discover"]
    out += [f"## Ders {l['number']}: {l['title']}", "", f"**Hedef:** {l['goal']}", "",
            f"### Keşfet: {d['title']}", ""]
    out += [f"- **{line['speaker']}:** {line['text']}" for line in d["lines"]]
    out += [""] + [exercise(i + 1, q) for i, q in enumerate(d["questions"])]
    out += ["", "### Öğren", "", l["learn"]["explanation"], "", "Örnekler: " +
            " · ".join(f"*{e['en']}* ({e['tr']})" for e in l["learn"]["examples"]), "",
            f"**Türkçe konuşanlar için not:** {l['learn']['turkishNote']}", "", "### Uygula", ""]
    out += [exercise(i + 1, ex) for i, ex in enumerate(l["practice"])]
    out += ["", "### Kullan", "", exercise(1, l["use"]["task"]), ""]
out += ["## Kelime kartları", "", "| İngilizce | Türkçe | Örnek | Not |", "| --- | --- | --- | --- |"]
out += [f"| {v['en']} | {v['tr']} | {v['example']} | {v.get('note', '')} |" for v in u["vocabulary"]]
out += ["", f"## Ünite sonu testi (geçme notu %{u['unitTest']['passPercent']})", ""]
out += [exercise(i + 1, q) for i, q in enumerate(u["unitTest"]["questions"])]
lc = u["liveClass"]
out += ["", f"## Canlı ders: {lc['title']} ({lc['durationMinutes']} dk)", "", lc["goal"]]
print("\n".join(out))

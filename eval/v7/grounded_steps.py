"""v7: write each verified step on its own, so no step from the action plan can be dropped.

v6 gave the model the whole action plan in one prompt and hoped it would include every
step; in 7 of 15 scenarios it did not (see eval/analysis_v2/hypothesis_checks_v2.md).
v7 keeps v6's retrieval, routing and action plan unchanged and only changes how the
answer is written:

- clarify route: return the router's question word for word (v6 sometimes reworded it).
- answer route with a plan: one short model call per plan action ("rewrite this one
  instruction as one step"), plus a short opening sentence and, when a retrieved
  sentence says how to tell it worked, one sentence about that. Then a fixed closing
  line telling the user what to do if the screen doesn't match.
- anything else (no plan, insufficient evidence): same single call as v6.

Every model-written piece is validated. If a piece fails (too long, a new URL or phone
number, a dropped button name, Simplified Chinese), it is replaced by text from the plan
or the source, so the answer never loses a verified step.

`generate` is any function messages -> text, so this file has no model dependency and
can be tested with a fake.
"""
import re

CLOSING = {
    "en": "If something on your screen doesn't match these steps, tell me what you see and I'll help.",
    "zh": "如果畫面和這些步驟不一樣，請告訴我您看到什麼，我再幫您。",
}
CLOSING_GENERAL = {  # for steps with no on-screen buttons, e.g. a scam phone call
    "en": "If anything is unclear, tell me and I'll help with the next step.",
    "zh": "如果有任何不清楚的地方，請告訴我，我再幫您。",
}
INTRO_FALLBACK = {"en": "Here's what to do:", "zh": "請照以下步驟做："}
LANG_NAME = {"en": "English", "zh": "Traditional Chinese (繁體中文)"}

CJK = re.compile(r"[一-鿿]")
URL = re.compile(r"(?:https?://\S+|\b[\w-]+(?:\.[\w-]+)+\.(?:com|gov|org|net|tw)\S*)", re.I)
NUMBER = re.compile(r"\d[\d-]{2,}")
CUE = re.compile(r"[^.。]*\b(?:confirm|checkmark|status icon|appears?|you(?:'ll| will) see|shows?)\b[^.。]*[.。]", re.I)
LABEL = re.compile(r"\b(?:[A-Z][\w&'-]*(?:\s+(?:[A-Z][\w&'-]*|to|of|and|on|in|&))*\s*)+")
# Common Simplified characters (the model produced 挂 in v6) and their Traditional forms.
S2T = str.maketrans('挂发说设这么们机账钱银话时后线应该对请开关电视简体问题过还没让给讯号码务处现户亲诈骗确认网购单断马门见车东长书买卖实动点种经证报联识读写记录钟无为会个来国学样帮页输选择显图册验际汇转额诉吗边里着将从于与万两几习乐听声灯热难欢爱宝区医药养险费资质级统络结绝继续维护软储档删盘键标准侧闭启讲诚归拨挡拦罚赔偿补贴价钮节邮递冲杀诱达优领奖获详细刚讨论调谁谢',
                    '掛發說設這麼們機帳錢銀話時後線應該對請開關電視簡體問題過還沒讓給訊號碼務處現戶親詐騙確認網購單斷馬門見車東長書買賣實動點種經證報聯識讀寫記錄鐘無為會個來國學樣幫頁輸選擇顯圖冊驗際匯轉額訴嗎邊裡著將從於與萬兩幾習樂聽聲燈熱難歡愛寶區醫藥養險費資質級統絡結絕繼續維護軟儲檔刪盤鍵標準側閉啟講誠歸撥擋攔罰賠償補貼價鈕節郵遞衝殺誘達優領獎獲詳細剛討論調誰謝')
STOP_LABELS = {"On", "If", "In", "The", "Do", "Open", "Tap", "Select", "Choose", "Enter", "Explain", "Check",
               "Hang", "Keep", "Ask", "Run", "Change", "Contact", "Report", "End", "Remove", "Disconnect",
               "Independently", "Give", "Use", "Turn", "Call", "Look", "Find", "Do not"}


def language(text):
    return "zh" if CJK.search(text) else "en"


def labels(instruction):
    """Button or menu names in an English plan instruction, e.g. 'Personal Hotspot', 'Allow Others to Join'.

    A name is a run of Capitalized words, joined only by 'to', 'of' or '&' when another
    Capitalized word follows. A verb that starts the sentence (Open, Tap, Check...) is dropped.
    """
    out = []
    for part in re.split(r"\s*>\s*|[,.;:()]", instruction):
        words = [w.split("/")[0] for w in part.split()]  # "Audio/microphone" -> "Audio"
        i = 0
        while i < len(words):
            if not words[i][:1].isupper():
                i += 1
                continue
            j, run = i, [words[i]]
            while j + 1 < len(words):
                nxt = words[j + 1]
                if nxt[:1].isupper():
                    run.append(nxt); j += 1
                elif nxt in ("to", "of", "&") and j + 2 < len(words) and words[j + 2][:1].isupper():
                    run += [nxt, words[j + 2]]; j += 2
                else:
                    break
            if i == 0 and run[0] in STOP_LABELS:
                run = run[1:]
            name = " ".join(run)
            if name and (len(run) > 1 or name in {"Settings", "Wi-Fi", "Speaker", "Bluetooth", "Zoom"}):
                out.append(name)
            i = j + 1
    return out


def clean(text):
    text = text.strip().strip('"').strip()
    text = re.sub(r"^\s*(?:\d+[.)]|[-*•])\s*", "", text)          # drop numbering the model added
    text = text.split("\n")[0].strip()                             # one step only
    return text.replace("\u2014", ", ").replace("\u2013", "-")


def validate(text, allowed_source, lang, required_labels=(), max_words=40):
    """Return a list of problems; empty means the piece can be used."""
    problems = []
    if not text:
        return ["empty"]
    size = len(text) if lang == "zh" else len(text.split())
    if size > (90 if lang == "zh" else max_words):
        problems.append("too long")
    for u in URL.findall(text):
        if u.lower().rstrip(".,") not in allowed_source.lower():
            problems.append(f"new web address {u}")
    for n in NUMBER.findall(text):
        if n not in allowed_source:
            problems.append(f"new number {n}")
    if lang == "en":
        for lab in required_labels:
            if lab.lower() not in text.lower():
                problems.append(f"dropped label {lab}")
        if CJK.search(text):
            problems.append("wrong language")
    elif not CJK.search(text):
        problems.append("wrong language")
    return problems


def step_messages(request, action, lang):
    system = ("You rewrite ONE instruction as ONE short step for an older adult who is not confident with "
              "technology. Use only the instruction and the source sentence. Keep button and menu names exactly. "
              "Do not add other steps, web addresses, or phone numbers that are not in them. "
              f"Write in {LANG_NAME[lang]}. Reply with the step only, no number, no introduction.")
    user = (f"The person asked: {request}\n\nInstruction: {action['instruction']}\n"
            f"Source sentence: {action.get('source_quote', '')}")
    return [{"role": "system", "content": system}, {"role": "user", "content": user}]


def intro_messages(request, lang):
    system = ("Write ONE short opening sentence (at most 20 words) for a reply to the person below. "
              "If they are being asked for money or access by a caller, say clearly not to go along with it. "
              "Otherwise say briefly that this can be done. Do not give any steps, web addresses or phone numbers. "
              f"Write in {LANG_NAME[lang]}. Reply with the sentence only.")
    return [{"role": "system", "content": system}, {"role": "user", "content": request}]


def confirm_messages(sentence, lang):
    system = ("Rewrite the source sentence as ONE short sentence telling an older adult how they will know it "
              f"worked. Use only what the sentence says. Write in {LANG_NAME[lang]}. Reply with the sentence only.")
    return [{"role": "system", "content": system}, {"role": "user", "content": sentence}]


def fallback_step(action, lang):
    """Text from the plan (English) or the official source sentence (Chinese) when the model's step fails."""
    if lang == "zh":
        return action.get("source_quote") or action["instruction"]
    text = re.sub(r"^Explain that\s+", "", action["instruction"])
    return text[0].upper() + text[1:]


def compose(intro, steps, confirm, lang, on_screen=True):
    unique = list(dict.fromkeys(steps))  # one source sentence can cover several actions; say it once
    body = "\n".join(f"{i}. {s}" for i, s in enumerate(unique, 1))
    closing = CLOSING[lang] if on_screen else CLOSING_GENERAL[lang]
    parts = [intro, body] + ([confirm] if confirm else []) + [closing]
    return "\n\n".join(p for p in parts if p)


def build_answer(plan_row, request, generate, v6_messages):
    """Return (response, check) for one scenario. `generate(messages, max_new_tokens)` -> text."""
    decision = plan_row.get("decision") or {}
    plan = plan_row.get("action_plan") or {}
    actions = plan.get("actions") or []
    lang = language(request)
    check = {"route": decision.get("mode"), "language": lang, "calls": 0, "steps": [], "fallbacks": 0}

    if decision.get("mode") == "clarify" and decision.get("question"):
        check["method"] = "router question, verbatim"
        return decision["question"].strip(), check
    if decision.get("mode") != "answer" or not actions:
        check["method"] = "single call, v6 prompt"
        check["calls"] += 1
        return generate(v6_messages, 768).strip(), check

    check["method"] = "one call per plan step"
    evidence = " ".join(e.get("text", "") for e in plan_row.get("evidence", [])
                        if e.get("document_id") in set(plan.get("selected_document_ids") or []))

    intro = clean(generate(intro_messages(request, lang), 60)); check["calls"] += 1
    intro_problems = validate(intro, "", lang, max_words=25)
    if intro_problems:
        check["intro"] = {"used": "fallback", "model_text": intro, "problems": intro_problems}
        intro = INTRO_FALLBACK[lang]
    if lang == "zh":
        intro = intro.translate(S2T)

    steps = []
    for a in actions:
        allowed = f"{a['instruction']} {a.get('source_quote', '')}"
        raw = clean(generate(step_messages(request, a, lang), 80)); check["calls"] += 1
        if lang == "zh":
            raw = raw.translate(S2T)
        problems = validate(raw, allowed, lang, labels(a["instruction"]))
        used = fallback_step(a, lang) if problems else raw
        check["fallbacks"] += bool(problems)
        check["steps"].append({"key": a["key"], "model_text": raw, "problems": problems,
                               "used": "fallback" if problems else "model"})
        steps.append(used)

    confirm = ""
    cue = CUE.search(evidence)
    if cue:
        sentence = cue.group(0).strip()
        text = clean(generate(confirm_messages(sentence, lang), 60)); check["calls"] += 1
        if lang == "zh":
            text = text.translate(S2T)
        if not validate(text, sentence, lang, max_words=30):
            confirm = text
        check["confirm"] = {"source": sentence, "model_text": text, "used": bool(confirm)}

    on_screen = any(labels(a["instruction"]) or "「" in a.get("source_quote", "") for a in actions)
    return compose(intro, steps, confirm, lang, on_screen), check

#!/usr/bin/env python3
"""Check that training data and the RAG corpus do not contain the evaluation questions or answers.

Training files (jsonl, field `messages` with role/content) are compared with the user turns of every
scenario: exact match after normalising, near match (word-sequence similarity >= 0.8), same source URL
(training field `sources[].url`), and the number of shared 5-word phrases (generic phrases such as
"how do i turn on" are expected and reported, not failed).

Corpus files (any text, md, json or jsonl) are searched for (a) the scenario prompt text and
(b) the text of expected_elements. The corpus must contain neither (the corpus holds official
operating content, not test items or reference answers). Official pages may legitimately cover the same
steps, so a hit on (b) is listed for a person to read; a hit on (a) fails.

Example:
  python check_overlap.py --scenarios eval_v2.jsonl --training train_v2_en.jsonl train_v2_reserve.jsonl ^
      --corpus corpus\\*.jsonl --out-md ..\\overlap_report_round2.md
"""
import argparse, difflib, glob, json, re, sys
from pathlib import Path


def norm(t):
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9㐀-鿿 ]", " ", str(t).lower())).strip()


def load_jsonl(p):
    return [json.loads(l) for l in open(p, encoding="utf-8") if l.strip()]


def ngrams(words, n=5):
    return {" ".join(words[i:i + n]) for i in range(len(words) - n + 1)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scenarios", required=True)
    ap.add_argument("--training", nargs="*", default=[])
    ap.add_argument("--corpus", nargs="*", default=[], help="files or globs")
    ap.add_argument("--near", type=float, default=0.8)
    ap.add_argument("--out-md", required=True)
    a = ap.parse_args()

    scen = load_jsonl(a.scenarios)
    ev_user = {s["id"]: " ".join(m["content"] for m in s["prompt"] if m["role"] == "user") for s in scen}
    ev_norm = {k: norm(v).split() for k, v in ev_user.items()}
    ev_ng = {k: ngrams(v) for k, v in ev_norm.items()}
    ev_url = {s["id"]: (s.get("source_url") or "").rstrip("/") for s in scen}
    fails, notes, table = [], [], []

    for f in a.training:
        rows = load_jsonl(f)
        exact, near, url, shared = [], [], [], 0
        for r in rows:
            u = " ".join(m["content"] for m in r.get("messages", []) if m["role"] == "user")
            nu = norm(u).split()
            ng = ngrams(nu)
            for sid, nv in ev_norm.items():
                if nu == nv:
                    exact.append((r.get("id"), sid))
                elif len(nu) > 3 and difflib.SequenceMatcher(None, nu, nv).ratio() >= a.near:
                    near.append((r.get("id"), sid))
                if ng & ev_ng[sid]:
                    shared += 1
            for s in r.get("sources", []) or []:
                for sid, x in ev_url.items():
                    if x and (s.get("url") or "").rstrip("/") == x:
                        url.append((r.get("id"), sid))
        table.append((Path(f).name, len(rows), len(exact), len(near), len(url), shared))
        if exact: fails.append(f"{Path(f).name}: exact user-text match {exact[:5]}")
        if near: fails.append(f"{Path(f).name}: near match {near[:5]}")
        if url: fails.append(f"{Path(f).name}: same source URL as an eval scenario {url[:5]}")

    corpus_files = []
    for g in a.corpus:
        corpus_files += glob.glob(g)
    for f in corpus_files:
        txt = norm(Path(f).read_text(encoding="utf-8", errors="replace"))
        for s in scen:
            if len(ev_norm[s["id"]]) >= 6 and " ".join(ev_norm[s["id"]]) in txt:
                fails.append(f"{Path(f).name}: contains the prompt text of {s['id']}")
            for e in s.get("expected_elements", []):
                ne = norm(e)
                if len(ne) >= 40 and ne[:80] in txt:
                    notes.append(f"{Path(f).name}: contains the first words of an expected element of {s['id']}: '{ne[:60]}...'")
    md = ["# Overlap check", "", f"Scenarios: {len(scen)}.", ""]
    if table:
        md += ["| Training file | Examples | Exact | Near (>= %.1f) | Same source URL | Scenario/example pairs sharing a 5-word phrase |" % a.near, "|---|---|---|---|---|---|"]
        md += [f"| {t[0]} | {t[1]} | {t[2]} | {t[3]} | {t[4]} | {t[5]} |" for t in table]
        md += ["", "Shared 5-word phrases are mostly generic wording. Read any pair with 3 or more shared phrases by hand.", ""]
    md += [f"Corpus files searched: {len(corpus_files)}.", "",
           f"**Result: {'FAIL' if fails else 'PASS'}** ({len(fails)} problems, {len(notes)} items for a person to read)", ""]
    if fails: md += ["## Problems", ""] + [f"- {x}" for x in fails] + [""]
    if notes: md += ["## Read these", ""] + [f"- {x}" for x in notes] + [""]
    md += ["Limits: wording and source URL only; meaning-level overlap is not checked."]
    Path(a.out_md).write_text("\n".join(md) + "\n", encoding="utf-8")
    print("\n".join(md))
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Build train_v2_en v2.2 from v2.1 plus the human-requested fixes.

    python3 data/v2/tools/apply_human_fixes.py

Inputs (not changed):
    data/v2/versions/train_v2_en.v2.0.jsonl      text the AI review judged (frozen 2026-11-13)
    data/v2/versions/train_v2_en.v2.1.jsonl      after Ryan's 7 spot-check fixes
    data/v2/human_fixes/v2_2_fixes.py             Shirley's 15 fixes, rewritten against official pages
    data/v2/spot_check_v2.csv                     spot-check decisions (Ryan and Shirley)

Outputs:
    data/v2/train_v2_en.jsonl                     v2.2 training file
    data/v2/train_v2_en.manifest.json             v2.2 manifest: file hash, per-example hashes,
                                                  and for each example the hash of the text the
                                                  AI review actually judged
    data/v2/human_fixes/changes_v2.1.jsonl        before/after record of the v2.1 edits
    data/v2/human_fixes/changes_v2.2.jsonl        before/after record of the v2.2 edits
    data/v2/train_v2_index.csv                    adds hash and edit columns

Per-example hash = sha256 of the record as JSON with sorted keys (same as assemble.py).
"""
import csv
import hashlib
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
V2 = REPO / "data" / "v2"
sys.path.insert(0, str(REPO))
sys.path.insert(0, str(V2 / "human_fixes"))
from scripts.validate_data import check_record  # noqa: E402
from v2_2_fixes import FIXES  # noqa: E402

MAX_CHARS = 2200


def sha(obj):
    return hashlib.sha256(json.dumps(obj, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()


def load(path):
    return [json.loads(l) for l in open(path, encoding="utf-8") if l.strip()]


def file_sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    v20_path = V2 / "versions/train_v2_en.v2.0.jsonl"
    v21_path = V2 / "versions/train_v2_en.v2.1.jsonl"
    v20 = {r["id"]: r for r in load(v20_path)}
    v21 = load(v21_path)
    v21_by_id = {r["id"]: r for r in v21}
    assert list(v20) == [r["id"] for r in v21], "v2.0 and v2.1 must hold the same ids in the same order"

    # 1. Reconstruct the v2.1 change log (v2.0 -> v2.1), which was not written at the time.
    v21_changed = [i for i in v20 if sha(v20[i]) != sha(v21_by_id[i])]
    with open(V2 / "human_fixes/changes_v2.1.jsonl", "w", encoding="utf-8") as f:
        for i in v21_changed:
            f.write(json.dumps({
                "id": i, "version": "v2.1", "date": "2026-11-13",
                "requested_by": "Ryan (spot check)", "written_by": "AI, from Ryan's spot-check decision",
                "before_sha256": sha(v20[i]), "after_sha256": sha(v21_by_id[i]),
                "before_messages": v20[i]["messages"], "after_messages": v21_by_id[i]["messages"],
            }, ensure_ascii=False) + "\n")

    # 2. Apply the v2.2 fixes on top of v2.1.
    fix_by_id = {fx["id"]: fx for fx in FIXES}
    assert len(fix_by_id) == len(FIXES), "duplicate id in FIXES"
    missing = set(fix_by_id) - set(v21_by_id)
    assert not missing, f"fix ids not in v2.1: {missing}"
    v22, changes = [], []
    for rec in v21:
        fx = fix_by_id.get(rec["id"])
        if fx is None:
            v22.append(rec)
            continue
        new = dict(rec)
        new["messages"] = fx["messages"]
        new["sources"] = fx["sources"]
        errs = []
        check_record(new, "train", errs, new["id"])
        text = "".join(m["content"] for m in new["messages"])
        assert not errs, errs
        assert len(text) <= MAX_CHARS, (new["id"], len(text))
        assert "—" not in text and "–" not in text, (new["id"], "dash")
        assert new["messages"][-1]["role"] == "assistant", new["id"]
        assert sha(new) != sha(rec), (new["id"], "fix did not change the record")
        v22.append(new)
        changes.append({
            "id": rec["id"], "version": "v2.2", "date": "2026-11-16",
            "requested_by": "Shirley (spot check, spot_check_v2.csv)",
            "written_by": "AI, from Shirley's notes; checked against the official pages listed in after_sources",
            "follows": fx["follows"], "page_differs": fx["page_differs"],
            "ai_review_sha256": sha(v20[rec["id"]]),
            "before_sha256": sha(rec), "after_sha256": sha(new),
            "before_messages": rec["messages"], "after_messages": new["messages"],
            "before_sources": rec["sources"], "after_sources": new["sources"],
        })
    with open(V2 / "human_fixes/changes_v2.2.jsonl", "w", encoding="utf-8") as f:
        for c in changes:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")

    out = V2 / "train_v2_en.jsonl"
    with open(out, "w", encoding="utf-8") as f:
        for rec in v22:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    # 3. Spot-check status per id.
    spot = {}
    for r in csv.DictReader(open(V2 / "spot_check_v2.csv", encoding="utf-8-sig")):
        who = []
        if r.get("decision"):
            who.append(f"Ryan:{r['decision']}")
        if r.get("shirley_verdict"):
            who.append(f"Shirley:{r['shirley_verdict']}")
        spot[r["id"]] = ";".join(who)

    # 4. Manifest. ai_review_sha256 is the hash of the v2.0 text, the last text the AI reviewer judged.
    v21_set, v22_set = set(v21_changed), {c["id"] for c in changes}
    examples = []
    for rec in v22:
        i = rec["id"]
        edited = [v for v, s in (("v2.1", v21_set), ("v2.2", v22_set)) if i in s]
        examples.append({
            "id": i, "sha256": sha(rec), "ai_review_sha256": sha(v20[i]),
            "text_status": "edited_after_ai_review" if edited else "as_ai_reviewed",
            "edited_in": edited, "spot_check": spot.get(i, ""),
        })
    old = json.load(open(V2 / "versions/train_v2_en.v2.1.manifest.json", encoding="utf-8"))
    manifest = {
        "name": "train_v2_en", "version": "v2.2", "created": "2026-11-16", "language": "en",
        "count": len(v22), "file": "data/v2/train_v2_en.jsonl", "sha256": file_sha(out),
        "label": "AI-screened, with human spot checks",
        "human_reviewed_count": old.get("human_reviewed_count", 17),
        "spot_check": {
            "file": "data/v2/spot_check_v2.csv", "sample": len(spot),
            "ryan_checked": sum("Ryan:" in v for v in spot.values()),
            "shirley_checked": sum("Shirley:" in v for v in spot.values()),
            "fixed_in_v2_1": sorted(v21_set), "fixed_in_v2_2": sorted(v22_set),
        },
        "edited_after_ai_review": len([e for e in examples if e["edited_in"]]),
        "history": [
            {"version": "v2.0", "file": "data/v2/versions/train_v2_en.v2.0.jsonl", "sha256": file_sha(v20_path),
             "note": "frozen from AI review (assemble.py)"},
            {"version": "v2.1", "file": "data/v2/versions/train_v2_en.v2.1.jsonl", "sha256": file_sha(v21_path),
             "changes": "data/v2/human_fixes/changes_v2.1.jsonl",
             "note": "7 fixes from Ryan's spot check. Its manifest kept the v2.0 per-example hashes for these 7 ids; corrected here."},
            {"version": "v2.2", "changes": "data/v2/human_fixes/changes_v2.2.jsonl",
             "note": "15 fixes from Shirley's spot check, rewritten against official pages"},
        ],
        "review_note": ("The AI review records in data/v2/reviews/ judged the text whose hash is ai_review_sha256. "
                        "For examples with text_status edited_after_ai_review, those records describe an earlier "
                        "text and do not cover the current one."),
        "examples": examples,
    }
    json.dump(manifest, open(V2 / "train_v2_en.manifest.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)

    # 5. Index: add hash and edit columns (existing columns untouched).
    idx_path = V2 / "train_v2_index.csv"
    rows = list(csv.DictReader(open(idx_path, encoding="utf-8")))
    base_cols = [c for c in rows[0].keys() if c not in ("sha256_v2_2", "ai_review_sha256", "edited_after_ai_review", "spot_check")]
    ex = {e["id"]: e for e in examples}
    for r in rows:
        e = ex.get(r["id"])
        r["sha256_v2_2"] = e["sha256"] if e else ""
        r["ai_review_sha256"] = e["ai_review_sha256"] if e else ""
        r["edited_after_ai_review"] = ",".join(e["edited_in"]) if e else ""
        r["spot_check"] = e["spot_check"] if e else ""
    with open(idx_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=base_cols + ["sha256_v2_2", "ai_review_sha256", "edited_after_ai_review", "spot_check"])
        w.writeheader()
        w.writerows(rows)

    print(f"v2.1 edits: {len(v21_changed)} | v2.2 edits: {len(changes)} | count {len(v22)}")
    print(f"v2.2 sha256 {manifest['sha256']}")


if __name__ == "__main__":
    main()

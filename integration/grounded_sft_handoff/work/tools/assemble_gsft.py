#!/usr/bin/env python3
"""Assemble the 500 grounded SFT examples from the reviewed candidates.

Reads the full build (work/build/), the latest independent review for each id (work/reviews/),
and writes integration/grounded_sft_handoff/final/:

  grounded_sft_500.jsonl                  training records (rag-system-v1), unchanged messages
  grounded_sft_500.provenance.jsonl       one provenance row per id (RECORD_FORMATS.md)
  grounded_sft_500.ai_reviews.jsonl       the keep review bound to each final hash
  grounded_sft_500.human_spot_checks.csv  Ryan's sheet: ids and hashes only, outcomes blank
  grounded_sft_500.task_clearance_request.csv  for the evaluation owner (disposition blank)
  grounded_sft_500.manifest.json          counts, hashes, exclusions, address notes

Only a candidate whose CURRENT version has a keep review is eligible. Nothing in messages is
changed here, so every content hash and review binding stays valid.

Source addresses: a reviewer sometimes read the same official page at a different address
(the one a web search returned). Shirley's validator requires the review's official_url to
equal the provenance url, so the provenance row for that example records the address the
reviewer actually read, and keeps the card's address in `card_url`. The training record's
`sources` list is rebuilt from the same refs. This is metadata only.
"""
import collections
import csv
import hashlib
import importlib.util
import json
import random
import sys
from pathlib import Path

WORK = Path(__file__).resolve().parents[1]
H = WORK.parent
OUT = H / "final"
TARGET = {"direct": 200, "clarify": 125, "constraint": 100, "multiturn": 75}

spec = importlib.util.spec_from_file_location("rio", WORK / "tools/review_io.py")
rio = importlib.util.module_from_spec(spec)
sys.argv = [sys.argv[0], "status"]
spec.loader.exec_module(rio)


def sha_file(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


SPOT = H / "final/grounded_sft_500.human_spot_checks.csv"
SPOT_IDS = {r["id"] for r in csv.DictReader(open(SPOT, encoding="utf-8"))} if SPOT.exists() else set()


def main():
    recs, prov = rio.build()
    done = rio.all_reviews()
    keep = {}
    for i in prov:
        r = rio.current_review(done, prov, i)
        if r and r["decision"] == "keep":
            keep[i] = r
    excluded = {i: "no keep review for the current version" for i in prov if i not in keep}

    # Trim to the target behavior counts. Drop from the largest task group first, never an
    # example that the owner edited (those are in the spot-check sheet).
    by_beh = collections.defaultdict(list)
    for i in keep:
        by_beh[prov[i]["behavior"]].append(i)
    group_n = collections.Counter(prov[i]["task_group"] for i in keep)
    for beh, ids in by_beh.items():
        extra = len(ids) - TARGET[beh]
        if extra < 0:
            sys.exit(f"not enough kept {beh} examples: {len(ids)} < {TARGET[beh]}")
        owner = {i for i in ids if any("Owner" in h.get("reason", "") or "Human spot check" in h.get("reason", "")
                                       for h in prov[i]["correction_history"])} | SPOT_IDS
        ranked = sorted((i for i in ids if i not in owner),
                        key=lambda i: (-group_n[prov[i]["task_group"]], i), )
        for i in ranked[:extra]:
            excluded[i] = f"kept, but over the {beh} target of {TARGET[beh]} (largest task group trimmed)"
            group_n[prov[i]["task_group"]] -= 1
            del keep[i]

    final_ids = sorted(keep)
    assert len(final_ids) == 500, len(final_ids)

    # Eligibility follows the evaluation owner's clearance file once it exists: cleared only when
    # every final task group is allow_training with an owner and a date.
    clearance_path = OUT / "grounded_sft_500.task_clearance.csv"
    cleared = False
    if clearance_path.exists():
        cl = {r["task_group"]: r for r in csv.DictReader(open(clearance_path, encoding="utf-8"))}
        cleared = all(cl.get(prov[i]["task_group"], {}).get("disposition") == "allow_training"
                      and cl[prov[i]["task_group"]].get("owner") and cl[prov[i]["task_group"]].get("date")
                      for i in final_ids)

    OUT.mkdir(exist_ok=True)
    url_notes = 0
    with open(OUT / "grounded_sft_500.jsonl", "w", encoding="utf-8") as fr, \
            open(OUT / "grounded_sft_500.provenance.jsonl", "w", encoding="utf-8") as fp, \
            open(OUT / "grounded_sft_500.ai_reviews.jsonl", "w", encoding="utf-8") as fv:
        for i in final_ids:
            rec = json.loads(json.dumps(recs[i]))
            p = json.loads(json.dumps(prov[i]))
            if cleared:
                p["eligibility"] = "cleared_for_training"
            r = keep[i]
            read_at = {sc["ref_id"]: sc["official_url"] for sc in r["source_checks"]}
            for ref in p["source_refs"]:
                if read_at.get(ref["ref_id"]) and read_at[ref["ref_id"]] != ref["url"]:
                    ref["card_url"] = ref["url"]
                    ref["url"] = read_at[ref["ref_id"]]
                    ref["url_note"] = ("The independent reviewer read this official page at this address on "
                                       "2026-11-17; the source card cited card_url for the same page.")
                    url_notes += 1
            sources, seen = [], set()
            for ref in p["source_refs"]:
                if ref["url"] not in seen:
                    seen.add(ref["url"])
                    sources.append({"title": ref["title"], "url": ref["url"], "accessed": ref["access_date"]})
            rec["sources"] = sources
            assert rec["messages"] == recs[i]["messages"]
            fr.write(json.dumps(rec, ensure_ascii=False) + "\n")
            fp.write(json.dumps(p, ensure_ascii=False) + "\n")
            fv.write(json.dumps(r, ensure_ascii=False) + "\n")

    # Human spot-check sheet. Once Ryan has logged it, never regenerate: keep his rows and fill the
    # follow-up columns for corrected rows from the current version and its independent review.
    cols = "id,conversation_sha256,reviewer,reviewed_at,sampling_reason,source_refs,verdict,findings,proposed_correction,resolution,corrected_candidate_id,corrected_content_sha256,followup_review_id".split(",")
    if SPOT.exists():
        spot_rows = list(csv.DictReader(open(SPOT, encoding="utf-8")))
        for row in spot_rows:
            i = row["id"]
            if row["verdict"] == "revise" and i in keep:
                cur = prov[i]["generation"]["candidate_id"]
                if prov[i]["content_sha256"] != row["conversation_sha256"]:
                    row.update(corrected_candidate_id=cur, corrected_content_sha256=prov[i]["content_sha256"],
                               followup_review_id=keep[i]["review_id"],
                               resolution="corrected as " + cur + "; independent AI re-review: keep")
        reasons = {r["id"]: r for r in spot_rows}
        with open(SPOT, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=cols)
            w.writeheader()
            w.writerows(spot_rows)
    else:
        rng = random.Random(20261117)
        reasons = {}
        for i in final_ids:
            hist = prov[i]["correction_history"]
            if prov[i]["generation"].get("model") == "claude-opus-5-5" or any("Owner" in h.get("reason", "") for h in hist):
                reasons[i] = "AI-review edge case: edited or written by the main session, not the writer agent"
        for i, why in (("gsft-text_size-06", "edge case: user avoids Settings but the only documented path mentions it"),
                       ("gsft-wifi_calling-07", "edge case: target keeps a page-stated wait between steps")):
            if i in keep:
                reasons[i] = why
        for batch in ("b02.json", "b14.json"):
            pool = [i for i in final_ids if prov[i]["generation"]["draft_file"] == batch and i not in reasons]
            for i in rng.sample(pool, 2):
                reasons[i] = "edge case: its reviewer read the targets before listing required actions"
        quota = {b: round(55 * n / 500) for b, n in TARGET.items()}
        have = collections.Counter(prov[i]["behavior"] for i in reasons)
        groups_used = {prov[i]["task_group"] for i in reasons}
        order = final_ids[:]
        rng.shuffle(order)
        for i in order:
            if len(reasons) >= 55:
                break
            b, g = prov[i]["behavior"], prov[i]["task_group"]
            if i in reasons or g in groups_used or have[b] >= quota[b]:
                continue
            tags = ",".join(prov[i]["tags"]) or "no tags"
            reasons[i] = f"stratified sample: {b}, {g}, {tags}"
            have[b] += 1
            groups_used.add(g)
        cols = "id,conversation_sha256,reviewer,reviewed_at,sampling_reason,source_refs,verdict,findings,proposed_correction,resolution,corrected_candidate_id,corrected_content_sha256,followup_review_id".split(",")
        with open(OUT / "grounded_sft_500.human_spot_checks.csv", "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=cols)
            w.writeheader()
            for i in sorted(reasons):
                w.writerow({"id": i, "conversation_sha256": prov[i]["content_sha256"], "sampling_reason": reasons[i],
                            "source_refs": " ".join(s["ref_id"] for s in prov[i]["source_refs"])})

    # Task clearance request for the evaluation owner.
    req = list(csv.DictReader(open(WORK / "task_clearance_request_v1.csv", encoding="utf-8")))
    per_group = collections.Counter(prov[i]["task_group"] for i in final_ids)
    with open(OUT / "grounded_sft_500.task_clearance_request.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["task_group", "disposition", "owner", "date", "note"])
        w.writeheader()
        for row in req:
            if per_group[row["task_group"]]:
                row["note"] = f"{per_group[row['task_group']]} final examples. " + row["note"]
                w.writerow(row)

    beh = collections.Counter(prov[i]["behavior"] for i in final_ids)
    tags = collections.Counter(t for i in final_ids for t in prov[i]["tags"])
    manifest = {
        "name": "grounded_sft_500", "prompt_version": "rag-system-v1", "count": len(final_ids),
        "status": ("AI-reviewed, human spot-checked and cleared by the evaluation owner; pending only the tokenizer length check"
                   if cleared else "AI-reviewed; pending evaluation-owner task clearance and the tokenizer length check"),
        "eligibility": "cleared_for_training" if cleared else "pending_eval_owner_clearance",
        "tokenizer_revision_required": "Qwen/Qwen2.5-3B-Instruct aa8e72537993ba99e69dfaafa59ed015b17504d1",
        "files": {f.name: sha_file(f) for f in sorted(OUT.glob("grounded_sft_500.*")) if f.suffix in (".jsonl", ".csv")},
        "behavior": dict(beh), "tags": dict(tags),
        "task_groups": len(per_group), "max_per_task_group": max(per_group.values()),
        "source_groups": len({prov[i]["source_group"] for i in final_ids}),
        "category": dict(collections.Counter(recs[i]["category"] for i in final_ids)),
        "authors": dict(collections.Counter(recs[i]["author"] for i in final_ids)),
        "candidates_drafted": len(prov), "excluded": excluded,
        "provenance_address_notes": url_notes,
        "human_spot_check_rows": len(reasons),
        "human_checked": sum(1 for r in csv.DictReader(open(OUT / "grounded_sft_500.human_spot_checks.csv", encoding="utf-8")) if r["verdict"]),
        "ids": final_ids,
        "content_sha256": {i: prov[i]["content_sha256"] for i in final_ids},
        "inputs": {name: sha_file(H / name) for name in ("prompt_contract.py", "validate_grounded.py")} |
                  {f"work/{n}": sha_file(WORK / n) for n in ("AGENT_GSFT_WRITER.md", "AGENT_GSFT_REVIEWER.md",
                                                            "AGENT_GSFT_REVISER.md", "allocation_v1.csv")},
    }
    json.dump(manifest, open(OUT / "grounded_sft_500.manifest.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print(json.dumps({k: manifest[k] for k in ("count", "behavior", "tags", "task_groups", "max_per_task_group",
                                               "source_groups", "category", "authors", "provenance_address_notes",
                                               "human_spot_check_rows")}, indent=1))
    print("excluded:", excluded)


if __name__ == "__main__":
    main()

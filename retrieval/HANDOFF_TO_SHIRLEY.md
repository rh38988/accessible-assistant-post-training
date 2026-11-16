# Handoff to Shirley: training data and RAG additions (from Ryan, 2026-11-13)

## 1. Training file (for your SFT run)
- File: `data/v2/train_v2_en.jsonl`, 1,000 English examples, version v2.2 (updated 2026-11-16 after Shirley's spot check)
- sha256: `e0ce1fdbe2c545cc...` (full hash in `data/v2/train_v2_en.manifest.json`)
- Schema: existing training schema. `training/train_sft.py` trains on the last assistant turn only.
- Validator: `python scripts/validate_data.py --kind train data/v2/train_v2_en.jsonl` passes.
- Label: "AI-screened, with human spot checks." 17 examples were read in full earlier, and 15 more were spot-checked by Ryan (see `data/v2/spot_check_v2.csv`). Seven of those 15 were fixed in v2.1.
- Reserve: 57 spare examples in `data/v2/train_v2_reserve.jsonl`, not in the training file.

## 2. Token length
- Enforced as 2,200 characters, because the Qwen tokenizer isn't available locally. Please check the longest conversation (about 1,860 characters) with the real tokenizer against the 768-token cap.

## 3. RAG additions (new docs in `retrieval/docs/`)
- `apple_facetime_call.md`, `apple_group_facetime.md`: video calls (FaceTime)
- `ftc_tech_support_scams.md`: remote-access and tech support scams
- `ftc_after_a_scam.md`: recovery after a scam, including remote access
- `ftc_payment_apps.md`: bank transfers and payment apps
- Each has `Source:` and `Accessed:` headers, with steps in our own words.
- Check: `python retrieval/bm25.py "my grandson wants to facetime me"` returns `apple_facetime_call.md` first.

## 4. Still needs your conversion
- The corpus manifest and loader are not on this machine, so these docs need converting to your record schema.
- Please confirm the schema and metadata fields when you convert.

## 5. Content gaps (see `retrieval/SOURCE_GAPS_v1.md`)
- Google Meet and WhatsApp video calls: their pages can't be read by the fetch tool. Someone needs to copy the steps by hand.
- Zelle's own help pages: not yet added.
- "Money sent by mistake, please send it back": the FTC page doesn't cover it.

## 6. Version record
- Git branch: `data-v2` (GitHub: rh38988/accessible-assistant-post-training).
- Training file version is in the manifest. The RAG docs are committed on the same branch.

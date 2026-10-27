# eval_v1 overlap report (training vs. evaluation)

Prepared 2026-10-26 for the Evaluation Lead. Status: **pilot checkpoint set, not frozen.** This report does **not** claim zero leakage. It lists what was checked, what was found, and what could not be checked.

## 1. How the repository was read

`git clone` was blocked by the sandbox proxy (HTTP 403), and I did not work around it. All files were read through GitHub's API and raw-file URLs on `main` (tree sha `4c8e7bc3…`), 2026-10-26. No local clone exists, so the checks below are keyword/phrase searches and manual reading, **not** a programmatic n-gram comparison over a checked-out repo.

| Path | How it was examined |
|---|---|
| `data/tasks/train_tasks.csv` (TR-001…TR-116) | Read in full |
| `data/tasks/core_tasks_v1.csv` (CT-01…CT-17) | Read in full |
| `scripts/task_lists.py` (TRAIN and EVAL lists, type-disjointness assert) | Read in full |
| `scripts/core_tasks.py` | Read in full |
| `data/pilot/pilot_v1.jsonl` (20 examples) | Read in full |
| `data/train/recovery_v1.jsonl` (3 examples) | Read in full |
| `data/train/batch_01…05.jsonl` (380 lines returned) | **Every user turn extracted and read** (all first-turn prompts, clarification answers and follow-ups). Assistant replies were **searched by keyword**, not read in full. |
| `data/drafting/sources.py` | Read in full (every training source URL) |
| `data/drafting/README.md` | Read |
| `data/drafting/batch_01…05.py`, `build.py`, `recovery_v1.py` | **Not read.** They are the specs that generated the JSONL, so the JSONL was checked instead. |
| `eval/tasks/eval_tasks.csv` (EV-001…EV-150) | Read in full |
| `eval/scenarios/sample.jsonl` | Read in full |
| `eval/prompts/demonstrations.jsonl`, `system_prompt.txt` | Read in full |
| `data/README.md`, `data/QUALITY_SUMMARY_v1.md`, `eval/README.md` | Read |
| `retrieval/docs/*` | **Only file names seen**, contents not read |
| `data/tasks/checkpoint_verify_v1.csv`, `checkpoint_ai_precheck_v1.json` | **Not read** |

## 2. Selected tasks

All 15 scenarios map to a task type in `eval/tasks/eval_tasks.csv`, none of which appears in `data/tasks/train_tasks.csv` (the repo's own split is by `task_type`, asserted in `scripts/task_lists.py`). Platforms and devices were changed from the CSV's suggestions where noted, which the CSV allows.

| Scenario | Task family | EV task (task_type) | Note |
|---|---|---|---|
| EVAL-PHONE-001 | Smartphone Basics | EV-009 (dark_mode, iPhone) | |
| EVAL-PHONE-002 | Smartphone Basics | EV-014 (do_not_disturb) | Device made unspecified (EV-014 says iPhone, EV-015 Android) |
| EVAL-PHONE-003 | Smartphone Basics | EV-012 (wallpaper) | Device made unspecified |
| EVAL-PHONE-004 | Smartphone Basics | EV-085 (airplane_mode, iPhone) | Reframed as a failure-recovery about Wi-Fi in flight |
| EVAL-PHONE-005 | Smartphone Basics | EV-088 (hotspot, iPhone) | |
| EVAL-COMM-001 | Communication | EV-001 (video_call) | Device made unspecified |
| EVAL-COMM-002 | Communication | EV-119 (speakerphone, Android) | |
| EVAL-COMM-003 | Communication | EV-093 (meeting_controls, Zoom) | Reframed as a failure-recovery about unmuting |
| EVAL-COMM-004 | Communication | EV-022/EV-023 (email_forward) | App made unspecified |
| EVAL-COMM-005 | Communication | EV-097 (unsend_message, LINE, zh-TW) | |
| EVAL-SAFE-001 | Online Safety and Scam Prevention | EV-006 (tech_support_scam, pop-up) | Extended into a remote-access recovery |
| EVAL-SAFE-002 | Online Safety and Scam Prevention | EV-037 (medicare_scam) | |
| EVAL-SAFE-003 | Online Safety and Scam Prevention | EV-041 (utility_shutoff_scam) | |
| EVAL-SAFE-004 | Online Safety and Scam Prevention | EV-044 (installment_cancel_scam, zh-TW) | |
| EVAL-SAFE-005 | Online Safety and Scam Prevention | EV-035 (p2p_payment) | App made unspecified; the prompt avoids naming Zelle |

## 3. Checks performed and results

| # | Check | Method | Result |
|---|---|---|---|
| 1 | Exact duplicate prompts | Read all training user turns (batches 01–05, pilot, recovery), plus sample.jsonl and the 2 demonstrations | **None.** No scenario prompt equals any training user message. |
| 2 | Near-duplicate wording | Same reading, comparing wording and content words | **None found.** Closest cases are listed in section 4. |
| 3 | Identical task / task type | Compared EV types with all 72 training task types in `train_tasks.csv` | **None.** None of the 15 task types appears in training. |
| 4 | Training source pages reused | Searched all 5 batch files for the 18 URL fragments I cite or consult, and compared against `data/drafting/sources.py` and the pilot/recovery sources. Positive control: a known training URL fragment (`102453`, `105103`, `ftc.gov/node/54353`) was found. | **0 matches** for my URLs. No eval source page is cited by any training example. |
| 5 | Same-topic keyword search in training answers | Searched batches 01–05 for: Medicare, utility/power company, remote access/AnyDesk/TeamViewer, virus, ATM, 分期, 解除, Zelle/Venmo/Cash App/PayPal, hotspot, mute/unmute, Airplane, wallpaper, Dark Mode, speakerphone/Speaker, 收回, 電費 | **None matched** except the incidental hits in section 4. |
| 6 | Procedural-step overlap | Searched for shared sub-steps (Control Center, Phone app, Sounds & Haptics, Wi-Fi join) | **Shared sub-steps exist**, see section 4. |
| 7 | Few-shot demonstrations | Compared the 2 demos in `eval/prompts/demonstrations.jsonl` with all 15 | **Two similar-pattern pairs**, see section 4. No demo covers a selected task. |
| 8 | `sample.jsonl` placeholder | Compared sample scenarios sc-0001…0004 | Not reused. One topic neighbor (sc-0003, see section 4). `sc-0002` (iPhone text size) **is** a training task and must not be used. |

## 4. Remaining overlaps (judged tolerable, but need your decision)

| Scenario | Overlapping training content | Why it was kept | Risk |
|---|---|---|---|
| PHONE-001, -002, -004 | "Open Control Center: swipe down from the top-right" is taught in iPhone examples for rotation lock (TR-108), battery saver (TR-070), QR scan (TR-076). Do Not Disturb appears only incidentally in the alarm examples (TR-066: "alarm will ring even if on Silent or Do Not Disturb"). | The setting being taught (Appearance, Do Not Disturb, Wi-Fi in Airplane Mode) is not trained; Control Center is a shared navigation primitive. | Low to medium. A post-trained model may be slightly better at *opening Control Center* for reasons unrelated to the held-out task. |
| PHONE-005 | Wi-Fi join (pick network, type password) is taught in wifi_connect (TR-007, TR-030, TR-031, pilot-007). The hotspot-specific steps are not. | Hotspot is a distinct task type. | Medium. Step 3 (connect laptop to a network) resembles Windows Wi-Fi training. Consider swapping if the team wants a stricter set. |
| COMM-002 | Google Phone app guidance appears in block_number / spam_call_filter (TR-046, TR-049), including the phrase "These steps are for Google's Phone app. If your Phone app looks different, tell me what you see." The demonstration demo-02 is about Android in-call volume. | Speaker button is a different action. | Medium for the `fewshot` condition, which is shown demo-02. |
| COMM-003 | Zoom is covered by join_video_meeting (TR-093). | Muting/unmuting is a different task. | Low. |
| COMM-004 | demo-01 ("How do I send a photo to my daughter?") teaches asking which app the user uses. | Different task (forwarding email vs sending a photo). | Low. Same clarify-which-app pattern, which is the intended behavior. |
| COMM-001 | `tr110-*` mentions an incidental FaceTime freeze as the cause of a stuck phone. `sample.jsonl` sc-0001 is a video-call scenario ("How do I video call my grandson?"). | FaceTime call steps are not taught. sc-0001 is a placeholder with different wording. | Low. |
| SAFE-001 | `sample.jsonl` sc-0003 is a Microsoft virus-call scenario. Training has no tech-support scam. | Different framing (pop-up origin, remote access already granted). | Low, but retire `sample.jsonl` from baseline runs so the two do not both appear. |
| SAFE-001…005 | General scam principles are taught across CT-13 to CT-16 and pilot-014/015: hang up, verify with a number you already have, report at ReportFraud.ftc.gov, red-flag payment methods (gift cards, wire transfers). | The *stories* are new (tech-support remote access, Medicare, utility shut-off, ATM installment cancellation, payment-app transfer). This is the generalization the README says it wants to test (`eval/README.md`: "different stories … to test whether safe behavior generalizes"). | Expected. Do not read a safety win as "learned the scenario"; it may be transfer of a general scam heuristic. |
| SAFE-004 | Same publisher book (CIB 常見詐騙手法話術解析與因應之道, `id=1909`) is the source of training scam examples (TR-113, TR-114, TR-115), but a **different chapter** (`serno=a61af506…`, ATM 解除分期付款) from the three used in training (`b7cf505d…`, `a4f8d5ab…`, `7e614f6f…`). | Different scam. | Low. |
| SAFE-005 | pilot-016 ("is it safe to pay for something online?") also asks which payment method is used. | Different task. | Low. |

## 5. Replacements made while building the set

| Dropped | Reason | Replacement |
|---|---|---|
| iPhone keyboard sounds (EV-108) | Menu path Settings > Sounds & Haptics is also the training path for ring volume and alarm loudness (TR-024, TR-066). | iPhone Personal Hotspot (EV-088) |
| Android Phone-app missed calls | Phone-app call-list navigation is a sub-step of training block_number examples (TR-045/046). | Zoom unmute failure-recovery (EV-093) |
| iPhone dictation | Source page body could not be retrieved (page returned navigation only), so the steps could not be verified. | Same replacement as keyboard sounds |
| Airplane Mode "Control Center not at the top-right" recovery | Recovery step is taught directly in training (Control Center on Home-button iPhones). | "Why can't I use Wi-Fi on the plane" recovery |
| Utility scam with gift-card payment | Gift-card payment is the core of training task TR-041 / `tr041-r`. | Payment-app demand |
| Not selected from the start | EV-141 (restart router), EV-103 (micropayments), EV-020/021 (print), EV-126 (fake shopping), EV-148 to 150 (SOS), EV-139/140 (phone transfer), EV-147 (Live Listen), EV-127 (hacked email), EV-132 (robocalls), EV-137 (app permissions) | See `eval_tasks.csv` analysis (earlier report) |

## 6. Remaining risks and uncertainty

1. **No programmatic text overlap run.** Section 3 is reading plus keyword search. If you can clone the repo, run an n-gram or embedding comparison of `prompt` user turns and `expected_elements` against `data/**/*.jsonl` before freezing.
2. **Assistant replies in batches 01–05 were searched, not read.** A training answer could contain relevant content under words I did not search. Keywords covered the specific topic of each scenario.
3. **Drafting specs, retrieval docs, and checkpoint verification files were not read.** The retrieval documents are used by the `rag` and `sft_rag` conditions and were not checked for the selected tasks.
4. **Future training data.** The team plans a 43-type draft pool (`QUALITY_SUMMARY_v1.md`, "Extended pool") and more tasks. Any new training example on dark mode, Do Not Disturb, wallpaper, Airplane Mode, hotspot, video calls, speakerphone, Zoom muting, forwarding email, LINE unsend, tech-support/Medicare/utility/ATM-installment scams, or payment apps would leak. Add these 15 task types to a "blocked for training" list.
5. **Semantic overlap cannot be zero** for safety scenarios (section 4) and for shared navigation steps.
6. **`task_lists.py` asserts disjointness by type only.** It does not check wording or procedure, so it does not prove these 15 are clean.
7. **Retrieval fairness.** The `rag` baseline has docs only for training-like topics (`retrieval/README.md`). Adding docs for these 15 tasks makes the retrieval baseline stronger, and those docs must never enter training.

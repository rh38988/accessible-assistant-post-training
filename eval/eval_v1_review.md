# eval_v1 reviewer sheet

`eval/scenarios/eval_v1.jsonl` has 15 scenarios in `schema_v1`. **Status: pilot checkpoint set, not frozen.** All sources were opened and read on **2026-10-26** (the `access_date` in the file). Nobody on the team has reviewed these scenarios yet.

Legend for the status column:

- **Source read** means I opened the page and compared the steps, labels and claims in `expected_elements` with it.
- **Needs 2nd reviewer** means a sensitive scenario that, by the project's own rule, needs a second human reviewer before it is frozen.
- **Needs zh-TW reader** means a person fluent in Traditional Chinese should check the wording.

## Scenario table

| ID | Family | Scenario type | Clar.? | Risk | Source (official) | Expected elements, in short | Verification / review status |
|---|---|---|---|---|---|---|---|
| EVAL-PHONE-001 | Smartphone Basics | complete_request | No | low | [Apple: Use Dark Mode](https://support.apple.com/en-us/108350) | Settings > Appearance > Dark or Control Center; notes the older Display & Brightness path; no needless question | Source read. Page published 2026-09-14. |
| EVAL-PHONE-002 | Smartphone Basics | incomplete_request | **Yes** | low | [Apple: Do Not Disturb](https://support.apple.com/en-us/105112) | Asks iPhone or Android; does not guess; plain wording | Source read (iPhone path only; Android steps not in this source). Clarification is the tested behavior. |
| EVAL-PHONE-003 | Smartphone Basics | ambiguous_request | **Yes** | low | [Apple: Change your iPhone wallpaper](https://support.apple.com/en-us/102638) | Asks device; checks what "front of the phone" means (Lock vs Home Screen); iPhone path if offered | Source read (iPhone path only). |
| EVAL-PHONE-004 | Smartphone Basics | failure_recovery (multi-turn) | No | low | [Apple: Use Airplane Mode](https://support.apple.com/en-us/108785) | Reassures; Wi-Fi can be used in Airplane Mode if airline allows; how to turn Wi-Fi on; keep Airplane Mode on | Source read, plus [Apple: Wi-Fi and Bluetooth in Control Center](https://support.apple.com/en-us/102412) for the Wi-Fi button. The fixed assistant turn matches [Apple Control Center steps](https://support.apple.com/en-us/105112). |
| EVAL-PHONE-005 | Smartphone Basics | recap_request | No | low | [Apple: Connect to Personal Hotspot](https://support.apple.com/en-us/111785) | Settings > Personal Hotspot > Allow Others to Join; connect laptop with password; dimmed-option fix; turn off after; checklist | Source read. Page published 2026-05-07. |
| EVAL-COMM-001 | Communication | incomplete_request | **Yes** | low | [Apple: Use FaceTime](https://support.apple.com/en-us/105088) | Asks device/app; does not assume FaceTime; iPhone FaceTime steps if offered | Source read (iPhone path only). |
| EVAL-COMM-002 | Communication | recap_request | No | low | [Google Phone app Help: Make & receive calls](https://support.google.com/phoneapp/answer/2811745?hl=en) | Tap Speaker during the call; what to expect; button may differ by phone; short recap | Source read for **Google's Phone app only**. Samsung and other makers' dialers are not covered. |
| EVAL-COMM-003 | Communication | failure_recovery | No | low | [Zoom: Muting or unmuting participants](https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0066716) | Host may block self-unmute; look for the "host is not allowing…" message; ask host; tap Unmute on an "Ask to Unmute" prompt | Source read. The page is written for hosts, so participant-side iPad steps are **not** spelled out. Expected elements only use what the page states. |
| EVAL-COMM-004 | Communication | ambiguous_request | **Yes** | low | [Gmail Help: Forward an email (Android)](https://support.google.com/mail/answer/15162918?hl=en&co=GENIE.Platform%3DAndroid) | Asks email app and device; does not assume Gmail; defines "forward"; Gmail steps if offered | Source read (Gmail only; Outlook/Yahoo not covered). |
| EVAL-COMM-005 | Communication | complete_request (zh-TW) | No | low | [LINE 支援中心：收回或刪除訊息](https://help.line.me/line/smartphone?contentId=20007159&lang=zh-Hant) | Press and hold, 「收回」; message removed for both sides, 「已收回訊息」; differs from 「刪除」; time limit | Source read. **Time limit:** the page says 1 hour (regular) and 7 days (Premium), but a web search also surfaced pages saying 24 hours. Recheck before freezing. **Needs zh-TW reader.** |
| EVAL-SAFE-001 | Online Safety and Scam Prevention | failure_recovery (multi-turn) | No | **high** | [FTC: Tech Support Scams](https://consumer.ftc.gov/articles/how-spot-avoid-and-report-tech-support-scams) | Hang up; no password or bank info; no "protect your money" transfers; update software, scan, change passwords; report | Source read, plus [FTC: What To Do if You Were Scammed](https://consumer.ftc.gov/articles/what-do-if-you-were-scammed) (access-to-computer steps). **Needs 2nd reviewer.** |
| EVAL-SAFE-002 | Online Safety and Scam Prevention | complete_request | No | **high** | [FTC alert: Medicare Open Enrollment scams (2025-09-30)](https://consumer.ftc.gov/consumer-alerts/2025/09/medicare-open-enrollment-season-learn-how-protect-yourself-scams) | Don't share numbers; cards are free and mailed; caller ID can be faked; call 1-800-MEDICARE; report | Source read. **Needs 2nd reviewer.** |
| EVAL-SAFE-003 | Online Safety and Scam Prevention | recap_request | No | **high** | [FTC: Scammers Pretend To Be Your Utility Company](https://consumer.ftc.gov/articles/scammers-pretend-be-your-utility-company) | Hang up; no immediate-payment demands; payment-method red flags; contact utility via the bill's number; report; short list; if paid, reverse | Source read. "If paid" element comes from the linked [FTC: What To Do if You Were Scammed](https://consumer.ftc.gov/articles/what-do-if-you-were-scammed). **Needs 2nd reviewer.** |
| EVAL-SAFE-004 | Online Safety and Scam Prevention | complete_request (zh-TW) | No | **high** | [刑事警察局：ATM解除分期付款詐騙](https://www.cib.npa.gov.tw/ch/app/data/view?module=wg116&id=1909&serno=a61af506-a4ac-49eb-9c79-ef75ddc6f237) | No ATM or transfer or game points; ATM can't cancel installments; hang up and verify or call 165; warning phrases | Source read. The element "if already followed, contact 165 and the bank" is **a reviewer-judgment addition**: the page only says to consult 165. **Needs 2nd reviewer and zh-TW reader.** |
| EVAL-SAFE-005 | Online Safety and Scam Prevention | incomplete_request | **Yes** | medium | [FTC: Mobile Payment Apps](https://consumer.ftc.gov/articles/mobile-payment-apps-how-avoid-scam-when-you-use-one) | Asks which app; no invented menus; double-check recipient; money hard to recover; no passwords | Source read. Page dated May 2022 (modified 2024-04-23). The page has no how-to-send steps, so the scenario tests clarification and safety only. "Only send to people you know" is a **reviewer paraphrase**. **Needs 2nd reviewer.** |

## Mix at a glance (computed from the file)

| Property | Count |
|---|---|
| Records | 15 (5 per family) |
| `clarification_required` = true | 5 of 15: PHONE-002, PHONE-003, COMM-001, COMM-004, SAFE-005 |
| scenario_type | complete_request 4, incomplete_request 3, ambiguous_request 2, failure_recovery 3, recap_request 3 |
| risk_level | low 10, medium 1, high 4 |
| Multi-turn (ends on a user turn) | 2: PHONE-004, SAFE-001 |
| Traditional Chinese | 2: COMM-005, SAFE-004 |

The 33% clarification rate is below the repo's 40% training target on purpose: scenarios where a good answer can safely proceed were not given a forced question.

## Metadata kept outside the record

`schema_v1` has no `language` field, so it is recorded here only: **zh-TW** for EVAL-COMM-005 and EVAL-SAFE-004, **English** for the other 13.

## Open items before freezing

1. Second human reviewer on SAFE-001 to SAFE-005 and a Traditional Chinese reader on COMM-005 and SAFE-004.
2. Recheck the LINE unsend time limit (COMM-005).
3. Device-test the iPhone, Android and Zoom steps on real hardware where possible. The sources were read, not tried on devices.
4. Decide whether the three medium-risk overlap cases in `eval/overlap_report_v1.md` (PHONE-005, COMM-002, shared Control Center steps) are acceptable.
5. Confirm with the team that `expected_elements` may be shown to raters (it is the successor to `notes_for_raters`) and must never be sent to the model.

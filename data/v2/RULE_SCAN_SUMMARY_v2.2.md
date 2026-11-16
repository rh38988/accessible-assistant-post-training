# Rule scan of the other 950 examples (train_v2_en v2.2)

Date: 2026-11-16. Scope: the 950 examples not in the 50-example spot check. Nothing was regenerated or edited; this is a list for people to review.

## How it was done

1. The 22 spot-check fixes (Shirley 15, Ryan 7) were turned into 14 rules: `SPOT_CHECK_RULES_v1.md`.
2. 19 Haiku agents read 50 examples each and flagged rule breaks from the conversation text only (no web pages): `rule_scan/out/part_01..19.jsonl`, instructions in `rule_scan/AGENT_SCANNER.md`.
3. Timing claims (R13) were re-found with one fixed text search, because the agents applied that rule unevenly. 'A few seconds' is not flagged.
4. Examples that still contain a sentence a fix removed were added (`SAME`).
5. All 36 high-severity agent flags were checked by hand, against the official page where needed. 6 were wrong (the page supports the reply), 11 were real but milder (lowered to medium), 19 were confirmed.
6. Built by `tools/finalize_scan.py`; full list in `RULE_SCAN_v2.2.csv` (one row per flag, with quote, reason, suggestion, and check_status).

## How far to trust it

A calibration run on the 50 spot-checked examples (v2.1 text) flagged 14 of Shirley's 15 fixes (missed tr063-d). This is optimistic, because the rules cite those examples. It also flagged 10 of the 35 she kept, mostly low-severity timing or guarantee flags, plus 2 high flags that were wrong. So: high flags marked confirmed are reliable; medium and low flags are candidates, and many are judgment calls.

## Counts

- Examples with at least one open flag: **252 of 950**
- By worst flag: high 15, medium 85, low 152
- Timing phrases alone (R13, text search): 81 examples. These are mechanical: deleting the sentence fixes them.

| Rule | Flags | Examples |
|---|---|---|
| R13 Unsupported specific | 139 | 131 |
| R9 Overgeneralized claim | 38 | 38 |
| R4 Unexplained term | 30 | 30 |
| R5 Recovery without checking | 21 | 21 |
| R8 Distracting detail | 15 | 15 |
| R3 No way to reach the screen | 11 | 11 |
| R12 Data-loss risk not separated | 8 | 8 |
| R14 Risky context ignored | 8 | 8 |
| R6 Device or brand mismatch | 7 | 7 |
| SAME Same text as a fixed example | 7 | 7 |
| R11 Safety instruction that can be misread | 5 | 5 |
| R2 Urgent step missing after the user acted | 5 | 5 |
| R1 Constraint ignored | 4 | 4 |
| R10 Protection depends on an unstated condition | 1 | 1 |

## Confirmed high-severity problems (fix these first)

| ID | Rule | Problem | Suggested fix |
|---|---|---|---|
| tr010-c | R10 | The reply does not warn that signing in on a shared library computer can leave the Apple Account open to the next person. | Library computer; add a step to sign out and not save the password in the browser. |
| tr062-a | R12 | Uninstalling an app can delete the data saved inside it, and the reply does not warn about that, while the iPhone reply on this topic does. | Same problem as tr062-d. |
| tr120-e | R2 | The user has already put in money and cannot withdraw it, yet the time-sensitive exchange step is a conditional last item after the reporting steps. | Reporting to the exchange used is on the FTC page; make it an early, unconditional step and say crypto payments usually can't be reversed. |
| tr173-a | R12 | The reply has the user delete Large or unused files and Files synced to the cloud without warning that these can include personal files or without saying to back up first. | Large or unused files and Files synced to the cloud can hold the user's own files; add a check before removing them. |
| tr173-e | R12 | The steps move irreplaceable family photos off the PC without a copy check, and no step says to confirm the USB copy opens before the originals are removed. | Cut moves the only copy of family photos; safer to Copy, check they open on the USB drive, then delete from the PC. |
| tr197-a | R12 | The steps permanently delete files with no reminder to back up or download anything the user may want to keep first. | Permanent delete with no download-first step (tr197-e shows the safer version). |
| tr197-d | R12 | The user only asked what to do about full storage, yet the steps permanently delete files with no check for a backup or download first. | Same as tr197-a. |
| tr214-c | R9 | Seven calls in seven days is a U.S. presumption of harassment, not an absolute ban, and the reply does not say it applies only in the U.S. | Same frequency-rule simplification Shirley fixed in tr214-g. |
| tr218-a | R11 | Deleting comes before reporting, which could destroy evidence needed for the FTC report. | Delete comes before report (same as tr218-e). |
| tr218-a | R9 | Saying the threats are all talk is broader than what is known, since the sender may have real data from a breach. | 'All talk' (same as tr218-e). |
| tr218-c | R11 | Deleting comes before reporting, which could destroy evidence needed for the FTC report. | Delete comes before report (same as tr218-e). |
| tr218-c | R9 | Calling the claims all talk is broader than what is known, since the sender may have real data from a breach. | 'All talk' (same as tr218-e). |
| tr218-f | R11 | Deleting comes before reporting, which could destroy evidence needed for the FTC report. | Delete comes before report (same as tr218-e). |
| tr218-f | R9 | Calling the claims all talk is broader than what is known, since the sender may have real data from a breach. | 'All talk' (same as tr218-e). |
| tr218-g | R11 | Deleting is told before reporting, which could destroy evidence needed for the FTC report. | Delete comes before report (same as tr218-e). |
| tr218-g | R9 | Calling the claims all talk is broader than what is known, since the sender may have real data from a breach. | 'All talk' (same as tr218-e). |
| tr221-r | R2 | The user already paid $1,800, but the reply leads with reporting and leaves out contacting the card company or bank about the charge, which can be time-limited. | Already paid $1,800; add asking the card company or bank to reverse the charge (FTC 'What To Do if You Were Scammed'). |
| tr223-r | R2 | The user already sent gift cards, but the reply leaves out the time-sensitive step of contacting the gift card company to ask it to freeze the cards. | Gift cards already sent; add contacting the gift card company right away (FTC 'What To Do if You Were Scammed'). |
| tr224-r | R2 | The user already wired money, but the reply leaves out the time-sensitive step of calling the bank or wire company to try to stop or recall the transfer. | Wire already sent; add contacting the wire transfer company or bank to ask for a reversal (FTC 'What To Do if You Were Scammed'). |

## Patterns worth a shared fix

- **Scam tasks after the user already paid (R2):** tr221-r (card or bank), tr223-r (gift cards), tr224-r (wire), tr120-e (crypto exchange). Each needs the time-sensitive step from the FTC 'What To Do if You Were Scammed' page before reporting.
- **Sextortion replies (tr218-a, -c, -f, -g):** 'all talk' and delete-before-report, same as tr218-e. Apply the tr218-e fix.
- **Debt collection (tr214-a, -c, -r):** same simplification as tr214-g; reuse its U.S. framing and frequency wording.
- **Deleting files or apps (R12):** tr173-a, tr173-e, tr197-a, tr197-d, tr062-a. Add a backup or copy check before anything is removed.
- **Timing estimates (R13):** 81 replies open with 'It takes about a minute' or similar. One search-and-delete pass would clear them.

## Not done

- No example was edited. The training file is still v2.2.
- Medium and low flags were not checked by a person. Flags marked `needs_source_check` were not checked against the page except the high ones above.

## Dismissed after checking (page supports the reply)

- tr124-e R12: Apple 102610: 'Deleting or uninstalling an app doesn't remove any documents or other files that you created with the app.'
- tr050-d R9: Apple 101575: 'This message doesn't indicate a safety issue.' See same_text_as_fix tr050-a instead.
- tr078-r R9: Apple 105072: 'If you turn off Emergency Calls & SOS, your Medical ID information will not be shared.'
- tr120-c R9: FTC crypto page: 'Only scammers demand payment in cryptocurrency.'
- tr120-g R9: FTC crypto page: 'Only scammers demand payment in cryptocurrency.'
- tr219-a R9: FTC public Wi-Fi page: 'connecting through a public Wi-Fi network is usually safe.'

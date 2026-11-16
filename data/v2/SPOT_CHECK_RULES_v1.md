# Spot-check rules v1 (from the 50-example human spot check, 2026-11-16)

These rules come from the problems Shirley (15 fixes) and Ryan (7 fixes) found in `spot_check_v2.csv`.
They add to `DATA_RUBRIC_v1.md`; they do not replace it. Each rule names the example it came from.
Use them to flag examples for a person to look at. A flag is not a decision.

Severity: **high** = the user could lose money or data, be less safe, or do the wrong thing.
**medium** = the user probably can't finish the task. **low** = clarity or wording.

| Rule | Flag when | From | Severity |
|---|---|---|---|
| R1 Constraint ignored | The main steps or a fallback use something the user said they can't or don't want to do (a hard-to-press button, a menu they want to avoid, an app they can't use). | tr012-e | medium |
| R2 Urgent step missing after the user acted | The user already sent money, shared a code or password, or let someone in, and the reply leads with prevention or reporting but leaves out the time-sensitive step (stop or intercept the payment, call the bank or carrier, change the password, cut remote access). | tr014-r | high |
| R3 No way to reach the screen | The reply sends the user to a place (Control Center, a folder, a tab, a menu, a settings page) without saying how to get there, or assumes it appears in one fixed spot with no fallback if it doesn't. | tr129-e, tr028-r | medium |
| R4 Unexplained term | A feature name or technical word a low-confidence user may not know is used without a plain explanation (for example Maximum Capacity, Lost Mode, RCS, MMS, VPN, cache, two-factor). | tr050-a | low |
| R5 Recovery without checking | In a failure or follow-up reply, the assistant jumps to a generic fix (update, restart, reset) or gives branches that cannot apply to what the user said, instead of first checking what the user sees. | tr054-r, tr058-r | medium |
| R6 Device or brand mismatch | The user names a brand, model, app, or system (Samsung, Pixel, Outlook, Windows 10), but the reply gives generic steps or another platform's labels. | tr062-d | medium |
| R7 Goal assumed | The request could mean two different tasks and the reply picks one without asking, or the clarifying question asks about the device when the goal is what's unclear. | tr063-d | medium |
| R8 Distracting detail | Version numbers, account requirements, or edge cases that don't help this user finish the task and may confuse them. A short troubleshooting line at the end is fine. | tr103-e | low |
| R9 Overgeneralized claim | A statement broader than the source or than reality: one option unavailable becomes "you can't report it", blocking one number becomes "stops them", a scam claim becomes "all talk", a U.S. rule with exceptions is stated as universal. | tr133-e, tr214-g, tr218-e | high if about money, safety, or the law; otherwise medium |
| R10 Protection depends on an unstated condition | Security or privacy advice only works under a condition the reply doesn't mention (a shared Windows account or PIN, a shared Apple Account, a shared device). | tr192-e | high |
| R11 Safety instruction that can be misread | "Don't pay anything", "delete it", "turn it off" could be read as stopping something the user should keep doing (regular bills, mortgage payments) or as destroying evidence needed to report. | tr224-e, tr218-e | high |
| R12 Data-loss risk not separated | Deleting, resetting, or clearing without separating the device copy from the cloud copy, or without checking a backup first. | tr062-d | high |
| R13 Unsupported specific | A specific duration ("about a minute", "a few minutes"), a guarantee, or a precise claim ("calls from contacts still ring", "you won't be charged") stated as fact with no basis. | tr048-a, tr049-a, tr038-c, tr050-a | low |
| R14 Risky context ignored | The user mentions a risky situation (driving, a stranger on the phone right now, an elderly parent's account) and the reply doesn't address it. | tr054-r | medium |

Not a problem, so do not flag:
- One clarifying question with no steps, when the device or goal is truly unknown.
- Official on-screen labels shown exactly, even if they sound technical, when the reply also says what they do.
- Rough timing words like "a few seconds" (Cian-Rong to confirm).
- General protective advice that the source does not contradict (for example "only share your location with people you trust").

Two of Shirley's notes conflicted with the official pages; the page was followed (see `human_fixes/changes_v2.2.jsonl`, field `page_differs`):
Microsoft's page calls the Snipping Tool control "Snipping Mode", and Apple's Find My page does list "a custom time period".

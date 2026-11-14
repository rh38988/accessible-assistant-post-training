# Assignment: batch ny8b

Spec file: `data/v2/specs/ny8b.py`

SAFETY batch: use the safety table in the spec (suffixes a, c, e, r, f, g). Publishers: FTC consumer advice (consumer.ftc.gov articles and alerts) first; other U.S. government sites where noted.

Write these 6 tasks, 6 examples each. Use the task_id and task_type exactly as given. Each task must use a different official page.

| task_id | task_type | task | platform | category | sensitive |
|---|---|---|---|---|---|
| TR-219 | public_wifi_safety | Is it safe to use public Wi-Fi (FTC) | any | online_services | True |
| TR-220 | unordered_package_scam | A package arrives that the user never ordered (FTC or uspis.gov) | any | online_services | True |
| TR-221 | timeshare_resale_scam | A company promises to sell the user's timeshare for an upfront fee (FTC) | any | online_services | True |
| TR-222 | money_mule_scam | Someone asks the user to receive money and forward it (FTC) | any | online_services | True |
| TR-223 | rental_listing_scam | A rental listing asks for a deposit before any viewing (FTC) | any | online_services | True |
| TR-224 | mortgage_relief_scam | A company promises to stop foreclosure for an upfront fee (FTC or consumerfinance.gov) | any | online_services | True |

Backup topics (if a topic's page cannot be read or does not cover the core action, replace it with one of these and reuse that topic's task_id; if you run out, deliver fewer tasks):

- moving_scam | A moving company demands more money before delivering belongings (fmcsa.dot.gov or FTC) | any | online_services | True
- veterans_benefit_scam | Someone offers to help with veterans benefits for a fee (FTC or va.gov) | any | online_services | True

Tasks marked sensitive True that are about settings or accounts (not scams) still use the normal device table (a, c, b, d, e, r).

Notes: Do NOT write about these reserved topics: tech support scams, bank impersonation, Medicare scams, utility shut-off scams, prize or lottery scams, charity scams, job scams, fake shopping sites, health product scams, subscription renewal scams, payment-app scams (Zelle, Venmo), QR code payment scams, company impersonation, telecom impersonation, hacked accounts, data breach notices, credit freezes. The six examples in a task must be six clearly different situations. Lead with the protective action; never ask a question before it.

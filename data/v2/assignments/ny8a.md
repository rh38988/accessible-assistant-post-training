# Assignment: batch ny8a

Spec file: `data/v2/specs/ny8a.py`

SAFETY batch: use the safety table in the spec (suffixes a, c, e, r, f, g). Publishers: FTC consumer advice (consumer.ftc.gov articles and alerts) first; other U.S. government sites where noted.

Write these 7 tasks, 6 examples each. Use the task_id and task_type exactly as given. Each task must use a different official page.

| task_id | task_type | task | platform | category | sensitive |
|---|---|---|---|---|---|
| TR-212 | fake_check_scam | Someone sends a check and asks the user to send part of the money back (FTC) | any | online_services | True |
| TR-213 | home_improvement_scam | A contractor at the door pushes for a quick repair deal and upfront payment (FTC) | any | online_services | True |
| TR-214 | fake_debt_collector | A caller demands payment for a debt the user does not recognize (FTC) | any | online_services | True |
| TR-215 | toll_text_scam | A text says the user owes an unpaid road toll (FTC consumer alert) | any | online_services | True |
| TR-216 | government_impersonation | A call or message claims to be the IRS and demands payment (IRS.gov or FTC) | any | online_services | True |
| TR-217 | government_impersonation | A caller says the user missed jury duty and must pay a fine (FTC or uscourts.gov) | any | online_services | True |
| TR-218 | extortion_email_scam | An email claims to have embarrassing video or a password and demands payment (FTC) | any | online_services | True |

Backup topics (if a topic's page cannot be read or does not cover the core action, replace it with one of these and reuse that topic's task_id; if you run out, deliver fewer tasks):

- caller_id_spoofing | A call shows a familiar or local number but is not who it claims (fcc.gov) | any | online_services | True
- ticket_scam | Buying event tickets from a reseller online (FTC) | any | online_services | True

Tasks marked sensitive True that are about settings or accounts (not scams) still use the normal device table (a, c, b, d, e, r).

Notes: Do NOT write about these reserved topics: tech support scams, bank impersonation, Medicare scams, utility shut-off scams, prize or lottery scams, charity scams, job scams, fake shopping sites, health product scams, subscription renewal scams, payment-app scams (Zelle, Venmo), QR code payment scams, company impersonation, telecom impersonation, hacked accounts, data breach notices, credit freezes. The six examples in a task must be six clearly different situations. Lead with the protective action; never ask a question before it.

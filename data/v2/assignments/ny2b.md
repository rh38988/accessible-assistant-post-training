# Assignment: batch ny2b

Spec file: `data/v2/specs/ny2b.py`

Publisher: Apple (support.apple.com). Prefer pages with URLs like support.apple.com/en-us/1xxxxx; pages under support.apple.com/guide/ often cannot be read by WebFetch.

Write these 6 tasks, 6 examples each. Use the task_id and task_type exactly as given. Each task must use a different official page.

| task_id | task_type | task | platform | category | sensitive |
|---|---|---|---|---|---|
| TR-141 | voicemail | Set up and listen to voicemail | iPhone | communication | False |
| TR-142 | call_forwarding | Forward calls to another number | iPhone | communication | False |
| TR-143 | flash_alerts | Make the light flash for calls and alerts | iPhone | technical_support | False |
| TR-144 | find_model | Find out which iPhone model it is | iPhone | technical_support | False |
| TR-145 | scan_document | Scan a paper document with the phone | iPhone | technical_support | False |
| TR-146 | home_screen_organize | Move apps and organize the Home Screen | iPhone | technical_support | False |

Backup topics (if a topic's page cannot be read or does not cover the core action, replace it with one of these and reuse that topic's task_id; if you run out, deliver fewer tasks):

- restart_phone | Restart the iPhone (a normal restart) | iPhone | technical_support | False
- liquid_detected | The phone shows a liquid detected alert when charging | iPhone | technical_support | False

Tasks marked sensitive True that are about settings or accounts (not scams) still use the normal device table (a, c, b, d, e, r).

Notes: For troubleshooting tasks, the direct answer is the source's troubleshooting sequence in order.

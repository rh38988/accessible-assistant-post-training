# Assignment: batch ny1b

Spec file: `data/v2/specs/ny1b.py`

Publisher: Apple (support.apple.com). Prefer pages with URLs like support.apple.com/en-us/1xxxxx; pages under support.apple.com/guide/ often cannot be read by WebFetch.

Write these 6 tasks, 6 examples each. Use the task_id and task_type exactly as given. Each task must use a different official page.

| task_id | task_type | task | platform | category | sensitive |
|---|---|---|---|---|---|
| TR-128 | bluetooth_pair | Pair a Bluetooth accessory such as headphones or a speaker | iPhone | technical_support | False |
| TR-129 | bluetooth_pair | Connect a Bluetooth device | Mac | technical_support | False |
| TR-130 | two_step_verification | Turn on two-factor authentication for the Apple Account | iPhone | online_services | True |
| TR-131 | password_manager | Save and find passwords (Passwords app or iCloud Keychain) | iPhone | online_services | True |
| TR-132 | force_restart | iPad is frozen or will not respond | iPad | technical_support | False |
| TR-133 | report_spam_text | Report and block junk text messages | iPhone | online_services | True |

Backup topics (if a topic's page cannot be read or does not cover the core action, replace it with one of these and reuse that topic's task_id; if you run out, deliver fewer tasks):

- display_scale | Make everything on screen bigger with Display Zoom | iPhone | technical_support | False
- internet_not_working | Mac will not connect to the internet over Wi-Fi | Mac | technical_support | False

Tasks marked sensitive True that are about settings or accounts (not scams) still use the normal device table (a, c, b, d, e, r).

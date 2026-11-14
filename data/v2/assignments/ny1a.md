# Assignment: batch ny1a

Spec file: `data/v2/specs/ny1a.py`

Publisher: Apple (support.apple.com). Prefer pages with URLs like support.apple.com/en-us/1xxxxx; pages under support.apple.com/guide/ often cannot be read by WebFetch.

Write these 7 tasks, 6 examples each. Use the task_id and task_type exactly as given. Each task must use a different official page.

| task_id | task_type | task | platform | category | sensitive |
|---|---|---|---|---|---|
| TR-121 | screenshot | Take a screenshot | iPad | technical_support | False |
| TR-122 | software_update | Update the Mac's software (macOS) | Mac | technical_support | False |
| TR-123 | wifi_connect | Connect to a Wi-Fi network | Mac | technical_support | False |
| TR-124 | delete_app | Delete (uninstall) an app | Mac | technical_support | False |
| TR-125 | free_storage | Free up storage space | Mac | technical_support | False |
| TR-126 | battery_saver | Turn on Low Power Mode | Mac laptop | technical_support | False |
| TR-127 | backup_computer | Back up the Mac with Time Machine | Mac | technical_support | False |

Backup topics (if a topic's page cannot be read or does not cover the core action, replace it with one of these and reuse that topic's task_id; if you run out, deliver fewer tasks):

- phone_not_charging | iPad will not charge | iPad | technical_support | False
- add_printer | Add a printer | Mac | technical_support | False

Tasks marked sensitive True that are about settings or accounts (not scams) still use the normal device table (a, c, b, d, e, r).

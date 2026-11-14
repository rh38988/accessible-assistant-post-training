# Assignment: batch ny4a

Spec file: `data/v2/specs/ny4a.py`

Publishers: Samsung US support (www.samsung.com/us/support/answer/...) for Galaxy tasks; Chromebook Help (support.google.com/chromebook) for Chromebook tasks. Samsung pages can be hard to read: try twice with a specific question, then use a backup.

Write these 7 tasks, 6 examples each. Use the task_id and task_type exactly as given. Each task must use a different official page.

| task_id | task_type | task | platform | category | sensitive |
|---|---|---|---|---|---|
| TR-160 | screenshot | Take a screenshot | Samsung Galaxy | technical_support | False |
| TR-161 | software_update | Update the phone's software | Samsung Galaxy | technical_support | False |
| TR-162 | wifi_connect | Connect to a Wi-Fi network | Samsung Galaxy | technical_support | False |
| TR-163 | block_number | Block a phone number | Samsung Galaxy | communication | False |
| TR-164 | flashlight | Turn the flashlight on and off | Samsung Galaxy | technical_support | False |
| TR-165 | easy_mode | Turn on Easy mode for bigger icons and a simpler screen | Samsung Galaxy | technical_support | False |
| TR-166 | find_lost_phone | Find a lost phone | Samsung Galaxy | technical_support | True |

Backup topics (if a topic's page cannot be read or does not cover the core action, replace it with one of these and reuse that topic's task_id; if you run out, deliver fewer tasks):

- force_restart | The phone is frozen or will not respond | Samsung Galaxy | technical_support | False
- phone_not_charging | The phone will not charge | Samsung Galaxy | technical_support | False

Tasks marked sensitive True that are about settings or accounts (not scams) still use the normal device table (a, c, b, d, e, r).

# Assignment: batch ny4b

Spec file: `data/v2/specs/ny4b.py`

Publishers: Samsung US support (www.samsung.com/us/support/answer/...) for Galaxy tasks; Chromebook Help (support.google.com/chromebook) for Chromebook tasks. Samsung pages can be hard to read: try twice with a specific question, then use a backup.

Write these 6 tasks, 6 examples each. Use the task_id and task_type exactly as given. Each task must use a different official page.

| task_id | task_type | task | platform | category | sensitive |
|---|---|---|---|---|---|
| TR-167 | battery_saver | Turn on power saving mode | Samsung Galaxy | technical_support | False |
| TR-168 | screenshot | Take a screenshot | Chromebook | technical_support | False |
| TR-169 | wifi_connect | Connect to a Wi-Fi network | Chromebook | technical_support | False |
| TR-170 | software_update | Update the Chromebook | Chromebook | technical_support | False |
| TR-171 | magnifier | Zoom in or magnify the screen | Chromebook | technical_support | False |
| TR-172 | read_aloud | Have text read aloud (Select-to-speak) | Chromebook | technical_support | False |

Backup topics (if a topic's page cannot be read or does not cover the core action, replace it with one of these and reuse that topic's task_id; if you run out, deliver fewer tasks):

- add_printer | Set up a printer | Chromebook | technical_support | False
- mouse_pointer_size | Make the mouse pointer bigger | Chromebook | technical_support | False

Tasks marked sensitive True that are about settings or accounts (not scams) still use the normal device table (a, c, b, d, e, r).

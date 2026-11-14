# Assignment: batch ny2a

Spec file: `data/v2/specs/ny2a.py`

Publisher: Apple (support.apple.com). Prefer pages with URLs like support.apple.com/en-us/1xxxxx; pages under support.apple.com/guide/ often cannot be read by WebFetch.

Write these 7 tasks, 6 examples each. Use the task_id and task_type exactly as given. Each task must use a different official page.

| task_id | task_type | task | platform | category | sensitive |
|---|---|---|---|---|---|
| TR-134 | email_not_working | Cannot send or receive email in the Mail app | iPhone | communication | False |
| TR-135 | messages_not_sending | Text messages will not send or arrive | iPhone | communication | False |
| TR-136 | no_service | Phone shows No Service or SOS | iPhone | technical_support | False |
| TR-137 | touchscreen_unresponsive | The screen does not respond to touch | iPhone | technical_support | False |
| TR-138 | overheating | The phone is too hot or shows a temperature warning | iPhone | technical_support | False |
| TR-139 | date_time | Fix the wrong date or time | iPhone | technical_support | False |
| TR-140 | brightness | Make the screen brighter or dimmer | iPhone | technical_support | False |

Backup topics (if a topic's page cannot be read or does not cover the core action, replace it with one of these and reuse that topic's task_id; if you run out, deliver fewer tasks):

- popups | Block pop-ups in Safari | iPhone | technical_support | False
- magnifier | Use the phone as a magnifying glass | iPhone | technical_support | False

Tasks marked sensitive True that are about settings or accounts (not scams) still use the normal device table (a, c, b, d, e, r).

Notes: For troubleshooting tasks, the direct answer is the source's troubleshooting sequence in order.

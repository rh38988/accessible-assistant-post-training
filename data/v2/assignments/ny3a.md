# Assignment: batch ny3a

Spec file: `data/v2/specs/ny3a.py`

Publisher: Google (support.google.com: Android Help, Pixel Phone Help, Google Messages Help, Phone app Help).

Write these 7 tasks, 6 examples each. Use the task_id and task_type exactly as given. Each task must use a different official page.

| task_id | task_type | task | platform | category | sensitive |
|---|---|---|---|---|---|
| TR-147 | force_restart | The phone is frozen or will not respond | Android | technical_support | False |
| TR-148 | phone_not_charging | The phone will not charge | Android (Pixel) | technical_support | False |
| TR-149 | internet_not_working | The phone cannot connect to the internet | Android | technical_support | False |
| TR-150 | messages_not_sending | Text messages will not send or arrive | Android (Google Messages) | communication | False |
| TR-151 | group_text | Send a group text | Android (Google Messages) | communication | False |
| TR-152 | report_spam_text | Report and block spam texts | Android (Google Messages) | online_services | True |
| TR-153 | voicemail | Set up and check voicemail | Android (Phone app) | communication | False |

Backup topics (if a topic's page cannot be read or does not cover the core action, replace it with one of these and reuse that topic's task_id; if you run out, deliver fewer tasks):

- flash_alerts | Make the screen or light flash for notifications | Android | technical_support | False
- display_scale | Make everything on screen bigger (display size) | Android | technical_support | False

Tasks marked sensitive True that are about settings or accounts (not scams) still use the normal device table (a, c, b, d, e, r).

Notes: Android pages often say settings differ by phone; when the page says so, the reply may say it too. For troubleshooting tasks, the direct answer is the source's troubleshooting sequence in order. For brightness, write only about brightness (not dark theme, night light, or screen timeout).

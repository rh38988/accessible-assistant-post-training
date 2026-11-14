# Assignment: batch ny3b

Spec file: `data/v2/specs/ny3b.py`

Publisher: Google (support.google.com: Android Help, Pixel Phone Help, Google Messages Help, Phone app Help).

Write these 6 tasks, 6 examples each. Use the task_id and task_type exactly as given. Each task must use a different official page.

| task_id | task_type | task | platform | category | sensitive |
|---|---|---|---|---|---|
| TR-154 | bluetooth_pair | Pair a Bluetooth accessory | Android | technical_support | False |
| TR-155 | brightness | Make the screen brighter or dimmer | Android | technical_support | False |
| TR-156 | date_time | Fix the wrong date or time | Android | technical_support | False |
| TR-157 | home_screen_organize | Add and move apps on the Home screen | Android | technical_support | False |
| TR-158 | stolen_device_protection | Turn on theft protection | Android | technical_support | True |
| TR-159 | wifi_calling | Make calls over Wi-Fi | Android | communication | False |

Backup topics (if a topic's page cannot be read or does not cover the core action, replace it with one of these and reuse that topic's task_id; if you run out, deliver fewer tasks):

- touchscreen_unresponsive | The screen does not respond to touch | Android | technical_support | False
- call_forwarding | Forward calls to another number | Android (Phone app) | communication | False

Tasks marked sensitive True that are about settings or accounts (not scams) still use the normal device table (a, c, b, d, e, r).

Notes: Android pages often say settings differ by phone; when the page says so, the reply may say it too. For troubleshooting tasks, the direct answer is the source's troubleshooting sequence in order. For brightness, write only about brightness (not dark theme, night light, or screen timeout).

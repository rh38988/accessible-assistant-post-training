# fx5 generation report

Sources (all fetched once, same URL as in ex5.py): TR-062 support.google.com/android/answer/7431795; TR-063 support.apple.com/en-us/105001; TR-064 support.google.com/android/answer/9083864; TR-066 support.apple.com/en-us/118444; TR-067 support.google.com/android/answer/2840926; TR-068 support.apple.com/en-us/108780; TR-069 support.google.com/android/answer/9417604; TR-070 support.apple.com/en-us/101604; TR-071 support.google.com/android/answer/7664692; TR-072 support.apple.com/en-us/102629; TR-073 support.google.com/accessibility/android/answer/6006949; TR-074 support.apple.com/en-us/101593; TR-075 support.google.com/accounts/answer/6160491.

Backups: none. TR-074 and TR-075 are flagged sensitive but are device tasks, so r is failure_recovery, not already_acted.

Not fully sure the page supports:
- TR-064 e/r: the page never names a Flashlight tile (generic Quick Settings Edit/Add/drag only).
- TR-070 e: wording "Siri, turn on Low Power Mode" is the page's phrase for on; off uses "Hey Siri".
- TR-071 r: troubleshooting steps come from the "Fix battery problems" section inside the page.
- TR-074 r: Lost Mode while offline is implied by the page (not shows as in Lost Mode until reconnects); Lost section label is "Lost [Device]" on the page.
- TR-068 e: "rechargeable, no switch: remove from charger" is from the page.

Existing examples the source shows are wrong or unsupported:
- tr073-a / tr073-c: "It can zoom up to 8 times" is not on the page; "pressing both volume keys" vs page "Hold volume keys".
- tr064-a / tr064-c / tr064-d: "edit icon (a pencil)" not on page (page says Edit); Flashlight tile not named by page.
- tr066-a / c / d: "plus (+) button" not on page (page says Add button); "Tap Save (on some versions Done)" page says Done.
- tr071-a / c / d: nothing contradicted, but the Quick-tile claim is absent (fine).

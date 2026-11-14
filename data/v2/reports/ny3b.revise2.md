# Revise report: batch ny3b, round 2 (revise2)

Revision list: data/v2/reviews/input/ny3b.revise2.md (2 examples)

## Fixed
- tr154-e (Pair a Bluetooth accessory, keyboard constraint): added the fallback for a passcode prompt at step 5 ("If the keyboard asks for a passcode and you don't have one, try 0000 or 1234."). Source checked: https://support.google.com/android/answer/9417604 says "If you're asked for a passcode and don't have it, try the most common ones like "0000" or "1234."" Other steps unchanged.
- tr159-e (Make calls over Wi-Fi, no mobile plan): added the notification cue ("When you are connected to the internet, the notification screen shows Internet Call or Wi-Fi calling.") after step 6, and the charges sentence at the end of the reply. Source checked: https://support.google.com/phoneapp/answer/2811843 confirms the notification wording and "You may incur additional charges for making calls over Wi-Fi, so check with your mobile service provider for details." Menu path unchanged.

## Could not fix
- None.

## Follow-ups touched
- None.

## Contradictions with reviewer
- None. Both pages matched the reviewer's notes.

## Builder
- `python3 data/v2/tools/build_v2.py ny3b` prints OK.
- Remaining warning, not on this list and left unchanged: tr159-r, reply is very short (19 words).

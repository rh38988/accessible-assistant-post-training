# Revision list: batch ny3b, after review round 1 (3 examples)

Edit ONLY these examples in data/v2/specs/ny3b.py, then rebuild.

## tr154-e
- reasons: Unsupported claim about tapping the icon once; contradicts the touch-and-hold step as written on the page.
- fix requested: Delete the sentence 'If the Bluetooth icon is off, tap it once to turn Bluetooth on.' Keep only the Airplane mode note, e.g. 'Bluetooth is off while Airplane mode is on, so turn Airplane mode off before you pair.'
- unsupported claims: 'If the Bluetooth icon is off, tap it once to turn Bluetooth on.' -> the page only says to touch and hold the Bluetooth icon; it never says a single tap turns Bluetooth on.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/android/answer/9417604

## tr158-e
- reasons: The android.com/lock instructions are packed into one run-on sentence with four separate actions (S4), and 'reCAPTCHA' is unexplained jargon for this audience (S5). Content matches the page.
- fix requested: Rewrite the last paragraph as a short numbered list: 'To lock the phone later, use your laptop: 1. Go to android.com/lock. 2. Enter your phone number. 3. Complete the security check (reCaptcha) that appears. 4. Request the lock. The phone screen locks shortly after.' Do not add any description of what the reCaptcha looks like beyond what the page says.
- low scores: {'actionable': 1, 'plain': 1} | gates not passed: {}
- sources: https://support.google.com/android/answer/15146908

## tr159-e
- reasons: The page says some carriers allow Wi-Fi calling without service, 'otherwise, you need a carrier for this to work'. The reply gives only the hopeful half, so a user with no plan is not told it may not work at all.
- fix requested: After 'Some carriers let you use Wi-Fi calling without a mobile service plan.' add 'If yours does not, you need a mobile service plan for calls to work.' Keep the final line 'If you don't see Wi-Fi calling, your carrier doesn't support it,' and add 'Ask your carrier to confirm.'
- required actions missing from the reply: Some carriers allow Wi-Fi calling without a service plan; otherwise a carrier is needed
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://support.google.com/phoneapp/answer/2811843

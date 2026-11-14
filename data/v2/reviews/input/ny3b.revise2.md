# Revision list: batch ny3b, after review round 2 (2 examples)

Edit ONLY these examples in data/v2/specs/ny3b.py, then rebuild.

## tr154-e
- reasons: The source says that if a passcode is asked for and none is known, common codes such as 0000 or 1234 can be tried. The reply leaves out this fallback, which a keyboard pairing can hit at the Follow the on-screen prompts step.
- fix requested: In step 5 of the reply, change 'Follow the on-screen prompts.' to 'Follow the on-screen prompts. If the keyboard asks for a passcode and you don't have one, try 0000 or 1234.' Keep every other step and sentence unchanged.
- required actions missing from the reply: If asked for a passcode and none is known, try 0000 or 1234 (non-critical)
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://support.google.com/android/answer/9417604

## tr159-e
- reasons: The reply does not say what the user will see when a call is made over Wi-Fi, although the source gives the 'Internet Call' or 'Wi-Fi calling' notification cue (S4). It also omits the source's warning that Wi-Fi calls may incur charges, which matters for a user with no mobile service plan (S1).
- fix requested: After step 6 of the reply (Turn on Wi-Fi calling), add the line: 'When you are connected to the internet, the notification screen shows Internet Call or Wi-Fi calling.' After the carrier-support sentence, add: 'You may incur additional charges for calls over Wi-Fi, so check with your mobile service provider for details.' Keep the menu path and all other sentences unchanged.
- required actions missing from the reply: When connected to the internet, the notification screen shows 'Internet Call' or 'Wi-Fi calling' (non-critical) | Calls over Wi-Fi may incur charges, so check with the mobile service provider (non-critical)
- low scores: {'steps': 1, 'actionable': 1} | gates not passed: {}
- sources: https://support.google.com/phoneapp/answer/2811843

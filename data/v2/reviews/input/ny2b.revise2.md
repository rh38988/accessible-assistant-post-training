# Revision list: batch ny2b, after review round 2 (3 examples)

Edit ONLY these examples in data/v2/specs/ny2b.py, then rebuild.

## tr141-e
- reasons: All claims are supported (Siri page: 'Say “Siri” or “Hey Siri”'; 'Tap Turn On Siri'; voicemail page: Voicemail, Play button, and both Siri example phrases). One non-critical required action is missing: the voicemail page says the first time you tap Voicemail you must tap "Set Up Now", create a voicemail password, and choose a greeting. Without this, the Siri voicemail commands have nothing to play for a phone that was never set up. The task name is 'Set up and listen to voicemail', so the set-up step belongs in the reply.
- fix requested: Add one short sentence after the Siri tips, for example: "If voicemail was never set up on this phone, ask a helper to open Phone, tap Voicemail, tap Set Up Now, create a voicemail password, and choose a greeting." Source for the claim: https://support.apple.com/en-kz/guide/iphone/check-voicemail-iph3c99490e/14.0 ("The first time you tap Voicemail, tap 'Set Up Now,' create a voicemail password, and choose a greeting: Default or Custom."). Keep the rest of the reply unchanged.
- required actions missing from the reply: If voicemail was never set up: Phone, Voicemail, Set Up Now, create a voicemail password, choose a greeting (not covered)
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://support.apple.com/en-kz/guide/iphone/check-voicemail-iph3c99490e/14.0 ; https://support.apple.com/guide/iphone/turn-on-and-activate-siri-iph83aad8922/ios

## tr142-c
- reasons: All steps match the page, and the page supports the range requirement, the 'Forward To' and 'Back' steps, and the status-bar indicator (the reply's 'top of the screen' is the same area). The plain-language score fails on the last paragraph: "Call forwarding works on GSM networks. If you use a CDMA network, contact your carrier." GSM and CDMA are unexplained jargon for this user, and the first sentence is not needed to act. The page itself says 'on GSM networks' and 'If you have cellular service through a CDMA network, you should contact your carrier for setup information.'
- fix requested: Replace the last paragraph's network sentence with: "If your phone service uses a CDMA network, ask your carrier for setup information." Keep everything else. Source: https://support.apple.com/en-ca/guide/iphone/iph7405291c4/ios
- low scores: {'plain': 1} | gates not passed: {}
- sources: https://support.apple.com/en-ca/guide/iphone/iph7405291c4/ios

## tr143-r
- reasons: Settings path (Settings, Accessibility, Audio/Visual, LED Flash for Alerts), the 'works only when locked' rule, the light beside the camera lens, and the notification cue all match https://support.apple.com/en-us/111774. The failure: the recovery step tells the user that a dark screen means the phone is locked. The page does not say that, and the reply gives no supported way to lock the phone. Because step 1 of the recovery is not supported, the source gate fails.
- fix requested: Replace the first recovery step "Put the phone down and let the screen go dark so it is locked." with "Put the phone down and lock it." Do not describe a button for locking, because the source page does not give one; if the reply must name the lock method, add a second source from Apple support on locking an iPhone and cite it. Keep the rest of the reply unchanged, since its other statements match the source. Source: https://support.apple.com/en-us/111774
- unsupported claims: "Put the phone down and let the screen go dark so it is locked." -> the page says the flash works only when the device is locked and does not mention the screen going dark or any way to lock the phone; equating a dark screen with a locked phone is not on the page.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/111774

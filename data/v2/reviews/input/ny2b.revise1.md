# Revision list: batch ny2b, after review round 1 (7 examples)

Edit ONLY these examples in data/v2/specs/ny2b.py, then rebuild.

## tr141-e
- reasons: User cannot tap well; the reply says 'ask Siri' but never says how to start Siri, so there is no clear starting point. The cited voicemail page does not say how to activate Siri.
- fix requested: Add a first step telling the user how to wake Siri hands-free, taken from https://support.apple.com/guide/iphone/turn-on-and-activate-siri-iph83aad8922/ios (for example saying 'Hey Siri', only as that page states it, and noting that Siri must be turned on in settings if it does not answer). Add that URL as a second source. Keep the two example phrases exactly as they are.
- required actions missing from the reply: Know how to start Siri (the page assumes Siri is already listening)
- low scores: {'actionable': 1} | gates not passed: {}
- sources: https://support.apple.com/en-kz/guide/iphone/check-voicemail-iph3c99490e/14.0

## tr142-c
- reasons: Dual SIM step is in the wrong order, and step 6 bundles tapping Forward To with typing the number.
- fix requested: Reorder: 5 Turn on Call Forwarding; 6 Because your iPhone has Dual SIM, choose a line (below SIMs); 7 Tap Forward To; 8 Type your son's number; 9 Tap Back. Keep the range note and the status-bar icon sentence. Optionally add one short line that call forwarding works on GSM networks only (page: contact your carrier if CDMA).
- unsupported claims: '6. Tap Forward To and type in your son's number. 7. Because your iPhone has two SIMs, choose the line you want to forward. 8. Tap Back.' -> the page puts the Dual SIM line choice (below SIMs) right after turning on Call Forwarding and BEFORE tapping Forward To; the reply puts it after.
- required actions missing from the reply: If Dual SIM, choose a line (below SIMs) BEFORE Forward To
- low scores: {'steps': 1, 'actionable': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-ca/guide/iphone/iph7405291c4/ios

## tr143-r
- reasons: One unsupported control instruction.
- fix requested: In step 1 delete 'Press the side button to lock the phone, or'. Use only: 'Put the phone down and let the screen go dark so it is locked.'
- unsupported claims: 'Press the side button to lock the phone' -> the cited page never says how to lock the phone or names the side button.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/111774

## tr144-a
- reasons: Two unsupported closing claims.
- fix requested: Delete both closing sentences. End after step 5, optionally with 'Use that number when you sell the phone.'
- unsupported claims: 'The model number starts with the letter A and four digits.' -> page does not describe the format. | 'You can match it against Apple's list of iPhone models to see which model you have.' -> not stated on the cited page.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/106343

## tr144-c
- reasons: Unsupported format claim and unsupported statement about not turning the phone on.
- fix requested: Delete both sentences. Answer: 'Yes. On an iPhone 7 or earlier, the model number is on the back of the phone.' then steps 1 and 2 as written. The user can see this is the back-of-phone method without needing it turned on; you may say 'This method looks at the back of the phone itself' only if you keep it to that.
- unsupported claims: 'The model number starts with the letter A and four digits.' -> not on the page. | 'You do not need to turn the phone on.' -> page does not say this.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/106343

## tr144-d
- reasons: Unsupported format claim.
- fix requested: Replace the last paragraph with 'You can tell the store that number.' Remove the sentence about the letter A and four digits.
- unsupported claims: 'The model number starts with the letter A and four digits.' -> page does not describe the format.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/106343

## tr144-e
- reasons: Unsupported format claim; unlock statement not on page.
- fix requested: Delete the letter A sentence. Change the opening to 'Yes. On an iPhone 8 or later with a SIM tray, you can look inside the SIM tray slot.' Keep the three steps. Optionally say step 2 means 'a place with bright light overhead'.
- unsupported claims: 'The model number starts with the letter A and four digits.' -> page does not describe the format. | 'Yes, you do not need to unlock the phone.' -> page does not state this.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/106343

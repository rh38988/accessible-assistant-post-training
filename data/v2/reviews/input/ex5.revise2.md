# Revision list: batch ex5, after review round 2 (5 examples)

Edit ONLY these examples in data/v2/specs/ex5.py, then rebuild.

## tr073-c
- reasons: The opening claim that magnification leaves how the app looks unchanged the rest of the time is not on the page (the page does not discuss app appearance or text size when magnification is off).
- fix requested: Replace the first sentence of the reply ("Magnification is a good fit for that: it zooms in only when you need it and doesn't change how the app looks the rest of the time.") with a sentence that uses only supported facts, for example: "Magnification can help with that. It zooms in on the whole screen, and you turn it on and off with your shortcut." Keep the rest of the reply unchanged.
- unsupported claims: "Magnification is a good fit for that: it zooms in only when you need it and doesn't change how the app looks the rest of the time." -> the page says nothing about how apps look or about text size or layout when magnification is off; it only says the shortcut stops magnification. Only the part 'you use the shortcut to turn it on and off' is supported.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/accessibility/android/answer/6006949?hl=en

## tr074-a
- reasons: Unsupported description of what the user sees after selecting the iPhone (a map).
- fix requested: Change "Select your iPhone to see it on a map." to "Select your iPhone to locate it." The page only says Find My can be used to locate devices; it does not describe a map. Keep every other step as it is.
- unsupported claims: "Select your iPhone to see it on a map." -> the page does not mention a map or describe what the screen shows after a device is selected; it only says to use Find My to locate devices.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/101593

## tr074-c
- reasons: Unsupported description of what the user sees after selecting the iPhone (a map).
- fix requested: Change "Select your iPhone to see it on a map." to "Select your iPhone to locate it." The page only says Find My can be used to locate devices; it does not describe a map. Keep every other step as it is.
- unsupported claims: "Select your iPhone to see it on a map." -> the page does not mention a map or describe what the screen shows after a device is selected; it only says to use Find My to locate devices.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/101593

## tr075-a
- reasons: The locating condition is taken from the page's securing or erasing checklist, and the PIN or password prompt is mislabelled.
- fix requested: Replace "It works if your phone is on and connected to the internet." with "It works best when your phone is on and connected. If its current location can't be found, Find Hub may show its last known location." The page lists the power and connection conditions only for securing or erasing the phone, not for locating it. Replace "enter your lock screen PIN or password" with "enter your lock screen PIN", and add "If the phone has no PIN, or runs Android 8 or lower, you may be asked for your Google password." Keep every other sentence unchanged.
- unsupported claims: "It works if your phone is on and connected to the internet." -> the page lists power and a data or Wi-Fi connection only as conditions for securing or erasing; for locating it gives no such condition and mentions last known location instead. | "If asked, enter your lock screen PIN or password." -> the page says the lock screen PIN is requested (Android 9 or higher); a Google password is requested only when the phone has no PIN or runs Android 8 or lower. The reply does not say this.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/accounts/answer/6160491?hl=en

## tr075-d
- reasons: The locating condition is taken from the page's securing or erasing checklist, and the PIN or password prompt is mislabelled.
- fix requested: Replace "It works if your phone is on and connected to the internet." with "It works best when your phone is on and connected. If its current location can't be found, Find Hub may show its last known location." The page lists the power and connection conditions only for securing or erasing the phone, not for locating it. Replace "enter your lock screen PIN or password" with "enter your lock screen PIN", and add "If the phone has no PIN, or runs Android 8 or lower, you may be asked for your Google password." Keep every other sentence unchanged.
- unsupported claims: "It works if your phone is on and connected to the internet." -> the page lists power and a data or Wi-Fi connection only as conditions for securing or erasing; for locating it gives no such condition and mentions last known location instead. | "If asked, enter your lock screen PIN or password." -> the page says the lock screen PIN is requested (Android 9 or higher); a Google password is requested only when the phone has no PIN or runs Android 8 or lower. The reply does not say this.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/accounts/answer/6160491?hl=en

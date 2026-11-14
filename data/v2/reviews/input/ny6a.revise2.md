# Revision list: batch ny6a, after review round 2 (5 examples)

Edit ONLY these examples in data/v2/specs/ny6a.py, then rebuild.

## tr188-a
- reasons: The menu steps are supported. The keyboard shortcut is supported only for Windows, and the user only said Edge on a computer.
- fix requested: Change the last sentence to name the platform, for example: 'On Windows, you can also hold the Ctrl key and press the plus sign key.' Or delete that sentence. Do not add a Mac shortcut, because the page does not give one.
- unsupported claims: 'You can also hold the **Ctrl** key and press the **plus sign** key.' -> the page gives Ctrl+Plus only in a section headed 'Making a web page bigger in Edge (Windows)'; the reply does not say the shortcut is for Windows, and the page gives no Ctrl shortcut for other computers
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.microsoft.com/en-us/microsoft-edge/accessibility-features-in-microsoft-edge-4c696192-338e-9465-b2cd-bd9b698ad19a

## tr188-r
- reasons: The menu path (Settings and more, then Zoom out) is supported. The Ctrl+0 shortcut is supported only for Windows and the reply does not say so.
- fix requested: Say the shortcut is for Windows, for example: 'On Windows, hold down the Ctrl key and press the 0 key. That resets the page to the default size.' Keep the Settings and more then Zoom out option as written. Do not add a Mac shortcut.
- unsupported claims: 'Hold down the **Ctrl** key and press the **0** key. That resets the page to the default size.' -> the page lists Ctrl+0 only in a section headed 'Making a web page bigger in Edge (Windows)'; the reply does not say it is a Windows shortcut
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.microsoft.com/en-us/microsoft-edge/accessibility-features-in-microsoft-edge-4c696192-338e-9465-b2cd-bd9b698ad19a

## tr192-a
- reasons: The final-steps path is supported except for the item selected under Passwords. The page says select the password, so the reply's step does not match the page.
- fix requested: In the 'To find it later' list, change step 3 to: 'Under **Passwords**, select the password.' Keep every other step as written.
- unsupported claims: 'Under **Passwords**, select the site.' -> the page says to select the password entry under Passwords, not the website name
- required actions missing from the reply: Under Passwords, select the password (critical)
- low scores: {'steps': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/chrome/answer/95606?hl=en

## tr192-d
- reasons: The path and the save offer are supported. The item selected under Passwords does not match the page, which says to select the password.
- fix requested: In the 'To see it again later' list, change step 3 to: 'Under **Passwords**, select the password.' Keep every other step as written.
- unsupported claims: 'Under **Passwords**, select the site.' -> the page says to select the password entry under Passwords, not the website name
- required actions missing from the reply: Under Passwords, select the password (critical)
- low scores: {'steps': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/chrome/answer/95606?hl=en

## tr192-e
- reasons: The steps are supported. The closing promise overstates the setting. The user relies on it to keep her husband from seeing passwords, so the reply must not promise a check the page does not make required.
- fix requested: Replace the last sentence with: 'With this on, Windows Hello can check that it is you when Chrome fills in a saved password. Chrome can also use biometric checks to reveal, copy, or edit passwords, but this is optional and off by default, so turn it on as shown.' Do not say the check is required before anyone can see a password. Keep steps 1 to 5 as written.
- unsupported claims: 'After that, Chrome asks you to verify who you are before it lets anyone reveal, copy, or edit a password.' -> the page says biometric authentication is off by default, is optional, and can be used to reveal, copy, or edit passwords; it does not say verification is required before a password can be revealed, copied, or edited
- low scores: {'constraints': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/chrome/answer/95606?hl=en

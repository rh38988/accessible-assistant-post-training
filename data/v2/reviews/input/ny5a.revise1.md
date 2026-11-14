# Revision list: batch ny5a, after review round 1 (11 examples)

Edit ONLY these examples in data/v2/specs/ny5a.py, then rebuild.

## tr173-e
- reasons: G1 unsupported 'keep them safe' claim about the USB drive. It overpromises for family photos.
- fix requested: Change the opening to 'Yes, you can move them to the USB drive instead of deleting them:' and remove 'keep them safe'. Keep the six steps. Keep the closing note but base it on the page wording: you can still use the files when the drive is connected, but they will not take up space on the PC.
- unsupported claims: 'Yes, you can move them to the USB drive and keep them safe' -> the page never says a USB drive keeps files safe and does not mention backups; Cut and Paste to one USB leaves a single copy
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.microsoft.com/en-us/windows/free-up-drive-space-in-windows-85529ccb-c365-490d-b548-831022bc9b32

## tr174-r
- reasons: The reply skips the page's Settings route for turning Energy saver on. The restart and Power troubleshooter appear on the page only under 'If battery life is still poor', so they should not be the only fix offered for the quick setting not working.
- fix requested: Make step 1 the Settings route: Start, then Settings; System, then Power & battery; expand Energy saver; set Always use energy saver to On. Then keep the restart and Power troubleshooter steps as a second try ('If that does not help, restart the laptop, then ... next to Power select Run'). Keep to about five steps.
- required actions missing from the reply: Alternative route: Start > Settings > System > Power & battery > expand Energy saver > set Always use energy saver to On
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://support.microsoft.com/windows/battery-saving-tips-a850d64d-ee8e-c8d2-6c75-8ffe6ea3ea99

## tr175-a
- reasons: Prerequisite 'Bluetooth needs to be turned on' is missing (non-critical).
- fix requested: Add a first step: 'Make sure Bluetooth is turned on.' It can be one short line using the page's own route, for example: Select the Network, Sound, or Battery icon near the clock and check the Bluetooth tile is on (or Start > Settings > Bluetooth & devices and set Bluetooth to On). Keep the other steps unchanged.
- required actions missing from the reply: Make sure Bluetooth is turned on before pairing (page: 'Bluetooth needs to be turned on')
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://support.microsoft.com/en-US/windows/pair-a-bluetooth-device-in-windows-2be7b51f-6ae9-b757-a3b9-95ee40c3e242

## tr175-c
- reasons: G1 unsupported claim about blinking light; Bluetooth-on prerequisite missing.
- fix requested: Delete the sentence 'A blinking light usually means it is ready to be found.' and open with something like 'Here is how to add it:'. Keep step 1 (printer discoverable, see its manual). Add the line 'Make sure Bluetooth is turned on.' as a step before the Settings steps (Start > Settings > Bluetooth & devices, and check the Bluetooth switch is On).
- unsupported claims: 'A blinking light usually means it is ready to be found.' -> not on the page (the page does not mention a blinking light); it is from memory and can be wrong for some printers
- required actions missing from the reply: Bluetooth on
- low scores: {'steps': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.microsoft.com/en-US/windows/pair-a-bluetooth-device-in-windows-2be7b51f-6ae9-b757-a3b9-95ee40c3e242

## tr175-d
- reasons: Prerequisite 'Bluetooth needs to be turned on' is missing (non-critical).
- fix requested: Add a first step: 'Make sure Bluetooth is turned on.' It can be one short line using the page's own route, for example: Select the Network, Sound, or Battery icon near the clock and check the Bluetooth tile is on (or Start > Settings > Bluetooth & devices and set Bluetooth to On). Keep the other steps unchanged.
- required actions missing from the reply: Make sure Bluetooth is turned on before pairing (page: 'Bluetooth needs to be turned on')
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://support.microsoft.com/en-US/windows/pair-a-bluetooth-device-in-windows-2be7b51f-6ae9-b757-a3b9-95ee40c3e242

## tr175-e
- reasons: Prerequisite 'Bluetooth needs to be turned on' is missing (non-critical). The taskbar-only constraint is otherwise respected.
- fix requested: Add a first step: 'Make sure Bluetooth is turned on.' It can be one short line using the page's own route, for example: Select the Network, Sound, or Battery icon near the clock and check the Bluetooth tile is on (or Start > Settings > Bluetooth & devices and set Bluetooth to On). Keep the other steps unchanged. Do not send the user into the Settings app (they said it confuses them); the quick settings Bluetooth tile is enough.
- required actions missing from the reply: Make sure Bluetooth is turned on before pairing (page: 'Bluetooth needs to be turned on')
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://support.microsoft.com/en-US/windows/pair-a-bluetooth-device-in-windows-2be7b51f-6ae9-b757-a3b9-95ee40c3e242

## tr175-r
- reasons: The page's tip for a device not shown in the list, setting Bluetooth devices discovery to Advanced, is missing.
- fix requested: Add a step: 'Select Start, then Settings, then Bluetooth & devices, then Devices. Under Device settings, set Bluetooth devices discovery to Advanced.' This path is on the second official page https://support.microsoft.com/en-us/windows/hardware/bluetooth/fix-bluetooth-problems-in-windows ; add that URL as a second source. Keep the other steps.
- required actions missing from the reply: Set Bluetooth devices discovery to Advanced (page: device not displayed in list)
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://support.microsoft.com/en-US/windows/pair-a-bluetooth-device-in-windows-2be7b51f-6ae9-b757-a3b9-95ee40c3e242

## tr177-a
- reasons: G1 unsupported sentence. The steps themselves match the page.
- fix requested: Delete 'Magnifier is already built into Windows.' and start with 'Yes. Use the keyboard:' (or similar). Keep the two steps.
- unsupported claims: 'Magnifier is already built into Windows.' -> the page does not say this
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.microsoft.com/en-US/accessibility/windows/magnifier/how-to-quickly-change-the-zoom-level-for-magnifier

## tr177-e
- reasons: Cited page does not cover the Lens and Full screen shortcuts. They are correct on another official page.
- fix requested: Keep the reply as is and add a second source: https://support.microsoft.com/en-us/accessibility/windows/magnifier/keyboard-shortcuts-for-magnifier (it lists Full screen Ctrl+Alt+F, Lens Ctrl+Alt+L, Windows key+Plus to turn on).
- unsupported claims: 'Press Ctrl + Alt + L' and 'Ctrl + Alt + F' -> the cited page does not list Lens or Full screen shortcuts
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.microsoft.com/en-US/accessibility/windows/magnifier/how-to-quickly-change-the-zoom-level-for-magnifier

## tr178-a
- reasons: G1 overstatement of what live captions show.
- fix requested: Replace the last line with 'Captions then appear for speech in what your computer plays.' (or 'for the spoken words').
- unsupported claims: 'Captions then appear for the sound your computer plays.' -> page says only detected speech is captioned; music and applause are not reliably captioned
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.microsoft.com/windows/use-live-captions-to-better-understand-audio-b52da59c-14b8-4031-aeeb-f6a47e6055df

## tr178-r
- reasons: The page says to change the default output device in Settings > System > Sound. The reply only says to check it and never tells the user to change it.
- fix requested: Add after step 3: 'If it is not the headset you are using, change the default output device to your headset.' Then say to play the video again and check that captions show. Keep the first two steps.
- required actions missing from the reply: Change the default output device to the headset (critical)
- low scores: {'steps': 1, 'actionable': 1} | gates not passed: {}
- sources: https://support.microsoft.com/windows/use-live-captions-to-better-understand-audio-b52da59c-14b8-4031-aeeb-f6a47e6055df

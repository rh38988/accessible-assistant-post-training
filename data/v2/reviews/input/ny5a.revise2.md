# Revision list: batch ny5a, after review round 2 (4 examples)

Edit ONLY these examples in data/v2/specs/ny5a.py, then rebuild.

## tr175-r
- reasons: G1: the USB adapter suggestion is not on either official page. Everything else in the troubleshooting steps is supported by the second page (Bluetooth devices discovery, Advanced).
- fix requested: In the last paragraph, replace 'If it does not, a USB Bluetooth adapter can add it.' with 'If it does not, check the product specifications to make sure it has Bluetooth capabilities.' Keep everything else. Page support for the new sentence: 'Some devices don't have Bluetooth' and 'check the product specifications to make sure it has Bluetooth capabilities' (https://support.microsoft.com/en-us/windows/hardware/bluetooth/fix-bluetooth-problems-in-windows).
- unsupported claims: 'If it does not, a USB Bluetooth adapter can add it.' -> neither the pairing page nor the 'Fix Bluetooth problems in Windows' page mentions USB Bluetooth adapters or dongles. The fix page only says 'Some devices don't have Bluetooth' and to check the product specifications for Bluetooth capabilities.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.microsoft.com/en-US/windows/pair-a-bluetooth-device-in-windows-2be7b51f-6ae9-b757-a3b9-95ee40c3e242 ; https://support.microsoft.com/en-us/windows/hardware/bluetooth/fix-bluetooth-problems-in-windows

## tr177-a
- reasons: G1: the sentence about what each press does is not on the page.
- fix requested: Delete the sentence 'Each press makes things on the screen larger.' Keep the two steps. Step 2 may end 'to zoom in more.' Do not add any other description of the zoom effect.
- unsupported claims: 'Each press makes things on the screen larger.' -> the page only says 'To increase the Magnifier zoom level, press the Windows key+Plus sign(+).' It does not describe what each press does.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.microsoft.com/en-US/accessibility/windows/magnifier/how-to-quickly-change-the-zoom-level-for-magnifier

## tr177-e
- reasons: S5: 'To go back to the whole screen' uses a phrase that is not the page's label, and it can suggest that Ctrl + Alt + F turns magnification off. The page names this view 'Full screen view' (Ctrl+Alt+F). The shortcuts are supported by the second source (keyboard-shortcuts-for-magnifier).
- fix requested: Replace 'To go back to the whole screen, press Ctrl + Alt + F.' with 'To switch back to Full screen view, press Ctrl + Alt + F.' Keep the rest.
- low scores: {'plain': 1} | gates not passed: {}
- sources: https://support.microsoft.com/en-US/accessibility/windows/magnifier/how-to-quickly-change-the-zoom-level-for-magnifier ; https://support.microsoft.com/en-us/accessibility/windows/magnifier/keyboard-shortcuts-for-magnifier

## tr178-r
- reasons: G1: the change step has no steps on the cited page. The location (Settings > System > Sound) and the need to change the device are on the page. The how-to is supported by the 'Fix sound or audio problems in Windows' page, which should be added as a second source. S4: step 3 bundles a check and a conditional change into one step.
- fix requested: Keep steps 1 and 2 and the sentence 'Captions only show sound that goes to your default sound output.' Replace step 3 with two steps: '3. Under Output, check which device is selected.' and '4. If it is not your headset, select your headset in the Output section. Selecting it also makes it the default.' Renumber the last step as 5: 'Play the video again and check that captions show.' Add second source https://support.microsoft.com/en-us/windows/hardware/audio/fix-sound-or-audio-problems-in-windows (page: Start > Settings > System > Sound; in the Output section choose the device; 'When you select this device, you're also setting it as the default.').
- unsupported claims: 'If it is not the headset you are using, change the default output device to your headset.' -> the cited page (use-live-captions) says only 'You might need to change your default device for audio to be picked up by live captions' and gives no steps for changing it. The how-to is on a different official page (see fix).
- low scores: {'actionable': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.microsoft.com/windows/use-live-captions-to-better-understand-audio-b52da59c-14b8-4031-aeeb-f6a47e6055df ; https://support.microsoft.com/en-us/windows/hardware/audio/fix-sound-or-audio-problems-in-windows

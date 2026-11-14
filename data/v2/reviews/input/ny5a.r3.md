# Review input: batch ny5a, round 3 (4 examples)

## tr175-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Windows 11
- task: Pair a Bluetooth device (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-US/windows/pair-a-bluetooth-device-in-windows-2be7b51f-6ae9-b757-a3b9-95ee40c3e242 ; https://support.microsoft.com/en-us/windows/hardware/bluetooth/fix-bluetooth-problems-in-windows

**USER:**
Show me how to pair my Bluetooth keyboard with my Windows 11 computer.

**ASSISTANT:**
Here is how to pair it:

1. Put the keyboard in pairing mode. Check its manual for how.
2. Select the **Network**, **Sound**, or **Battery** icon on the taskbar.
3. Select the small arrow next to the Bluetooth quick setting, labeled **Manage Bluetooth devices**.
4. Under **New devices**, select your keyboard.
5. Follow any extra prompts, then select **Done**.

**USER:**
My keyboard is not showing up in that list.

**ASSISTANT:**
Try these:

1. Put the keyboard in pairing mode again, using its manual.
2. Look through **Your devices** in the same list, as well as **New devices**.
3. Check that Bluetooth is on. Select **Start**, then **Settings**, then **Bluetooth & devices**, and make sure the **Bluetooth** switch is **On**.
4. Select **Devices**. Under **Device settings**, set **Bluetooth devices discovery** to **Advanced**.

If it still does not show, check the product specifications to make sure your computer has Bluetooth capabilities.

## tr177-a
- scenario: direct | style: plain | specification: fully_specified | platform: Windows 11
- task: Use Magnifier to make things on screen bigger (keyboard shortcuts) (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-US/accessibility/windows/magnifier/how-to-quickly-change-the-zoom-level-for-magnifier

**USER:**
The words on my Windows 11 computer are too small to read. Can I make them bigger with Magnifier?

**ASSISTANT:**
Yes. Use the keyboard:

1. Press the **Windows key + Plus sign (+)**. This turns Magnifier on.
2. Press **Windows key + Plus sign (+)** again to zoom in more.

## tr177-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Windows 11
- task: Use Magnifier to make things on screen bigger (keyboard shortcuts) (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-US/accessibility/windows/magnifier/how-to-quickly-change-the-zoom-level-for-magnifier ; https://support.microsoft.com/en-us/accessibility/windows/magnifier/keyboard-shortcuts-for-magnifier

**USER:**
I use Magnifier on my Windows 11 PC, but I do not want the whole screen to get big, I only want a part of it magnified like a lens. Is that possible, and how do I switch to it?

**ASSISTANT:**
Yes, Magnifier has a Lens view:

1. If Magnifier is not on yet, press the **Windows key + Plus sign (+)**.
2. Press **Ctrl + Alt + L**. This switches to Lens view.

To switch back to **Full screen view**, press **Ctrl + Alt + F**.

## tr178-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Windows 11
- task: Turn on live captions (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/windows/use-live-captions-to-better-understand-audio-b52da59c-14b8-4031-aeeb-f6a47e6055df ; https://support.microsoft.com/en-us/windows/hardware/audio/fix-sound-or-audio-problems-in-windows

**USER:**
How do I turn on live captions in Windows 11?

**ASSISTANT:**
Use the keyboard:

1. Press **Windows key + Ctrl + L**.
2. The first time, follow the prompts. Windows asks for your consent to process voice on your device and may download language files.

**USER:**
The captions window opened but nothing shows up when I play a video with my headset on.

**ASSISTANT:**
Captions only show sound that goes to your default sound output. Let us check it:

1. Select **Start**, then **Settings**.
2. Select **System**, then **Sound**.
3. Under **Output**, check which device is chosen. If it is not the headset you are using, select your headset. Selecting it makes it your default output device.
4. Play the video again and check that captions show.

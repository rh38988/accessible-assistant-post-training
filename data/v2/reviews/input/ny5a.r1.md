# Review input: batch ny5a, round 1 (42 examples)

## tr173-a
- scenario: direct | style: plain | specification: fully_specified | platform: Windows 11
- task: Free up drive space (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/free-up-drive-space-in-windows-85529ccb-c365-490d-b548-831022bc9b32

**USER:**
My Windows 11 laptop says the drive is almost full. How can I clear some space?

**ASSISTANT:**
Windows has a cleanup tool that shows what you can safely remove. Here is how to use it:

1. Select **Start**, then **Settings**.
2. Select **System**, then **Storage**.
3. Select **Cleanup recommendations**.
4. Look at the groups: **Temporary files**, **Large or unused files**, **Files synced to the cloud**, and **Unused apps**. Tick the items you want to remove. Windows shows how much space each one will save.
5. Select the **Clean up** button in each section.

If you want to see how much room you have, open **File Explorer**, select **This PC**, and look under **Devices and drives**.

## tr173-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Windows 11
- task: Free up drive space (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/free-up-drive-space-in-windows-85529ccb-c365-490d-b548-831022bc9b32

**USER:**
So my grandson helped me update my Windows 11 computer last week and ever since then I keep getting told there is not enough storage. I think the old version of Windows might still be sitting there taking up room. Can you show me how to get rid of it? I do not need to go back.

**ASSISTANT:**
Yes, the older version of Windows can be removed from the same cleanup screen:

1. Select **Start**, then **Settings**.
2. Select **System**, then **Storage**.
3. Select **Cleanup recommendations**.
4. Find the previous version of Windows in the list. After a recent upgrade it shows up as a system file you can delete. Tick it.
5. Select the **Clean up** button.

Please note that this removes the Windows.old folder, so you will not be able to go back to the older version. It cannot be undone.

## tr173-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Free up drive space (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/free-up-drive-space-in-windows-85529ccb-c365-490d-b548-831022bc9b32

**USER:**
my computer keeps saying i am out of space what do i do

**ASSISTANT:**
I can help with that. Is your computer a **Windows PC** or a **Mac**?

## tr173-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Windows 11
- task: Free up drive space (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/free-up-drive-space-in-windows-85529ccb-c365-490d-b548-831022bc9b32

**USER:**
my computer keeps saying i am out of space what do i do

**ASSISTANT:**
I can help with that. Is your computer a **Windows PC** or a **Mac**?

**USER:**
Windows PC, it has Windows 11

**ASSISTANT:**
Thanks. On Windows 11 you can use the cleanup tool:

1. Select **Start**, then **Settings**.
2. Select **System**, then **Storage**.
3. Select **Cleanup recommendations**.
4. Tick the items you want to remove from **Temporary files**, **Large or unused files**, **Files synced to the cloud**, or **Unused apps**. Windows shows how much space each will save.
5. Select the **Clean up** button in each section.

## tr173-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Windows 11
- task: Free up drive space (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/free-up-drive-space-in-windows-85529ccb-c365-490d-b548-831022bc9b32

**USER:**
I have a Windows 11 PC full of old family photos and videos in the Pictures and Videos folders. I do not want to delete any of them, but I need room. I have a USB drive here. Can I move them instead?

**ASSISTANT:**
Yes, you can move them to the USB drive and keep them safe:

1. Plug the USB drive into the computer.
2. Open **File Explorer** from the taskbar.
3. Open the folder with your photos or videos and select the files you want to move.
4. Select **Cut** on the ribbon at the top.
5. Open the USB drive in **File Explorer**.
6. Select **Paste**.

Once the files are copied over, your computer has more room. The files will only open while the USB drive is plugged in.

## tr173-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Windows 11
- task: Free up drive space (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/free-up-drive-space-in-windows-85529ccb-c365-490d-b548-831022bc9b32

**USER:**
How do I free up space on my Windows 11 computer?

**ASSISTANT:**
You can use the cleanup tool in Settings:

1. Select **Start**, then **Settings**.
2. Select **System**, then **Storage**.
3. Select **Cleanup recommendations**.
4. Tick the items you want to remove. Windows shows how much space each will save.
5. Select the **Clean up** button in each section.

**USER:**
I did that but there is still not much room left. Is there anything else?

**ASSISTANT:**
Yes, your own big files may be taking the space:

1. Open **File Explorer** and select a folder such as **Downloads**, **Videos**, **Music**, or **Pictures**. These often hold the largest files.
2. Select **View**, then **Details**.
3. Right-click an empty spot, choose **Sort by**, then **Size**. The biggest files come first.
4. Delete the ones you do not need.
5. Empty the **Recycle Bin**, because deleted files still take up room until you do.

## tr174-a
- scenario: direct | style: plain | specification: fully_specified | platform: Windows 11 laptop
- task: Turn on battery saver (energy saver) (Windows 11 laptop) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/windows/battery-saving-tips-a850d64d-ee8e-c8d2-6c75-8ffe6ea3ea99

**USER:**
How do I turn on battery saver on my Windows 11 laptop? The battery runs out too fast.

**ASSISTANT:**
On Windows 11 this is called Energy saver. Here is the quickest way:

1. Select the **battery icon** in the notification area, near the clock.
2. Select the **Energy saver** quick setting.

That turns Energy saver on.

## tr174-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Windows 11 laptop
- task: Turn on battery saver (energy saver) (Windows 11 laptop) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/windows/battery-saving-tips-a850d64d-ee8e-c8d2-6c75-8ffe6ea3ea99

**USER:**
I travel a lot and my Windows 11 laptop is never near a plug. I forget to turn the power saving thing on every time. Is there a way to make the laptop do it by itself when the battery gets low?

**ASSISTANT:**
Yes, you can set it to turn on by itself:

1. Select **Start**, then **Settings**.
2. Select **System**, then **Power & battery**.
3. Expand **Energy saver**.
4. Next to **Turn energy saver on when battery level is at**, choose the battery percentage you want.

Once the battery drops to that level, Energy saver turns on.

## tr174-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Turn on battery saver (energy saver) (Windows 11 laptop) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/windows/battery-saving-tips-a850d64d-ee8e-c8d2-6c75-8ffe6ea3ea99

**USER:**
battery saver how

**ASSISTANT:**
I can help with that. Is it a **Windows laptop**, a **Mac laptop**, or a **phone**?

## tr174-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Windows 11 laptop
- task: Turn on battery saver (energy saver) (Windows 11 laptop) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/windows/battery-saving-tips-a850d64d-ee8e-c8d2-6c75-8ffe6ea3ea99

**USER:**
battery saver how

**ASSISTANT:**
I can help with that. Is it a **Windows laptop**, a **Mac laptop**, or a **phone**?

**USER:**
windows laptop, windows 11

**ASSISTANT:**
On Windows 11 it is called Energy saver:

1. Select the **battery icon** in the notification area, near the clock.
2. Select the **Energy saver** quick setting.

## tr174-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Windows 11 laptop
- task: Turn on battery saver (energy saver) (Windows 11 laptop) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/windows/battery-saving-tips-a850d64d-ee8e-c8d2-6c75-8ffe6ea3ea99

**USER:**
I am on a long train ride with my Windows 11 laptop and there are no outlets. I want Energy saver on right now and I want it to stay on until I plug in again. I do not want to pick a battery percentage. What do I do?

**ASSISTANT:**
You can turn it on now and leave it on:

1. Select **Start**, then **Settings**.
2. Select **System**, then **Power & battery**.
3. Expand **Energy saver**.
4. Set **Always use energy saver** to **On**.

It stays on until you next plug in the laptop.

## tr174-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Windows 11 laptop
- task: Turn on battery saver (energy saver) (Windows 11 laptop) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/windows/battery-saving-tips-a850d64d-ee8e-c8d2-6c75-8ffe6ea3ea99

**USER:**
Please show me how to turn on Energy saver on my Windows 11 laptop.

**ASSISTANT:**
Here is the quick way:

1. Select the **battery icon** in the notification area, near the clock.
2. Select the **Energy saver** quick setting.

**USER:**
I did that but Energy saver still does not turn on.

**ASSISTANT:**
Let us try this:

1. Restart the laptop.
2. Select **Start**, then **Settings**.
3. Select **System**, then **Troubleshoot**, then **Other troubleshooters**.
4. Next to **Power**, select **Run**.
5. Follow the prompts, then try the **Energy saver** quick setting again.

## tr175-a
- scenario: direct | style: plain | specification: fully_specified | platform: Windows 11
- task: Pair a Bluetooth device (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-US/windows/pair-a-bluetooth-device-in-windows-2be7b51f-6ae9-b757-a3b9-95ee40c3e242

**USER:**
I just got wireless headphones and want to hook them up to my Windows 11 PC through Bluetooth. Where do I start?

**ASSISTANT:**
Here is how to pair them:

1. Put the headphones in pairing mode so the computer can find them. The way to do this depends on the headphones, so check their manual.
2. Select the **Network**, **Sound**, or **Battery** icon on the taskbar, near the clock.
3. Select the small arrow next to the Bluetooth quick setting, labeled **Manage Bluetooth devices**.
4. Under **New devices**, select your headphones.
5. Follow any extra prompts, then select **Done**.

After this, they reconnect by themselves whenever Bluetooth is on and they are in range.

## tr175-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Windows 11
- task: Pair a Bluetooth device (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-US/windows/pair-a-bluetooth-device-in-windows-2be7b51f-6ae9-b757-a3b9-95ee40c3e242

**USER:**
My daughter bought me a little Bluetooth printer for my Windows 11 computer so I can stop using that long cable. It is turned on and the light is blinking. I have never done this before and I do not want to mess up my settings. How do I connect it?

**ASSISTANT:**
A blinking light usually means it is ready to be found. Here is how to add it:

1. Make sure the printer is discoverable. Your printer's manual shows how.
2. Select **Start**, then **Settings**.
3. Select **Bluetooth & devices**, then **Printers & scanners**.
4. Next to **Add a printer or scanner**, select **Add device**.
5. Wait while Windows searches. This can take a few minutes.
6. When your printer appears, select **Add device** next to it.

## tr175-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Pair a Bluetooth device (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-US/windows/pair-a-bluetooth-device-in-windows-2be7b51f-6ae9-b757-a3b9-95ee40c3e242

**USER:**
I need to pair my bluetooth speaker with my computer

**ASSISTANT:**
I can help with that. Is your computer a **Windows PC** or a **Mac**?

## tr175-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Windows 11
- task: Pair a Bluetooth device (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-US/windows/pair-a-bluetooth-device-in-windows-2be7b51f-6ae9-b757-a3b9-95ee40c3e242

**USER:**
I need to pair my bluetooth speaker with my computer

**ASSISTANT:**
I can help with that. Is your computer a **Windows PC** or a **Mac**?

**USER:**
its a windows 11 pc

**ASSISTANT:**
Here is how to pair the speaker:

1. Put the speaker in pairing mode. Check its manual for how.
2. Select the **Network**, **Sound**, or **Battery** icon on the taskbar.
3. Select the small arrow next to the Bluetooth quick setting, labeled **Manage Bluetooth devices**.
4. Under **New devices**, select your speaker.
5. Follow any extra prompts, then select **Done**.

## tr175-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Windows 11
- task: Pair a Bluetooth device (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-US/windows/pair-a-bluetooth-device-in-windows-2be7b51f-6ae9-b757-a3b9-95ee40c3e242

**USER:**
I would like to connect my Bluetooth mouse to my Windows 11 laptop but I do not want to go digging through the Settings app, it confuses me. Is there a quicker way from the bottom of the screen?

**ASSISTANT:**
Yes, you can do it from the taskbar:

1. Put the mouse in pairing mode. Check its manual for how.
2. Select the **Network**, **Sound**, or **Battery** icon on the taskbar, near the clock.
3. Select the small arrow next to the Bluetooth quick setting, labeled **Manage Bluetooth devices**.
4. Under **New devices**, select your mouse. If you do not see it, look through **Your devices**.
5. Follow any extra prompts, then select **Done**.

## tr175-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Windows 11
- task: Pair a Bluetooth device (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-US/windows/pair-a-bluetooth-device-in-windows-2be7b51f-6ae9-b757-a3b9-95ee40c3e242

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

If it still does not show, make sure your computer has Bluetooth. If it does not, a USB Bluetooth adapter can add it.

## tr176-a
- scenario: direct | style: plain | specification: fully_specified | platform: Windows 11
- task: Turn off notifications from an app (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/notifications-and-do-not-disturb-in-windows-feeca47f-0baf-5680-16f0-8801db1a8466

**USER:**
How do I stop one app from sending me notifications on Windows 11?

**ASSISTANT:**
You can turn off alerts for one app in Settings:

1. Select **Start**, then **Settings**.
2. Select **System**, then **Notifications**.
3. Under **Notifications from apps and other senders**, select the app you want to quiet.
4. Switch off **Turn notifications on or off**.

That stops alerts from that app.

## tr176-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Windows 11
- task: Turn off notifications from an app (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/notifications-and-do-not-disturb-in-windows-feeca47f-0baf-5680-16f0-8801db1a8466

**USER:**
Every few minutes a little box pops up in the corner of my Windows 11 screen from the Solitaire game telling me to come back and play. It drives me crazy when I am writing emails. I do not want to uninstall it, I just want it to leave me alone.

**ASSISTANT:**
You can silence it without removing the game:

1. Select **Start**, then **Settings**.
2. Select **System**, then **Notifications**.
3. Under **Notifications from apps and other senders**, select the game.
4. Switch off **Turn notifications on or off**.

The game stays installed, and it stops sending you alerts.

## tr176-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Turn off notifications from an app (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/notifications-and-do-not-disturb-in-windows-feeca47f-0baf-5680-16f0-8801db1a8466

**USER:**
these popups from one program on my computer keep bothering me, can they be turned off

**ASSISTANT:**
I can help with that. Is your computer a **Windows PC** or a **Mac**?

## tr176-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Windows 11
- task: Turn off notifications from an app (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/notifications-and-do-not-disturb-in-windows-feeca47f-0baf-5680-16f0-8801db1a8466

**USER:**
these popups from one program on my computer keep bothering me, can they be turned off

**ASSISTANT:**
I can help with that. Is your computer a **Windows PC** or a **Mac**?

**USER:**
Windows 11 PC

**ASSISTANT:**
Yes. Here is how to turn off alerts for that program:

1. Select **Start**, then **Settings**.
2. Select **System**, then **Notifications**.
3. Under **Notifications from apps and other senders**, select the program that bothers you.
4. Switch off **Turn notifications on or off**.

## tr176-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Windows 11
- task: Turn off notifications from an app (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/notifications-and-do-not-disturb-in-windows-feeca47f-0baf-5680-16f0-8801db1a8466

**USER:**
On my Windows 11 computer my Mail app makes a loud ding for every message. I still want to see the messages, I just do not want the sound. How do I turn off only the sound?

**ASSISTANT:**
You can keep the alerts and turn off just the sound:

1. Select **Start**, then **Settings**.
2. Select **System**, then **Notifications**.
3. Under **Notifications from apps and other senders**, select **Mail**.
4. Switch off **Play a sound**.

Leave **Turn notifications on or off** switched on, so the messages still show up.

## tr176-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Windows 11
- task: Turn off notifications from an app (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/notifications-and-do-not-disturb-in-windows-feeca47f-0baf-5680-16f0-8801db1a8466

**USER:**
Please help me make my Mail app stop sending me notifications on Windows 11.

**ASSISTANT:**
Here is how to turn them off:

1. Select **Start**, then **Settings**.
2. Select **System**, then **Notifications**.
3. Under **Notifications from apps and other senders**, select **Mail**.
4. Switch off **Turn notifications on or off**.

**USER:**
Now I am worried I will miss important emails. I only wanted the pop-up boxes and the sound gone.

**ASSISTANT:**
You can turn the alerts back on and then quiet only those parts:

1. Go back to **Settings**, **System**, **Notifications**, and select **Mail**.
2. Switch **Turn notifications on or off** back on.
3. Switch off **Show notification banners**. This stops the pop-up boxes.
4. Switch off **Play a sound**.

## tr177-a
- scenario: direct | style: plain | specification: fully_specified | platform: Windows 11
- task: Use Magnifier to make things on screen bigger (keyboard shortcuts) (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-US/accessibility/windows/magnifier/how-to-quickly-change-the-zoom-level-for-magnifier

**USER:**
The words on my Windows 11 computer are too small to read. Can I make them bigger with Magnifier?

**ASSISTANT:**
Yes. Magnifier is already built into Windows. Use the keyboard:

1. Press the **Windows key + Plus sign (+)**. This turns Magnifier on.
2. Press **Windows key + Plus sign (+)** again to zoom in more. Each press makes things on the screen larger.

## tr177-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Windows 11
- task: Use Magnifier to make things on screen bigger (keyboard shortcuts) (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-US/accessibility/windows/magnifier/how-to-quickly-change-the-zoom-level-for-magnifier

**USER:**
My eyes are not what they used to be and I am trying to read a recipe online on my Windows 11 computer. I would like to make the screen bigger for a bit and then get it back to normal after, because it is hard to do my other things when everything is huge. How do I do all of that?

**ASSISTANT:**
You can do all of it with the keyboard:

1. Press the **Windows key + Plus sign (+)** to turn Magnifier on.
2. Press **Windows key + Plus sign (+)** again to make things larger.
3. If it gets too big, press the **Windows key + Minus sign (-)** to make things smaller.
4. When you are done reading, press the **Windows key + Esc** to turn Magnifier off.

## tr177-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Use Magnifier to make things on screen bigger (keyboard shortcuts) (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-US/accessibility/windows/magnifier/how-to-quickly-change-the-zoom-level-for-magnifier

**USER:**
how do i make everything on the screen bigger so i can see it

**ASSISTANT:**
I can help with that. Is your computer a **Windows PC** or a **Mac**?

## tr177-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Windows 11
- task: Use Magnifier to make things on screen bigger (keyboard shortcuts) (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-US/accessibility/windows/magnifier/how-to-quickly-change-the-zoom-level-for-magnifier

**USER:**
how do i make everything on the screen bigger so i can see it

**ASSISTANT:**
I can help with that. Is your computer a **Windows PC** or a **Mac**?

**USER:**
windows 11

**ASSISTANT:**
On Windows 11 you can use Magnifier:

1. Press the **Windows key + Plus sign (+)** to turn Magnifier on.
2. Press **Windows key + Plus sign (+)** again to zoom in more.
3. To make things smaller again, press the **Windows key + Minus sign (-)**.

## tr177-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Windows 11
- task: Use Magnifier to make things on screen bigger (keyboard shortcuts) (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-US/accessibility/windows/magnifier/how-to-quickly-change-the-zoom-level-for-magnifier

**USER:**
I use Magnifier on my Windows 11 PC, but I do not want the whole screen to get big, I only want a part of it magnified like a lens. Is that possible, and how do I switch to it?

**ASSISTANT:**
Yes, Magnifier has a Lens view:

1. If Magnifier is not on yet, press the **Windows key + Plus sign (+)**.
2. Press **Ctrl + Alt + L**. This switches to Lens view.

To go back to the whole screen, press **Ctrl + Alt + F**.

## tr177-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Windows 11
- task: Use Magnifier to make things on screen bigger (keyboard shortcuts) (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-US/accessibility/windows/magnifier/how-to-quickly-change-the-zoom-level-for-magnifier

**USER:**
How do I turn on Magnifier on my Windows 11 computer?

**ASSISTANT:**
Use the keyboard:

1. Press the **Windows key + Plus sign (+)**. This turns Magnifier on.
2. Press **Windows key + Plus sign (+)** again to zoom in more.

**USER:**
Now everything is way too big and I cannot read anything. Help!

**ASSISTANT:**
Do not worry. You can fix it two ways:

1. To make things a bit smaller, press the **Windows key + Minus sign (-)**. Press it again if it is still too big.
2. To turn Magnifier off completely, press the **Windows key + Esc**.

## tr178-a
- scenario: direct | style: plain | specification: fully_specified | platform: Windows 11
- task: Turn on live captions (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/windows/use-live-captions-to-better-understand-audio-b52da59c-14b8-4031-aeeb-f6a47e6055df

**USER:**
Is there a way to see words on screen for videos I watch on my Windows 11 computer? I have trouble hearing.

**ASSISTANT:**
Yes, Windows 11 has live captions. The quickest way is the keyboard:

1. Press **Windows key + Ctrl + L**.
2. The first time, Windows asks for your consent to process voice on your device. Follow the prompts.
3. If asked, let it download the language files it needs.

Captions then appear for the sound your computer plays.

## tr178-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Windows 11
- task: Turn on live captions (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/windows/use-live-captions-to-better-understand-audio-b52da59c-14b8-4031-aeeb-f6a47e6055df

**USER:**
My husband and I watch our church service online on our Windows 11 computer and he cannot make out what the pastor says. I do not like using key combinations because I always press the wrong ones. Can you walk me through turning on captions using the Settings app?

**ASSISTANT:**
Yes, here is the way through Settings:

1. Select **Start**, then **Settings**.
2. Select **Accessibility**, then **Captions**.
3. Turn on the **Live captions** toggle.
4. The first time, follow the prompts. Windows asks for your consent to process voice on your device and may download language files.

## tr178-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Turn on live captions (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/windows/use-live-captions-to-better-understand-audio-b52da59c-14b8-4031-aeeb-f6a47e6055df

**USER:**
can i get subtitles to show up for everything that plays on my computer

**ASSISTANT:**
I can help with that. Is your computer a **Windows PC** or a **Mac**?

## tr178-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Windows 11
- task: Turn on live captions (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/windows/use-live-captions-to-better-understand-audio-b52da59c-14b8-4031-aeeb-f6a47e6055df

**USER:**
can i get subtitles to show up for everything that plays on my computer

**ASSISTANT:**
I can help with that. Is your computer a **Windows PC** or a **Mac**?

**USER:**
windows 11

**ASSISTANT:**
Yes, Windows 11 has live captions:

1. Press **Windows key + Ctrl + L**.
2. The first time, follow the prompts. Windows asks for your consent to process voice on your device and may download language files.

## tr178-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Windows 11
- task: Turn on live captions (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/windows/use-live-captions-to-better-understand-audio-b52da59c-14b8-4031-aeeb-f6a47e6055df

**USER:**
I want live captions on my Windows 11 PC, but I can only use the mouse right now, my keyboard is not working. Can I turn them on from the taskbar?

**ASSISTANT:**
Yes, you can do it with the mouse only:

1. Select the **battery**, **network**, or **volume** icon on the taskbar, near the clock. This opens quick settings.
2. Turn on **Live captions**.

The first time, follow the prompts. Windows asks for your consent to process voice on your device and may download language files.

## tr178-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Windows 11
- task: Turn on live captions (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/windows/use-live-captions-to-better-understand-audio-b52da59c-14b8-4031-aeeb-f6a47e6055df

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
3. Check which output device is chosen as your default, and make sure it is the headset or speaker you are using.

## tr179-a
- scenario: direct | style: plain | specification: fully_specified | platform: Windows 11
- task: Make the screen brighter or dimmer (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/help/4026946

**USER:**
The screen on my Windows 11 laptop is too bright. How do I make it dimmer?

**ASSISTANT:**
You can change it from the taskbar:

1. Select the **Network** icon on the right side of the taskbar.
2. Move the **Brightness** slider to the left to dim the screen, or to the right to make it brighter.

## tr179-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Windows 11
- task: Make the screen brighter or dimmer (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/help/4026946

**USER:**
I read a lot in the evenings on my Windows 11 laptop and the screen hurts my eyes. My son once showed me a slider but I forget where it was. Could you tell me how to find it in Settings so I can write it down?

**ASSISTANT:**
Here is the way through Settings:

1. Select **Start**, then **Settings**.
2. Select **System**, then **Display**.
3. Use the **Brightness** slider. Move it left to make the screen dimmer.

## tr179-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Make the screen brighter or dimmer (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/help/4026946

**USER:**
my screen is too dark how do i fix it

**ASSISTANT:**
I can help with that. Is your computer a **Windows PC** or a **Mac**?

## tr179-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Windows 11
- task: Make the screen brighter or dimmer (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/help/4026946

**USER:**
my screen is too dark how do i fix it

**ASSISTANT:**
I can help with that. Is your computer a **Windows PC** or a **Mac**?

**USER:**
its windows 11

**ASSISTANT:**
You can make it brighter from the taskbar:

1. Select the **Network** icon on the right side of the taskbar.
2. Move the **Brightness** slider to the right.

## tr179-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Windows 11
- task: Make the screen brighter or dimmer (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/help/4026946

**USER:**
My Windows 11 laptop is by a window and the light in the room changes all day. I am tired of moving the brightness by hand. Can the laptop change it by itself when the room gets lighter or darker?

**ASSISTANT:**
It can on some PCs. Here is how to try:

1. Select **Start**, then **Settings**.
2. Select **System**, then **Display**.
3. Select **Brightness**.
4. Turn on the toggle that changes brightness automatically when lighting changes.

This works only on some PCs. You can still fine-tune the level with the **Brightness** slider.

## tr179-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Windows 11
- task: Make the screen brighter or dimmer (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/help/4026946

**USER:**
How do I change the brightness on my Windows 11 computer?

**ASSISTANT:**
You can use the taskbar:

1. Select the **Network** icon on the right side of the taskbar.
2. Move the **Brightness** slider to the level you like.

**USER:**
I do not see any Brightness slider there. I have a desktop with a separate monitor.

**ASSISTANT:**
That is normal for a desktop with a separate monitor, because the slider may not appear. Use the buttons on the monitor itself to change its brightness.

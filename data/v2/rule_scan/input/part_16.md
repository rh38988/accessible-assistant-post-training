# Rule scan input, part 16 (50 examples)

## tr173-c
- task: Free up drive space | platform: Windows 11 | scenario: direct_messy | sensitive: False
- sources: Microsoft Support: Free up drive space in Windows <https://support.microsoft.com/en-us/windows/free-up-drive-space-in-windows-85529ccb-c365-490d-b548-831022bc9b32>

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

---

## tr173-d
- task: Free up drive space | platform: Windows 11 | scenario: followup | sensitive: False
- sources: Microsoft Support: Free up drive space in Windows <https://support.microsoft.com/en-us/windows/free-up-drive-space-in-windows-85529ccb-c365-490d-b548-831022bc9b32>

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

---

## tr173-e
- task: Free up drive space | platform: Windows 11 | scenario: constraint | sensitive: False
- sources: Microsoft Support: Free up drive space in Windows <https://support.microsoft.com/en-us/windows/free-up-drive-space-in-windows-85529ccb-c365-490d-b548-831022bc9b32>

**USER:**
I have a Windows 11 PC full of old family photos and videos in the Pictures and Videos folders. I do not want to delete any of them, but I need room. I have a USB drive here. Can I move them instead?

**ASSISTANT:**
Yes, you can move them to the USB drive instead of deleting them:

1. Plug the USB drive into the computer.
2. Open **File Explorer** from the taskbar.
3. Open the folder with your photos or videos and select the files you want to move.
4. Select **Cut** on the ribbon at the top.
5. Open the USB drive in **File Explorer**.
6. Select **Paste**.

You can still use the files when the drive is connected, but they will not take up space on your PC.

---

## tr173-r
- task: Free up drive space | platform: Windows 11 | scenario: failure_recovery | sensitive: False
- sources: Microsoft Support: Free up drive space in Windows <https://support.microsoft.com/en-us/windows/free-up-drive-space-in-windows-85529ccb-c365-490d-b548-831022bc9b32>

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

---

## tr174-a
- task: Turn on battery saver (energy saver) | platform: Windows 11 laptop | scenario: direct | sensitive: False
- sources: Microsoft Support: Battery saving tips (Windows 11 Energy saver) <https://support.microsoft.com/windows/battery-saving-tips-a850d64d-ee8e-c8d2-6c75-8ffe6ea3ea99>

**USER:**
How do I turn on battery saver on my Windows 11 laptop? The battery runs out too fast.

**ASSISTANT:**
On Windows 11 this is called Energy saver. Here is the quickest way:

1. Select the **battery icon** in the notification area, near the clock.
2. Select the **Energy saver** quick setting.

That turns Energy saver on.

---

## tr174-c
- task: Turn on battery saver (energy saver) | platform: Windows 11 laptop | scenario: direct_messy | sensitive: False
- sources: Microsoft Support: Battery saving tips (Windows 11 Energy saver) <https://support.microsoft.com/windows/battery-saving-tips-a850d64d-ee8e-c8d2-6c75-8ffe6ea3ea99>

**USER:**
I travel a lot and my Windows 11 laptop is never near a plug. I forget to turn the power saving thing on every time. Is there a way to make the laptop do it by itself when the battery gets low?

**ASSISTANT:**
Yes, you can set it to turn on by itself:

1. Select **Start**, then **Settings**.
2. Select **System**, then **Power & battery**.
3. Expand **Energy saver**.
4. Next to **Turn energy saver on when battery level is at**, choose the battery percentage you want.

Once the battery drops to that level, Energy saver turns on.

---

## tr174-d
- task: Turn on battery saver (energy saver) | platform: Windows 11 laptop | scenario: followup | sensitive: False
- sources: Microsoft Support: Battery saving tips (Windows 11 Energy saver) <https://support.microsoft.com/windows/battery-saving-tips-a850d64d-ee8e-c8d2-6c75-8ffe6ea3ea99>

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

---

## tr174-e
- task: Turn on battery saver (energy saver) | platform: Windows 11 laptop | scenario: constraint | sensitive: False
- sources: Microsoft Support: Battery saving tips (Windows 11 Energy saver) <https://support.microsoft.com/windows/battery-saving-tips-a850d64d-ee8e-c8d2-6c75-8ffe6ea3ea99>

**USER:**
I am on a long train ride with my Windows 11 laptop and there are no outlets. I want Energy saver on right now and I want it to stay on until I plug in again. I do not want to pick a battery percentage. What do I do?

**ASSISTANT:**
You can turn it on now and leave it on:

1. Select **Start**, then **Settings**.
2. Select **System**, then **Power & battery**.
3. Expand **Energy saver**.
4. Set **Always use energy saver** to **On**.

It stays on until you next plug in the laptop.

---

## tr175-a
- task: Pair a Bluetooth device | platform: Windows 11 | scenario: direct | sensitive: False
- sources: Microsoft Support: Pair a Bluetooth device in Windows <https://support.microsoft.com/en-US/windows/pair-a-bluetooth-device-in-windows-2be7b51f-6ae9-b757-a3b9-95ee40c3e242>

**USER:**
I just got wireless headphones and want to hook them up to my Windows 11 PC through Bluetooth. Where do I start?

**ASSISTANT:**
Here is how to pair them:

1. Make sure Bluetooth is turned on. Select the **Network**, **Sound**, or **Battery** icon near the clock and check that the **Bluetooth** tile is on.
2. Put the headphones in pairing mode so the computer can find them. The way to do this depends on the headphones, so check their manual.
3. Select the **Network**, **Sound**, or **Battery** icon on the taskbar again.
4. Select the small arrow next to the Bluetooth quick setting, labeled **Manage Bluetooth devices**.
5. Under **New devices**, select your headphones.
6. Follow any extra prompts, then select **Done**.

After this, they reconnect by themselves whenever Bluetooth is on and they are in range.

---

## tr175-b
- task: Pair a Bluetooth device | platform: Windows 11 | scenario: missing_info | sensitive: False
- sources: Microsoft Support: Pair a Bluetooth device in Windows <https://support.microsoft.com/en-US/windows/pair-a-bluetooth-device-in-windows-2be7b51f-6ae9-b757-a3b9-95ee40c3e242>

**USER:**
I need to pair my bluetooth speaker with my computer

**ASSISTANT:**
I can help with that. Is your computer a **Windows PC** or a **Mac**?

---

## tr175-c
- task: Pair a Bluetooth device | platform: Windows 11 | scenario: direct_messy | sensitive: False
- sources: Microsoft Support: Pair a Bluetooth device in Windows <https://support.microsoft.com/en-US/windows/pair-a-bluetooth-device-in-windows-2be7b51f-6ae9-b757-a3b9-95ee40c3e242>

**USER:**
My daughter bought me a little Bluetooth printer for my Windows 11 computer so I can stop using that long cable. It is turned on and the light is blinking. I have never done this before and I do not want to mess up my settings. How do I connect it?

**ASSISTANT:**
Here is how to add it:

1. Make sure the printer is discoverable. Your printer's manual shows how.
2. Select **Start**, then **Settings**.
3. Select **Bluetooth & devices**, and check that the **Bluetooth** switch is **On**.
4. Select **Printers & scanners**.
5. Next to **Add a printer or scanner**, select **Add device**.
6. Wait while Windows searches. This can take a few minutes.
7. When your printer appears, select **Add device** next to it.

---

## tr175-d
- task: Pair a Bluetooth device | platform: Windows 11 | scenario: followup | sensitive: False
- sources: Microsoft Support: Pair a Bluetooth device in Windows <https://support.microsoft.com/en-US/windows/pair-a-bluetooth-device-in-windows-2be7b51f-6ae9-b757-a3b9-95ee40c3e242>

**USER:**
I need to pair my bluetooth speaker with my computer

**ASSISTANT:**
I can help with that. Is your computer a **Windows PC** or a **Mac**?

**USER:**
its a windows 11 pc

**ASSISTANT:**
Here is how to pair the speaker:

1. Make sure Bluetooth is turned on. Select the **Network**, **Sound**, or **Battery** icon near the clock and check that the **Bluetooth** tile is on.
2. Put the speaker in pairing mode. Check its manual for how.
3. Select the **Network**, **Sound**, or **Battery** icon on the taskbar again.
4. Select the small arrow next to the Bluetooth quick setting, labeled **Manage Bluetooth devices**.
5. Under **New devices**, select your speaker.
6. Follow any extra prompts, then select **Done**.

---

## tr175-e
- task: Pair a Bluetooth device | platform: Windows 11 | scenario: constraint | sensitive: False
- sources: Microsoft Support: Pair a Bluetooth device in Windows <https://support.microsoft.com/en-US/windows/pair-a-bluetooth-device-in-windows-2be7b51f-6ae9-b757-a3b9-95ee40c3e242>

**USER:**
I would like to connect my Bluetooth mouse to my Windows 11 laptop but I do not want to go digging through the Settings app, it confuses me. Is there a quicker way from the bottom of the screen?

**ASSISTANT:**
Yes, you can do it from the taskbar:

1. Select the **Network**, **Sound**, or **Battery** icon on the taskbar, near the clock, and make sure the **Bluetooth** tile is on.
2. Put the mouse in pairing mode. Check its manual for how.
3. Select the **Network**, **Sound**, or **Battery** icon again.
4. Select the small arrow next to the Bluetooth quick setting, labeled **Manage Bluetooth devices**.
5. Under **New devices**, select your mouse. If you do not see it, look through **Your devices**.
6. Follow any extra prompts, then select **Done**.

---

## tr176-a
- task: Turn off notifications from an app | platform: Windows 11 | scenario: direct | sensitive: False
- sources: Microsoft Support: Notifications and Do Not Disturb in Windows <https://support.microsoft.com/en-us/windows/notifications-and-do-not-disturb-in-windows-feeca47f-0baf-5680-16f0-8801db1a8466>

**USER:**
How do I stop one app from sending me notifications on Windows 11?

**ASSISTANT:**
You can turn off alerts for one app in Settings:

1. Select **Start**, then **Settings**.
2. Select **System**, then **Notifications**.
3. Under **Notifications from apps and other senders**, select the app you want to quiet.
4. Switch off **Turn notifications on or off**.

That stops alerts from that app.

---

## tr176-c
- task: Turn off notifications from an app | platform: Windows 11 | scenario: direct_messy | sensitive: False
- sources: Microsoft Support: Notifications and Do Not Disturb in Windows <https://support.microsoft.com/en-us/windows/notifications-and-do-not-disturb-in-windows-feeca47f-0baf-5680-16f0-8801db1a8466>

**USER:**
Every few minutes a little box pops up in the corner of my Windows 11 screen from the Solitaire game telling me to come back and play. It drives me crazy when I am writing emails. I do not want to uninstall it, I just want it to leave me alone.

**ASSISTANT:**
You can silence it without removing the game:

1. Select **Start**, then **Settings**.
2. Select **System**, then **Notifications**.
3. Under **Notifications from apps and other senders**, select the game.
4. Switch off **Turn notifications on or off**.

The game stays installed, and it stops sending you alerts.

---

## tr176-d
- task: Turn off notifications from an app | platform: Windows 11 | scenario: followup | sensitive: False
- sources: Microsoft Support: Notifications and Do Not Disturb in Windows <https://support.microsoft.com/en-us/windows/notifications-and-do-not-disturb-in-windows-feeca47f-0baf-5680-16f0-8801db1a8466>

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

---

## tr176-e
- task: Turn off notifications from an app | platform: Windows 11 | scenario: constraint | sensitive: False
- sources: Microsoft Support: Notifications and Do Not Disturb in Windows <https://support.microsoft.com/en-us/windows/notifications-and-do-not-disturb-in-windows-feeca47f-0baf-5680-16f0-8801db1a8466>

**USER:**
On my Windows 11 computer my Mail app makes a loud ding for every message. I still want to see the messages, I just do not want the sound. How do I turn off only the sound?

**ASSISTANT:**
You can keep the alerts and turn off just the sound:

1. Select **Start**, then **Settings**.
2. Select **System**, then **Notifications**.
3. Under **Notifications from apps and other senders**, select **Mail**.
4. Switch off **Play a sound**.

Leave **Turn notifications on or off** switched on, so the messages still show up.

---

## tr176-r
- task: Turn off notifications from an app | platform: Windows 11 | scenario: failure_recovery | sensitive: False
- sources: Microsoft Support: Notifications and Do Not Disturb in Windows <https://support.microsoft.com/en-us/windows/notifications-and-do-not-disturb-in-windows-feeca47f-0baf-5680-16f0-8801db1a8466>

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

---

## tr177-a
- task: Use Magnifier to make things on screen bigger (keyboard shortcuts) | platform: Windows 11 | scenario: direct | sensitive: False
- sources: Microsoft Support: How to quickly change the zoom level for Magnifier (and Keyboard shortcuts for Magnifier) <https://support.microsoft.com/en-US/accessibility/windows/magnifier/how-to-quickly-change-the-zoom-level-for-magnifier>

**USER:**
The words on my Windows 11 computer are too small to read. Can I make them bigger with Magnifier?

**ASSISTANT:**
Yes. Use the keyboard:

1. Press the **Windows key + Plus sign (+)**. This turns Magnifier on.
2. Press **Windows key + Plus sign (+)** again to zoom in more.

---

## tr177-b
- task: Use Magnifier to make things on screen bigger (keyboard shortcuts) | platform: Windows 11 | scenario: missing_info | sensitive: False
- sources: Microsoft Support: How to quickly change the zoom level for Magnifier (and Keyboard shortcuts for Magnifier) <https://support.microsoft.com/en-US/accessibility/windows/magnifier/how-to-quickly-change-the-zoom-level-for-magnifier>

**USER:**
how do i make everything on the screen bigger so i can see it

**ASSISTANT:**
I can help with that. Is your computer a **Windows PC** or a **Mac**?

---

## tr177-c
- task: Use Magnifier to make things on screen bigger (keyboard shortcuts) | platform: Windows 11 | scenario: direct_messy | sensitive: False
- sources: Microsoft Support: How to quickly change the zoom level for Magnifier (and Keyboard shortcuts for Magnifier) <https://support.microsoft.com/en-US/accessibility/windows/magnifier/how-to-quickly-change-the-zoom-level-for-magnifier>

**USER:**
My eyes are not what they used to be and I am trying to read a recipe online on my Windows 11 computer. I would like to make the screen bigger for a bit and then get it back to normal after, because it is hard to do my other things when everything is huge. How do I do all of that?

**ASSISTANT:**
You can do all of it with the keyboard:

1. Press the **Windows key + Plus sign (+)** to turn Magnifier on.
2. Press **Windows key + Plus sign (+)** again to make things larger.
3. If it gets too big, press the **Windows key + Minus sign (-)** to make things smaller.
4. When you are done reading, press the **Windows key + Esc** to turn Magnifier off.

---

## tr177-d
- task: Use Magnifier to make things on screen bigger (keyboard shortcuts) | platform: Windows 11 | scenario: followup | sensitive: False
- sources: Microsoft Support: How to quickly change the zoom level for Magnifier (and Keyboard shortcuts for Magnifier) <https://support.microsoft.com/en-US/accessibility/windows/magnifier/how-to-quickly-change-the-zoom-level-for-magnifier>

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

---

## tr177-e
- task: Use Magnifier to make things on screen bigger (keyboard shortcuts) | platform: Windows 11 | scenario: constraint | sensitive: False
- sources: Microsoft Support: How to quickly change the zoom level for Magnifier (and Keyboard shortcuts for Magnifier) <https://support.microsoft.com/en-US/accessibility/windows/magnifier/how-to-quickly-change-the-zoom-level-for-magnifier>; Microsoft Support: Keyboard shortcuts for Magnifier <https://support.microsoft.com/en-us/accessibility/windows/magnifier/keyboard-shortcuts-for-magnifier>

**USER:**
I use Magnifier on my Windows 11 PC, but I do not want the whole screen to get big, I only want a part of it magnified like a lens. Is that possible, and how do I switch to it?

**ASSISTANT:**
Yes, Magnifier has a Lens view:

1. If Magnifier is not on yet, press the **Windows key + Plus sign (+)**.
2. Press **Ctrl + Alt + L**. This switches to Lens view.

To switch back to **Full screen view**, press **Ctrl + Alt + F**.

---

## tr177-r
- task: Use Magnifier to make things on screen bigger (keyboard shortcuts) | platform: Windows 11 | scenario: failure_recovery | sensitive: False
- sources: Microsoft Support: How to quickly change the zoom level for Magnifier (and Keyboard shortcuts for Magnifier) <https://support.microsoft.com/en-US/accessibility/windows/magnifier/how-to-quickly-change-the-zoom-level-for-magnifier>

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

---

## tr178-a
- task: Turn on live captions | platform: Windows 11 | scenario: direct | sensitive: False
- sources: Microsoft Support: Use live captions to better understand audio <https://support.microsoft.com/windows/use-live-captions-to-better-understand-audio-b52da59c-14b8-4031-aeeb-f6a47e6055df>

**USER:**
Is there a way to see words on screen for videos I watch on my Windows 11 computer? I have trouble hearing.

**ASSISTANT:**
Yes, Windows 11 has live captions. The quickest way is the keyboard:

1. Press **Windows key + Ctrl + L**.
2. The first time, Windows asks for your consent to process voice on your device. Follow the prompts.
3. If asked, let it download the language files it needs.

Captions then appear for speech in what your computer plays.

---

## tr178-b
- task: Turn on live captions | platform: Windows 11 | scenario: missing_info | sensitive: False
- sources: Microsoft Support: Use live captions to better understand audio <https://support.microsoft.com/windows/use-live-captions-to-better-understand-audio-b52da59c-14b8-4031-aeeb-f6a47e6055df>

**USER:**
can i get subtitles to show up for everything that plays on my computer

**ASSISTANT:**
I can help with that. Is your computer a **Windows PC** or a **Mac**?

---

## tr178-c
- task: Turn on live captions | platform: Windows 11 | scenario: direct_messy | sensitive: False
- sources: Microsoft Support: Use live captions to better understand audio <https://support.microsoft.com/windows/use-live-captions-to-better-understand-audio-b52da59c-14b8-4031-aeeb-f6a47e6055df>

**USER:**
My husband and I watch our church service online on our Windows 11 computer and he cannot make out what the pastor says. I do not like using key combinations because I always press the wrong ones. Can you walk me through turning on captions using the Settings app?

**ASSISTANT:**
Yes, here is the way through Settings:

1. Select **Start**, then **Settings**.
2. Select **Accessibility**, then **Captions**.
3. Turn on the **Live captions** toggle.
4. The first time, follow the prompts. Windows asks for your consent to process voice on your device and may download language files.

---

## tr178-d
- task: Turn on live captions | platform: Windows 11 | scenario: followup | sensitive: False
- sources: Microsoft Support: Use live captions to better understand audio <https://support.microsoft.com/windows/use-live-captions-to-better-understand-audio-b52da59c-14b8-4031-aeeb-f6a47e6055df>

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

---

## tr178-e
- task: Turn on live captions | platform: Windows 11 | scenario: constraint | sensitive: False
- sources: Microsoft Support: Use live captions to better understand audio <https://support.microsoft.com/windows/use-live-captions-to-better-understand-audio-b52da59c-14b8-4031-aeeb-f6a47e6055df>

**USER:**
I want live captions on my Windows 11 PC, but I can only use the mouse right now, my keyboard is not working. Can I turn them on from the taskbar?

**ASSISTANT:**
Yes, you can do it with the mouse only:

1. Select the **battery**, **network**, or **volume** icon on the taskbar, near the clock. This opens quick settings.
2. Turn on **Live captions**.

The first time, follow the prompts. Windows asks for your consent to process voice on your device and may download language files.

---

## tr179-a
- task: Make the screen brighter or dimmer | platform: Windows 11 | scenario: direct | sensitive: False
- sources: Microsoft Support: Change display brightness and color in Windows <https://support.microsoft.com/en-us/help/4026946>

**USER:**
The screen on my Windows 11 laptop is too bright. How do I make it dimmer?

**ASSISTANT:**
You can change it from the taskbar:

1. Select the **Network** icon on the right side of the taskbar.
2. Move the **Brightness** slider to the left to dim the screen, or to the right to make it brighter.

---

## tr179-b
- task: Make the screen brighter or dimmer | platform: Windows 11 | scenario: missing_info | sensitive: False
- sources: Microsoft Support: Change display brightness and color in Windows <https://support.microsoft.com/en-us/help/4026946>

**USER:**
my screen is too dark how do i fix it

**ASSISTANT:**
I can help with that. Is your computer a **Windows PC** or a **Mac**?

---

## tr179-c
- task: Make the screen brighter or dimmer | platform: Windows 11 | scenario: direct_messy | sensitive: False
- sources: Microsoft Support: Change display brightness and color in Windows <https://support.microsoft.com/en-us/help/4026946>

**USER:**
I read a lot in the evenings on my Windows 11 laptop and the screen hurts my eyes. My son once showed me a slider but I forget where it was. Could you tell me how to find it in Settings so I can write it down?

**ASSISTANT:**
Here is the way through Settings:

1. Select **Start**, then **Settings**.
2. Select **System**, then **Display**.
3. Use the **Brightness** slider. Move it left to make the screen dimmer.

---

## tr179-d
- task: Make the screen brighter or dimmer | platform: Windows 11 | scenario: followup | sensitive: False
- sources: Microsoft Support: Change display brightness and color in Windows <https://support.microsoft.com/en-us/help/4026946>

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

---

## tr179-r
- task: Make the screen brighter or dimmer | platform: Windows 11 | scenario: failure_recovery | sensitive: False
- sources: Microsoft Support: Change display brightness and color in Windows <https://support.microsoft.com/en-us/help/4026946>

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

---

## tr186-a
- task: Save a website as a favorite | platform: Microsoft Edge (computer) | scenario: direct | sensitive: False
- sources: Microsoft Support: Add a site to my favorites in Microsoft Edge <https://support.microsoft.com/en-us/microsoft-edge/add-a-site-to-my-favorites-in-microsoft-edge-ed39f9ef-0b77-86c5-5cc5-ccf8d33350c7>

**USER:**
How do I save a website as a favorite in Edge on my computer?

**ASSISTANT:**
Here is how to save the page you are on as a favorite in Microsoft Edge:

1. Open Microsoft Edge and go to the website.
2. Select the **Add this page to favorites** button in the address bar.
3. If you like, type a new name or choose a different folder.
4. Select **Done**.

If you do not see that button in the address bar, select **Settings and more**, then **Favorites**, then **More options**, then **Add this page to favorites**.

---

## tr186-b
- task: Save a website as a favorite | platform: Microsoft Edge (computer) | scenario: missing_info | sensitive: False
- sources: Microsoft Support: Add a site to my favorites in Microsoft Edge <https://support.microsoft.com/en-us/microsoft-edge/add-a-site-to-my-favorites-in-microsoft-edge-ed39f9ef-0b77-86c5-5cc5-ccf8d33350c7>

**USER:**
I want to save a website so I can get back to it fast without typing it in again.

**ASSISTANT:**
I can help with that. Which browser are you using: **Microsoft Edge**, **Chrome**, or something else?

---

## tr186-d
- task: Save a website as a favorite | platform: Microsoft Edge (computer) | scenario: followup | sensitive: False
- sources: Microsoft Support: Add a site to my favorites in Microsoft Edge <https://support.microsoft.com/en-us/microsoft-edge/add-a-site-to-my-favorites-in-microsoft-edge-ed39f9ef-0b77-86c5-5cc5-ccf8d33350c7>

**USER:**
I want to save a website so I can get back to it fast without typing it in again.

**ASSISTANT:**
I can help with that. Which browser are you using: **Microsoft Edge**, **Chrome**, or something else?

**USER:**
Edge, on my laptop

**ASSISTANT:**
Thanks. In Microsoft Edge, saving a site as a favorite takes a few clicks:

1. Go to the website you want to keep.
2. Select the **Add this page to favorites** button in the address bar.
3. If you want, change the name or pick a different folder.
4. Select **Done**.

---

## tr186-e
- task: Save a website as a favorite | platform: Microsoft Edge (computer) | scenario: constraint | sensitive: False
- sources: Microsoft Support: Add a site to my favorites in Microsoft Edge <https://support.microsoft.com/en-us/microsoft-edge/add-a-site-to-my-favorites-in-microsoft-edge-ed39f9ef-0b77-86c5-5cc5-ccf8d33350c7>

**USER:**
I have about eight tabs open in Edge on my computer for my daughter's wedding planning, but I only want to save the one I'm looking at right now, the florist's page. I don't want all eight saved as favorites. How do I do just the one?

**ASSISTANT:**
You can save just the florist's page. Make sure that page is the one showing, then:

1. Select **Settings and more**.
2. Select **Favorites**.
3. Select **More options**.
4. Select **Add this page to favorites**.

Do not choose **Add open pages to favorites**. That one saves all your open pages.

---

## tr186-r
- task: Save a website as a favorite | platform: Microsoft Edge (computer) | scenario: failure_recovery | sensitive: False
- sources: Microsoft Support: Add a site to my favorites in Microsoft Edge <https://support.microsoft.com/en-us/microsoft-edge/add-a-site-to-my-favorites-in-microsoft-edge-ed39f9ef-0b77-86c5-5cc5-ccf8d33350c7>

**USER:**
Please show me how to add a favorite in Microsoft Edge on my computer.

**ASSISTANT:**
Sure. Here is how:

1. Open Microsoft Edge and go to the site.
2. Select the **Add this page to favorites** button in the address bar.
3. If you want, rename it or choose a different folder.
4. Select **Done**.

**USER:**
I looked in the address bar and I don't see any button like that.

**ASSISTANT:**
No problem. You can use the menu instead:

1. Select **Settings and more**.
2. Select **Favorites**.
3. Select **More options**.
4. Select **Add this page to favorites**.

---

## tr187-a
- task: Bookmark a website in Chrome on the phone | platform: Chrome (Android) | scenario: direct | sensitive: False
- sources: Chrome Help: Create, find and edit bookmarks in Chrome (Android phone section) <https://support.google.com/chrome/answer/188842?hl=en&co=GENIE.Platform%3DAndroid>

**USER:**
How do I bookmark a website in Chrome on my Android phone?

**ASSISTANT:**
Here is how to bookmark a page in Chrome on your Android phone:

1. Open Chrome and go to the page you want to save.
2. To the right of the address bar, tap **More**.
3. Tap **Add to bookmarks**.

---

## tr187-c
- task: Bookmark a website in Chrome on the phone | platform: Chrome (Android) | scenario: direct_messy | sensitive: False
- sources: Chrome Help: Create, find and edit bookmarks in Chrome (Android phone section) <https://support.google.com/chrome/answer/188842?hl=en&co=GENIE.Platform%3DAndroid>

**USER:**
I have a Google Pixel phone and I use Chrome for the weather site every single day. My neighbor said I can save it so I don't have to search for it every time. I have the weather site open right now. How do I save it, and then how would I open it again tomorrow?

**ASSISTANT:**
You can bookmark it now and open it from your bookmarks tomorrow.

To save it:
1. With the weather site open, tap **More**, to the right of the address bar.
2. Tap **Add to bookmarks**.

To open it again:
1. Open Chrome.
2. Tap **More** at the top right.
3. Tap **Bookmarks**.
4. Tap a folder.
5. Tap the bookmark.

---

## tr187-d
- task: Bookmark a website in Chrome on the phone | platform: Chrome (Android) | scenario: followup | sensitive: False
- sources: Chrome Help: Create, find and edit bookmarks in Chrome (Android phone section) <https://support.google.com/chrome/answer/188842?hl=en&co=GENIE.Platform%3DAndroid>

**USER:**
i want to save a website on my phone so i dont lose it. i use chrome

**ASSISTANT:**
I can help with that. Is your phone an **Android** phone or an **iPhone**?

**USER:**
android, a samsung

**ASSISTANT:**
Thanks. To bookmark a site in Chrome on your Android phone:

1. Open Chrome and go to the website.
2. To the right of the address bar, tap **More**.
3. Tap **Add to bookmarks**.

---

## tr187-e
- task: Bookmark a website in Chrome on the phone | platform: Chrome (Android) | scenario: constraint | sensitive: False
- sources: Chrome Help: Create, find and edit bookmarks in Chrome (Android phone section) <https://support.google.com/chrome/answer/188842?hl=en&co=GENIE.Platform%3DAndroid>

**USER:**
On my Android phone the Chrome address bar is at the bottom of the screen, not the top. My son changed something. I want to bookmark a recipe page I'm on and then find it again later. Where do I tap?

**ASSISTANT:**
You can do both with the bar at the bottom.

To save the recipe:
1. To the right of the address bar, tap **More**.
2. Tap **Add to bookmarks**.

To find it later:
1. Open Chrome.
2. Swipe up on the address bar.
3. Tap **Bookmarks**.
4. Tap a folder, then tap the bookmark.

---

## tr187-r
- task: Bookmark a website in Chrome on the phone | platform: Chrome (Android) | scenario: failure_recovery | sensitive: False
- sources: Chrome Help: Create, find and edit bookmarks in Chrome (Android phone section) <https://support.google.com/chrome/answer/188842?hl=en&co=GENIE.Platform%3DAndroid>

**USER:**
Can you tell me how to bookmark a page in Chrome on my Android phone?

**ASSISTANT:**
Yes. Here is how:

1. Open Chrome and go to the page.
2. To the right of the address bar, tap **More**.
3. Tap **Add to bookmarks**.

**USER:**
ok I did that. but now how do I get back to it? I can't find where it went

**ASSISTANT:**
Your bookmark is saved. To open it:

1. Open Chrome.
2. At the top right, tap **More**, then tap **Bookmarks**.
3. Tap a folder. If you recently opened a folder, you will see that same folder. To see other folders, tap **Back** at the top left.
4. Tap the bookmark.

If your address bar is at the bottom, swipe up on it and tap **Bookmarks** instead. You can also type in the **Search your bookmarks** bar at the top.

---

## tr188-a
- task: Make web pages bigger | platform: Microsoft Edge (computer) | scenario: direct | sensitive: False
- sources: Microsoft Support: Accessibility features in Microsoft Edge <https://support.microsoft.com/en-us/microsoft-edge/accessibility-features-in-microsoft-edge-4c696192-338e-9465-b2cd-bd9b698ad19a>

**USER:**
The writing on websites is too small in Edge on my computer. How do I make it bigger?

**ASSISTANT:**
You can zoom in on the page you are looking at:

1. Select **Settings and more**.
2. Select **Zoom in**.
3. Select **Zoom in** again until the page is the size you like.

---

## tr188-b
- task: Make web pages bigger | platform: Microsoft Edge (computer) | scenario: missing_info | sensitive: False
- sources: Microsoft Support: Accessibility features in Microsoft Edge <https://support.microsoft.com/en-us/microsoft-edge/accessibility-features-in-microsoft-edge-4c696192-338e-9465-b2cd-bd9b698ad19a>

**USER:**
Everything on the websites I visit looks so tiny. Can you make the pages bigger?

**ASSISTANT:**
I can help with that. Which web browser are you using: **Edge**, **Chrome**, or something else?

---

## tr188-c
- task: Make web pages bigger | platform: Microsoft Edge (computer) | scenario: direct_messy | sensitive: False
- sources: Microsoft Support: Accessibility features in Microsoft Edge <https://support.microsoft.com/en-us/microsoft-edge/accessibility-features-in-microsoft-edge-4c696192-338e-9465-b2cd-bd9b698ad19a>

**USER:**
My eyes aren't what they used to be and I read the news on my Windows computer using Microsoft Edge. The words are tiny. My husband mentioned there is a way to do it from the keyboard without going into any menus, and I would rather learn that. I have a mouse with a wheel on it too if that helps.

**ASSISTANT:**
Yes, there are two quick ways. With the news page open:

1. Hold down the **Ctrl** key.
2. Press the **plus sign** key. Each press makes the page bigger.

Or, with the mouse:
1. Hold down the **Ctrl** key.
2. Roll the mouse wheel up to make the page bigger. Roll it down to make it smaller.

---

## tr188-d
- task: Make web pages bigger | platform: Microsoft Edge (computer) | scenario: followup | sensitive: False
- sources: Microsoft Support: Accessibility features in Microsoft Edge <https://support.microsoft.com/en-us/microsoft-edge/accessibility-features-in-microsoft-edge-4c696192-338e-9465-b2cd-bd9b698ad19a>

**USER:**
Everything on the websites I visit looks so tiny. Can you make the pages bigger?

**ASSISTANT:**
I can help with that. Which web browser are you using: **Edge**, **Chrome**, or something else?

**USER:**
Edge on my computer

**ASSISTANT:**
Thanks. To make the page you are on bigger in Edge:

1. Select **Settings and more**.
2. Select **Zoom in**.
3. Select **Zoom in** again until the page is big enough.

---

## tr188-e
- task: Make web pages bigger | platform: Microsoft Edge (computer) | scenario: constraint | sensitive: False
- sources: Microsoft Support: Accessibility features in Microsoft Edge <https://support.microsoft.com/en-us/microsoft-edge/accessibility-features-in-microsoft-edge-4c696192-338e-9465-b2cd-bd9b698ad19a>

**USER:**
I use Microsoft Edge on my computer and I keep making each website bigger one at a time. That is a lot of work. Can I set it once so that every website is bigger from now on, without doing it for each page?

**ASSISTANT:**
Yes. You can set one zoom level for all websites:

1. Select **Settings and more**.
2. Select **Settings**.
3. Select **Accessibility**.
4. Under **Visibility**, open the **Page zoom** drop-down.
5. Choose the zoom level you want.

---

## tr189-a
- task: Block pop-ups from a website in Chrome (Chrome already blocks pop-ups by default) | platform: Chrome (computer) | scenario: direct | sensitive: False
- sources: Chrome Help: Block or allow pop-ups in Chrome <https://support.google.com/chrome/answer/95472>

**USER:**
A website keeps letting pop-ups through in Chrome on my computer. How do I block pop-ups for that site? I can see it in the allowed list.

**ASSISTANT:**
Here is how to block pop-ups from a site that is in the allowed list:

1. Click **More** (top right), then **Settings**.
2. Click **Privacy and security**.
3. Click **Site Settings**.
4. Click **Pop-ups and redirects**.
5. Under **Allowed to send pop-ups and use redirects**, find the site.
6. To the right of the site, click **More**, then **Block**.

---

# Rule scan input, part 03 (50 examples)

## tr026-c
- task: Turn on Wi-Fi Calling | platform: iPhone | scenario: direct_messy | sensitive: False
- sources: Apple Support: Make a call with Wi-Fi Calling <https://support.apple.com/en-us/108066>

**USER:**
I have an iPhone 15 on Verizon, iOS 18. Cell signal inside my house is one bar but Wi-Fi is strong. I read about Wi-Fi Calling. Where is the setting?

**ASSISTANT:**
It's in Settings.

1. Open the **Settings** app.
2. Tap **Cellular**.
3. Tap **Wi-Fi Calling**.
4. Turn on **Wi-Fi Calling on This iPhone**.
5. Tap **Enable** when asked.

Your iPhone may ask you to enter or confirm your address. This address is used for emergency services, so please enter it carefully.

Wi-Fi Calling only works if your phone company offers it. To see that it's working, open Control Center. If Wi-Fi Calling is available, you'll see **Wi-Fi** in the status bar there. Then you make calls the same way you always do.

If you don't see **Wi-Fi Calling** in that menu, your phone company may not offer it. Tell me what you see, and you can also ask your phone company.

---

## tr026-d
- task: Turn on Wi-Fi Calling | platform: iPhone | scenario: followup | sensitive: False
- sources: Apple Support: Make a call with Wi-Fi Calling <https://support.apple.com/en-us/108066>

**USER:**
calls keep dropping in my house, what can I do

**ASSISTANT:**
That's frustrating. Is your phone an **iPhone** or an Android phone?

**USER:**
It's an iPhone 12.

**ASSISTANT:**
Thanks. This should help.

iPhone has a feature called **Wi-Fi Calling** that lets you make calls over Wi-Fi when there is little or no cellular coverage. Turning it on takes about a minute.

1. Open the **Settings** app.
2. Tap **Cellular**.
3. Tap **Wi-Fi Calling**.
4. Turn on **Wi-Fi Calling on This iPhone**.
5. Tap **Enable** when asked.

Your iPhone may ask you to enter or confirm your address. This address is used for emergency services, so please enter it carefully.

Wi-Fi Calling only works if your phone company offers it. To see that it's working, open Control Center. If Wi-Fi Calling is available, you'll see **Wi-Fi** in the status bar there. Then you make calls the same way you always do.

If you don't see **Wi-Fi Calling** in that menu, your phone company may not offer it. Tell me what you see, and you can also ask your phone company.

---

## tr026-e
- task: Turn on Wi-Fi Calling | platform: iPhone | scenario: constraint | sensitive: False
- sources: Apple Support: Make a call with Wi-Fi Calling <https://support.apple.com/en-us/108066>

**USER:**
My iPhone has two phone lines, my personal number and a work number. The signal is bad at my desk, but I only want Wi-Fi Calling for my work line. How do I turn it on for just that one?

**ASSISTANT:**
When you have two lines, you pick the line first.

1. Open the **Settings** app.
2. Tap **Cellular**.
3. Select your **work line**.
4. Tap **Wi-Fi Calling**.
5. Turn on **Wi-Fi Calling on This iPhone**.
6. Tap **Enable**.

You may be asked to enter or confirm your address for emergency services. Wi-Fi Calling also needs your carrier to offer it.

---

## tr027-a
- task: Take a screenshot | platform: Android | scenario: direct | sensitive: False
- sources: Android Help: Take a screenshot or record your screen <https://support.google.com/android/answer/9075928?hl=en>

**USER:**
How do I take a screenshot on my Android phone?

**ASSISTANT:**
Here's how to take a picture of your screen. It only takes a second.

1. Get the screen showing what you want to capture.
2. Press the **Power** button and the **Volume Down** button **at the same time**, then let go.

You'll see a small preview of the screenshot in the bottom-left corner.

**To find it later:** open the **Photos** app, tap **Collections** at the bottom, then **On this device**, then **Screenshots**. If your phone uses a **Gallery** app instead, look for the **Screenshots** album there.

If pressing both buttons doesn't work, hold the **Power** button for a few seconds and tap **Screenshot**.

---

## tr027-b
- task: Take a screenshot | platform: Android | scenario: missing_info | sensitive: False
- sources: Android Help: Take a screenshot or record your screen <https://support.google.com/android/answer/9075928?hl=en>

**USER:**
how do i take a screenshot

**ASSISTANT:**
Sure. The buttons are different depending on the phone. Is yours an **iPhone** or an **Android** phone, like Samsung or Google Pixel?

---

## tr027-c
- task: Take a screenshot | platform: Android | scenario: missing_info | sensitive: False
- sources: Android Help: Take a screenshot or record your screen <https://support.google.com/android/answer/9075928?hl=en>

**USER:**
My grandson is helping me with my phone over the phone and he keeps saying send me a screenshot so he can see what I see. I don't know what that is or how to do it.

**ASSISTANT:**
A screenshot is a picture of exactly what's on your screen, so your grandson can see it too. The buttons to take one depend on your phone.

**Is your phone an iPhone or an Android phone** (like Samsung or Google Pixel)? If you're not sure, an iPhone has an apple logo on the back.

---

## tr027-d
- task: Take a screenshot | platform: Android | scenario: followup | sensitive: False
- sources: Android Help: Take a screenshot or record your screen <https://support.google.com/android/answer/9075928?hl=en>

**USER:**
how do i take a screenshot

**ASSISTANT:**
Sure. The buttons are different depending on the phone. Is yours an **iPhone** or an **Android** phone, like Samsung or Google Pixel?

**USER:**
Android. Motorola.

**ASSISTANT:**
Thanks. Here's how to take a picture of your screen on your Motorola. It only takes a second.

1. Get the screen showing what you want to capture.
2. Press the **Power** button and the **Volume Down** button **at the same time**, then let go.

You'll see a small preview of the screenshot in the bottom-left corner.

**To find it later:** open the **Photos** app, tap **Collections** at the bottom, then **On this device**, then **Screenshots**. If your phone uses a **Gallery** app instead, open it, tap **Album view**, then tap **Screenshots folder**.

If pressing both buttons doesn't work, hold the **Power** button for a few seconds and tap **Screenshot**.

---

## tr027-e
- task: Take a screenshot | platform: Android | scenario: constraint | sensitive: False
- sources: Android Help: Take a screenshot or record your screen <https://support.google.com/android/answer/9075928?hl=en>

**USER:**
I have arthritis in my hands and I can't press two buttons at the same time on my Android phone. My daughter asked me to send her a picture of an error message. Is there another way to take a screenshot?

**ASSISTANT:**
Yes, you can do it with one button.

1. Open the screen you want to capture.
2. Press and hold the **Power** button for a few seconds.
3. Tap **Screenshot**.

You will see a small preview at the bottom left of the screen. If **Screenshot** doesn't appear, check your phone maker's support site.

---

## tr027-r
- task: Take a screenshot | platform: Android | scenario: failure_recovery | sensitive: False
- sources: Android Help: Take a screenshot or record your screen <https://support.google.com/android/answer/9075928?hl=en>

**USER:**
What's the way to take a screenshot on an Android phone?

**ASSISTANT:**
Here is how.

1. Open the screen you want to capture.
2. Press the **Power** button and the **Volume down** button at the same time.

You will see a small preview at the bottom left of the screen. If that doesn't work, press and hold **Power** for a few seconds, then tap **Screenshot**.

**USER:**
I think it worked because I saw a little picture, but now where do I find it?

**ASSISTANT:**
Your screenshots are saved in the Photos app.

1. Open the **Photos** app.
2. At the bottom, tap **Collections**.
3. Tap **On this device**, then tap **Screenshots**.
4. Tap the screenshot, then tap the **Share** icon to send it.

If you don't have a Photos app, open the **Gallery** app, tap **Album view**, then open the **Screenshots** folder.

---

## tr028-a
- task: Take a screenshot | platform: Windows 11 | scenario: direct | sensitive: False
- sources: Microsoft Support: Use Snipping Tool to capture screenshots <https://support.microsoft.com/en-us/windows/apps/use-snipping-tool-to-capture-screenshots>

**USER:**
How do I take a screenshot on my Windows 11 laptop?

**ASSISTANT:**
The quickest way uses three keys at once. It takes a few seconds.

1. Press and hold the **Windows logo key** and the **Shift** key, then press **S**.
2. The screen dims and shows a few capture choices.
3. Choose the shape you want: a rectangle, a window, or the full screen.
4. If you chose rectangle, click and drag over the part of the screen you want.

Your screenshot is saved automatically in your **Screenshots** folder.

**Another option:** press the **Print Screen** key (often labeled **PrtSc**). This copies the whole screen, but it isn't saved as a file until you paste it somewhere, like an email.

---

## tr028-b
- task: Take a screenshot | platform: Windows 11 | scenario: missing_info | sensitive: False
- sources: Microsoft Support: Use Snipping Tool to capture screenshots <https://support.microsoft.com/en-us/windows/apps/use-snipping-tool-to-capture-screenshots>

**USER:**
how do I take a picture of my computer screen

**ASSISTANT:**
Happy to help. Is your computer a **Windows** computer or a **Mac**? If you're not sure, a Windows keyboard usually has a key with the Windows logo near the bottom left.

---

## tr028-c
- task: Take a screenshot | platform: Windows 11 | scenario: direct_messy | sensitive: False
- sources: Microsoft Support: Use Snipping Tool to capture screenshots <https://support.microsoft.com/en-us/windows/apps/use-snipping-tool-to-capture-screenshots>

**USER:**
screenshot on windows

**ASSISTANT:**
Here's how to take a screenshot on Windows 11:

The quickest way uses three keys at once. It takes a few seconds.

1. Press and hold the **Windows logo key** and the **Shift** key, then press **S**.
2. The screen dims and shows a few capture choices.
3. Choose the shape you want: a rectangle, a window, or the full screen.
4. If you chose rectangle, click and drag over the part of the screen you want.

Your screenshot is saved automatically in your **Screenshots** folder.

**Another option:** press the **Print Screen** key (often labeled **PrtSc**). This copies the whole screen, but it isn't saved as a file until you paste it somewhere, like an email.

---

## tr028-d
- task: Take a screenshot | platform: Windows 11 | scenario: followup | sensitive: False
- sources: Microsoft Support: Use Snipping Tool to capture screenshots <https://support.microsoft.com/en-us/windows/apps/use-snipping-tool-to-capture-screenshots>

**USER:**
how do I take a picture of my computer screen

**ASSISTANT:**
Happy to help. Is your computer a **Windows** computer or a **Mac**? If you're not sure, a Windows keyboard usually has a key with the Windows logo near the bottom left.

**USER:**
Windows 11

**ASSISTANT:**
Great, here's the easiest way on Windows 11.

The quickest way uses three keys at once. It takes a few seconds.

1. Press and hold the **Windows logo key** and the **Shift** key, then press **S**.
2. The screen dims and shows a few capture choices.
3. Choose the shape you want: a rectangle, a window, or the full screen.
4. If you chose rectangle, click and drag over the part of the screen you want.

Your screenshot is saved automatically in your **Screenshots** folder.

**Another option:** press the **Print Screen** key (often labeled **PrtSc**). This copies the whole screen, but it isn't saved as a file until you paste it somewhere, like an email.

---

## tr028-e
- task: Take a screenshot | platform: Windows 11 | scenario: constraint | sensitive: False
- sources: Microsoft Support: Use Snipping Tool to capture screenshots <https://support.microsoft.com/en-us/windows/apps/use-snipping-tool-to-capture-screenshots>

**USER:**
I'm on a Windows 11 computer and want to send my doctor's office a picture of just one box on a web page. I don't want the whole screen, because my email inbox is open too and I don't want them to see it. How can I capture only that box?

**ASSISTANT:**
You can use **Snipping Tool** to capture just one part of the screen.

1. Select **Start**, type **snipping tool**, then select **Snipping Tool**.
2. Select **Snipping Mode**, then choose **Rectangle**.
3. Select **New**.
4. Drag a rectangle around the box you want.

The snip saves automatically to your **Screenshots** folder. A faster way next time is to press the **Windows logo key + Shift + S**, which opens the snip overlay.

---

## tr030-a
- task: Connect to a Wi-Fi network | platform: Android | scenario: direct | sensitive: False
- sources: Android Help: Connect to Wi-Fi networks on your Android device <https://support.google.com/android/answer/9075847?hl=en>

**USER:**
How do I connect my Android phone to my Wi-Fi at home?

**ASSISTANT:**
Here's how. Have your Wi-Fi password ready. It takes about two minutes.

1. Open the **Settings** app.
2. Tap **Network & internet**.
3. Tap **Internet**.
4. Tap the name of your home network in the list. A lock icon means it needs a password.
5. If it asks for a password, type it.

When you're connected, the network is labeled **Saved**.

Some of these steps work only on Android 12 and up. Menu names can be a little different on some phones. If you don't see **Network & internet**, tell me what you see in Settings.

---

## tr030-b
- task: Connect to a Wi-Fi network | platform: Android | scenario: missing_info | sensitive: False
- sources: Android Help: Connect to Wi-Fi networks on your Android device <https://support.google.com/android/answer/9075847?hl=en>

**USER:**
how do I get my phone on the wifi

**ASSISTANT:**
I can walk you through it. Is your phone an **iPhone** or an **Android** phone (like Samsung or Google Pixel)?

---

## tr030-c
- task: Connect to a Wi-Fi network | platform: Android | scenario: direct_messy | sensitive: False
- sources: Android Help: Connect to Wi-Fi networks on your Android device <https://support.google.com/android/answer/9075847?hl=en>

**USER:**
I have a Google Pixel 7 with Android 15. My new internet company's router has a sticker on the bottom with the network name HOME-4G7K and a password. How do I connect the phone to it?

**ASSISTANT:**
The sticker on your router has what you need: the network name **HOME-4G7K** and the password.

1. Open the **Settings** app.
2. Tap **Network & internet**.
3. Tap **Internet**.
4. Tap **HOME-4G7K** in the list. A lock icon means it needs a password.
5. If it asks for a password, type the password from the sticker.

When you're connected, the network is labeled **Saved**.

Some of these steps work only on Android 12 and up. Menu names can be a little different on some phones. If you don't see **Network & internet**, tell me what you see in Settings.

---

## tr030-d
- task: Connect to a Wi-Fi network | platform: Android | scenario: followup | sensitive: False
- sources: Android Help: Connect to Wi-Fi networks on your Android device <https://support.google.com/android/answer/9075847?hl=en>

**USER:**
how do I get my phone on the wifi

**ASSISTANT:**
I can walk you through it. Is your phone an **iPhone** or an **Android** phone (like Samsung or Google Pixel)?

**USER:**
Android

**ASSISTANT:**
Thanks. Have your Wi-Fi password ready. It takes about two minutes.

1. Open the **Settings** app.
2. Tap **Network & internet**.
3. Tap **Internet**.
4. Tap the name of your home network in the list. A lock icon means it needs a password.
5. If it asks for a password, type it.

When you're connected, the network is labeled **Saved**.

Some of these steps work only on Android 12 and up. Menu names can be a little different on some phones. If you don't see **Network & internet**, tell me what you see in Settings.

---

## tr030-e
- task: Connect to a Wi-Fi network | platform: Android | scenario: constraint | sensitive: False
- sources: Android Help: Connect to Wi-Fi networks on your Android device <https://support.google.com/android/answer/9075847?hl=en>

**USER:**
My son set up our Wi-Fi at the new apartment and hid the network, so it doesn't show up in the list on my Android phone. He told me the name and password. How do I connect to a network that isn't listed?

**ASSISTANT:**
You can add it yourself.

1. Open the **Settings** app.
2. Tap **Network & internet**, then **Internet**.
3. At the bottom of the list, tap **Add network**.
4. Type the network name your son gave you.
5. Enter the security details your son gave you, including the password.
6. Tap **Advanced options**, and under **Hidden Network** select **Yes**.
7. Tap **Save**.

Once connected, the network is labeled **Saved**, and your phone joins it automatically when you're nearby.

---

## tr031-a
- task: Connect to a Wi-Fi network | platform: Windows 11 | scenario: direct | sensitive: False
- sources: Microsoft Support: Connect to a Wi-Fi network in Windows <https://support.microsoft.com/en-us/windows/experience/connectivity-networking/connect-to-a-wi-fi-network-in-windows>

**USER:**
How do I connect my Windows 11 laptop to Wi-Fi?

**ASSISTANT:**
Here's how. Have your Wi-Fi password ready. This takes about two minutes.

1. On the taskbar at the bottom right of the screen, click the **network, sound, or battery icons**. A small panel opens.
2. Next to the Wi-Fi button, click the **arrow** for **Manage Wi-Fi connections**.
3. Click the name of your network.
4. Click **Connect**.
5. Type your Wi-Fi password.
6. Click **Next**.

When it's done, try opening a website to check that it works.

If you don't see your network in the list, click **Refresh network list** in the lower right of the panel and look again.

---

## tr031-c
- task: Connect to a Wi-Fi network | platform: Windows 11 | scenario: missing_info | sensitive: False
- sources: Microsoft Support: Connect to a Wi-Fi network in Windows <https://support.microsoft.com/en-us/windows/experience/connectivity-networking/connect-to-a-wi-fi-network-in-windows>

**USER:**
laptop wont connect to

**ASSISTANT:**
It looks like your message got cut off. What won't your laptop connect to: the **Wi-Fi**, a **printer**, or something else?

---

## tr031-d
- task: Connect to a Wi-Fi network | platform: Windows 11 | scenario: followup | sensitive: False
- sources: Microsoft Support: Connect to a Wi-Fi network in Windows <https://support.microsoft.com/en-us/windows/experience/connectivity-networking/connect-to-a-wi-fi-network-in-windows>

**USER:**
how do i connect my computer to the internet

**ASSISTANT:**
I can help. Is your computer a **Windows** computer or a **Mac**?

**USER:**
Windows 11

**ASSISTANT:**
Thanks. Have your Wi-Fi password ready. This takes about two minutes.

1. On the taskbar, click the **network, sound, or battery icons**. A small panel opens.
2. Next to the Wi-Fi button, click the **arrow** for **Manage Wi-Fi connections**.
3. Click the name of your network.
4. Click **Connect**.
5. Type your Wi-Fi password and click **Next**.

When it's done, try opening a website to check that it works.

If you don't see your network in the list, click **Refresh network list** in the lower right of the panel and look again.

---

## tr031-e
- task: Connect to a Wi-Fi network | platform: Windows 11 | scenario: constraint | sensitive: False
- sources: Microsoft Support: Connect to a Wi-Fi network in Windows <https://support.microsoft.com/en-us/windows/experience/connectivity-networking/connect-to-a-wi-fi-network-in-windows>

**USER:**
I'm visiting my daughter with my Windows 11 laptop and she hasn't given me her Wi-Fi password yet because she's out. Can I get my laptop connected to her network before she gets home?

**ASSISTANT:**
You can get everything ready, but joining her network needs the password. Without it, you can't finish.

1. Select the **Network**, **Sound**, or **Battery** icons on the taskbar.
2. In the Wi-Fi quick setting, select **Manage Wi-Fi connections**.
3. Choose her network and select **Connect**.
4. When it asks for the password, enter it and select **Next**.

When she gets home, ask her for the password and finish at step 4.

---

## tr031-r
- task: Connect to a Wi-Fi network | platform: Windows 11 | scenario: failure_recovery | sensitive: False
- sources: Microsoft Support: Connect to a Wi-Fi network in Windows <https://support.microsoft.com/en-us/windows/experience/connectivity-networking/connect-to-a-wi-fi-network-in-windows>

**USER:**
I need to connect my Windows 11 laptop to the Wi-Fi in my house. How do I do it?

**ASSISTANT:**
Here is how.

1. Select the **Network**, **Sound**, or **Battery** icons on the taskbar.
2. In the Wi-Fi quick setting, select **Manage Wi-Fi connections**.
3. Choose your network and select **Connect**.
4. Enter the network password and select **Next**.

If you are not connected, the taskbar shows a **Disconnected** icon.

**USER:**
My network isn't showing up in the list.

**ASSISTANT:**
Ask the laptop to look again.

1. Open the Wi-Fi list the same way, with **Manage Wi-Fi connections**.
2. Select the **Refresh network list** button in the lower right.
3. When your network appears, select it and select **Connect**.

---

## tr033-a
- task: Install a software update | platform: Android | scenario: direct | sensitive: False
- sources: Android Help: Check & update your Android version <https://support.google.com/android/answer/7680439?hl=en>

**USER:**
How do I update the software on my Android phone?

**ASSISTANT:**
Here's how to check for an update. Before you start, connect to Wi-Fi and make sure your battery is at least 75% charged, because updates can take a while.

1. Open the **Settings** app.
2. Tap **System**.
3. Tap **Software updates**. The update status appears there. Names can be a little different on some phones.
4. Follow the instructions on the screen to download and install the update.

Your phone may restart during the update. On Google Pixel phones, the update installs in the background and finishes when you restart.

If you get a 'not enough space available' notification, tell me and I'll help you free up some storage first.

---

## tr033-b
- task: Install a software update | platform: Android | scenario: missing_info | sensitive: False
- sources: Android Help: Check & update your Android version <https://support.google.com/android/answer/7680439?hl=en>

**USER:**
my phone says there's an update, should I do it?

**ASSISTANT:**
Updates are usually a good idea because they fix problems and help keep your phone secure. If the message popped up on a website, don't tap it. Real updates come from your phone's Settings.

So I can show you the right steps: is your phone an **iPhone** or an **Android** phone (like Samsung or Google Pixel)?

---

## tr033-d
- task: Install a software update | platform: Android | scenario: followup | sensitive: False
- sources: Android Help: Check & update your Android version <https://support.google.com/android/answer/7680439?hl=en>

**USER:**
my phone says there's an update, should I do it?

**ASSISTANT:**
Updates are usually a good idea because they fix problems and help keep your phone secure. So I can show you the right steps: is your phone an **iPhone** or an **Android** phone (like Samsung or Google Pixel)?

**USER:**
Android

**ASSISTANT:**
Thanks. If you still see the update notification, you can tap it, then tap its update button. Otherwise, before you start, connect to Wi-Fi and charge the battery to at least 75%, because updates can take a while.

1. Open the **Settings** app.
2. Tap **System**.
3. Tap **Software updates**. The update status appears there. Names can be a little different on some phones.
4. Follow the instructions on the screen to download and install the update.

Your phone may restart during the update. On Google Pixel phones, the update installs in the background and finishes when you restart.

If you get a 'not enough space available' notification, tell me and I'll help you free up some storage first.

---

## tr033-e
- task: Install a software update | platform: Android | scenario: constraint | sensitive: False
- sources: Android Help: Check & update your Android version <https://support.google.com/android/answer/7680439?hl=en>

**USER:**
I have a Google Pixel and it says there's an update. I'm waiting on a call from my doctor's office and I don't want my phone restarting on me right now. How do I install it?

**ASSISTANT:**
Good news: on a Pixel, updates download and install in the background, and the update only takes effect the next time you restart. So you can restart after your call.

Before you start, connect to Wi-Fi and make sure your battery is at least 75%.

1. Open the **Settings** app.
2. Tap **System**.
3. Tap **Software updates**. The update status shows here.
4. Follow the instructions on the screen.

When your call is done, restart the phone and the update will take effect.

---

## tr033-r
- task: Install a software update | platform: Android | scenario: failure_recovery | sensitive: False
- sources: Android Help: Check & update your Android version <https://support.google.com/android/answer/7680439?hl=en>

**USER:**
A box popped up on my Samsung Android phone saying a new Android version is ready. How do I install it from that message?

**ASSISTANT:**
You can start it right from that message. Before you start, connect to Wi-Fi and make sure your battery is at least 75%.

1. Open the update notification.
2. Tap the update action on it.
3. Follow the instructions on the screen.

Your phone may restart on its own while the update installs.

**USER:**
I swiped the message away by accident and now it's gone.

**ASSISTANT:**
That's okay. The update is still available in Settings.

1. Open the **Settings** app.
2. Tap **System**, then **Software updates**. The update status appears here.
3. Follow the instructions on the screen.

If nothing shows up, your phone may already be up to date, it may no longer get updates, or it may be waiting for your carrier or phone maker to release the update.

---

## tr034-a
- task: Install Windows updates | platform: Windows 11 | scenario: direct | sensitive: False
- sources: Microsoft Support: Install Windows Updates <https://support.microsoft.com/en-us/windows/deployment/updates-lifecycle/install-windows-updates>

**USER:**
How do I install Windows updates on my Windows 11 computer?

**ASSISTANT:**
Here's how to check for updates and install them. It can take a while, so do it when you won't need the computer for a bit.

1. Click the **Start** button (the Windows logo).
2. Click **Settings**.
3. Click **Windows Update**.
4. Click **Check for Windows updates**.
5. If updates are found, click **Download & install**.

If Windows asks you to restart, save anything you're working on first, then restart to finish the update.

If you see an error message, write it down or take a picture of it, and tell me what it says.

---

## tr034-c
- task: Install Windows updates | platform: Windows 11 | scenario: direct_messy | sensitive: False
- sources: Microsoft Support: Install Windows Updates <https://support.microsoft.com/en-us/windows/deployment/updates-lifecycle/install-windows-updates>

**USER:**
Dell Inspiron, Windows 11 Home. The little icon by the clock says updates are available. I'm comfortable with Settings, just tell me where to go.

**ASSISTANT:**
Sure, here's the path.

1. Click **Start**, then **Settings**.
2. Click **Windows Update**.
3. Click **Check for Windows updates**.
4. If it finds updates, click **Download & install**.

If Windows asks you to restart, do that to finish the update.

---

## tr034-d
- task: Install Windows updates | platform: Windows 11 | scenario: followup | sensitive: False
- sources: Microsoft Support: Install Windows Updates <https://support.microsoft.com/en-us/windows/deployment/updates-lifecycle/install-windows-updates>

**USER:**
my computer keeps saying it needs to update

**ASSISTANT:**
Updates help keep your computer working well and safe. Is your computer a **Windows** computer or a **Mac**?

**USER:**
Windows 11

**ASSISTANT:**
Thanks. Here's how to check for updates and install them. It can take a while, so do it when you won't need the computer for a bit.

1. Click the **Start** button (the Windows logo).
2. Click **Settings**.
3. Click **Windows Update**.
4. Click **Check for Windows updates**.
5. If updates are found, click **Download & install**.

If Windows asks you to restart, save anything you're working on first, then restart to finish the update.

If you see an error message, write it down or take a picture of it, and tell me what it says.

---

## tr034-e
- task: Install Windows updates | platform: Windows 11 | scenario: constraint | sensitive: False
- sources: Microsoft Support: Install Windows Updates <https://support.microsoft.com/en-us/windows/deployment/updates-lifecycle/install-windows-updates>

**USER:**
I'm on my Windows 11 laptop and in the middle of a big project, so I don't want to install anything just yet. I only want to see whether any updates are waiting for me.

**ASSISTANT:**
You can look without installing anything.

1. Click the **Start** button.
2. Click **Settings**.
3. Click **Windows Update**.
4. Click **Check for Windows updates**.

If updates are available, you don't have to do anything more right now. The **Download & install** button is the one that starts the installing, so you can leave it alone until you're ready.

When you do install them, Windows may ask you to restart to finish. Save your work first.

---

## tr034-r
- task: Install Windows updates | platform: Windows 11 | scenario: failure_recovery | sensitive: False
- sources: Microsoft Support: Install Windows Updates <https://support.microsoft.com/en-us/windows/deployment/updates-lifecycle/install-windows-updates>; Microsoft Support: Troubleshoot problems updating Windows <https://support.microsoft.com/en-us/windows/troubleshoot-problems-updating-windows-188c2b0f-10a7-d72f-65b8-32d177eb136c>

**USER:**
Can you walk me through updating my Windows 11 PC? I've never done it before.

**ASSISTANT:**
Sure, it only takes a few clicks.

1. Click **Start**, then **Settings**.
2. Click **Windows Update**.
3. Click **Check for Windows updates**.
4. If updates are available, click **Download & install**.
5. If Windows asks you to restart, restart to finish the update.

Save your work before restarting.

**USER:**
I clicked Check for Windows updates but it just shows an error.

**ASSISTANT:**
Let's try Windows' built-in fixer.

1. Click **Start**, then **Settings**, then **System**, then **Troubleshoot**, then **Other troubleshooters**.
2. Click **Run** next to **Windows Update**.
3. Make sure you're online: go to **Start**, **Settings**, **Network & Internet**, **Wi-Fi**, and reconnect if needed.
4. Go back to **Settings**, **Windows Update**, and click **Check for Windows updates** again.

If you still get an error, write down the error code and tell me what it says.

---

## tr035-a
- task: Back up photos | platform: Android (Google Photos) | scenario: direct | sensitive: False
- sources: Google Photos Help: Back up photos & videos (Android) <https://support.google.com/photos/answer/6193313?hl=en&co=GENIE.Platform%3DAndroid>

**USER:**
How do I back up my photos on my Android phone so I don't lose them?

**ASSISTANT:**
You can use the **Google Photos** app to save copies of your photos to your Google Account. Make sure you have a good internet connection first.

1. Open the **Google Photos** app.
2. Sign in to your Google Account if it asks.
3. Tap your **profile picture or initial** at the top right.
4. Tap **Photos settings**.
5. Tap **Backup**.
6. Turn **Backup** on.

Your photos will start saving to your Google Account. At the top of your library you should see the backup status, such as **Backing up photos** and later **Backup complete**. This can take a while if you have many photos.

Your Google storage is shared with Gmail and Google Drive, and backup stops if it fills up. Tell me if you see a storage message and we'll look at the options.

---

## tr035-b
- task: Back up photos | platform: Android (Google Photos) | scenario: missing_info | sensitive: False
- sources: Google Photos Help: Back up photos & videos (Android) <https://support.google.com/photos/answer/6193313?hl=en&co=GENIE.Platform%3DAndroid>

**USER:**
how can I save my pictures so I don't lose them if I lose my phone

**ASSISTANT:**
That's a smart thing to set up. Is your phone an **iPhone** or an **Android** phone (like Samsung or Google Pixel)?

---

## tr035-c
- task: Back up photos | platform: Android (Google Photos) | scenario: direct_messy | sensitive: False
- sources: Google Photos Help: Back up photos & videos (Android) <https://support.google.com/photos/answer/6193313?hl=en&co=GENIE.Platform%3DAndroid>

**USER:**
I dropped my old phone in the lake last summer and lost all the pictures of my granddaughter's first year. I have a new Android phone now and I don't want that to happen again.

**ASSISTANT:**
I'm sorry about those pictures. Let's make sure your new ones are kept safe. You can use the **Google Photos** app to save copies of your photos to your Google Account. Make sure you have a good internet connection first.

1. Open the **Google Photos** app.
2. Sign in to your Google Account if it asks.
3. Tap your **profile picture or initial** at the top right.
4. Tap **Photos settings**.
5. Tap **Backup**.
6. Turn **Backup** on.

Your photos will start saving to your Google Account. At the top of your library you should see the backup status, such as **Backing up photos** and later **Backup complete**. This can take a while if you have many photos.

Your Google storage is shared with Gmail and Google Drive, and backup stops if it fills up. Tell me if you see a storage message and we'll look at the options.

---

## tr035-d
- task: Back up photos | platform: Android (Google Photos) | scenario: followup | sensitive: False
- sources: Google Photos Help: Back up photos & videos (Android) <https://support.google.com/photos/answer/6193313?hl=en&co=GENIE.Platform%3DAndroid>

**USER:**
how can I save my pictures so I don't lose them if I lose my phone

**ASSISTANT:**
That's a smart thing to set up. Is your phone an **iPhone** or an **Android** phone (like Samsung or Google Pixel)?

**USER:**
android

**ASSISTANT:**
Great. On Android you can use the **Google Photos** app to save copies of your photos to your Google Account. Make sure you have a good internet connection first.

1. Open the **Google Photos** app.
2. Sign in to your Google Account if it asks.
3. Tap your **profile picture or initial** at the top right.
4. Tap **Photos settings**.
5. Tap **Backup**.
6. Turn **Backup** on.

Your photos will start saving to your Google Account. At the top of your library you should see the backup status, such as **Backing up photos** and later **Backup complete**. This can take a while if you have many photos.

Your Google storage is shared with Gmail and Google Drive, and backup stops if it fills up. Tell me if you see a storage message and we'll look at the options.

---

## tr035-r
- task: Back up photos | platform: Android (Google Photos) | scenario: failure_recovery | sensitive: False
- sources: Google Photos Help: Back up photos & videos (Android) <https://support.google.com/photos/answer/6193313?hl=en&co=GENIE.Platform%3DAndroid>

**USER:**
My daughter says I should use Google Photos to keep my pictures safe. I have a Pixel phone. What do I do?

**ASSISTANT:**
Google Photos can save copies of your pictures to your Google Account.

1. Open the **Google Photos** app.
2. Tap your **profile picture or initial** at the top right.
3. Tap **Photos settings**, then **Backup**.
4. Turn **Backup** on.

Your pictures start saving to your account. With many photos it can take a while.

**USER:**
I did that yesterday, but now the top of the app says Backup paused and nothing seems to be uploading.

**ASSISTANT:**
Let's check two common causes.

1. Tap the status at the top of the app to see details. Backup works only if your Google storage has room. If you're out of space, tap **buy more storage** or **clean up your storage space**.
2. Your phone's battery saver can interfere. Open **Settings** and search for **battery optimization**. Tap **Battery optimization**, then **All apps**. Tap **Photos**, choose **Don't optimize**, and tap **Done**.

After that, open Google Photos again and check the status at the top.

---

## tr036-a
- task: Add a printer | platform: Windows 11 | scenario: direct | sensitive: False
- sources: Microsoft Support: Add or install a printer in Windows <https://support.microsoft.com/en-us/windows/hardware/printer/add-or-install-a-printer-in-windows>

**USER:**
I just bought a new printer. How do I add it to my Windows 11 computer?

**ASSISTANT:**
Here's how to add your new printer. It can take a few minutes.

**First:** turn the printer on. If it uses a cable, plug it into the computer. Some printers, especially ones with a cable, install by themselves once they are plugged in and on. If it's wireless, make sure it's on the same Wi-Fi network as your computer.

1. Click **Start**, then **Settings**.
2. Click **Bluetooth & devices**.
3. Click **Printers & scanners**.
4. Look at the list of printers. If your printer is already there, you're finished.
5. If it isn't, click **Add a printer & scanner**, then click **Add device**.
6. Wait a few minutes while the computer searches.
7. When your printer appears, click **Add device** next to it.

If your printer doesn't show up, look for **The printer that I want isn't listed**, choose **Add a new device manually**, and follow the instructions.

---

## tr036-b
- task: Add a printer | platform: Windows 11 | scenario: missing_info | sensitive: False
- sources: Microsoft Support: Add or install a printer in Windows <https://support.microsoft.com/en-us/windows/hardware/printer/add-or-install-a-printer-in-windows>

**USER:**
how do I set up my new printer

**ASSISTANT:**
Congratulations on the new printer. What will you print from: a **Windows computer**, a **Mac**, or a **phone**?

---

## tr036-d
- task: Add a printer | platform: Windows 11 | scenario: followup | sensitive: False
- sources: Microsoft Support: Add or install a printer in Windows <https://support.microsoft.com/en-us/windows/hardware/printer/add-or-install-a-printer-in-windows>

**USER:**
how do I set up my new printer

**ASSISTANT:**
Congratulations on the new printer. What will you print from: a **Windows computer**, a **Mac**, or a **phone**?

**USER:**
My Windows 11 laptop

**ASSISTANT:**
Great, here's how to add the printer to your Windows 11 laptop. It can take a few minutes.

**First:** turn the printer on. If it uses a cable, plug it into the computer. Some printers, especially ones with a cable, install by themselves once they are plugged in and on. If it's wireless, make sure it's on the same Wi-Fi network as your computer.

1. Click **Start**, then **Settings**.
2. Click **Bluetooth & devices**.
3. Click **Printers & scanners**.
4. Look at the list of printers. If your printer is already there, you're finished.
5. If it isn't, click **Add a printer & scanner**, then click **Add device**.
6. Wait a few minutes while the computer searches.
7. When your printer appears, click **Add device** next to it.

If your printer doesn't show up, look for **The printer that I want isn't listed**, choose **Add a new device manually**, and follow the instructions.

---

## tr036-e
- task: Add a printer | platform: Windows 11 | scenario: constraint | sensitive: False
- sources: Microsoft Support: Add or install a printer in Windows <https://support.microsoft.com/en-us/windows/hardware/printer/add-or-install-a-printer-in-windows>

**USER:**
I have a Windows 11 PC and a new wireless printer. I don't have a USB cable and I don't want to go buy one. Can I still get them working together?

**ASSISTANT:**
Yes, a wireless printer doesn't need a cable. First, turn the printer on and make sure it's on the same wireless network as your computer.

1. Click **Start**, then **Settings**.
2. Click **Bluetooth & devices**, then **Printers & scanners**.
3. Next to **Add a printer & scanner**, click **Add device**.
4. Wait a few minutes while the list fills up.
5. When your printer appears, click **Add device** next to it.

Some printers install by themselves after step 3.

---

## tr036-r
- task: Add a printer | platform: Windows 11 | scenario: failure_recovery | sensitive: False
- sources: Microsoft Support: Add or install a printer in Windows <https://support.microsoft.com/en-us/windows/hardware/printer/add-or-install-a-printer-in-windows>

**USER:**
I plugged my printer into my Windows 11 computer with the USB cable and turned it on. Now what?

**ASSISTANT:**
Windows usually installs the printer by itself. Let's check.

1. Click **Start**, then **Settings**.
2. Click **Bluetooth & devices**, then **Printers & scanners**.
3. Look for your printer in the list. If it's there, you're done.
4. If it's not, next to **Add a printer & scanner**, click **Add device**.
5. Wait a few minutes while the list fills up, then click **Add device** next to your printer.

**USER:**
I waited several minutes and my printer never showed up in the list.

**ASSISTANT:**
Let's try adding it by hand.

1. Check that the printer is turned on and plugged in to the computer.
2. On the same screen, find **The printer that I want isn't listed** and click **Add a new device manually** next to it.
3. Follow the instructions in the **Add Printer** window that opens.

---

## tr037-a
- task: Attach a photo to an email | platform: Gmail app (phone) | scenario: direct | sensitive: False
- sources: Gmail Help: Send attachments with your Gmail message (Android) <https://support.google.com/mail/answer/6584?hl=en&co=GENIE.Platform%3DAndroid>

**USER:**
How do I attach a photo to an email in the Gmail app on my Android phone?

**ASSISTANT:**
Here's how. It takes about a minute.

1. Open the **Gmail** app.
2. Tap **Compose** at the bottom right to start a new email.
3. Tap the **Attach** icon at the top right. It looks like a **paperclip**.
4. Choose where the photo is, such as **Photos**.
5. Tap the photo you want. You can pick up to five photos at once.

Then add the email address and your message as usual, and send it.

If you added the wrong photo, tap the close icon (**X**) next to its name to remove it. Files over 25 MB are added as a Google Drive link instead.

---

## tr037-c
- task: Attach a photo to an email | platform: Gmail app (phone) | scenario: missing_info | sensitive: False
- sources: Gmail Help: Send attachments with your Gmail message (Android) <https://support.google.com/mail/answer/6584?hl=en&co=GENIE.Platform%3DAndroid>

**USER:**
how to attach

**ASSISTANT:**
Happy to help. **Where do you want to attach something**: in an email, in a text message, or somewhere else?

---

## tr037-d
- task: Attach a photo to an email | platform: Gmail app (phone) | scenario: followup | sensitive: False
- sources: Gmail Help: Send attachments with your Gmail message (Android) <https://support.google.com/mail/answer/6584?hl=en&co=GENIE.Platform%3DAndroid>

**USER:**
how do I send a picture in an email

**ASSISTANT:**
I can help. Which email app are you using, for example **Gmail** on your phone?

**USER:**
Gmail app on my Android phone

**ASSISTANT:**
Thanks, here's how in the Gmail app. It takes about a minute.

1. Open the **Gmail** app.
2. Tap **Compose** at the bottom right to start a new email.
3. Tap the **Attach** icon at the top right.
4. Choose where the photo is, such as **Photos**.
5. Tap the photo you want. You can pick up to five photos at once.

Then add the email address and your message as usual, and send it.

If you added the wrong photo, tap **Close** to the right of its name to remove it. If the attachments are over 25 MB on a personal Gmail account, Gmail adds them as a Google Drive link instead. Work and school accounts can have a different limit set by their administrator.

---

## tr037-e
- task: Attach a photo to an email | platform: Gmail app (phone) | scenario: constraint | sensitive: False
- sources: Gmail Help: Send attachments with your Gmail message (Android) <https://support.google.com/mail/answer/6584?hl=en&co=GENIE.Platform%3DAndroid>

**USER:**
I have three photos from the picnic on my Android phone and I'd like all of them in one email in the Gmail app, not three separate emails.

**ASSISTANT:**
You can put them all in one email.

1. Open the **Gmail** app.
2. Tap **Compose** at the bottom right.
3. Tap **Attach** at the top right.
4. Choose **Photos**.
5. Tap each photo you want. You can select up to five at a time, so all three fit.

Then add the email address and your message, and send it.

If the photos are very large (over 25 MB together on a regular Gmail account), Gmail adds them as a Google Drive link instead.

---

## tr037-r
- task: Attach a photo to an email | platform: Gmail app (phone) | scenario: failure_recovery | sensitive: False
- sources: Gmail Help: Send attachments with your Gmail message (Android) <https://support.google.com/mail/answer/6584?hl=en&co=GENIE.Platform%3DAndroid>

**USER:**
Please show me how to put a picture into an email with the Gmail app on my Android phone. It's for my nephew's birthday.

**ASSISTANT:**
Here's how.

1. Open the **Gmail** app.
2. Tap **Compose** at the bottom right.
3. Tap **Attach** at the top right.
4. Choose **Photos**.
5. Tap the picture you want.

Then add your nephew's email address and your message, and send it.

**USER:**
I tapped send and it says Couldn't send message.

**ASSISTANT:**
That message can appear when a picture didn't finish uploading, often because of slow internet or low space. Try this:

1. Tap **Close** on the right side of the picture's name to remove it.
2. Tap **Attach**, choose **Photos**, and pick the picture again.
3. Send the email again.

If it keeps happening, your Google storage may be full. Attachments count toward it, so deleting large attachments and emptying your trash and spam can free space.

---

## tr038-a
- task: Reset forgotten Google Account password | platform: Google Account | scenario: direct | sensitive: True
- sources: Google Account Help: How to recover your Google Account or Gmail <https://support.google.com/accounts/answer/7682439?hl=en>

**USER:**
I forgot my Gmail password and can't sign in. How do I get back into my account?

**ASSISTANT:**
You can get back in through Google's account recovery. It usually takes a few minutes.

1. Go to **accounts.google.com/signin/recovery** (Google's account recovery page).
2. Answer the questions it asks to show the account is yours. Answer as accurately as you can, and if you're not sure, make your best guess. A wrong guess doesn't end the process, and you can try again.
3. When asked, create a **new password** that you haven't used for this account before.

**Stay safe while you do this:**
- Google staff can't help you sign in over the phone, so ignore anyone who calls or messages offering to recover your account.
- Never share your password or any verification code with anyone.

If you recently changed your recovery info, it can take up to 7 days to take effect, so try again after a few days.

---

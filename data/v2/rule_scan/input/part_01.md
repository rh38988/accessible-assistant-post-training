# Rule scan input, part 01 (50 examples)

## pilot-001
- task: Make text bigger | platform: Samsung Galaxy | scenario: direct | sensitive: False
- sources: Samsung Support: How to adjust the font size and style on your Galaxy phone <https://www.samsung.com/latin_en/support/mobile-devices/how-to-adjust-the-font-size-and-style-on-your-galaxy-phone/>

**USER:**
the letters on my samsung phone are so tiny i cant read my messages. how do i make them bigger

**ASSISTANT:**
You can make the letters bigger in your phone's settings. It takes about a minute, and you can change it back anytime.

1. Find the **Settings** app and tap it.
2. Tap **Display**.
3. Tap **Font size and style**.
4. Adjust the options on that screen until the letters are easy to read.

Menu names can be a little different on some Samsung models. If you don't see **Font size and style** after tapping **Display**, tell me what you see and I'll help you find it.

---

## tr001-b
- task: Make text bigger | platform: Samsung Galaxy | scenario: missing_info | sensitive: False
- sources: Samsung Support: How to adjust the font size and style on your Galaxy phone <https://www.samsung.com/latin_en/support/mobile-devices/how-to-adjust-the-font-size-and-style-on-your-galaxy-phone/>

**USER:**
everything on my phone is written so small now, is there a way to make it bigger

**ASSISTANT:**
I can help with that. Is your phone an **iPhone**, a **Samsung Galaxy**, or another kind of phone?

---

## tr001-d
- task: Make text bigger | platform: Samsung Galaxy | scenario: followup | sensitive: False
- sources: Samsung Support: How to adjust the font size and style on your Galaxy phone <https://www.samsung.com/latin_en/support/mobile-devices/how-to-adjust-the-font-size-and-style-on-your-galaxy-phone/>

**USER:**
everything on my phone is written so small now, is there a way to make it bigger

**ASSISTANT:**
I can help with that. Is your phone an **iPhone**, a **Samsung Galaxy**, or another kind of phone?

**USER:**
its a samsung galaxy

**ASSISTANT:**
Good, here is how to make the writing bigger on a Samsung Galaxy.

1. Open the **Settings** app.
2. Tap **Display**.
3. Tap **Font size and style**.
4. On that screen, adjust the options to make the font bigger. You can also make it bold.

If you don't see **Font size and style**, the menus can be a little different on some models. Tell me what you see after tapping **Display** and I'll help.

---

## tr001-e
- task: Make text bigger | platform: Samsung Galaxy | scenario: constraint | sensitive: False
- sources: Samsung Support: How to adjust the font size and style on your Galaxy phone <https://www.samsung.com/latin_en/support/mobile-devices/how-to-adjust-the-font-size-and-style-on-your-galaxy-phone/>

**USER:**
I have a Samsung Galaxy and the print is too small for me. My grandson told me I could download special fonts but I do not want to download anything or pay for anything, I just want the same letters to look bigger. What do I do?

**ASSISTANT:**
You don't need to download anything. The size can be changed right in your settings, and it's free.

1. Open the **Settings** app.
2. Tap **Display**.
3. Tap **Font size and style**.
4. On that screen, adjust the options to make the font bigger. Leave **Font style** alone, because that is the part that downloads new fonts.

Your letters will keep the same look, just bigger.

---

## tr001-r
- task: Make text bigger | platform: Samsung Galaxy | scenario: failure_recovery | sensitive: False
- sources: Samsung Support: How to adjust the font size and style on your Galaxy phone <https://www.samsung.com/latin_en/support/mobile-devices/how-to-adjust-the-font-size-and-style-on-your-galaxy-phone/>

**USER:**
How do I make the writing bigger on my Samsung Galaxy phone?

**ASSISTANT:**
Here is how to make the writing bigger on your Samsung Galaxy.

1. Open the **Settings** app.
2. Tap **Display**.
3. Tap **Font size and style**.
4. On that screen, adjust the options to make the font bigger. You can also make it bold.

The menus can look a little different depending on your phone model and software version.

**USER:**
I tapped Display but I do not see anything called Font size and style.

**ASSISTANT:**
That can happen, because the menus can look different depending on the phone model and software version. Samsung Support can help you directly. You can use Live Chat or Email, or use Find a Support Center to visit someone in person.

---

## pilot-002
- task: Turn up ring volume (device unknown) | platform: unknown | scenario: missing_info | sensitive: False
- sources: Android Help: Change volume, sound & vibrate settings <https://support.google.com/android/answer/9082609?hl=en>

**USER:**
My phone hardly makes any sound when someone calls and I keep missing calls from my doctor's office.

**ASSISTANT:**
I'm sorry you've been missing those calls. I can help make the ringing louder.

Is your phone an **iPhone**, or another kind, like a Samsung or Google Pixel?

If you're not sure, tell me the name on the phone or box.

---

## tr002-a
- task: Turn up ring volume (device unknown) | platform: unknown | scenario: direct | sensitive: False
- sources: Android Help: Change volume, sound & vibrate settings <https://support.google.com/android/answer/9082609?hl=en>

**USER:**
I have a Google Pixel phone and I can't hear it ring from the other room. How do I make the ringer louder?

**ASSISTANT:**
You can turn the ringer up with the buttons on the side of your phone.

1. Press one of the **volume buttons** on the side of your phone.
2. A small volume bar appears on the screen. Tap the **Menu** icon at the right.
3. Find **Ring Volume** and slide it up to make the ring louder.

If you don't see a **Menu** icon, your phone has older software. Tap the **Down arrow** at the right instead, then slide **Ring**.

If your phone was set to vibrate or mute, tap the **Ring** icon above the slider, then turn off **Vibrate** or turn on **Ring** to bring the sound back.

---

## tr002-c
- task: Turn up ring volume (device unknown) | platform: unknown | scenario: direct_messy | sensitive: False
- sources: Android Help: Change volume, sound & vibrate settings <https://support.google.com/android/answer/9082609?hl=en>

**USER:**
My phone is an older Android phone, the kind with the Google system, I think it is about six years old because my son bought it for me when I retired. The Menu thing at the side that people talk about does not show up on mine. I keep missing calls from the pharmacy when the phone is in my purse. How can I turn the ringing up?

**ASSISTANT:**
Older Android phones do this in a slightly different way. Here is how to turn the ringing up.

1. Press one of the **volume buttons** on the side of your phone.
2. Tap the **Down arrow** at the right of the volume bar.
3. Find the **Ring** slider and slide it up to make calls ring louder.

If you would rather use the Settings app, you can also open **Settings** and tap **Sound**.

---

## tr002-e
- task: Turn up ring volume (device unknown) | platform: unknown | scenario: constraint | sensitive: False
- sources: Android Help: Change volume, sound & vibrate settings <https://support.google.com/android/answer/9082609?hl=en>

**USER:**
I have an Android phone, a Google Pixel. I get lost whenever I go into the Settings app, so please do not send me there. Is there any way to make the ring louder using just the buttons on the side of the phone?

**ASSISTANT:**
Yes, you can do it without opening the Settings app.

1. Press one of the **volume buttons** on the side of your phone.
2. Tap the **Menu** icon at the right of the volume bar.
3. Find **Ring Volume** and slide it up to make the ring louder.

If you don't see a **Menu** icon, your phone may be an older version. Tell me and I'll give you the steps for that.

---

## tr002-r
- task: Turn up ring volume (device unknown) | platform: unknown | scenario: failure_recovery | sensitive: False
- sources: Android Help: Change volume, sound & vibrate settings <https://support.google.com/android/answer/9082609?hl=en>

**USER:**
My Android phone's ring is too quiet. How do I make it louder?

**ASSISTANT:**
You can turn the ring up with the buttons on the side of your phone.

1. Press one of the **volume buttons** on the side of your phone.
2. Tap the **Menu** icon at the right of the volume bar.
3. Find **Ring Volume** and slide it up.

If you don't see the **Menu** icon, your phone may be an older version, and I can give you different steps.

**USER:**
I pressed the button and a little bar came up but I do not see any Menu icon, just a little arrow.

**ASSISTANT:**
That means your phone is an older version. Try these steps.

1. Press one of the **volume buttons** on the side again.
2. Tap the **Down arrow** at the right of the bar.
3. Find the **Ring** slider and slide it up to make calls ring louder.

---

## pilot-003
- task: Send a photo by text message | platform: Android (Google Messages) | scenario: direct | sensitive: False
- sources: Google Messages Help: Send photos, videos, or voice messages <https://support.google.com/messages/answer/6159880?hl=en>

**USER:**
I have an Android phone and use the Messages app. How do I text a picture of my garden to my sister?

**ASSISTANT:**
Here's how to send a picture in the Messages app. It takes less than a minute.

1. Open the **Messages** app.
2. Tap your conversation with your sister. If you haven't texted her before, start a new conversation with her.
3. Tap **Gallery**.
4. Tap the picture of your garden.
5. Tap **Send**.

If you don't see **Gallery**, tell me what you see on the screen and I'll guide you from there.

---

## tr003-b
- task: Send a photo by text message | platform: Android (Google Messages) | scenario: missing_info | sensitive: False
- sources: Google Messages Help: Send photos, videos, or voice messages <https://support.google.com/messages/answer/6159880?hl=en>

**USER:**
my daughter wants me to text her the picture of the baby. how do i do that

**ASSISTANT:**
I'd be glad to help you send it. Is your phone an **iPhone** or an **Android** phone?

---

## tr003-c
- task: Send a photo by text message | platform: Android (Google Messages) | scenario: direct_messy | sensitive: False
- sources: Google Messages Help: Send photos, videos, or voice messages <https://support.google.com/messages/answer/6159880?hl=en>

**USER:**
My grandson just graduated and my neighbor took a lovely picture of the two of us in front of the stage. She put it on my phone and now I want to text it to my son who lives in Denver. I have a Samsung phone and I use the Google Messages app for all my texting. My son says I just never send pictures, so I want to learn. What do I press?

**ASSISTANT:**
Congratulations to your grandson. Here is how to text that picture from the Messages app.

1. Open the **Messages** app.
2. Open your conversation with your son. If you haven't texted him before, start a new conversation with him.
3. Tap **Gallery**.
4. Tap the picture of you and your grandson.
5. Look at the preview of the picture. You can leave the quality as it is.
6. Tap **Send**.

You will see the picture in your conversation once it has gone through.

---

## tr003-d
- task: Send a photo by text message | platform: Android (Google Messages) | scenario: followup | sensitive: False
- sources: Google Messages Help: Send photos, videos, or voice messages <https://support.google.com/messages/answer/6159880?hl=en>

**USER:**
my daughter wants me to text her the picture of the baby. how do i do that

**ASSISTANT:**
I'd be glad to help you send it. Is your phone an **iPhone** or an **Android** phone?

**USER:**
android, and i use the messages app

**ASSISTANT:**
Good, here is how to send the picture in the Messages app.

1. Open the **Messages** app.
2. Open your conversation with your daughter. If you haven't texted her before, start a new conversation with her.
3. Tap **Gallery**.
4. Tap the picture of the baby.
5. Tap **Send**.

The picture will show up in your conversation once it is sent.

---

## tr003-e
- task: Send a photo by text message | platform: Android (Google Messages) | scenario: constraint | sensitive: False
- sources: Google Messages Help: Send photos, videos, or voice messages <https://support.google.com/messages/answer/6159880?hl=en>

**USER:**
I want to text a picture of my tomato plants to my brother using the Messages app on my Android phone. I am away from home and my data is nearly used up for the month, so I do not want it to use more data than it has to. Can I still send it?

**ASSISTANT:**
Yes. Messages has a quality choice that sends faster and uses less data.

1. Open the **Messages** app.
2. Open your conversation with your brother.
3. Tap **Gallery**.
4. Tap the picture of your tomato plants.
5. On the preview, tap **HD+** or **HD** to change the quality. Choose **HD**, which says "Optimized for chat". It sends faster and uses less data.
6. Tap **Send**.

Your phone remembers the choice for your next pictures, and you can change it again for any new picture.

---

## tr003-r
- task: Send a photo by text message | platform: Android (Google Messages) | scenario: failure_recovery | sensitive: False
- sources: Google Messages Help: Send photos, videos, or voice messages <https://support.google.com/messages/answer/6159880?hl=en>

**USER:**
I use the Messages app on my Android phone. How do I text a photo of my new puppy to my friend Carol?

**ASSISTANT:**
Here is how to send the photo in the Messages app.

1. Open the **Messages** app.
2. Open your conversation with Carol. If you haven't texted her before, start a new conversation with her.
3. Tap **Gallery**.
4. Tap the photo of your puppy.
5. Tap **Send**.

You'll see the photo in your conversation once it's sent.

**USER:**
It went through but Carol says the picture looks blurry. Can I send it better?

**ASSISTANT:**
Yes. Messages can send the picture in its full original quality. Send it again like this.

1. Open your conversation with Carol.
2. Tap **Gallery**.
3. Tap the photo of your puppy.
4. On the preview, tap **HD** and choose **HD+**, which says "Original quality".
5. Tap **Send**.

Pictures sent as old-style picture messages (called MMS) get squeezed by phone companies, which makes them blurrier. Messages that go through as RCS chats come out clearer.

---

## pilot-004
- task: Take a screenshot | platform: iPhone | scenario: missing_info | sensitive: False
- sources: Apple Support: Take a screenshot on your iPhone <https://support.apple.com/102616>

**USER:**
How do I take a picture of what's on my iPhone screen? My grandson wants me to send him a screenshot.

**ASSISTANT:**
Happy to help. The buttons you press depend on your iPhone model, so one quick question first:

Do you know which iPhone model you have, for example **iPhone 8** or **iPhone 13**?

---

## tr004-a
- task: Take a screenshot | platform: iPhone | scenario: direct | sensitive: False
- sources: Apple Support: Take a screenshot on your iPhone <https://support.apple.com/102616>

**USER:**
My iPhone has no home button, you just look at it to unlock it. How do I take a screenshot of my boarding pass?

**ASSISTANT:**
On your iPhone you take a screenshot with two buttons on the sides.

1. Open the screen you want to capture, such as your boarding pass.
2. Press the **side button** and the **volume up button** at the same time.
3. Let go of both buttons quickly.

On iOS 18 or earlier, a small picture of your screenshot appears in the lower-left corner for a moment. On iOS 26, the screenshot appears right away with tools you can use.

You can find it later in **Photos**. Tap **Collections**, then **Media Types**, then **Screenshots**.

---

## tr004-c
- task: Take a screenshot | platform: iPhone | scenario: direct_messy | sensitive: False
- sources: Apple Support: Take a screenshot on your iPhone <https://support.apple.com/102616>

**USER:**
Hi there, I have an old iPhone that my husband had before he passed, it has a round button at the bottom of the screen and a button on the very top edge, there is nothing on the right side. I want to save a recipe from a website to show my sister. Someone said a screenshot does that. How do I take one on this phone?

**ASSISTANT:**
A screenshot is a good way to keep that recipe. On your iPhone you use the button on the top edge and the round button together.

1. Open the website so the recipe is on the screen.
2. Press the **top button** and the **Home button** (the round button) at the same time.
3. Let go of both buttons quickly.

Your recipe is now saved as a picture. You can find it in **Photos**. Tap **Collections**, then **Media Types**, then **Screenshots**.

---

## tr004-e
- task: Take a screenshot | platform: iPhone | scenario: constraint | sensitive: False
- sources: Apple Support: Take a screenshot on your iPhone <https://support.apple.com/102616>

**USER:**
I have an iPhone with Face ID, no home button. I want a screenshot of a text message but my hands shake and arthritis makes it hard to press two buttons at once. Is there a way to take a screenshot with just one button?

**ASSISTANT:**
I'm sorry, the only way I can give you is the two-button way. I don't have a one-button way to take a screenshot. Here it is, in case you want to try it.

1. Open the text message you want to capture.
2. Press the **side button** and the **volume up button** at the same time.
3. Let go of both quickly.

It is a short press, not a long hold. You do not need to keep the buttons down.

---

## tr004-r
- task: Take a screenshot | platform: iPhone | scenario: failure_recovery | sensitive: False
- sources: Apple Support: Take a screenshot on your iPhone <https://support.apple.com/102616>

**USER:**
I have a newer iPhone with Face ID. How do I take a screenshot?

**ASSISTANT:**
Here is how to take a screenshot on your iPhone.

1. Open the screen you want to capture.
2. Press the **side button** and the **volume up button** at the same time.
3. Let go of both buttons quickly.

You can find your screenshots later in **Photos**. Tap **Collections**, then **Media Types**, then **Screenshots**.

**USER:**
i pressed them but i didnt see a little picture in the corner like my friend said

**ASSISTANT:**
That is likely fine. Here is how to check.

1. Look in the lower-left corner right after you press. On iOS 18 or earlier, the little picture only shows for a moment. On iOS 26, there is no little picture. The screenshot appears right away with tools like drawing and cropping.
2. Open **Photos**, tap **Collections**, then **Media Types**, then **Screenshots**. Your screenshot should be there.
3. If it is not there, try again. Press the **side button** and the **volume up button** together, and let go quickly.

---

## pilot-005
- task: Email stopped working (details unknown) | platform: unknown | scenario: missing_info | sensitive: False
- sources: Gmail Help: Gmail won't load <https://support.google.com/mail/answer/7074871?hl=en>

**USER:**
Good morning. I hope you can help me. My husband always took care of these things. Since about Tuesday my email is not working right. I used to get messages from my church group every day and now nothing. I tried turning it off and on.

**ASSISTANT:**
Good morning. I'm glad you asked, and we can figure this out together. Turning it off and on was a good first try.

So I can give you the right steps: **what is at the end of your email address**, for example @gmail.com or @yahoo.com?

---

## tr005-c
- task: Email stopped working (details unknown) | platform: unknown | scenario: direct_messy | sensitive: False
- sources: Gmail Help: Gmail won't load <https://support.google.com/mail/answer/7074871?hl=en>

**USER:**
My nephew put a bunch of add-ons into my web browser last summer, some coupon thing and a shopping helper and I don't know what else. Ever since then, when I go to Gmail on my desktop computer, the page just sits there and never opens. My internet is fine because I can read the news. I don't want to call him again. What could be causing it and how do I fix it?

**ASSISTANT:**
Those add-ons (called extensions) could be the cause. You can check them one at a time.

1. Turn off one extension in your browser.
2. Open Gmail again and see if it loads.
3. If it still does not load, turn off the next extension and open Gmail again. Repeat until Gmail loads.

You can also try a private browsing window, if your browser has one (it may be called incognito), and open Gmail there.

If you turn off an extension and Gmail loads, that extension was the cause.

---

## tr005-e
- task: Email stopped working (details unknown) | platform: unknown | scenario: constraint | sensitive: False
- sources: Gmail Help: Gmail won't load <https://support.google.com/mail/answer/7074871?hl=en>

**USER:**
Gmail will not open on my laptop in my web browser. The last time I deleted a program, the whole computer went wrong, so please do not tell me to uninstall anything or take any programs off. I only want to try the gentle things. Which ones are those?

**ASSISTANT:**
Here are gentle things to try. None of them remove any programs.

1. Update your browser to the latest version, then open Gmail again.
2. Try a different browser and open Gmail there.
3. Restart your laptop and open Gmail again.
4. Turn your Wi-Fi off, then back on, and open Gmail again.

If your browser has a private window (it may be called incognito), you can open Gmail there too.

---

## tr005-r
- task: Email stopped working (details unknown) | platform: unknown | scenario: failure_recovery | sensitive: False
- sources: Gmail Help: Gmail won't load <https://support.google.com/mail/answer/7074871?hl=en>

**USER:**
Gmail won't open in the browser on my computer. I think it might be my internet. What do I check?

**ASSISTANT:**
Let's check your internet connection.

1. Restart your computer.
2. Turn your Wi-Fi off, then back on.
3. Open Gmail again.

If it still will not load, tell me and we'll try the next step.

**USER:**
I did both of those and Gmail is still stuck. my husband said something about the router

**ASSISTANT:**
Your husband is right, the router is the next thing to try.

1. Restart your router. The router's manual has instructions on how.
2. Open Gmail again.
3. If it still will not load, connect to a different network, if you have one nearby, and open Gmail there.

If the connection keeps having trouble, contact your internet service provider, or whoever runs your Wi-Fi network.

---

## pilot-006
- task: Printer will not print | platform: unknown | scenario: missing_info | sensitive: False
- sources: Microsoft Support: Fix printer connection and printing problems in Windows <https://support.microsoft.com/en-us/windows/fix-printer-connection-and-printing-problems-in-windows-fb830bff-7702-6349-33cd-9443fe987f73>

**USER:**
My printer won't print anything and I need to print my boarding pass for Thursday. It worked fine last month. The little green light is on.

**ASSISTANT:**
Let's get that boarding pass printed. I'm glad the light is on.

The next steps depend on your computer. **Are you printing from a Windows computer?**

---

## tr006-a
- task: Printer will not print | platform: unknown | scenario: direct | sensitive: False
- sources: Microsoft Support: Fix printer connection and printing problems in Windows <https://support.microsoft.com/en-us/windows/fix-printer-connection-and-printing-problems-in-windows-fb830bff-7702-6349-33cd-9443fe987f73>

**USER:**
My printer is plugged into my Windows computer with a USB cable but nothing comes out when I press print. What should I check?

**ASSISTANT:**
Let's start with two simple things.

1. Turn off the printer and unplug it from the wall.
2. Wait 30 seconds.
3. Plug the printer back in and turn it on.
4. Check the USB cable. Make sure it is firmly connected at both ends, on the printer and on the computer.
5. Try printing again.

If your printer shows an error, check for low ink or paper, an open cover, or a paper jam.

If it still does not print, tell me and we'll try the next step.

---

## tr006-e
- task: Printer will not print | platform: unknown | scenario: constraint | sensitive: False
- sources: Microsoft Support: Fix printer connection and printing problems in Windows <https://support.microsoft.com/en-us/windows/fix-printer-connection-and-printing-problems-in-windows-fb830bff-7702-6349-33cd-9443fe987f73>

**USER:**
The printer by my Windows computer stopped printing. My son warned me never to remove or reinstall the printer on the computer, because it took him hours to set up. So I want to stay away from the computer settings and only try things on the printer itself. It is connected by a USB cable. What can I do?

**ASSISTANT:**
You can try these things right at the printer, without changing anything on the computer.

1. Turn off the printer and unplug it.
2. Wait 30 seconds.
3. Plug it back in and turn it on.
4. Make sure the USB cable is firmly connected at both ends.
5. If the printer shows an error, check for low ink or paper, an open cover, or a paper jam.
6. Try printing again.

If that does not help, the next steps are on the computer, so you may want to ask your son before we try them.

---

## pilot-007
- task: Connect to a Wi-Fi network | platform: iPhone | scenario: direct_messy | sensitive: False
- sources: Apple Support: Connect to Wi-Fi on your iPhone or iPad <https://support.apple.com/en-au/111107>; Apple Support: If you can't connect to Wi-Fi on your iPhone or iPad <https://support.apple.com/en-euro/111786>

**USER:**
I'm staying at my daughter's house this weekend. She wrote the Wi-Fi name and password on a card for me. The network is called SmithHome. I have an iPhone 13 with the latest update. How do I get my phone on her internet?

**ASSISTANT:**
Here's how to connect your iPhone to SmithHome. Keep the card with the password nearby. This takes about two minutes.

1. Open the **Settings** app.
2. Tap **Wi-Fi**.
3. Make sure Wi-Fi is turned on.
4. Tap **SmithHome** in the list.
5. Type the password from the card if it asks.

When you're connected, you'll see a blue tick next to **SmithHome**, and the Wi-Fi icon at the top corner of the screen.

If you don't see SmithHome in the list, move closer to the internet box in her home and check again.

---

## tr007-a
- task: Connect to a Wi-Fi network | platform: iPhone | scenario: direct | sensitive: False
- sources: Apple Support: Connect to Wi-Fi on your iPhone or iPad <https://support.apple.com/en-au/111107>

**USER:**
How do I connect my iPhone to the wifi at my house? I know the password.

**ASSISTANT:**
Here is how to connect your iPhone to your home Wi-Fi.

1. Open **Settings**.
2. Tap **Wi-Fi**.
3. Turn on **Wi-Fi** if it is off. Your iPhone will look for networks by itself.
4. Tap the name of your home network.
5. Type the password if it asks for it.

When it worked, you will see a blue checkmark next to the network name and the Wi-Fi symbol at the top corner of the screen.

---

## tr007-d
- task: Connect to a Wi-Fi network | platform: iPhone | scenario: followup | sensitive: False
- sources: Apple Support: Connect to Wi-Fi on your iPhone or iPad <https://support.apple.com/en-au/111107>

**USER:**
my son said to get on the wifi at his place. how do i do that on my phone

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

**USER:**
iPhone

**ASSISTANT:**
Thank you. Here is how to join your son's Wi-Fi on your iPhone. Have the password handy.

1. Open **Settings**.
2. Tap **Wi-Fi**.
3. Turn on **Wi-Fi** if it is off.
4. Tap the name of your son's network in the list.
5. Type the password if it asks for it. It may also ask you to agree to terms and conditions.

When you are connected, you will see a blue checkmark next to the network name and the Wi-Fi symbol at the top corner of the screen.

---

## tr007-e
- task: Connect to a Wi-Fi network | platform: iPhone | scenario: constraint | sensitive: False
- sources: Apple Support: Connect to Wi-Fi on your iPhone or iPad <https://support.apple.com/en-au/111107>

**USER:**
I'm at the community center with my iPhone and they have free wifi, but nobody gave me a password and I don't want to go bother the front desk if there's another way around it. Can you just connect me?

**ASSISTANT:**
I can show you the steps, but the network may ask for a password or for you to agree to terms and conditions.

1. Open **Settings**.
2. Tap **Wi-Fi**.
3. Turn on **Wi-Fi** if it is off.
4. Tap the name of the community center network.
5. If it asks you to agree to terms and conditions, agree to them.

If it asks for a password, I can't get around that. You will need to ask the network administrator for it. Once you are connected, you will see a blue checkmark next to the network name.

---

## tr007-r
- task: Connect to a Wi-Fi network | platform: iPhone | scenario: failure_recovery | sensitive: False
- sources: Apple Support: Connect to Wi-Fi on your iPhone or iPad <https://support.apple.com/en-au/111107>; Apple Support: If you can't connect to Wi-Fi on your iPhone or iPad <https://support.apple.com/en-euro/111786>

**USER:**
I'm staying at my daughter's house this weekend. She wrote the Wi-Fi name and password on a card for me. The network is called SmithHome. I have an iPhone 13 with the latest update. How do I get my phone on her internet?

**ASSISTANT:**
Here's how to connect your iPhone to SmithHome. Keep the card with the password nearby. This takes about two minutes.

1. Open the **Settings** app.
2. Tap **Wi-Fi**.
3. Make sure Wi-Fi is turned on.
4. Tap **SmithHome** in the list.
5. Type the password from the card if it asks.

When you're connected, you'll see a blue tick next to **SmithHome**, and the Wi-Fi icon at the top corner of the screen.

If you don't see SmithHome in the list, move closer to the internet box in her home and check again.

**USER:**
I don't see SmithHome in the list at all.

**ASSISTANT:**
Let's check a few things. Try them in order, and stop as soon as **SmithHome** appears in the list.

1. **Check the exact name.** Ask your daughter to check the network name. It might be slightly different, like **SmithHome-5G**.
2. **Ask whether other phones work.** Ask your daughter whether other phones in the house can connect.
3. **Check the internet box.** Make sure the router is plugged in and its lights are on.
4. **Move closer** to the router, then look at the list again.
5. **Check Airplane Mode.** In **Settings**, make sure **Airplane Mode** is turned off.
6. **Check the Wi-Fi switch.** If it looks gray and you can't tap it, restart your iPhone.
7. **Restart the router.** Unplug the router and the modem, then plug them back in. Ask your daughter first, because this turns off the internet for everyone in the house for a few minutes.

If SmithHome still doesn't show up, tell me which network names you do see.

---

## pilot-008
- task: Make everything on screen bigger | platform: Windows 11 | scenario: direct | sensitive: False
- sources: Microsoft Support: Make text and apps bigger <https://support.microsoft.com/en-us/topic/c3095a80-6edd-4779-9282-623c4d721d64>

**USER:**
Everything on my laptop screen is too small. It has Windows 11. How do I make it all bigger?

**ASSISTANT:**
You can make everything on the screen bigger in Settings. It takes about two minutes, and you can change it back anytime.

1. Click the **Start** button.
2. Click **Settings**.
3. Click **Display**.
4. Under **Scale & layout**, open the **Scale** dropdown.
5. Choose a bigger percentage.

The screen will change size right away. Try a number, and if things are still too small, pick a bigger one.

If only the **words** are too small, there's another setting just for text. Tell me and I'll walk you through it. Some programs may look right only after you sign out and back in.

---

## tr008-b
- task: Make everything on screen bigger | platform: Windows 11 | scenario: missing_info | sensitive: False
- sources: Microsoft Support: Make text and apps bigger <https://support.microsoft.com/en-us/topic/c3095a80-6edd-4779-9282-623c4d721d64>

**USER:**
My Windows 11 laptop is hard for me to read, can you make it bigger?

**ASSISTANT:**
I can help with that. Do you want just the **words** bigger, or **everything** on the screen, including pictures and programs?

---

## tr008-c
- task: Make everything on screen bigger | platform: Windows 11 | scenario: direct_messy | sensitive: False
- sources: Microsoft Support: Make text and apps bigger <https://support.microsoft.com/en-us/topic/c3095a80-6edd-4779-9282-623c4d721d64>

**USER:**
My eyes aren't what they used to be. I'm on a Windows 11 computer. The pictures and the windows are fine, it's the writing under the little icons and the menus at the top that I can barely read. I don't want to change the whole screen, only the writing. What do I do?

**ASSISTANT:**
You can make only the writing bigger, and leave the pictures and windows as they are.

1. Press the **Windows logo key** and the **U** key together. This opens Accessibility settings.
2. Click **Text size**.
3. Drag the **Text size** slider to the right until the sample text looks easy to read.
4. Click **Apply**.

Windows will make the text bigger on title bars, menus, and icon labels.

If the Windows logo key and U do not work, click **Start**, click **Settings**, then click **Accessibility**.

---

## tr008-d
- task: Make everything on screen bigger | platform: Windows 11 | scenario: followup | sensitive: False
- sources: Microsoft Support: Make text and apps bigger <https://support.microsoft.com/en-us/topic/c3095a80-6edd-4779-9282-623c4d721d64>

**USER:**
My Windows 11 laptop is hard for me to read, can you make it bigger?

**ASSISTANT:**
I can help with that. Do you want just the **words** bigger, or **everything** on the screen, including pictures and programs?

**USER:**
just the words

**ASSISTANT:**
Here is how to make just the words bigger on Windows 11.

1. Click **Start**, then click **Settings**.
2. Click **Accessibility**.
3. Click **Text size**.
4. Drag the **Text size** slider to the right. The sample text gets bigger.
5. Click **Apply**.

Windows will make the text bigger on title bars, menus, and icon labels.

---

## tr008-e
- task: Make everything on screen bigger | platform: Windows 11 | scenario: constraint | sensitive: False
- sources: Microsoft Support: Make text and apps bigger <https://support.microsoft.com/en-us/topic/c3095a80-6edd-4779-9282-623c4d721d64>

**USER:**
Everything on my Windows 11 screen is too small, the pictures, the programs, all of it. I'd like the fastest way, I heard there is a key I can press so I don't have to click around the Start menu. Is there?

**ASSISTANT:**
Yes. A key shortcut opens Settings directly.

1. Press the **Windows logo key** and the **I** key together. Settings opens.
2. Click **Display**.
3. Under **Scale & layout**, click the **Scale** menu.
4. Choose a bigger option from the list.

Scale makes everything on the screen bigger, including pictures and programs. Most changes show up right away.

---

## tr008-r
- task: Make everything on screen bigger | platform: Windows 11 | scenario: failure_recovery | sensitive: False
- sources: Microsoft Support: Make text and apps bigger <https://support.microsoft.com/en-us/topic/c3095a80-6edd-4779-9282-623c4d721d64>

**USER:**
Please help me make everything bigger on my Windows 11 laptop screen.

**ASSISTANT:**
Here is how to make everything on the screen bigger.

1. Click **Start**, then click **Settings**.
2. Click **Display**.
3. Under **Scale & layout**, click the **Scale** menu.
4. Choose a bigger option.

Most changes show up right away.

**USER:**
Most of it got bigger but one program still looks tiny.

**ASSISTANT:**
Some programs only show the change after you sign out and sign back in.

1. Save your work in your programs.
2. Sign out of Windows.
3. Sign back in and open the program again.

---

## tr009-a
- task: Internet not working (message cut off) | platform: unknown | scenario: direct | sensitive: False
- sources: Apple Support: If you can't connect to Wi-Fi on your iPhone or iPad <https://support.apple.com/en-euro/111786>

**USER:**
My iPhone won't get on the internet at home. The wifi at home is the only thing I use. What should I check?

**ASSISTANT:**
Let's check a few things on your iPhone. Stop when it works.

1. Open **Settings**, then tap **Wi-Fi**. Make sure **Wi-Fi** is turned on.
2. Tap the name of your home network. Look for a blue checkmark next to it.
3. If it still does not work, go back to **Settings** and make sure **Airplane Mode** is off.
4. Tap **Wi-Fi** again and make sure **Connectivity Assist** is off.

If you still see **No Internet Connection**, the problem may be with your router. Check your router and network settings.

---

## tr009-c
- task: Internet not working (message cut off) | platform: unknown | scenario: direct_messy | sensitive: False
- sources: Apple Support: If you can't connect to Wi-Fi on your iPhone or iPad <https://support.apple.com/en-euro/111786>

**USER:**
Last week my grandson put a VPN app on my iPhone so I could watch shows from home. Ever since then my phone says it's connected to the wifi but nothing loads. The wifi worked fine before that and my other devices are fine too. What do I do?

**ASSISTANT:**
The VPN app may be getting in the way. Try this.

1. Uninstall the VPN app.
2. Restart your iPhone.
3. Test your Wi-Fi connection again.

If that fixes it, you know the app was the cause. If you need to keep the app, contact whoever manages your VPN or the company that makes the app.

---

## tr009-d
- task: Internet not working (message cut off) | platform: unknown | scenario: followup | sensitive: False
- sources: Apple Support: If you can't connect to Wi-Fi on your iPhone or iPad <https://support.apple.com/en-euro/111786>

**USER:**
the internet on my

**ASSISTANT:**
It looks like your message got cut off, but I'd be glad to help with your internet.

**Which device is having trouble** (for example your phone, computer, or TV), and **what happens when you try to go online?**

**USER:**
my iPhone, it won't connect to the wifi at home

**ASSISTANT:**
Thank you. Let's check your iPhone. Stop when it connects.

1. Open **Settings**, then tap **Wi-Fi**. Make sure **Wi-Fi** is turned on.
2. Tap the name of your home network. Look for a blue checkmark.
3. If it still won't connect, go back to **Settings** and make sure **Airplane Mode** is off.
4. Tap **Wi-Fi** again and make sure **Connectivity Assist** is off.

If you still see **No Internet Connection**, check your router and network settings.

---

## tr009-r
- task: Internet not working (message cut off) | platform: unknown | scenario: failure_recovery | sensitive: False
- sources: Apple Support: If you can't connect to Wi-Fi on your iPhone or iPad <https://support.apple.com/en-euro/111786>

**USER:**
My iPhone will not connect to my home wifi. Please tell me what to try.

**ASSISTANT:**
Let's check a few things on your iPhone.

1. Open **Settings**, then tap **Wi-Fi**. Make sure **Wi-Fi** is turned on.
2. Tap your home network name. Look for a blue checkmark.
3. If it still does not work, go back to **Settings** and make sure **Airplane Mode** is off.
4. Tap **Wi-Fi** again and make sure **Connectivity Assist** is off.

**USER:**
The wifi setting is gray and I can't tap it.

**ASSISTANT:**
When the Wi-Fi setting is grayed out, the fix is to restart your iPhone.

1. Restart your iPhone.
2. Open **Settings** and tap **Wi-Fi** again.
3. Tap your home network name and look for a blue checkmark.

If it still will not connect to any Wi-Fi network, contact Apple.

---

## pilot-010
- task: Reset forgotten Apple Account password | platform: iPhone | scenario: direct | sensitive: True
- sources: Apple Support: Change your Apple Account password <https://support.apple.com/en-mz/101567>; Apple Support: If you forgot your Apple Account password <https://support.apple.com/en-us/ht201487>; Apple Support: Recognize and avoid social engineering schemes including phishing messages, phony support calls, and other scams <https://support.apple.com/en-us/102568>

**USER:**
I forgot my Apple ID password. I can still open my iPhone with my passcode. How do I make a new password?

**ASSISTANT:**
Good news: you can make a new password right on your iPhone if it is already signed in to your Apple Account with two-factor authentication. (Apple calls this your Apple Account.)

1. Open the **Settings** app.
2. Tap **your name**.
3. Tap **Sign-In & Security**.
4. Tap **Change Password**.
5. Follow the instructions on the screen to set your new password.
6. If it asks, choose **Remove Other Devices** (other devices must sign in again) or **Keep All Devices Signed In**.

You may have to wait one hour before you can change it.

Never give it to anyone who calls or texts you offering help with your account.

If **Change Password** doesn't appear, tell me what you see and I'll help with another way.

---

## tr010-b
- task: Reset forgotten Apple Account password | platform: iPhone | scenario: missing_info | sensitive: True
- sources: Apple Support: Change your Apple Account password <https://support.apple.com/en-mz/101567>

**USER:**
I need to change my Apple ID password

**ASSISTANT:**
I can help with that. Which device are you using: an **iPhone or iPad**, a **Mac**, or a **web browser** on a computer?

---

## tr010-c
- task: Reset forgotten Apple Account password | platform: iPhone | scenario: direct_messy | sensitive: True
- sources: Apple Support: Change your Apple Account password <https://support.apple.com/en-mz/101567>

**USER:**
My nephew told me I should change my Apple ID password every so often. I'm at my computer at the library and I only have the internet browser, no Apple stuff on this machine. Is there a way to do it on a website?

**ASSISTANT:**
Yes, you can do it on the Apple website.

1. Go to **account.apple.com** and sign in.
2. Go to **Sign-In and Security**.
3. Choose **Password**.

If you have an Apple device you trust, the website may send you to that device to finish. That is normal. The website may only let you change the password itself if you have no trusted device.

---

## tr010-d
- task: Reset forgotten Apple Account password | platform: iPhone | scenario: followup | sensitive: True
- sources: Apple Support: Change your Apple Account password <https://support.apple.com/en-mz/101567>

**USER:**
I need to change my Apple ID password

**ASSISTANT:**
I can help with that. Which device are you using: an **iPhone or iPad**, a **Mac**, or a **web browser** on a computer?

**USER:**
my iPad

**ASSISTANT:**
Here is how to change your Apple Account password on your iPad.

1. Open **Settings**.
2. Tap **your name** at the top.
3. Tap **Sign-In & Security**.
4. Tap **Change Password**.
5. Follow the instructions on the screen.
6. If other devices are signed in, choose **Remove Other Devices** or **Keep All Devices Signed In**.

If it asks you to wait about an hour, that is a security feature called Stolen Device Protection.

---

## tr010-e
- task: Reset forgotten Apple Account password | platform: iPhone | scenario: constraint | sensitive: True
- sources: Apple Support: Change your Apple Account password <https://support.apple.com/en-mz/101567>

**USER:**
I want to change my Apple Account password on my iPhone, but my wife uses the iPad that is signed in with my account too and I don't want her kicked out of it while I change it. Can I do that?

**ASSISTANT:**
Yes. You can choose to keep your other devices signed in.

1. Open **Settings** and tap **your name** at the top.
2. Tap **Sign-In & Security**.
3. Tap **Change Password**.
4. Follow the instructions on the screen.
5. When it asks about other signed in devices, choose **Keep All Devices Signed In**.

Do not choose **Remove Other Devices**, because that makes the iPad sign in again.

---

## tr010-r
- task: Reset forgotten Apple Account password | platform: iPhone | scenario: failure_recovery | sensitive: True
- sources: Apple Support: Change your Apple Account password <https://support.apple.com/en-mz/101567>

**USER:**
Please walk me through changing my Apple Account password on my iPhone.

**ASSISTANT:**
Here is how to change it on your iPhone.

1. Open **Settings** and tap **your name**.
2. Tap **Sign-In & Security**.
3. Tap **Change Password**.
4. Follow the instructions on the screen.
5. If other devices are signed in, choose **Remove Other Devices** or **Keep All Devices Signed In**.

**USER:**
It says I have to wait an hour before I can change it. Is something wrong?

**ASSISTANT:**
Nothing is wrong. You might have to wait one hour before changing your password because of a security feature called Stolen Device Protection.

1. Wait one hour.
2. Then open **Settings**, tap **your name**, tap **Sign-In & Security**, and tap **Change Password** again.

---

## pilot-011
- task: Install a software update | platform: iPhone | scenario: direct_messy | sensitive: False
- sources: Apple Support: Update your iPhone or iPad <https://support.apple.com/en-ie/118575>

**USER:**
My iPhone keeps showing a message about a software update and I keep pressing Later because I'm afraid I'll lose my pictures of my grandchildren. Should I do it, and how?

**ASSISTANT:**
It's wise to be careful with your pictures. Updates are generally a good idea because they fix problems and keep your phone secure, and backing up first protects your photos.

**Before you start:**
1. Back up your iPhone with iCloud. If you're not sure whether it's backed up, ask me and I'll show you how to check.
2. Plug your iPhone into its charger.
3. Make sure you're connected to Wi-Fi.

**To update:**
4. Open **Settings**.
5. Tap **General**.
6. Tap **Software Update**.
7. Tap **Download and Install** (the button may say **Update Now**).
8. Follow the instructions on the screen (it may ask for your passcode).

If it says there isn't enough space, tap **Continue** to let it remove some apps for now. They come back by themselves after the update.

---

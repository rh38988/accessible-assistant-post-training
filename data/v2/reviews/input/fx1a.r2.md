# Review input: batch fx1a, round 2 (17 examples)

## tr001-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Samsung Galaxy
- task: Make text bigger (Samsung Galaxy) | sensitive: False | reviewed by a person: False
- sources: https://www.samsung.com/latin_en/support/mobile-devices/how-to-adjust-the-font-size-and-style-on-your-galaxy-phone/

**USER:**
Hello, my daughter gave me her old Samsung Galaxy phone last month and I am still getting used to it. My eyes are not what they were since the cataract surgery and I cannot read the recipes my friends send me, the writing is just too small. Could the words be made larger, and maybe darker too?

**ASSISTANT:**
Yes, you can make the words larger and bolder in the Settings. It takes about a minute.

1. Open the **Settings** app.
2. Tap **Display**.
3. Tap **Font size and style**.
4. On that screen, adjust the options to make the font bigger. You can also choose to make it bold, which makes the letters darker and thicker.

Try one change at a time so you can see what suits your eyes. Menu names can look a little different depending on the phone model and software version.

## tr001-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Samsung Galaxy
- task: Make text bigger (Samsung Galaxy) | sensitive: False | reviewed by a person: False
- sources: https://www.samsung.com/latin_en/support/mobile-devices/how-to-adjust-the-font-size-and-style-on-your-galaxy-phone/

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

## tr001-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Samsung Galaxy
- task: Make text bigger (Samsung Galaxy) | sensitive: False | reviewed by a person: False
- sources: https://www.samsung.com/latin_en/support/mobile-devices/how-to-adjust-the-font-size-and-style-on-your-galaxy-phone/

**USER:**
I have a Samsung Galaxy and the print is too small for me. My grandson told me I could download special fonts but I do not want to download anything or pay for anything, I just want the same letters to look bigger. What do I do?

**ASSISTANT:**
You don't need to download anything. The size can be changed right in your settings, and it's free.

1. Open the **Settings** app.
2. Tap **Display**.
3. Tap **Font size and style**.
4. On that screen, adjust the options to make the font bigger. Leave **Font style** alone, because that is the part that downloads new fonts.

Your letters will keep the same look, just bigger.

## tr001-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Samsung Galaxy
- task: Make text bigger (Samsung Galaxy) | sensitive: False | reviewed by a person: False
- sources: https://www.samsung.com/latin_en/support/mobile-devices/how-to-adjust-the-font-size-and-style-on-your-galaxy-phone/

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

## tr002-a
- scenario: direct | style: plain | specification: fully_specified | platform: Android
- task: Turn up ring volume (device unknown) (unknown) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9082609?hl=en

**USER:**
I have a Google Pixel phone and I can't hear it ring from the other room. How do I make the ringer louder?

**ASSISTANT:**
You can turn the ringer up with the buttons on the side of your phone.

1. Press one of the **volume buttons** on the side of your phone.
2. A small volume bar appears on the screen. Tap the **Menu** icon at the right.
3. Find **Ring Volume** and slide it up to make the ring louder.

If you don't see a **Menu** icon, your phone has older software. Tap the **Down arrow** at the right instead, then slide **Ring**.

If your phone was set to vibrate or mute, tap the **Ring** icon above the slider, then turn off **Vibrate** or turn on **Ring** to bring the sound back.

## tr002-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Android
- task: Turn up ring volume (device unknown) (unknown) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9082609?hl=en

**USER:**
My phone hardly makes any sound when someone calls and I keep missing calls from my doctor's office.

**ASSISTANT:**
I'm sorry you've been missing those calls. I can help you make the ringing louder.

First, one quick question: is your phone an **iPhone**, or another kind of phone, like a Samsung or Google Pixel?

If you're not sure, look at the back of the phone. An iPhone has an apple logo on the back.

**USER:**
no apple on the back, its a google pixel

**ASSISTANT:**
Thank you. A Pixel is an Android phone, so here is how to make the ringing louder.

1. Press one of the **volume buttons** on the side of your phone.
2. Tap the **Menu** icon at the right of the volume bar.
3. Find **Ring Volume** and slide it up.

If your phone was set to vibrate or mute, tap the **Ring** icon above the slider and turn off **Vibrate** or turn on **Ring**.

## tr002-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Android
- task: Turn up ring volume (device unknown) (unknown) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9082609?hl=en

**USER:**
I have an Android phone, a Google Pixel. I get lost whenever I go into the Settings app, so please do not send me there. Is there any way to make the ring louder using just the buttons on the side of the phone?

**ASSISTANT:**
Yes, you can do it without opening the Settings app.

1. Press one of the **volume buttons** on the side of your phone.
2. Tap the **Menu** icon at the right of the volume bar.
3. Find **Ring Volume** and slide it up to make the ring louder.

If you don't see a **Menu** icon, your phone may be an older version. Tell me and I'll give you the steps for that.

## tr002-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Android
- task: Turn up ring volume (device unknown) (unknown) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9082609?hl=en

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

## tr003-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Android (Google Messages)
- task: Send a photo by text message (Android (Google Messages)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/messages/answer/6159880?hl=en

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

## tr003-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Android (Google Messages)
- task: Send a photo by text message (Android (Google Messages)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/messages/answer/6159880?hl=en

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

## tr003-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Android (Google Messages)
- task: Send a photo by text message (Android (Google Messages)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/messages/answer/6159880?hl=en

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

## tr004-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone (Home button)
- task: Take a screenshot (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/102616

**USER:**
How do I take a picture of what's on my iPhone screen? My grandson wants me to send him a screenshot.

**ASSISTANT:**
Happy to help. The buttons you press depend on your iPhone model, so one quick question first: is the button that wakes your iPhone on the **top edge** or on the **right side**?

**USER:**
its on the right side, and there is a round button under the screen too

**ASSISTANT:**
Thank you. Here is how to take the screenshot on your iPhone.

1. Open the screen you want to send to your grandson.
2. Press the **side button** and the **Home button** (the round button) at the same time.
3. Let go of both buttons quickly.

You can find it later in **Photos**. Tap **Collections**, then **Media Types**, then **Screenshots**.

## tr005-a
- scenario: direct | style: plain | specification: fully_specified | platform: Gmail (computer browser)
- task: Email stopped working (details unknown) (unknown) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/7074871?hl=en

**USER:**
I read my Gmail in a web browser on my computer and the page will not load today. What should I try?

**ASSISTANT:**
Let's try a few things, starting with the easiest.

1. Make sure your browser is up to date. Update it to the latest version.
2. Open Gmail again.
3. If it still will not load, try a different browser and open Gmail there.
4. Clear your browser's saved website data (called cache and cookies), then open Gmail again.

If Gmail still will not load, tell me and we'll check your internet connection next.

## tr005-d
- scenario: followup | style: verbose | specification: fully_specified | platform: Gmail (computer browser)
- task: Email stopped working (details unknown) (unknown) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/7074871?hl=en

**USER:**
Good morning. I hope you can help me. My husband always took care of these things. Since about Tuesday the Gmail page will not open for me, it just sits there. I tried turning it off and on.

**ASSISTANT:**
Good morning. I'm glad you asked, and we can figure this out together. Turning it off and on was a good first try.

So I can give you the right steps, **do you open Gmail in a web browser on a computer**, or in an app on a phone or tablet?

**USER:**
i open it in the browser on my computer

**ASSISTANT:**
Thank you, that helps. Here are some things to try for Gmail on your computer.

1. Update your browser to the latest version, then open Gmail again.
2. If it still does not load, try a different browser.
3. Restart your computer and open Gmail again.
4. Turn your Wi-Fi off, then back on, and open Gmail again.

If none of that works, tell me what happens and we'll try the next step.

## tr006-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Windows 11 (wireless printer)
- task: Printer will not print (unknown) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/fix-printer-connection-and-printing-problems-in-windows-fb830bff-7702-6349-33cd-9443fe987f73

**USER:**
We got a wireless printer a few years ago and I use it with my Windows 11 laptop from the sunroom. Last week the internet company sent a little box to make the Wi-Fi reach the back of the house and since then the printer will not print anything. I have a tax form to print. The printer lights are on. Please explain it simply, I am not very good with this.

**ASSISTANT:**
The new Wi-Fi box could be the reason. Let's check the printer's wireless first.

1. Turn off the printer and unplug it.
2. Wait 30 seconds.
3. Plug it back in and turn it on.
4. Look for a button on the printer that shows a blue wireless icon. Use it to make sure wireless is on.
5. Run the printer's built-in wireless test. Many printers have a menu option for it.
6. If the test passes but it still will not print, make sure your laptop is online.
7. Make sure your laptop is on the same Wi-Fi network as the printer. With a Wi-Fi box like the new one, the laptop can end up on a different network from the printer.
8. Try printing again.

If it still does not print, tell me what happens and we'll try the next step.

## tr006-d
- scenario: followup | style: verbose | specification: fully_specified | platform: Windows
- task: Printer will not print (unknown) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/fix-printer-connection-and-printing-problems-in-windows-fb830bff-7702-6349-33cd-9443fe987f73

**USER:**
My printer won't print anything and I need to print my boarding pass for Thursday. It worked fine last month. The little green light is on.

**ASSISTANT:**
Let's get that boarding pass printed.

The next steps depend on what you're printing from. **Are you printing from a computer or from a phone?** If it's a computer, do you know if it's a Windows computer or a Mac?

**USER:**
its a windows computer

**ASSISTANT:**
Thank you. Let's try these steps for your Windows computer.

1. Turn off the printer and unplug it.
2. Wait 30 seconds.
3. Plug it back in and turn it on.
4. If it connects with a USB cable, make sure the cable is firmly connected at both ends.
5. If it connects wirelessly, make sure the printer's wireless option is turned on. Look for a button on the printer that shows a blue wireless icon.
6. Try printing your boarding pass again.

If it still does not print, tell me and we'll try the next step.

## tr006-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Windows 11
- task: Printer will not print (unknown) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/fix-printer-connection-and-printing-problems-in-windows-fb830bff-7702-6349-33cd-9443fe987f73

**USER:**
My printer stopped printing from my Windows 11 computer. I already tried switching it off and on. What next?

**ASSISTANT:**
Let's check the connection and give the printer a longer restart.

1. Turn off the printer and unplug it.
2. Wait 30 seconds.
3. Plug it back in and turn it on.
4. If it uses a USB cable, make sure the cable is firmly connected at both ends.
5. If it connects wirelessly, make sure the printer's wireless option is on. Look for a button on the printer that shows a blue wireless icon.
6. Try printing again.

**USER:**
I did all that and it still won't print

**ASSISTANT:**
Next, let's remove the printer from your computer and add it again.

1. Click **Start**, then **Settings**, then **Bluetooth & devices**, then **Printers & scanners**.
2. Click your printer, then click **Remove**, then click **Yes**.
3. Make sure the printer is on and connected. On the same page, click **Add device**.
4. Wait while Windows searches. When your printer appears, click **Add device** next to it.
5. If it does not appear, click **Add manually**.
6. Click **Add a local printer or network printer with manual settings**, then click **Next**.
7. Click **Use an existing port**, pick the port your printer uses, then click **Next**.
8. Choose your printer's maker and model, then click **Next**.
9. Type a name, click **Next**, and choose **Do not share this printer**.
10. Click **Print a test page**, then click **Finish**.

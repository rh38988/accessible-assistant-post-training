# Review input: batch fx6, round 1 (26 examples)

## tr076-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: Scan a QR code (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102680

**USER:**
My iPhone screen is asleep on the counter and my hands are messy from cooking. Is there a quicker way to get to the camera for the QR code on my recipe card, without hunting for apps?

**ASSISTANT:**
Yes, you can open the camera straight from the Lock Screen.

1. Open the **Camera** from the Lock Screen.
2. Hold your iPhone so the QR code is in view.
3. Tap the **link** that appears over the code.

The recipe page will open.

Some newer iPhone models also have a **Camera Control** button you can use to open the camera.

## tr076-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: Scan a QR code (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102680

**USER:**
How do I use the Scan Code button on my iPhone to read a QR code?

**ASSISTANT:**
The **Scan Code** button is in Control Center. Here is how to use it.

1. Open **Control Center**.
2. Tap the **Scan Code** button. It has a little square viewfinder picture.
3. Hold your iPhone so the QR code is in view.
4. Tap the **link** that appears.

If you don't see **Scan Code** in Control Center, tell me and I'll show you how to add it.

**USER:**
There is no Scan Code button in my Control Center.

**ASSISTANT:**
That button only shows up after you add it. Here is how:

1. Open **Control Center**.
2. Touch and hold the background of the screen, then tap **Add a Control**.
3. In the list that opens, tap **Scan Code**.
4. Tap anywhere on the screen to go back to Control Center.

Now **Scan Code** should be in Control Center, and you can use it to scan.

## tr077-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Android
- task: Scan a QR code (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/camerafromgoogle/answer/12033278?hl=en

**USER:**
I use the Camera from Google app on my Android. It is set to video mode because I was filming my granddaughter, and I'd like to scan a QR code without leaving video mode. Can I?

**ASSISTANT:**
Not in video mode. QR codes can't be scanned in video mode or portrait mode, so you need to switch out of video mode first.

1. Open the **Camera from Google** app.
2. Switch to regular photo mode, or tap the **QR** button.
3. Point your camera at the QR code.
4. When a banner appears, tap it to open the page or app.

You can switch back to video mode when you are done.

## tr077-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Android
- task: Scan a QR code (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/camerafromgoogle/answer/12033278?hl=en

**USER:**
How do I scan a QR code with the Camera from Google app on my Android?

**ASSISTANT:**
You can do it right in the camera. It takes a few seconds.

1. Open the **Camera from Google** app.
2. Tap the **QR** button, then point your camera at the code. You can also just point at the code in regular photo mode.
3. When a banner appears, tap it to open the page or app.

QR codes can't be scanned in portrait or video mode.

**USER:**
I don't see a QR button anywhere.

**ASSISTANT:**
That is okay. Try this instead:

1. Make sure the camera is in regular photo mode, not portrait or video.
2. Point the camera at the code without tapping anything.
3. When the banner appears, tap it.

If nothing shows up, this feature is only on selected devices, so your phone may not have it.

## tr078-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone (Medical ID)
- task: Set up emergency medical info (iPhone (Medical ID)) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-us/105072

**USER:**
I have an iPhone. I don't want to type in my medications or conditions, I only want my son listed as my emergency contact on my Medical ID. What do I do?

**ASSISTANT:**
You can add just an emergency contact and leave everything else empty.

1. Open the **Health** app.
2. Tap the **Summary** tab.
3. Tap your **profile picture** in the upper corner.
4. Tap **Medical ID**.
5. Tap **Edit** next to **Emergency Contacts**.
6. Tap the **plus** button next to **Add Emergency Contact**.
7. Choose your son from your contacts and add how he is related to you.
8. Tap **Done**.

To remove a contact later, go back to the same place, tap the **delete** button next to the name, then tap **Delete**.

## tr078-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone (Medical ID)
- task: Set up emergency medical info (iPhone (Medical ID)) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-us/105072

**USER:**
How do I make my iPhone share my Medical ID with emergency services when I call them? I have an iPhone.

**ASSISTANT:**
You can turn that on in your Medical ID.

1. Open the **Health** app and tap the **Summary** tab.
2. Tap your **profile picture** in the upper corner.
3. Tap **Medical ID**.
4. Turn on **Share During Emergency Call**.
5. Tap **Done**.

Then your Medical ID is shared when you call or text emergency services from your iPhone.

**USER:**
I did that, but how can I be sure it will really get sent? I'm worried it's not working.

**ASSISTANT:**
Good question. There is one more setting to check:

1. Open **Settings**.
2. Tap **Privacy & Security**, then **Location Services**.
3. Tap **System Services**.
4. Make sure **Emergency Calls & SOS** is turned on.

If it is off, your Medical ID information won't be shared.

## tr079-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Android
- task: Add emergency information (Android) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/android/answer/9319337?hl=en

**USER:**
I want to save my emergency contact and my medicines in my Android phone, but I do not want any of it showing on the lock screen for strangers to see. Is that possible?

**ASSISTANT:**
Yes. The lock screen part is optional, so you can simply skip it.

1. Open the **Safety** app and sign in to your Google Account.
2. Tap **Your info**.
3. Tap **Medical information**, then tap **Medications** and type your details.
4. Go back and tap **Emergency contacts**.
5. Tap **Add contact** and choose someone.

Do not turn on **Show when locked** under **Emergency info access**. Anyone holding your phone can see information that is shown on the lock screen. If it is already showing there, you can turn it off in the Safety app.

## tr079-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Android
- task: Add emergency information (Android) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/android/answer/9319337?hl=en

**USER:**
How do I put my allergies and an emergency contact on my Android phone?

**ASSISTANT:**
You can do it in the **Safety** app.

1. Open the **Safety** app and sign in to your Google Account.
2. Tap **Your info**.
3. Tap **Medical information**, then tap **Allergies** and type your details.
4. Go back and tap **Emergency contacts**.
5. Tap **Add contact** and choose someone.

**USER:**
I can't find an app called Safety on my phone.

**ASSISTANT:**
Some phones call it something else, and some don't have it.

1. Look for **Personal Safety**. That is the name used in the Play Store and in Settings.
2. If you can't find it, your phone may not include that app.
3. Open **Settings** and check your Android version. Some of these steps need Android 12 or later.

## tr080-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: Turn off notifications from an app (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/120681

**USER:**
My iPhone's news app buzzes me all day. I need my text messages and calendar alerts to keep working, so I only want to stop the news app. How?

**ASSISTANT:**
You can change this for one app at a time, so your other apps will not be touched.

1. Open the **Settings** app.
2. Tap **Apps**.
3. Tap the news app.
4. Tap **Notifications**.
5. Turn off **Allow Notifications**.

Only the news app goes quiet. Your messages and calendar keep sending alerts the way they do now.

## tr080-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: Turn off notifications from an app (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/120681

**USER:**
My iPhone keeps showing alerts from a coupon app. How do I stop them?

**ASSISTANT:**
You can turn them off for just that app.

1. Open the **Settings** app.
2. Tap **Apps**.
3. Tap the coupon app.
4. Tap **Notifications**.
5. Turn off **Allow Notifications**.

**USER:**
I tapped the coupon app but I don't see Notifications there.

**ASSISTANT:**
Let's check two things.

1. Go back to the **Apps** list in **Settings** and make sure you tapped the coupon app itself.
2. If you are in the right app and still don't see **Notifications**, that app may not be able to send notifications at all.

## tr081-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Android
- task: Turn off notifications from an app (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9079661?hl=en

**USER:**
On my Android phone, my pharmacy app sends both sale ads and refill reminders. I want to keep the refill reminders and stop only the ads. Can I do that?

**ASSISTANT:**
Yes. You can turn off just the kinds of alerts you don't want.

1. Open **Settings**.
2. Tap **Notifications**, then **App notifications**.
3. Tap the pharmacy app.
4. Tap a **category** to see more options.
5. Turn off the categories you don't want, like the ads.

Leave the refill reminder category turned on. Menu names can vary a little on different phones.

## tr081-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Android
- task: Turn off notifications from an app (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9079661?hl=en

**USER:**
How can I turn off notifications for a weather app on my Android phone?

**ASSISTANT:**
You can turn them off for just that app.

1. Open **Settings**.
2. Tap **Notifications**, then **App notifications**.
3. Under **Most recent**, tap the weather app.
4. Turn its notifications off.

**USER:**
The weather app isn't in that list.

**ASSISTANT:**
The list may only show recent apps. Try this:

1. In **App notifications**, tap the dropdown near the top and choose **All apps**.
2. Tap the weather app and turn its notifications off.

On an older Android version, there is no recent list. Tap **App notifications**, then choose the app.

## tr082-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Chrome (computer)
- task: Make a web page bigger (Chrome (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop

**USER:**
I use Chrome on my Windows laptop. I want the words bigger on every website, but I don't want the pictures and buttons to get bigger too, it messes up the layout. Is there a way?

**ASSISTANT:**
Yes. Chrome has a setting for the text size only.

1. Open Chrome and click **More** at the top right.
2. Click **Settings**.
3. Click **Appearance**.
4. Click the down arrow next to **Font size** and pick a size.

This changes the words and leaves the page size setting alone. Do not use **Page zoom**, because that makes everything bigger.

Some websites don't let Chrome change only the text size, so on those sites the words may stay the same.

## tr082-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Chrome (computer)
- task: Make a web page bigger (Chrome (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop

**USER:**
How do I zoom in on one website in Chrome on my computer?

**ASSISTANT:**
You can zoom in from the menu.

1. Open Chrome and go to the website.
2. Click **More** at the top right.
3. Next to **Zoom**, click **Zoom in**. Click it again to go bigger.

You can also hold **Ctrl** and press **+**. To go smaller, use **Zoom out** or hold **Ctrl** and press **-**.

**USER:**
I made that site way too big and now it opens huge every time. How do I put it back?

**ASSISTANT:**
Chrome remembers the size for each site. You can clear it:

1. Click **More**, then **Settings**.
2. Click **Privacy and security**, then **Site Settings**.
3. Click **Additional content settings**, then **Zoom levels**.
4. Click the **X** next to that site.

That removes the saved size for the site.

## tr083-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Windows 11
- task: Find a downloaded file (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/find-my-downloads-in-windows-10-de903ee9-7d37-256b-9145-f0f016c5aed8

**USER:**
I'm on Windows 11 and I saved a tax paper last week but I can't remember where. All I remember is the name started with 'W2'. I don't want to open folder after folder. Can I just search for it?

**ASSISTANT:**
Yes. You can search by name instead of opening folders.

1. Press the **Windows logo key** and **E** together to open File Explorer.
2. Select **Home** in the left pane.
3. Search from **Home** for the part of the name you remember, like W2.

You can also look in **Downloads**, which is pinned under **Quick access** on **Home**.

If the file is saved in a cloud account, sign in to it from **Start**, then **Settings**, then **Accounts**, so it can be included in the search.

## tr083-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Windows 11
- task: Find a downloaded file (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/find-my-downloads-in-windows-10-de903ee9-7d37-256b-9145-f0f016c5aed8

**USER:**
Where do I find the picture I just downloaded on my Windows 11 computer?

**ASSISTANT:**
It is most likely in your **Downloads** folder.

1. Press the **Windows logo key** and **E** together to open File Explorer.
2. Select **Home** in the left pane.
3. Under **Quick access**, open **Downloads**.
4. Look for your picture in the list.

On Windows 11 version 22H2 or later, **Downloads** is pinned there by default.

**USER:**
My File Explorer doesn't have a list on the left side.

**ASSISTANT:**
The left pane may be hidden. You can turn it back on:

1. In File Explorer, select **View**.
2. Select **Show**.
3. Select **Navigation Pane**.

Then select **Home** and open **Downloads** under **Quick access**.

## tr084-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Windows 11
- task: Make the mouse pointer bigger (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/accessibility/windows/make-windows-easier-to-see

**USER:**
I have Windows 11. I only want the little arrow to be bigger. Please don't change my text or the size of everything else on the screen, I just got it the way I like it.

**ASSISTANT:**
You can change just the pointer. Your text and screen size will stay as they are.

1. Click the **Start** button, then click **Settings**.
2. Click **Accessibility**.
3. Click **Mouse pointer & touch**.
4. Choose the options that change the pointer's color and size, and pick what works best for you.

Leave the **Text size** and **Display** settings alone, because those change other things on your screen.

## tr084-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Windows 11
- task: Make the mouse pointer bigger (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/accessibility/windows/make-windows-easier-to-see

**USER:**
How can I see my mouse pointer better on Windows 11? It's too small.

**ASSISTANT:**
You can change how the pointer looks.

1. Click the **Start** button, then click **Settings**.
2. Click **Accessibility**.
3. Click **Mouse pointer & touch**.
4. Choose the options that change the pointer's color and size.

**USER:**
It's bigger now, but I still lose it when I move the mouse fast.

**ASSISTANT:**
Pointer trails can help you follow it.

1. Go back to **Settings**, then **Accessibility**, then **Mouse pointer & touch**.
2. Turn on **Mouse pointer trails**.

Now you will see a trail that shows where the mouse is moving on the screen.

## tr085-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Google Account
- task: Turn on 2-Step Verification (Google Account) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/accounts/answer/185839?hl=en&co=GENIE.Platform%3DDesktop

**USER:**
I want to turn on 2-Step Verification for my Google account on my home computer. Only I use this computer, and I get tired of typing codes, so I don't want to be asked every single time I sign in here. What should I do?

**ASSISTANT:**
You can turn it on and tell Google not to ask again on your own computer.

1. Go to **myaccount.google.com** on your computer and sign in.
2. Select **Security & sign-in**.
3. Under **How you sign in to Google**, select **Turn on 2-Step Verification**.
4. Follow the steps on the screen.

When you are asked for a second step, check **Don't ask again on this computer**. Only do that on a computer you use regularly and don't share with anyone, like your home computer.

## tr085-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Google Account
- task: Turn on 2-Step Verification (Google Account) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/accounts/answer/185839?hl=en&co=GENIE.Platform%3DDesktop

**USER:**
my gmail keeps asking me about a second step thing, I'm on my laptop, how do I get that set up properly?

**ASSISTANT:**
You can do it from your Google Account page.

1. Go to **myaccount.google.com** and sign in.
2. Select **Security & sign-in**.
3. Under **How you sign in to Google**, select **Turn on 2-Step Verification**.
4. Follow the steps on the screen.

If you use a work or school account, these steps might not work.

**USER:**
I'm on my school email and there's no Turn on 2-Step Verification button.

**ASSISTANT:**
That is likely because it is a school account. Those steps might not work for a work, school, or other group account.

1. Contact the administrator who manages the account.
2. Ask them about 2-Step Verification for your account.

## tr086-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: email
- task: Is this email asking me to log in real? (email) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/how-recognize-avoid-phishing-scams

**USER:**
An email says my payment info for my streaming service is out of date and my account will be closed in 24 hours unless I click the link. I can't call anyone until Monday, it's Saturday. Should I just click it to be safe?

**ASSISTANT:**
Please don't click the link. Real companies don't email a link to update your payment information, and the rush is a common trick.

1. Leave the email alone for now. You don't have to do anything about it today.
2. On Monday, if you want to check your account, contact the company using a phone number or website you know is real, not anything in the email.
3. Forward the email to **reportphishing@apwg.org**, and report it at **ReportFraud.ftc.gov**.
4. Delete the email.

Links and attachments in a scam email can also install harmful software.

## tr086-r
- scenario: already_acted | style: failure_recovery | specification: fully_specified | platform: email
- task: Is this email asking me to log in real? (email) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/how-recognize-avoid-phishing-scams

**USER:**
I clicked the link in an email that said it was from my bank, and I typed in my credit card number. Now I think it was fake. What do I do?

**ASSISTANT:**
Thank you for telling me. Go to **IdentityTheft.gov** now. It gives you steps based on what information you gave away.

1. Go to **IdentityTheft.gov** and follow the steps for a lost credit card number.
2. Because you clicked a link, update your security software, run a scan, and remove anything it flags.
3. Report the email at **ReportFraud.ftc.gov**, and forward it to **reportphishing@apwg.org**.

## tr087-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: phone
- task: Report a spam text message (phone) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/how-recognize-and-report-spam-text-messages

**USER:**
I get fake package delivery texts. I don't know how to copy a text and send it to another number, and I don't use a computer. Is there another way to report them?

**ASSISTANT:**
Yes. You do not have to copy and forward the text. Please don't click any link in it.

1. Open the text in your messaging app and look for an option to **report junk or spam**.
2. You can also report it at **ReportFraud.ftc.gov**.
3. Ask your phone company about tools that block unwanted texts.

Real delivery companies don't ask for your account information by text. If you think a delivery might be real, contact the company using a phone number or website you know is real, not the one in the text.

## tr087-r
- scenario: already_acted | style: failure_recovery | specification: fully_specified | platform: phone
- task: Report a spam text message (phone) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/how-recognize-and-report-spam-text-messages

**USER:**
I tapped the link in a text that said my package was delayed. A page came up asking me to log in, so I closed it right away without typing anything. Did I do something bad?

**ASSISTANT:**
You did the right thing by closing it. Please don't open that link again, and don't reply to the text.

1. Don't type any information into that page if you open it again by accident.
2. If you think the package could be real, contact the company using a phone number or website you know is real, not the details in the text.
3. Forward the text to **7726** (SPAM), and report it at **ReportFraud.ftc.gov**.

Links in scam texts can lead to fake websites that look real, and some can install harmful software. Closing the page right away without typing anything is a good move.

## tr088-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: any
- task: Online friend asks for money (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/what-know-about-romance-scams

**USER:**
A man I met on a dating site wants me to move our chats to email, and now he says he needs money for a visa so he can visit me. He asked me not to tell my kids because they won't understand. I really do care about him. What should I do?

**ASSISTANT:**
Please don't send him any money. Never send money or gifts to someone you haven't met in person.

What you describe matches signs of a romance scam: asking to move off the site and asking for money, which is often framed as urgent.

1. Stop communicating with him right away.
2. Talk to a trusted friend or family member, including your kids, and listen if they voice concerns.
3. Do a reverse image search on his profile photo to see if it is linked to other names.
4. Report it at **ReportFraud.ftc.gov**, and tell the dating site.

I know this is hard when you care about someone.

## tr088-r
- scenario: already_acted | style: failure_recovery | specification: fully_specified | platform: any
- task: Online friend asks for money (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/what-know-about-romance-scams

**USER:**
I already sent $500 in gift cards to a man I met online. I read the PINs to him over the phone. Now he wants more. What do I do?

**ASSISTANT:**
Please don't send him anything more, and stop talking to him. 

1. Contact the gift card company right away. Tell them you paid a scammer and ask for a refund.
2. Report it at **ReportFraud.ftc.gov**.
3. Tell the site or app where you met him.
4. Talk to a trusted friend or family member about what happened.

Gift cards are one of the hard-to-reverse ways scammers ask for money, so acting quickly matters.

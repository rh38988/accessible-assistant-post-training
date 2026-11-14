# Review input: batch fx2, round 1 (32 examples)

## tr014-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: any
- task: Caller claims to be grandchild needing gift cards (any) | sensitive: True | reviewed by a person: False
- sources: https://www.ftc.gov/node/54353

**USER:**
I got a Facebook message from someone who says she is my granddaughter Emily. She wrote that she is stuck in another country, lost her bag, and needs me to wire her money today or she can't get home. The picture looks like her but the writing sounds a bit odd. I want to help her but I'm not sure. What should I do?

**ASSISTANT:**
I'm glad you stopped to ask. **Please don't wire any money yet.** Scammers often pretend to be a grandchild in trouble, and they push for payment right away.

1. Take a breath. You don't have to act right now, even if the story sounds dramatic.
2. Call Emily on a phone number **you know is really hers**. Don't use any number from the message.
3. Check the story with another trusted family member too.
4. Don't wire money, pay with a gift card, or send cash for an emergency request.

You can report the message at **www.ftc.gov/complaint**.

## tr014-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: any
- task: Caller claims to be grandchild needing gift cards (any) | sensitive: True | reviewed by a person: False
- sources: https://www.ftc.gov/node/54353

**USER:**
A man called saying he is my grandson Kevin and he was in a car accident. He said a lawyer will call me for the bail money, and he begged me not to tell his parents because they'd be so angry. His mother is traveling and I can't reach her right now. He says there's no time. Should I do what he asks?

**ASSISTANT:**
**Please don't send any money yet.** A caller who begs for secrecy and says there is no time is a common sign of a family emergency scam. A fake lawyer is another sign.

1. Hang up and take your time. There is no need to rush.
2. Call Kevin on a number **you know is genuine**.
3. If you can't reach his mother, check the story with **another trusted family member**, even though the caller asked you to keep it secret.
4. Don't wire money, pay with a gift card, or send cash.

## tr014-r
- scenario: already_acted | style: failure_recovery | specification: fully_specified | platform: any
- task: Caller claims to be grandchild needing gift cards (any) | sensitive: True | reviewed by a person: False
- sources: https://www.ftc.gov/node/54353

**USER:**
Oh no. I think I got scammed. A woman said my grandson was in jail and I mailed $1,500 cash to an address she gave me. Now I called my grandson's real number and he is fine. What do I do now?

**ASSISTANT:**
I'm sorry this happened. It is not your fault, and you did the right thing by calling your grandson.

1. **Don't send any more money**, even if the caller contacts you again.
2. Tell another trusted family member what happened so you have support.
3. Report it to the FTC at **www.ftc.gov/complaint**.

I don't have steps for getting the cash back. Reporting helps. Agree with your family that no one will ever call with an emergency request for wired money, gift cards, or cash.

## tr014-f
- scenario: helper | style: plain | specification: fully_specified | platform: any
- task: Caller claims to be grandchild needing gift cards (any) | sensitive: True | reviewed by a person: False
- sources: https://www.ftc.gov/node/54353

**USER:**
My mother is 84 and just told me someone called saying he was her grandson and needed money fast for bail. She hasn't sent anything but she is shaken. How can I help her?

**ASSISTANT:**
It's good she told you before sending anything. Here is how to help her.

1. Reassure her. These calls are built to make people panic, and the caller pushes for money right away.
2. Help her call her grandson on a number you know is genuine.
3. Check the story with another trusted family member, even if the caller asked for secrecy.
4. Remind her not to wire money, pay with a gift card, or send cash for an emergency request.
5. Report the call at **www.ftc.gov/complaint**.

It also helps to agree as a family that no one will ever call with an emergency request for wired money, gift card payment, or cash.

## tr014-g
- scenario: prevention | style: plain | specification: fully_specified | platform: any
- task: Caller claims to be grandchild needing gift cards (any) | sensitive: True | reviewed by a person: False
- sources: https://www.ftc.gov/node/54353

**USER:**
My friend was just fooled by a call from a fake grandchild. How can I tell if a call like that is a scam in the future?

**ASSISTANT:**
Here are the signs of this kind of scam:

1. The caller says they are a family member in an emergency, such as needing bail or medical care.
2. They say things like "I know I don't sound like myself" or "Don't tell Mom. Let's keep this our secret."
3. A doctor, lawyer, or police officer may be part of the story.
4. They want money **right away**, by wire, gift card, or cash.

What to do if it happens:
1. Don't act right away, however dramatic the story is.
2. Call your relative on a number you know is genuine.
3. Check with another trusted family member.

Agree with your family that no one will ever call with an emergency request for wired money, gift cards, or cash. You can report scams at **www.ftc.gov/complaint**.

## tr015-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: any
- task: Stranger asks for a verification code (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/node/84809

**USER:**
A woman phoned me saying she works in the fraud department at my bank and that someone is trying to take money out of my account. She was very polite and said she would text me a code to stop it, and I just need to read the code back to her. I'm worried about my savings. Is this real?

**ASSISTANT:**
**Please don't read her the code.** This is a known scam. Scammers pretend to be someone you trust and claim there is a problem with your account. With the code, they can log in and move your money.

1. Hang up. Don't argue with her.
2. Block the number.
3. If you're worried about your account, contact your bank directly. Use a number you trust, like the one on your statement or in your app. Don't use any number the caller gave you.
4. Report the call at **ReportFraud.ftc.gov**.

Remember that anyone who asks for your verification code is a scammer.

## tr015-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: any
- task: Stranger asks for a verification code (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/node/84809

**USER:**
A man keeps calling and texting me. He already knows my full name and the town I live in, and he sounds very kind. He says someone stole my identity and he'll help me fix it, but first I must tell him the code that was just texted to my phone. He knows so much about me that it must be real, right?

**ASSISTANT:**
**Please don't tell him the code.** Scammers often know details about you and sound sympathetic. That is part of how they earn your trust. Anyone who asks you for your verification code is a scammer.

1. Don't engage. Hang up and stop texting him.
2. Block his number.
3. If you're worried about your accounts, contact your bank, credit union, or investment advisor directly. Use a number you trust, such as the one on your statement or in your app.
4. Report him at **ReportFraud.ftc.gov**.

Never call back a number he gave you.

## tr015-r
- scenario: already_acted | style: failure_recovery | specification: fully_specified | platform: any
- task: Stranger asks for a verification code (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/node/84809

**USER:**
I already read a code to a man who said he was from my credit union. Right after, I got a bad feeling. What should I do?

**ASSISTANT:**
I'm sorry, and thank you for acting quickly. With a code, a scammer may be able to log in to your account, so contact your credit union right away.

1. Call your credit union directly. Use a number you trust, like the one on your statement or in your app.
2. Don't call back any number the man gave you. It would take you to the scammer.
3. Don't talk to him or text him again, and block his number.
4. Report it at **ReportFraud.ftc.gov**.

I don't have more specific steps than these, so your credit union is the best place to ask what else to do.

## tr015-f
- scenario: helper | style: plain | specification: fully_specified | platform: any
- task: Stranger asks for a verification code (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/node/84809

**USER:**
My dad is 79 and keeps getting texts and calls from people who say there is a problem with his accounts and ask for a code that gets sent to his phone. What should I tell him to do?

**ASSISTANT:**
It's good you're looking out for him. Here is what to tell him.

1. **Never give a verification code to anyone.** Anyone who asks for it is a scammer.
2. If someone asks, don't engage. Hang up, block the number, and stop texting.
3. If he is worried about an account, he should contact his bank, credit union, or investment advisor directly, using a number he trusts, like the one on his statement or in his app.
4. He should never use a number the caller gave him.
5. You can report the contacts at **ReportFraud.ftc.gov**.

If he already shared a code, he should contact his bank or credit union right away using a trusted number.

## tr015-g
- scenario: prevention | style: plain | specification: fully_specified | platform: any
- task: Stranger asks for a verification code (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/node/84809

**USER:**
How do these verification code scams work, and how can I stay safe from them?

**ASSISTANT:**
Here is how they work. Scammers pretend to be someone you trust and say there is a problem with an account or that your identity was stolen. They may know details about you and sound sympathetic. Then they ask for your verification code. With it, they can log in to your account and move money out of savings or investment accounts.

How to stay safe:

1. **Never give your verification code to anyone.**
2. Remember that anyone who asks for it is a scammer.
3. If someone asks, hang up, block the number, and stop texting.
4. If you're worried, contact your bank directly using a number on your statement or in your app.
5. Report it at **ReportFraud.ftc.gov**.

## tr016-d
- scenario: followup | style: plain | specification: fully_specified | platform: any
- task: Is it safe to pay online? (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/consumer-alerts/2026/07/way-spot-scams-how-someone-asks-you-pay

**USER:**
is it safe to pay for something online?

**ASSISTANT:**
It can be, but it depends on what you're buying, who you're buying from, and how they want you to be paid.

**What are you trying to buy, and how is the seller asking you to pay** (for example a credit card, a gift card, or a bank transfer)?

One quick tip while you check: if a seller says you can only pay with **gift cards, a wire transfer, or cryptocurrency**, stop. That's a common sign of a scam.

**USER:**
I'm buying a used lawn mower from a man on a website and he says I have to pay with a gift card.

**ASSISTANT:**
**Please don't pay with a gift card.** When someone says gift card is the only way to pay, that is a sign of a scam. The same goes for a bank transfer, wire transfer, cryptocurrency, or a payment app.

1. Don't send money to anyone who says you can only pay one specific way, whatever reason they give.
2. Search online for the seller's name with words like "review," "scam," or "complaint" and see what others say.
3. If you decide to buy, pay by **credit card** whenever possible. It has more protections and lets you dispute charges.

You can report a seller like this at **ReportFraud.ftc.gov**.

## tr016-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: any
- task: Is it safe to pay online? (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/consumer-alerts/2026/07/way-spot-scams-how-someone-asks-you-pay

**USER:**
I found a beautiful rocking chair on a website I've never heard of, and the price is half what stores charge. They only accept cryptocurrency and say it's because of fees. My nephew says no but I really want it. Is it safe to pay them that way?

**ASSISTANT:**
**Please don't pay with cryptocurrency.** When a seller says that is the only way to pay, it is probably a scam, whatever reason they give.

1. Don't send money to anyone who says you can only pay one specific way.
2. Search online for the website's name with words like "review," "scam," or "complaint."
3. If the seller accepts a **credit card**, that is safer. Credit cards have more protections and let you dispute charges.

Your nephew is right to be careful. If you want to report the website, you can do that at **ReportFraud.ftc.gov**.

## tr016-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: any
- task: Is it safe to pay online? (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/consumer-alerts/2026/07/way-spot-scams-how-someone-asks-you-pay

**USER:**
I don't have a credit card, only a debit card and some cash. A person selling concert tickets online says they only take a payment app like Zelle, and that tickets are going fast. Is that okay? I really can't use a credit card.

**ASSISTANT:**
**Please be careful.** When a seller says a payment app is the only way to pay, that is a warning sign of a scam.

1. Don't send money to anyone who says you can only pay one specific way, whatever reason they give.
2. Search online for the seller's name with words like "review," "scam," or "complaint."
3. Paying by credit card is safest, because it lets you dispute charges. I don't have advice on other payment methods, so if you can't use a credit card, it's safer to skip a seller who insists on a payment app.

For more tips, you can visit **ftc.gov/scams**.

## tr016-r
- scenario: already_acted | style: failure_recovery | specification: fully_specified | platform: any
- task: Is it safe to pay online? (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/consumer-alerts/2026/07/way-spot-scams-how-someone-asks-you-pay

**USER:**
I already paid. A seller told me to wire money for a puppy and now they've stopped answering. What can I do?

**ASSISTANT:**
I'm sorry. Act quickly, because the sooner you do, the better.

1. Contact the company you used to send the wire right away.
2. Tell them it was fraud.
3. Ask whether they can stop or reverse the transaction and return your money.
4. Report the seller at **ReportFraud.ftc.gov**.

I don't have steps that are specific to wire transfers beyond these.

## tr016-g
- scenario: prevention | style: plain | specification: fully_specified | platform: any
- task: Is it safe to pay online? (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/consumer-alerts/2026/07/way-spot-scams-how-someone-asks-you-pay

**USER:**
What are the warning signs that someone is trying to scam me when I buy things online?

**ASSISTANT:**
The biggest warning sign is how they ask you to pay.

1. If someone says the **only** way to pay is a bank transfer, wire transfer, cryptocurrency, payment app, or gift card, it is probably a scam.
2. Never send money to anyone who says you can only pay one specific way, whatever reason they give.
3. Check the seller. Search online for the name with words like "review," "scam," or "complaint."
4. Pay by **credit card** whenever possible. It has more protections and lets you dispute charges.

If you already paid a scammer, contact the company you used to send the money right away, tell them it was fraud, and ask if they can stop or reverse it. You can report scams at **ReportFraud.ftc.gov**.

## tr021-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: Make text bigger (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102453

**USER:**
I already made the text bigger on my iPhone using the slider in Display & Brightness, but my eyes are bad and it still isn't big enough. That slider is at the end. Is there any way to get the words even larger?

**ASSISTANT:**
Yes, there is a separate setting for larger sizes.

1. Open the **Settings** app.
2. Tap **Accessibility**.
3. Tap **Display & Text Size**.
4. Tap **Larger Text**.
5. Drag the slider to the size you want.

The larger sizes work in apps like Mail, Contacts, Calendar, Phone, and Notes. Very large text can make some buttons hard to tap. If that happens, come back to the same screen and slide it down a little.

## tr022-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Android (Pixel)
- task: Make text bigger (Android (Pixel)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/accessibility/android/answer/11183305?hl=en

**USER:**
I have a Pixel phone and I like to change the text size depending on whether I'm wearing my glasses. I don't want to dig through Settings every single time. Is there a quicker way to switch the size?

**ASSISTANT:**
Yes. Once it is set up, the quick way is the top of the screen. Set it up first in Settings.

1. Open the **Settings** app.
2. Search for **Font size** and tap it.
3. Move the slider once. This adds a **Font Size** tile to Quick Settings.

From then on:

1. Swipe down from the top of the screen to open Quick Settings.
2. Tap **Font Size**.
3. Tap **Increase** or **Decrease**, or drag the percentage slider.

Font size can go up to 200%.

## tr022-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Android (Pixel)
- task: Make text bigger (Android (Pixel)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/accessibility/android/answer/11183305?hl=en

**USER:**
My Pixel's text is too small to read. How do I make it bigger?

**ASSISTANT:**
You can make it bigger in Settings. It takes about a minute.

1. Open the **Settings** app.
2. Search for **Font size** and tap it.
3. Move the slider toward the larger end.

You will see a preview of the new size. A few apps ignore this setting, so text in them may stay the same.

**USER:**
I slid it all the way and now it is way too big and I can't even read the screen. How do I go back?

**ASSISTANT:**
You can put it back to the way it was.

1. Open **Settings**.
2. Search for **Font size** and tap it.
3. Tap **Reset settings** to return to the phone's default size.

Or move the slider back toward the smaller end a little at a time until it is comfortable.

## tr024-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: Turn up ringer volume (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/105103

**USER:**
Every time I press the volume up button on my iPhone it only makes my YouTube videos louder, not the phone ringing. I'm usually watching videos when my daughter calls. I want the ringer louder, not the videos. How do I do that?

**ASSISTANT:**
That happens because the volume buttons change **media volume** while you are watching videos, listening to music, or playing games. They change the ringer volume only when you aren't using other apps.

1. Close the video app and go to your Home Screen, so no other app is in use.
2. Press the **volume up** button on the side of the phone a few times.

Now the buttons raise the ringer volume. If your phone still only vibrates when someone calls, it may be in Silent mode. Tell me and I'll show you how to check.

## tr024-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: Turn up ringer volume (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/105103

**USER:**
Can you tell me how to make my iPhone ringer louder?

**ASSISTANT:**
Yes, you can use the volume buttons. It takes a few seconds.

1. Go to your Home Screen so you are not inside another app.
2. Press the **volume up** button on the side of the phone a few times.

When no other app is in use, these buttons change the ringer volume. If your phone only vibrates, it may be in Silent mode. Tell me and I'll show you how to check.

**USER:**
I did that but it still only buzzes when someone calls. I see something orange on the side of the phone.

**ASSISTANT:**
The orange means your iPhone is in **Silent mode**. In Silent mode it vibrates for calls instead of ringing.

1. Find the small **Ring/Silent switch** above the volume buttons.
2. Flip it so the orange is no longer showing.
3. Press the **volume up** button a few times.

If you have an iPhone 15 Pro or a newer model, there is no switch. The **Action button** toggles Silent mode by default. Calls from your favorite contacts still ring in Silent mode.

## tr025-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Android
- task: Turn up ring volume (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9082609?hl=en

**USER:**
My Android phone is quite old and I can't update it. When I press the volume button I only see a little slider with a small arrow, no menu thing. How do I make the ring louder on an older phone like that?

**ASSISTANT:**
On older Android phones you use the small arrow.

1. Press a **volume button** on the side of the phone.
2. Tap the **Down arrow** that appears next to the slider.
3. Find **Ring** in the list.
4. Slide it to the right to make the ring louder.

The Down arrow is where older versions show Media, Ring, and Alarm.

## tr025-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Android
- task: Turn up ring volume (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9082609?hl=en

**USER:**
Please show me how to make my Android phone ring louder.

**ASSISTANT:**
You can do this with the volume buttons. It takes a few seconds.

1. Press a **volume button** on the side of the phone.
2. Tap the **Menu** icon on the right side of the volume panel.
3. Find the **Ring Volume** slider and slide it to the right.

If you don't see the **Menu** icon, tell me what you see and I'll help you find it.

**USER:**
I pressed the button but there is no menu icon. I only see a small arrow pointing down.

**ASSISTANT:**
That's normal on older Android versions. Use the arrow instead.

1. Press a **volume button** again.
2. Tap the **Down arrow**.
3. Choose **Ring**.
4. Slide it to the right to make it louder.

## tr026-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: Turn on Wi-Fi Calling (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108066

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

## tr026-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: Turn on Wi-Fi Calling (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108066

**USER:**
I want my iPhone to use my home Wi-Fi for phone calls because the signal here is poor. How do I set that up?

**ASSISTANT:**
You can turn on **Wi-Fi Calling**. It takes about a minute.

1. Open the **Settings** app.
2. Tap **Cellular**.
3. Tap **Wi-Fi Calling**.
4. Turn on **Wi-Fi Calling on This iPhone**.
5. Tap **Enable**.

You may be asked to enter or confirm an address for emergency services. Your carrier must offer Wi-Fi Calling.

**USER:**
I tried but I can't get it to turn on.

**ASSISTANT:**
Let's check the basics first.

1. Make sure your carrier offers Wi-Fi Calling.
2. Make sure your iPhone software is up to date.
3. If it still won't turn on, contact your carrier.
4. If your carrier can't fix it, restart your iPhone, try a different Wi-Fi network, and then turn Wi-Fi Calling off and on again.

Some Wi-Fi networks don't work with Wi-Fi Calling.

## tr027-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Android
- task: Take a screenshot (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9075928?hl=en

**USER:**
I have arthritis in my hands and I can't press two buttons at the same time on my Android phone. My daughter asked me to send her a picture of an error message. Is there another way to take a screenshot?

**ASSISTANT:**
Yes, you can do it with one button.

1. Open the screen you want to capture.
2. Press and hold the **Power** button for a few seconds.
3. Tap **Screenshot**.

You will see a small preview at the bottom left of the screen. If **Screenshot** doesn't appear, check your phone maker's support site.

## tr027-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Android
- task: Take a screenshot (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9075928?hl=en

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

## tr028-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Windows 11
- task: Take a screenshot (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/apps/use-snipping-tool-to-capture-screenshots

**USER:**
I'm on a Windows 11 computer and want to send my doctor's office a picture of just one box on a web page. I don't want the whole screen, because my email inbox is open too and I don't want them to see it. How can I capture only that box?

**ASSISTANT:**
You can use **Snipping Tool** to capture just one part of the screen.

1. Select **Start**, type **snipping tool**, then select **Snipping Tool**.
2. Select **Snipping Mode**, then choose **Rectangle**.
3. Select **New**.
4. Drag a rectangle around the box you want.

The snip saves automatically to your **Screenshots** folder. A faster way next time is to press the **Windows logo key + Shift + S**, which opens the snip overlay.

## tr028-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Windows 11
- task: Take a screenshot (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/apps/use-snipping-tool-to-capture-screenshots

**USER:**
How can I take a picture of my whole screen on my Windows 11 computer?

**ASSISTANT:**
You can use **Snipping Tool**.

1. Select **Start**, type **snipping tool**, then select **Snipping Tool**.
2. Select **Snipping Mode**, then choose **Full screen**.
3. Select **New**.

It captures the whole screen right away.

**USER:**
OK it took the picture but I can't tell where it went. How do I find it?

**ASSISTANT:**
Snips are saved automatically in your **Screenshots** folder.

1. Look in your **Screenshots** folder.
2. If you want another copy somewhere else, select **Save as** in Snipping Tool, choose a location and a name, then select **Save**.

To change where snips are saved, select **See More** in Snipping Tool, then **Settings**.

## tr030-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Android
- task: Connect to a Wi-Fi network (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9075847?hl=en

**USER:**
My son set up our Wi-Fi at the new apartment and hid the network, so it doesn't show up in the list on my Android phone. He told me the name and password. How do I connect to a network that isn't listed?

**ASSISTANT:**
You can add it yourself.

1. Open the **Settings** app.
2. Tap **Network & internet**, then **Internet**.
3. At the bottom of the list, tap **Add network**.
4. Type the network name your son gave you.
5. Enter the security details if asked.
6. Tap **Advanced options**, and under **Hidden Network** select **Yes**.
7. Tap **Save**.

Once connected, the network is labeled **Saved**, and your phone joins it automatically when you're nearby.

## tr030-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Android
- task: Connect to a Wi-Fi network (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9075847?hl=en

**USER:**
I'm at my sister's house with an Android phone. How do I get on her Wi-Fi?

**ASSISTANT:**
Here is how.

1. Open the **Settings** app.
2. Tap **Network & internet**, then **Internet**.
3. Tap your sister's network in the list. A lock icon means it needs a password.
4. Enter the password if asked.

When you're connected, the network shows as **Saved**.

**USER:**
I don't see her network in the list at all.

**ASSISTANT:**
Try this.

1. Wait a few seconds for the list to reload.
2. If it still isn't there, her network may be hidden. Ask her for the network name, then at the bottom of the list tap **Add network** and enter the name.
3. Tap **Save**.

## tr031-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Windows 11
- task: Connect to a Wi-Fi network (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/experience/connectivity-networking/connect-to-a-wi-fi-network-in-windows

**USER:**
I'm visiting my daughter with my Windows 11 laptop and she hasn't given me her Wi-Fi password yet because she's out. Can I get my laptop connected to her network before she gets home?

**ASSISTANT:**
You can get everything ready, but joining her network needs the password. Without it, you can't finish.

1. Select the **Network**, **Sound**, or **Battery** icons on the taskbar.
2. In the Wi-Fi quick setting, select **Manage Wi-Fi connections**.
3. Choose her network and select **Connect**.
4. When it asks for the password, enter it and select **Next**.

When she gets home, ask her for the password and finish at step 4.

## tr031-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Windows 11
- task: Connect to a Wi-Fi network (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/experience/connectivity-networking/connect-to-a-wi-fi-network-in-windows

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

# Rule scan input, part 08 (50 examples)

## tr084-r
- task: Make the mouse pointer bigger | platform: Windows 11 | scenario: failure_recovery | sensitive: False
- sources: Microsoft Support: Make Windows easier to see <https://support.microsoft.com/en-us/accessibility/windows/make-windows-easier-to-see>

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

---

## tr085-a
- task: Turn on 2-Step Verification | platform: Google Account | scenario: direct | sensitive: True
- sources: Google Account Help: Turn on 2-Step Verification (computer) <https://support.google.com/accounts/answer/185839?hl=en&co=GENIE.Platform%3DDesktop>; Google Account Help: How to recover your Google Account or Gmail <https://support.google.com/accounts/answer/7682439?hl=en>

**USER:**
How do I turn on 2-Step Verification for my Google account on my computer?

**ASSISTANT:**
2-Step Verification adds a second check when you sign in, so a password alone isn't enough to get into your account.

1. Go to **myaccount.google.com** and sign in.
2. Click **Security & sign-in**.
3. Under **How you sign in to Google**, click **Turn on 2-Step Verification**.
4. Follow the steps on the screen.

After it's on, when you sign in Google will ask for a second step as well as your password, such as tapping Yes on a prompt on your phone.

**Never share a verification code with anyone.** Google will not call you to ask for one.

If you use a work or school account, your administrator may control this setting.

---

## tr085-b
- task: Turn on 2-Step Verification | platform: Google Account | scenario: missing_info | sensitive: True
- sources: Google Account Help: Turn on 2-Step Verification (computer) <https://support.google.com/accounts/answer/185839?hl=en&co=GENIE.Platform%3DDesktop>; Google Account Help: How to recover your Google Account or Gmail <https://support.google.com/accounts/answer/7682439?hl=en>

**USER:**
how do I make my email account more secure

**ASSISTANT:**
Good question. Which email do you use, for example **Gmail**, **Outlook**, or **Yahoo**?

---

## tr085-c
- task: Turn on 2-Step Verification | platform: Google Account | scenario: missing_info | sensitive: True
- sources: Google Account Help: Turn on 2-Step Verification (computer) <https://support.google.com/accounts/answer/185839?hl=en&co=GENIE.Platform%3DDesktop>; Google Account Help: How to recover your Google Account or Gmail <https://support.google.com/accounts/answer/7682439?hl=en>

**USER:**
My friend's email got hacked and sent everyone weird links. Her son told her to turn on two step something. I want to do that too so it doesn't happen to me.

**ASSISTANT:**
That's a smart idea. It's called **2-Step Verification**, and most email services offer it.

**Which email do you use**, for example Gmail, Yahoo, or Outlook?

---

## tr085-d
- task: Turn on 2-Step Verification | platform: Google Account | scenario: followup | sensitive: True
- sources: Google Account Help: Turn on 2-Step Verification (computer) <https://support.google.com/accounts/answer/185839?hl=en&co=GENIE.Platform%3DDesktop>; Google Account Help: How to recover your Google Account or Gmail <https://support.google.com/accounts/answer/7682439?hl=en>

**USER:**
how do I make my email account more secure

**ASSISTANT:**
Good question. Which email do you use, for example **Gmail**, **Outlook**, or **Yahoo**?

**USER:**
Gmail, on my computer

**ASSISTANT:**
Thanks. A strong next step for Gmail is turning on 2-Step Verification.

2-Step Verification adds a second check when you sign in, so a password alone isn't enough to get into your account.

1. Go to **myaccount.google.com** and sign in.
2. Click **Security & sign-in**.
3. Under **How you sign in to Google**, click **Turn on 2-Step Verification**.
4. Follow the steps on the screen.

After it's on, when you sign in Google will ask for a second step as well as your password, such as tapping Yes on a prompt on your phone.

**Never share a verification code with anyone.** Google will not call you to ask for one.

If you use a work or school account, your administrator may control this setting.

---

## tr085-e
- task: Turn on 2-Step Verification | platform: Google Account | scenario: constraint | sensitive: True
- sources: Google Account Help: Turn on 2-Step Verification <https://support.google.com/accounts/answer/185839?hl=en&co=GENIE.Platform%3DDesktop>

**USER:**
I want to turn on 2-Step Verification for my Google account on my home computer. Only I use this computer, and I get tired of typing codes, so I don't want to be asked every single time I sign in here. What should I do?

**ASSISTANT:**
You can turn it on and tell Google not to ask again on your own computer.

1. Go to **myaccount.google.com** on your computer and sign in.
2. Select **Security & sign-in**.
3. Under **How you sign in to Google**, select **Turn on 2-Step Verification**.
4. Follow the steps on the screen.

When you are asked for a second step, check **Don't ask again on this computer**. Only do that on a computer you use regularly and don't share with anyone, like your home computer.

---

## tr085-r
- task: Turn on 2-Step Verification | platform: Google Account | scenario: failure_recovery | sensitive: True
- sources: Google Account Help: Turn on 2-Step Verification <https://support.google.com/accounts/answer/185839?hl=en&co=GENIE.Platform%3DDesktop>

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

---

## tr086-b
- task: Is this email asking me to log in real? | platform: email | scenario: missing_info | sensitive: True
- sources: FTC Consumer Advice: How To Recognize and Avoid Phishing Scams <https://consumer.ftc.gov/articles/how-recognize-avoid-phishing-scams>

**USER:**
I got a weird email, should I click on it?

**ASSISTANT:**
Good thinking to check first. Please don't click anything yet. **Who does the email say it's from?**

---

## tr087-b
- task: Report a spam text message | platform: phone | scenario: missing_info | sensitive: True
- sources: FTC Consumer Advice: How to Recognize and Report Spam Text Messages <https://consumer.ftc.gov/articles/how-recognize-and-report-spam-text-messages>

**USER:**
what do I do about junk texts

**ASSISTANT:**
There are a couple of things you can do about junk texts. Is your phone an **iPhone** or an **Android** phone?

---

## tr087-e
- task: Report a spam text message | platform: phone | scenario: constraint | sensitive: True
- sources: FTC Consumer Advice: How to Recognize and Report Spam Text Messages <https://consumer.ftc.gov/articles/how-recognize-and-report-spam-text-messages>

**USER:**
I get fake package delivery texts. I don't know how to copy a text and send it to another number, and I don't use a computer. Is there another way to report them?

**ASSISTANT:**
Yes. You do not have to copy and forward the text. Please don't click any link in it.

1. Open the text in your messaging app and look for an option to **report junk or spam**.
2. If you are able to open web pages on your phone, you can also report it at **ReportFraud.ftc.gov**.
3. Ask your phone company about tools that block unwanted texts.

Real delivery companies don't ask for your account information by text. If you think a delivery might be real, contact the company using a phone number or website you know is real, not the one in the text.

---

## tr087-r
- task: Report a spam text message | platform: phone | scenario: already_acted | sensitive: True
- sources: FTC Consumer Advice: How to Recognize and Report Spam Text Messages <https://consumer.ftc.gov/articles/how-recognize-and-report-spam-text-messages>

**USER:**
I tapped the link in a text that said my package was delayed. A page came up asking me to log in, so I closed it right away without typing anything. Did I do something bad?

**ASSISTANT:**
You did the right thing by closing it. Please don't open that link again.

1. Don't type any information into that page if you open it again by accident.
2. If you think the package could be real, contact the company using a phone number or website you know is real, not the details in the text.
3. Forward the text to **7726** (SPAM), and report it at **ReportFraud.ftc.gov**.

Links in scam texts can lead to fake websites that look real, and some can install harmful software. Closing the page right away without typing anything is a good move.

---

## tr088-a
- task: Online friend asks for money | platform: any | scenario: direct | sensitive: True
- sources: FTC Consumer Advice: What To Know About Romance Scams <https://consumer.ftc.gov/articles/what-know-about-romance-scams>

**USER:**
I met a man online three months ago. He says he loves me, he works on an oil rig overseas, and now he needs $2,000 for a plane ticket to come see me. Should I send it?

**ASSISTANT:**
I'm glad you asked before sending anything. Please **don't send the money**. What you're describing matches a very common scam called a **romance scam**.

**Warning signs:**
- The person can't meet in person, often saying they work far away, like on an **oil rig** or in the military.
- Strong feelings grow quickly through lots of messages.
- Now there's a **need for money**, like travel costs or an emergency.

**What to do:**
1. **Don't send money or gift cards** to someone you haven't met in person.
2. **Talk to a friend or family member** you trust. People close to you can often spot things that are hard to see from the inside.
3. You can **search his photo** online to see if it appears under other names. I can show you how.
4. If it's a scam, stop contact and report it at **ReportFraud.ftc.gov** and to the website or app where you met.

If you've already sent money, contact your bank or the payment company right away and ask for a refund.

---

## tr088-b
- task: Online friend asks for money | platform: any | scenario: missing_info | sensitive: True
- sources: FTC Consumer Advice: What To Know About Romance Scams <https://consumer.ftc.gov/articles/what-know-about-romance-scams>

**USER:**
my online friend needs money for an emergency, should I help?

**ASSISTANT:**
I'm glad you asked first. Please don't send any money or gift cards yet. **Have you met this person in person?**

---

## tr088-r
- task: Online friend asks for money | platform: any | scenario: already_acted | sensitive: True
- sources: FTC Consumer Advice: What You Need to Know About Romance Scams <https://consumer.ftc.gov/articles/what-know-about-romance-scams>

**USER:**
I already sent $500 in gift cards to a man I met online. I read the PINs to him over the phone. Now he wants more. What do I do?

**ASSISTANT:**
Please don't send him anything more, and stop talking to him. 

1. Contact the gift card company right away. Tell them you paid a scammer and ask for a refund.
2. Report it at **ReportFraud.ftc.gov**.
3. Tell the site or app where you met him.
4. Talk to a trusted friend or family member about what happened.

Gift cards are one of the hard-to-reverse ways scammers ask for money, so acting quickly matters.

---

## tr089-a
- task: Caller claims to be from Social Security | platform: phone | scenario: direct | sensitive: True
- sources: FTC Consumer Advice: How To Avoid a Government Impersonation Scam <https://consumer.ftc.gov/articles/how-avoid-government-impersonation-scam>

**USER:**
A caller said he's from Social Security and my number has been suspended because of a crime. He wants me to buy gift cards to fix it. What should I do?

**ASSISTANT:**
Please **hang up and don't pay anything**. This is a scam. The real Social Security Administration **won't threaten you, won't suspend your Social Security number, and won't ask you to pay with gift cards**.

**What to do:**
1. **Hang up.** Don't share any personal or bank information.
2. Don't trust caller ID. Scammers can make it show a government name or number.
3. If you're worried, **call Social Security yourself** using the phone number on its official website, not a number the caller gave you.
4. **Report the call** to the Social Security Administration's Office of the Inspector General and to the FTC at **ReportFraud.ftc.gov**.

If you already shared your Social Security number or bank details, go to **IdentityTheft.gov** for next steps, and tell me so I can help.

---

## tr089-b
- task: Caller claims to be from Social Security | platform: phone | scenario: missing_info | sensitive: True
- sources: FTC Consumer Advice: How To Avoid a Government Impersonation Scam <https://consumer.ftc.gov/articles/how-avoid-government-impersonation-scam>

**USER:**
Got a call from the government saying I owe money. Is that real?

**ASSISTANT:**
Please don't pay or share any personal information yet, and don't call back any number they gave you. **Which agency did the caller say they were from?**

---

## tr089-c
- task: Caller claims to be from Social Security | platform: phone | scenario: missing_info | sensitive: True
- sources: FTC Consumer Advice: How To Avoid a Government Impersonation Scam <https://consumer.ftc.gov/articles/how-avoid-government-impersonation-scam>

**USER:**
social security called me

**ASSISTANT:**
Okay, let's make sure it was really them. Until we know, please don't give them any money or personal information.

**Did the caller ask you for money or personal information?**

---

## tr089-d
- task: Caller claims to be from Social Security | platform: phone | scenario: followup | sensitive: True
- sources: FTC Consumer Advice: How To Avoid a Government Impersonation Scam <https://consumer.ftc.gov/articles/how-avoid-government-impersonation-scam>

**USER:**
Got a call from the government saying I owe money. Is that real?

**ASSISTANT:**
Please don't pay or share any personal information yet, and don't call back any number they gave you. **Which agency did the caller say they were from?**

**USER:**
Social Security. They said I need to buy gift cards or my number will be suspended.

**ASSISTANT:**
Thank you.

Please **hang up and don't pay anything**. This is a scam. The real Social Security Administration **won't threaten you, won't suspend your Social Security number, and won't ask you to pay with gift cards**.

**What to do:**
1. **Hang up.** Don't share any personal or bank information.
2. Don't trust caller ID. Scammers can make it show a government name or number.
3. If you're worried, **call Social Security yourself** using the phone number on its official website, not a number the caller gave you.
4. **Report the call** to the Social Security Administration's Office of the Inspector General and to the FTC at **ReportFraud.ftc.gov**.

If you already shared your Social Security number or bank details, go to **IdentityTheft.gov** for next steps, and tell me so I can help.

---

## tr089-e
- task: Caller claims to be from Social Security | platform: phone | scenario: constraint | sensitive: True
- sources: FTC Consumer Advice: How To Avoid a Government Impersonation Scam <https://consumer.ftc.gov/articles/how-avoid-government-impersonation-scam>

**USER:**
A man phoned and said he is with Social Security and my number is tied to fraud. He knew my name and my street address. He told me I must not tell my family or I could be arrested, and my caller ID really did say Social Security. He is going to call me back in an hour. Is this real?

**ASSISTANT:**
Please **do not give him anything**, and hang up if he calls again. This is a scam. The real Social Security Administration **won't threaten you** or suspend your Social Security number. Knowing your name and address, threats of arrest, and a real-looking caller ID are all tricks scammers use. Caller ID can be faked.

1. When he calls back, **hang up**. Don't share personal or bank information.
2. Don't call back the number he gave you or the one on your caller ID.
3. If you are worried, **call your local Social Security office yourself**. You can find the number at **secure.ssa.gov/ICON/main.jsp**.
4. **Report the call** at **reportfraud.ftc.gov**, and to the Social Security Office of the Inspector General at **oig.ssa.gov**.

---

## tr089-r
- task: Caller claims to be from Social Security | platform: phone | scenario: already_acted | sensitive: True
- sources: FTC Consumer Advice: How To Avoid a Government Impersonation Scam <https://consumer.ftc.gov/articles/how-avoid-government-impersonation-scam>

**USER:**
I feel so silly. A woman from Social Security said my number was being suspended, and I told her my Social Security number and my birthday before I got suspicious and hung up. What do I do now?

**ASSISTANT:**
Please don't feel silly. These callers are good at sounding real, and you did the right thing by hanging up. Here is what to do now.

1. Go to **IdentityTheft.gov** for steps to protect your identity.
2. **Report the call** to the FTC at **reportfraud.ftc.gov**.
3. Also report it to the Social Security Office of the Inspector General at **oig.ssa.gov**, and to your state attorney general.

If she calls again, hang up and don't call back the number she used. If you ever want to check on your account, call your local Social Security office using a number you find yourself.

---

## tr090-b
- task: Make a strong password | platform: any | scenario: missing_info | sensitive: True
- sources: FTC Consumer Advice: Creating Strong Passwords and Other Ways To Protect Your Accounts <https://consumer.ftc.gov/articles/creating-strong-passwords-and-other-ways-protect-your-accounts>

**USER:**
Can you help me with my passwords?

**ASSISTANT:**
Of course. What would you like help with: **making a strong new password**, **keeping track of the ones you have**, or **resetting one you forgot**?

---

## tr090-e
- task: Make a strong password | platform: any | scenario: constraint | sensitive: True
- sources: FTC Consumer Advice: Creating Strong Passwords and Other Ways To Protect Your Accounts <https://consumer.ftc.gov/articles/creating-strong-passwords-and-other-ways-protect-your-accounts>

**USER:**
I'm making a new password for my insurance company's website and it keeps rejecting my long phrase of words because it has a length limit. I also don't trust password manager programs and don't want one. How can I still make a strong password?

**ASSISTANT:**
You can still make a strong one without a password manager. When a site rejects long passwords, **mix different kinds of characters** instead.

1. Use **uppercase and lowercase letters**, **numbers**, and **symbols** together.
2. Make it as long as the site allows. Aim for at least 12 characters if you can.
3. Don't use a common phrase, song lyric, or movie quote.

Your **email** password matters most, because password reset links often go to your email inbox.

---

## tr090-r
- task: Make a strong password | platform: any | scenario: already_acted | sensitive: True
- sources: FTC Consumer Advice: Creating Strong Passwords and Other Ways To Protect Your Accounts <https://consumer.ftc.gov/articles/creating-strong-passwords-and-other-ways-protect-your-accounts>

**USER:**
An online store emailed me that it lost its customers' passwords in a data breach. I use the same password for that store and for my email and my bank. What should I do?

**ASSISTANT:**
Please **change your password right away**, starting with the store. Then do the other two, since you used the same one.

1. At the store, **create a new strong password**. Make it long, at least 12 characters. Several random words work well.
2. Change the password on your **email** and your **bank** account too, since they share the old one.
3. If you see that someone is using your personal information, get help at **IdentityTheft.gov**.

Email is the most important one to protect, because password reset links often go there.

---

## tr091-b
- task: Get directions | platform: Google Maps (phone) | scenario: missing_info | sensitive: False
- sources: Google Maps Help: Get directions & show routes (Android) <https://support.google.com/maps/answer/144339?hl=en&co=GENIE.Platform%3DAndroid>

**USER:**
how do I find my way to a new place

**ASSISTANT:**
I can help. Is your phone an **iPhone** or an **Android** phone?

---

## tr091-c
- task: Get directions | platform: Google Maps (phone) | scenario: missing_info | sensitive: False
- sources: Google Maps Help: Get directions & show routes (Android) <https://support.google.com/maps/answer/144339?hl=en&co=GENIE.Platform%3DAndroid>

**USER:**
directions to

**ASSISTANT:**
It looks like your message got cut off. Are you using an **iPhone** or an **Android** phone?

---

## tr091-e
- task: Get directions | platform: Google Maps (phone) | scenario: constraint | sensitive: False
- sources: Google Maps Help: Get directions & show routes (Android) <https://support.google.com/maps/answer/144339?hl=en&co=GENIE.Platform%3DAndroid>

**USER:**
I'm driving to my sister's house tomorrow with my Android phone and I use Google Maps. I have to pick up a prescription at the pharmacy on the way, so I can't just go straight there. Can Maps take me to the pharmacy first and then my sister's?

**ASSISTANT:**
Yes. You can add the pharmacy as a stop on the way.

1. Open the **Google Maps** app.
2. Search for your sister's address and tap it.
3. At the bottom left, tap **Directions**.
4. Choose **Driving**.
5. At the top right, tap **More**, then tap **Edit stops**.
6. Search for the pharmacy along your route and add it as a stop. You can add up to 9 stops, including the final destination.
7. If the pharmacy is listed after your sister's house, press and hold the **Reorder** icon next to it and drag it above.
8. Tap **Done**.

Maps will show the route with your stop in it. The best route is **blue** and other routes are gray.

---

## tr091-r
- task: Get directions | platform: Google Maps (phone) | scenario: failure_recovery | sensitive: False
- sources: Google Maps Help: Get directions & show routes (Android) <https://support.google.com/maps/answer/144339?hl=en&co=GENIE.Platform%3DAndroid>

**USER:**
Using Google Maps on my Android phone, how do I get walking directions to the library downtown?

**ASSISTANT:**
Here is how.

1. Open the **Google Maps** app.
2. Search for the library, or tap it on the map.
3. At the bottom left, tap **Directions**.
4. Choose **Walking**.
5. Tap a route on the map to pick it. The best route is **blue** and the others are gray.
6. Swipe up on the route information to see a list of turns.

To see a turn-by-turn preview, tap **Preview**.

**USER:**
I did all that but it only shows me a preview and won't start guiding me. What's wrong?

**ASSISTANT:**
Navigation only starts when your starting point is **your location**. Otherwise it only shows a preview.

1. Look at the starting point at the top of the screen. If it shows some other place, tap it and change it to **your location**.
2. Then try again.

---

## tr093-a
- task: Join a Zoom meeting from a link | platform: Zoom | scenario: direct | sensitive: False
- sources: Zoom Support: Joining a meeting with the invite link <https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0065180>

**USER:**
My book club meets on Zoom now and they emailed me a link. How do I join from my computer?

**ASSISTANT:**
Joining with a link is pretty simple.

1. Open the email and **click the Zoom link**.
2. Your web browser opens a page, and a small box (pop-up) asks whether you want to open **Zoom Meetings**.
3. Click **Open**. Depending on your browser, the button may read **Allow** or **Open zoom.us**.
4. The Zoom app will open and take you into the meeting.

If the link already includes the passcode, you won't need to type one.

If Zoom doesn't open, or you don't have the Zoom app yet, tell me what you see on the screen and I'll help.

---

## tr093-b
- task: Join a Zoom meeting from a link | platform: Zoom | scenario: missing_info | sensitive: False
- sources: Zoom Support: Joining a meeting with the invite link <https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0065180>

**USER:**
how do I get on a zoom call

**ASSISTANT:**
Happy to help. Did someone send you a **link** to the meeting, in an email or a text?

---

## tr093-c
- task: Join a Zoom meeting from a link | platform: Zoom | scenario: direct_messy | sensitive: False
- sources: Zoom Support: Joining a meeting with the invite link <https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0065180>

**USER:**
Since my knees got bad I can't drive to my book club anymore, so the ladies started doing it on Zoom. My friend emailed me the link for Thursday but I've never done a Zoom before and I'm nervous I'll mess it up.

**ASSISTANT:**
You won't mess it up, and it's lovely that your book club found a way to keep you in. Here's what to do on Thursday:

Joining with a link is pretty simple.

1. Open the email and **click the Zoom link**.
2. Your web browser opens a page, and a small box (pop-up) asks whether you want to open **Zoom Meetings**.
3. Click **Open**. Depending on your browser, the button may read **Allow** or **Open zoom.us**.
4. The Zoom app will open and take you into the meeting.

If the link already includes the passcode, you won't need to type one.

If Zoom doesn't open, or you don't have the Zoom app yet, tell me what you see on the screen and I'll help.

---

## tr093-d
- task: Join a Zoom meeting from a link | platform: Zoom | scenario: followup | sensitive: False
- sources: Zoom Support: Joining a meeting with the invite link <https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0065180>

**USER:**
how do I get on a zoom call

**ASSISTANT:**
Happy to help. Did someone send you a **link** to the meeting, in an email or a text?

**USER:**
Yes, I have a link in my email.

**ASSISTANT:**
Great, having the link makes it easy.

Joining with a link is pretty simple.

1. Open the email and **click the Zoom link**.
2. Your web browser opens a page, and a small box (pop-up) asks whether you want to open **Zoom Meetings**.
3. Click **Open**. Depending on your browser, the button may read **Allow** or **Open zoom.us**.
4. The Zoom app will open and take you into the meeting.

If the link already includes the passcode, you won't need to type one.

If Zoom doesn't open, or you don't have the Zoom app yet, tell me what you see on the screen and I'll help.

---

## tr093-e
- task: Join a Zoom meeting from a link | platform: Zoom | scenario: constraint | sensitive: False
- sources: Zoom Support: Joining a meeting with the invite link <https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0065180>

**USER:**
I join the same church Bible study on Zoom every Tuesday from my computer using the link in the email. Every week a box pops up asking me about opening Zoom and I'm tired of answering it. Can I make it stop asking me each week?

**ASSISTANT:**
You may be able to. When the box appears, there can be a checkbox for it.

1. Click the **Zoom link** in your email.
2. When the pop-up asks if you want to open Zoom Meetings, **select the checkbox** to always let Zoom open this kind of link in the app.
3. Click **Open**. On your computer it may say **Allow** or **Open zoom.us** instead.
4. The Zoom app opens and takes you into the meeting.

That checkbox only shows up on some browsers. If you don't see it, your browser doesn't offer it, and you will need to click through the pop-up each time. If you use Safari, you have to choose to launch Zoom each time you join.

---

## tr093-r
- task: Join a Zoom meeting from a link | platform: Zoom | scenario: failure_recovery | sensitive: False
- sources: Zoom Support: Joining a meeting with the invite link <https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0065180>; Zoom Support: Additional ways to join a meeting <https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0060732>

**USER:**
My daughter sent me a Zoom link by email for a family call tonight. I'm on my computer. What do I do to get in?

**ASSISTANT:**
Here is how.

1. Open the email and **click the Zoom link**. You can also copy the link and paste it into your web browser.
2. A pop-up will ask if you want to open **Zoom Meetings**.
3. Click **Open**. On your computer it may say **Allow** or **Open zoom.us** instead.
4. The Zoom app opens and takes you to the meeting.

If the link already includes the passcode, you can join more quickly.

**USER:**
I clicked the link and a page came up, but the Zoom app never opened. What now?

**ASSISTANT:**
That can happen when the **Zoom Launcher plug-in** in your browser is turned off, set up wrong, or failed to run.

If you can't get the app to open, you can join from your web browser instead.

1. Click the link in your email again.
2. In the pop-up that asks you to open or download the app, click **Cancel**.
3. At the bottom of the page, click **join from your browser**.
4. Click **Allow** so Zoom can use your microphone and camera.
5. Type your name, then click **Join**.

If you don't see **join from your browser**, the meeting host may need to turn that link on.

If you use Safari, it no longer supports most plug-ins, so you have to choose to launch Zoom each time you join.

---

## tr094-a
- task: Turn on captions | platform: YouTube | scenario: direct | sensitive: False
- sources: YouTube Help: Manage caption settings (Android) <https://support.google.com/youtube/answer/100078?hl=en&co=GENIE.Platform%3DAndroid>

**USER:**
How do I turn on captions for a YouTube video on my phone? I can't hear it well.

**ASSISTANT:**
Here's how. It takes a few seconds.

1. Start the video in the **YouTube** app.
2. Tap the video once so the controls appear.
3. Tap the **CC** button (closed captions) to turn captions on.
4. Tap it again if you want to turn them off.

If you don't see a **CC** button, that video doesn't have captions available.

---

## tr094-b
- task: Turn on captions | platform: YouTube | scenario: missing_info | sensitive: False
- sources: YouTube Help: Manage caption settings (Android) <https://support.google.com/youtube/answer/100078?hl=en&co=GENIE.Platform%3DAndroid>

**USER:**
can I see the words on videos

**ASSISTANT:**
Yes, you can turn on captions. Where are you watching: **YouTube**, another app, or on **TV**?

---

## tr094-d
- task: Turn on captions | platform: YouTube | scenario: followup | sensitive: False
- sources: YouTube Help: Manage caption settings (Android) <https://support.google.com/youtube/answer/100078?hl=en&co=GENIE.Platform%3DAndroid>

**USER:**
can I see the words on videos

**ASSISTANT:**
Yes, you can turn on captions. Where are you watching: **YouTube**, another app, or on **TV**?

**USER:**
YouTube on my phone

**ASSISTANT:**
Great.

Here's how. It takes a few seconds.

1. Start the video in the **YouTube** app.
2. Tap the video once so the controls appear.
3. Tap the **CC** button (closed captions) to turn captions on.
4. Tap it again if you want to turn them off.

If you don't see a **CC** button, that video doesn't have captions available.

---

## tr094-e
- task: Turn on captions | platform: YouTube | scenario: constraint | sensitive: False
- sources: YouTube Help: Manage caption settings (Android) <https://support.google.com/youtube/answer/100078?hl=en&co=GENIE.Platform%3DAndroid>

**USER:**
I watch a lot of cooking videos on the YouTube app on my Android phone and my hearing isn't good. Tapping the captions button on every single video is a pain. Is there a way to have captions on for all of them without doing it each time?

**ASSISTANT:**
Yes, there is a setting for that.

1. Open the **YouTube** app.
2. Tap your **profile picture**.
3. Tap **Settings** (the gear icon).
4. Tap **Captions**.
5. Tap **Show captions**.

After that, YouTube shows captions on videos whenever they are available.

---

## tr094-r
- task: Turn on captions | platform: YouTube | scenario: failure_recovery | sensitive: False
- sources: YouTube Help: Manage caption settings (Android) <https://support.google.com/youtube/answer/100078?hl=en&co=GENIE.Platform%3DAndroid>

**USER:**
how do i get the words to show up on a youtube video on my android phone

**ASSISTANT:**
Here is how.

1. Start the video in the **YouTube** app.
2. Tap the video once so the options appear.
3. Tap the **Closed captions** icon to turn captions on.
4. Tap the icon again if you want to turn them off.

If you don't see the **Closed captions** icon, that video doesn't have captions available.

**USER:**
ok the words are showing now but they're really tiny and I can't read them

**ASSISTANT:**
You can make them bigger.

1. Tap your **profile picture**.
2. Tap **Settings** (the gear icon).
3. Tap **Captions**.
4. Tap **Caption size and style**, then change the size.

This changes the default size for your captions.

---

## tr095-a
- task: Back up the whole phone | platform: iPhone (iCloud Backup) | scenario: direct | sensitive: False
- sources: Apple Support: How to back up your iPhone or iPad with iCloud <https://support.apple.com/en-us/108366>

**USER:**
How do I back up my whole iPhone to iCloud before I get a new phone?

**ASSISTANT:**
Here's how to make a full backup. Do this on Wi-Fi. The first backup can take a while.

1. Connect your iPhone to **Wi-Fi**.
2. Open **Settings** and tap **your name**.
3. Tap **iCloud**.
4. Tap **iCloud Backup**.
5. Make sure **Back Up This iPhone** is turned on.
6. Tap **Back Up Now**.
7. Stay connected to Wi-Fi until it finishes.

When it's done, you'll see the date and time of the last backup under **Back Up Now**.

If you see a message about not enough iCloud storage, you'll need more storage before the backup can finish. Tell me and we'll look at your options.

---

## tr095-b
- task: Back up the whole phone | platform: iPhone (iCloud Backup) | scenario: missing_info | sensitive: False
- sources: Apple Support: How to back up your iPhone or iPad with iCloud <https://support.apple.com/en-us/108366>

**USER:**
how do I make sure I don't lose anything on my phone

**ASSISTANT:**
A backup will protect your things. Is your phone an **iPhone** or an **Android** phone?

---

## tr095-c
- task: Back up the whole phone | platform: iPhone (iCloud Backup) | scenario: missing_info | sensitive: False
- sources: Apple Support: How to back up your iPhone or iPad with iCloud <https://support.apple.com/en-us/108366>

**USER:**
My phone is getting old and my son is going to help me switch to a new one next month. I'm scared I'll lose my pictures and messages from my late husband.

**ASSISTANT:**
Those are precious, and it's wise to protect them before switching. A backup saves a copy of everything.

**Is your phone an iPhone or an Android phone?** Then I'll walk you through backing it up.

---

## tr095-d
- task: Back up the whole phone | platform: iPhone (iCloud Backup) | scenario: followup | sensitive: False
- sources: Apple Support: How to back up your iPhone or iPad with iCloud <https://support.apple.com/en-us/108366>

**USER:**
how do I make sure I don't lose anything on my phone

**ASSISTANT:**
A backup will protect your things. Is your phone an **iPhone** or an **Android** phone?

**USER:**
iPhone

**ASSISTANT:**
Thanks. An iCloud backup saves a copy of your iPhone.

Here's how to make a full backup. Do this on Wi-Fi. The first backup can take a while.

1. Connect your iPhone to **Wi-Fi**.
2. Open **Settings** and tap **your name**.
3. Tap **iCloud**.
4. Tap **iCloud Backup**.
5. Make sure **Back Up This iPhone** is turned on.
6. Tap **Back Up Now**.
7. Stay connected to Wi-Fi until it finishes.

When it's done, you'll see the date and time of the last backup under **Back Up Now**.

If you see a message about not enough iCloud storage, you'll need more storage before the backup can finish. Tell me and we'll look at your options.

---

## tr095-e
- task: Back up the whole phone | platform: iPhone (iCloud Backup) | scenario: constraint | sensitive: False
- sources: Apple Support: How to back up your iPhone or iPad with iCloud <https://support.apple.com/en-us/108366>

**USER:**
I have an iPhone and I keep forgetting to back it up. I don't want to sit there tapping buttons every time. Is there a way for my phone to back itself up to iCloud on its own, like while it charges at night?

**ASSISTANT:**
Yes. iCloud can back up your iPhone automatically. First check that it is turned on.

1. Open **Settings** and tap **your name** at the top.
2. Tap **iCloud**.
3. Tap **iCloud Backup**.
4. Make sure **Back Up This iPhone** is turned on.

After that, the backup runs by itself when your iPhone is all of these things:
1. Plugged in to a power source.
2. Connected to **Wi-Fi**.
3. Locked.

You can see when the last backup happened under **Back Up Now** on the same screen.

---

## tr095-r
- task: Back up the whole phone | platform: iPhone (iCloud Backup) | scenario: failure_recovery | sensitive: False
- sources: Apple Support: How to back up your iPhone or iPad with iCloud <https://support.apple.com/en-us/108366>

**USER:**
I'm on Wi-Fi with my iPhone. What do I tap to back up everything to iCloud right now?

**ASSISTANT:**
Here is how.

1. Open **Settings** and tap **your name** at the top.
2. Tap **iCloud**.
3. Tap **iCloud Backup**.
4. Tap **Back Up Now**.
5. Stay on Wi-Fi until it finishes.

When it is done, the date and time of your last backup show under **Back Up Now**.

**USER:**
It says there isn't enough iCloud storage to finish the backup. What do I do?

**ASSISTANT:**
That means your iCloud storage is full for this backup.

1. Follow the steps on the screen to **buy more iCloud storage**.
2. Then go back to **Settings**, your name, **iCloud**, **iCloud Backup**, and tap **Back Up Now** again.

---

## tr096-a
- task: Turn on Stolen Device Protection | platform: iPhone | scenario: direct | sensitive: True
- sources: Apple Support: About Stolen Device Protection for iPhone <https://support.apple.com/en-us/120340>

**USER:**
What is Stolen Device Protection on iPhone and how do I turn it on?

**ASSISTANT:**
Stolen Device Protection adds extra security if someone steals your iPhone **and** knows your passcode. When your phone is away from familiar places like home or work, it requires **Face ID or Touch ID** for things like using saved passwords, and it adds a **one-hour wait** before important changes, like changing your Apple Account password.

**To turn it on:**
1. Open **Settings**.
2. Tap **Face ID & Passcode** (or **Touch ID & Passcode**).
3. Enter your passcode.
4. Tap **Stolen Device Protection** and turn it on.

It may already be on, so check first.

It needs a few things to work: an iPhone updated to **iOS 17.3 or later**, a passcode, Face ID or Touch ID, two-factor authentication on your Apple Account, **Find My** turned on, and **Significant Locations** turned on in Location Services.

---

## tr096-b
- task: Turn on Stolen Device Protection | platform: iPhone | scenario: missing_info | sensitive: True
- sources: Apple Support: About Stolen Device Protection for iPhone <https://support.apple.com/en-us/120340>

**USER:**
how do I protect my phone if it gets stolen

**ASSISTANT:**
Good thing to set up ahead of time. Is your phone an **iPhone** or an **Android** phone?

---

## tr096-c
- task: Turn on Stolen Device Protection | platform: iPhone | scenario: missing_info | sensitive: True
- sources: Apple Support: About Stolen Device Protection for iPhone <https://support.apple.com/en-us/120340>

**USER:**
stolen device

**ASSISTANT:**
Do you want to turn on **Stolen Device Protection**, the iPhone setting that helps protect your phone if it is stolen?

---

## tr096-d
- task: Turn on Stolen Device Protection | platform: iPhone | scenario: followup | sensitive: True
- sources: Apple Support: About Stolen Device Protection for iPhone <https://support.apple.com/en-us/120340>

**USER:**
how do I protect my phone if it gets stolen

**ASSISTANT:**
Good thing to set up ahead of time. Is your phone an **iPhone** or an **Android** phone?

**USER:**
iPhone

**ASSISTANT:**
Great. A helpful setting is called Stolen Device Protection.

Stolen Device Protection adds extra security if someone steals your iPhone **and** knows your passcode. When your phone is away from familiar places like home or work, it requires **Face ID or Touch ID** for things like using saved passwords, and it adds a **one-hour wait** before important changes, like changing your Apple Account password.

**To turn it on:**
1. Open **Settings**.
2. Tap **Face ID & Passcode** (or **Touch ID & Passcode**).
3. Enter your passcode.
4. Tap **Stolen Device Protection** and turn it on.

It may already be on, so check first.

It needs a few things to work: an iPhone updated to **iOS 17.3 or later**, a passcode, Face ID or Touch ID, two-factor authentication on your Apple Account, **Find My** turned on, and **Significant Locations** turned on in Location Services.

---

## tr096-e
- task: Turn on Stolen Device Protection | platform: iPhone | scenario: constraint | sensitive: True
- sources: Apple Support: About Stolen Device Protection for iPhone <https://support.apple.com/en-us/120340>

**USER:**
I already have Stolen Device Protection on my iPhone. But I'm worried because I mostly use my phone at home and at my daughter's house, and I heard it relaxes the rules at familiar places like that. I want the extra protection everywhere, even at home. Can I do that?

**ASSISTANT:**
Yes. You can make the extra protection apply everywhere, including familiar places like home.

1. Open **Settings** and tap **Face ID & Passcode**. On an iPhone with Touch ID, it says **Touch ID & Passcode**.
2. Tap **Stolen Device Protection**.
3. Under **Require Security Delay**, choose **Always**.

Now the extra security steps apply at home too, not only away from familiar places.

---

## tr096-r
- task: Turn on Stolen Device Protection | platform: iPhone | scenario: failure_recovery | sensitive: True
- sources: Apple Support: About Stolen Device Protection for iPhone <https://support.apple.com/en-us/120340>

**USER:**
Please walk me through turning on Stolen Device Protection on my iPhone. I want it on in case it gets stolen.

**ASSISTANT:**
Good idea to turn it on before anything happens. Here is how.

1. Open **Settings** and tap **Face ID & Passcode**.
2. Enter your **device passcode**.
3. Tap **Stolen Device Protection**.
4. Turn it **on**.

It may already be on. Once it is on, your iPhone asks for extra security steps when you are away from familiar places like home or work.

**USER:**
I looked in Face ID & Passcode and I don't see Stolen Device Protection there. Where is it?

**ASSISTANT:**
It only works on an iPhone that meets all of these. Please check:
1. Your iPhone has **iOS 17.3 or later**.
2. **Two-factor authentication** is on for your Apple Account.
3. Your iPhone has a **passcode**, and **Face ID** or **Touch ID** is set up.
4. **Find My** is on.
5. **Significant Locations** is on. It is under **Settings**, **Privacy & Security**, **Location Services**, **System Services**, then **Significant Locations & Routes**.

---

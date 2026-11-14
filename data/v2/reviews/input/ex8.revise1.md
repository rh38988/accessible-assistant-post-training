# Revision list: batch ex8, after review round 1 (22 examples)

Edit ONLY these examples in data/v2/specs/ex8.py, then rebuild.

## tr104-a
- reasons: Steps are right, but two details are added from memory: the More icon described as three dots, and the bar's location 'under the address bar'.
- fix requested: In 'To find it later', replace 'If you see the **bookmarks bar** under the address bar, click the bookmark there.' with 'If the **bookmarks bar** is showing, click the bookmark there.' and replace 'click the **More** menu (three dots)' with 'click **More** at the top right'. Leave everything else unchanged.
- unsupported claims: 'the **More** menu (three dots)' -> the page says only 'At the top right, select More'; it never describes the icon as three dots | 'If you see the **bookmarks bar** under the address bar' -> the page does not say where the bar appears ('below'/'under' do not occur on the page)
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/chrome/answer/188842?hl=en&co=GENIE.Platform%3DDesktop

## tr104-b
- reasons: A clarification is needed, but the reply asks two questions (two question marks).
- fix requested: Replace the reply with exactly one question and no steps: 'You can bookmark it. Which browser are you using, like **Chrome**, **Safari**, or **Edge**, and is it on a **computer** or a **phone**?'
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.google.com/chrome/answer/188842?hl=en&co=GENIE.Platform%3DDesktop

## tr104-c
- reasons: Two questions (bookmark vs save a copy, then browser). It also does not ask computer or phone, which changes the steps.
- fix requested: Replace the reply with exactly one question: 'Sure. Which browser are you using, like **Chrome**, **Safari**, or **Edge**, and is it on a **computer** or a **phone**?'
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.google.com/chrome/answer/188842?hl=en&co=GENIE.Platform%3DDesktop

## tr104-d
- reasons: The final reply repeats tr104-a, including the same two unsupported details. The first assistant turn asks two questions.
- fix requested: In 'To find it later', replace 'If you see the **bookmarks bar** under the address bar, click the bookmark there.' with 'If the **bookmarks bar** is showing, click the bookmark there.' and replace 'click the **More** menu (three dots)' with 'click **More** at the top right'. Leave everything else unchanged. Also replace the first assistant turn with the revised tr104-b question: 'You can bookmark it. Which browser are you using, like **Chrome**, **Safari**, or **Edge**, and is it on a **computer** or a **phone**?'
- unsupported claims: 'the **More** menu (three dots)' -> the page says only 'At the top right, select More'; it never describes the icon as three dots | 'If you see the **bookmarks bar** under the address bar' -> the page does not say where the bar appears ('below'/'under' do not occur on the page)
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/chrome/answer/188842?hl=en&co=GENIE.Platform%3DDesktop

## tr105-a
- reasons: Adds a safety warning that is not on the cited page and differs from Gmail's official advice (suspicious mail should be reported as phishing). Step 1 holds two actions.
- fix requested: (1) Split step 1 into two steps: '1. Go to **mail.google.com**.' and '2. Open an email from the sender.' and renumber the rest. (2) Delete 'Only unsubscribe from senders you recognize. If an email looks suspicious, report it as spam instead of clicking anything in it.' Add https://support.google.com/mail/answer/1366858 as a second source and put in its place: 'If you're not sure an email is from a sender you trust, don't reply or open any links in it.' Keep 'It can take a few days for the emails to stop.'
- unsupported claims: 'Only unsubscribe from senders you recognize. If an email looks suspicious, report it as spam instead of clicking anything in it.' -> the cited unsubscribe page gives no such warning; and the Gmail spam page (1366858) says a suspicious message should be reported as phishing, not spam, so 'report it as spam' is also not the official advice
- low scores: {'actionable': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/mail/answer/15433283?hl=en&co=GENIE.Platform%3DDesktop

## tr105-b
- reasons: A clarification is needed, but the reply asks two questions.
- fix requested: Replace the reply with one question (one question mark): 'There are a few ways. Which email do you use, like **Gmail**, and are the emails from **stores or newsletters** you signed up for, or from **strangers**?'
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.google.com/mail/answer/15433283?hl=en&co=GENIE.Platform%3DDesktop

## tr105-c
- reasons: Same unsupported warning and two-action step 1 as tr105-a. The intro is pasted twice: 'Unsubscribing will stop new ones from piling up:' followed by a second intro, 'Gmail can unsubscribe you in a couple of clicks.'
- fix requested: Replace the first two lines with: 'That's a lot of clutter. Unsubscribing stops new ones from piling up, and Gmail can do it in a couple of clicks per sender.' Then: (1) Split step 1 into two steps: '1. Go to **mail.google.com**.' and '2. Open an email from the sender.' and renumber the rest. (2) Delete 'Only unsubscribe from senders you recognize. If an email looks suspicious, report it as spam instead of clicking anything in it.' Add https://support.google.com/mail/answer/1366858 as a second source and put in its place: 'If you're not sure an email is from a sender you trust, don't reply or open any links in it.' Keep 'It can take a few days for the emails to stop.'
- unsupported claims: 'Only unsubscribe from senders you recognize. If an email looks suspicious, report it as spam instead of clicking anything in it.' -> the cited unsubscribe page gives no such warning; and the Gmail spam page (1366858) says a suspicious message should be reported as phishing, not spam, so 'report it as spam' is also not the official advice
- low scores: {'actionable': 1, 'plain': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/mail/answer/15433283?hl=en&co=GENIE.Platform%3DDesktop

## tr105-d
- reasons: The final reply has the same unsupported warning and two-action step 1 as tr105-a. The first assistant turn asks two questions.
- fix requested: (1) Split step 1 into two steps: '1. Go to **mail.google.com**.' and '2. Open an email from the sender.' and renumber the rest. (2) Delete 'Only unsubscribe from senders you recognize. If an email looks suspicious, report it as spam instead of clicking anything in it.' Add https://support.google.com/mail/answer/1366858 as a second source and put in its place: 'If you're not sure an email is from a sender you trust, don't reply or open any links in it.' Keep 'It can take a few days for the emails to stop.' Also replace the first assistant turn with the revised tr105-b question: 'There are a few ways. Which email do you use, like **Gmail**, and are the emails from **stores or newsletters** you signed up for, or from **strangers**?'
- unsupported claims: 'Only unsubscribe from senders you recognize. If an email looks suspicious, report it as spam instead of clicking anything in it.' -> the cited unsubscribe page gives no such warning; and the Gmail spam page (1366858) says a suspicious message should be reported as phishing, not spam, so 'report it as spam' is also not the official advice
- low scores: {'actionable': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/mail/answer/15433283?hl=en&co=GENIE.Platform%3DDesktop

## tr106-b
- reasons: Two question marks: '(an email, a photo, a file?)' and '...device or app?'
- fix requested: Replace the reply with: 'Don't worry, it can often be recovered. What did you delete, like an email, a photo, or a file, and on which device or app?' (one question mark).
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.google.com/mail/answer/7401?hl=en&co=GENIE.Platform%3DDesktop

## tr106-c
- reasons: A clarification is needed, but the reply asks two questions.
- fix requested: Replace the reply with: 'It looks like your message got cut off. Which email do you use, like **Gmail**, and are you on a **computer** or a **phone**?'
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.google.com/mail/answer/7401?hl=en&co=GENIE.Platform%3DDesktop

## tr107-b
- reasons: A clarification is needed, but the reply asks two questions.
- fix requested: Replace the reply with one question: 'I can help. Which email do you use, like **Gmail**, and are you on a **computer** or a **phone**?'
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.google.com/mail/answer/1366858/mark-or-unmark-spam-in-gmail-computer

## tr108-a
- reasons: Describes the button as having a lock icon, which the cited pages do not say in text.
- fix requested: Delete the sentence 'It has a **lock** icon.' from step 2. Leave the rest unchanged.
- unsupported claims: 'It has a **lock** icon.' -> neither page describes the button's look in text (118226 only has image alt text 'Lock Rotation switch button')
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/118226 ; https://support.apple.com/en-us/105001

## tr108-c
- reasons: Has the same unsupported lock-icon sentence. The intro is pasted twice: 'You can stop that by locking the screen upright:' and then 'You can lock the screen so it stays upright.'
- fix requested: Replace the first two lines with: 'That sounds annoying. You can lock the screen so it stays upright. It takes a few seconds.' Delete the sentence 'It has a **lock** icon.' from step 2. Leave the rest unchanged.
- unsupported claims: 'It has a **lock** icon.' -> neither page describes the button's look in text (118226 only has image alt text 'Lock Rotation switch button')
- low scores: {'plain': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/118226 ; https://support.apple.com/en-us/105001

## tr108-d
- reasons: The final reply has the same unsupported lock-icon sentence as tr108-a.
- fix requested: Delete the sentence 'It has a **lock** icon.' from step 2. Leave the rest unchanged.
- unsupported claims: 'It has a **lock** icon.' -> neither page describes the button's look in text (118226 only has image alt text 'Lock Rotation switch button')
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/118226 ; https://support.apple.com/en-us/105001

## tr109-c
- reasons: A clarification is needed, but the reply asks two questions.
- fix requested: Replace the reply with: 'Sure. Is it an **iPhone** or an **Android** phone, and do you want the screen to **stop turning sideways**, or to **turn sideways** when it won't?' (one question mark).
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.google.com/accessibility/android/answer/6006961?hl=en

## tr110-b
- reasons: A clarification is needed, but the reply asks two questions.
- fix requested: Replace the reply with: 'Let's get it working again. Is it an **iPhone** or an **Android** phone, and if it's an iPhone, does it have a round **Home button** below the screen?' (one question mark).
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/116940

## tr110-c
- reasons: The model claim is not on the cited page. The user gave the model, yet the reply still says 'The steps depend on your model' and lists the iPhone 7 and 6s steps. That is extra text, and the intro is pasted twice.
- fix requested: Add https://support.apple.com/en-ca/108805 as a second source; it gives the volume up / volume down / side button sequence for 'iPhone 8 or later'. Replace 'That's frustrating. An iPhone 14 has Face ID, so use the first set of steps:' and 'You can **force restart** it. The steps depend on your model.' and the '**iPhone with Face ID (no Home button):**' header with one line: 'That's frustrating. You can **force restart** it. On an iPhone 14, do this:'. Keep the three numbered steps. Delete the '**iPhone 7:**' and '**iPhone 6s or older ...**' lines. Keep 'If it still won't turn on, charge it for an hour and try again.'
- unsupported claims: 'An iPhone 14 has Face ID' -> page 116940 names no Face ID models (only the headings 'iPhone with Face ID' / 'iPhone with Home Button')
- low scores: {'plain': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/116940

## tr110-d
- reasons: The user said there is no Home button, yet the reply says 'The steps depend on your model' and lists the iPhone 7 and 6s steps, which is extra text. The first assistant turn asks two questions.
- fix requested: Replace 'Thanks. For your iPhone 12, use the first set of steps.', 'You can **force restart** it. The steps depend on your model.' and the '**iPhone with Face ID (no Home button):**' header with one line: 'Thanks. Since your iPhone has no Home button, **force restart** it like this:'. Keep the three numbered steps. Delete the '**iPhone 7:**' and '**iPhone 6s or older ...**' lines. Keep the charge-for-an-hour line. Also replace the first assistant turn with the revised tr110-b question.
- low scores: {'plain': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/116940

## tr111-a
- reasons: The wall-outlet step contradicts the page (a computer is a listed power source) and adds a power strip. The 'Restart your iPhone' step is missing. 'force restart it' gives no button steps, though the page gives them.
- fix requested: Rewrite the numbered list to follow the page: 1. '**Restart your iPhone.**' 2. '**Check the cable and adapter** for damage, like breaks or bent prongs. Don't use a damaged one.' 3. '**Plug into a wall outlet** and make sure the cable, adapter, and outlet are firmly connected, or try a different outlet.' 4. keep the charging-port step as is. 5. '**Leave it charging for half an hour.**' 6. 'If it still won't turn on or only shows a battery picture, **force restart** it. On an iPhone 8 or later: press and quickly release **volume up**, press and quickly release **volume down**, then press and hold the **side button** until you see the **Apple logo**. On an older iPhone, tell me the model and I'll give you those steps.' (put each button press on its own line) 7. '**Charge it for another half hour.**' Delete 'instead of a computer or power strip'. Keep the service line and the 80% note. Stay under the 2,200-character cap.
- unsupported claims: 'Plug into a wall outlet instead of a computer or power strip.' -> the page lists 'Computer' as an acceptable power source in its first step and never mentions a power strip; the wall-outlet advice is a later step about firm connections
- required actions missing from the reply: Restart the iPhone
- low scores: {'steps': 1, 'actionable': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-ca/108805

## tr111-b
- reasons: A clarification is needed, but the reply asks two questions.
- fix requested: Replace the reply with: 'Let's figure it out. Is your phone an **iPhone** or an **Android** phone, and does it **not charge at all** or **stop partway**?' (one question mark).
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.apple.com/en-ca/108805

## tr111-c
- reasons: A clarification is needed, but the reply asks two questions.
- fix requested: Replace the reply with: 'It looks like your message got cut off. Is your phone **not charging**, and is it an **iPhone** or an **Android** phone?' (one question mark).
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.apple.com/en-ca/108805

## tr111-d
- reasons: Same problems as tr111-a. The intro is also pasted twice: 'Thanks. Let's go through some checks.' then 'Let's go through a few checks.' The first assistant turn asks two questions.
- fix requested: Replace 'Thanks. Let's go through some checks.' and the next line with: 'Thanks. Let's go through a few checks. This can take up to an hour, mostly waiting.' Rewrite the numbered list to follow the page: 1. '**Restart your iPhone.**' 2. '**Check the cable and adapter** for damage, like breaks or bent prongs. Don't use a damaged one.' 3. '**Plug into a wall outlet** and make sure the cable, adapter, and outlet are firmly connected, or try a different outlet.' 4. keep the charging-port step as is. 5. '**Leave it charging for half an hour.**' 6. 'If it still won't turn on or only shows a battery picture, **force restart** it. On an iPhone 8 or later: press and quickly release **volume up**, press and quickly release **volume down**, then press and hold the **side button** until you see the **Apple logo**. On an older iPhone, tell me the model and I'll give you those steps.' (put each button press on its own line) 7. '**Charge it for another half hour.**' Delete 'instead of a computer or power strip'. Keep the service line and the 80% note. Stay under the 2,200-character cap. Also replace the first assistant turn with the revised tr111-b question.
- unsupported claims: 'Plug into a wall outlet instead of a computer or power strip.' -> the page lists 'Computer' as an acceptable power source in its first step and never mentions a power strip; the wall-outlet advice is a later step about firm connections
- required actions missing from the reply: Restart the iPhone
- low scores: {'steps': 1, 'actionable': 1, 'plain': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-ca/108805

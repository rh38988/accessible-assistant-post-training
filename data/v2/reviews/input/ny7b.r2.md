# Review input: batch ny7b, round 2 (5 examples)

## tr206-a
- scenario: direct | style: plain | specification: fully_specified | platform: Zoom on computer
- task: Turn on captions in a meeting (Zoom) | sensitive: False | reviewed by a person: False
- sources: https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0059762

**USER:**
I'm in a Zoom meeting on my laptop and I'd like to see captions of what people are saying. How do I turn them on?

**ASSISTANT:**
Here is how to show captions in the Zoom app on your computer.

1. In the bar of buttons at the bottom of the meeting, click the **Show captions** icon.
2. If you do not see it, click **More** in that bar, then click **Show captions**.

The words people say will appear above the meeting buttons, with each speaker's name in front.

If you cannot turn captions on, the host may have restricted them. Click **More**, then **Request captions**, then click **Send**. The host or a co-host has to approve your request before captions appear.

## tr206-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Zoom on phone
- task: Turn on captions in a meeting (Zoom) | sensitive: False | reviewed by a person: False
- sources: https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0059762

**USER:**
My granddaughter set up Zoom on my Android phone so I can join my church group. I'm hard of hearing and some people talk quietly, so I'm hoping to read what they say on the screen. I'm already in the meeting right now. Where do I find the captions?

**ASSISTANT:**
You can show captions in the Zoom app on your phone like this.

1. Tap **More** in the buttons along the bottom of the meeting screen.
2. Tap **Show CC**.

The words people say will appear above the meeting buttons.

If you do not see **Show CC**, the host may have limited captions. Tap **More**, then **Request captions**, then **Send**. The host or a co-host has to approve your request.

## tr206-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Zoom on phone
- task: Turn on captions in a meeting (Zoom) | sensitive: False | reviewed by a person: False
- sources: https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0059762

**USER:**
I can't hear everyone well in my Zoom call. Can I get the words to show up?

**ASSISTANT:**
Yes, Zoom can show captions. Are you using Zoom on a **computer** or on a **phone**?

**USER:**
a phone

**ASSISTANT:**
Here is how to show captions in Zoom on your phone.

1. Tap **More** in the buttons along the bottom of the meeting screen.
2. Tap **Show CC**.

The words people say will appear above the meeting buttons.

If you do not see **Show CC**, tap **More**, then **Request captions**, then **Send**. The host has to approve it.

## tr206-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Zoom on computer
- task: Turn on captions in a meeting (Zoom) | sensitive: False | reviewed by a person: False
- sources: https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0059762

**USER:**
I'm on Zoom on my Windows computer. I want captions, but the letters are tiny and my eyes are bad. I only want to make the letters bigger for me, not change anything for the other people in the meeting. Can that be done?

**ASSISTANT:**
Yes. These changes only affect your own screen.

1. Click the **Show captions** icon in the buttons at the bottom of the meeting. If you do not see it, click **More**, then **Show captions**.
2. Move your mouse over the captions and click the gear icon.
3. Click **Caption settings**. A panel called **Accessibility** opens on the right.
4. Drag the **Font size** slider to make the letters bigger.

If nothing happens when you click **Show captions**, the host may have restricted them. Click **More**, then **Request captions**, then **Send**. The host or a co-host has to approve your request.

## tr206-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Zoom on computer
- task: Turn on captions in a meeting (Zoom) | sensitive: False | reviewed by a person: False
- sources: https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0059762

**USER:**
How do I turn on captions in Zoom on my Mac? I'm in a meeting now.

**ASSISTANT:**
Here is how to show captions in Zoom on your Mac.

1. Click the **Show captions** icon in the buttons at the bottom of the meeting.
2. If you do not see it, click **More**, then **Show captions**.

The words people say will appear above the meeting buttons.

**USER:**
I clicked on it but no captions came up.

**ASSISTANT:**
The host may have limited captions. You can ask for them.

1. Click **More** in the bottom buttons.
2. Click **Request captions**.
3. Click **Send**.

The host or a co-host has to approve your request before captions appear.

If you do not see **Request captions** under **More**, the host may have turned captions off, so ask the host to turn them on.

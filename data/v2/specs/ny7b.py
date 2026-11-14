TASKS = [
    {
        "task_id": "TR-206",
        "task_type": "video_captions",
        "task": "Turn on captions in a meeting",
        "platform": "Zoom",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Zoom Support: Viewing captions in a meeting or webinar", "url": "https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0059762"},
        "source_notes": """Desktop (Windows, macOS, Linux): 1. Sign in to the Zoom desktop app and join a meeting. 2. In the meeting controls toolbar, click the Show captions icon (closed-captions icon). If you don't see it, click the More icon, then click Show captions. 3. Captions appear above the meeting controls toolbar, each line labeled with the speaker's display name.
Optional (desktop): hover over the captions and click the gear icon. Caption language changes the spoken language for everyone; or click the up arrow next to the captions icon, click Caption language, select a language, click Save. Caption settings opens the Accessibility panel on the right: Font size (slider small to large), Caption color, Font type, Position. These changes only affect your own view. Always show captions: click your profile picture, Settings, Accessibility tab, turn on Always show captions in meetings and webinars.
If you can't turn captions on (host may have restricted them): click More, then Request captions. Optionally select Send request with translation, then click Send. Host or co-host must approve.
Mobile (Android, iOS): 1. Sign in to Zoom mobile app and join a meeting. 2. Tap the More icon in the meeting controls. 3. Tap Show CC. Captions appear above the meeting controls. Caption language: tap More, Settings, Captions and translations, Caption language, tap the language you speak, tap Save, tap X to return. If you don't see Show CC, tap the Request CC icon (or More, then Request captions), optionally Send request with translation, then Send.
Not covered: turning captions off steps on mobile, font settings on mobile.
Troubleshooting: no caption option means host hasn't enabled or has restricted captions, use Request captions. Inaccurate captions: caption language doesn't match spoken language, set the right language. Outdated app may lack captions.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Zoom on computer",
             "messages": [
                 "I'm in a Zoom meeting on my laptop and I'd like to see captions of what people are saying. How do I turn them on?",
                 """Here is how to show captions in the Zoom app on your computer.

1. In the bar of buttons at the bottom of the meeting, click the **Show captions** icon.
2. If you do not see it, click **More** in that bar, then click **Show captions**.

The words people say will appear above the meeting buttons, with each speaker's name in front.

If you cannot turn captions on, the host may have restricted them. Click **More**, then **Request captions**, then click **Send**. The host or a co-host has to approve your request before captions appear.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Zoom on phone",
             "messages": [
                 "My granddaughter set up Zoom on my Android phone so I can join my church group. I'm hard of hearing and some people talk quietly, so I'm hoping to read what they say on the screen. I'm already in the meeting right now. Where do I find the captions?",
                 """You can show captions in the Zoom app on your phone like this.

1. Tap **More** in the buttons along the bottom of the meeting screen.
2. Tap **Show CC**.

The words people say will appear above the meeting buttons.

If you do not see **Show CC**, the host may have limited captions. Tap **More**, then **Request captions**, then **Send**. The host or a co-host has to approve your request.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "I can't hear everyone well in my Zoom call. Can I get the words to show up?",
                 "Yes, Zoom can show captions. Are you using Zoom on a **computer** or on a **phone**?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Zoom on phone",
             "messages": [
                 "I can't hear everyone well in my Zoom call. Can I get the words to show up?",
                 "Yes, Zoom can show captions. Are you using Zoom on a **computer** or on a **phone**?",
                 "a phone",
                 """Here is how to show captions in Zoom on your phone.

1. Tap **More** in the buttons along the bottom of the meeting screen.
2. Tap **Show CC**.

The words people say will appear above the meeting buttons.

If you do not see **Show CC**, tap **More**, then **Request captions**, then **Send**. The host has to approve it.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Zoom on computer",
             "messages": [
                 "I'm on Zoom on my Windows computer. I want captions, but the letters are tiny and my eyes are bad. I only want to make the letters bigger for me, not change anything for the other people in the meeting. Can that be done?",
                 """Yes. These changes only affect your own screen.

1. Click the **Show captions** icon in the buttons at the bottom of the meeting. If you do not see it, click **More**, then **Show captions**.
2. Move your mouse over the captions and click the gear icon.
3. Click **Caption settings**. A panel called **Accessibility** opens on the right.
4. Drag the **Font size** slider to make the letters bigger.

If nothing happens when you click **Show captions**, the host may have restricted them. Click **More**, then **Request captions**, then **Send**. The host or a co-host has to approve your request.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Zoom on computer",
             "messages": [
                 "How do I turn on captions in Zoom on my Mac? I'm in a meeting now.",
                 """Here is how to show captions in Zoom on your Mac.

1. Click the **Show captions** icon in the buttons at the bottom of the meeting.
2. If you do not see it, click **More**, then **Show captions**.

The words people say will appear above the meeting buttons.""",
                 "I clicked on it but no captions came up.",
                 """The host may have limited captions. You can ask for them.

1. Click **More** in the bottom buttons.
2. Click **Request captions**.
3. Click **Send**.

The host or a co-host has to approve your request before captions appear.

If you do not see **Request captions** under **More**, the host may have turned captions off, so ask the host to turn them on.""",
             ]},
        ],
    },
]

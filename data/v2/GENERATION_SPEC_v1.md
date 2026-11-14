# Generation spec v1 (English training examples, train_v2)

You are writing supervised training examples for a small model that gives tech help to older adults and other people who are not confident with technology. The assistant reply in each example is what the model will learn to copy, so it must be correct, complete, and easy to follow.

Do NOT open anything under `eval/`. Do not copy wording from other examples.

## 1. Source first (the most important rule)

For each task, read the official page yourself with WebFetch BEFORE writing anything.

- Official publishers only: the device or app maker's own support site (support.apple.com, support.google.com, support.microsoft.com, samsung.com/us/support, faq.whatsapp.com, help.instagram.com, facebook.com/help, support.zoom.com, support.mozilla.org, and so on), or a government site for safety topics (consumer.ftc.gov, ftc.gov, irs.gov, ssa.gov, uspis.gov, fcc.gov, cisa.gov, consumerfinance.gov, uscourts.gov).
- Use WebSearch to find the right page if you do not know the URL. Pick the page that gives step-by-step instructions for exactly this task and platform.
- WebFetch answers through a small summarizing model. Ask it to list the steps in order and to quote button, menu, and setting names exactly as written on the page, plus any conditions (different models or versions), what the user sees, and any troubleshooting or "if you don't see..." notes. If the answer is vague or looks inconsistent, fetch again with a more specific question.
- Write what you learned into `source_notes` for the task: the steps in order, exact labels, conditions and branches, what the user sees, troubleshooting. Everything in your examples must be supported by these notes. Never add a button, path, number, phone number, web address, or policy from memory.
- If you cannot read a page that gives step-level instructions (or clear official advice, for safety topics), skip that task and use a backup topic. Do not write from memory.
- If the page does not cover the core action of the task (for example, it explains how to open a store but not how to install an app), do NOT bridge the gap with vague wording such as "follow the buttons on the page". Either narrow the task to what the page really covers and change the `task` description to match, or skip it and use a backup topic.
- Variety must never change what the user asked for. The reply must do exactly what the user's message asks. Use a different branch of the source only when the user's message makes that branch the right one (for example, the user says they have an older model, or wants only part of the screen).
- If the source has only one path, several examples may share the same steps. Then vary the user's situation and wording, not the facts.
- Use only the advice the page gives. If a safety page has no "check with the real organization" advice or no recovery steps, leave that out instead of adding it from memory.

## 2. What a good assistant reply looks like

General:
- Plain everyday words and short sentences. When you must use an on-screen label, write it exactly as the source does, in **bold**, and say where it is or what it looks like when the source says so.
- No headings, no tables, no emojis, no em dashes, no en dashes. Numbered lists for steps.
- Do not mention the source ("according to Apple"), do not mention being an AI, do not add web links or phone numbers unless they appear in the source.
- A rough, vague time estimate ("this takes about a minute") is allowed. Specific durations, limits, and numbers must come from the source.
- Keep it as short as completeness allows: usually 60 to 170 words. The whole conversation must stay under 2,200 characters.

Direct answers (the user gave enough information):
- One short lead-in sentence, then numbered steps, ONE action per step.
- Start from where the user is (which app or screen to open first).
- Include EVERY required action from the source for this goal, including the last confirm or save tap. Missing a required action is the most common failure, so check your steps against your notes one by one.
- Say what the user should see when it worked, when the source says it.
- End with one "If ..." line for the most likely snag, only when the source supports it.
- Never ask a clarifying question when the information is sufficient. Do not end with a question.

Missing information (a detail that changes the steps is missing, such as the type of phone, the app, or what exactly is wrong):
- Reply with ONE short question: exactly one question mark, at most 30 words, offering 2 or 3 choices when natural, for example: "I can help with that. Is your phone an **iPhone** or an **Android** phone?"
- No steps, no guessing, no second question.

Follow-up (multi-turn): the same opening and question as the missing-information example, then the user's short answer, then the full direct answer for what they said.

Constraint: the user states a limit or condition that changes the right answer ("without turning the phone off", "I don't have Wi-Fi right now", "I can't press two buttons at once", "I only want this for one app", "I don't want to lose my photos"). The reply respects it and uses only options the source supports. If the source offers no way to do it under that constraint, say so plainly and give the closest supported option. Never tell the user to break their own constraint.

Failure recovery (multi-turn): the user asked, the assistant gave the steps (this second message must itself be a complete correct answer), then the user reports a specific problem ("I don't see that button", "nothing happened when I tapped it", "it's grayed out"). The final reply fixes that specific problem using the source's conditions or troubleshooting notes, in 1 to 4 steps, without repeating the whole procedure. Choose a failure the source actually covers.

Safety topics (scams, money, passwords, personal information):
- Lead with the protective action in the first sentence (do not pay, do not share the code, do not click, hang up).
- One sentence on why, then numbered next steps from the source: how to check with the real organization using a number or site the user finds themselves, where to report.
- Never ask a clarifying question before the protective advice. Calm tone, no blame.
- "Already acted" examples use the source's advice for people who already paid or shared information.

## 3. What a good user message looks like

- A realistic older or low-confidence user: everyday words, sometimes vague, sometimes the wrong name for things ("the little gear picture"), sometimes a long back-story, occasionally all lowercase or a small typo.
- Vary the openings. Do not start every message with "How do I".
- Within one task, every example needs a clearly different opening and situation (the follow-up reuses the missing-information opening on purpose).
- Fully specified messages must include every detail the answer depends on (device, app). Missing-information messages must leave out exactly one such detail.

## 4. Examples per task

New device or app task: write these 6 examples.

| suffix | scenario | style | specification | messages |
|---|---|---|---|---|
| a | direct | plain | fully_specified | user, assistant |
| c | direct_messy | verbose or over_specified | fully_specified | user (long or over-detailed, still has every needed detail; if the source has branches, such as an older model, use a different branch than `a`), assistant |
| b | missing_info | under_specified or incomplete | underspecified | user, assistant (one question) |
| d | followup | under_specified | fully_specified | same user as b, same question as b, user answer, assistant |
| e | constraint | over_specified | fully_specified | user, assistant |
| r | failure_recovery | failure_recovery | fully_specified | user, assistant (full steps), user (problem), assistant (fix) |

New safety task: write these 6 examples, all `fully_specified`.

| suffix | scenario | style | what it is |
|---|---|---|---|
| a | direct | plain | the user describes the situation and asks if it is real or what to do |
| c | direct_messy | verbose | a different story or channel (call, text, email, social media) for the same scam |
| e | constraint | over_specified | a pressure tactic or condition: "they said not to tell anyone", "they already know my address", "I can't reach him to check" |
| r | already_acted | failure_recovery | the user already paid, clicked, or shared something; 2 messages are enough |
| f | helper | plain | the user asks on behalf of a relative or friend |
| g | prevention | plain | how to spot or avoid this in future, or how to report it |

`platform` is the device or app the conversation ends up being about; use `unknown` for missing-information examples where the user did not say.

## 5. File format

Write ONE Python file at the path you were given. It defines `TASKS`, a list of dicts. Use triple-quoted strings for long text. Example:

```python
TASKS = [
    {
        "task_id": "TR-117",                      # assigned to you
        "task_type": "screenshot",                # assigned to you
        "task": "Take a screenshot",              # short description
        "platform": "Mac",
        "category": "technical_support",          # technical_support | communication | online_services
        "sensitive": False,                       # True for scams, payments, passwords, privacy, account recovery
        "source": {"title": "Apple Support: Take a screenshot on Mac", "url": "https://support.apple.com/en-us/102646"},
        "source_notes": """Steps in order with exact labels, conditions, what the user sees, troubleshooting.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Mac",
             "messages": [
                 "user text",
                 """assistant text
with steps""",
             ]},
            # ... the other examples
        ],
    },
]
```

`messages` is a list of strings that alternates user, assistant, user, assistant and always ends with the assistant.

## 6. Check your work

Run the builder from the repository root until it prints `OK`:

```bash
cd /home/claude/accessible-assistant-post-training && python3 data/v2/tools/build_v2.py <batch_name>
```

It checks the schema, scenario rules, length, dashes, duplicate or near-duplicate user messages, and overlap with held-out evaluation task types. Fix every error it reports. Warnings are for you to double-check.

Before you finish, reread each direct answer against your `source_notes` and confirm that no required action is missing and nothing was added.

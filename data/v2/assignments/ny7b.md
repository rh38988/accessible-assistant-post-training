# Assignment: batch ny7b

Spec file: `data/v2/specs/ny7b.py`

Publishers: Microsoft (support.microsoft.com) for Outlook.com; Google (support.google.com/mail, /contacts) for Gmail and Contacts; WhatsApp Help Center (faq.whatsapp.com); Instagram Help Center (help.instagram.com); Facebook Help Center (www.facebook.com/help).

Write these 6 tasks, 6 examples each. Use the task_id and task_type exactly as given. Each task must use a different official page.

| task_id | task_type | task | platform | category | sensitive |
|---|---|---|---|---|---|
| TR-206 | block_number | Block a contact | WhatsApp | communication | False |
| TR-207 | group_text | Create a group chat | WhatsApp | communication | False |
| TR-208 | share_location | Share live location with someone | WhatsApp | communication | True |
| TR-209 | two_step_verification | Turn on two-step verification | WhatsApp | online_services | True |
| TR-210 | social_media_privacy | Make the account private | Instagram | communication | True |
| TR-211 | account_password_reset | Get back into the account when you cannot log in | Facebook | online_services | True |

Backup topics (if a topic's page cannot be read or does not cover the core action, replace it with one of these and reuse that topic's task_id; if you run out, deliver fewer tasks):

- video_captions | Turn on captions in a meeting | Zoom (support.zoom.com) | technical_support | False
- mute_chat | Mute notifications for a chat | WhatsApp | communication | False

Tasks marked sensitive True that are about settings or accounts (not scams) still use the normal device table (a, c, b, d, e, r).

Notes: WhatsApp, Instagram, and Facebook pages often give separate Android and iPhone steps; then the missing detail is the type of phone and direct examples name the phone. Do not write about forwarding email, CC, signatures, creating a new email account, unsending messages, or video calls.

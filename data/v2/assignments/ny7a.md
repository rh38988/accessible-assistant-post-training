# Assignment: batch ny7a

Spec file: `data/v2/specs/ny7a.py`

Publishers: Microsoft (support.microsoft.com) for Outlook.com; Google (support.google.com/mail, /contacts) for Gmail and Contacts; WhatsApp Help Center (faq.whatsapp.com); Instagram Help Center (help.instagram.com); Facebook Help Center (www.facebook.com/help).

Write these 7 tasks, 6 examples each. Use the task_id and task_type exactly as given. Each task must use a different official page.

| task_id | task_type | task | platform | category | sensitive |
|---|---|---|---|---|---|
| TR-199 | email_attach | Attach a file or photo to an email | Outlook.com | communication | False |
| TR-200 | mark_spam_email | Mark an email as junk or block the sender | Outlook.com | communication | True |
| TR-201 | recover_deleted_email | Recover a deleted email | Outlook.com | communication | False |
| TR-202 | email_labels | Organize email with labels | Gmail (computer) | communication | False |
| TR-203 | auto_reply | Set an out-of-office (vacation) reply | Gmail (computer) | communication | False |
| TR-204 | print_email | Print an email | Gmail (computer) | communication | False |
| TR-205 | add_contact | Add a contact | Google Contacts (computer) | communication | False |

Backup topics (if a topic's page cannot be read or does not cover the core action, replace it with one of these and reuse that topic's task_id; if you run out, deliver fewer tasks):

- join_video_meeting | Join a meeting from an invitation link | Google Meet (support.google.com/meet) | communication | False
- email_not_working | Email is not arriving or syncing | Outlook.com | communication | False

Tasks marked sensitive True that are about settings or accounts (not scams) still use the normal device table (a, c, b, d, e, r).

Notes: WhatsApp, Instagram, and Facebook pages often give separate Android and iPhone steps; then the missing detail is the type of phone and direct examples name the phone. Do not write about forwarding email, CC, signatures, creating a new email account, unsending messages, or video calls.

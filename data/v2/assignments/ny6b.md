# Assignment: batch ny6b

Spec file: `data/v2/specs/ny6b.py`

Publishers: Google (support.google.com: Chrome Help, Google Account Help, Google One or Drive Help, Maps Help); Microsoft (support.microsoft.com) for Edge tasks.

Write these 6 tasks, 6 examples each. Use the task_id and task_type exactly as given. Each task must use a different official page.

| task_id | task_type | task | platform | category | sensitive |
|---|---|---|---|---|---|
| TR-193 | app_notifications_off | Stop a website from sending notifications | Chrome (computer) | technical_support | False |
| TR-194 | live_captions | Turn on Live Caption | Chrome (computer) | technical_support | False |
| TR-195 | sign_out | Sign out of a Google Account on a shared computer or another device | Google Account | online_services | True |
| TR-196 | recovery_info | Add a recovery phone number or email | Google Account | online_services | True |
| TR-197 | free_storage | Free up Google account storage | Google Account (Drive, Gmail, Photos) | online_services | False |
| TR-198 | maps_directions | Get directions on a computer | Google Maps (computer) | online_services | False |

Backup topics (if a topic's page cannot be read or does not cover the core action, replace it with one of these and reuse that topic's task_id; if you run out, deliver fewer tasks):

- read_aloud | Have a web page read aloud | Microsoft Edge (computer) | technical_support | False
- family_sharing | Share purchased apps with family (Google Play Family Library) | Android | technical_support | False

Tasks marked sensitive True that are about settings or accounts (not scams) still use the normal device table (a, c, b, d, e, r).

Notes: For browser tasks the missing detail is usually which browser, or computer versus phone. Do not write about clearing browsing history or browsing data.

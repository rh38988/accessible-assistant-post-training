# Assignment: batch ny6a

Spec file: `data/v2/specs/ny6a.py`

Publishers: Google (support.google.com: Chrome Help, Google Account Help, Google One or Drive Help, Maps Help); Microsoft (support.microsoft.com) for Edge tasks.

Write these 7 tasks, 6 examples each. Use the task_id and task_type exactly as given. Each task must use a different official page.

| task_id | task_type | task | platform | category | sensitive |
|---|---|---|---|---|---|
| TR-186 | bookmark_site | Save a website as a favorite | Microsoft Edge (computer) | technical_support | False |
| TR-187 | bookmark_site | Bookmark a website in Chrome on the phone | Chrome (Android) | technical_support | False |
| TR-188 | browser_zoom | Make web pages bigger | Microsoft Edge (computer) | technical_support | False |
| TR-189 | popups | Block pop-ups | Chrome (computer) | technical_support | False |
| TR-190 | default_browser | Make Chrome the default browser | Chrome (Windows computer) | technical_support | False |
| TR-191 | find_downloads | Find a file downloaded with Chrome | Chrome (computer) | technical_support | False |
| TR-192 | password_manager | Save and find passwords with Google Password Manager | Chrome (computer) | online_services | True |

Backup topics (if a topic's page cannot be read or does not cover the core action, replace it with one of these and reuse that topic's task_id; if you run out, deliver fewer tasks):

- print_webpage | Print a web page | Chrome (computer) | technical_support | False
- browser_zoom | Make web pages bigger | Firefox (computer), support.mozilla.org | technical_support | False

Tasks marked sensitive True that are about settings or accounts (not scams) still use the normal device table (a, c, b, d, e, r).

Notes: For browser tasks the missing detail is usually which browser, or computer versus phone. Do not write about clearing browsing history or browsing data.

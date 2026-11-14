# RAG source gaps, v1 (Data Lead, 2026-11-13)

Format: the `retrieval/README.md` on GitHub main (one `.md` per page, `Source:` and `Accessed:` headers, steps summarized in our own words, exact button names). The 41-record corpus, `corpus_manifest.json`, and loader exist only on a teammate's machine, so these docs still need converting to that schema once it is pushed. No eval prompts, reference answers, or `expected_elements` were used to write them.

| Gap (from the retrieval audit) | Eval tasks it serves | Added | Status |
|---|---|---|---|
| Video calls | EV-001, EV-135 (FaceTime), EV-030 (telehealth link, partly) | `apple_facetime_call.md`, `apple_group_facetime.md` | Done |
| Video calls, Android / WhatsApp | EV-002 (Google Meet), EV-003 (WhatsApp) | none | **Open**: Google's calling guidebook and faq.whatsapp.com could not be read by the fetch tool. Needs a person to copy the steps from the page. |
| Money transfers | EV-035 (Zelle), EV-036 (money sent by mistake) | `ftc_after_a_scam.md` (bank transfer / Zelle), `ftc_payment_apps.md` | Partly: the FTC page does not cover the "sent by mistake, please send it back" story; Zelle's own help pages not yet added. |
| Remote-access recovery | EV-005, EV-006 (tech support scams) | `ftc_tech_support_scams.md`, `ftc_after_a_scam.md` | Done |

Check: `python retrieval/bm25.py "my grandson wants to facetime me"` and `python retrieval/bm25.py "a man on the phone got into my computer"` both return the new docs first.

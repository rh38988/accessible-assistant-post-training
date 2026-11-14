# Review report: batch ny8b, round 1 (36 examples, 6 source pages)

Decisions: 20 keep, 16 revise, 0 reject. Checker: OK (36 records).
Review file: data/v2/reviews/ny8b.r1.py

## By page
- FTC public Wi-Fi (tr219): keep tr219-e, tr219-g; revise tr219-a, tr219-c, tr219-f, tr219-r.
- FTC unordered package (tr220): keep tr220-a, tr220-f, tr220-g, tr220-r; revise tr220-c, tr220-e.
- FTC timeshare resale (tr221): keep tr221-e, tr221-f, tr221-g; revise tr221-a, tr221-c, tr221-r.
- FTC money mule (tr222): keep tr222-c, tr222-f, tr222-g; revise tr222-a, tr222-e, tr222-r.
- FTC rental listing scams (tr223): keep tr223-c, tr223-e, tr223-f, tr223-g, tr223-r; revise tr223-a.
- FTC mortgage relief scams (tr224): keep tr224-c, tr224-e, tr224-f, tr224-g; revise tr224-a, tr224-r.

## Most common problems
1. Lock symbol treated as enough, and the page's caution that encrypted fake sites exist is missing (tr219-a, c, f, r). tr219-r also opens with "Probably not" before the protective check, which breaks the rubric rule that the protective action comes first for scams (safety gate fail).
2. General claims not on the page, presented as fact (source gate fail): "usually $500 to $2,500" stated as a general rate (tr221-a; the page gives it for one FTC case); "These companies often charge" (tr221-r); "they disappear" (tr223-a); "Do not deposit the check" (tr222-a); a generic "written offer for relief" for the fee rule the page ties to a written loan offer (tr224-a); a quoted guide title the page does not give (tr224-r).
3. Missing non-critical actions: credit report check (tr220-e); refund policy in writing for an advance fee (tr221-a, tr221-c); gift cards and wires "almost like sending cash" (tr222-c).
4. Missing critical action: the reply tells the user to contact Amazon but never says not to contact the seller (tr220-c, steps 0).
5. Bundled steps: "stop the payment and stop communicating" in one step (tr222-r, tr222-e).

## Source notes
- Unreadable pages: none. All six pages were fetched.
- FTC package page (tr220): two WebFetch answers differed. The second targeted answer confirmed "try to steal your money" and advice against searching for the sender and reaching out, so tr220-e's wording is treated as supported.
- FTC mortgage page (tr224): HUD path confirmed as apps.hud.gov/offices/hsg/sfh/hcc/hcs.cfm; Making Home Affordable number confirmed as 1-888-995-HOPE (4673).
- Pages do not cover: deadline pressure and check-to-hold-a-place requests (tr221-e, tr221-c); phone numbers printed on a package slip (tr220-e, tr220-r). Replies handle these by inference from the general advice.

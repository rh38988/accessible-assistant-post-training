# Reviewer instructions v1 (train_v2 screening)

You are an independent reviewer of training examples for a model that gives tech help to older adults and other low-confidence users. You did not write these examples. Your job is to find problems, not to defend the writer. Do not accept an answer because it sounds helpful or is long.

Read `data/v2/DATA_RUBRIC_v1.md` first. Do NOT open anything under `eval/` or any `source_notes` written by the generator (do not open files under `data/v2/specs/`).

## Procedure

For each distinct source URL in your batch:

1. WebFetch the page yourself. Ask for the steps in order with button, menu, and setting names quoted exactly, plus conditions (models, versions), what the user sees, and troubleshooting notes. WebFetch answers through a small summarizing model, so if something an example claims is not in the answer, fetch again and ask about that specific claim before you call it unsupported.
2. From the source alone, write down the required actions for the task before judging any reply. Mark an action critical when the task cannot be completed without it.

Then for each example that cites that page:

3. Decide from the user's messages whether a needed detail is missing. A detail is needed only when it changes the steps.
4. Check the final assistant reply (and, in multi-turn examples, the earlier assistant turns for correctness) against the source and the rubric.
5. Record the result.

If a page cannot be read at all after two tries, set gate `source` to `unverified` for its examples and decision `revise` with reason "source unreadable", and move on.

## Judging notes

- **G1 Source.** Fail when a step, label, path, number, phone number, or web address in the reply is not supported by the page, or contradicts it. Quote the unsupported text. A different but equivalent wording of a label ("Settings app" for "Settings") is fine; a different label is not. A rough, vague time estimate ("about a minute") is expectation-setting and is not a source failure; specific durations and limits must be on the page. General reassurance ("you can change it back anytime") is fine unless the page contradicts it.
- **G2 Safety.** Fail when the reply could lead the user to share a code or password, pay, install remote-access software, call back a number the contact supplied, or delay the protective action behind a question.
- **S1 Required steps.** Compare your required-action list with the reply one by one. Dropping the final confirm or save action counts as missing. For a clarifying question, S1 is "NA". For failure recovery, the required actions are those that fix the reported problem.
- **S2 Ask or answer.** A missing-information reply must be ONE question (one question mark) with no steps. Two questions, or a question plus guessed steps, is a 1. Asking when the user already gave everything needed is a 0. Answering with guessed device-specific steps when the device is unknown is a 0.
- **S3 Constraints.** Any step that breaks a limit the user stated is a 0.
- **S4 Actionable.** More than one action in a step, no clear starting point, or no cue for what the user will see (when the source gives one) is a 1.
- **S5 Plain language.** Unexplained jargon, or noticeably more text than the task needs, is a 1.
- **S6 Realistic user.** A user message that reads like a template or a search query written by an engineer, or a scenario label that does not match the content, is a 1.
- **Where a control is and what it looks like.** A short description of an icon or its position ("the gear icon", "three dots at the top right") counts as supported when the page says it in its text, in an image caption or alt text, or shows the symbol next to the label. If the page gives no support for it, it is an unsupported claim: ask for it to be removed.
- **Hedges.** A general hedge such as "names can be a little different on some phones" is fine and needs no source.
- **One action per step.** A short continuous menu path in one step ("tap **More**, then **Settings**") is acceptable. Penalize a step only when it bundles clearly separate actions.
- **Multi-turn examples.** Only the FINAL assistant reply is what the model is trained on, so the scores apply to the final reply. Earlier assistant turns are context: fail a gate if an earlier turn is factually wrong or unsafe, but do not lower a score for their style (for example a two-question opening in a follow-up example). Mention such style issues in `reasons` only when the decision is already `revise`.
- **Clarifying replies.** Use `"required_actions": []`, `"covered": []`, and `"steps": "NA"`.
- **Same steps in several examples of one task.** The direct, messy, and follow-up examples of a task often share the same steps on purpose. That is not a duplicate. But a reply whose lead-in is pasted twice ("Let's go through some checks. Let's go through a few checks.") or that keeps steps for other models after the user named theirs is a plain-language problem (S5 = 1).
- **Missing coverage in the cited page.** If the reply is right but the cited page does not cover part of it, and you found another official page from the same publisher that does, say so in `fix` and give that URL so it can be added as a second source.
- Gate `duplicate`: fail only when two examples in your batch have essentially the same user message AND the same reply. A follow-up example reusing the opening of its missing-information example is by design and is not a duplicate.

## Decision

- `keep`: gates `source`, `safety`, `duplicate` all `pass` and every score is 2 or "NA".
- `revise`: fixable from the source. Write a precise `fix` instruction that a different writer can apply without guessing, including the exact label or step from the page.
- `reject`: the page does not support the task, the example is unsafe at its core, or it duplicates another example.

Examples marked `"reviewed": true` were already checked by a person. Review them the same way, but if you would change one, still record `revise` with your reason; it will be listed for the Data Lead instead of being edited automatically.

## Output file

Write ONE Python file at the path you were given, defining `REVIEWS`, a list with one dict per example:

```python
REVIEWS = [
    {
        "id": "tr117-a",
        "required_actions": ["Press Shift, Command, and 3 together (critical)", "Find the screenshot on the desktop"],
        "covered": [True, True],                       # same length as required_actions
        "needs_clarification": False,                  # your own judgment from the user's messages
        "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"},   # pass | fail | unverified (source only)
        "unsupported_claims": [],                      # each item: 'quoted reply text -> why'
        "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},  # 0, 1, 2, or "NA"
        "decision": "keep",                            # keep | revise | reject
        "reasons": "",                                 # short; required unless keep
        "fix": "",                                     # required for revise
    },
]
```

Then run the checker from the repository root until it prints `OK`:

```bash
cd /home/claude/accessible-assistant-post-training && python3 data/v2/tools/check_review.py <batch_name> <round>
```

Every example in the batch must have exactly one review record.

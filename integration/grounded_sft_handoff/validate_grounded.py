"""Validate grounded SFT JSONL with the actual train_sft preprocessing, offline.

No model weights, judge, generation, or training are loaded. Example:
  .venv/Scripts/python.exe integration/grounded_sft_handoff/validate_grounded.py \
    integration/grounded_sft_handoff/DEMONSTRATIONS.jsonl \
    --provenance integration/grounded_sft_handoff/DEMONSTRATION_PROVENANCE.jsonl \
    --against data/v2/train_v2_en_ready.jsonl
"""

import argparse
import csv
from difflib import SequenceMatcher
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from scripts.validate_data import check_record
from training.train_sft import to_prompt_completion
from integration.grounded_sft_handoff.prompt_contract import build_messages, user_only_query

MODEL_REVISION = 'aa8e72537993ba99e69dfaafa59ed015b17504d1'
REQUIRED_REVIEW_CHECKS = (
    'factual_steps_labels_contacts_claims',
    'necessary_action_coverage',
    'explicit_constraints_and_completed_state',
    'clarification_decision',
    'no_invented_history_or_unsupported_content',
    'one_action_per_step',
    'brevity_without_omission',
    'safety',
)


def canonical_messages(messages):
    return json.dumps(messages, ensure_ascii=False, sort_keys=True,
                      separators=(',', ':')).encode('utf-8')


def load_jsonl(path):
    rows = []
    with Path(path).open(encoding='utf-8') as handle:
        for line_number, line in enumerate(handle, 1):
            if line.strip():
                try:
                    rows.append(json.loads(line))
                except json.JSONDecodeError as exc:
                    raise ValueError(f'{path}:{line_number}: invalid JSON: {exc}') from exc
    return rows


def normalized(text):
    return re.sub(r'\s+', ' ', re.sub(r'[^a-z0-9 ]+', ' ', text.lower())).strip()


def validate(args):
    rows = load_jsonl(args.file)
    errors, warnings = [], []
    if not args.provenance:
        errors.append('Source/generation and inference-template provenance is required')
    if args.expected_count is not None and len(rows) != args.expected_count:
        errors.append(f'Expected {args.expected_count} records; found {len(rows)}')
    ids = [r.get('id') for r in rows if isinstance(r, dict)]
    if len(set(ids)) != len(rows):
        errors.append('IDs are missing or duplicated')
    for number, row in enumerate(rows, 1):
        check_record(row, 'train', errors, f'{args.file}:{number}')
        if not isinstance(row, dict) or not isinstance(row.get('messages'), list) or len(row['messages']) < 2:
            continue
        if row.get('language') != 'en':
            errors.append(f"{row.get('id')}: this handoff requires English")
        if row.get('prompt_format') != 'rag-system-v1':
            errors.append(f"{row.get('id')}: prompt_format must be rag-system-v1")
        if not row.get('task_id') or not row.get('task_group') or not row.get('source_group'):
            errors.append(f"{row.get('id')}: task_id, task_group, source_group required")
        if len(row['messages']) != 3 or [m.get('role') for m in row['messages']] != [
                'system', 'user', 'assistant']:
            errors.append(f"{row.get('id')}: expected system, joined user conversation, final assistant")

    provenance, inference_messages = {}, {}
    if args.provenance:
        items = load_jsonl(args.provenance)
        provenance = {r['id']: r for r in items}
        if len(provenance) != len(items) or set(provenance) != set(ids):
            errors.append('Provenance must have exactly one row per training ID')
        for row in rows:
            rid = row['id']
            rec = provenance.get(rid)
            if not rec:
                continue
            digest = hashlib.sha256(canonical_messages(row['messages'])).hexdigest()
            if rec.get('content_sha256') != digest:
                errors.append(f'{rid}: provenance conversation hash does not match current messages')
            for key in ('task_id', 'task_group', 'source_group'):
                if rec.get(key) != row.get(key):
                    errors.append(f'{rid}: provenance {key} mismatch')
            source_urls = {s['url'] for s in row['sources']}
            refs = rec.get('source_refs', [])
            if not refs:
                errors.append(f'{rid}: no source provenance refs')
            for ref in refs:
                for key in ('ref_id', 'organization', 'url', 'access_date', 'section',
                            'applicability', 'verified_excerpt'):
                    if not ref.get(key):
                        errors.append(f'{rid}: source ref missing {key}')
                if ref.get('url') not in source_urls:
                    errors.append(f'{rid}: source URL differs from training metadata')
                if not str(ref.get('url', '')).startswith('https://'):
                    errors.append(f'{rid}: source must use HTTPS')
            template = rec.get('inference_template') or {}
            if (template.get('builder') != 'eval.generate_rag.build_messages' or
                    template.get('condition') != 'sft_v2_rag' or
                    template.get('accessibility') != ''):
                errors.append(f'{rid}: inference template metadata is missing or differs from ordinary RAG')
            try:
                source_conversation = template['source_conversation']
                decision = template['decision']
                sections = template['sections']
                if any(set(section) != {'platform', 'app', 'text'} for section in sections):
                    errors.append(f'{rid}: inference sections must contain only platform, app, text')
                query = user_only_query(source_conversation)
                expected = build_messages(query, decision, sections, accessibility='')
                inference_messages[rid] = expected
                if row['messages'][:-1] != expected:
                    errors.append(f'{rid}: training prefix does not match actual RAG inference messages')
                if decision['mode'] not in ('answer', 'clarify'):
                    errors.append(f'{rid}: accepted training examples require ANSWER or CLARIFY routing')
                if decision['mode'] == 'answer':
                    ref_ids = template['section_ref_ids']
                    if len(ref_ids) != len(sections) or len(ref_ids) != len(refs):
                        errors.append(f'{rid}: source references and RAG sections differ in count')
                    else:
                        for source_ref, ref_id, section in zip(refs, ref_ids, sections):
                            if (ref_id != source_ref['ref_id'] or
                                    section['text'] != source_ref.get('model_visible_text') or
                                    section['text'] not in row['messages'][0]['content']):
                                errors.append(f'{rid}: source passage not mapped to model-visible system content')
                elif sections or template.get('section_ref_ids'):
                    errors.append(f'{rid}: CLARIFY route must not include procedural sections')
            except (KeyError, TypeError, ValueError) as exc:
                errors.append(f'{rid}: cannot reconstruct inference prompt: {exc}')
            if not rec.get('generation') or 'correction_history' not in rec:
                errors.append(f'{rid}: generation and correction provenance required')

    with Path(args.eval_task_types).open(encoding='utf-8', newline='') as handle:
        eval_types = {r['task_type'] for r in csv.DictReader(handle)}
    for row in rows:
        if row.get('task_group') in eval_types:
            errors.append(f"{row['id']}: task group is assigned to existing evaluation")
    if args.task_clearance:
        with Path(args.task_clearance).open(encoding='utf-8', newline='') as handle:
            clearance = {r['task_group']: r for r in csv.DictReader(handle)}
        for row in rows:
            entry = clearance.get(row['task_group'])
            if not entry or entry.get('disposition') != 'allow_training' or not entry.get('owner'):
                errors.append(f"{row['id']}: frozen-test task clearance missing or not approved")
    elif args.require_task_clearance:
        errors.append('Evaluation-owner task clearance file is required')

    if args.against:
        existing = [r for path in args.against for r in load_jsonl(path)]
        existing_ids = {r['id'] for r in existing}
        existing_users = [(r['id'], normalized(m['content'])) for r in existing
                          for m in r['messages'] if m['role'] == 'user']
        for row in rows:
            if row['id'] in existing_ids:
                errors.append(f"{row['id']}: ID already used in comparison training file")
            comparison_texts = [row['messages'][1]['content']]
            if row['id'] in provenance:
                comparison_texts += [m['content'] for m in provenance[row['id']]
                                     .get('inference_template', {}).get('source_conversation', [])
                                     if m['role'] == 'user']
            for current_text in comparison_texts:
                current = normalized(current_text)
                current_words = set(current.split())
                for old_id, old_text in existing_users:
                    if current == old_text:
                        errors.append(f"{row['id']}: exact user-turn duplicate of {old_id}")
                    elif (current and old_text and
                          0.75 <= len(current) / len(old_text) <= 1.33 and
                          len(current_words & set(old_text.split())) >= max(4, int(len(current_words) * .55)) and
                          SequenceMatcher(None, current, old_text).ratio() >= 0.90):
                        warnings.append(f"{row['id']}: possible wording overlap with {old_id}; review manually")

    if args.require_ai_review:
        if not args.reviews:
            errors.append('Separate AI review file required for accepted examples')
        else:
            reviews = load_jsonl(args.reviews)
            by_id = {r['id']: r for r in reviews}
            if len(by_id) != len(reviews) or set(by_id) != set(ids):
                errors.append('AI review file must have exactly one final review per accepted ID')
            for row in rows:
                source = provenance.get(row['id'], {})
                basis = source.get('inference_template', {}).get('decision_basis', '')
                if (source.get('eligibility') != 'cleared_for_training' or
                        not basis or 'fixture' in basis.lower()):
                    errors.append(f"{row['id']}: source/task eligibility or real routing basis is missing")
                review = by_id.get(row['id'])
                if not review:
                    continue
                digest = hashlib.sha256(canonical_messages(row['messages'])).hexdigest()
                if review.get('conversation_sha256') != digest or review.get('decision') != 'keep':
                    errors.append(f"{row['id']}: accepted review does not bind to exact final conversation")
                if any(not review.get(field) for field in (
                        'review_id', 'candidate_id', 'reviewer_model',
                        'reviewer_prompt_sha256', 'reviewed_at')):
                    errors.append(f"{row['id']}: review provenance is incomplete")
                checks = review.get('checks') or {}
                failed_checks = [name for name in REQUIRED_REVIEW_CHECKS
                                 if checks.get(name) != 'pass']
                if failed_checks:
                    errors.append(f"{row['id']}: review checks not passed: {', '.join(failed_checks)}")
                source_checks = review.get('source_checks') or []
                reviewed_refs = {item.get('ref_id'): item for item in source_checks
                                 if isinstance(item, dict)}
                if len(reviewed_refs) != len(source_checks):
                    errors.append(f"{row['id']}: source checks have missing or duplicate ref IDs")
                for ref in provenance.get(row['id'], {}).get('source_refs', []):
                    check = reviewed_refs.get(ref['ref_id'])
                    if (not check or check.get('official_url') != ref['url'] or
                            check.get('source_accessible') is not True or
                            check.get('applicability_confirmed') is not True or
                            not check.get('finding')):
                        errors.append(f"{row['id']}: official source review missing or unresolved for {ref['ref_id']}")
                for action in review.get('required_actions') or []:
                    if action.get('critical') is True and action.get('covered_in_target') is not True:
                        errors.append(f"{row['id']}: critical reviewed action is absent from the target")
                if review.get('findings') or review.get('correction_required'):
                    errors.append(f"{row['id']}: review has unresolved findings or correction")

    if errors:
        return {'status': 'failed', 'count': len(rows), 'errors': errors, 'warnings': warnings}

    # The same preprocessing method as training/train_sft.py, with truncation
    # disabled for measurement; no model weights or training call.
    from datasets import Dataset
    from transformers import AutoTokenizer
    from trl import SFTConfig, SFTTrainer
    from trl.trainer.sft_trainer import DataCollatorForLanguageModeling

    snapshot = (Path.home() / '.cache/huggingface/hub/models--Qwen--Qwen2.5-3B-Instruct/snapshots'
                / MODEL_REVISION)
    if not snapshot.is_dir():
        raise FileNotFoundError(f'Cached tokenizer revision unavailable: {snapshot}')
    tokenizer = AutoTokenizer.from_pretrained(str(snapshot), local_files_only=True)
    config = SFTConfig(output_dir=str(ROOT / 'integration/grounded_sft_handoff/.unused'),
        max_length=None, completion_only_loss=True, packing=False, padding_free=False,
        report_to='none')
    dataset = Dataset.from_list([to_prompt_completion(r) for r in rows])
    processed = SFTTrainer._prepare_dataset(None, dataset, tokenizer, config,
        packing=False, formatting_func=None, dataset_name='grounded_sft_validation')
    collator = DataCollatorForLanguageModeling(pad_token_id=tokenizer.pad_token_id,
        completion_only_loss=True, padding_free=False)
    lengths, results = [], []
    for start in range(0, len(rows), 8):
        batch_items = [processed[i] for i in range(start, min(start + 8, len(rows)))]
        collated = collator(batch_items)
        for offset, item in enumerate(batch_items):
            row = rows[start + offset]
            rid = row['id']
            ids = item['input_ids']
            mask = item['completion_mask']
            prompt_len = len(mask) - sum(mask)
            if ids != tokenizer.apply_chat_template(row['messages']):
                errors.append(f'{rid}: TRL token IDs differ from complete Qwen chat template')
            if mask != [0] * prompt_len + [1] * (len(ids) - prompt_len):
                errors.append(f'{rid}: completion mask is not final-turn-only')
            labels = collated['labels'][offset].tolist()
            if (any(x != -100 for x in labels[:prompt_len]) or
                labels[prompt_len:len(ids)] != ids[prompt_len:] or
                any(x != -100 for x in labels[len(ids):])):
                errors.append(f'{rid}: actual collated labels do not mask prompt/padding only')
            rendered = tokenizer.apply_chat_template(row['messages'], tokenize=False)
            inference = inference_messages[rid]
            inference_rendered = tokenizer.apply_chat_template(inference, tokenize=False,
                add_generation_prompt=True)
            inference_ids = tokenizer.apply_chat_template(inference,
                add_generation_prompt=True)
            assistant_header_ids = tokenizer.encode('<|im_start|>assistant\n',
                add_special_tokens=False)
            if (row['messages'][:-1] != inference or
                    not rendered.startswith(inference_rendered) or
                    ids[:len(inference_ids)] != inference_ids):
                errors.append(f'{rid}: train/inference message or chat-template prefix differs')
            if inference_ids[prompt_len:] != assistant_header_ids:
                errors.append(f'{rid}: expected assistant generation header is not the only prefix difference')
            if any(m['content'] not in rendered for m in inference):
                errors.append(f'{rid}: system instructions, references or user conversation lost')
            if provenance:
                if provenance[rid]['inference_template']['decision']['mode'] == 'answer':
                    for ref in provenance[rid]['source_refs']:
                        if ref['model_visible_text'] not in rendered:
                            errors.append(f'{rid}: source passage lost during preprocessing')
            lengths.append(len(ids))
            if len(ids) > args.max_length:
                errors.append(f'{rid}: {len(ids)} tokens exceed {args.max_length}; no truncation allowed')
            results.append({'id': rid, 'full_tokens_before_truncation': len(ids),
                'prompt_tokens_masked': prompt_len, 'supervised_tokens': len(ids) - prompt_len,
                'inference_prompt_tokens': len(inference_ids),
                'assistant_header_tokens_supervised': len(assistant_header_ids),
                'inference_messages_sha256': hashlib.sha256(canonical_messages(inference)).hexdigest(),
                'training_prefix_messages_sha256': hashlib.sha256(
                    canonical_messages(row['messages'][:-1])).hexdigest(),
                'inference_rendering_sha256': hashlib.sha256(
                    inference_rendered.encode('utf-8')).hexdigest(),
                'training_rendering_sha256': hashlib.sha256(rendered.encode('utf-8')).hexdigest(),
                'inference_messages_match': row['messages'][:-1] == inference,
                'chat_template_prefix_match': rendered.startswith(inference_rendered),
                'input_roles': [m['role'] for m in row['messages']],
                'final_assistant_only': True,
                'reference_text_in_model_input': provenance[rid]['inference_template']['decision']['mode'] == 'answer'})
    return {'status': 'passed' if not errors else 'failed', 'count': len(rows),
            'tokenizer_revision': MODEL_REVISION, 'max_length': args.max_length,
            'max_full_tokens': max(lengths, default=0), 'results': results,
            'errors': errors, 'warnings': sorted(set(warnings))}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('file', type=Path)
    parser.add_argument('--provenance', type=Path)
    parser.add_argument('--reviews', type=Path)
    parser.add_argument('--require-ai-review', action='store_true')
    parser.add_argument('--expected-count', type=int)
    parser.add_argument('--max-length', type=int, default=1028)
    parser.add_argument('--against', type=Path, nargs='*')
    parser.add_argument('--eval-task-types', type=Path, default=ROOT / 'eval/tasks/eval_tasks.csv')
    parser.add_argument('--task-clearance', type=Path)
    parser.add_argument('--require-task-clearance', action='store_true')
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    result = validate(args)
    output = json.dumps(result, ensure_ascii=False, indent=2)
    if args.report:
        with args.report.open('x', encoding='utf-8') as handle:
            handle.write(output + '\n')
    print(output)
    raise SystemExit(0 if result['status'] == 'passed' else 1)


if __name__ == '__main__':
    main()

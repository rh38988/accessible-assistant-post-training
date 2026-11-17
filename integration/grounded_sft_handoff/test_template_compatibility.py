"""Template compatibility tests for the new grounded SFT handoff."""

from argparse import Namespace
import copy
import importlib.util
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from integration.grounded_sft_handoff.prompt_contract import build_messages, user_only_query
from scripts.validate_data import check_record
from training.train_sft import to_prompt_completion
from integration.grounded_sft_handoff.validate_grounded import validate

ROOT = Path(__file__).resolve().parents[2]
PACKAGE = Path(__file__).resolve().parent
LEGACY_DATASET = ROOT / 'data/v2/train_v2_en_ready.jsonl'
if not LEGACY_DATASET.is_file():
    LEGACY_DATASET = ROOT / 'data/v2/versions/train_v2_en.v2.1.jsonl'


def read_jsonl(path):
    return [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines()
            if line.strip()]


class TemplateCompatibilityTests(unittest.TestCase):
    def test_legacy_record_keeps_its_original_roles_and_split(self):
        old = read_jsonl(LEGACY_DATASET)[0]
        self.assertNotIn('prompt_format', old)
        errors = []
        check_record(old, 'train', errors, 'legacy')
        self.assertEqual(errors, [])
        split = to_prompt_completion(old)
        self.assertEqual(split['prompt'], old['messages'][:-1])
        self.assertEqual(split['completion'], [old['messages'][-1]])

    def test_legacy_schema_does_not_accept_an_unmarked_system_role(self):
        old = read_jsonl(LEGACY_DATASET)[0]
        old['messages'] = [{'role': 'system', 'content': 'unmarked'}, *old['messages']]
        errors = []
        check_record(old, 'train', errors, 'legacy-with-system')
        self.assertTrue(errors)

    def test_grounded_demos_exactly_match_the_existing_inference_builder(self):
        rows = read_jsonl(PACKAGE / 'DEMONSTRATIONS.jsonl')
        provenance = read_jsonl(PACKAGE / 'DEMONSTRATION_PROVENANCE.jsonl')
        self.assertEqual(len(rows), 2)
        for row, source in zip(rows, provenance):
            with self.subTest(id=row['id']):
                errors = []
                check_record(row, 'train', errors, row['id'])
                self.assertEqual(errors, [])
                self.assertEqual(row['prompt_format'], 'rag-system-v1')
                self.assertEqual([m['role'] for m in row['messages']],
                                 ['system', 'user', 'assistant'])
                template = source['inference_template']
                query = user_only_query(template['source_conversation'])
                expected = build_messages(query, template['decision'],
                                          template['sections'], accessibility='')
                self.assertEqual(row['messages'][:-1], expected)
                self.assertEqual(row['messages'][1]['content'], query)
                self.assertNotIn('Reference passages for this request',
                                 row['messages'][1]['content'])
                for section in template['sections']:
                    self.assertIn(section['text'], row['messages'][0]['content'])
                split = to_prompt_completion(row)
                self.assertEqual(split['prompt'], expected)
                self.assertEqual(split['completion'], [row['messages'][-1]])

    def test_previous_assistant_turn_is_not_hidden_inside_user_text(self):
        row = read_jsonl(PACKAGE / 'DEMONSTRATIONS.jsonl')[1]
        source = read_jsonl(PACKAGE / 'DEMONSTRATION_PROVENANCE.jsonl')[1]
        conversation = source['inference_template']['source_conversation']
        earlier_assistant = next(m['content'] for m in conversation
                                 if m['role'] == 'assistant')
        self.assertNotIn(earlier_assistant, row['messages'][1]['content'])
        self.assertIn('I got to Mouse pointer and touch already',
                      row['messages'][1]['content'])

    def test_portable_prompt_contract_matches_actual_inference_when_available(self):
        if importlib.util.find_spec('eval.generate_rag') is None:
            self.skipTest('Historical inference builder is absent from this branch')
        from eval.generate_rag import RULES as actual_rules
        from eval.generate_rag import build_messages as actual_builder
        from retrieval.audit import user_only_query as actual_query
        from integration.grounded_sft_handoff.prompt_contract import RULES
        self.assertEqual(RULES, actual_rules)
        provenance = read_jsonl(PACKAGE / 'DEMONSTRATION_PROVENANCE.jsonl')
        for source in provenance:
            template = source['inference_template']
            conversation = template['source_conversation']
            self.assertEqual(user_only_query(conversation), actual_query(conversation))
            query = user_only_query(conversation)
            for decision in (template['decision'],
                             {'mode': 'clarify', 'question': 'Which device are you using?'},
                             {'mode': 'insufficient', 'question': ''}):
                with self.subTest(id=source['id'], mode=decision['mode']):
                    self.assertEqual(build_messages(query, decision, template['sections']),
                                     actual_builder(query, decision, template['sections']))

    def test_relocated_reference_is_rejected_before_tokenization(self):
        rows = copy.deepcopy(read_jsonl(PACKAGE / 'DEMONSTRATIONS.jsonl'))
        provenance = read_jsonl(PACKAGE / 'DEMONSTRATION_PROVENANCE.jsonl')
        source_text = provenance[0]['source_refs'][0]['model_visible_text']
        rows[0]['messages'][0]['content'] = rows[0]['messages'][0]['content'].replace(
            source_text, '')
        rows[0]['messages'][1]['content'] += '\n\n' + source_text
        with TemporaryDirectory() as directory:
            path = Path(directory) / 'relocated.jsonl'
            path.write_text(''.join(json.dumps(row) + '\n' for row in rows),
                            encoding='utf-8')
            args = Namespace(file=path, provenance=PACKAGE / 'DEMONSTRATION_PROVENANCE.jsonl',
                             reviews=None, require_ai_review=False, expected_count=2,
                             max_length=1028, against=None,
                             eval_task_types=ROOT / 'eval/tasks/eval_tasks.csv',
                             task_clearance=None, require_task_clearance=False)
            result = validate(args)
        self.assertEqual(result['status'], 'failed')
        self.assertTrue(any('training prefix does not match actual RAG inference messages' in error
                            for error in result['errors']))


if __name__ == '__main__':
    unittest.main()

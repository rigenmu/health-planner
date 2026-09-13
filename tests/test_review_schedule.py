import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.review_schedule import pending_reviews, timestamp


def state(anchor='2026-01-01', closed=None, reviews=None, zone='Asia/Shanghai'):
    return {'schema_version': 1, 'anchor_date': anchor, 'timezone': zone,
            'closed_through': closed, 'reviews': reviews or []}


def windows(result):
    return [w for b in result['delivery_batches'] for w in b['windows']]


class ReviewScheduleTests(unittest.TestCase):
    def test_day_six_and_unclosed_day_seven_are_not_due(self):
        for day in ['06', '07']:
            self.assertFalse(windows(pending_reviews(state(), timestamp(f'2026-01-{day}T12:00:00+08:00'))))

    def test_day_seven_closure_triggers_immediately(self):
        result = pending_reviews(state(closed='2026-01-07'), timestamp('2026-01-07T22:00:00+08:00'))
        self.assertEqual([w['period_id'] for w in windows(result)], ['7d:2026-01-01:2026-01-07'])

    def test_next_day_triggers_without_complete_records(self):
        result = pending_reviews(state(), timestamp('2026-01-08T08:00:00+08:00'))
        self.assertEqual(windows(result)[0]['calendar_days'], 7)

    def test_day_thirteen_cannot_complete_fourteen_days(self):
        result = pending_reviews(state(closed='2026-01-13'), timestamp('2026-01-13T23:00:00+08:00'))
        self.assertNotIn('14d', [w['kind'] for w in windows(result)])

    def test_day_fourteen_coalesces_week_and_fortnight(self):
        result = pending_reviews(state(closed='2026-01-14'), timestamp('2026-01-14T22:00:00+08:00'))
        batch = result['delivery_batches'][-1]
        self.assertEqual(batch['primary'], '14d')
        self.assertEqual([w['kind'] for w in batch['windows']], ['14d', '7d'])
        self.assertEqual(batch['windows'][0]['start'], '2026-01-01')
        self.assertEqual(batch['windows'][1]['start'], '2026-01-08')

    def test_generated_file_is_not_delivery(self):
        report = {'period_ids': ['7d:2026-01-01:2026-01-07'],
                  'generated_at': '2026-01-07T22:00:00+08:00', 'report_path': 'reviews/example.md'}
        result = pending_reviews(state(reviews=[report]), timestamp('2026-01-08T08:00:00+08:00'))
        self.assertEqual(windows(result)[0]['existing_report'], 'reviews/example.md')
        report['delivered_at'] = '2026-01-07T22:01:00+08:00'
        self.assertTrue(windows(pending_reviews(state(reviews=[report]), timestamp('2026-01-08T08:00:00+08:00'))))
        report['conversation_ref'] = 'synthetic-message-1'
        self.assertFalse(windows(pending_reviews(state(reviews=[report]), timestamp('2026-01-08T08:00:00+08:00'))))

    def test_delivery_is_independent_of_pending_discussion(self):
        report = {'period_ids': ['7d:2026-01-01:2026-01-07'],
                  'delivered_at': '2026-01-07T22:01:00+08:00',
                  'conversation_ref': 'synthetic-message-1', 'discussion_status': 'pending'}
        self.assertFalse(windows(pending_reviews(state(reviews=[report]), timestamp('2026-01-08T08:00:00+08:00'))))

    def test_month_overlap_is_one_batch_with_explicit_windows(self):
        result = pending_reviews(state(anchor='2026-01-18', closed='2026-01-31'), timestamp('2026-01-31T22:00:00+08:00'))
        batch = result['delivery_batches'][-1]
        self.assertEqual(batch['primary'], 'month')
        self.assertEqual([w['kind'] for w in batch['windows']], ['month', '14d', '7d'])
        self.assertTrue(batch['windows'][0]['partial_month'])

    def test_leap_month_and_year_boundary(self):
        for anchor, now, end, days in [('2024-02-01', '2024-03-01', '2024-02-29', 29),
                                      ('2025-12-01', '2026-01-01', '2025-12-31', 31)]:
            result = pending_reviews(state(anchor), timestamp(now + 'T08:00:00+08:00'))
            month = [w for w in windows(result) if w['kind'] == 'month'][0]
            self.assertEqual((month['end'], month['calendar_days']), (end, days))

    def test_local_timezone_determines_boundary(self):
        now = timestamp('2026-01-07T16:30:00Z')
        self.assertTrue(windows(pending_reviews(state(), now)))
        self.assertFalse(windows(pending_reviews(state(zone='America/Los_Angeles'), now)))

    def test_overdue_windows_remain_visible_and_input_is_unchanged(self):
        data = state()
        original = copy.deepcopy(data)
        result = pending_reviews(data, timestamp('2026-02-02T08:00:00+08:00'))
        self.assertEqual(len(windows(result)), 7)
        self.assertEqual(data, original)

    def test_future_closure_and_naive_timestamps_rejected(self):
        with self.assertRaises(ValueError):
            pending_reviews(state(closed='2026-01-14'), timestamp('2026-01-13T08:00:00+08:00'))
        with self.assertRaises(ValueError):
            timestamp('2026-01-14T08:00:00')

    def test_future_delivery_rejected(self):
        report = {'period_ids': ['7d:2026-01-01:2026-01-07'],
                  'delivered_at': '2026-01-09T08:00:00+08:00', 'conversation_ref': 'synthetic-message'}
        with self.assertRaises(ValueError):
            pending_reviews(state(reviews=[report]), timestamp('2026-01-08T08:00:00+08:00'))

    def test_cli_does_not_modify_state(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'state.json'
            original = json.dumps(state())
            path.write_text(original)
            script = Path(__file__).resolve().parents[1] / 'scripts/review_schedule.py'
            result = subprocess.run([sys.executable, str(script), '--state', str(path),
                                     '--as-of', '2026-01-08T08:00:00+08:00'], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(len(windows(json.loads(result.stdout))), 1)
            self.assertEqual(path.read_text(), original)


if __name__ == '__main__':
    unittest.main()

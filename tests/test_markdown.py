import unittest
from pathlib import Path

from scripts.check_response import PARSER, inspect_response

ROOT = Path(__file__).resolve().parents[1]


class MarkdownTests(unittest.TestCase):
    def test_reproduces_cjk_punctuation_failure(self):
        broken = '准备收尾了，**今晚先休息。**明早接着聊。'
        self.assertNotIn('<strong>', PARSER.render(broken))
        self.assertTrue(inspect_response(broken)['issues'])

    def test_corrected_sentence_preserves_text_and_emphasis(self):
        result = inspect_response('💬 准备收尾了，**今晚先休息**。明早接着聊。')
        self.assertEqual(result['issues'], [])
        self.assertEqual(result['strong_texts'], ['今晚先休息'])

    def test_rejects_literal_or_broken_delimiters(self):
        cases = [r'💬 \*\*今晚先休息\*\*。', '💬 **今晚先休息。',
                 '💬 &#42;&#42;今晚先休息&#42;&#42;。', '💬 ** 今晚先休息 **。',
                 '💬 **“今晚先休息”**，明早继续。', '💬 `**今晚先休息**`。',
                 '💬 **今天先\n结束记录**。', '```text\n**今晚先休息**\n```']
        for value in cases:
            with self.subTest(value=value):
                self.assertTrue(inspect_response(value)['issues'])

    def test_cjk_latin_numbers_and_colon(self):
        for value, expected in [
            ('**体重：72.4 kg**。', '体重：72.4 kg'),
            ('**Rest tonight**, then check in tomorrow.', 'Rest tonight'),
            ('💬 下次再看，**先按原计划继续**。', '先按原计划继续')]:
            with self.subTest(value=value):
                result = inspect_response(value)
                self.assertEqual(result['issues'], [])
                self.assertEqual(result['strong_texts'], [expected])

    def test_feedback_is_not_swallowed_by_quote(self):
        broken = '> 晚间记录\n💬 继续记录。'
        self.assertTrue(inspect_response(broken)['issues'])
        self.assertFalse(inspect_response('> 晚间记录\n\n💬 继续记录。')['issues'])

    def test_samples_render_with_only_intended_emphasis(self):
        expected = {
            'fragment.md': ['饭后活动：步行约 15 分钟', '晚餐后再接着记'],
            'daily.md': ['晚间活动：散步约 10 分钟', '先结束今天的记录'],
            'view-only.md': [],
            'review-opening.md': ['先挑出最值得调整的一两件事'],
        }
        for name, bold in expected.items():
            with self.subTest(name=name):
                text = (ROOT / 'evals/examples' / name).read_text(encoding='utf-8')
                result = inspect_response(text)
                self.assertEqual(result['issues'], [])
                self.assertEqual(result['strong_texts'], bold)
                self.assertNotIn('<code>', PARSER.render(text))
                if name != 'review-opening.md':
                    tokens = PARSER.parse(text)
                    self.assertGreaterEqual(sum(t.type == 'blockquote_open' for t in tokens), 3)
                    self.assertEqual(sum(t.type == 'bullet_list_open' for t in tokens), 0)


if __name__ == '__main__':
    unittest.main()

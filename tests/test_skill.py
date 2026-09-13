import re
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


class SkillTests(unittest.TestCase):
    def test_metadata_and_discovery(self):
        text = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
        data = yaml.safe_load(text.split('---', 2)[1])
        self.assertEqual(data['name'], 'health-planner')
        self.assertTrue(data['description'])
        config = yaml.safe_load((ROOT / 'agents/openai.yaml').read_text(encoding='utf-8'))
        self.assertTrue(config['policy']['allow_implicit_invocation'])
        self.assertIn('$health-planner', config['interface']['default_prompt'])

    def test_local_reference_targets_exist(self):
        for path in ROOT.rglob('*.md'):
            if '.git' in path.parts:
                continue
            for link in re.findall(r'\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
                if '://' in link or link.startswith('#'):
                    continue
                target = (path.parent / link.split('#')[0]).resolve()
                with self.subTest(path=path, target=target):
                    self.assertTrue(target.is_file())


if __name__ == '__main__':
    unittest.main()

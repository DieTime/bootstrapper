import unittest
import os
import sys

parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent)
from config import Config, DEFAULT_PRIORITY


class TestConfig(unittest.TestCase):
    def test_not_found(self):
        with self.assertRaises(RuntimeError):
            _ = Config('tests/assets/not-found.yaml')

    def test_invalid_syntax(self):
        with self.assertRaises(RuntimeError):
            _ = Config('tests/assets/invalid-syntax.yaml')

    def test_no_question(self):
        with self.assertRaises(RuntimeError):
            _ = Config('tests/assets/no-question.yaml')

    def test_empty_question(self):
        with self.assertRaises(RuntimeError):
            _ = Config('tests/assets/empty-question.yaml')

    def test_no_priotiry(self):
        cfg = Config('tests/assets/no-priority.yaml')
        self.assertEqual(cfg.get_priority(), DEFAULT_PRIORITY)

    def test_empty_priotiry(self):
        with self.assertRaises(RuntimeError):
            _ = Config('tests/assets/empty-priority.yaml')

    def test_no_steps(self):
        with self.assertRaises(RuntimeError):
            _ = Config('tests/assets/no-steps.yaml')

    def test_empty_steps(self):
        with self.assertRaises(RuntimeError):
            _ = Config('tests/assets/empty-steps.yaml')

    def test_valid(self):
        config_path = 'tests/assets/valid.yaml'
        config = Config(config_path)

        self.assertEqual(config.get_priority(), 1)
        self.assertEqual(config.get_name(), 'valid.yaml')
        self.assertEqual(config.get_path(), config_path)
        self.assertEqual(config.get_question(), 'Test config file?')
        self.assertEqual(config.get_dir(), 'tests/assets')
        self.assertListEqual(config.get_steps(), [
            {'Check invalid syntax': ['...', '...']},
            {'Check question section exists': ['...', '...']},
            {'Check steps section exists': ['...', '...']}
        ])


if __name__ == '__main__':
    unittest.main()

import unittest
from config import Config


class TestConfig(unittest.TestCase):
    def test_not_found(self):
        with self.assertRaises(RuntimeError):
            _ = Config('test-configs/not-found.yaml')

    def test_invalid_syntax(self):
        with self.assertRaises(RuntimeError):
            _ = Config('test-configs/invalid-syntax.yaml')

    def test_no_question(self):
        with self.assertRaises(RuntimeError):
            _ = Config('test-configs/no-question.yaml')

    def test_empty_question(self):
        with self.assertRaises(RuntimeError):
            _ = Config('test-configs/empty-question.yaml')

    def test_no_steps(self):
        with self.assertRaises(RuntimeError):
            _ = Config('test-configs/no-steps.yaml')

    def test_empty_steps(self):
        with self.assertRaises(RuntimeError):
            _ = Config('test-configs/empty-steps.yaml')

    def test_valid(self):
        config_path = 'test-configs/valid.yaml'
        config = Config(config_path)

        self.assertEqual(config.get_name(), 'valid.yaml')
        self.assertEqual(config.get_path(), config_path)
        self.assertEqual(config.get_question(), 'Test config file?')
        self.assertEqual(config.get_dir(), 'test-configs')
        self.assertListEqual(config.get_steps(), [
            {'Check invalid syntax': ['...', '...']},
            {'Check question section exists': ['...', '...']},
            {'Check steps section exists': ['...', '...']}
        ])


if __name__ == '__main__':
    unittest.main()

import unittest
from cybertoolkit.module_registry import ModuleRegistry
from cybertoolkit.config import Config

class TestCyberToolkit(unittest.TestCase):
    def test_module_registry(self):
        registry = ModuleRegistry()
        self.assertIsInstance(registry.modules, dict)
        self.assertGreater(len(registry.modules), 0)
    
    def test_config(self):
        config = Config()
        self.assertIsInstance(config.config, dict)
        self.assertIn('log_level', config.config)
    
    def test_config_get_set(self):
        config = Config()
        config.set('test_key', 'test_value')
        self.assertEqual(config.get('test_key'), 'test_value')

if __name__ == '__main__':
    unittest.main()
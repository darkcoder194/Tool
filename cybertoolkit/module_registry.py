import os
import importlib.util
import sys

class ModuleRegistry:
    def __init__(self):
        self.modules = {}
        sys.path.insert(0, os.getcwd())  # Add current dir to path for imports
        self.load_modules()

    def load_modules(self):
        # load from modules/
        self._load_from_dir('cybertoolkit/modules')
        # load from plugins/
        self._load_from_dir('cybertoolkit/plugins')

    def _load_from_dir(self, dirname):
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        for file in os.listdir(dirname):
            if file.endswith('.py') and not file.startswith('__'):
                path = os.path.join(dirname, file)
                spec = importlib.util.spec_from_file_location(file[:-3], path)
                module = importlib.util.module_from_spec(spec)
                try:
                    spec.loader.exec_module(module)
                    if hasattr(module, 'tool_info'):
                        info = module.tool_info()
                        self.modules[info['id']] = (info['name'], info['run'])
                except Exception as e:
                    print(f"Error loading {file}: {e}")

    def get_module(self, id):
        return self.modules.get(id)

    def list_modules(self):
        return self.modules

    def reload(self):
        self.modules = {}
        self.load_modules()

registry = ModuleRegistry()

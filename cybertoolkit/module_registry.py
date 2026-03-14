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

        # Walk the directory tree to support plugins installed as repos (subdirectories)
        for root, _, files in os.walk(dirname):
            for file in files:
                if not file.endswith('.py') or file.startswith('__'):
                    continue
                path = os.path.join(root, file)

                # Build a stable module name based on path so imports don't collide
                rel_path = os.path.relpath(path, dirname).replace(os.sep, '.')
                module_name = f"{dirname.replace(os.sep, '.')}.{rel_path[:-3]}"

                spec = importlib.util.spec_from_file_location(module_name, path)
                module = importlib.util.module_from_spec(spec)
                try:
                    spec.loader.exec_module(module)
                    if hasattr(module, 'tool_info'):
                        info = module.tool_info()
                        self.modules[info['id']] = (info['name'], info['run'])
                except Exception as e:
                    print(f"Error loading {path}: {e}")

    def get_module(self, id):
        return self.modules.get(id)

    def list_modules(self):
        return self.modules

    def reload(self):
        self.modules = {}
        self.load_modules()

registry = ModuleRegistry()

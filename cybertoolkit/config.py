import json
import os

class Config:
    def __init__(self):
        self.config_file = os.path.expanduser("~/.cybertoolkit/config.json")
        self.config = self.load_config()
    
    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                return json.load(f)
        else:
            # Default config
            default = {
                "log_level": "INFO",
                "output_format": "rich",
                "api_keys": {},
                "update_check": True
            }
            self.save_config(default)
            return default
    
    def save_config(self, config=None):
        if config is None:
            config = self.config
        os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
        with open(self.config_file, 'w') as f:
            json.dump(config, f, indent=4)
    
    def get(self, key, default=None):
        return self.config.get(key, default)
    
    def set(self, key, value):
        self.config[key] = value
        self.save_config()
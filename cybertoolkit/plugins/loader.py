import os
import importlib

def load_plugins():

    plugins=[]

    path="cybertoolkit/plugins"

    for file in os.listdir(path):

        if file.endswith(".py") and file not in ["__init__.py","loader.py"]:

            name=file[:-3]

            mod=importlib.import_module(f"cybertoolkit.plugins.{name}")

            plugins.append(mod.tool_info())

    return plugins

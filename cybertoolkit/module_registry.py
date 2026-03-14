import os
import importlib

MODULE_PATH="cybertoolkit.modules"

def load_modules():

    modules=[]

    folder="cybertoolkit/modules"

    for file in os.listdir(folder):

        if file.endswith(".py") and file!="__init__.py":

            name=file[:-3]

            mod=importlib.import_module(f"{MODULE_PATH}.{name}")

            modules.append(mod.tool_info())

    return modules

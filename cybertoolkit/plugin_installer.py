import subprocess
import os

PLUGIN_DIR="cybertoolkit/plugins"

def install_plugin(repo):

    name=repo.split("/")[-1]

    path=os.path.join(PLUGIN_DIR,name)

    subprocess.run(["git","clone",repo,path])

    print("Plugin installed:",name)

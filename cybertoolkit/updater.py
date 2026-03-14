import subprocess

def update():

    print("Updating toolkit...")

    subprocess.run(["git","pull"])

    print("Update complete")

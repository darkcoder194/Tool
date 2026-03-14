import pyfiglet
from rich.console import Console
from rich.table import Table

from cybertoolkit.auth import login_user, login_token
from cybertoolkit.module_registry import load_modules
from cybertoolkit.plugins.loader import load_plugins
from cybertoolkit.plugin_installer import install_plugin
from cybertoolkit.updater import update
from cybertoolkit.ai_assistant import run_ai
from cybertoolkit.ai_builder import run_ai_builder
from cybertoolkit.dashboard import show_dashboard

console=Console()

def banner():

    text=pyfiglet.figlet_format("CYBER TOOLKIT")

    console.print(text)


def show_tools():

    table=Table(title="Toolkit Modules")

    table.add_column("ID")
    table.add_column("Name")

    modules=load_modules()

    for m in modules:
        table.add_row(m["id"],m["name"])

    plugins=load_plugins()

    for p in plugins:
        table.add_row(p["id"],p["name"])

    console.print(table)


def run_module(cmd):

    modules = load_modules()

    for m in modules:
        if m["id"] == cmd:
            try:
                m["run"]()
            except Exception as e:
                console.print(f"[red]Module error:[/red] {e}")
            return True

    plugins = load_plugins()

    for p in plugins:
        if p["id"] == cmd:
            try:
                p["run"]()
            except Exception as e:
                console.print(f"[red]Plugin error:[/red] {e}")
            return True

    return False

def reload_system():

    console.print("[yellow]Reloading modules and plugins...[/yellow]")

    load_modules()
    load_plugins()

    console.print("[green]Reload complete[/green]")

def shell():

    show_dashboard()

    while True:

        cmd=input("cybertool > ").strip()

        if cmd=="exit":
            break

        elif cmd=="tools":
            show_tools()

        elif cmd=="reload":
            reload_system()

        elif cmd=="dashboard":
            show_dashboard()

        elif cmd.startswith("install "):

            repo=cmd.split(" ",1)[1]

            install_plugin(repo)

        elif cmd=="update":

            update()

        elif cmd=="ai":

            run_ai()

        elif cmd=="ai-build":

            run_ai_builder()

        else:

            if not run_module(cmd):
                print("Unknown command")



def start():

    print("1 Username Login")
    print("2 Token Login")

    c=input("Select: ")

    auth=False

    if c=="1":
        auth=login_user()

    if c=="2":
        auth=login_token()

    if auth:
        shell()
    else:
        print("Login failed")

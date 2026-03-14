import os
import subprocess
from rich.console import Console

console = Console()

def tool_info():
    return {
        "id": "install",
        "name": "Plugin Installer",
        "run": run
    }

def run(args):
    if not args:
        console.print("[red]Usage: install <github-repo-url>[/red]")
        return
    url = args[0]
    # assume https://github.com/user/repo
    parts = url.split('/')
    if len(parts) < 5:
        console.print("[red]Invalid URL[/red]")
        return
    repo_name = parts[-1]
    if repo_name.endswith('.git'):
        repo_name = repo_name[:-4]
    plugins_dir = 'plugins'
    if not os.path.exists(plugins_dir):
        os.makedirs(plugins_dir)
    dest = os.path.join(plugins_dir, repo_name)
    if os.path.exists(dest):
        console.print(f"[yellow]Plugin {repo_name} already installed[/yellow]")
        return
    try:
        subprocess.run(['git', 'clone', url, dest], check=True)
        console.print(f"[green]Plugin {repo_name} installed[/green]")
    except Exception as e:
        console.print(f"[red]Error installing plugin: {e}[/red]")

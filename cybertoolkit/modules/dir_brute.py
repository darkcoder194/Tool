import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from rich.progress import Progress
from rich.table import Table
from rich.console import Console

console = Console()

def tool_info():
    return {
        "id": "dir",
        "name": "Directory Brute-Force Scanner",
        "run": run
    }

def run(args):
    if not args:
        console.print("[red]Usage: dir <url> [threads][/red]")
        return
    url = args[0].rstrip('/')
    threads = int(args[1]) if len(args) > 1 else 10
    # Built-in wordlist
    wordlist = [
        'admin', 'login', 'dashboard', 'wp-admin', 'administrator', 'phpmyadmin',
        'test', 'dev', 'backup', 'config', 'api', 'upload', 'files', 'images',
        'css', 'js', 'assets', 'static', 'public', 'private', 'secret', 'hidden'
    ]
    found = []
    with Progress() as progress:
        task = progress.add_task(f"Scanning {url}...", total=len(wordlist))
        with ThreadPoolExecutor(max_workers=threads) as executor:
            futures = {executor.submit(check_dir, url, path): path for path in wordlist}
            for future in as_completed(futures):
                path = futures[future]
                result = future.result()
                if result:
                    found.append(result)
                progress.update(task, advance=1)
    if found:
        table = Table(title=f"Found directories on {url}")
        table.add_column("Path", style="cyan")
        table.add_column("Status")
        for path, status in found:
            table.add_row(path, str(status))
        console.print(table)
    else:
        console.print(f"[yellow]No directories found[/yellow]")

def check_dir(base_url, path):
    try:
        response = requests.get(f"{base_url}/{path}", timeout=5)
        if response.status_code == 200:
            return (f"/{path}", response.status_code)
    except:
        pass
    return None
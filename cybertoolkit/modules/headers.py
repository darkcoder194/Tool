import requests
from rich.table import Table
from rich.console import Console

console = Console()

def tool_info():
    return {
        "id": "headers",
        "name": "HTTP Headers Analyzer",
        "run": run
    }

def run(args):
    if not args:
        console.print("[red]Usage: headers <url>[/red]")
        return
    url = args[0]
    if not url.startswith('http'):
        url = 'http://' + url
    try:
        response = requests.head(url, timeout=10)
        table = Table(title=f"Headers for {url}")
        table.add_column("Header", style="cyan")
        table.add_column("Value")
        for key, value in response.headers.items():
            table.add_row(key, value)
        console.print(table)
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")

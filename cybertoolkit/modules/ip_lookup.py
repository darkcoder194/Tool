import requests
from rich.table import Table
from rich.console import Console

console = Console()

def tool_info():
    return {
        "id": "ip",
        "name": "IP Lookup",
        "run": run
    }

def run(args):
    if not args:
        console.print("[red]Usage: ip <ip_address>[/red]")
        return
    ip = args[0]
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}", timeout=10)
        data = response.json()
        if data.get('status') == 'success':
            table = Table(title=f"IP Information for {ip}")
            table.add_column("Field", style="cyan")
            table.add_column("Value")
            for key, value in data.items():
                table.add_row(key, str(value))
            console.print(table)
        else:
            console.print("[red]Failed to get IP info[/red]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")

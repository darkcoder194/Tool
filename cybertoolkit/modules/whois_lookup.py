import whois
from rich.table import Table
from rich.console import Console

console = Console()

def tool_info():
    return {
        "id": "whois",
        "name": "WHOIS Lookup",
        "run": run
    }

def run(args):
    if not args:
        console.print("[red]Usage: whois <domain>[/red]")
        return
    domain = args[0]
    try:
        w = whois.whois(domain)
        table = Table(title=f"WHOIS for {domain}")
        table.add_column("Field", style="cyan")
        table.add_column("Value")
        for key, value in w.items():
            if value:
                table.add_row(key, str(value))
        console.print(table)
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")

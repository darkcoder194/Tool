import socket
from rich.table import Table
from rich.console import Console

console = Console()

def tool_info():
    return {
        "id": "dns",
        "name": "DNS Lookup",
        "run": run
    }

def run(args):
    if not args:
        console.print("[red]Usage: dns <domain>[/red]")
        return
    domain = args[0]
    try:
        ip = socket.gethostbyname(domain)
        table = Table(title=f"DNS Lookup for {domain}")
        table.add_column("Type", style="cyan")
        table.add_column("Result")
        table.add_row("A Record", ip)
        try:
            hostname = socket.gethostbyaddr(ip)[0]
            table.add_row("Reverse DNS", hostname)
        except:
            pass
        console.print(table)
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")

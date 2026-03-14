import socket
from rich.table import Table
from rich.console import Console

console = Console()

def tool_info():
    return {
        "id": "sub",
        "name": "Subdomain Finder",
        "run": run
    }

def run(args):
    if not args:
        console.print("[red]Usage: sub <domain>[/red]")
        return
    domain = args[0]
    subdomains = ['www', 'mail', 'ftp', 'admin', 'test', 'dev', 'api', 'blog', 'ns1', 'ns2', 'shop', 'm', 'beta', 'portal']
    found = []
    for sub in subdomains:
        full = f"{sub}.{domain}"
        try:
            ip = socket.gethostbyname(full)
            found.append((full, ip))
        except:
            pass
    if found:
        table = Table(title=f"Subdomains for {domain}")
        table.add_column("Subdomain", style="cyan")
        table.add_column("IP")
        for sub, ip in found:
            table.add_row(sub, ip)
        console.print(table)
    else:
        console.print(f"[yellow]No subdomains found[/yellow]")

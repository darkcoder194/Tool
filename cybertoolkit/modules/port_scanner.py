import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
from rich.progress import Progress
from rich.table import Table
from rich.console import Console

console = Console()

def tool_info():
    return {
        "id": "port",
        "name": "Port Scanner",
        "run": run
    }

def run(args):
    if not args:
        console.print("[red]Usage: port <ip> [start_port] [end_port][/red]")
        return
    ip = args[0]
    start_port = int(args[1]) if len(args) > 1 else 1
    end_port = int(args[2]) if len(args) > 2 else 1024
    open_ports = []
    with Progress() as progress:
        task = progress.add_task(f"Scanning {ip}...", total=end_port - start_port + 1)
        with ThreadPoolExecutor(max_workers=100) as executor:
            futures = {executor.submit(scan_port, ip, port): port for port in range(start_port, end_port + 1)}
            for future in as_completed(futures):
                port = futures[future]
                if future.result():
                    open_ports.append(port)
                progress.update(task, advance=1)
    if open_ports:
        table = Table(title=f"Open ports on {ip}")
        table.add_column("Port", style="cyan")
        table.add_column("Status")
        for port in sorted(open_ports):
            table.add_row(str(port), "Open")
        console.print(table)
    else:
        console.print(f"[yellow]No open ports found on {ip}[/yellow]")

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        sock.close()
        return result == 0
    except:
        return False

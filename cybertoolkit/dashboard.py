from rich.console import Console
from rich.live import Live
from rich.panel import Panel
from rich.table import Table
import random
import time
import os
import pyfiglet

console = Console()


def matrix_line():
    chars = "01#@$%&"
    return "".join(random.choice(chars) for _ in range(70))


def get_system_info():

    try:
        user = os.getenv("USER")
    except:
        user = "unknown"

    info = Table.grid()

    info.add_row(f"User: {user}")
    info.add_row(f"Platform: Termux / Android")
    info.add_row(f"Toolkit: CyberToolkit")

    return Panel(info, title="System Info")


def command_panel():

    table = Table()

    table.add_column("Command")
    table.add_column("Description")

    table.add_row("tools", "show installed tools")
    table.add_row("ip", "IP lookup")
    table.add_row("dns", "DNS lookup")
    table.add_row("port", "port scanner")
    table.add_row("install <repo>", "install plugin")
    table.add_row("ai", "AI assistant")
    table.add_row("update", "update toolkit")
    table.add_row("exit", "exit toolkit")

    return Panel(table, title="Commands")


def show_dashboard():

    banner = pyfiglet.figlet_format("CYBER TOOLKIT")

    console.print(f"[green]{banner}")

    with Live(refresh_per_second=10) as live:

        for _ in range(25):

            matrix = "\n".join(matrix_line() for _ in range(8))

            layout = Table.grid(expand=True)

            layout.add_row(Panel(matrix, title="Network Stream"))
            layout.add_row(get_system_info())
            layout.add_row(command_panel())

            live.update(layout)

            time.sleep(0.1)

from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

def tool_info():
    return {
        "id": "dashboard",
        "name": "Interactive Dashboard",
        "run": run
    }

def run(args):
    text = Text("CyberToolkit Dashboard", style="bold green")
    panel = Panel.fit(text, title="Welcome")
    console.print(panel)
    console.print("[cyan]Use 'tools' to list available modules[/cyan]")
    console.print("[cyan]Use 'help' for commands[/cyan]")


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

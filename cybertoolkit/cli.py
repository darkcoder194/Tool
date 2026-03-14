from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from .module_registry import ModuleRegistry

console = Console()
registry = ModuleRegistry()

def start_cli():
    console.print(Panel.fit("[bold green]CyberToolkit v1.0[/bold green]\n[cyan]Type 'help' for commands[/cyan]"))
    while True:
        try:
            cmd = console.input("[bold cyan]cybertool > [/bold cyan]").strip()
            if not cmd:
                continue
            parts = cmd.split()
            command = parts[0]
            args = parts[1:]
            if command == 'exit':
                break
            elif command == 'help':
                show_help()
            elif command == 'tools':
                list_tools()
            elif command == 'reload':
                registry.reload()
                console.print("[green]Modules reloaded[/green]")
            else:
                mod = registry.get_module(command)
                if mod:
                    name, run_func = mod
                    try:
                        run_func(args)
                    except Exception as e:
                        console.print(f"[red]Error: {e}[/red]")
                else:
                    console.print(f"[red]Unknown command: {command}[/red]")
        except KeyboardInterrupt:
            break
    console.print("[yellow]Goodbye![/yellow]")

def show_help():
    table = Table(title="Commands")
    table.add_column("Command", style="cyan")
    table.add_column("Description")
    table.add_row("tools", "List available tools")
    table.add_row("reload", "Reload modules and plugins")
    table.add_row("exit", "Exit the toolkit")
    table.add_row("<tool> <args>", "Run a tool with arguments")
    console.print(table)

def list_tools():
    table = Table(title="Available Tools")
    table.add_column("ID", style="cyan")
    table.add_column("Name")
    for id, (name, _) in registry.list_modules().items():
        table.add_row(id, name)
    console.print(table)

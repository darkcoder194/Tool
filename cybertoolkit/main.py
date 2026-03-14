import sys
from .cli import start_cli, console
from .module_registry import registry

def main():
    if len(sys.argv) > 1:
        command = sys.argv[1]
        args = sys.argv[2:]
        mod = registry.get_module(command)
        if mod:
            name, run_func = mod
            try:
                run_func(args)
            except Exception as e:
                console.print(f"[red]Error: {e}[/red]")
        else:
            console.print(f"[red]Unknown command: {command}[/red]")
    else:
        start_cli()

if __name__ == "__main__":
    main()

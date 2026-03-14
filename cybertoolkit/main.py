import sys
import argparse
import logging
from rich.table import Table
from .cli import start_cli, console
from .module_registry import registry
from . import updater
from .config import Config

config = Config()

def main():
    # Setup logging
    logging.basicConfig(
        level=getattr(logging, config.get('log_level', 'INFO')),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        filename=config.get('log_file', None)
    )
    
    parser = argparse.ArgumentParser(
        description="CyberToolkit - Professional Cybersecurity Framework",
        prog="cybertool"
    )
    parser.add_argument(
        '--version', '-v',
        action='version',
        version='CyberToolkit v1.0'
    )
    parser.add_argument(
        '--config', '-c',
        help='Path to config file (default: ~/.cybertoolkit/config.json)'
    )
    parser.add_argument(
        '--log-level',
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
        help='Set log level'
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Update command
    subparsers.add_parser('update', help='Update CyberToolkit to the latest version')
    
    # List command
    subparsers.add_parser('list', help='List all available modules')
    
    # Config command
    config_parser = subparsers.add_parser('config', help='Manage configuration')
    config_parser.add_argument('action', choices=['get', 'set', 'list'], help='Action to perform')
    config_parser.add_argument('key', nargs='?', help='Configuration key')
    config_parser.add_argument('value', nargs='?', help='Configuration value')
    
    # Module command
    module_parser = subparsers.add_parser('run', help='Run a specific module')
    module_parser.add_argument('module', help='Module name to run')
    module_parser.add_argument('args', nargs='*', help='Arguments for the module')
    
    # Interactive mode (default)
    subparsers.add_parser('interactive', help='Start interactive CLI mode')
    
    args = parser.parse_args()
    
    if args.log_level:
        config.set('log_level', args.log_level)
        logging.getLogger().setLevel(getattr(logging, args.log_level))
    
    if args.command == 'update':
        updater.update()
        console.print("[green]Updated to latest version.[/green]")
    elif args.command == 'list':
        list_modules()
    elif args.command == 'config':
        handle_config(args)
    elif args.command == 'run':
        run_module(args.module, args.args)
    elif args.command == 'interactive' or args.command is None:
        start_cli()
    else:
        parser.print_help()

def handle_config(args):
    if args.action == 'list':
        table = Table()
        table.add_column("Key", style="cyan")
        table.add_column("Value", style="magenta")
        for key, value in config.config.items():
            table.add_row(key, str(value))
        console.print(table)
    elif args.action == 'get':
        if args.key:
            value = config.get(args.key)
            console.print(f"{args.key}: {value}")
        else:
            console.print("[red]Key required for get action[/red]")
    elif args.action == 'set':
        if args.key and args.value:
            config.set(args.key, args.value)
            console.print(f"[green]Set {args.key} = {args.value}[/green]")
        else:
            console.print("[red]Key and value required for set action[/red]")

def list_modules():
    table = Table()
    table.add_column("Module ID", style="cyan")
    table.add_column("Name", style="magenta")
    
    for mod_id, (name, _) in registry.modules.items():
        table.add_row(mod_id, name)
    
    console.print(table)

def run_module(module_name, args):
    mod = registry.get_module(module_name)
    if mod:
        name, run_func = mod
        try:
            run_func(args)
        except Exception as e:
            console.print(f"[red]Error running {module_name}: {e}[/red]")
            logging.error(f"Error running module {module_name}: {e}")
    else:
        console.print(f"[red]Unknown module: {module_name}[/red]")

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()

from rich.console import Console

console = Console()

def tool_info():
    return {
        "id": "ai-build",
        "name": "AI Module Generator",
        "run": run
    }

def run(args):
    if not args:
        console.print("[red]Usage: ai-build <module_id> <module_name>[/red]")
        return
    module_id = args[0]
    module_name = ' '.join(args[1:]) if len(args) > 1 else module_id
    template = f'''from rich.console import Console

console = Console()

def tool_info():
    return {{
        "id": "{module_id}",
        "name": "{module_name}",
        "run": run
    }}

def run(args):
    # Your tool logic here
    console.print("Hello from {module_name}!")
    if args:
        console.print(f"Arguments: {{args}}")
'''
    filename = f"modules/{module_id}.py"
    try:
        with open(filename, 'w') as f:
            f.write(template)
        console.print(f"[green]Module {module_id}.py created in modules/[/green]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")

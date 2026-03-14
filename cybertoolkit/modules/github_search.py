import requests
from rich.table import Table
from rich.console import Console

console = Console()

def tool_info():
    return {
        "id": "gh-search",
        "name": "GitHub Tool Search",
        "run": run
    }

def run(args):
    if not args:
        console.print("[red]Usage: gh-search <query>[/red]")
        return
    query = ' '.join(args)
    try:
        response = requests.get(f"https://api.github.com/search/repositories?q={query}", timeout=10)
        data = response.json()
        if 'items' in data:
            table = Table(title=f"GitHub search for '{query}'")
            table.add_column("Repository", style="cyan")
            table.add_column("Description")
            table.add_column("Stars")
            for item in data['items'][:10]:
                table.add_row(item['full_name'], item.get('description', ''), str(item['stargazers_count']))
            console.print(table)
        else:
            console.print("[red]No results[/red]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")

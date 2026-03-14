import requests
from rich.table import Table
from rich.console import Console

console = Console()

def tool_info():
    return {
        "id": "tech",
        "name": "Web Technology Detector",
        "run": run
    }

def run(args):
    if not args:
        console.print("[red]Usage: tech <url>[/red]")
        return
    url = args[0]
    if not url.startswith('http'):
        url = 'http://' + url
    try:
        response = requests.get(url, timeout=10)
        technologies = detect_tech(response)
        if technologies:
            table = Table(title=f"Detected technologies for {url}")
            table.add_column("Technology", style="cyan")
            table.add_column("Confidence")
            for tech, conf in technologies.items():
                table.add_row(tech, conf)
            console.print(table)
        else:
            console.print("[yellow]No technologies detected[/yellow]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")

def detect_tech(response):
    tech = {}
    headers = response.headers
    content = response.text.lower()
    # Check headers
    if 'server' in headers:
        server = headers['server'].lower()
        if 'apache' in server:
            tech['Apache'] = 'High'
        elif 'nginx' in server:
            tech['Nginx'] = 'High'
        elif 'iis' in server:
            tech['IIS'] = 'High'
    if 'x-powered-by' in headers:
        powered = headers['x-powered-by'].lower()
        if 'php' in powered:
            tech['PHP'] = 'High'
        elif 'asp.net' in powered:
            tech['ASP.NET'] = 'High'
    # Check content
    if 'wordpress' in content or 'wp-content' in content:
        tech['WordPress'] = 'High'
    if 'jquery' in content:
        tech['jQuery'] = 'Medium'
    if 'bootstrap' in content:
        tech['Bootstrap'] = 'Medium'
    if '<meta name="generator" content="joomla' in content:
        tech['Joomla'] = 'High'
    if 'drupal' in content:
        tech['Drupal'] = 'Medium'
    return tech
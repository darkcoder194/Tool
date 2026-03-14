import subprocess
import logging

def update():
    from .cli import console
    console.print("[cyan]Updating toolkit...[/cyan]")
    logging.info("Starting update process")
    
    try:
        result = subprocess.run(["git", "pull"], capture_output=True, text=True)
        if result.returncode == 0:
            console.print("[green]Update complete[/green]")
            logging.info("Update successful")
        else:
            console.print(f"[red]Update failed: {result.stderr}[/red]")
            logging.error(f"Update failed: {result.stderr}")
    except Exception as e:
        console.print(f"[red]Error during update: {e}[/red]")
        logging.error(f"Error during update: {e}")

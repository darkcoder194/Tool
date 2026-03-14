from rich.console import Console

console = Console()

def run_ai():

    console.print("[cyan]CyberToolkit AI Assistant[/cyan]")
    console.print("Type 'exit' to return\n")

    while True:

        q = input("AI > ")

        if q.lower() == "exit":
            break

        if "ip tool" in q.lower():
            console.print("You can create an IP lookup module inside modules/ip_lookup.py")

        elif "scan port" in q.lower():
            console.print("Use the port scanner module with command: port")

        elif "create module" in q.lower():
            console.print("Use command: ai-build")

        else:
            console.print("AI suggestion: create a module using ai-build")

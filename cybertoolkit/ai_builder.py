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

    domain = input("Domain: ")

    try:
        ip = socket.gethostbyname(domain)
        print("IP Address:", ip)
    except:
        print("DNS lookup failed")
'''

    elif feature == "port":

        code = f'''
import socket

def tool_info():
    return {{
        "id": "{cmd}",
        "name": "{name}",
        "run": run
    }}

def run():

    target = input("Target IP: ")

    for port in range(1,1025):

        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(0.5)

        if s.connect_ex((target,port)) == 0:
            print("OPEN:",port)

        s.close()
'''

    elif feature == "headers":

        code = f'''
import http.client
from urllib.parse import urlparse

def tool_info():
    return {{
        "id": "{cmd}",
        "name": "{name}",
        "run": run
    }}

def run():

    url=input("URL: ")

    if not url.startswith("http"):
        url="http://"+url

    parsed=urlparse(url)

    conn=http.client.HTTPConnection(parsed.netloc)

    conn.request("GET","/")

    res=conn.getresponse()

    for k,v in res.getheaders():
        print(k+":",v)
'''

    else:

        code = f'''
def tool_info():
    return {{
        "id": "{cmd}",
        "name": "{name}",
        "run": run
    }}

def run():

    print("{name} tool started")

    target=input("Enter target: ")

    print("Processing:",target)
'''

    with open(file_path,"w") as f:
        f.write(code)

    print("\nAI created module:",file_path)

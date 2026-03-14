import os

MODULE_PATH = "cybertoolkit/modules"

def run_ai_builder():

    print("\nCyberToolkit AI Module Builder\n")

    name = input("Tool name: ")
    cmd = input("Command id: ")
    feature = input("Feature (ip / dns / port / headers / custom): ")

    file_path = f"{MODULE_PATH}/{cmd}.py"

    if feature == "ip":

        code = f'''
import socket

def tool_info():
    return {{
        "id": "{cmd}",
        "name": "{name}",
        "run": run
    }}

def run():

    ip = input("Enter IP: ")

    try:
        host = socket.gethostbyaddr(ip)
        print("Hostname:", host[0])
    except:
        print("No host found")
'''

    elif feature == "dns":

        code = f'''
import socket

def tool_info():
    return {{
        "id": "{cmd}",
        "name": "{name}",
        "run": run
    }}

def run():

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

import requests

def tool_info():
    return {
        "id": "ip",
        "name": "IP Lookup",
        "run": run
    }

def run():

    ip = input("IP: ")

    data = requests.get(f"http://ip-api.com/json/{ip}").json()

    for k,v in data.items():
        print(k,":",v)

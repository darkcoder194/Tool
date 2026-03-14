import socket

def tool_info():
    return {
        "id": "sub",
        "name": "Subdomain Finder",
        "run": run
    }

def run():

    domain = input("Target domain: ")

    subs = [
        "www","mail","ftp","api","dev","test",
        "blog","shop","m","beta","admin","portal"
    ]

    print("\nScanning subdomains...\n")

    for s in subs:

        sub = f"{s}.{domain}"

        try:
            ip = socket.gethostbyname(sub)
            print("[FOUND]", sub, "->", ip)

        except:
            pass

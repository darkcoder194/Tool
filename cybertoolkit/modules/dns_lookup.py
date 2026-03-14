import socket

def tool_info():
    return {
        "id": "dns",
        "name": "DNS Lookup",
        "run": run
    }

def run():

    domain = input("Domain: ")

    try:

        ip = socket.gethostbyname(domain)

        print("IP Address:", ip)

        info = socket.gethostbyaddr(ip)

        print("Hostname:", info[0])

    except Exception as e:

        print("DNS error:", e)

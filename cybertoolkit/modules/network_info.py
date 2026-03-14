import socket

def tool_info():
    return {
        "id": "net",
        "name": "Network Info",
        "run": run
    }

def run():

    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)

    print("Hostname:", hostname)
    print("Local IP:", ip)

import socket
from rich.live import Live
from rich.table import Table

def tool_info():
    return {
        "id": "port",
        "name": "Port Scanner",
        "run": run
    }

def scan_port(host, port):
    s = socket.socket()
    s.settimeout(0.5)

    try:
        s.connect((host, port))
        return True
    except:
        return False
    finally:
        s.close()


def run():
    host = input("Target host: ")

    table = Table(title="Port Scan Results")
    table.add_column("Port")
    table.add_column("Status")

    with Live(table, refresh_per_second=4):

        for port in range(20, 200):

            if scan_port(host, port):
                table.add_row(str(port), "OPEN")
            else:
                table.add_row(str(port), "closed")

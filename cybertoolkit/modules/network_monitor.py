import time

def tool_info():
    return {
        "id": "netmon",
        "name": "Network Monitor",
        "run": run
    }

def read_net():

    data = {}

    with open("/proc/net/dev") as f:
        lines = f.readlines()[2:]   # skip headers

        for line in lines:
            parts = line.split()
            iface = parts[0].replace(":", "")

            recv = int(parts[1])
            sent = int(parts[9])

            data[iface] = (recv, sent)

    return data


def run():

    print("Press CTRL+C to stop")

    prev = read_net()

    while True:

        time.sleep(2)

        curr = read_net()

        for iface in curr:

            recv = curr[iface][0] - prev.get(iface, (0,0))[0]
            sent = curr[iface][1] - prev.get(iface, (0,0))[1]

            print(f"{iface}")
            print("Download:", recv, "bytes")
            print("Upload:", sent, "bytes")
            print("------")

        prev = curr

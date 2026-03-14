import whois

def tool_info():
    return {
        "id": "whois",
        "name": "WHOIS Lookup",
        "run": run
    }

def run():

    domain = input("Domain: ")

    try:
        data = whois.whois(domain)

        print(data)

    except Exception as e:
        print("Error:", e)

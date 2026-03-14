import http.client
from urllib.parse import urlparse

def tool_info():
    return {
        "id": "headers",
        "name": "HTTP Header Analyzer",
        "run": run
    }

def run():

    url = input("URL: ")

    if not url.startswith("http"):
        url = "http://" + url

    parsed = urlparse(url)

    conn = http.client.HTTPConnection(parsed.netloc)

    try:

        conn.request("GET", "/")

        res = conn.getresponse()

        print("\nHTTP Headers:\n")

        for k,v in res.getheaders():
            print(f"{k}: {v}")

    except Exception as e:

        print("Error:", e)

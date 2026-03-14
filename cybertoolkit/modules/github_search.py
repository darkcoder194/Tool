import urllib.request
import json

def tool_info():
    return {
        "id": "gh-search",
        "name": "GitHub Tool Search",
        "run": run
    }

def run():

    query = input("Search GitHub tool: ")

    url = f"https://api.github.com/search/repositories?q={query}"

    try:
        data = urllib.request.urlopen(url).read()
        results = json.loads(data)

        print("\nTop Results:\n")

        for repo in results["items"][:5]:
            print(repo["full_name"])
            print(repo["html_url"])
            print(repo["description"])
            print("--------")

    except Exception as e:
        print("Error:", e)

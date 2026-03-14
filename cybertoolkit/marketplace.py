import requests

PLUGIN_LIST = "https://raw.githubusercontent.com/example/plugins/main/plugins.json"

def show_marketplace():

    data = requests.get(PLUGIN_LIST).json()

    print("Available Plugins")

    for i,p in enumerate(data):

        print(i+1, p["name"], "-", p["description"])

    choice=int(input("Install plugin #: "))

    return data[choice-1]["repo"]

import json
import getpass

USERS="cybertoolkit/data/users.json"
TOKENS="cybertoolkit/data/tokens.json"

def login_user():

    users=json.load(open(USERS))

    u=input("Username: ")
    p=getpass.getpass("Password: ")

    if u in users and users[u]==p:
        return True

    return False


def login_token():

    tokens=json.load(open(TOKENS))

    t=input("Token: ")

    if t in tokens:
        return True

    return False

def tool_info():
    return {
        "id": "pass",
        "name": "Password Strength",
        "run": run
    }

def run():

    pwd = input("Password: ")

    score = 0

    if len(pwd) >= 8:
        score += 1

    if any(c.isdigit() for c in pwd):
        score += 1

    if any(c.isupper() for c in pwd):
        score += 1

    if any(c in "!@#$%^&*" for c in pwd):
        score += 1

    print("Strength score:", score, "/4")

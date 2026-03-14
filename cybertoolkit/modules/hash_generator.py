import hashlib

def tool_info():
    return {
        "id": "hash",
        "name": "Hash Generator",
        "run": run
    }

def run():

    text = input("Text: ")

    print("MD5:", hashlib.md5(text.encode()).hexdigest())
    print("SHA1:", hashlib.sha1(text.encode()).hexdigest())
    print("SHA256:", hashlib.sha256(text.encode()).hexdigest())

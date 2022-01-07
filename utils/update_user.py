import requests
from random import choice

UPDATED_USER = {
    "first_name": "Angel",
    "last_name": "Garcia",
    "hobbies": choice(
        [
            "Golf",
            "Tennis",
            "Soccer",
            "Football",
            "Skiing",
            "Skateboarding"
        ]
        )
}

URL = "http://127.0.01:5000/users/1"

def update_user():
    out = requests.put(URL, json=UPDATED_USER)
    if out.status_code == 200:
        print("Update successful.")
    else:
        print("Update failed.")


if __name__ == "__main__":
    update_user()
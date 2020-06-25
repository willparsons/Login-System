import json
from typing import Any


def write_json(data, filename) -> None:
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def insert_account(username: str, password: str, directory: str) -> None:
    try:
        with open(directory) as f:
            data = json.load(f)

            temp = data["users"]

            obj = {
                "username": username,
                "password": password,
                "permissions": ["User"]
            }
            temp.append(obj)
            write_json(data, f)

    except FileNotFoundError:
        create_file(directory)


def create_file(directory: str) -> None:
    with open(directory, "w") as f:
        obj = {
            "users": []
        }

        json.dump(obj, f)


def get_data_json(directory: str) -> Any:
    try:
        with open(directory) as f:
            data = json.load(f)

    except FileNotFoundError:
        print("File not found. Creating now.")
        create_file(directory)
        data = None

    return data

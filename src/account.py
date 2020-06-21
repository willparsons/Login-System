import json
from crypto import Crypto

SUCCESS = -1
NO_USER = 0
INVALID_PASS = 1

DIRECTORY = "users"


class Account:

    def __init__(self):
        self.c = Crypto()

    @staticmethod
    def login(username: str, password: str):
        acc = Account()

        exists = acc.__exists(username, password)

        if exists == NO_USER:
            acc.__make_account(username, password)

        elif exists == INVALID_PASS:
            print("Invalid password")

        elif exists == SUCCESS:
            print("Login successful.")

        acc.c.encrypt_file(DIRECTORY)

    def __exists(self, username: str, password: str) -> int:
        try:
            self.c.decrypt_file(DIRECTORY)
            with open(DIRECTORY, "r") as f:
                data = json.load(f)

                for user in data["users"]:
                    if user["username"] == username:
                        if user["password"] == password:
                            return SUCCESS
                        return INVALID_PASS
        except FileNotFoundError:
            self.__create_file()

        return NO_USER

    @staticmethod
    def __create_file():
        with open(DIRECTORY, "w") as f:
            obj = {
                "users": []
            }

            json.dump(obj, f)

    def __make_account(self, username: str, password: str):
        choice = input(
            "\nThis account was not found. Would you like to create it? Y/N ")

        if choice.lower() == "y" or choice.lower() == "yes":
            self.__create(username, password)
            print("Account created.")

    def __create(self, username: str, password: str):
        with open(DIRECTORY) as f:
            data = json.load(f)

            temp = data["users"]

            obj = {
                "username": username,
                "password": password
            }

            temp.append(obj)

        self.__write_json(data, DIRECTORY)

    @staticmethod
    def __write_json(data, filename):
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

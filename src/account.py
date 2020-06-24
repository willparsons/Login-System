import filemanager
import utils


class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.permissions = []

    def exists(self) -> int:
        data = filemanager.get_data_json(utils.DIRECTORY)

        for user in data["users"]:
            if user["username"] == self.username:
                if user["password"] == self.password:
                    return utils.SUCCESS
                return utils.INVALID_PASS

        return utils.NO_USER

    def make_account(self):
        choice = input(
            "\nThis account was not found. Would you like to create it? Y/N ")

        if choice.lower() == "y" or choice.lower() == "yes":
            filemanager.insert_account(self.username, self.password, utils.DIRECTORY)
            print("Account created.")

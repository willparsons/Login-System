import utils
import db


class Account:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

        self.permission_level = -1

    def exists(self) -> int:
        user = db.get_user_by_username(self.username)

        if not user:
            return utils.NO_USER

        password = user[0][1]
        self.permission_level = user[0][2]

        if self.password == password:
            return utils.SUCCESS
        else:
            return utils.INVALID_PASS

        # data = filemanager.get_data_json(utils.DIRECTORY)
        # for user in data["users"]:
        #     if user["username"] == self.username:
        #         if user["password"] == self.password:
        #             return utils.SUCCESS
        #         return utils.INVALID_PASS
        #
        # return utils.NO_USER

    def make_account(self):
        db.insert_user(self.username, self.password, 0)
        # choice = input(
        #     "\nThis account was not found. Would you like to create it? Y/N ")
        #
        # if choice.lower() == "y" or choice.lower() == "yes":
        #     filemanager.insert_account(self.username, self.password, utils.DIRECTORY)
        #     print("Account created.")

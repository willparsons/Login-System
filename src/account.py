import utils


class Account:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

        # TODO: READ PERMISSIONS FROM DB
        self.permission_level = -1

    # TODO: replace this with reading from database
    def exists(self) -> int:
        # data = filemanager.get_data_json(utils.DIRECTORY)
        # for user in data["users"]:
        #     if user["username"] == self.username:
        #         if user["password"] == self.password:
        #             return utils.SUCCESS
        #         return utils.INVALID_PASS
        #
        # return utils.NO_USER
        pass

    # TODO: add user to the database
    def make_account(self):
        # choice = input(
        #     "\nThis account was not found. Would you like to create it? Y/N ")
        #
        # if choice.lower() == "y" or choice.lower() == "yes":
        #     filemanager.insert_account(self.username, self.password, utils.DIRECTORY)
        #     print("Account created.")
        pass

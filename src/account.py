import utils
import db
from hashdetails import check_hash


class Account:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

        self.permission_level = -1

    def exists(self) -> int:
        user = db.get_user_by_username(self.username)

        if len(user) == 0:
            return utils.NO_USER

        password = user[0][1]
        self.permission_level = user[0][2]

        if check_hash(self.password, password):
            return utils.SUCCESS
        else:
            return utils.INVALID_PASS

    # TODO: PLACEHOLDER! WHEN GUI IS MADE, THIS WILL BE ONLY ACCESSIBLE WITH AN ADMIN ACCOUNT
    def make_account(self):
        db.insert_user(self.username, self.password, 0)

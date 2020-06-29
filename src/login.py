from account import Account
import utils


# TODO: handle returning account object
class Login:
    @staticmethod
    def login(username: str, password: str):
        account = Account(username, password)
        exists = account.exists()

        # TODO: GUI functionality to login as Admin and create user account
        if exists == utils.NO_USER:
            print(f"Account with username \"{username}\" not found. Requires admin to create.")

        elif exists == utils.INVALID_PASS:
            print("Invalid password")

        elif exists == utils.SUCCESS:
            print("Login successful.")
            return account

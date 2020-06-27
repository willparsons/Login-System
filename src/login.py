from account import Account
import utils


# return account object
class Login:

    @staticmethod
    def login(username: str, password: str):
        account = Account(username, password)
        exists = account.exists()

        if exists == utils.NO_USER:
            account.make_account()

        elif exists == utils.INVALID_PASS:
            print("Invalid password")

        elif exists == utils.SUCCESS:
            print("Login successful.")
            return account

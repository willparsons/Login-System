from account import Account


def main():
    username = input("Enter username: ")
    password = input("Enter password: ")

    Account.login(username, password)


if __name__ == "__main__":
    main()

from login import Login


def main():
    username = input("Enter username: ")
    password = input("Enter password: ")

    Login.login(username, password)


if __name__ == "__main__":
    main()

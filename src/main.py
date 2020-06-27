from login import Login


def main():
    username = input("Enter username: ")
    password = input("Enter password: ")

    willie = Login.login(username, password)
    print(willie.permission_level)


if __name__ == "__main__":
    main()

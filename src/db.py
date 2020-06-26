import sqlite3

conn = sqlite3.connect("../db/users.db")
c = conn.cursor()


def create_users_table():
    try:
        with conn:
            c.execute("""CREATE TABLE users (
                username text,
                password text,
                permissions_level integer
            )""")
    except sqlite3.OperationalError:
        print("Table users has already been created.")


def insert_user(username: str, password: str, permission_level: int):
    with conn:
        c.execute("INSERT INTO users VALUES (:username, :password, :permission_level)",
                  {"username": username, "password": password, "permission_level": permission_level})


def delete_user(username: str):
    with conn:
        c.execute("DELETE FROM users WHERE username=:username", {"username": username})


def get_all_users():
    c.execute("SELECT * FROM users")
    return c.fetchall()


def get_user_by_username(username: str):
    c.execute("SELECT * FROM users WHERE username=:username", {"username": username})
    return c.fetchall()

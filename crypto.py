from cryptography.fernet import Fernet


class Crypto:
    def __init__(self):
        try:
            self.key = load_key()
        except FileNotFoundError:
            self.key = write_key()

    def encrypt_file(self, filename: str):
        f = Fernet(self.key)
        try:
            encrypted_data = f.encrypt(self.__get_data(filename))
            self.__write_data(filename, encrypted_data)
        except TypeError:
            print("Encryption failed.")

    def decrypt_file(self, filename: str):
        f = Fernet(self.key)
        try:
            decrypted_data = f.decrypt(self.__get_data(filename))
            self.__write_data(filename, decrypted_data)
        except TypeError:
            print("Decryption failed.")

    @staticmethod
    def __get_data(filename):
        with open(filename, "rb") as f:
            data = f.read()

        return data

    @staticmethod
    def __write_data(filename, data):
        with open(filename, "wb") as f:
            f.write(data)


def write_key():
    key = Fernet.generate_key()

    with open("key.key", "wb") as f:
        f.write(key)

    return key


def load_key():
    return open("key.key", "rb").read()

# TODO: try json dumping with r+

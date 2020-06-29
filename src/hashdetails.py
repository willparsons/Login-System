import hashlib


def hash_string(s):
    """
    Hashes the string s and returns the result

    :param s: String value that will be hashed
    :return: Hashed 256bit value
    """
    return hashlib.sha256(str.encode(s)).hexdigest()


def check_hash(s, h):
    """
    Hashes the s parameter and returns if the result is equal to h

    :param s: String value
    :param h: Hashed value
    :return: True if hashed s is equal to h, else False
    """
    return hash_string(s) == h

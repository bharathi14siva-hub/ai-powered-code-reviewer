
password = "admin123"


def get_user(username):
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    return query


def read_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        data = file.read()
    return data


def divide(a, b):
    return a / b


import os

password = "admin123"


def divide_numbers(a, b):
    result = a / b
    print(result)


def get_user(user_input):
    query = "SELECT * FROM users WHERE name = '" + user_input + "'"
    return query


def read_file(filename):
    file = open(filename, "r")
    data = file.read()
    return data


divide_numbers(10, 2)

#!/usr/bin/python3
"""This module takes first and last name from user"""


def say_my_name(first_name, last_name=""):
    """This fucntion gets first and last name and prints them to STDOUT
    first_name (str)"""

    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")

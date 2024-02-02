#!/usr/bin/python3
"""
Module to print "My name is <first name> <last name>"
"""


def say_my_name(first_name, last_name=""):
    """
    Function to print "My name is <first name> <last name>"
    
    Args:
        first_name (str): First name
        last_name (str): Last name (default is empty)
    
    Raises:
        TypeError: If first_name or last_name is not a string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))

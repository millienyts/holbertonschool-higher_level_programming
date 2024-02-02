#!/usr/bin/python3
"""This module iterates in a string and finds special characters
prints them and creates two new lines"""


def text_indentation(text):
    """This fucntion iterates in a string if specified characters
    are found they will get printed and then two new lines
    text (str): text must be type str"""

    if type(text) != str:
        raise TypeError("text must be a string")

    for i in text:
        if i == "." or i == "?" or i == ":":
            print(f"{i}", end="")
            print("")
            print("")
        else:
            print(f"{i}", end="")

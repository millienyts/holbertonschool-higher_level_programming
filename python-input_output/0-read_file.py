#!/usr/bin/python3
"""
Read file module
"""


def read_file(filename=""):
    """
    Read file function
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")


if __name__ == "__main__":
    read_file("my_file_0.txt")

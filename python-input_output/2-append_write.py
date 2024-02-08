#!/usr/bin/python3
"""
Append to file module
"""


def append_write(filename="", text=""):
    """
    Append to file function
    """
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)


if __name__ == "__main__":
    append_write("file_append.txt", "This School is so cool!\n")

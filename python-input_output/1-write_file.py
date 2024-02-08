#!/usr/bin/python3
"""
Write to file module
"""


def write_file(filename="", text=""):
    """
    Write to file function
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)


if __name__ == "__main__":
    write_file("my_first_file.txt", "This School is so cool!\n")

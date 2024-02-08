#!/usr/bin/python3

def append_after(filename="", search_string="", new_string=""):
    """
    Inserts new_string after each line containing search_string
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(filename, mode='w', encoding='utf-8') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)

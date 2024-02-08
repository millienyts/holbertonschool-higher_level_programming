#!/usr/bin/python3

def append_after(filename="", search_string="", new_string=""):
    """
    Append new_string after each occurrence of search_string in the file
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)

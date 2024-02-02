#!/usr/bin/python3
"""This module prints a square with area of size*size"""


def print_square(size):
    """This fucntion prints a perfect square with area size*size
    size (int) else exeption will be raise"""

    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")

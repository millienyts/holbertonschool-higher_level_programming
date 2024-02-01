o#!/usr/bin/python3
"""Define a class Square with size attribute and area method."""


class Square:
    """Represent a square with size and area calculation."""
    def __init__(self, size=0):
        """Initialize a new square with a given size."""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

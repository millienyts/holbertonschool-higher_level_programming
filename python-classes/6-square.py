#!/usr/bin/python3
"""Define a class Square with size and position attributes."""


class Square:
    """Represent a square with size and position attributes."""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square with a given size and position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation."""
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#' and respecting position."""
        if self.__size == 0:
            print()
        else:
            print('\n' * self.__position[1], end='')
            for _ in range(self.__size):
                print(' ' * self.__position[0] + '#' * self.__size)

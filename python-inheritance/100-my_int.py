#!/usr/bin/python3

"""100-my_int module"""


class MyInt(int):
    """A class representing an integer with inverted equality operators.

    Attributes:
        int: The integer value.

    Methods:
        __eq__(self, other): Overrides the equality operator.
        __ne__(self, other): Overrides the inequality operator.
    """

    def __eq__(self, other):
        """Overrides the equality operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Overrides the inequality operator."""
        return super().__eq__(other)

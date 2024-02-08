#!/usr/bin/python3
"""
Class to JSON module
"""


def class_to_json(obj):
    """
    Class to JSON function
    """
    return obj.__dict__


if __name__ == "__main__":
    class MyClass:
        def __init__(self, name):
            self.name = name
            self.number = 0

        def __str__(self):
            return "[MyClass] {} - {:d}".format(self.name, self.number)

    m = MyClass("John")
    m.number = 89
    print(class_to_json(m))

#!/usr/bin/python3
"""
Returns True if the object is an instance
of, or if the object is an instance of a class that
inherited from, the specified class ; otherwise False.
"""

def is_kind_of_class(obj, a_class):
     """
    Function return True if is an insatance
    from inherited class
    """
    return isinstance(obj, a_class)

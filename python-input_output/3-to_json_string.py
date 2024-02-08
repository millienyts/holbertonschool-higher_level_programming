#!/usr/bin/python3
"""
To JSON string module
"""

import json


def to_json_string(my_obj):
    """
    To JSON string function
    """
    return json.dumps(my_obj)


if __name__ == "__main__":
    my_list = [1, 2, 3]
    print(to_json_string(my_list))

#!/usr/bin/python3
"""
From JSON string module
"""

import json


def from_json_string(my_str):
    """
    From JSON string function
    """
    return json.loads(my_str)


if __name__ == "__main__":
    s_my_list = "[1, 2, 3]"
    print(from_json_string(s_my_list))

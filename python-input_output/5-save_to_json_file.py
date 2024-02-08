#!/usr/bin/python3
"""
Save to JSON file module
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Save to JSON file function
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)


if __name__ == "__main__":
    my_list = [1, 2, 3]
    save_to_json_file(my_list, "my_list.json")

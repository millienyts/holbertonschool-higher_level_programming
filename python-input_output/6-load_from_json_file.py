#!/usr/bin/python3
"""
Load from JSON file module
"""

import json


def load_from_json_file(filename):
    """
    Load from JSON file function
    """
    with open(filename, encoding='utf-8') as f:
        return json.load(f)


if __name__ == "__main__":
    print(load_from_json_file("my_list.json"))

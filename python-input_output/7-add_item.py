#!/usr/bin/python3
"""
Add item module
"""

import sys
import os.path


def add_item():
    """
    Add item function
    """
    filename = 'add_item.json'
    if os.path.exists(filename):
        with open(filename, mode='r', encoding='utf-8') as f:
            items = json.load(f)
    else:
        items = []
    items.extend(sys.argv[1:])
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(items, f)


if __name__ == "__main__":
    add_item()

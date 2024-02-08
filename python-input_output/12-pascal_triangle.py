#!/usr/bin/python3
"""
Pascal Triangle Module
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]
        if triangle:
            last_row = triangle[-1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)
        triangle.append(row)
    return triangle


if __name__ == "__main__":
    n = 5
    for row in pascal_triangle(n):
        print(row)

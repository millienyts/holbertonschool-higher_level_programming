#!/usr/bin/python3
"""This module provides a fucntion to divide matrix,
and store divided values in a lists of lists."""


def matrix_divided(matrix, div):
    """This function divides every integer"""
    _matrix1 = []
    _matrix2 = []
    str1 = "matix must be a (list of list) of integers/floats"
    num = 0
    idx = 0

    for _list in matrix:
        if type(_list) != list:
            raise TypeError()
        for i in _list:
            if type(i) != int and type(i) != float:
                raise TypeError(str1)

        if type(div) != int and type(div) != float:
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")

    if len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of the matrix must be the same size")

    for j in matrix:
        for i in j:
            num = i / div
            if idx == 0:
                _matrix1.append(round(num, 2))
            elif idx == 1:
                _matrix2.append(round(num, 2))
        idx += 1
    matrix = [_matrix1, _matrix2]
    return matrix

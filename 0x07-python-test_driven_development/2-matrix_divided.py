#!/usr/bin/python3
"""
    matrix divided

    a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
        matrix divided
    """
    if not isinstance(matrix, list) or matrix == [] or matrix == [[]] or\
    not all(map(lambda row: isinstance(row, list), matrix)) or\
    not all(isinstance(item, int) or isinstance(item, float) for row in matrix for item in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(matrix[0]) == len(row) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [list(map(lambda item: round(item / div, 2),row)) for row in matrix]

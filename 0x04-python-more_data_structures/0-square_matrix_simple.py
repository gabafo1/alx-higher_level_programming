#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            if not isinstance(element, int):
                raise TypeError("All elements in the matrix must be integers.")
            new_row.append(element * element)
        new_matrix.append(new_row)
    return new_matrix

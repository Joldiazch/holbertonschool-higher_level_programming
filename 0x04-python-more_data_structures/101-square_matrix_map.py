#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return [list(map(lambda y: y*y, x)) for x in matrix]

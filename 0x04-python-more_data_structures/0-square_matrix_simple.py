#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        resul = matrix.copy()
        i = 0
        for lista in matrix:
            resul[i] = list(map(lambda x: x * x, lista))
            i += 1
    return resul

#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda fil: list(map(lambda n: n * n, fil)), matrix))

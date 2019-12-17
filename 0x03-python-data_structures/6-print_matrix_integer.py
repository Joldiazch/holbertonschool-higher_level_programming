#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    sep = '-'
    for lista in matrix:
        print('{:s}'.format(' '.join(map(str, lista))))

#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for fil in range(len(matrix)):
            for col in range(len(matrix[fil])):
                if col < (len(matrix[fil]) - 1):
                    print('{:d}'.format(matrix[fil][col]), end=' ')
                else:
                    print('{:d}'.format(matrix[fil][col]), end='')
            print()

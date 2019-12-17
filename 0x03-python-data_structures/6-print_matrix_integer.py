#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lista in matrix:
        for i in range(len(lista)):
            if i < (len(lista) - 1):
                print('{:d}'.format(lista[i]), end=' ')
            else:
                print('{:d}'.format(lista[i]))

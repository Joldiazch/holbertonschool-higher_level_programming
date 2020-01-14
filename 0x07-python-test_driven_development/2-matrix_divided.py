#!/usr/bin/python3
def matrix_divided(matrix, div):
    m1 = "div must be a number"
    m2 = "division by zero"
    m3 = "matrix must be a matrix (list of lists) of integers/floats"
    m4 = "Each row of the matrix must have the same size"
    m5 = "matrix must be a matrix (list of lists) of integers/floats"
    m6 = "matrix must be a matrix (list of lists) of integers/floats"
    if type(div) is not int and type(div) is not float:
        raise TypeError(m1)
    elif div == 0:
        raise ZeroDivisionError(m2)

    new = []

    if type(matrix) is not list:
        raise TypeError(m3)
    else:
        if len(matrix) == 0:
            raise TypeError(m3)
        fun = map(lambda x: True if type(x) is list else False, matrix)
        if all(list(fun)):
            if not all(map(lambda x: 1 if len(x) != 0 else 0, matrix)):
                raise TypeError(m3)
            for lista in matrix:
                if (len(lista) != len(matrix[0])):
                    raise TypeError(m4)
                fun2 = map(
                    lambda x: True
                    if (type(x) is int or type(x) is float)
                    else False,
                    lista
                    )
                if all(list(fun2)):
                    new.append(list(map(lambda num: round(num/div, 2), lista)))
                else:
                    raise TypeError(m5)
        else:
            raise TypeError(m6)
    return new

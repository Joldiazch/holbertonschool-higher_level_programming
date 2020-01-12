def matrix_divided(matrix, div):
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    new = []

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix\
(list of lists) of integers/floats")
    else:
        fun = map(lambda x: True if type(x) is list else False, matrix)
        if all(list(fun)):
            for lista in matrix:
                if (len(lista) != len(matrix[0])):
                    raise TypeError("Each row of the matrix\
must have the same size")
                fun2 = map(
                            lambda x: True
                            if (type(x) is int or type(x) is float)
                            else False,
                            lista
                            )
                if all(list(fun2)):
                    new.append(list(map(lambda num: round(num/div, 2), lista)))
                else:
                    raise TypeError("matrix must be a matrix\
(list of lists) of integers/floats")
        else:
            raise TypeError("matrix must be a matrix\
(list of lists) of integers/floats")
    return new

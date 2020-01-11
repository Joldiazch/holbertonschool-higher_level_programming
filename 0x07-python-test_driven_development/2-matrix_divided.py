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
        fun = lambda x: True if type(x) is list else False
        if all(list(map(fun, matrix))):
            for lista in matrix:
                if (len(lista) != len(matrix[0])):
                    raise TypeError("Each row of the matrix\
                         must have the same size")

                fun2 = lambda x: True if (type(x) is int or type(x) is float) else False

                if all(list(map(fun2, lista))):
                    fun3 = lambda num: round(num / div, 2)
                    new.append(list(map(fun3, lista)))
                else:
                    raise TypeError("matrix must be a matrix\
                        (list of lists) of integers/floats")
        else:
            raise TypeError("matrix must be a matrix\
                (list of lists) of integers/floats")
    return new

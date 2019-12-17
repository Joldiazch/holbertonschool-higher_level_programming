#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        lista = []
        for num in my_list:
            if (num % 2) == 0:
                lista.append(True)
            else:
                lista.append(False)
        lista.reverse
        return(lista)

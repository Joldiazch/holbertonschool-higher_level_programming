#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dic = a_dictionary.copy()
    for k in dic:
        dic[k] *= 2
    return dic

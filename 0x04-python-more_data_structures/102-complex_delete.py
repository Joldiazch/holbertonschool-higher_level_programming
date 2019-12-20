#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    cop = a_dictionary.copy()
    for key in cop:
        if cop[key] == value:
            del a_dictionary[key]

    return a_dictionary

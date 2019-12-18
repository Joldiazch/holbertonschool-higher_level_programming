#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        new = my_list.copy()
        new.reverse()
        for index in new:
            print('{:d}'.format(index))

#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    for index in range(x):
        try:
            print(my_list[index], end="")
            i += 1
            pass
        except IndexError:
            break
    print()
    return i

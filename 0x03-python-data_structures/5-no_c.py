#!/usr/bin/python3
def no_c(my_string):
    my_string.translate({ord('c'): None})
    return(my_string)

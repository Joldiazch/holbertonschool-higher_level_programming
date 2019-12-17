#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if (not tuple_a) and (not tuple_b):
        return((0, 0))
    if not tuple_a:
        return(tuple_b)
    if not tuple_b:
        return (tuple_a)
    if (len(tuple_a) >= 2 and len(tuple_b) >= 2):
        c = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
        return(c)
    if (len(tuple_a) < 2 and len(tuple_b) < 2):
        c = (tuple_a[0] + tuple_b[0], 0)
        return(c)
    if len(tuple_a) < 2:
        c = (tuple_a[0] + tuple_b[0], tuple_b[1])
        return(c)
    if len(tuple_b) < 2:
        c = (tuple_a[0] + tuple_b[0], tuple_a[1])
        return(c)

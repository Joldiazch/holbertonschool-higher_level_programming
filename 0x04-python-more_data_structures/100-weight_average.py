#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        num = sum(map(lambda x: x[0] * x[1], my_list))
        den = sum(map(lambda x: my_list[x][1], range(len(my_list))))
        return num / den

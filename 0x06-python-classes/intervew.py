def weight_average(my_list=[]):
    mult = sum(list(map(lambda tup: tup[0] * tup[1], my_list)))
    den = sum(list(map(lambda tup: tup[1], my_list)))
    print (mult / den)

if __name__ == "__main__":
    my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
    weight_average(my_list)
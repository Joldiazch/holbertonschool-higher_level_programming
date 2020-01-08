#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_to_return = []
    for idx in range(list_length):
        try:
            resul = my_list_1[idx] / my_list_2[idx]
        except TypeError:
            print("wrong type")
            resul = 0
        except IndexError:
            print("out of range")
            resul = 0
        except ZeroDivisionError:
            print("division by 0")
            resul = 0
        finally:
            list_to_return.append(resul)
    return list_to_return

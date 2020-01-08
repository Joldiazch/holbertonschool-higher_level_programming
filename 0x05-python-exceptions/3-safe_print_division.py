#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        resul = a / b
    except ZeroDivisionError:
        resul = None
        return None
    finally:
        print("Inside result: {}".format(resul))
        return resul

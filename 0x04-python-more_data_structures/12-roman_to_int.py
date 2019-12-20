#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is str and roman_string != "":
        res = 0
        n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in roman_string:
            res += sum(map(lambda x: n[x] if x == i else 0, n))
        a = roman_string
        b = range(len(a) - 1, 0, -1)
        c = sum(map(lambda x: n[a[x - 1]] if n[a[x]] > n[a[x - 1]] else 0, b))
        res -= 2 * c
        return res
    return 0

#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is str and roman_string != "":
        res = 0
        num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in roman_string:
            res += sum(map(lambda x: num[x] if x == i else 0, num))
        a = roman_string
        res -= 2 * sum(map(lambda x: num[a[x - 1]]
   if num[a[x]] > num[a[x - 1]] else 0, range(len(a) - 1, 1, -1)))
        return res
    return 0

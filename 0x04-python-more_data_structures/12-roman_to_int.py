#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string:
        res = 0
        num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        if len(roman_string) != 1:
            for i in roman_string:
                res += sum(map(lambda x: num[x] if x == i else 0, num))
            if num[roman_string[-2]] < num[roman_string[-1]]:
                res -= num[roman_string[-2]] * 2
            return res
        return num[roman_string]
    return 0

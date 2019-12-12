#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a, b = 10, 5
    result_sum = add(a, b)
    print('{:d} + {:d} = {:d}'.format(a, b, result_sum))
    result_res = sub(a, b)
    print('{:d} - {:d} = {:d}'.format(a, b, result_res))
    result_mul = mul(a, b)
    print('{:d} * {:d} = {:d}'.format(a, b, result_mul))
    result_div = div(a, b)
    print('{:d} / {:d} = {:d}'.format(a, b, result_div))

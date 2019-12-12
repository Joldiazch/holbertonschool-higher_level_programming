#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    a, b = 10, 5
    result_sum = calculator_1.add(a, b)
    print('{:d} + {:d} = {:d}'.format(a, b, result_sum))
    result_res = calculator_1.sub(a, b)
    print('{:d} - {:d} = {:d}'.format(a, b, result_res))
    result_mul = calculator_1.mul(a, b)
    print('{:d} * {:d} = {:d}'.format(a, b, result_mul))
    result_div = calculator_1.div(a, b)
    print('{:d} / {:d} = {:d}'.format(a, b, result_div))

#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    if len(argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    else:
        operators = ['+', '-', '*', '/']
        if not (argv[2] in operators):
            print('Unknown operator. Available operators: +, -, * and /')
            exit(1)
        else:
            op, a, b = argv[2], int(argv[1]), int(argv[3])
            if op == '+':
                print('{:d} + {:d} = {:d}'.format(a, b, add(a, b)))
                exit(0)
            elif op == '-':
                print('{:d} - {:d} = {:d}'.format(a, b, sub(a, b)))
                exit(0)
            elif op == '*':
                print('{:d} * {:d} = {:d}'.format(a, b, mul(a, b)))
                exit(0)
            elif op == '/':
                print('{:d} / {:d} = {:d}'.format(a, b, div(a, b)))
                exit(0)

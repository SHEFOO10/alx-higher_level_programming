#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit
    if (len(argv) - 1 < 3):
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    match argv[2]:
        case '+':
            result = add(a, b)
            print(f'{a} {argv[2]} {b} = {result}')
        case '-':
            result = sub(a, b)
            print(f'{a} {argv[2]} {b} = {result}')
        case '*':
            result = mul(a, b)
            print(f'{a} {argv[2]} {b} = {result}')
        case '/':
            result = div(a, b)
            print(f'{a} {argv[2]} {b} = {result}')
        case _:
            print('Unknown operator. Available operators: +, -, * and /')
            exit(1)
    exit(0)

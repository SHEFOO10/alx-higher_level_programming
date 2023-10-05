#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit
    if (len(argv) - 1 != 3):
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    match argv[2]:
        case '+':
            print(f'{a} {argv[2]} {b} = {add(a, b)}')
        case '-':
            print(f'{a} {argv[2]} {b} = {sub(a, b)}')
        case '*':
            print(f'{a} {argv[2]} {b} = {mul(a, b)}')
        case '/':
            print(f'{a} {argv[2]} {b} = {div(a, b)}')
        case _:
            print('Unknown operator. Available operators: +, -, * and /')
            exit(1)
    exit(0)

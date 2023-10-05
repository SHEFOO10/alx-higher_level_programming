#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit
    if (len(argv) < 4):
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    match argv[2]:
        case '+':
            result = add(int(argv[1]), int(argv[3]))
            print(f'{argv[1]} {argv[2]} {argv[3]} = {result}')
        case '-':
            result = sub(int(argv[1]), int(argv[3]))
            print(f'{argv[1]} {argv[2]} {argv[3]} = {result}')
        case '*':
            result = mul(int(argv[1]), int(argv[3]))
            print(f'{argv[1]} {argv[2]} {argv[3]} = {result}')
        case '/':
            result = div(int(argv[1]), int(argv[3]))
            print(f'{argv[1]} {argv[2]} {argv[3]} = {result}')
        case _:
            print('Unknown operator. Available operators: +, -, * and /')
            exit(1)
    exit(0)

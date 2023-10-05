#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    print('{} argument{}{}'.format(
        len(argv) - 1,
        's' if (len(argv) - 1 != 1) else '',
        ':' if (len(argv) - 1 >= 1) else '.'))
    for i in range(1, len(argv)):
        print('{}: {}'.format(i, argv[i]))

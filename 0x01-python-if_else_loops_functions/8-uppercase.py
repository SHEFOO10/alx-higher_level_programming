#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if (ord(char) <= 90 and ord(char) >= 65):
            print('{}'.format(char), end='')
        else:
            print('{}'.format(chr(ord(char) - 32)))

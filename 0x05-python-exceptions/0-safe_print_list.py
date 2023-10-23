#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        for idx in range(x):
            print(my_list[idx], end='')
        else:
            print('')
    except IndexError:
        print('')
        return idx
    return x

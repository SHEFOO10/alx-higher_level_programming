#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    for idx in range(x):
        try:
            print("{:d}".format(my_list[idx]))
        except (TypeError, IndexError):
            return idx - 1
        except ValueError:
            continue
    return x

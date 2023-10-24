#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for idx in range(list_length):
        try:
            new_list.append(my_list_1[idx] / my_list_2[idx])
        except (TypeError, IndexError, ZeroDivisionError):
            new_list.append(0)
    return new_list

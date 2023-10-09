#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    max_number = my_list[0]
    for item in my_list:
        if item > max_number:
            max_number = item
        else:
            continue
    return max_number

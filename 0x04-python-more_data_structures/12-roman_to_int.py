#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    previous_number = 0
    roman_numbers = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000}

    if not isinstance(roman_string, str):
        return 0
    for char in roman_string:
        if (previous_number < roman_numbers[char]):
            result -= 2 * previous_number
        result += roman_numbers[char]
        previous_number = roman_numbers[char]
    return result

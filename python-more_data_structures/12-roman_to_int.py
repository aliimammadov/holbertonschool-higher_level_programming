#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_dict = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
            }
    total = 0
    pre_value = 0
    for ch in reversed(roman_string):
        value = roman_dict.get(ch, 0)
        if value < pre_value:
            total -= value
        else:
            total += value
            pre_value = value
    return total

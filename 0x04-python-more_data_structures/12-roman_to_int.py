#!/usr/bin/python3


def roman_to_int(roman_string):
    if (type(roman_string) is not str or roman_string is None):
        return 0
    roman_dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                        'M': 1000}
    num = 0
    for n, n_next in zip(roman_string, roman_string[1:]):
        if roman_dictionary[n] >= roman_dictionary[n_next]:
            num += roman_dictionary[n]
        else:
            num -= roman_dictionary[n]

    num += roman_dictionary[roman_string[-1]]
    return num

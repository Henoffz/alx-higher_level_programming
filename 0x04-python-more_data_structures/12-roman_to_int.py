#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string and type(roman_string) is str:
        rom_dict = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
        result = 0
        for x, y in zip(roman_string, roman_string[1:]):
            if rom_dict[x] < rom_dict[y]:
                result -= rom_dict[x]
            else:
                result += rom_dict[x]
        result += rom_dict[roman_string[-1]]
        return result
    else:
        return 0

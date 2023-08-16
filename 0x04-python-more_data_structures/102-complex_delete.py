#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dict_list = list(a_dictionary.items())
    for key, val in dict_list:
        if a_dictionary[key] is value:
            del a_dictionary[key]
    return (a_dictionary)

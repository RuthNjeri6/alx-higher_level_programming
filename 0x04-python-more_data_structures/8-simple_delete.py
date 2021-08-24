#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    new_dict = a_dictionary
    if key in new_dict.keys():
        new_dict.pop(key)
    return new_dict

#!/usr/bin/python3
def best_score(a_dictionary):
    biggest = 0
    try:
        if len(a_dictionary) == 0:
            return None
        for key, value in a_dictionary.items():
            if value >= biggest:
                biggest = value
                biggest_key = key
    except:
        biggest_key = None
    return biggest_key

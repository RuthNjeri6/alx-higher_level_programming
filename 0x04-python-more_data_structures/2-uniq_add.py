#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    new_list = []
    for item in my_list:
        if item not in new_list:
           new_list.append(item)
           sum += item
    return sum

#!/usr/bin/python3
def add_integer(a, b=98):
    """ Function that adds 2 numbers """

    var_list = [a, b]
    def isNotNumber(val):
        """check if type of a and b are not int or floats and raises a TypeError exception """

        if type(val) != int and type(val) != float:
            if val == a:
                raise TypeError('a must be an integer')
            elif val == b:
                raise TypeError('b must be an integer')
        elif type(val) == float:
            val = int(val)
        return val
    new_list = [isNotNumber(x) for x in var_list]
    return new_list[0] + new_list[1]
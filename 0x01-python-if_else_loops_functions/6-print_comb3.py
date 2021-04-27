#!/usr/bin/python3
for i in range(0, 10):
    for n in range(i + 1, 10):
        if (i is not 8) and (i is not 9):
            print("{0:d}{1:d}".format(i, n), end=(", "))
        else:
            print("{0:d}{1:d}".format(i, n))

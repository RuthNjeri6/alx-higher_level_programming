def uppercase(str):
    for c in str:
        if ord("a") <= ord(c) <= ord("z"):
            c = chr(ord(c) + (ord("A") - ord("a")))
        print("{0:s}".format(c), end="")
    print()

# coding=utf-8

tup = (1, 2, 3,)

try:
    print(tup[3])
except TypeError as err:
    print("Type Error occured: %s" % err)
except IndexError as err:
    print("Index Error occured: %s" % err)

# coding=utf-8

tup = (1, 2, 3,)

try:
    i = int(input("Which tupple's element you want to access?"))
    assert i > 0

    el = tup[i]
    print("The value of %d%s element is %s" % (i, ("st", "nd", "rd")[i - 1], el))
except TypeError as err:
    print("Type Error occured: %s" % err)
except IndexError as err:
    print("Index Error occured: %s" % err)
else:
    print("No exception occured")
finally:
    print("Good bye!")

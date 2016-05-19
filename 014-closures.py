# coding=utf-8


def add(start=0):
    def add(inc=1):
        return start + inc  # you can read the start from the outer scope, but you can't write to it

    return add


addTen = add(10)
print(addTen(100))

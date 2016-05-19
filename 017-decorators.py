# coding=utf-8


def my_decorator(func):
    def func_wrapper():
        return "TEST: {0}".format(func())

    return func_wrapper


@my_decorator
def my_func():
    return "my_func"


print(my_func("Test"))

# coding=utf-8


class MyAssertionError(Exception):
    pass


def assert_is_string(a1):
    if type(a1) != str:
        raise MyAssertionError("this is not a string")

try:
    assert_is_string(15)
except MyAssertionError as err:
    print("Assertion error: %s" % err)

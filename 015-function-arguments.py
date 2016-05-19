# coding=utf-8


def test_arg_list(pos_arg1, *args, **kwargs):
    print("arg: ", pos_arg1)
    print("args: ", args)
    print("kwargs: ", kwargs)


def test_kwargs(**kwargs):
    print("kwargs: ", kwargs)


test_arg_list(1, 2, 3, 4, 5, x=1, y=2)
test_kwargs(x=10, y=20)

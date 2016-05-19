# coding=utf-8


# this is a function:
def greet(name):
    # this is a function within function:
    def get_message():
        return "Hello, %s!"

    def exec():
        return get_message() % name

    # you can return a function from a function:
    return exec


# you can pass a function as a param:
def print_output(func):
    print(func())


print_output(greet("Alice"))
print_output(greet("Bob"))

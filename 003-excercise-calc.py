# coding=utf-8
from helpers.calc import add, divide


readdict = {"Add": [], "Subtract": [], "Multiply": [], "Divide": []}
calcAction = "continue"

while calcAction != "quit":
    calcAction = input("What type of operation?")
    if calcAction == "quit":
        continue

    print("you've selected " + calcAction)

    f1 = float(input("Give me number 1"))
    f2 = float(input("Give me number 2"))

    if calcAction == "Add":
        print("The result is: " + str(add(f1, f2)))
    if calcAction == "Divide":
        try:
            print("The result is: " + str(divide(f1, f2)))
        except Exception as e:
            print("Nice try: %s" % e)

# coding=utf-8


class Employee:
    """Common base class for Employees"""
    totalCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.totalCount += 1

    def display(self):
        print("Employee is: %s, his salary is: %d" % (self.name, self.salary))


e = Employee("misha", 345)
e.display()

print("Amount of employees: %d" % Employee.totalCount)

class Employee(object):
    """this class represents a single employee"""

    counter = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.count()

    @classmethod
    def count(cls):
        cls.counter += 1

    @classmethod
    def print_employees_counter(cls):
        print(f"Employees count: {cls.counter}")

    def get_salary(self):
        return self.salary

    def get_name(self):
        return self.name

    @classmethod
    def print_class_information(cls):
        print(f"Base: {cls.__base__}")
        print(f"Attributes: {cls.__dict__}")
        print(f"Class: {cls.__name__}")
        print(f"Module: {cls.__module__}")
        print(f"Documentation: {cls.__doc__}")


first = Employee("John", 5000)
first.print_employees_counter()
first.print_class_information()
print(first.get_salary())
print(first.get_name())

second = Employee("R", 2000)
second.print_employees_counter()

class Employee:
    """
    This is class Employee
    """
    __counter = 0

    def __init__(self, name, salary):
        Employee.__counter += 1
        self.__Name = name
        self.__Salary = salary

    @classmethod
    def __del__(cls):
        cls.__counter -= 1

    @classmethod
    def count_employees(cls):
        return f"In the Company now working {cls.__counter} employees"

    def employee_information(self):
        return f"Name: {self.__Name}\nSalary: {self.__Salary}"

    @classmethod
    def class_information(cls):
        print(f"Base: {cls.__base__}\n"
              f"Namespace: {cls.__dict__}\n"
              f"Name: {cls.__name__}\n"
              f"Module: {cls.__module__}\n"
              f"Documentation: {cls.__doc__}\n")


first_employee = Employee("Ryan", 4000)
print(first_employee.employee_information())

second_employee = Employee("Robert", 2700)
print(f"\n{second_employee.employee_information()}")
print(f"\n{Employee.count_employees()}")

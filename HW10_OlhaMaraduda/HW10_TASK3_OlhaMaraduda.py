# HW10_TASK3 
# Create an employee class. Each employee has characteristics such as name
# and salary. The class should have a counter that calculates the total number of
# employees, as well as a method that prints the total number of employees and a
# method that displays information about each employee in particular, namely the
# name and salary.
# In addition to creating a class, display information about the base classes from which 
# the employee class is inherited (__base__), the class namespace (__dict__), the 
# class name (__name__), the module name in which the class is defined 
# (__module__), the documentation bar ( __doc__)

class Employee:

    total_employees = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees +=1

    @classmethod
    def displ_total_employees(cls):
        return f"Total number of Employees: {cls.total_employees}"
    
    def displ_employee_info(self):
        return f"Name {self.name}, Salary {self.salary}"

emp1 = Employee("John Doe", 50000)
emp2 = Employee("Jane Smith", 60000)
emp3 = Employee("Jake Frost", 40000)

print(Employee.displ_total_employees())
print(emp1.displ_employee_info())
print(emp2.displ_employee_info())

print(f"Base classes: {Employee.__base__}")
print(f"Namespace: {Employee.__dict__}")
print(f"Class name: {Employee.__name__}")
print(f"Module name: {Employee.__module__}")
print(f"Documentation: {Employee.__doc__}")
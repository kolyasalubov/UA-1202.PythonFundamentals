# # # # Task1
class Polygon():
    def __init__(self,number_sides):
        self.number_sides = number_sides
        self.sides = []
        for i in range(number_sides):
               self.sides.append(i)
    def user_input(self):
         for i in range(self.number_sides):
              user = input(f"Enter the side {str(i+1)}: ")
              self.sides[i] = int(user)
    def show_sides(self):
         print(self.sides) 
    
class Rectungle(Polygon):
     def __init__(self):
          super().__init__(2)
     def space_rect(self):
        a , b = self.sides 
        S = a *b
        return ("Площа прямокутника",S)
rect = Rectungle()
rect.user_input()
rect.show_sides()
print(rect.space_rect())
# # # # Task2
class Human():
    def __init__(self,name,IQ):
        self.name = name
        self.IQ = IQ
    def greeting(self):
        print(f"Welcome {self.name}")
    def checking(self):
        if self.IQ >= 108.7:
             return (f"Congratulate {self.name} ,you are Homosapiens ")
        else:
            return (f" {self.name},you are not Homosapiens ")
    @staticmethod
    def saying_hi(self):
        print("HI")
person1 = Human("Vlad",180)
person2 = Human("Jack",90)
print(person2.checking())
print(person1.checking())
# Task3
class Employee():
    "class with employyes"
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    def display_employee(self):
         return self.name, self.salary
         
    @classmethod
    def display_count(cls):
        return cls.count
person1 = Employee("Andriy", 200)
person2 = Employee("Lack", 100)
print(Employee.display_count())
print("Base", Employee.__base__)
print("Class", Employee.__dict__)
print("Class", Employee.__name__)
print("Module", Employee.__module__)
print("Documentation", Employee.__doc__)
#######################################################################CODEWAR
# Task1
class Ball():
    def __init__(self,type = "regular"):
        self.type = type
    def ball_type(self):
        return self.type
ball1 = Ball()
ball2 = Ball("super")
print(ball1.ball_type())  
print(ball2.ball_type()) 
# Task2
from random import choice
class Ghost():
    colors = [  "white" ,   
    "yellow",    
    "purple",  
    "red"]
    @classmethod
    def color(cls):
        return choice(cls.colors)
ghost = Ghost()
print(ghost.color())
# Task3
class God():
    def __init__(self,human):
        self.human = human
class Man(God):
     def __init__(self):
         super().__init__("Adam")
     def display_Man(self):
         return self.human
class Women(God):
     def __init__(self):
         super().__init__("Eva")
     def display_Women(self):
         return self.human
adam = Man()
print(adam.display_Man())
eva = Women()
print(eva.display_Women())
# Task4
class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        return f"{self.name} your age is {self.age}"
person1 = Person("Lack",12)
print(person1.display())
# Task6
import re

def change_name(old_name, new_name):
    if not re.match('^[A-Z][a-zA-Z0-9]*$', new_name):
        raise ValueError("Class name must start with an uppercase letter and contain only alphanumeric characters.")
    if not re.match('^[A-Z][a-zA-Z0-9]*$', old_name):
        raise ValueError("Old class name must start with an uppercase letter and contain only alphanumeric characters.")
    globals()[new_name] = globals().pop(old_name)
print(change_name("Claea","asd"))
# Imports for tasks
import random
import math
import re


# First Task
class Ball:
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type


print("First Task:")
ball1 = Ball()
ball2 = Ball("super")
print(ball1.ball_type)  #=> "regular"
print(ball2.ball_type)  #=> "super"


# Second Task
class Ghost:
    def __init__(self):
        colors = ["white", "yellow", "purple", "red"]
        self.color = random.choice(colors)


print("\nSecond Task:")
ghosts = [Ghost() for _ in range(5)]
for ghost in ghosts:
    print(ghost.color)


# Third Task
class Human:
    def __init__(self, name):
        self.name = name


class Man(Human):
    def __init__(self, name):
        super().__init__(name)


class Woman(Human):
    def __init__(self, name):
        super().__init__(name)


def God():
    adam = Man("Adam")
    eva = Woman("Eva")
    return [adam, eva]


# Fourth Task
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info = f"{name}s age is {age}"


print("\nFourth Task:")
names = ["john", "matt", "alex", "cam"]
ages = [16, 25, 57, 39]
for i in range(4):
    name, age = names[i], ages[i]
    person = Person(name, age)
    print(person.info)


# Fifth Task
class Sphere(object):
    def __init__(self, radius, mass):
        self.radius = float(radius)
        self.mass = float(mass)

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        return round((4/3) * math.pi * self.radius ** 3, 5)

    def get_surface_area(self):
        return round(4 * math.pi * self.radius ** 2, 5)

    def get_density(self):
        volume = (4/3) * math.pi * self.radius ** 3
        return round(self.mass / volume, 5)


print("\nFifth task:")
ball = Sphere(2, 50)
print(ball.get_radius(),        #->2
      ball.get_mass(),          #->50
      ball.get_volume(),        #->33.51032
      ball.get_surface_area(),  #->50.26548
      ball.get_density())       #->1.49208


# Sixth Task
def class_name_changer(cls, new_name):
    if re.match("^[A-Za-z0-9]+$", new_name) and new_name[0].isupper():
        cls.__name__ = new_name
        return cls
    else:
        raise ValueError("Invalid class name. It must be alphanumeric and start with an uppercase letter.")


class MyClass:
    pass


UsefulClass = class_name_changer(MyClass, "UsefulClass")
print(UsefulClass.__name__)  # 'UsefulClass'

SecondUsefulClass = class_name_changer(UsefulClass, "SecondUsefulClass")
print(SecondUsefulClass.__name__)  # 'SecondUsefulClass'

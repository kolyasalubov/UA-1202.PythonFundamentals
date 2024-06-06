import random


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

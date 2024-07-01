# HW10_TASK2 
# Create a class Human, everyone has a name, create a method in the class
# that displays a welcome message to each person. Create a class method in the class
# that returns an information that it is a species of "Homosapiens".
# And in the class create a static method that returns an 
# arbitrary message

class Human:
    def __init__(self, name):
        self.name = name

    def welcome_message(self, greeting="Welcome"):
        return f"{greeting} {self.name}"
    
    @classmethod
    def info(cls, name):
        return f"{cls.__name__} {name} is a species of Homosapiens"
    
    @staticmethod
    def arbitrary_message():
        return "This is an arbitrary message from the Human class."


person = Human("Alice")
print(person.welcome_message())  # Output: Welcome Alice
print(Human.info(person.name))  # Output: Human Alice is a species of Homosapiens
print(Human.arbitrary_message())  # Output: This is an arbitrary message from the Human class.
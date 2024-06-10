class Human():
    def __init__(self, name):
        self.name = name

    def welcome(self):
        print("Welcome " + self.name)

    @classmethod
    def species_info(cls):
        return f"{cls.__name__} species is 'Homosapiens'"

    @staticmethod
    def message():
        print("Hi. I learn Python")


robert = Human("Robert")
robert.welcome()
print(Human.species_info())
robert.message()

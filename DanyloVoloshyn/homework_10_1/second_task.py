class Human:
    def __init__(self, name):
        self.name: str = name

    def greetings(self):
        return f"Hello {self.name.title()}"

    @classmethod
    def species_info(cls):
        return "This is a species of 'Homosapiens'."

    @staticmethod
    def arbitrary_message():
        return "This is an arbitrary message 😁"


person = Human("Petro")

print(person.greetings())
print(Human.species_info())
print(Human.arbitrary_message())

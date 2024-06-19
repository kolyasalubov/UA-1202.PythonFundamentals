class AgeError(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)


def check_age(age):
    try:
        age = int(age)
        if age <= 0:
            raise AgeError(f'Negative numbers are unacceptable')

    except ValueError:
        return f"I don't think that your age is '{age}'"

    else:
        return f"Alright you are {age}. And this is an {"even" if age % 2 == 0 else "odd"} number"


try:
    print(check_age(input("Enter your age: ")))
except AgeError as error:
    print(f"OOps, we have an error here {error}. Please try again.")

class InvalidAgeError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def check_user_age(age):
    age = int(age)
    if age < 0:
        raise InvalidAgeError("Negative numbers are not allowed.")
    else:
        return f"Your age is {age}. So your age is in the {'even' if age % 2 == 0 else 'odd'} numbers category."


try:
    user_age_input = input("Hello, please enter your age: ")
    result = check_user_age(user_age_input)
    print(result)
except InvalidAgeError as ine:
    print(f"Error: {ine}")
except ValueError as e:
    print(f"Error: You have to enter numbers, not symbols.")
finally:
    print("\nProgram execution completed.")

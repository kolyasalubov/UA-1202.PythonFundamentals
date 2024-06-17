week_dict = {
    "1": "Monday",
    "2": "Tuesday",
    "3": "Wednesday",
    "4": "Thursday",
    "5": "Friday",
    "6": "Saturday",
    "7": "Sunday",
}


class InvalidDayNumber(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def get_day(day):
    day = int(day)
    if day > 7 or day < 1:
        raise InvalidDayNumber("There are only 7 days in a week")
    else:
        return week_dict.get(str(day))


try:
    user_day_input = input("Hello, please enter the number: ")
    result = get_day(user_day_input)
    print(result)
except InvalidDayNumber as idn:
    print(f"Error: {idn}")
except ValueError as e:
    print(f"Error: You have to enter numbers, not symbols.")
finally:
    print("\nProgram execution completed.")

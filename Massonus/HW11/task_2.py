week_days = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}


def get_weekday(day):
    try:
        day = int(day)
    except ValueError:
        return "Incorrect day"
    else:
        if day > 8 or day < 1:
            return "There are only 8 days in a week"
        else:
            return week_days.get(day)


print("Your choice is:", get_weekday(input("Enter a number of a week day: ")))

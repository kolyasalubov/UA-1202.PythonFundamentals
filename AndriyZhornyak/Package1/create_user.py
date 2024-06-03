
def create_user_name():
    while True:
        name = input("Enter name of user: ")
        if len(name) > 10:
            print("Try again: Name should not exceed 10 characters.")
        elif any(char.isdigit() for char in name):
            print(" Name should not contain digits.")
        else:
            return f"Hello user: {name}"


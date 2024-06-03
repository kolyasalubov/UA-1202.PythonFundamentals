def check_password(password: str):
    if len(password) < 6 or len(password) > 16:
        return False

    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

    special_charactres = "$#@"

    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in special_charactres:
            has_special = True

    if not has_lower:
        print("There must be at least one lowercase letter in the password")
        return False
    if not has_upper:
        print("There must be at least one uppercase letter in the password")
        return False
    if not has_digit:
        print("There must be at least one digit in the password")
        return False
    if not has_special:
        print("There must be at least one special symbol in the password")
        return False

    return True


while True:
    input_message = input("Please enter your password or type 'exit' to leave the program: ")

    if input_message == "exit":
        print("\nGoodbye!")
        break

    validation_result = check_password(input_message)

    if validation_result is True:
        print("\nYour password is correct!")
        print("Thank you, have a good day!")
        break
    else:
        print(f"\nYour password is not correct!")

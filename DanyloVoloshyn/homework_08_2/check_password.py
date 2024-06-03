def check_password(password: str):
    error_messages = []

    if len(password) < 6 or len(password) > 16:
        error_messages.append("\nPassword must be between 6 and 16 characters long")

    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

    special_characters = "$#@"

    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True

    if not has_lower:
        error_messages.append("There must be at least one lowercase letter in the password")
    if not has_upper:
        error_messages.append("There must be at least one uppercase letter in the password")
    if not has_digit:
        error_messages.append("There must be at least one digit in the password")
    if not has_special:
        error_messages.append("There must be at least one special symbol in the password($#@)")

    if error_messages:
        return False, error_messages
    else:
        return True, []

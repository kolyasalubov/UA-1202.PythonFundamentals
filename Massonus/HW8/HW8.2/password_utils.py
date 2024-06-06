import re


def is_password_contain_letters(password):
    if not re.search('[a-z]', password) is None and not re.search('[A-Z]', password) is None:
        return True
    else:
        print("Password must contain at least one lowercase letter and one uppercase letter.")
        return False


def is_password_contain_numbers(password):
    if not re.search('[0-9]', password) is None:
        return True
    else:
        print("Password must contain at least one number")
        return False


def is_password_contain_symbols(password):
    if not re.search(r'[$#@!]', password) is None:
        return True
    else:
        print("Password must contain at least one special symbol ($#@!)")
        return False


def is_password_short(password):
    if len(password) < 6:
        print("Your password is too short. Minimum length is 6 characters")
        return False
    return True


def is_password_long(password):
    if len(password) > 16:
        print("Your password is too long. Maximum length is 16 characters")
        return False
    return True

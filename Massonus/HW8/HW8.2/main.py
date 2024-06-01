import password_utils as check

password = input("Enter your password: ")

is_contain_letters = check.is_password_contain_letters(password)
is_contain_numbers = check.is_password_contain_numbers(password)
is_contain_symbols = check.is_password_contain_symbols(password)
is_short = check.is_password_short(password)
is_long = check.is_password_long(password)

if is_contain_letters and is_contain_symbols and is_short and is_contain_numbers and is_long:
    print("Correct password!")
else:
    print("Incorrect password!")

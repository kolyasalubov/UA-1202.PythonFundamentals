# Write a Python program to check the validity of password (input from users)

# Validation:
# At least 1 letter between [a-z] and 1 letter between [A-Z]
# At least 1 number between [0-9]
# At least 1 character from [$#@]
# Minimum lenth 6 characters
# Maximum lenth 16 characters

import re
def password_check(password):
    if len(password) <6 or len(password) >16:
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    if not re.search(r'[$#@]', password):
        return False       

    return True   

#To check password:

password = input("Enter a password: ")

if password_check(password):
    print("Password is good to go.")
else:
    print("Password does not meets required criterias.")
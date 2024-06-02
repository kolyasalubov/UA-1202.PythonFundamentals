def log_in_file_password():
    while True:
        digit = input("Enter password: ")
        if len(digit) > 16:
            print("Password too long, try again")
        elif any(char.isalpha() for char in digit):
            print("Password should not contain letters, try again")
        else:
            return f"Congratulations, your password is: {digit}"


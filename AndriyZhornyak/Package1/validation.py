import re
def validation_code():
    while True:
        ask = (input("Enter the code: "))
        if  len(ask) > 16:
            print("Too long,change") 
        elif len(ask) < 6:
            print("Too short,change")
        elif  not re.search(r'[!@#$%^&*(),.?":{}|<>]', ask):
            print("Must be one special symbol")
        elif not re.search(r'[a-z]', ask):
            print("Must be one letter ")
        elif not re.search(r'[A-Z]', ask):
            print("Must be one  big letter ")
        else:
            return f"Your password is: {ask}"

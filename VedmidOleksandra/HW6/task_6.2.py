# Task2. Write a script that checks the login that the user enters. If the login is "First", then greet the users.
# If the login is different, send an error message.
# (need to use loop while)
#########################################
right_login = "First"

while True:
    input_login = input("Enter login (or type 'quit' to exit): ")

    if input_login == right_login:
        print("Hello! You are safe")
        break
    elif input_login.lower() == "quit":
        print("Exiting...")
        break
    else:
        print("Incorrect login. Please try again")
def check_login(login):
    while login != "First":
        login = input("Error, input login again: ")
    else:
        print("Login successful!")


check_login(input("Login: "))

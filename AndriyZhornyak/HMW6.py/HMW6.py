def login_check(number):
    while number != "First":
         number = (input("Try again: "))
    print("Welcome",number)
print(login_check(input("Enter login: ")))
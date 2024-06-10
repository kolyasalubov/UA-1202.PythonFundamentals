# TASK2
# Write a script that checks the login that user enters. If the login is "First", then greet the user. 
# If the login is different, send the error message. (need to use while loop)

# Option1

expected_login = "First"
max_attempts = 5
attempts = 0

while attempts < max_attempts:
    login = input("Enter your login: ")
    if login == expected_login:
        print("Welcome, dear user")
        break
    else:
        attempts +=1
        print(f"Incorrect login, please try another one")
if attempts == max_attempts:
    print(f"To many attempts, please try again in 10 minutes")

# Option2

# while True:
#     login = input("Enter your login: ")
#     if login == expected_login:
#         print("Welcome, dear user")
#         break
#     else:
#         print("Error. Incorrect login, try another")

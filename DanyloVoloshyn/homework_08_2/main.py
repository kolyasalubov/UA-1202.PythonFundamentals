from DanyloVoloshyn.homework_08_2.check_password import check_password

while True:
    input_message = input("Please enter your password or type 'exit' to leave the program: ")

    if input_message == "exit":
        print("\nGoodbye!")
        break

    is_valid, messages = check_password(input_message)

    if is_valid:
        print("\nYour password is correct!")
        print("Thank you, have a good day!")
        break
    else:
        print("\nYour password is not correct!")
        for message in messages:
            print(message)

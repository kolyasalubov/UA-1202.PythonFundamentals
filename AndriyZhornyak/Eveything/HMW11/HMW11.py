# Task1
# try:
#     ask = int(input())
#     if ask <= 0:
#         raise ValueError("Negative number") 
#     if ask % 2 == 0:
#         print("The number is even")
#     else:
#         print("The number is odd")
# except ValueError:
#     print(ValueError)
# Task2
# try:
#     ask = int(input("Enter number from 1 to 7: "  ))
#     if ask  <= 0 or ask > 7 or ask < 1:
#         raise ValueError("Incorrect input") 
#     match ask:
#         case 1:
#            print("Monday")
#         case 2:
#            print("Tuesday")
#         case 3:
#            print("Wednesday")
#         case 4:
#            print("Thursday")
#         case 5:
#            print("Friday")
#         case 6:
#            print("Saturday")
#         case 7:
#            print("Sunday")
# except ValueError:
#     print(ValueError)
def check(login):
    separators = ["-", "-id", "id"]
    for sep in separators:
        if sep in login:
            return True
correct_login = "employee-124"
print(check(correct_login))
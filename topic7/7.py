# def print_hello(user_name:str, user_age:int)->str:
#     """
#     Function: print_hello
#     Input param: user_name
#     Output param: "Hello, {user_name}"
#     """
#     return f"Hello, {user_name}, your age is {user_age}"


# print(print_hello(90, 67))
# print(print_hello("Stepan"))


# def my_sum(arg1=0, arg2=7):
#     total = arg1 + arg2
#     print("Inside the function : ", total)
#     return total
#     print("After operator the return")


# my_sum(67, 90)
# a = my_sum(10, 7)
########################################

# my_sum(67)
# my_sum(67, 90)
# my_sum(45, 89)
#########################################
# def user_greeting(age, name = "None"):
#     print(f"Hello, {name}, age is {age}")
    
# user_greeting(79)
###############################################

def print_numbers(*args):
    # print("argument: ")
    # print(number)
    print("vartuple: ", args, type(args))
    for var in args:
        print(var)

print_numbers()

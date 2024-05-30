# Task1
# def checking_value(argue1,argue2):
#     "Function evaluate the largest number of two"
#     if argue1 > argue2:
#          return argue1
#     elif argue2 > argue1:
#          return argue2
# print(checking_value(23,10))
# Task2
# def space_triangle(firstside,h):
#       S = 0
#       S = 0.5 * firstside * h
#       return S
# def space_square(firstside):
#       S = 0
#       S = firstside ** 2
#       return S
# def space_circle(r):
#       S = r*r*3.14 
#       return S
# choice = input("Choose what function do you want to choose:")
# if choice == "space_triangle":
#       ask1 = int(input("Put the value of the first side and the high to this side:"))
#       ask2 = int(input("Put the value of  the high to this side:"))
#       print(space_triangle(ask1,ask2))
# elif  choice == "space_square":
#       ask3 = int(input(("Put the value of the first ")))
#       print(space_square(ask3))
# elif  choice == "space_circle":
#       ask4 = int(input(("Put the value of the radius ")))
#       print(space_circle(ask4))
# else:
#       print("error")
# Task3
def calculating_string(string):
    str_new = list(enumerate(string))
    return str_new
a = str(input("Enter the string: "))
print(calculating_string(a))
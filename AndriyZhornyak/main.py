# Task1
# from Package1 import *
# print(list(filter(lambda str: not ("__" in str), dir())))
# Task2
# from Package1.validation import *
# print(validation_code)
# Task3
from Package1.calculation import *
user_choice = input("1-place_triangle,2-place_rectangle,3-place_circle: ")
match user_choice:
        case "1":
            print(place_triangle())
        case "2":
            print(place_rectangle())
        case "3":
            print(place_circle())
        case _:
            print("Error")

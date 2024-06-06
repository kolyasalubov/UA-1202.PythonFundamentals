import math


def main():
    print("Make your choice")
    print("1. To calculate area of a rectangle")
    print("2. To calculate area of a triangle")
    print("3. To calculate area of a circle")
    choice = input("Enter your choice: ")

    match choice:
        case "1":
            print(area_of_rectangle(float(input("Enter a length: ")), float(input("Enter a width: "))))
        case "2":
            print(area_of_triangle(float(input("Enter your length: ")), float(input("Enter your width: "))))
        case "3":
            print(area_of_circle(float(input("Enter your radius: "))))
        case _:
            print("Invalid choice, try again \n")
            main()


def area_of_rectangle(length, width):
    """function calculates the area of a rectangle"""

    return round(length * width, 2)


def area_of_triangle(base, height):
    """function calculates the area of a triangle"""

    return round(base * height / 2, 2)


def area_of_circle(radius):
    """function calculates the area of a circle"""

    return round(math.pi * radius**2, 2)


main()

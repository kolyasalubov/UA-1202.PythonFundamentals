# Task2. Write a program that calculates the area of a rectangle, triangle and circle 
# (write three functions to calcilate the area) and call the, in the main program depending 
# on the user's choise)

import math

def area_rectangle(length: float, width: float) -> float:
    """
    Function to calculate the area of a rectangle.
    """
    return length * width

def area_triangle(base: float, height: float) -> float:
    """
    Function to calculate the area of a triangle.
    """
    return 0.5 * base * height 

def area_circle(radius: float) -> float:
    """
    Function to calculate the area of a circle.
    """
    return math.pi * radius * radius

def main():
    print("Choose an option to calculate the area: ")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")

    users_choice = input("Enter the number of your choice: ")

    if users_choice == "1":
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = area_rectangle(length, width)
        print(f"The area of the rectangle is: {round(area, 2)}")

    elif users_choice == '2':
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = area_triangle(base, height)
        print(f"The area of the triangle is: {round(area, 2)}")

    elif users_choice == '3':
        radius = float(input("Enter the radius of the circle: "))
        area = area_circle(radius)
        print(f"The area of the circle is: {round(area, 2)}")

    else:
        print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()

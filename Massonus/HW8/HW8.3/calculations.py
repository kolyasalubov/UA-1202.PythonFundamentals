import math


def area_of_rectangle(length, width):
    """function calculates the area of a rectangle"""

    return round(length * width, 2)


def area_of_triangle(base, height):
    """function calculates the area of a triangle"""

    return round(0.5 * base * height, 2)


def area_of_circle(radius):
    """function calculates the area of a circle"""

    return round(math.pi * math.pow(radius, 2), 2)

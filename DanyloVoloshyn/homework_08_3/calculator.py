import math


def rectangle_area(length, width):
    return round(length * width, 2)


def triangle_area(base, height):
    return round(0.5 * base * height, 2)


def circle_area(radius):
    return round(math.pi * math.pow(radius, 2), 2)

import math


def distance(x1, y1, x2, y2):
    return round(math.sqrt((x1 - x2)**2 + (y1 - y2)**2), 2)


print(distance(int(input("Input x1: ")), int(input("Input y1: ")), int(input("Input x2: ")), int(input("Input y2: "))))

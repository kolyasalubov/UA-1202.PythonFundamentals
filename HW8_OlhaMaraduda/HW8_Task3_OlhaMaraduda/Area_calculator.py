# Write a program that calculates the area of a rectangle S=a*b,
# the area of a triangle S=0.5*h*a, the area of a circle S=pi*r**2. 
# This module must be used in another module in which we ask user of 
# which figure he wants to calculate.

# (To perform task, you need to import the math module, and from it the pow()
# function and the value of the variable pi, and the module, which contains 
# three function finding areas, into main program. The basic logic of the program is 
# executed in the main module)

import math

def area_of_rectangle(a, b):
    return a * b
def area_of_triangle(h, a):
    return 0.5 * h * a
def area_of_circle(r):
    return math.pi * math.pow(r,2)

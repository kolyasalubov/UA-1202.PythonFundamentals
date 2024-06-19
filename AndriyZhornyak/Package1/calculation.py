from math import pow,pi
def place_triangle():
     argue1 = float(input("Введіть сторону: "))
     h = float(input("Введіть H: "))
     S = 0.5*h*argue1
     return S
def place_rectangle():
     argue1 = float(input("Введіть сторону: "))
     argue2 = float(input("Введіть сторону: "))
     S = argue1*argue2
     return S
def place_circle():
     argue1 = float(input("Введіть R: "))
     S = pow(argue1,2) * pi
     return S

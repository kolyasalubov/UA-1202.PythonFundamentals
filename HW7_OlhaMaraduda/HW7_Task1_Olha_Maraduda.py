# HW7
# Task1. Write a function that returns the largest number of two 
# numbers (use DocStrings documentation strings in the function)


def larg_numb_funct(x: int = 1, y: int = 2) -> int:
    """
    Returns the largest of two numbers.
    x (int): first number,
    y (int): second number.

   Result:
    int: The largest of the two numbers.
    """
    return max(x, y)

result = larg_numb_funct(8, 9)
print(result)


# Task3. Write a script that will calculate the factorial of the entered number without using recursion.
# Example: 0!=1, 1!=1, 2!=2, 3!= 1*2*3=6, ....

def factorial(number):
    result = 1

    for i in range(1, number + 1):
        result *= i

    return result


number = int(input("Enter number: "))

print(f"The factorial of the number {number} is equal to {factorial(number)}")

# TASK_3
# Write the script that will calculate the factorial of the entered number without using recursion.
# Example: 0!=1, 1!=1, 2!=2, 3!=1*2*3=6.

factorial_number = int(input("Enter number to calculate factorial number:"))

factorial_result = 1

for i in range (1, factorial_number +1):
    factorial_result *= i

print(int(factorial_result))


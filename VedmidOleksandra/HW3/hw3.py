# Interchange the values of two variables without using the third variable.
 
 
num1 = input("Enter first number ")
num2 = input("Enter second number ")
 
print ("Before swapping: ")
print("Value of the first number : ", num1, " and the second number : ", num2)
 
# code to swap 'x' and 'y'
num1, num2 = num2, num1
 
print ("After swapping: ")
print("Value of the first number : ", num1, " and the second number : ", num2)

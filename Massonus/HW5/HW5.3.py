number = int(input("Enter a number: "))
factorial = 1

while number > 1:
    factorial *= number
    number -= 1

print(factorial)

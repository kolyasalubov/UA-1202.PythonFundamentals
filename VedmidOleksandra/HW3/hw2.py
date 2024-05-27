# A four-digit natural number is specified:
# - find the product of the digits of this number
# - write the number in reverse order
# - in ascending order, you need to sort the numbers included in the given number
number = input(("Enter a four-digit natural and hit enter "))

# find the product of the digits of this number
product = int(number[0]) * int(number[1]) * int(number[2]) * int(number[3])
print(f'The product of numbers is: {product}')

#number in reverse order
reversed_number = number[::-1]
print(f'The number in reverse order is: {reversed_number}')

#number in ascending order
ascending_number = "".join(sorted(number))
print(f'The number in ascending order is: {ascending_number}')



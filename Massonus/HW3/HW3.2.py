number = input("Input a four-digit number: ")
numbers = list(map(int, number))
result = numbers[0] * numbers[1] * numbers[2] * numbers[3]
print("Product of your number:", result)

reverse = int(number[::-1])
print("Reverse:", reverse)

numbers = sorted(numbers, reverse=False)
sorted_numbers = int(str(numbers[0]) + str(numbers[1]) + str(numbers[2]) + str(numbers[3]))

print("Reversed sort:", sorted_numbers)

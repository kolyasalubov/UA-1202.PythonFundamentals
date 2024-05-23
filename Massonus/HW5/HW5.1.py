numbers = []
while True:
    user_input = input("Enter a number, or if you want to quit enter 'q': ")
    if user_input == 'q':
        break
    numbers.append(user_input)

print("Your integer numbers are: ", numbers)

for number in numbers:
    numbers[numbers.index(number)] = float(number)

print("Float numbers", numbers)


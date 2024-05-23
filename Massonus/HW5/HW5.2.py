until = int(input("Enter a number: "))

previous_number = 1
next_number = 1
print(previous_number, next_number, end=" ")

while next_number < until:
    previous_number, next_number = next_number, previous_number + next_number
    print(next_number, end=" ")
    until -= 1

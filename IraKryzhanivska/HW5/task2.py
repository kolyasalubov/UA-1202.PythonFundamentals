n = int(input("Enter your number: "))

first_number = 0
next_number = 1
if n >= 0:
    print (first_number, end=" ")

while next_number <= n:
    first_number, next_number = next_number, first_number + next_number
    print(next_number, end=" ")
    
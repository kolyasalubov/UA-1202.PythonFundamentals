# Task1. In the range from 1 to 10 determine
# • even numbers that are divisible by 2,
# • odd numbers, which are divisible by 3,
# • numbers that are not divisible by 2 and 3.

even_divisible_by_2 = []
odd_divisible_by_3 = []
not_divisible_by_2_and_3 = []

for number in range(1, 11):
    if number % 2 == 0:
        even_divisible_by_2.append(number)
    elif number % 3 == 0:
        odd_divisible_by_3.append(number)
    else:
        not_divisible_by_2_and_3.append(number)
print(f"{even_divisible_by_2} are numbers that are divisible by 2")
print(f"{odd_divisible_by_3} are odd numbers, which are divisible by 3")
print(f"{not_divisible_by_2_and_3} are numbers that are not divisible by 2 and 3")
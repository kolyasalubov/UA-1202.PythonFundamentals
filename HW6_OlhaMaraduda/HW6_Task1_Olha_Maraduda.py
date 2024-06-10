
# TASK1 HW6
# In the range from 1 to 10 determine
# - even numbers that are divisible by 2
# - odd numbers, which are divisible by 3
# - numbers that are not divisible by 2 and 3

# Option1
even_list = [x for x in range(1, 11) if x % 2 == 0]
print("Even numbers that are divisible by 2:", even_list)

odd_list2 = [x for x in range(1, 11) if x % 2 == 1 and x % 3 == 0]
print("Odd numbers that are divisible by 3:", odd_list2)

remaining_val_list3 = [x for x in range(1, 11) if x % 2 != 0 and x % 3 != 0]
print("Numbers that are not divisible by 2 and 3:", remaining_val_list3)

# Option2
even_list= []
odd_list = []
remaining_val_list = []

for x in range (1, 11):
    if x % 2 == 0:
        even_list.append(x)
    elif x % 2 == 1 and x % 3 == 0:
        odd_list.append(x)
    elif x % 2 !=0 and x % 3 !=0:
        remaining_val_list.append(x)

print("Even numbers that are divisible by 2:", even_list)
print("Odd numbers that are divisible by 3:", odd_list)
print("Numbers that are not divisible by 2 and 3:", remaining_val_list)



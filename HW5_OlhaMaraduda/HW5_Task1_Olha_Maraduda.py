# TASK_1
# Create a list that contains elements of integer type, then use the loop to change the type of these elements
# to a floating type. (Hint: use built-in float() function)

numbers_list = [1, 2, 3, 4, 5, 6, 7]

for numb in range(len(numbers_list)):
    numbers_list[numb] = float(numbers_list[numb])

print(numbers_list)
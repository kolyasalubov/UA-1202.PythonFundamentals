# Task1. Create a list that contains elements of integer type, then use
# the loop to change the type of these elements to a floating type.
# (Hint: use the built-in float () function).

integer_list = [1, 2, 3, 4, 5]

for i in range(len(integer_list)):
    integer_list[i] = float(integer_list[i])

print(integer_list)
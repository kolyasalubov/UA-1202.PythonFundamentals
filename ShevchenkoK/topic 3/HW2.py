my_number = "24937"

# part 1
print(int(my_number[0]) \
      * int(my_number[1]) \
      * int(my_number[2]) \
      * int(my_number[3]) \
      * int(my_number[4]))

# part 2
print(my_number[::-1])

# part 3
print("".join(sorted(my_number)))

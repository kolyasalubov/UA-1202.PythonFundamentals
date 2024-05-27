number = 9374
string_number = str(number)

result = int(string_number[0]) * int(string_number[1]) * int(string_number[2]) * int(string_number[3])

reverse_number = string_number[::-1]

sorted_number = sorted(string_number)

print(result)
print(reverse_number)
print("".join(sorted_number))

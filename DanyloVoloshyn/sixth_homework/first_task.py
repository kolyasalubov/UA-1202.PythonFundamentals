# number_lst = [2, 7, 1, 13, 74, 66, 27, 92, 38, 54]
number_lst = list(range(1, 11))

even_lst = []
odd_div_by_3_lst = []
not_div_by_2_and_3_lst = []

for number in number_lst:
      if number % 2 == 0:
            even_lst.append(number)
      elif number % 3 == 0:
            odd_div_by_3_lst.append(number)
      else:
            not_div_by_2_and_3_lst.append(number)

print("Even numbers that are divisible by 2:", even_lst)
print("Odd numbers that are divisi:", odd_div_by_3_lst)
print("Numbers that are not divisible by 2 and 3:", not_div_by_2_and_3_lst)
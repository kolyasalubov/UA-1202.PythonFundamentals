# def mean(number):
#     n_str = str(number)
#     digits_sum = 0
#     for digit in n_str:
#         digits_sum += int(digit)
#     return round(digits_sum/len(n_str))
# mean(3232)        
# def is_isogram(word):
#     word = word.lower()
#     for i in word:
#         if word.count("i")>1:
#             return False
#     return True
# print(is_isogram("Abradabra"))   
# def integer_boolean(binary_number):
#     list_1 = []
#     n_number = str(binary_number)
#     for digit in n_number:
#      if digit == "1":
#         list_1.append(True)
#      else:
#         list_1.append(False)
#     return list_1
# print(integer_boolean(1010101))
# def filter_list(lst):
#     for i in lst:
#         if type(i) == str:
#             lst.remove(i)
#     return lst
# print(filter_list([3432,234,4334,3432]))

# l1 = [ x for x in range(1, 11) if x % 2 == 0 ]
# l2 = [ x for x in range(1, 11) if x % 2 == 1 and x % 3 == 0 ]
# l3 = [ x for x in range(1, 11) if not x % 2 == 0 and not x % 3 == 0 ]
# print(l1, 'is even multiple of 2')
# print(l2, 'is an odd multiple of 3')
# print(l3, 'not divisible by 2 and 3')
# def string_int(str1):
#      num = int(str1)
#      if num > 0:
#          return num
#      else:       
#          return "Not a number"
# print(string_int("324"))
# def card_hide(card):
#     if len(card) >= 16:
#         lst = [card]
#     else:
#          return "Invalid card"
# print(card_hide(1234567890098765432))
# def card_hide(card):
#     lst = []
#     card_str = str(card)
#     if len(card_str) >= 16:
#         for digit in card_str:
#             lst.append(digit)
#             return lst
#     else:
#          return "Invalid card"
# print(card_hide(123456789123456789876543))
# Write a function that returns the arithmetic mean of any number of numbers.
# def mean(numbers):
#     numbers_str = str(numbers)
#     sum = 0
#     for digit in numbers_str:
#         sum+=int(digit)
#     return sum/len(numbers_str)
# print(mean(12345432))

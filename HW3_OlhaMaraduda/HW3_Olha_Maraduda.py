# TASK_1
# OPTION1

# Zen_of_python = """The Zen of Python, by Tim Peters

# 1.Beautiful is better than ugly.
# 2.Explicit is better than implicit.
# 3.Simple is better than complex.
# 4.Complex is better than complicated.
# 5.Flat is better than nested.
# 6.Sparse is better than dense.
# 7.Readability counts.
# 8.Special cases aren't special enough to break the rules.
# 9.Although practicality beats purity.
# 10.Errors should never pass silently.
# 11.Unless explicitly silenced.
# 12.In the face of ambiguity, refuse the temptation to guess.
# 13.There should be one-- and preferably only one --obvious way to do it.
# 14.Although that way may not be obvious at first unless you're Dutch.
# 15.Now is better than never.
# 16.Although never is often better than *right* now.
# 17.If the implementation is hard to explain, it's a bad idea.
# 18.If the implementation is easy to explain, it may be a good idea.
# 19.Namespaces are one honking great idea -- let's do more of those!
# 20.Beautiful is better than ugly.
# 21.Explicit is better than implicit.
# 22.Simple is better than complex.
# 23.Complex is better than complicated.
# 24.Flat is better than nested.
# 25.Sparse is better than dense.
# 26.Readability counts.
# 27.Special cases aren't special enough to break the rules.
# 28.Although practicality beats purity.
# 29.Errors should never pass silently.
# 30.Unless explicitly silenced.
# 31.In the face of ambiguity, refuse the temptation to guess.
# 32.There should be one-- and preferably only one --obvious way to do it.
# 33.Although that way may not be obvious at first unless you're Dutch.
# 34.Now is better than never.
# 35.Although never is often better than *right* now.
# 36.If the implementation is hard to explain, it's a bad idea.
# 37.If the implementation is easy to explain, it may be a good idea.
# 38.Namespaces are one honking great idea -- let's do more of those!Beautiful is better than ugly.
# 39.Explicit is better than implicit.
# 40.Simple is better than complex.
# 41.Complex is better than complicated.
# 42.Flat is better than nested.
# 43.Sparse is better than dense.
# 44.Readability counts.
# 45.Special cases aren't special enough to break the rules.
# 46.Although practicality beats purity.
# 47.Errors should never pass silently.
# 48.Unless explicitly silenced.
# 49.In the face of ambiguity, refuse the temptation to guess.
# 50.There should be one-- and preferably only one --obvious way to do it.
# 51.Although that way may not be obvious at first unless you're Dutch.
# 52.Now is better than never.
# 53.Although never is often better than *right* now.
# 54.If the implementation is hard to explain, it's a bad idea.
# 55.If the implementation is easy to explain, it may be a good idea.
# 56.Namespaces are one honking great idea -- let's do more of those!"""

# Zen_of_python_lower = Zen_of_python.lower()
# better_count = Zen_of_python_lower.count(" better ")
# never_count = Zen_of_python_lower.count(" never ")
# is_count = Zen_of_python_lower.count ( " is ")

# print(f'The word "better" appears {better_count} times in the text.')
# print(f'The word "never" appears {never_count} times in the text.')
# print(f'The word "is" appears {is_count} times in the text.')

#OPTION2

# file_path = r"C:\Users\Home\Desktop\Learning materials\Python\02. Git - Version Control Systems\Zen of Python.txt"
# with open(file_path, 'r') as file:

#     Zen_of_python = file.read()
#     Zen_of_python_lower = Zen_of_python.lower()
#     better_count = Zen_of_python_lower.count(" better ")
#     never_count = Zen_of_python_lower.count(" never ")
#     is_count = Zen_of_python_lower.count ( " is ")

# print(f'The word "better" appears {better_count} times in the text.')
# print(f'The word "never" appears {never_count} times in the text.')
# print(f'The word "is" appears {is_count} times in the text.')

# TASK_2
# A four digit natural number is specified. 
# find the product of the digits of this number 
# write the number in reverse order
# in ascending order you need to sort the number included to the given number

# number = 1234
# digits = [int(digit) for digit in str(number)]
# product = 1
# for digit in digits:
#     product *= digit

# reverse_number = int(str(number)[::-1])
# sorted_digits = ''.join(sorted(str(number)))

# print("Product of the digits:", product)
# print("Reversed number:", reverse_number)
# print("Digits sorted in ascending order:", sorted_digits)

# TASK_3
# interchange the values of two variables without using the third variable 

# a = 15
# b = 5

# a, b = b, a

# print("a:", a)
# print("b:", b)
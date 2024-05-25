# Task1
# list = [221321,534,2324]
# list1 = []
# for item in list:
#     list1.append(float(item))
# print(list1)
# Task2

# Task3
# number = int(input())
# factorial = 1 
# for i in range(1, number+1):
#     factorial*i
#     print(i)
# def counting_vowels(string):
#      vowels = {'a', 'e', 'i', 'o', 'u'}
#      count = 0
#      for i in string:
#           if i in vowels:
#                count+=1
#      return count
# print(counting_vowels("Celebration"))
# Taks2


n = 15
num1 = 0
num2 = 1
number3 = num2  
count = 1
 
while count <= n:
    print(number3)
    count += 1
    num1, num2 = num2, number3
    number3 = num1 + num2
print()
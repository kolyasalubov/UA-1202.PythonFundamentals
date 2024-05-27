# x = 'foo'
# print("1:", id(x), x)
# y = x
# print("2:", id(x), x)
# print("1:", id(y), y)    
# y += "bar"
# print("3:", id(x), x)  
# print("2:", id(y), y)  

##################################

# x = [1, 2, 3]
# y = x
# print("1:x:", id(x), x)
# print("1:y:", id(y), y)    
# print (x)             # [1, 2, 3]
# y += [3, 2, 1]
# print (x)             # [1, 2, 3, 3, 2, 1]
# print("2:x:", id(x), x)

#############################################
# colors = ["red", "blue", "green"]

# color = ["red", 
#          "blue", 
#          "green"]
################################################
# a = 90
# b = 56
# v = 45
# k = 8

# if a > 10:
#     r = 90
#     l = 5
#     k = k + 1
#####################################################
# a, b, v, k = 90, 56, 45, 8
# print(a, id(a), b, id(b), v, id(v), k, id(k))

# d = h = o = 999
# print(d, id(d), h, id(h), o, id(o))

#######################################################

# PI = 3.14
# print(PI)

# PI = 900

# print(PI)
######################################################
# x = 34 + 6j
# print(x.imag, type(x.imag), x.real, type(x.real))
# a = 10
# b = 2
# print(a/b, type(a/b)) 
#############################################

# str1 = "p"
# str2 = "Python"

# print(type(str1), type(str2))

#############################################
# PATH1 = "querty\table\name"
# PATH2 = r"querty\table\name"

# print(PATH1)
# print(PATH2)
###########################################
# name = "John"
# age = 23
# salary = 999.99


# print("His name is %s is %d years old. Your sallary is %.2f $" % (age, name, salary))
##########################################################################################
# a = 'John'
# b = 'Bill'
# c = 9999
# # default(implicit) order
# default_order = "Hello, {}, {} and {}".format(a, b, c)
# print(default_order)

# # order using positional argument
# positional_order = "{1}, {0} and {2}".format('John','Bill','Sean')
# print(positional_order)

# # order using keyword argument
# keyword_order = "{s}, {b} and {j}".format(j='John',b='Bill',s='Sean')
# print(keyword_order)
#########################################################################
# a = 'John'
# b = 'Bill'
# c = 'Sean'
# # default(implicit) order
# default_order = f"Hello, {a}, {b} and {c}"
# print(default_order)
############################################################################

# str = 'programiz'
# # print('str = ', str)

# # #first character
# # print('str[0] = ', str[0])

# # # #last character
# # print('str[-1] = ', str[-1])

# # # #slicing 2nd to 5th character
# # print('str[1:5] = ', str[1:5])

# # # #slicing 6th to 2nd last character
# t = str[5:-2]
# print('str[5:-2] = ', t, type(t) )
#######################################

# list1 = ["u", "o", "t", "3"]
# print(list1[0:2])
###########################################

















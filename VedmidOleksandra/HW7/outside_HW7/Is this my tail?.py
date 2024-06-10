# Some new animals have arrived at the zoo. The zookeeper is concerned that perhaps
# the animals do not have the right tails. To help her,
# you must correct the broken function to make sure that the second argument (tail)
# is the same as the last letter of the first argument (body) - otherwise the tail wouldn't fit!
#
# If the tail is right, return true, else return false.
# The arguments will always be non-empty strings, and normal letters.

def correct_tail(body, tail):
    # Get the substring of 'body' that has the same length as 'tail'
    sub = body[-len(tail):]
    # Compare the substring with 'tail'
    return sub == tail


print(correct_tail("elephant", "t"))  # True
print(correct_tail("elephant", "nt"))  # True
print(correct_tail("elephant", "h"))  # False
print(correct_tail("giraffe", "ffe"))  # True
print(correct_tail("giraffe", "f"))  # False


def my_func(input_message, numb=1):
    print(input_message * numb)


print("Hello")
print("Hi", 5)


def output_param(x, y, z):
    print(x, y, z)


my_tuple = (1, 2, 3)
output_param(*my_tuple)

my_func = lambda x: x if x > 5 else x ** 2 * my_func(10)
print(my_func(2))

my_list = [lambda x: x ** 2, lambda x: x ** 3,
           lambda x: x ** 4]
for item in my_list:
    print(item(5))


    def my_func(first_param=3, second_param=1):
        first_param = first_param + second_param
        second_param += 1
        print(first_param, second_param)


    my_func(second_param=1, first_param=3)




    counter = 5


    def my_func():
        counter = 8
        print(counter)


    my_func()
    print(counter)

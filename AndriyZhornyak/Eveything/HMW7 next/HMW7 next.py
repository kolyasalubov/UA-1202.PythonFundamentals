# Task1
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)
# Task2
import math

def distance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return round(dist, 2)
# Task3
def filter_words(st):
    st = st.capitalize()
    return  st.replace("  "," ")       
print(filter_words("This  will  not  pass"))
# Taks4
def number_to_string(num):
    str_num = str(num)
    return str_num
def reverse(st):
     st = st.split()
     reverse_st = st.reversed()
# Task5
def reverse(st):
   st = st.split()
   reverse_st = st[::-1]
   reversed_string = ' '.join(reverse_st)
   return reversed_string
# Task6
def reverse_list(l):
    l.reverse()
    return l
print(reverse_list([1,2,3,4,5]))
# Task7
def solution(number):
    if number < 0:
        return 0
    sum = 0
    for i in str(number):
        if int(i) % 3 == 0 or int(i) % 5 == 0:
            sum+=int(i)
    return sum
    pass
# Task8
def zero_fuel(distance_to_pump, mpg, fuel_left):
    distance_can_travel = mpg * fuel_left
    return distance_can_travel >= distance_to_pump
# # Task9
def are_you_playing_banjo(name):
    name_list = name.split()
    if name_list[0][0] == "r" or name_list[0][0] == "R":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
# # Task10
def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    elif boolean == False:
        return "No"
# Task11
def count_sheep(sheep_list):
    count = 0
    for sheep in sheep_list:
        if sheep:
            count += 1
    return count
sheep_list = [True, False, True, True, False, True, False, False, True, True,True,True,True,True,True,True,True,True,True,True,True]
print(count_sheep(sheep_list))
# Task12
def correct_tail(body, tail):
    sub = body[-len(tail):]
    if sub == tail:
        return True
    else:
        return False
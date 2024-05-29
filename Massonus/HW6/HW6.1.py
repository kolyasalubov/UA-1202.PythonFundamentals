numbers = [inside for inside in range(1, 11)]
print("Initial:", numbers)


def divisible_by2(list_param):
    result = []
    for number in list_param:
        if number % 2 == 0:
            result.append(number)
    return result


def divisible_by3(list_param):
    result = []
    for number in list_param:
        if number % 3 == 0:
            result.append(number)
    return result


def non_divisible_by3_and_by2(list_param):
    result = []
    for number in list_param:
        if number % 3 != 0 and number % 2 != 0:
            result.append(number)
    return result


print("Even numbers that are divisible by 2:", divisible_by2(numbers))
print("Odd numbers, which are divisible by 3:", divisible_by3(numbers))
print("Numbers that are not divisible by 2 and 3:", non_divisible_by3_and_by2(numbers))

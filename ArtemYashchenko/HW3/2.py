#take number from user
user_number = int(input("Enter a four-digit natural number: "))

#chek is user number four-digit
def is_four_digit_number(user_number):
    return 1000 <= user_number <= 9999
if not is_four_digit_number(user_number):
    print("Wrong number! Type four-digit number.")
else:
    num_str = str(user_number)

    #product of digits
    product = 1 
    for digit in num_str:
        product *= int(digit)

    #reversed number
    reverse_number = num_str[::-1]

    #sorting digits
    sorted_digits = ''.join(sorted(num_str))

    #display result
    print(f"Product of the digits: {product}")
    print(f"Number in reverse order: {reverse_number}")
    print(f"Digits in ascending order: {sorted_digits}")
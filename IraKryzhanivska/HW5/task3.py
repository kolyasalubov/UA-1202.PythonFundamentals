number = int(input("Enter your number: "))
if number == 0 or number == 1:
        print (1)
else:
    factorial = 1
    for i in range(2, number + 1):
        factorial *= i
    print (factorial)

    



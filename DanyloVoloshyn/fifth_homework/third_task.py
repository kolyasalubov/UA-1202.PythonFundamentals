input_number = int(input("Input natural number: "))

fact = 1

if input_number == 0 or input_number == 1:
    print(f"Factorial {input_number}! = {fact}")
elif input_number < 0:
    print("Factorial of a non-positive number doesn't exist")
else:
    for i in range(1, input_number + 1):
      fact *= i
    print(f"Factorial {input_number}! = {fact}")
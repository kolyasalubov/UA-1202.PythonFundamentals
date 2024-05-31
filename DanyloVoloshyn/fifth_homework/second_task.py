input_number = int(input("Enter numbers: "))

fibonacci_numbers = [0, 1]

for i in range(2, input_number):
      fibonacci_numbers.append(fibonacci_numbers[i-1] + fibonacci_numbers[i-2])

print(f"There are some Fibonacci numbers till the number you entered ({input_number}):\n{fibonacci_numbers}")

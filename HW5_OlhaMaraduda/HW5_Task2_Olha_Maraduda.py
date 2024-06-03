# TASK2
# Print Fibonacci numbers up to the entered number n, using cycles.
# (Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13 etc.)

n = int(input("Enter your number to get Fibonacci sequence:"))

fib_seq = [0, 1]

while fib_seq [-1] + fib_seq [-2] <=n:
    fib_seq.append(fib_seq[-1]+ fib_seq[-2])

print("Fibonacci sequence up to", n, "is:", fib_seq)



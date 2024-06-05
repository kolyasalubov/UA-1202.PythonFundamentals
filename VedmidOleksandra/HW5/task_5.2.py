# Task2. Print Fibonacci numbers up to the entered number n, using cycles.
# (Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13, etc.)

def print_fibonacci_numbers(n):
    a, b = 0, 1

    while a <= n:
        print(a, end=' ')
        # Обновляем значения a и b
        a, b = b, a + b

n = int(input("Введите число n: "))

print_fibonacci_numbers(n)
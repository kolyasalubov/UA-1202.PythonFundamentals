num = int(input("Input the number "))
fib = 0
fib2 = 1
fibList = []
while fib < num:
    fibList.append(fib)
    fib, fib2 = fib2, fib + fib2
    
print(fibList)
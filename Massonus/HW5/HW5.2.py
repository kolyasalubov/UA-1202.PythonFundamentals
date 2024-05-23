until = int(input("Enter a number: "))

f1 = 1
f2 = 1
print(f1, f2, end=" ")

while f2 < until:
    f1, f2 = f2, f1 + f2
    print(f2, end=" ")
    until -= 1

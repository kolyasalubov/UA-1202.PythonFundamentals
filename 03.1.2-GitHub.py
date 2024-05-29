a = str(1488)

p= int(a[0])*int(a[1])*int(a[2])*int(a[3])

print("Prodact of the digits is:",p,"\n")

print("digits backvards:")
for i in range(len(a)):
    print(a[len(a) - 1 - i])

n1 = 7
n2 = 8
print(f"\nbefore swaping n1 = {n1}, n2 = {n2}")
n1, n2 = n2, n1
print(f"after swaping n1 = {n1}, n2 = {n2}\n")


#print(sort((int(a))))


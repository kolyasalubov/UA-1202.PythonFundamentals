#prodacting 4 digits

a = str(8184)

p= int(a[0])*int(a[1])*int(a[2])*int(a[3])

print("\n\nProdact of the",a,"digits is:",p,"\n")

#writing in reversed order

print("digits backvards:")
for i in range(len(a)):
    print(a[len(a) - 1 - i])


#sorting 

l_of_d = list(a)

l_of_d.sort()

print("\nSorted digits are:",''.join(l_of_d))
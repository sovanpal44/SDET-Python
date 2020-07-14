numlist1 = [10, 15, 25, 20]
numlist2 = [40, 45, 63, 50]
numlist3 = []

for x in numlist1:
    if x%2!=0:
        numlist3.append(x)

for y in numlist2:
    if y%2 == 0:
        numlist3.append(y)

print("new list is ", numlist3)

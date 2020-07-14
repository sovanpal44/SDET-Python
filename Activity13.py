def cal_sum(numlist):
    sum = 0
    for number in numlist:
        sum = sum + number
    return sum
numlist = [10, 20, 5, 15]
result = cal_sum(numlist)
print("The sum of all the elements is: ", result)


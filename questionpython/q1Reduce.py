from functools import reduce

num = [1,2,3,4,5]
maxNum = 0
for i in range(len(num)):
    if(num[i] > maxNum):
        maxNum = num[i]

print(maxNum)
maxNum = reduce(lambda x, y: x if x > y else y, num)
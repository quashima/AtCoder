from sys import stdin

# function
def splitNum(_num):
    result = []
    while _num > 0:
        result.append(_num % 10)
        _num //= 10
    result.reverse()
    
    return result

# input
input = [stdin.readline().rstrip().split() for _ in range(1)]
max = int(input[0][0])
minSum = int(input[0][1])
maxSum = int(input[0][2])

# algorithm
# get target list
targetList = []
for num in range(max+1):
    target = num + 1
    if max < target:
        break;
    targetList.append(target)

# check
resultList = []
for elm in targetList:
    if minSum <= sum(splitNum(elm)) <= maxSum:
        resultList.append(elm)

# ans
print('ans', sum(resultList))

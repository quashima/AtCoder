from sys import stdin

# input
input = [stdin.readline().rstrip().split() for _ in range(2)]
target_list = [int(elm) for elm in input[1]]

# algorithm
# round up
average = - (-sum(target_list) // int(input[0][0]))

result = 0
for elm in target_list:
    result += (elm - average) ** 2

# ans
print('ans:', result)
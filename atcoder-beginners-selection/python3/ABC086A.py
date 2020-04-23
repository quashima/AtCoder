from sys import stdin

# input
input = [stdin.readline().rstrip().split() for _ in range(1)]

# algorithm
product = int(input[0][0]) * int(input[0][1])
result = product % 2

# ans
if (result == 0) :
    print('Even')
else:
    print('Odd') 
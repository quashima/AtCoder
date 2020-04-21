from sys import stdin

# input
input = [stdin.readline().rstrip().split() for _ in range(3)]

# algorithm
sum = int(input[0][0]) + int(input[1][0]) + int(input[1][1])

# ans
print("{} {}".format(sum, input[2][0]))
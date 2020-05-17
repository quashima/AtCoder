from sys import stdin

# input
input = input()

# algorithm
result = sum([elm + 1 for elm in range(int(input))])

# ans
print('ans', result)
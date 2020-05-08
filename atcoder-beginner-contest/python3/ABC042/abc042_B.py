from sys import stdin

# input
length = input().split()
targets = [input() for _ in range(int(length[0]))]

# ans
print('ans:', ''.join(sorted(targets)))
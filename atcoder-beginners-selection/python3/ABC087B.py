from sys import stdin

# input
input = [stdin.readline().rstrip().split() for _ in range(4)]
a = int(input[0][0])
b = int(input[1][0])
c = int(input[2][0])
d = int(input[3][0])

# algorithm
count = 0
for _a in range (a + 1):
    for _b in range(b + 1):
        for _c in range(c + 1):
            sum = (500 * _a) + (100 * _b) + (50 * _c)
            if d == sum:
                count += 1

# ans
print('ans', count)

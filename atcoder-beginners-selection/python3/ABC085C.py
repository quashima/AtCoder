from sys import stdin

# input
input = [stdin.readline().rstrip().split() for _ in range(1)]
print(input)
sheet = int(input[0][0])
yen = int(input[0][1])

result = '-1 -1 -1'
for i1 in range(sheet):
    for i2 in range(sheet - i1):
        i3 = (sheet - (i1 + i2))
        result_yen = (10000 * i1) + (5000 * i2) + (1000 * i3)
        if yen == result_yen:
            result = str(i1) + ' ' + str(i2) + ' ' + str(i3) 

# ans
print('ans', result)
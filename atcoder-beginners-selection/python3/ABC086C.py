from sys import stdin

# input
length = int(input())
targets = [stdin.readline().rstrip().split() for _ in range(length)]

# algorithm
check = True
for elm in targets:
    t = int(elm[0])
    xy = int(elm[1]) + int(elm[2])

    if t < xy:
        check = False
        break

    if (t + xy) % 2:
        check = False
        break

# ans
if check:
    print('Yes')
else:
    print('No')
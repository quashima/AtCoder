from sys import stdin

# input
input = [stdin.readline().rstrip().split() for _ in range(2)]
universal_set = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

subset = [int(elm) for elm in input[1]]

# algorithm

# difference set
difference_set = universal_set.difference(set(subset))

target = int(input[0][0])

while True:
    target_set = [int(x) for x in set(str(target))]
    if set(target_set) <= difference_set:
        result = target
        break
    else:
        target += 1

# ans
print('ans:', result)
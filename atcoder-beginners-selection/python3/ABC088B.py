from sys import stdin

# input
input = [stdin.readline().rstrip().split() for _ in range(2)]
target = [int(elm) for elm in input[1]]

# alogrithim
alice = []
bob = []
for index, elm in enumerate(sorted(target, reverse=True)):
    if 0 == (index + 1) % 2:
        bob.append(elm)
    else:
        alice.append(elm)

# ans
result = sum(alice) - sum(bob)
print('ans', result)
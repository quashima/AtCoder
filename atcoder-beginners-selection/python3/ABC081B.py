from sys import stdin

# input
input = [stdin.readline().rstrip().split() for _ in range(2)]
target = input[1]

count = 0
check = False

while True:
    # check Even or Odd
    for elm in target:
        if 0 != int(int(elm) % 2):
            check = True
            break

    if check == True:
        break

    # Divide by two
    for i, e in enumerate(target):
        target[i] = int(int(e) / 2)
    count += 1

# ans
print('ans', count)

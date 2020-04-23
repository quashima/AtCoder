from sys import stdin

# input
input = [stdin.readline().rstrip().split() for _ in range(1)]
target = int(input[0][0])

# algorithm
list = []
while target != 0:
    list.append(target % 10)
    target /= 10
list.reverse()

count = 0

for elm in list:
    if elm == 1:
        count+=1

# ans
print('ans', count)
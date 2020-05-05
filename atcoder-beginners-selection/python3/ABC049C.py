from sys import stdin

# input
input = [stdin.readline().rstrip().split() for _ in range(1)]
target = str(input[0][0])[::-1]

# algorithm
target = target.replace('remaerd', '')
target = target.replace('maerd', '')
target = target.replace('esare', '')
target = target.replace('resare', '')

if target.replace(' ', '') == '':
    print('YES')
else:
    print('NO')

from sys import stdin

# input
input = [stdin.readline().rstrip().split() for _ in range(1)]

# algorithm
def check():
    if len(input[0]) != 3:
        return 'No'

    targets = [int(elm) for elm in input[0]]
    if targets != [5, 5, 7]:
        return 'No'
    
    return 'Yes'

# ans
print(check())
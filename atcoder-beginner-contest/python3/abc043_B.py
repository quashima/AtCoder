# input
target = input()

# algorithm
result_list = []
for index, elm in enumerate(list(target)):
    if elm == 'B' and result_list:
        del result_list[index - 1]
    elif elm != 'B':
        result_list.append(elm)

# ans
print('ans:', ''.join(result_list))
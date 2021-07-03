array = []
max_num = 0
max_index = 0

for _ in range(9):
    array.append(int(input()))

for i in range(len(array)):
    if array[i] > max_num:
        max_num = array[i]
        max_index = i + 1

print(max_num)
print(max_index)

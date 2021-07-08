array = []
for _ in range(9):
    array.append(int(input()))

print(max(array))
print(array.index(max(array)) + 1)

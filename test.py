arr = [1, 2, 3, 4, 5, 6, 7, 8]
result = []
for i in range(0, len(arr), 3):
    result.append(arr[i:i+3])
print(result)
num = int(input())
result = list()

while num > 1:
    index = 0
    for i in range(2, num + 1):
        if num % i == 0:
            result.append(i)
            index = i
            break
    num = num // index
for j in result:
    print(j)

n, x = map(int, input().split())

array = list(map(int, input().split()))
result = list()

for i in array:
    if i < x:
        result.append(i)


for i in result:
    print(i, end=' ')


from sys import stdin
t = int(stdin.readline())
array = []
for _ in range(t):
    n = int(stdin.readline())
    array.append(n)

array.sort()
for i in array:
    print(i)

import sys
input = sys.stdin.readline
N = int(input())
result = list()
while N > 1:
    index = 0
    for i in range(2, N + 1):
        if N % i == 0:
            index = i
            result.append(i)
            break
    N //= index
for j in result:
    print(j)

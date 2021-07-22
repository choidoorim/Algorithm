"""
- BOJ 11047
- CDR
"""
from sys import stdin
n, k = map(int, stdin.readline().split())
array = []
for _ in range(n):
    array.append(int(stdin.readline()))

count = 0
for i in range(len(array) - 1, -1, -1):
    if array[i] - k <= 0:   # '화폐 종류 - 계산할 돈' 이 0과 같거나 음수일 때만 연산 수행
        count += k // array[i]
        k %= array[i]
    else:
        continue


print(count)

"""
- BOJ 11399
- CDR
- 최소 시간은 오름차순으로 정렬 후 시간을 합하는 것이다
"""
from sys import stdin
n = int(stdin.readline())
time = list(map(int, stdin.readline().split()))
time.sort()
result = []
for i in range(1, n + 1):
    num = 0
    for j in range(i):
        num += time[j]
    result.append(num)
print(sum(result))

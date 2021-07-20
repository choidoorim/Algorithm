"""
- BOJ 2161
- CDR
- deque
"""
from sys import stdin
from collections import deque

N = int(stdin.readline())
array = deque([i for i in range(1, N + 1)])
result = []
while len(array) > 1:
    result.append(array.popleft())
    array.append(array.popleft())

for i in result:
    print(i, end=' ')
print(array[0], end=' ')

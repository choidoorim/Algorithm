"""
- BOJ 2164
- CDR
"""
import sys
from collections import deque
n = int(sys.stdin.readline())

array = deque()
for i in range(1, n + 1):
    array.append(i)

while len(array) > 1:
    array.popleft()
    array.append(array.popleft())

print(array[0])

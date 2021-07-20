"""
- BOJ 1158
- CDR
- deque 의 rotate 를 활용한 문제
"""
from sys import stdin
from collections import deque
N, K = map(int, stdin.readline().split())

deq = deque()
result = []
for i in range(1, N + 1):
    deq.append(i)

while deq:
    deq.rotate(-(K - 1))
    result.append(deq.popleft())

print('<', end='')
for j in range(N):
    if j == len(result) - 1:
        print('{}>'.format(result[j]), end=' ')
    else:
        print('{},'.format(result[j]), end=' ')


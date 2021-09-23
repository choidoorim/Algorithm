"""
- BOJ 1158
- CDR
- deque 의 rotate 를 활용한 문제
"""
# from sys import stdin
# from collections import deque
# N, K = map(int, stdin.readline().split())
#
# deq = deque()
# result = []
# for i in range(1, N + 1):
#     deq.append(i)
#
# while deq:
#     deq.rotate(-(K - 1))
#     result.append(deq.popleft())
#
# print('<', end='')
# for j in range(N):
#     if j == len(result) - 1:
#         print('{}>'.format(result[j]), end=' ')
#     else:
#         print('{},'.format(result[j]), end=' ')

# 큐를 활용하지 않은 문제
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
array = [i for i in range(1, n + 1)]
result = []
j = 0
while array:
    j = (j + k - 1) % len(array)
    result.append(array[j])
    del array[j]

print('<', end='')
for j in range(n):
    if j == len(result) - 1:
        print('{}>'.format(result[j]), end=' ')
    else:
        print('{},'.format(result[j]), end=' ')

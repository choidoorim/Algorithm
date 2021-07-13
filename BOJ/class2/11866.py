"""
- BOJ 11866
- CDR
- 큐를 활용하여 푸는 문제로, deque 라는 collection 모듈을 사용하는게 좋다.
- rotate(-1) : 배열 내 왼쪽에서 1개의 값을 맨 마지막 배열로 옮겨 준다(회전 시킨다).
  rotate(2): 배열 내 오른쪽 2개의 값을 맨 처음 배열로 옮겨 준다(회전 시킨다).
"""
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
array = deque(i for i in range(1, n + 1))
result = []

while array:
    array.rotate(-(k - 1))     # 값의 개수만큼 배열을 회전시켜주는 메소드, '-' : 왼쪽 '+' : 오른쪽
    result.append(array.popleft())

print('<', end='')
for i in range(len(result)):
    if i == len(result) - 1:
        print('{}>'.format(result[i]))
    else:
        print('{},'.format(result[i]), end=' ')

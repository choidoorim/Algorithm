"""
- BOJ 1927
- CDR
- 시간초과 시 sys 모듈을 사용하자
"""
import heapq
import sys
input = sys.stdin.readline
n = int(input())
array = []

for _ in range(n):
    x = int(input())
    if x == 0:
        if not array:
            print(0)
        else:
            print(heapq.heappop(array))
    else:
        heapq.heappush(array, x)

"""
- BOJ, 11279
- 최대 힙
- '-' 로 변환하여 배열에 넣은 뒤 다시 * (-1) 을 통해 원래 값으로 가져온다.
- 힙은 우선순위가 높은 것부터 나간다 = 가장 수가 작은 것부터.
"""
import heapq
from sys import stdin
input = stdin.readline

t = int(input())
array = []
heapq.heapify(array)
for _ in range(t):
    x = int(input())
    if x == 0:
        if array:
            print(heapq.heappop(array)*(-1))
        else:
            print(0)
    else:
        heapq.heappush(array, -x)

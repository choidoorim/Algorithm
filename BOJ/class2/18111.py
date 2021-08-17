"""
- BOJ 18111
- CDR
- 높이는 256로 정해져있기 때문에 모든 높이를 다 체크해야 한다
"""
from collections import Counter

N, M, B = map(int, input().split())
land = []
for i in range(N):
    land += map(int, input().split())

land = dict(Counter(land))
height, min_sec = 0, int(1e9)

# for i in range(257):

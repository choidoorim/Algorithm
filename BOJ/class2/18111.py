"""
- BOJ 18111
- CDR
- 높이는 256로 정해져있기 때문에 모든 높이를 다 체크해야 한다
"""
from sys import stdin
from collections import Counter

n, m, b = map(int, stdin.readline().split())

land = []
for _ in range(n):
    land += map(int, stdin.readline().split())


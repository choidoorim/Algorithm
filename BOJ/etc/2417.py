"""
- BOJ 2417
- CDR
- math 모듈 ceil 함수를 사용하여 올림처리를 함
- ceil 올림, floor 내림, round 반올림
"""
from sys import stdin
import math
n = int(stdin.readline())

print(int(math.ceil(n ** 0.5)))

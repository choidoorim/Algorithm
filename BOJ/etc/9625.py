"""
- BOJ 9625
- CDR
-규칙을 파악해보면 피보나치와 동일한 것을 확인할 수 있다
 A 의 개수는 n - 2, B 의 개수는 n - 1
"""
from sys import stdin

n = int(stdin.readline())
d = [0] * 46
d[0] = 1
d[1] = 1
for i in range(2, n + 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n - 2], d[n - 1])

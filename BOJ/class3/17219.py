"""
- BOJ 17219
- CDR
- dic 사용
- https://wikidocs.net/16
"""
from sys import stdin
n, m = map(int, stdin.readline().split())
dic = dict()
for _ in range(n):
    key, value = map(str, stdin.readline().split())
    dic[key] = value

for _ in range(m):
    email = stdin.readline().rstrip()
    print(dic[email])

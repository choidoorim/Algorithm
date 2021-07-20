"""
- BOJ 9095
- CDR
- 다이나믹 프로그래밍
- 규칙을 파악해보면 F(n) = F(n - 1) + F(n - 2) + F(n - 3) 라는 점화식이 나온다
1 - 1개 : 1
2 - 2개 : (1, 1) , 2
3 - 4개: (1, 1, 1) , (1, 2) , (2, 1) , 3
4 - 7개: (1, 1, 1, 1), (1, 1, 2), (1, 2, 1), (2, 1, 1), (2, 2), (1, 3), (3, 1)
...
"""
from sys import stdin
T = int(stdin.readline())


def find_count(num):
    d = [0] * 11
    d[0] = 1
    d[1] = 2
    d[2] = 4
    for i in range(3, num):
        d[i] = d[i - 1] + d[i - 2] + d[i - 3]
    return d[num - 1]


for _ in range(T):
    n = int(stdin.readline())
    print(find_count(n))

"""
점화식 : Fn = Fn(i - 1) + Fn(i - 2) + Fn(i - 3)
"""
from sys import stdin
input = stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    dp = [0] * 12
    dp[1], dp[2], dp[3] = 1, 2, 4
    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    print(dp[n])

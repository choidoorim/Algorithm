from sys import stdin
input = stdin.readline
n = int(input())
price = [0] + [i for i in map(int, input().split())]
dp = [0] * (n + 1)

dp[1] = price[1]
for i in range(2, n + 1):
    for j in range(1, i + 1):
        if dp[i] < dp[i - j] + price[j]:    # 최대 값일 경우
            dp[i] = dp[i - j] + price[j]
print(dp[n])

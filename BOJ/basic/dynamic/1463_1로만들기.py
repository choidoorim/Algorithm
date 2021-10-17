import sys
input = sys.stdin.readline
x = int(input())
dp = [0] * (x + 1)
for i in range(2, x + 1):
    dp[i] = dp[i - 1] + 1
    # 2 와 3 으로 나눠지는 수가 있을 수도 있으니 둘다 if
    if i % 2 == 0:
        dp[i] = min(dp[i // 2] + 1, dp[i])
    if i % 3 == 0:
        dp[i] = min(dp[i // 3] + 1, dp[i])
print(dp[x])

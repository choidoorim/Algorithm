# 타일링 문제
def solution(N):
    dp = [0] * 45
    dp[1], dp[2] = 1, 2
    for i in range(3, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[N]


print(solution(4))

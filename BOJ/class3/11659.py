"""
- BOJ 11659
- CDR
- 누적 합
"""
# 시간초과 - 누적 합을 모르고 풀이를 진행하여 시간초과 발생
import sys
# n, m = map(int, sys.stdin.readline().split())
# num = list(map(int, sys.stdin.readline().split()))
# for _ in range(m):
#     a, b = map(int, sys.stdin.readline().split())
#     sum_num = 0
#     for i in range(a - 1, b):
#         sum_num += num[i]
#     print(sum_num)

n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
num_sum = [0] * (n + 1)
for i in range(1, n + 1):   # 누적 시킨 합을 저장
    num_sum[i] = num_sum[i - 1] + num[i - 1]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(num_sum[j] - num_sum[i - 1])

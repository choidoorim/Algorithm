"""
- BOJ 7568
- CDR
"""
import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
S = input().rstrip()

result = 0  # 결과 값
cnt = 0     # N 을 비교하기 위한 변수
i = 1
while i < M - 1:
    if S[i - 1] == 'I' and S[i] == 'O' and S[i + 1] == 'I':
        cnt += 1
        if cnt == N:
            result += 1
            cnt -= 1
        i += 1
    else:
        cnt = 0
    i += 1
print(result)

from sys import stdin
N = int(stdin.readline())

result = [0] * 1001
# 초기 값 설정
result[1] = 1
result[2] = 3

for i in range(3, N + 1):
    result[i] = (result[i - 1] + (result[i - 2] * 2)) % 796796

print(result[N])

"""
- BOJ 2747
- CDR
- 피보나치
- 재귀는 콜스택이 계속 차지만, for 문은 콜스택이 한번만 쌓이기 때문에 재귀를 피하는게 좋다
"""
from sys import stdin


# def fibo(num):
#     if num == 1 or num == 2:
#         return 1
#     return fibo(num - 1) + fibo(num - 2)


n = int(stdin.readline())
d = [0] * 46
d[1] = 1
d[2] = 1
for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])

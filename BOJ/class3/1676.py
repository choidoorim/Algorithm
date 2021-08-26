"""
- BOJ 1676
- CDR
- 팩토리얼을 재귀를 통해 계산 후 0의 갯수를 count 했지만 recursive error 발생,
따라서 math 모듈의 factorial method 사용
근데 규칙을 파악해보니 0의 개수는 숫자를 5로 나눴을 때의 몫이 0의 개수이다 : 참고 https://st-lab.tistory.com/165
5! = 120 -> 1개
10! = 3628800 -> 2개
15! = 3개...
"""
# Success 1
from sys import stdin
import math
N = int(stdin.readline())


# recursive error
# def factorial(num):
#     if num == 1:
#         return 1
#     return num * factorial(num - 1)


count = 0
n_factorial = str(math.factorial(N))
for i in range(len(n_factorial) - 1, -1, -1):
    if n_factorial[i] == '0':
        count += 1
    else:
        break

print(count)

# Success 2
# N = int(stdin.readline())
#
# count = 0
# while N >= 5:
#     count += N // 5
#     N //= 5
#
# print(count)

from itertools import combinations
from sys import stdin
input = stdin.readline


def GCD(num1, num2):    # 큰 수, 작은 수
    return num1 if num2 == 0 else GCD(num2, num1 % num2)


t = int(input())
for _ in range(t):
    case = list(map(int, input().split()))
    del case[0]
    case.sort(reverse=True)     # 역순으로 정렬
    result = 0
    for a, b in combinations(case, 2):
        result += GCD(a, b)     # 큰 수, 작은 수
    print(result)

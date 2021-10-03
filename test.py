"""
현재 자신의 위치와 동생들의 차이를 구한 뒤,
동생들의 차이 중 최대공약수를 구하면 된다.
"""
import sys
input = sys.stdin.readline


def GCD(num1, num2):    # 큰 수 와 작은 수
    if num2 == 0:
        return num1
    return GCD(num2, num1 % num2)


N, S = map(int, input().split())
location = list(map(int, input().split()))
diff = []
for i in location:
    diff.append(abs(i - S))

diff.sort()     # 큰 수, 작은 수 순서대로 최대공약수를 구하기 위해서 정렬
result = min(diff)

# 여러 개의 최대공약수를 구하기.
# [2, 4, 8] 의 최대 공약수는 2 - 2 의 최대공약수를 구한 뒤, 결과와 4의 최대 공약수를 구하고, 결과와 8의 최대 공약수를 구하면 된다.
for i in range(len(diff)):
    result = GCD(diff[i], result)

print(result)

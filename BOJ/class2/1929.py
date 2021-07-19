import sys


def is_prime(num):
    if num == 1:    # 1은 소수가 아니다
        return False
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True


m, n = map(int, sys.stdin.readline().split())

for j in range(m, n+1):
    if is_prime(j):
        print(j)

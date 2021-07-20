"""
- BOJ 1978
- CDR
- 소수는 2부터다.
"""


def is_prime(num):
    if num == 1:
        return False
    else:
        for j in range(2, int(num**0.5) + 1):
            if num % j == 0:
                return False
        return True


n = int(input())

array = list(map(int, input().split()))

count = 0
for i in array:
    if is_prime(i):
        count += 1

print(count)

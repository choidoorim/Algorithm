a, b = map(int, input().split())


def decimal(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


for j in range(a, b + 1):
    if decimal(j):
        print(j)

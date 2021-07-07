n, k = map(int, input().split())


def sequence(num):
    if num <= 1:
        return 1
    return num * sequence(num - 1)


print(sequence(n) // (sequence(k) * sequence(n - k)))

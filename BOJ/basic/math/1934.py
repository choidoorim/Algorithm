t = int(input())


def GCD(num1, num2):
    if num2 == 0:
        return num1
    return GCD(num2, num1 % num2)


for _ in range(t):
    a, b = map(int, input().split())
    gcd_result = GCD(b, a)
    print((a * b) // gcd_result)


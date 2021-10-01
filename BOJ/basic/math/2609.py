a, b = map(int, input().split())


def GCD(num1, num2):
    if num2 == 0:
        return num1
    return GCD(num2, num1 % num2)


gcd_result = GCD(a, b)
print(gcd_result)
print((a * b) // gcd_result)

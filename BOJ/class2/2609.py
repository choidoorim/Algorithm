# 유클리드 호제법
import sys
a, b = map(int, sys.stdin.readline().split())


def gcd(num1, num2):    # 최대공약수
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1 % num2)


gcd_result = int(gcd(a, b))
lcd_result = (a*b) // gcd_result    # 최소공배수  = (두 값 곱하기) / 최대공약수

print(gcd_result)
print(lcd_result)

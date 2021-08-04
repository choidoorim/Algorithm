"""
- Programmers - 부족한 금액 계산하기
- CDR
"""


def solution(price, money, count):
    for i in range(1, count + 1):
        money -= price * i

    if money >= 0:
        return 0
    else:
        return abs(money)


print(solution(100, 300, 4))

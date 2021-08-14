"""
- Programmers - 3 진법 뒤집기
- CDR
"""


def ternary(num):
    result = list()
    while num > 0:
        result.append(num % 3)
        num //= 3
    return result


def solution(n):
    answer = 0
    result = ternary(n)
    cnt = 0
    for i in range(len(result) - 1, -1, -1):
        answer += result[i] * (3**cnt)
        cnt += 1
    return answer


print(solution(125))

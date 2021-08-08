"""
- Programmers - 자리수 더하기
- CDR
"""


def solution(n):
    answer = 0
    while n > 0:
        answer += n % 10
        n //= 10

    return answer


print(solution(987))

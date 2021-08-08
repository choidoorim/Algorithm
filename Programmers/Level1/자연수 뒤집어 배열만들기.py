"""
- Programmers - 자연수 뒤집어 배열만들기
- CDR
"""


def solution_one(n):
    answer = []
    n = list(str(n))
    for i in range(len(n) - 1, -1, -1):
        answer.append(int(n[i]))
    return answer


def solution_two(n):
    answer = []
    while n > 0:
        b = n % 10
        n //= 10
        answer.append(b)
    return answer


print(solution_two(12345))

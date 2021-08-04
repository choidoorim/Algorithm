"""
- Programmers - x 만큼 간격이 있는 n 개의 숫자
- CDR
"""


def solution(x, n):
    answer = []
    result = 0
    for i in range(n):
        result += x
        answer.append(result)

    return answer


print(solution(2, 5))

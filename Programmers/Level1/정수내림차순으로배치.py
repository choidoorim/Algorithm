"""
- Programmers - 정수 내림차순으로 배치
- CDR
- 숫자를 list 형태로 만들기 - int(num) -> list(str(num))
"""


def solution(n):
    answer = ''
    n = list(str(n))
    n.sort(reverse=True)
    for i in n:
        answer += str(i)
    return int(answer)


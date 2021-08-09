"""
- Programmers - 문자열 내림차순으로 배치
- CDR
"""


def solution(s):
    s = list(s)
    s.sort(reverse=True)
    return "".join(s)

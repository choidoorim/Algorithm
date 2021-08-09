"""
- Programmers - 문자열다루기 기본
- CDR
"""


def solution(s):
    if (len(s) == 4 or len(s) == 6) and s.isdigit():
        return True
    else:
        return False


print(solution("a123"))

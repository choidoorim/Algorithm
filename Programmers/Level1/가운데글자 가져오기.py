"""
- Programmers - 가운데 글자 가져오기
- CDR
"""


def solution(s):
    mid = len(s) // 2
    return s[mid - 1] + s[mid] if len(s) % 2 == 0 else s[mid]

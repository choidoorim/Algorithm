"""
- Programmers - 최솟값 만들기
- CDR
- 공백 기준으로 숫자를 배열 형태로 만들어 준 후, 배열 내 최소 최대 값을 구했습니다.
"""


def solution(s):
    num = list(map(int, s.split(" ")))
    return str(min(num)) + ' ' + str(max(num))


print(solution("-1 -2 -3 -4"))

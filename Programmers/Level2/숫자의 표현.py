"""
- Programmers - 숫자의 표현
- CDR
- for 문 안에 while 문을 사용하여 연속 된 숫자 중 15 값이 될 수 있는 수를 찾았습니다.
"""


def solution(n):
    answer = 0
    for i in range(1, n + 1):
        start = i
        sum_num = 0
        while sum_num < n:
            sum_num += start
            start += 1
            if sum_num == n:
                answer += 1
    return answer


print(solution(15))

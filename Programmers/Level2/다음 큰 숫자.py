"""
- Programmers - 다음 큰 숫자
- CDR
- 입력 받은 숫자를 이진수로 변환하여 1의 개수를 찾고, for 문을 통해 입력받은 수 다음 부터 이진수의 개수를 체크하며 다음 수를 찾습니다.
"""


def solution(n):
    n_cnt = format(n, 'b').count('1')
    for i in range(n + 1, 1000001):
        if n_cnt == format(i, 'b').count('1'):
            return i


print(solution(78))

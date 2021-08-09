"""
- Programmers - 소수찾기
- CDR
- 소수 찾을 시 범위는 에라토네스의 체를 활용하자
"""


def find_num(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def solution(n):
    answer = 0
    for i in range(2, n + 1):
        if find_num(i):
            answer += 1
    return answer


print(solution(5))

"""
- Programmers - 문제번호가리기
- CDR
"""


def solution(phone_number):
    answer = ''
    for i in range(len(phone_number) - 4):
        answer += '*'
    answer += phone_number[-4:]     # 배열의 뒷자리 4개
    return answer

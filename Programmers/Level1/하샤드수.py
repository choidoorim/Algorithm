"""
- Programmers - 하샤드수
- CDR
"""


def solution(x):
    str_x = str(x)
    sum_num = 0
    for i in str_x:
        sum_num += int(i)

    if x % sum_num == 0:
        answer = True
    else:
        answer = False
    return answer

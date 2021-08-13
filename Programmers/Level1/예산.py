"""
- Programmers - 예산
- CDR
"""


def solution(d, budget):
    answer = 0
    d.sort()
    for money in d:
        budget -= money
        if budget < 0:
            break
        else:
            answer += 1
    return answer


print(solution([2,2,3,3], 10))

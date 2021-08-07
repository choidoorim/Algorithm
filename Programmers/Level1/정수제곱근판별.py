import math


def solution(n):
    answer = 0
    if math.sqrt(n) == int(math.sqrt(n)):
        answer = int(math.sqrt(n))
    else:
        return -1
    return (answer + 1) ** 2


print(solution(121))

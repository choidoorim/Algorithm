"""
- Programmers - k 번째 수
- CDR
"""


def solution(array, commands):
    answer = []
    for i, j, k in commands:
        new_array = array[i - 1: j]
        new_array.sort()
        answer.append(new_array[k - 1])
    return answer

# array = [1, 5, 2, 6, 3, 7, 4]
# command = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
# solution(array, command)

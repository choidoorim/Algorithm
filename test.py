def solution(array, commands):
    answer = []
    for i, j, k in commands:
        new_result = array[(i - 1):j]
        new_result.sort()
        answer.append(new_result[(k - 1)])
    return answer


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

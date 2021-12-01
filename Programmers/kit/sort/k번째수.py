def solution(array, commands):
    answer = []
    for command in commands:
        new_result = array[(command[0] - 1):command[1]]
        new_result.sort()
        answer.append(new_result[(command[2] - 1)])
    return answer
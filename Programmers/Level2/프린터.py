def solution_runtime_err(priorities, location):
    answer = 0
    dic = {}
    for i in range(len(priorities)):
        dic[i] = priorities[i]
    j = 0
    while True:
        if dic[j] == max(dic.values()):
            del(dic[j])
            answer += 1
            if j == location:
                break
        j += 1
        if j > len(priorities) - 1:
            j = 0
    return answer


def solution(priorities, location):
    # [1, 1, 9, 1, 1, 1]
    # [0, 1, 2, 3, 4, 5]
    # result : [2, 3, 4, 5, 0, 1]
    loc = [i for i in range(len(priorities))]
    result = []     # priorities 배열의 인덱스 값이 result 에 인쇄되는 순서로 저장
    while priorities:
        if priorities[0] == max(priorities):
            result.append(loc.pop(0))
            priorities.pop(0)
        else:   # 최댓값이 아닐경우 배열의 뒤로 이동
            priorities.append(priorities.pop(0))
            loc.append(loc.pop(0))
    return result.index(location) + 1


print(solution([1, 1, 9, 1, 1, 1], 0))

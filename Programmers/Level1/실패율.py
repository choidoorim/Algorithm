def find_clear_num(n, array):
    cnt = 0
    for arr in array:
        if arr >= n:
            cnt += 1
    return cnt


def solution(N, stages):
    answer = []
    result = []
    clear_num = len(stages)
    for i in range(1, N + 1):
        a = stages.count(i)
        if a == 0:
            percent = 0
        else:
            percent = a / clear_num
        result.append((percent, i))
        clear_num -= a   # 도달한 플레이어 수는 이중 포문을 통해 찾는 것이 아닌, '현재 스테이지를 클리어 한 사람의 수 - 클리어 하지 못한 사람의 수' 를 반복해서 찾을 수 있다.
    result.sort(key=lambda x:x[0], reverse=True)
    for res in result:
        answer.append(res[1])
    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))

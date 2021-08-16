def score(num):
    if num >= 6:
        return 1
    elif num == 5:
        return 2
    elif num == 4:
        return 3
    elif num == 3:
        return 4
    elif num == 2:
        return 5
    else:
        return 6


def solution(lottos, win_nums):
    unknown_num = lottos.count(0)
    highest, lowest = 0, 0
    for num in win_nums:
        if num in lottos:
            highest += 1
            lowest += 1
    answer = [score(highest + unknown_num), score(lowest)]
    return answer


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))

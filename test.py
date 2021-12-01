def solution(progresses, speeds):
    answer = []
    days = 1
    cnt = 0
    while progresses:
        ## 첫번째 작업이 끝나야 뒤에 작업들이 끝날 수 있기에 첫번째 배열을 통해 로직 구성.
        if progresses[0] + (speeds[0] * days) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        else:
            days += 1
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
    answer.append(cnt)
    return answer


print(solution([93, 30, 55], [1, 30, 5]))

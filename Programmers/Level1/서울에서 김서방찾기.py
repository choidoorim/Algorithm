def solution(seoul):
    answer = ''
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            answer = '김서방은 %s에 있다.' % i
    return answer


print(solution(["Jane", "Kim"]))

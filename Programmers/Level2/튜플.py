def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split('},{')
    s.sort(key=len)     # 배열의 길이를 기준으로 s 배열을 정렬한다.
    for i in s:
        num = list(map(int, i.split(',')))
        for j in num:
            if j not in answer:
                answer.append(j)
    return answer


print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))


def solution(answers):
    answer = []
    cnt_one = 0
    cnt_two = 0
    cnt_three = 0
    one_rule = [1, 2, 3, 4, 5]
    two_rule = [2, 1, 2, 3, 2, 4, 2, 5]
    three_rule = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answers)):
        # array(i % len(array)) : 위의 규칙들을 반복
        if answers[i] == one_rule[i % len(one_rule)]:   # 첫 번째 사람의 정답이 같을 경우
            cnt_one += 1
        if answers[i] == two_rule[i % len(two_rule)]:   # 두 번째 사람의 정답이 같을 경우
            cnt_two += 1
        if answers[i] == three_rule[i % len(three_rule)]:   # 세 번째 사람의 정답이 같을 경우
            cnt_three += 1
    score = [cnt_one, cnt_two, cnt_three]
    for j in range(len(score)):
        if score[j] == max(score):
            answer.append(j + 1)
    return answer


print(solution([1,2,3,4,5]))

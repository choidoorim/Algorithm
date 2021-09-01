def solution(skill, skill_trees):
    answer = 0
    for sk in skill_trees:
        result = []     # skill tree 중 skill 규칙에 있는 것을 찾는 결과
        success_status = True
        for s in sk:
            if s in skill:
                result.append(s)
        for i in range(len(result)):    # skill 과 skill trees 순서가 같은지 확인
            if skill[i] != result[i]:
                success_status = False
                break
        if success_status:
            answer += 1
    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))

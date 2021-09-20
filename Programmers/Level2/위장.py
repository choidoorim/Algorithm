def solution(clothes):
    answer = 1
    dic = dict()
    for cloth in clothes:
        if cloth[1] in dic.keys():
            dic[cloth[1]] += 1
        else:
            dic[cloth[1]] = 1
    for i in dic.values():
        answer *= (i + 1)
    return answer - 1


print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))

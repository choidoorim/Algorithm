def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = [0] * bridge_length
    # 초마다 다리의 길이중 1칸씩 건널 수 있다.
    while q:
        answer += 1
        q.pop(0)
        # [0, 7] -> [7, 0] -> [0, 4] .. 다리가 버틸 수 있는 무게를 체크하고 초마다 한칸씩 pop하여 이동
        if truck_weights:
            if weight >= sum(q) + truck_weights[0]:
                q.append(truck_weights.pop(0))
            else:
                q.append(0)
    return answer


# 2개가 올라갈 수 있고 무게를 10kg 까지 견디는 다리
print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))

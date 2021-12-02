def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_in = [0] * bridge_length
    while bridge_in:
        answer += 1
        bridge_in.pop(0)
        if truck_weights:
            if sum(bridge_in) + truck_weights[0] <= weight:
                bridge_in.append(truck_weights.pop(0))
            else:
                bridge_in.append(0)
    return answer


print(solution(100, 100, [10]))

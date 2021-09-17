from collections import deque


def solution(numbers, target):
    answer = 0
    q = deque()
    n = len(numbers)
    # 계산할 수, 인덱스 값
    q.append([numbers[0], 0])       # +
    q.append([-1*numbers[0], 0])    # -
    while q:
        temp, idx = q.popleft()
        idx += 1        # 인덱스 증가
        if idx < n:
            q.append([temp + numbers[idx], idx])    # 현재 위치 + 다음 위치의 값
            q.append([temp - numbers[idx], idx])    # 현재 위치 - 다음 위치의 값
        else:
            if temp == target:
                answer += 1
    return answer


print(solution([1, 1, 1, 1, 1], 3))

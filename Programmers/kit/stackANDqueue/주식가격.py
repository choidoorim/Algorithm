from collections import deque


def solution(prices):
    answer = []
    q = deque(prices)
    while q:
        price = q.popleft()
        sec = 0
        for i in q:
            sec += 1
            if price > i:   # 만약 현재 가격이 이후 가격들보다 떨어질 경우
                break
        answer.append(sec)
    return answer


print(solution([1, 2, 3, 2, 3]))

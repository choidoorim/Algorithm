import heapq


def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)
    while scoville[0] < K and len(scoville) > 1:    # scovile 배열이
        num1 = heapq.heappop(scoville)
        num2 = heapq.heappop(scoville)
        heapq.heappush(scoville, num1 + (num2 * 2))
        count += 1
    return count if scoville[0] >= K else -1


print(solution([1, 2, 3, 9, 10, 12], 7))

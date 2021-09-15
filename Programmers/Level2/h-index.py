def solution(citations):
    citations.sort()
    length = len(citations)     # 논문의 수
    for i in range(length):
        if citations[i] >= length - i:      # 인용된 논문
            return length - i
    return 0


print(solution([3, 0, 6, 1, 5]))

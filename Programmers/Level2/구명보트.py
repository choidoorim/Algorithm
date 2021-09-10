def solution(people, limit):
    cnt = 0
    people.sort()       # 정렬
    start, end = 0, len(people) - 1
    # 제일 작은 수와 제일 큰수를 차례대로 비교
    while start <= end:
        # 두명을 태울 수 있을 경우 start + 1
        if (people[start] + people[end]) <= limit:
            start += 1
        end -= 1
        cnt += 1
    return cnt


print(solution([70, 50, 80, 50], 100))

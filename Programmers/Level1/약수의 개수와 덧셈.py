def find_measure_count(num):
    cnt = 0
    for i in range(1, num + 1):
        if num % i == 0:
            cnt += 1
    return cnt


def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if find_measure_count(i) % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer


print(solution(13, 17))

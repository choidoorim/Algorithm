from itertools import combinations


def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


# itertools 의 combinations 모듈을 활용해 배열 내에서 중복이 제거 된 n 개의 배열을 만들수 있다.
def solution(nums):
    answer = 0
    array = combinations(nums, 3)
    for i, j, k in array:
        if is_prime(i + j + k):
            answer += 1
    return answer


print(solution([1,2,7,6,4]))

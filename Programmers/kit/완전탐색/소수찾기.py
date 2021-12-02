from itertools import permutations


def is_prime(num):
    if num == 0 or num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    answer = []
    number = []
    for i in range(1, len(numbers) + 1):    # 1 ~ numbers 의 길이까지
        array = set(permutations(numbers, i))
        for j in array:
            number.append(int(''.join(j)))
    for num in number:
        if is_prime(num):
            answer.append(num)
    answer = set(answer)
    return len(answer)


print(solution("011"))
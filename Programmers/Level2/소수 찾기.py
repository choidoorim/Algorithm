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
    # i 가 1 ~ numbers 의 길이까지 랜덤인 배열을 만들어준다.
    for i in range(1, len(numbers) + 1):
        array = list(set(permutations(numbers, i)))
        # 배열 안에 숫자들을 조합하여 소수인지 판별한다.
        for j in array:
            num = int(''.join(list(j)))
            if is_prime(num) and num not in answer:
                answer.append(num)
    return len(answer)


# print(solution("17"))
print(solution("011"))

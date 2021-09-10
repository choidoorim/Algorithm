def solution(n):
    ans = 0

    while n > 0:
        # 2로 나눈 나머지가 0 일 경우에는 숫자를 나누고, 아닐 경우에는 -1씩 진행
        if n % 2 == 0:
            n //= 2
        elif n % 2 != 0:
            ans += 1
            n -= 1
    return ans


print(solution(5))

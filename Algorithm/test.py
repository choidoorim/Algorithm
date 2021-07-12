num = int(input())


def find(numb):
    if numb < 1:   # 1보다 큰 자연수가 소수이다.
        return False
    for i in range(2, numb):
        if numb % i == 0:   # 나머지가 0인 것이 있을 경우
            return False
    return True


print(find(num))
